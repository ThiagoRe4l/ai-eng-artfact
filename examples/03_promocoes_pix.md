# Example 3: expired promotion and PIX price

Two discount questions in the same conversation, one about an **inactive** promotion and one about an **active** promotion, both answered with data from the `search_products` tool.

**What this example shows**
- Takamine GD20 (id 95): the promotion exists in the data but is inactive. The agent says it no longer applies and gives the current price and the PIX price (5% off).
- Crafter HT-100 (id 90): an active 18% promotion, presented with the original price, discount percentage and final price (prompt rule 3).
- The 5% PIX discount does not stack with promotions: the agent says the PIX price stays at R$ 1,967.18 instead of applying a second discount.
- All amounts come precomputed from the tool (calculated in code, not by the model).

_The conversation below is in Brazilian Portuguese, the language of the store's customers. Agent answers are unedited._

---

**Cliente:** o Takamine GD20 ainda está em promoção?

**Assistente:** Oi! Aqui é o assistente virtual da **Empório da Música**, sua loja de instrumentos musicais em Campo Grande (MS). 🎶

**Assistente:** No momento, o Takamine GD20 Dreadnought Natural não está em promoção. 

O preço atual dele é R$ 2.199,00 (ou R$ 2.089,05 no PIX, com o desconto de 5% de pagamento à vista). Temos 5 unidades disponíveis em estoque!

Posso te ajudar com mais alguma dúvida ou com outro modelo?

**Cliente:** e o Crafter HT-100, quanto fica no pix?

**Assistente:** O Crafter HT-100 Folk Aço Natural está com uma promoção ativa ("Desconto Exclusivo"):

- **Preço original:** R$ 2.399,00
- **Desconto:** 18%
- **Preço final (inclusive no PIX):** R$ 1.967,18

Como os descontos não são cumulativos, o valor no PIX fica o mesmo valor promocional de R$ 1.967,18. Temos 3 unidades em estoque.

Posso te ajudar com mais alguma coisa?
