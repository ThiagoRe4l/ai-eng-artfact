from typing import Literal

from pydantic import BaseModel, Field

CategoryName = Literal[
    "Guitarras",
    "Baixos",
    "Baterias e Percussão",
    "Teclados e Pianos",
    "Violões",
    "Instrumentos de Sopro (Madeiras)",
    "Instrumentos de Sopro (Metais)",
    "Cordas Orquestrais",
    "Ukuleles",
]


class SearchProductsInput(BaseModel):
    term: str | None = Field(
        default=None,
        description=(
            "Palavras-chave buscadas no nome, descrição e especificações do produto. "
            "A busca é literal, então inclua sinônimos e variações separados por espaço: "
            "para iniciante, use 'iniciante estudante começando'; "
            "para eletroacústico, 'eletroacústico elétrico captação'. Também aceita marca e modelo (ex.: 'Yamaha F310'). "
            "Basta o produto ter uma das palavras; quem tem mais aparece primeiro."
        ),
    )
    
    category: CategoryName | None = Field(default=None, description="Categoria exata do catálogo.")
    min_price: float | None = Field(default=None, ge=0, description="Preço final mínimo em reais.")
    max_price: float | None = Field(
        default=None, ge=0, description="Preço final máximo em reais, já considerando promoção ativa."
    )

    on_promotion: bool = Field(default=False, description="True para trazer só produtos com promoção ativa.")
    sort: Literal["relevance", "price_asc", "price_desc"] = Field(
        default="relevance",
        description="Ordenação. Use 'price_desc' para os mais caros ou topo de linha e 'price_asc' para os mais baratos.",
    )

class SearchPoliciesInput(BaseModel):
    question: str = Field(
        description="Dúvida do cliente reescrita de forma objetiva, ex.: 'prazo para troca por defeito', 'parcelamento em 10x parcela mínima'."
    )

class GetOrderStatusInput(BaseModel):
    order_id: int = Field(description="Número do pedido informado pelo cliente.")
    email_or_phone: str = Field(
        description="E-mail ou telefone informado pelo cliente nesta conversa, para confirmar a identidade."
    )

class InputClassification(BaseModel):
    category: Literal["in_scope", "out_of_scope", "injection_or_abuse"]
    reason: str = Field(description="Justificativa curta, em uma frase.")