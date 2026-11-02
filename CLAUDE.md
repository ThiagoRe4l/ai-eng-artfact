# Empório da Música: assistente virtual de atendimento

Teste técnico (1ª fase) para a vaga de **AI Engineer na Artefact**. Autor: Thiago Santos.
O avaliador declarou que valoriza mais o **raciocínio e as decisões técnicas** do que uma solução perfeita.

Prazo: 2 dias úteis, provavelmente até 04/11/2026 (confirmar data e hora exatas no e-mail do processo).
Depois do prazo, o repositório não pode receber nenhum commit.

## O que o desafio pede

Agente conversacional por texto, em **Python**, para a Empório da Música, loja fictícia de instrumentos musicais em Campo Grande (MS). O agente precisa:

- ter uma persona coerente com o tom da loja (informal, mas profissional);
- responder com base **somente** nos dados fornecidos: CSVs em `data/` e o manual `data/politicas_da_loja.pdf`;
- **decidir sozinho** quando consultar dados estruturados (preço, estoque, promoção, status de pedido) e quando consultar políticas (troca, frete, pagamento, horário). Esse roteamento é o núcleo da avaliação;
- recusar ou redirecionar bem perguntas fora do escopo.

## Entregáveis

1. Repositório público no GitHub com **histórico real de commits**. Nada de commit único, squash ou force-push.
2. `README.md` com: como rodar, justificativas técnicas, limitações, o que faria com mais tempo e **como usou assistentes de IA** (inclusive este Claude Code).
3. De 3 a 5 conversas de exemplo (.md), sendo pelo menos uma não trivial (consulta de dados ou aplicação de política).

## Regras de trabalho para o Claude Code

- **O Thiago escreve o código principal.** O seu papel é testar, encontrar bugs, fazer correções pequenas e sugerir melhorias. Antes de refatorar, mudar a arquitetura, adicionar dependências ou criar módulos novos em `src/`, pergunte.
- **Git: não execute** `commit`, `push`, `reset`, `rebase`, `checkout` ou `stash`. Quando uma etapa estiver pronta, sugira os comandos, e o Thiago executa. Mensagens de commit **em inglês**, no padrão Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`, `chore:`, `refactor:`).
- **Nunca leia, imprima ou commite o `.env`**, e nunca coloque chaves de API no código.
- **Cota gratuita do Gemini:** economize chamadas reais à API. Prefira testes com `pytest` e mocks, sem rede. Quando precisar testar o modelo de verdade, use poucas mensagens e reporte as respostas.
- Identificadores, nomes de arquivos e commits em **inglês**. Textos para o cliente final e o system prompt em **português do Brasil**.
- Ao terminar cada tarefa, resuma em poucas linhas o que foi feito e o que você alterou. O Thiago usa isso na seção de uso de IA do README.

## Ambiente

- Windows, Python 3.12, ambiente virtual em `.venv` (`.venv/Scripts/python`). Dependências em `requirements.txt`.
- Rodar a CLI: `.venv/Scripts/python main.py`. Rodar os testes: `.venv/Scripts/python -m pytest`.
- Variáveis em `.env` (modelo em `.env.example`): `GOOGLE_API_KEY`, `MODEL_ID` (modelo leve) e `AGENT_MODEL_ID` (modelo do agente).
- `core.autocrlf=true`: o repositório guarda LF, e o editor do Thiago usa CRLF.

## Stack e estrutura

- LangChain 1.x (`create_agent`) e LangGraph (checkpointer), com Gemini via `langchain-google-genai` no free tier.
  - Agente: `gemini-3.6-flash`, com raciocínio para decidir as tools.
  - Modelo leve: `gemini-3.5-flash-lite`, reservado para o guardrail de entrada.
- `main.py`: loop de CLI. Ignora entrada vazia; `sair`, Ctrl+C e EOF encerram sem traceback.
- `src/config.py`: carrega o `.env` e valida as variáveis.
- `src/prompts.py`: `SYSTEM_PROMPT_TEMPLATE` e `build_system_prompt(now=None)`. Usa fuso fixo UTC-4 (Campo Grande, sem horário de verão), porque o Windows não traz `tzdata`.
- `src/assistant.py`: `create_assistant()` com `create_agent`, middleware `@dynamic_prompt` (remonta o prompt a cada chamada para a data e a hora nunca ficarem velhas) e `InMemorySaver`.
- `src/llm.py`: `get_model()` e `test_model()` com o modelo leve.
- `src/tools.py`, `src/rag.py`, `src/schemas.py`: vazios, aguardando as próximas etapas.

## Decisões de arquitetura

Já tomadas:

- **Sem fine-tuning.** Estoque, pedidos e promoções mudam, e o manual proíbe informar preço, estoque ou prazo sem consultar o sistema. A solução é um agente com tools, mais retrieval para as políticas.
- **Um único agente** de atendimento. Dividir em vários agentes (estilo CrewAI) adiciona latência sem ganho. O guardrail é separado porque tem outra responsabilidade.
- **System prompt:** persona, regras de comportamento e fatos usados quase sempre (endereço, contatos, horário). Detalhes de pagamento, trocas, frete e garantia ficam no RAG. A seção com a data atual fica **no fim** do prompt para preservar o prefixo estático (cache implícito do Gemini).
- **Thought signatures do Gemini 3:** o histórico precisa manter as `AIMessage` originais. Não reconstrua mensagens a partir do texto.

Planejadas:

- **Tools tipadas** em vez de text-to-SQL livre, para evitar vazamento de dados de clientes (LGPD):
  - `search_products(category, max_price, term, ...)`, que já considera status, estoque e promoção ativa;
  - `get_product_details(name_or_id)`;
  - `get_order_status(order_id, email_or_phone)`, que exige verificação de identidade.
- **RAG das políticas** com chunking por seção do PDF e `InMemoryVectorStore`. Não usar Weaviate, porque exige servidor e atrapalha o avaliador. Exposto como tool (`search_policies`).
- **Guardrail de entrada:** classificador com saída estruturada (Pydantic) no modelo leve. Categorias: `in_scope`, `accessory`, `out_of_scope`, `injection_or_abuse`. Cuidado com falsos positivos, como "qual violão para gospel?".
- **Guardrail de saída**, determinístico, sem LLM:
  - preços citados precisam vir do resultado das tools;
  - desconto só se a promoção tiver `is_active = 1`;
  - nenhum dado de outro cliente.
  - Se falhar, uma nova tentativa com o erro como feedback; depois, fallback.
- Persistência do histórico (SQLite), script de avaliação com mensagens de borda e conversas de exemplo.

## Dados (`data/`) e inconsistências conhecidas

Arquivos: `products`, `categories`, `promotions`, `orders`, `order_items`, `customers` (.csv) e `politicas_da_loja.pdf`.
O tratamento e as escolhas abaixo devem ser documentados no README.

**Produtos**
- Vários nomes não batem com a descrição. Por exemplo, "Music Man Bass 1X" é descrito como Fender Jazz Bass; "Bateria Yamaha Kit 1" como Pearl Export; "Korg Synth 1" como Roland de 88 teclas, mas o specs diz 61.
- Status com armadilhas:
  - 113 e 136 estão `discontinued`;
  - 130 está `coming_soon`, mas aparece vendido nos pedidos 3 e 14;
  - 96 está `active` com estoque 0.
- O `specs` é JSON com esquema diferente por categoria.
- As categorias 6, 7 e 8 (sopros e cordas orquestrais) não têm produtos, embora o manual diga que a loja vende.

**Promoções**
- Só 4 estão ativas: produtos 90, 94, 121 e 127.
- O Takamine GD20 (95), citado no enunciado, tem promoção **inativa**. O agente deve dizer que ela encerrou e informar o preço atual.

**Pedidos**
- O total do pedido 3 (2 × 1.749 = R$ 3.498) está registrado como R$ 3.450.
- O pedido 20 soma R$ 1.488 nos itens e registra R$ 1.400.
- Os pedidos `pending` são de março de 2026, o que exige usar a data atual com cuidado.

**Clientes**
- Os clientes 11 e 43 têm o **mesmo e-mail**. Por isso, a verificação de identidade usa número do pedido mais e-mail ou telefone.

**Manual de políticas (suposições adotadas)**
- WhatsApp (67) 3321-4500 (seção 7) e telefone (67) 3341-4444.
- E-mail sem acento (`contato@emporiodamusica.com.br`).
- No parcelamento, as regras detalhadas da seção 3.1 prevalecem sobre a tabela. Até 3x: parcela mínima de R$ 50.
- A loja não vende acessórios (cordas, cabos, palhetas, pedais, amplificadores, cases): redirecionar com gentileza, sem inventar lojas parceiras.
- O desconto de 5% no PIX não acumula com promoção.
- Promoção sempre apresentada com preço original, percentual e preço final.
