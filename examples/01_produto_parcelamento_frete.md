# Example 1: product + installments + shipping

A question that needs both data sources in the same answer: the catalog (`search_products`) and the policy manual (`search_policies`).

**What this example shows**
- Price and PIX price come from the products tool (computed in code, not by the model).
- The minimum installment rule (section 3.1): 10x of R$ 59.99 is below the R$ 100.00 minimum for 7x to 12x, so the agent declines and offers the maximum possible (6x of R$ 99.98; the minimum for 4x to 6x is R$ 80.00).
- Delivery times outside the metropolitan area (section 5.2), without inventing the shipping cost.

_The conversation below is in Brazilian Portuguese, the language of the store's customers. Agent answers are unedited._

---

**Cliente:** quanto fica o Yamaha C40 em 10x e qual o prazo de entrega para Dourados?

**Assistente:** O **Yamaha C40 Nylon Natural** está de R$ 599,90 (ou R$ 569,90 no PIX com 5% de desconto).

Sobre o parcelamento e o frete para Dourados:

* **Parcelamento:** Para parcelar entre 7x e 12x sem juros, a parcela mínima da loja é de R$ 100,00. Como o valor do violão é R$ 599,90, não é possível fazer em 10x. O parcelamento máximo para esse valor é em **até 6x de R$ 99,98 sem juros**.
* **Prazo de entrega para Dourados:**
  * **SEDEX:** 2 a 5 dias úteis
  * **Jadlog:** 3 a 8 dias úteis
  * **PAC:** 5 a 12 dias úteis

O valor exato do frete é calculado com o seu CEP na finalização da compra.

Posso te ajudar com mais alguma dúvida ou cálculo?
