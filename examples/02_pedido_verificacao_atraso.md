# Exemplo 2: status de pedido com verificação de identidade e atraso

Consulta de pedido (`get_order_status`), que só funciona com o número do pedido **e** um segundo dado do titular.

**O que este exemplo mostra**
- O agente não consulta o pedido só com o número: pede o e-mail ou o telefone cadastrado antes de chamar a tool.
- Verificação de identidade: o telefone informado como `99654-7821` confere com o cadastro `(67) 99654-7821` (a tool compara os últimos 9 dígitos, ignorando formatação e DDD).
- Atraso: o pedido está `shipped` com previsão de 28/02/2026. O agente compara a previsão com a data atual, avisa que ela já passou e encaminha ao WhatsApp da loja, sem inventar a situação do transporte.
- O nome do cliente vem do cadastro (só o primeiro nome), depois de a identidade ser confirmada.

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
