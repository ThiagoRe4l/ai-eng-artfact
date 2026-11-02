import json

from src.tools import search_products


def search(**kwargs) -> dict:
    return json.loads(search_products.invoke(kwargs))


def find(product_id: int) -> dict | None:
    """Busca o produto pelo nome exato para garantir que ele esteja nos resultados."""
    from src.db import query

    name = query("SELECT name FROM products WHERE product_id = ?", (product_id,))[0]["name"]
    for product in search(term=name)["results"]:
        if product["product_id"] == product_id:
            return product
    return None


def ids(data: dict) -> list[int]:
    return [p["product_id"] for p in data["results"]]


def test_search_without_accent_finds_accented_text():
    # O id 81 tem "Violão" só na descrição; o termo vem sem acento.
    assert 81 in ids(search(term="violao"))


def test_search_is_case_insensitive():
    assert ids(search(term="VIOLAO")) == ids(search(term="violão"))


def test_max_price_uses_promotional_price():
    # Crafter HT-100 (id 90): R$ 2.399 com 18% de desconto = R$ 1.967,18.
    data = search(term="Crafter HT-100", max_price=2000)
    assert ids(data) == [90]
    assert data["results"][0]["final_price"] == 1967.18


def test_max_price_excludes_when_promotional_price_is_above():
    assert search(term="Crafter HT-100", max_price=1900)["results"] == []


def test_promoted_product_has_no_pix_price():
    product = find(90)
    assert product is not None
    assert "pix_price" not in product
    assert product["active_promotion"]["discount_percent"] == 18
    assert product["price"] == 2399


def test_product_without_promotion_has_pix_price():
    # Yamaha F310 (id 87): R$ 699,90 -> PIX 5% = R$ 664,905 -> 664.9 (arredondado).
    product = find(87)
    assert product is not None
    assert "active_promotion" not in product
    assert product["pix_price"] == round(699.9 * 0.95, 2)


def test_inactive_promotion_is_not_shown():
    # Takamine GD20 (id 95) tem promoção inativa: preço cheio e sem promoção.
    product = find(95)
    assert product is not None
    assert "active_promotion" not in product
    assert product["final_price"] == product["price"] == 2199
    assert "pix_price" in product


def test_the_four_active_promotions_are_flagged():
    for pid in (90, 94, 121, 127):
        product = find(pid)
        assert product is not None and "active_promotion" in product, pid


def test_availability_labels_and_stock_quantity():
    expected = {
        96: "sem estoque",
        113: "descontinuado",
        136: "descontinuado",
        130: "em breve",
        87: "disponível",
    }
    for pid, label in expected.items():
        product = find(pid)
        assert product is not None, pid
        assert product["availability"] == label, pid
        if label == "disponível":
            assert product["stock_quantity"] > 0
        else:
            assert "stock_quantity" not in product, pid


def test_no_results_returns_friendly_message():
    data = search(term="saxofone")
    assert data["results"] == []
    assert "Nenhum produto encontrado" in data["message"]


def test_never_more_than_eight_results():
    data = search(term="violão guitarra baixo teclado bateria ukulele")
    assert data["total_found"] > 8
    assert len(data["results"]) == 8


def test_category_filter():
    data = search(category="Ukuleles")
    assert data["results"]
    assert {p["category"] for p in data["results"]} == {"Ukuleles"}


def test_empty_category_returns_nothing():
    # Categorias de sopro não têm produtos no catálogo.
    assert search(category="Instrumentos de Sopro (Madeiras)")["results"] == []
