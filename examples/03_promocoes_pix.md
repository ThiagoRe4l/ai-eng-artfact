# Exemplo 3: promoção encerrada e preço no PIX

Duas perguntas sobre desconto na mesma conversa, uma com promoção **inativa** e outra com promoção **ativa**, ambas respondidas com dados da tool `search_products`.

**O que este exemplo mostra**
- Takamine GD20 (id 95): a promoção existe nos dados, mas está inativa. O agente diz que ela não vale mais, informa o preço atual e o preço no PIX (5%).
- Crafter HT-100 (id 90): promoção ativa de 18%. A promoção é apresentada com preço original, percentual e preço final (regra 3 do prompt).
- O desconto de 5% do PIX não é cumulativo com promoção: o agente informa que no PIX o valor continua R$ 1.967,18, em vez de aplicar um segundo desconto.
- Todos os valores vêm prontos da tool (calculados em código, não pelo modelo).

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
