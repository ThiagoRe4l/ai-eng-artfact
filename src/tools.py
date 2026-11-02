import json
import unicodedata

from langchain_core.tools import tool

from src.db import query
from src.schemas import SearchProductsInput, SearchPoliciesInput, GetOrderStatusInput
from src.rag import retrieve_policies

MAX_RESULTS = 8
PIX_DISCOUNT_PERCENT = 5
AVAILABILITY_ORDER = {"disponível": 0, "sem estoque": 1, "em breve": 2, "descontinuado": 3}

ORDER_STATUS = {
    "pending": "aguardando confirmação do pagamento",
    "confirmed": "pagamento confirmado, em preparação para envio",
    "shipped": "enviado",
    "delivered": "entregue",
    "cancelled": "cancelado",
}
ORDER_NOT_FOUND = (
    "Não encontrei um pedido com esses dados. Confira o número do pedido "
    "e o e-mail ou telefone cadastrado."
)

def _digits(text: str) -> str:
    return "".join(ch for ch in text if ch.isdigit())


def _identity_matches(email_or_phone: str, email: str, phone: str) -> bool:
    value = email_or_phone.strip().lower()
    if "@" in value:
        return value == email.lower()
    digits = _digits(value)  # Aceita com ou sem código de área/formatação
    return len(digits) >= 9 and digits[-9:] == _digits(phone)[-9:]


def _payment_label(method: str) -> str:
    if method.startswith("credit_"):
        return f"cartão de crédito em {method.removeprefix('credit_')}"
    return {"pix": "PIX", "debit": "cartão de débito", "boleto": "boleto bancário"}.get(method, method)

def _normalize(text: str) -> str:
    """Acentos minúsculos e listrados para que 'violao' combine com 'Violão'."""
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def _availability(status: str, stock: int) -> str:
    if status == "discontinued":
        return "descontinuado"
    if status == "coming_soon":
        return "em breve"
    if stock <= 0:
        return "sem estoque"
    return "disponível"


@tool(args_schema=SearchProductsInput)
def search_products(
    term: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> str:
    """Busca instrumentos no catálogo com preço, promoção ativa e disponibilidade atualizados.

    Use sempre que o cliente perguntar por produtos, preços, estoque ou promoções, ou pedir
    recomendação. Se não encontrar nada, tente de novo com menos filtros ou outras palavras.
    """
    sql = """
        SELECT p.product_id, p.name, c.name AS category, p.price_brl, p.stock_quantity,
               p.status, p.description, p.specs,
               pr.discount_percent, pr.description AS promotion_name
        FROM products p
        JOIN categories c ON c.category_id = p.category_id
        LEFT JOIN promotions pr ON pr.product_id = p.product_id AND pr.is_active = 1
    """
    params: tuple = ()
    if category:
        sql += " WHERE c.name = ?"
        params = (category,)

    words = _normalize(term).split() if term else []
    results = []
    for row in query(sql, params):
        score = 0
        if words:
            haystack = _normalize(f"{row['name']} {row['description']} {row['specs']}")
            score = sum(word in haystack for word in words)
            if score == 0:
                continue

        price = row["price_brl"]
        discount = row["discount_percent"]
        final_price = round(price * (1 - discount / 100), 2) if discount else price
        if min_price is not None and final_price < min_price:
            continue
        if max_price is not None and final_price > max_price:
            continue

        availability = _availability(row["status"], row["stock_quantity"])
        product = {
            "product_id": row["product_id"],
            "name": row["name"],
            "category": row["category"],
            "availability": availability,
            "price": price,
            "final_price": final_price,
            "description": row["description"],
            "specs": json.loads(row["specs"]),
        }
        if availability == "disponível":
            product["stock_quantity"] = row["stock_quantity"]
        if discount:
            product["active_promotion"] = {"name": row["promotion_name"], "discount_percent": discount}
        else:
            product["pix_price"] = round(price * (1 - PIX_DISCOUNT_PERCENT / 100), 2)
        results.append((score, product))

    if not results:
        return json.dumps(
            {"results": [], "message": "Nenhum produto encontrado. Tente com menos filtros ou outras palavras."},
            ensure_ascii=False,
        )

    results.sort(key=lambda r: (-r[0], AVAILABILITY_ORDER[r[1]["availability"]], r[1]["final_price"]))
    return json.dumps(
        {"total_found": len(results), "results": [p for _, p in results[:MAX_RESULTS]]},
        ensure_ascii=False,
    )

@tool(args_schema=SearchPoliciesInput)
def search_policies(question: str) -> str:
    """Consulta o manual de políticas da loja: pagamento e parcelamento, trocas e devoluções, frete e prazos de entrega, garantia, regras de promoções, horário, contato e privacidade.

    Use para dúvidas sobre regras e condições. Não use para preço, estoque ou status de pedido.
    """
    docs = retrieve_policies(question)
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

@tool(args_schema=GetOrderStatusInput)
def get_order_status(order_id: int, email_or_phone: str) -> str:
    """Consulta o status de um pedido. Exige o número do pedido e o e-mail ou telefone
    cadastrado, para confirmar que quem pergunta é o titular.

    Se o cliente ainda não informou os dois dados, peça antes de chamar.
    Nunca use dados que o cliente não forneceu.
    """
    rows = query(
        """
        SELECT o.order_id, o.order_date, o.status, o.payment_method, o.tracking_code,
               o.estimated_delivery, o.notes, c.name, c.email, c.phone
        FROM orders o
        JOIN customers c ON c.customer_id = o.customer_id
        WHERE o.order_id = ?
        """,
        (order_id,),
    )
    # A resposta é a mesma para "o pedido não existe" e "a identidade não corresponde": não há vazamento de dados.
    if not rows or not _identity_matches(email_or_phone, rows[0]["email"], rows[0]["phone"]):
        return json.dumps({"found": False, "message": ORDER_NOT_FOUND}, ensure_ascii=False)

    order = rows[0]
    items = query(
        """
        SELECT p.name, oi.quantity
        FROM order_items oi
        JOIN products p ON p.product_id = oi.product_id
        WHERE oi.order_id = ?
        """,
        (order_id,),
    )
    result = {
        "found": True,
        "order_id": order["order_id"],
        "customer_first_name": order["name"].split()[0],
        "order_date": order["order_date"],
        "status": ORDER_STATUS.get(order["status"], order["status"]),
        "payment_method": _payment_label(order["payment_method"]),
        "items": [{"product": i["name"], "quantity": i["quantity"]} for i in items],
    }
    if order["tracking_code"]:
        result["tracking_code"] = order["tracking_code"]
    if order["estimated_delivery"]:
        result["estimated_delivery"] = order["estimated_delivery"]
    if order["notes"]:
        result["notes"] = order["notes"]
    return json.dumps(result, ensure_ascii=False)