import json
import unicodedata

from langchain_core.tools import tool

from src.db import query
from src.schemas import SearchProductsInput

MAX_RESULTS = 8
PIX_DISCOUNT_PERCENT = 5
AVAILABILITY_ORDER = {"disponível": 0, "sem estoque": 1, "em breve": 2, "descontinuado": 3}


def _normalize(text: str) -> str:
    """Lowercase and strip accents so 'violao' matches 'Violão'."""
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