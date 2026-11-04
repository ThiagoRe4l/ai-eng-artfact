# Example 2: order status with identity verification and a late delivery

An order lookup (`get_order_status`), which only works with the order number **and** a second piece of the owner's data.

**What this example shows**
- The agent does not look up the order with the number alone: it asks for the registered email or phone before calling the tool.
- Identity verification: the phone typed as `99654-7821` matches the record `(67) 99654-7821` (the tool compares the last 9 digits, ignoring formatting and area code).
- Delay: the order is `shipped` with an estimated delivery of 02/28/2026. The agent compares the estimate with the current date, says it has passed and refers the customer to the store's WhatsApp, without inventing the shipment status.
- The customer's name comes from the record (first name only), after the identity is confirmed.

_The conversation below is in Brazilian Portuguese, the language of the store's customers. Agent answers are unedited._

---

**Cliente:** quero saber do meu pedido 8

**Assistente:** Oi! Aqui é o assistente virtual da **Empório da Música**, sua loja de instrumentos musicais em Campo Grande (MS). 🎶

**Assistente:** Para consultar o seu pedido, preciso também do e-mail ou telefone cadastrado na sua conta. Pode me informar?

**Cliente:** meu telefone é 99654-7821

**Assistente:** Encontrei seu pedido nº 8, Ana!

- **Produto:** 1x Ukulele Kala KA-C Concert Mogno
- **Status:** Enviado
- **Código de rastreio:** BRJL5544332BR
- **Previsão de entrega original:** 28/02/2026

Como a previsão de entrega já passou, recomendo entrar em contato com a nossa equipe diretamente pelo WhatsApp no **(67) 3321-4500** para que possamos verificar o andamento do transporte para você.

Posso te ajudar em mais alguma coisa?
