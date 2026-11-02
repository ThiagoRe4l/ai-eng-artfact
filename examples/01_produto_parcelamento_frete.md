# Exemplo 1: produto + parcelamento + frete

Pergunta que exige as duas fontes de dados na mesma resposta: o catálogo (`search_products`) e o manual de políticas (`search_policies`).

**O que este exemplo mostra**
- Preço e preço no PIX vindos da tool de produtos (calculados em código, não pelo modelo).
- Aplicação da regra de parcela mínima (seção 3.1): 10x de R$ 59,99 fica abaixo do mínimo de R$ 100,00 para 7x a 12x, então o agente recusa e informa o máximo possível (6x de R$ 99,98, mínimo de R$ 80,00 para 4x a 6x).
- Prazos de entrega para fora da região metropolitana (seção 5.2), sem inventar o valor do frete.

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
