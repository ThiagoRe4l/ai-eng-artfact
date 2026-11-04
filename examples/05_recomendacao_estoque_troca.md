# Example 5: recommendation, out-of-stock product and return policy

A three-question conversation that uses both data sources: the catalog (`search_products`) and the policy manual (`search_policies`).

**What this example shows**
- Budget-based recommendation: the agent searches beginner guitars under R$ 700.00 (final price, promotions included) and shows each one's price and PIX price.
- Out-of-stock product: the Giannini GF-3D is `active` with zero stock. The agent says it is unavailable, keeps the price and suggests an available alternative from the same brand within budget.
- Return for defects: the agent decides on its own to consult the manual (section 4.2) and answers with the 30-calendar-day window, the manufacturer's warranty after that, and what is not covered. It also mentions the 7-day withdrawal right (section 4.1) for online purchases.

_The conversation below is in Brazilian Portuguese, the language of the store's customers. Agent answers are unedited._

---

**Cliente:** quero um violão pra começar, até uns 700 reais

**Assistente:** Oi! Aqui é o assistente virtual da **Empório da Música**, sua loja de instrumentos musicais em Campo Grande (MS). 🎶

**Assistente:** Temos ótimas opções de violões até R$ 700,00, ideais para quem está começando:

**Opções com cordas de nylon (mais macias para os dedos de quem está aprendendo):**
- **Tagima Memphis AC-39 Nylon**: R$ 429,90 (ou R$ 408,40 no PIX) — leve, confortável e com ótimo custo-benefício.
- **Rozini RC-104 Nylon Estudante**: R$ 459,90 (ou R$ 436,90 no PIX) — acabamento caprichado e madeiras nacionais.
- **Yamaha C40 Nylon**: R$ 599,90 (ou R$ 569,90 no PIX) — um dos modelos mais recomendados por professores pelo excelente equilíbrio e projeção.

**Opção com cordas de aço (som mais brilhante e encorpado):**
- **Yamaha F310 Aço**: R$ 699,90 (ou R$ 664,90 no PIX) — violão folk super tradicional e resistente.

Você tem preferência por nylon ou aço? Se quiser mais detalhes de algum deles, é só avisar! Posso te ajudar em mais alguma coisa?

**Cliente:** e o Giannini GF-3D?

**Assistente:** O Giannini GF-3D Dreadnought Sunburst custa R$ 799,90, mas no momento ele está temporariamente indisponível em nosso estoque.

Uma excelente alternativa equivalente e disponível da mesma marca é o **Giannini GF-1R Aço Folk Sunburst**:
- Preço: R$ 579,90 (ou R$ 550,90 no PIX)
- Também possui cordas de aço, estilo folk e o lindo acabamento Sunburst, além de ficar confortavelmente dentro do seu orçamento de R$ 700,00.

Quer saber mais sobre o GF-1R ou posso te ajudar com mais alguma coisa?

**Cliente:** se vier com defeito, posso trocar?

**Assistente:** Sim! Se o produto apresentar qualquer defeito de fabricação, você pode solicitar a troca diretamente com a loja em até **30 dias corridos** após a compra. 

Após esse prazo de 30 dias, a garantia é tratada com o próprio fabricante, mas nós também podemos te ajudar intermediando esse processo se precisar. Apenas lembrando que defeitos causados por mau uso, quedas ou exposição à umidade não são cobertos.

Além disso, para compras online, você também tem até 7 dias corridos após o recebimento para trocar ou devolver por arrependimento.

Posso te ajudar em mais alguma dúvida?
