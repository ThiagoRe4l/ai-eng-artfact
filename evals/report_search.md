# Relatório de avaliação da busca de produtos

Gerado em 02/11/2026 15:55. Cada caso roda numa thread nova do agente real.

## Resumo

- Casos com resultado: 18/18
- Checagem de preço (todo R$ citado existe no retorno da tool): 18/18
- Checagem de busca (produtos esperados retornados): 18/18
- Passaram nas duas checagens: 18/18
- Chamadas ao modelo (mensagens do assistente): 41

As checagens são automáticas e limitadas: a de preço só olha valores com `R$` e pode
acusar falso positivo em valores derivados (ex.: economia em reais). O comportamento
esperado de cada caso ainda exige leitura da resposta (seção abaixo).

## Tabela

| # | Mensagem | Args da busca | IDs retornados | Preço | Busca | Resposta |
|---|---|---|---|---|---|---|
| 1 | quero um violão para iniciantes, qual o valor? | {"term": "iniciante estudante começando", "category": "Violões"} | 81, 83, 84, 85, 87, 113, 114 | ✅ | ✅ | Olá! Temos ótimas opções de violão para quem está começando, especialmente com cordas de nylon, que são mais macias para os dedos de quem e… |
| 2 | to começando a tocar agora, qual violão vc indica? | {"term": "iniciante estudante começando", "category": "Violões"} | 81, 83, 84, 85, 87, 113, 114 | ✅ | ✅ | Que legal que você está começando a tocar! Para quem está dando os primeiros passos, o mais indicado costuma ser o violão com **cordas de n… |
| 3 | violao barato | {"category": "Violões"} | 81, 83, 84, 85, 86, 87, 88, 89 | ✅ | ✅ | Olá! Separamos algumas das opções de violão mais em conta que temos disponíveis por aqui, divididas entre cordas de nylon e de aço: **Corda… |
| 4 | tem violão com captação até 1500? | {"category": "Violões", "term": "eletroacústico elétrico captação", "max_price": 1500} | 99, 101, 103, 107 | ✅ | ✅ | Temos ótimas opções de violões eletroacústicos (com captação) por até R$ 1.500,00! Dá uma olhada: **Cordas de Aço:** - **Shelby SGD-195E Su… |
| 5 | quanto ta o yamaha f310 | {"term": "Yamaha F310"} | 81, 82, 87, 92, 98, 104, 114, 139 | ✅ | ✅ | O violão **Yamaha F310 Aço Natural** está saindo por **R$ 699,90** (ou por **R$ 664,90** no PIX, com 5% de desconto). Temos ele disponível … |
| 6 | o Takamine GD20 ainda está em promoção? | {"term": "Takamine GD20"} | 95, 100, 105, 115 | ✅ | ✅ | No momento, o **Takamine GD20 Dreadnought Natural** não está com preço promocional ativo, então ele está pelo valor regular de R$ 2.199,00.… |
| 7 | quais produtos estão em promoção? | {"on_promotion": true} | 90, 94, 121, 127 | ✅ | ✅ | Temos ótimas ofertas ativas no momento! Confira os instrumentos em promoção: - **Ukulele Tenor Kalani KAL-700T Natural** De R$ 359,00 por *… |
| 8 | tem o Giannini GF-3D? | {"term": "Giannini GF-3D"} | 84, 88, 96, 101, 110 | ✅ | ✅ | O violão **Giannini GF-3D Dreadnought Sunburst** está temporariamente indisponível no nosso estoque. Se você procura um modelo parecido, te… |
| 9 | quero o Shelby SN-7C | {"term": "Shelby SN-7C"}<br>{"term": "7 cordas nylon clássico", "category": "Violões"} | 81, 82, 83, 85, 89, 107, 109, 110, 111, 113, 119 | ✅ | ✅ | O violão **Shelby SN-7C 7 Cordas Nylon Natural** saiu do catálogo e não está mais disponível. Mas se você procura um violão de 7 cordas em … |
| 10 | o ukulele barítono Kala Cedar está disponível? | {"term": "Kala Cedar", "category": "Ukuleles"} | 116, 118, 120, 122, 124, 126, 127, 130 | ✅ | ✅ | O Ukulele Barítono Kala Cedar (KA-ABP-CTG) está temporariamente indisponível no momento (com previsão de chegada em breve). Como alternativ… |
| 11 | ukulele pra minha filha de 8 anos | {"category": "Ukuleles", "term": "soprano iniciante"} | 116, 117, 118, 119, 124 | ✅ | ✅ | O tamanho **Soprano** é o ideal para uma criança de 8 anos! Ele é levinho, compacto e bem confortável para as mãos menores. Separei algumas… |
| 12 | guitarra boa pra metal | {"term": "metal", "category": "Guitarras"}<br>{"category": "Guitarras"} | 131, 132, 133, 134, 145 | ✅ | ✅ | Para tocar metal, o modelo ideal costuma ter braço confortável para velocidade, captadores de alto ganho (como humbuckers) e boa estabilida… |
| 13 | vocês têm saxofone? | {"term": "saxofone"}<br>{"category": "Instrumentos de Sopro (Madeiras)"} | - | ✅ | ✅ | Temos instrumentos de sopro no catálogo, mas no momento não temos saxofones disponíveis em estoque. Se quiser, posso te mandar o contato do… |
| 14 | quanto fica o Crafter HT-100 no pix? | {"term": "Crafter HT-100"} | 90, 97, 102 | ✅ | ✅ | O **Crafter HT-100 Folk Aço Natural** está em promoção! - **Preço original:** R$ 2.399,00 - **Desconto:** 18% OFF - **Preço final:** R$ 1.9… |
| 15 | violão 7 cordas pra choro | {"category": "Violões", "term": "7 cordas"} | 82, 83, 86, 109, 110, 111, 112, 113 | ✅ | ✅ | Para tocar choro, os violões de 7 cordas com **nylon** são os mais indicados por causa do timbre tradicional e do conforto nas baixarias. T… |
| 16 | qual o melhor violão que vocês têm? dinheiro não é problema | {"sort": "price_desc", "category": "Violões"} | 93, 94, 97, 98, 102, 105, 106, 108 | ✅ | ✅ | O topo de linha do nosso catálogo hoje é a linha **Martin D-28**, que é uma verdadeira referência mundial em timbre e construção. As nossas… |
| 17 | quanto custa uma bateria? | {"category": "Baterias e Percussão"} | 139, 140, 141 | ✅ | ✅ | Temos opções de baterias acústicas no nosso catálogo a partir de **R$ 4.439,00**. Dá uma olhada nas opções disponíveis no momento: * **Bate… |
| 18 | teclado de 88 teclas | {"term": "88 teclas 88", "category": "Teclados e Pianos"}<br>{"category": "Teclados e Pianos"} | 142, 143, 144 | ✅ | ✅ | No momento, não temos modelos com 88 teclas disponíveis em nosso estoque. Atualmente, nossos teclados disponíveis são de 61 teclas: - **Tec… |

## Detalhe por caso

### 1. quero um violão para iniciantes, qual o valor?

- **Esperado:** Violões para iniciante, com preços da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "iniciante estudante começando", "category": "Violões"}`
- **IDs retornados:** [81, 83, 84, 85, 87, 113, 114]
- **Resposta:**

  > Olá! Temos ótimas opções de violão para quem está começando, especialmente com cordas de nylon, que são mais macias para os dedos de quem está aprendendo.
  >
  > Aqui estão algumas das nossas principais recomendações:
  >
  > - **Tagima Memphis AC-39 Nylon**: R$ 429,90 (ou R$ 408,40 no PIX)
  > - **Rozini RC-104 Nylon Estudante**: R$ 459,90 (ou R$ 436,90 no PIX)
  > - **Yamaha C40 Nylon**: R$ 599,90 (ou R$ 569,90 no PIX)
  >
  > Se você preferir um violão com cordas de aço, temos o **Yamaha F310 Aço** por R$ 699,90 (ou R$ 664,90 no PIX).
  >
  > Você prefere cordas de nylon ou de aço para começar? Se quiser saber mais detalhes de algum deles, é só me avisar!

### 2. to começando a tocar agora, qual violão vc indica?

- **Esperado:** Recomendação de violão de entrada
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "iniciante estudante começando", "category": "Violões"}`
- **IDs retornados:** [81, 83, 84, 85, 87, 113, 114]
- **Resposta:**

  > Que legal que você está começando a tocar! Para quem está dando os primeiros passos, o mais indicado costuma ser o violão com **cordas de nylon**, porque elas são mais macias e machucam bem menos os dedos no início.
  >
  > Separei três opções excelentes que temos disponíveis para estudantes:
  >
  > * **Tagima Memphis AC-39 Nylon:** R$ 429,90 (ou R$ 408,40 no PIX)  
  >   Leve, confortável e com ótimo custo-benefício para quem está começando.
  >
  > * **Rozini RC-104 Nylon Estudante:** R$ 459,90 (ou R$ 436,90 no PIX)  
  >   Muito caprichado, feito com madeiras nacionais e excelente timbre.
  >
  > * **Yamaha C40 Nylon:** R$ 599,90 (ou R$ 569,90 no PIX)  
  >   Um dos violões mais recomendados por professores no mundo todo pela qualidade e durabilidade.
  >
  > Você tem preferência por nylon mesmo ou gostaria de ver opções com cordas de aço?

### 3. violao barato

- **Esperado:** Violões de menor preço, sem acento
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões"}`
- **IDs retornados:** [81, 83, 84, 85, 86, 87, 88, 89]
- **Resposta:**

  > Olá! Separamos algumas das opções de violão mais em conta que temos disponíveis por aqui, divididas entre cordas de nylon e de aço:
  >
  > **Cordas de Nylon (mais macias para começar):**
  > - **Tagima Memphis AC-39 Nylon Natural**: R$ 429,90 (ou R$ 408,40 no PIX)
  > - **Rozini RC-104 Nylon Estudante**: R$ 459,90 (ou R$ 436,90 no PIX)
  >
  > **Cordas de Aço (som mais brilhante):**
  > - **Shelby SN-100 Folk Aço Preto**: R$ 549,00 (ou R$ 521,55 no PIX)
  > - **Giannini GF-1R Aço Folk Sunburst**: R$ 579,90 (ou R$ 550,90 no PIX)
  >
  > Você tem preferência por cordas de nylon ou de aço? Se quiser, posso te ajudar a escolher o ideal para o seu estilo!

### 4. tem violão com captação até 1500?

- **Esperado:** Eletroacústicos com preço final <= R$ 1.500
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "term": "eletroacústico elétrico captação", "max_price": 1500}`
- **IDs retornados:** [99, 101, 103, 107]
- **Resposta:**

  > Temos ótimas opções de violões eletroacústicos (com captação) por até R$ 1.500,00! Dá uma olhada:
  >
  > **Cordas de Aço:**
  > - **Shelby SGD-195E Sunburst**: R$ 799,00 (ou R$ 759,05 no PIX) – Modelo dreadnought com captação e afinador embutido.
  > - **Tagima Vegas Natural**: R$ 1.349,00 (ou R$ 1.281,55 no PIX) – Modelo Folk com captação ativa e som encorpado.
  >
  > **Cordas de Nylon:**
  > - **Giannini GNF-3 CEQ Natural**: R$ 1.049,00 (ou R$ 996,55 no PIX) – Equalizador de 4 bandas e ótimo acabamento.
  > - **Tagima Classical Sunburst**: R$ 1.199,00 (ou R$ 1.139,05 no PIX) – Pré-amplificador e afinador embutido.
  >
  > Você prefere cordas de aço ou nylon? Se quiser detalhes sobre algum deles, só me avisar!

### 5. quanto ta o yamaha f310

- **Esperado:** Yamaha F310 (id 87) com preço da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Yamaha F310"}`
- **IDs retornados:** [81, 82, 87, 92, 98, 104, 114, 139]
- **Resposta:**

  > O violão **Yamaha F310 Aço Natural** está saindo por **R$ 699,90** (ou por **R$ 664,90** no PIX, com 5% de desconto).
  >
  > Temos ele disponível em estoque no momento! 
  >
  > Quer saber mais sobre as especificações dele ou precisa de ajuda para fazer o pedido?

### 6. o Takamine GD20 ainda está em promoção?

- **Esperado:** Promoção encerrada + preço atual
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Takamine GD20"}`
- **IDs retornados:** [95, 100, 105, 115]
- **Resposta:**

  > No momento, o **Takamine GD20 Dreadnought Natural** não está com preço promocional ativo, então ele está pelo valor regular de R$ 2.199,00.
  >
  > Porém, pagando à vista no PIX, você garante 5% de desconto e ele sai por **R$ 2.089,05**. 
  >
  > Temos ele disponível em estoque! Quer tirar alguma dúvida sobre o instrumento?

### 7. quais produtos estão em promoção?

- **Esperado:** Os 4 ativos: ids 90, 94, 121, 127
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"on_promotion": true}`
- **IDs retornados:** [90, 94, 121, 127]
- **Resposta:**

  > Temos ótimas ofertas ativas no momento! Confira os instrumentos em promoção:
  >
  > - **Ukulele Tenor Kalani KAL-700T Natural**  
  >   De R$ 359,00 por **R$ 323,10** (10% de desconto)
  >
  > - **Ukulele Concert Ohana CK-20 Natural**  
  >   De R$ 549,00 por **R$ 439,20** (20% de desconto)
  >
  > - **Violão Folk Aço Crafter HT-100 Natural**  
  >   De R$ 2.399,00 por **R$ 1.967,18** (18% de desconto)
  >
  > - **Violão Eletroacústico Taylor 110e Dreadnought Natural**  
  >   De R$ 5.999,00 por **R$ 5.519,08** (8% de desconto)
  >
  > Procura alguma categoria específica de instrumento ou gostaria de saber mais detalhes sobre algum desses modelos?

### 8. tem o Giannini GF-3D?

- **Esperado:** Sem estoque + alternativas
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Giannini GF-3D"}`
- **IDs retornados:** [84, 88, 96, 101, 110]
- **Resposta:**

  > O violão **Giannini GF-3D Dreadnought Sunburst** está temporariamente indisponível no nosso estoque.
  >
  > Se você procura um modelo parecido, temos o **Giannini GF-1R Aço Folk Sunburst** disponível! Ele também é com cordas de aço e tem aquele acabamento Sunburst bonito. Está saindo por R$ 579,90 (ou R$ 550,90 no PIX).
  >
  > Quer que eu te passe mais detalhes sobre ele ou procure outro modelo?

### 9. quero o Shelby SN-7C

- **Esperado:** Descontinuado + equivalente
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "Shelby SN-7C"}`
- **search_products #2:** `{"term": "7 cordas nylon clássico", "category": "Violões"}`
- **IDs retornados:** [81, 82, 83, 85, 89, 107, 109, 110, 111, 113, 119]
- **Resposta:**

  > O violão **Shelby SN-7C 7 Cordas Nylon Natural** saiu do catálogo e não está mais disponível.
  >
  > Mas se você procura um violão de 7 cordas em nylon, temos ótimas opções disponíveis em estoque:
  >
  > - **Giannini GWNE-7 7 Cordas Nylon Natural**: R$ 1.149,00 (ou R$ 1.091,55 no PIX)
  > - **Rozini RV-174 7 Cordas Nylon Natural**: R$ 1.299,00 (ou R$ 1.234,05 no PIX)
  >
  > Algum desses te interessa ou quer ver outros modelos?

### 10. o ukulele barítono Kala Cedar está disponível?

- **Esperado:** Em breve (id 130)
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Kala Cedar", "category": "Ukuleles"}`
- **IDs retornados:** [116, 118, 120, 122, 124, 126, 127, 130]
- **Resposta:**

  > O Ukulele Barítono Kala Cedar (KA-ABP-CTG) está temporariamente indisponível no momento (com previsão de chegada em breve).
  >
  > Como alternativa com tampo sólido em cedro, temos disponível o **Kala KA-SRT-CTG Tenor Elétrico Cedar** por R$ 1.599,00 (ou R$ 1.519,05 à vista no PIX). Ele oferece um som bem quente e encorpado, além de ser eletroacústico.
  >
  > Posso te passar mais detalhes sobre esse modelo ou ajudar a procurar outra opção?

### 11. ukulele pra minha filha de 8 anos

- **Esperado:** Ukuleles de entrada/soprano
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Ukuleles", "term": "soprano iniciante"}`
- **IDs retornados:** [116, 117, 118, 119, 124]
- **Resposta:**

  > O tamanho **Soprano** é o ideal para uma criança de 8 anos! Ele é levinho, compacto e bem confortável para as mãos menores.
  >
  > Separei algumas opções muito legais que temos disponíveis em estoque:
  >
  > - **Shelby SU-21S Soprano (Sunburst):** R$ 159,90 (ou R$ 151,91 no PIX) — Ótimo custo-benefício e visual clássico.
  > - **Kalani KAL-300S Soprano (Natural):** R$ 179,90 (ou R$ 170,91 no PIX) — Boa projeção de som e acabamento natural.
  > - **Kala KA-15S Soprano (Mogno):** R$ 199,90 (ou R$ 189,91 no PIX) — Um dos modelos mais recomendados para iniciantes, com tom bem doce e cordas Aquila.
  >
  > Algum desses modelos chamou sua atenção ou gostaria de ver mais detalhes de algum deles?

### 12. guitarra boa pra metal

- **Esperado:** Guitarras adequadas a metal
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "metal", "category": "Guitarras"}`
- **search_products #2:** `{"category": "Guitarras"}`
- **IDs retornados:** [131, 132, 133, 134, 145]
- **Resposta:**

  > Para tocar metal, o modelo ideal costuma ter braço confortável para velocidade, captadores de alto ganho (como humbuckers) e boa estabilidade de afinação.
  >
  > A principal recomendação do nosso catálogo é:
  >
  > * **Ibanez RG550 Genesis Collection**
  >   * **Destaques:** Feita sob medida para *shred* e metal, com braço Super Wizard super rápido, ponte Edge tremolo e captadores V7/S1/V8.
  >   * **Preço:** R$ 7.500,00 (ou R$ 7.125,00 no PIX)
  >
  > Outra opção muito versátil para som pesado é:
  >
  > * **PRS SE Custom 24**
  >   * **Destaques:** 24 trastes, captadores humbucker 85/15 "S" e ótimo alcance para riffs pesados e solos.
  >   * **Preço:** R$ 6.800,00 (ou R$ 6.460,00 no PIX)
  >
  > Quer saber mais detalhes de alguma delas ou prefere ver opções em outra faixa de preço?

### 13. vocês têm saxofone?

- **Esperado:** Categoria sem produtos; não inventar
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "saxofone"}`
- **search_products #2:** `{"category": "Instrumentos de Sopro (Madeiras)"}`
- **IDs retornados:** []
- **Resposta:**

  > Temos instrumentos de sopro no catálogo, mas no momento não temos saxofones disponíveis em estoque. 
  >
  > Se quiser, posso te mandar o contato do nosso WhatsApp para você checar com a equipe se há previsão de chegada de novos modelos! Deseja mais alguma informação sobre outros instrumentos?

### 14. quanto fica o Crafter HT-100 no pix?

- **Esperado:** Preço promocional R$ 1.967,18, sem somar o desconto do PIX
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "Crafter HT-100"}`
- **IDs retornados:** [90, 97, 102]
- **Resposta:**

  > O **Crafter HT-100 Folk Aço Natural** está em promoção!
  >
  > - **Preço original:** R$ 2.399,00  
  > - **Desconto:** 18% OFF  
  > - **Preço final:** R$ 1.967,18  
  >
  > Como o produto já está com preço promocional, o desconto de 5% do PIX não é cumulativo. Ou seja, no PIX ele sai pelo mesmo preço final de **R$ 1.967,18**.
  >
  > Temos 3 unidades disponíveis em estoque. Posso te ajudar com mais alguma dúvida sobre ele?

### 15. violão 7 cordas pra choro

- **Esperado:** Shelby SN-7C descontinuado + equivalente
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "term": "7 cordas"}`
- **IDs retornados:** [82, 83, 86, 109, 110, 111, 112, 113]
- **Resposta:**

  > Para tocar choro, os violões de 7 cordas com **nylon** são os mais indicados por causa do timbre tradicional e do conforto nas baixarias. Temos ótimas opções disponíveis:
  >
  > - **Giannini GWNE-7 7 Cordas Nylon Natural** (Acústico)  
  >   Preço: R$ 1.149,00 (ou R$ 1.091,55 no PIX)  
  >   *Construção tradicional brasileira, tampo em Spruce e braço em Cedro.*
  >
  > - **Rozini RV-174 7 Cordas Nylon Natural** (Acústico)  
  >   Preço: R$ 1.299,00 (ou R$ 1.234,05 no PIX)  
  >   *Excelente resposta nos graves e baixarias bem definidas.*
  >
  > - **Rozini RV-175 7 Cordas Elétrico Natural** (Eletroacústico)  
  >   Preço: R$ 1.699,00 (ou R$ 1.614,05 no PIX)  
  >   *Tampo em Spruce sólido, laterais/fundo em Jacarandá e captação para tocar amplificado.*
  >
  > Algum desses modelos chama mais sua atenção? Se quiser, posso te dar mais detalhes!

### 16. qual o melhor violão que vocês têm? dinheiro não é problema

- **Esperado:** Topo de linha (Martin e Taylor)
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"sort": "price_desc", "category": "Violões"}`
- **IDs retornados:** [93, 94, 97, 98, 102, 105, 106, 108]
- **Resposta:**

  > O topo de linha do nosso catálogo hoje é a linha **Martin D-28**, que é uma verdadeira referência mundial em timbre e construção.
  >
  > As nossas duas melhores opções disponíveis são:
  >
  > 1. **Martin D-28E Elétrico Aço Natural** — **R$ 12.000,00** (ou R$ 11.400,00 no PIX com 5% de desconto)
  >    - É a versão com captação **LR Baggs Anthem**, o ápice do som amplificado profissional, mantendo o tampo sólido em Sitka Spruce e fundo em East Indian Rosewood.
  >
  > 2. **Martin D-28 Dreadnought Natural (Puro Acústico)** — **R$ 11.499,00** (ou R$ 10.924,05 no PIX com 5% de desconto)
  >    - O lendário D-28 acústico, famoso pela projeção impecável e pelo timbre encorpado que marcou a história da música mundial.
  >
  > Se você busca um instrumento definitivo, qualquer um dos dois vai te entregar o mais alto padrão. 
  >
  > Quer que eu ajude você com mais detalhes ou com o processo de compra de algum deles?

### 17. quanto custa uma bateria?

- **Esperado:** Baterias com preços da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Baterias e Percussão"}`
- **IDs retornados:** [139, 140, 141]
- **Resposta:**

  > Temos opções de baterias acústicas no nosso catálogo a partir de **R$ 4.439,00**. 
  >
  > Dá uma olhada nas opções disponíveis no momento:
  >
  > * **Bateria Acústica Yamaha Kit 1 Studio** (5 peças, com ferragens): **R$ 4.439,00** (ou **R$ 4.217,05** no PIX com 5% de desconto)
  > * **Bateria Acústica Pearl Kit 2 Studio** (5 peças, com ferragens): **R$ 13.285,00** (ou **R$ 12.620,75** no PIX)
  > * **Bateria Acústica Yamaha Kit 3 Studio** (5 peças, com ferragens): **R$ 14.922,00** (ou **R$ 14.175,90** no PIX)
  >
  > Você está buscando algum modelo específico ou uma faixa de preço específica?

### 18. teclado de 88 teclas

- **Esperado:** Teclados de 88 teclas
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "88 teclas 88", "category": "Teclados e Pianos"}`
- **search_products #2:** `{"category": "Teclados e Pianos"}`
- **IDs retornados:** [142, 143, 144]
- **Resposta:**

  > No momento, não temos modelos com 88 teclas disponíveis em nosso estoque. 
  >
  > Atualmente, nossos teclados disponíveis são de 61 teclas:
  >
  > - **Teclado Sintetizador Korg Synth 1 Pro**: R$ 1.127,00 (ou R$ 1.070,65 no PIX com 5% de desconto)
  > - **Teclado Sintetizador Roland Synth 3 Pro**: R$ 9.351,00 (ou R$ 8.883,45 no PIX com 5% de desconto)
  > - **Teclado Sintetizador Nord Synth 2 Pro**: R$ 19.567,00 (ou R$ 18.588,65 no PIX com 5% de desconto)
  >
  > Algum desses de 61 teclas te atende ou você precisa especificamente de 88 teclas? Se quiser, também posso te direcionar para a nossa equipe pelo WhatsApp para verificar previsões de novas chegadas!

