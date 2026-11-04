# Relatório de avaliação da busca de produtos

Gerado em 03/11/2026 21:30. Cada caso roda numa thread nova do agente real.

## Resumo

- Casos com resultado: 18/18
- Checagem de preço (todo R$ citado existe no retorno da tool): 18/18
- Checagem de busca (produtos esperados retornados): 18/18
- Passaram nas duas checagens: 18/18
- Chamadas ao modelo (mensagens do assistente): 44

As checagens são automáticas e limitadas: a de preço só olha valores com `R$` e pode
acusar falso positivo em valores derivados (ex.: economia em reais). O comportamento
esperado de cada caso ainda exige leitura da resposta (seção abaixo).

## Tabela

| # | Mensagem | Args da busca | IDs retornados | Preço | Busca | Resposta |
|---|---|---|---|---|---|---|
| 1 | quero um violão para iniciantes, qual o valor? | {"category": "Violões", "term": "iniciante estudante começando", "sort": "price_asc"} | 81, 83, 84, 85, 87, 113, 114 | ✅ | ✅ | Temos ótimas opções para quem está começando, especialmente modelos com cordas de nylon, que são mais macios para os dedos no início: - **T… |
| 2 | to começando a tocar agora, qual violão vc indica? | {"sort": "price_asc", "term": "iniciante estudante começando", "category": "Violões"} | 81, 83, 84, 85, 87, 113, 114 | ✅ | ✅ | Para quem está começando, os violões com cordas de nylon costumam ser os mais indicados, pois são mais macios para os dedos durante o apren… |
| 3 | violao barato | {"category": "Violões", "sort": "price_asc"} | 81, 83, 84, 85, 86, 87, 88, 89 | ✅ | ✅ | Aqui estão os violões mais em conta que temos disponíveis no momento: - **Tagima Memphis AC-39 Nylon Natural**: R$ 429,90 (cordas de nylon,… |
| 4 | tem violão com captação até 1500? | {"term": "eletroacústico elétrico captação", "category": "Violões", "max_price": 1500} | 99, 101, 103, 107 | ✅ | ✅ | Temos ótimas opções de violões eletroacústicos (com captação) abaixo de R$ 1.500,00! Olha só as opções disponíveis no nosso catálogo: **Cor… |
| 5 | quanto ta o yamaha f310 | {"term": "Yamaha F310"} | 81, 82, 87, 92, 98, 104, 114, 139 | ✅ | ✅ | O violão Yamaha F310 Aço Natural está custando R$ 699,90 (ou R$ 664,90 com desconto no PIX). Temos ele disponível em estoque! Posso te ajud… |
| 6 | o Takamine GD20 ainda está em promoção? | {"term": "Takamine GD20"} | 95, 100, 105, 115 | ✅ | ✅ | No momento, o Takamine GD20 Dreadnought Natural não está em promoção. O valor atual dele é R$ 2.199,00. No PIX, com o desconto de 5% sobre … |
| 7 | quais produtos estão em promoção? | {"on_promotion": true} | 90, 94, 121, 127 | ✅ | ✅ | Temos os seguintes instrumentos com desconto ativo no momento: - **Ukulele Tenor Kalani KAL-700T Natural**: De R$ 359,00 por R$ 323,10 (10%… |
| 8 | tem o Giannini GF-3D? | {"term": "Giannini GF-3D GF3D"} | 84, 88, 96, 101, 110 | ✅ | ✅ | O violão Giannini GF-3D Dreadnought Sunburst (R$ 799,90) está temporariamente indisponível no nosso estoque. Como alternativa semelhante co… |
| 9 | quero o Shelby SN-7C | {"term": "Shelby SN-7C"}<br>{"term": "7 cordas nylon", "category": "Violões"} | 82, 83, 89, 98, 107, 109, 110, 111, 112, 113, 119 | ✅ | ✅ | O Shelby SN-7C saiu do catálogo e não está mais disponível. Como alternativa de violão de 7 cordas de nylon, temos ótimas opções em estoque… |
| 10 | o ukulele barítono Kala Cedar está disponível? | {"term": "Kala Cedar Barítono", "category": "Ukuleles"} | 116, 118, 120, 124, 126, 127, 128, 130 | ✅ | ✅ | O Ukulele Barítono Kala KA-ABP-CTG Cedar está temporariamente indisponível no nosso estoque (status: em breve). O valor dele é R$ 1.749,00 … |
| 11 | ukulele pra minha filha de 8 anos | {"category": "Ukuleles"} | 116, 117, 118, 119, 120, 121, 124, 127 | ✅ | ✅ | Para uma criança de 8 anos, o tamanho **Soprano** é o mais indicado: é o modelo mais leve e compacto, perfeito para as mãos menores. Aqui e… |
| 12 | guitarra boa pra metal | {"category": "Guitarras", "term": "metal humbucker"}<br>{"category": "Guitarras", "sort": "relevance"} | 131, 132, 133, 134, 145 | ✅ | ✅ | Para quem busca uma guitarra ideal para metal, temos excelentes opções no catálogo: * **Ibanez RG550 Genesis Collection**: R$ 7.500,00 (ou … |
| 13 | vocês têm saxofone? | {"category": "Instrumentos de Sopro (Madeiras)", "term": "saxofone"}<br>{"term": "saxofone"}<br>{"category": "Instrumentos de Sopro (Madeiras)"}<br>{"category": "Instrumentos de Sopro (Metais)"} | - | ✅ | ✅ | No momento não temos saxofones disponíveis em nosso catálogo. Posso te ajudar com algum outro instrumento? |
| 14 | quanto fica o Crafter HT-100 no pix? | {"term": "Crafter HT-100"} | 90, 97, 102 | ✅ | ✅ | O Crafter HT-100 Folk Aço Natural já está com uma promoção ativa de 18% de desconto: de R$ 2.399,00 por R$ 1.967,18. Como as promoções não … |
| 15 | violão 7 cordas pra choro | {"category": "Violões", "term": "7 cordas sete cordas choro"} | 83, 86, 98, 109, 110, 111, 112, 113 | ✅ | ✅ | Temos ótimas opções de violão de 7 cordas de nylon, que é o padrão tradicional para choro e samba. Dá uma olhada nas opções disponíveis no … |
| 16 | qual o melhor violão que vocês têm? dinheiro não é problema | {"category": "Violões", "sort": "price_desc"} | 93, 94, 97, 98, 102, 105, 106, 108 | ✅ | ✅ | O modelo topo de linha do nosso catálogo é o **Martin D-28E Elétrico Aço Natural**, por R$ 12.000,00. Ele é uma verdadeira referência mundi… |
| 17 | quanto custa uma bateria? | {"category": "Baterias e Percussão", "sort": "price_asc"} | 139, 140, 141 | ✅ | ✅ | Temos opções de bateria acústica a partir de R$ 4.439,00. Confira os modelos disponíveis no nosso catálogo: - **Bateria Acústica Yamaha Kit… |
| 18 | teclado de 88 teclas | {"category": "Teclados e Pianos", "term": "88 teclas"}<br>{"category": "Teclados e Pianos"} | 142, 143, 144 | ✅ | ✅ | Temos a seguinte opção em nosso catálogo: - **Teclado Sintetizador Korg Synth 1 Pro** - **Preço:** R$ 1.127,00 - **Preço no PIX:** R$ 1.070… |

## Detalhe por caso

### 1. quero um violão para iniciantes, qual o valor?

- **Esperado:** Violões para iniciante, com preços da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "term": "iniciante estudante começando", "sort": "price_asc"}`
- **IDs retornados:** [81, 83, 84, 85, 87, 113, 114]
- **Resposta:**

  > Temos ótimas opções para quem está começando, especialmente modelos com cordas de nylon, que são mais macios para os dedos no início:
  >
  > - **Tagima Memphis AC-39 (Nylon):** R$ 429,90 — Leve, confortável e muito acessível.
  > - **Rozini RC-104 Estudante (Nylon):** R$ 459,90 — Feito com madeiras nacionais e ótimo som de estudo.
  > - **Yamaha C40 (Nylon):** R$ 599,90 — Um dos violões para iniciantes mais recomendados no mundo.
  >
  > Se você preferir cordas de aço, temos também o **Yamaha F310** por R$ 699,90.
  >
  > Você tem preferência por cordas de nylon ou aço? Posso te ajudar a escolher o modelo ideal!

### 2. to começando a tocar agora, qual violão vc indica?

- **Esperado:** Recomendação de violão de entrada
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"sort": "price_asc", "term": "iniciante estudante começando", "category": "Violões"}`
- **IDs retornados:** [81, 83, 84, 85, 87, 113, 114]
- **Resposta:**

  > Para quem está começando, os violões com cordas de nylon costumam ser os mais indicados, pois são mais macios para os dedos durante o aprendizado. Mas, se você quer tocar estilos como pop, rock ou sertanejo e prefere um som mais brilhante, as cordas de aço também são uma boa opção.
  >
  > Aqui estão algumas das melhores opções disponíveis na loja:
  >
  > - **Tagima Memphis AC-39 (Nylon)**: R$ 429,90 (ou R$ 408,40 no PIX) – Leve, confortável e com ótimo custo-benefício para iniciantes.
  > - **Yamaha C40 (Nylon)**: R$ 599,90 (ou R$ 569,90 no PIX) – Um dos modelos de estudo mais recomendados por professores, com excelente qualidade sonora.
  > - **Yamaha F310 (Aço)**: R$ 699,90 (ou R$ 664,90 no PIX) – Para quem prefere cordas de aço, é um modelo folk muito equilibrado e resistente.
  >
  > Você tem preferência por cordas de nylon ou de aço? Se quiser, posso te ajudar a decidir!

### 3. violao barato

- **Esperado:** Violões de menor preço, sem acento
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "sort": "price_asc"}`
- **IDs retornados:** [81, 83, 84, 85, 86, 87, 88, 89]
- **Resposta:**

  > Aqui estão os violões mais em conta que temos disponíveis no momento:
  >
  > - **Tagima Memphis AC-39 Nylon Natural**: R$ 429,90 (cordas de nylon, ótimo para iniciantes)
  > - **Rozini RC-104 Nylon Estudante**: R$ 459,90 (cordas de nylon)
  > - **Shelby SN-100 Folk Aço Preto**: R$ 549,00 (cordas de aço)
  >
  > Você prefere violão com cordas de nylon ou de aço? Posso te dar mais detalhes de qualquer um deles!

### 4. tem violão com captação até 1500?

- **Esperado:** Eletroacústicos com preço final <= R$ 1.500
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "eletroacústico elétrico captação", "category": "Violões", "max_price": 1500}`
- **IDs retornados:** [99, 101, 103, 107]
- **Resposta:**

  > Temos ótimas opções de violões eletroacústicos (com captação) abaixo de R$ 1.500,00! Olha só as opções disponíveis no nosso catálogo:
  >
  > **Cordas de Aço:**
  > - **Shelby SGD-195E Elétrico Sunburst:** R$ 799,00 (ou R$ 759,05 no PIX) — modelo Dreadnought com afinador integrado.
  > - **Tagima Vegas Elétrico Natural:** R$ 1.349,00 (ou R$ 1.281,55 no PIX) — modelo Folk com captação ativa.
  >
  > **Cordas de Nylon:**
  > - **Giannini GNF-3 CEQ Elétrico Natural:** R$ 1.049,00 (ou R$ 996,55 no PIX) — com equalizador de 4 bandas.
  > - **Tagima Classical Elétrico Sunburst:** R$ 1.199,00 (ou R$ 1.139,05 no PIX) — com pré-amplificador e afinador embutido.
  >
  > Você tem preferência por cordas de aço ou nylon? Posso te ajudar em algo mais?

### 5. quanto ta o yamaha f310

- **Esperado:** Yamaha F310 (id 87) com preço da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Yamaha F310"}`
- **IDs retornados:** [81, 82, 87, 92, 98, 104, 114, 139]
- **Resposta:**

  > O violão Yamaha F310 Aço Natural está custando R$ 699,90 (ou R$ 664,90 com desconto no PIX). Temos ele disponível em estoque!
  >
  > Posso te ajudar com mais alguma dúvida sobre ele ou sobre outro produto?

### 6. o Takamine GD20 ainda está em promoção?

- **Esperado:** Promoção encerrada + preço atual
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "Takamine GD20"}`
- **IDs retornados:** [95, 100, 105, 115]
- **Resposta:**

  > No momento, o Takamine GD20 Dreadnought Natural não está em promoção. 
  >
  > O valor atual dele é R$ 2.199,00. No PIX, com o desconto de 5% sobre o preço de tabela, ele sai por R$ 2.089,05. Temos 5 unidades disponíveis em estoque.
  >
  > Posso te ajudar com mais alguma dúvida ou informação sobre ele?

### 7. quais produtos estão em promoção?

- **Esperado:** Os 4 ativos: ids 90, 94, 121, 127
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"on_promotion": true}`
- **IDs retornados:** [90, 94, 121, 127]
- **Resposta:**

  > Temos os seguintes instrumentos com desconto ativo no momento:
  >
  > - **Ukulele Tenor Kalani KAL-700T Natural**: De R$ 359,00 por R$ 323,10 (10% de desconto)
  > - **Ukulele Concert Ohana CK-20 Natural**: De R$ 549,00 por R$ 439,20 (20% de desconto)
  > - **Violão Crafter HT-100 Folk Aço Natural**: De R$ 2.399,00 por R$ 1.967,18 (18% de desconto)
  > - **Violão Taylor 110e Dreadnought Natural**: De R$ 5.999,00 por R$ 5.519,08 (8% de desconto)
  >
  > Algum desses chamou sua atenção ou posso te ajudar a encontrar outro instrumento?

### 8. tem o Giannini GF-3D?

- **Esperado:** Sem estoque + alternativas
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Giannini GF-3D GF3D"}`
- **IDs retornados:** [84, 88, 96, 101, 110]
- **Resposta:**

  > O violão Giannini GF-3D Dreadnought Sunburst (R$ 799,90) está temporariamente indisponível no nosso estoque.
  >
  > Como alternativa semelhante com cordas de aço e acabamento Sunburst, temos disponível o **Giannini GF-1R Aço Folk Sunburst** por **R$ 579,90** (ou R$ 550,90 no PIX). Ele também tem tampo em Spruce e ótima sonoridade folk.
  >
  > Posso te ajudar com mais detalhes sobre ele ou com outro modelo?

### 9. quero o Shelby SN-7C

- **Esperado:** Descontinuado + equivalente
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"term": "Shelby SN-7C"}`
- **search_products #2:** `{"term": "7 cordas nylon", "category": "Violões"}`
- **IDs retornados:** [82, 83, 89, 98, 107, 109, 110, 111, 112, 113, 119]
- **Resposta:**

  > O Shelby SN-7C saiu do catálogo e não está mais disponível.
  >
  > Como alternativa de violão de 7 cordas de nylon, temos ótimas opções em estoque:
  >
  > - **Giannini GWNE-7 7 Cordas Nylon Natural**: R$ 1.149,00 (ou R$ 1.091,55 no PIX)
  > - **Rozini RV-174 7 Cordas Nylon Natural**: R$ 1.299,00 (ou R$ 1.234,05 no PIX)
  >
  > Gostaria de ver os detalhes de algum desses modelos ou precisa de ajuda para escolher?

### 10. o ukulele barítono Kala Cedar está disponível?

- **Esperado:** Em breve (id 130)
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Kala Cedar Barítono", "category": "Ukuleles"}`
- **IDs retornados:** [116, 118, 120, 124, 126, 127, 128, 130]
- **Resposta:**

  > O Ukulele Barítono Kala KA-ABP-CTG Cedar está temporariamente indisponível no nosso estoque (status: em breve). O valor dele é R$ 1.749,00 (ou R$ 1.661,55 no PIX).
  >
  > Se quiser uma opção de ukulele barítono disponível agora, temos o **Kala KA-B Barítono Mogno** por R$ 599,00 (ou R$ 569,05 no PIX). 
  >
  > Caso prefira o tampo em cedro, temos também o **Kala KA-SRT-CTG Tenor Elétrico Cedar** disponível por R$ 1.599,00 (ou R$ 1.519,05 no PIX).
  >
  > Posso te ajudar com mais alguma dúvida ou detalhe sobre essas opções?

### 11. ukulele pra minha filha de 8 anos

- **Esperado:** Ukuleles de entrada/soprano
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Ukuleles"}`
- **IDs retornados:** [116, 117, 118, 119, 120, 121, 124, 127]
- **Resposta:**

  > Para uma criança de 8 anos, o tamanho **Soprano** é o mais indicado: é o modelo mais leve e compacto, perfeito para as mãos menores.
  >
  > Aqui estão ótimas opções disponíveis:
  >
  > * **Shelby SU-21S Soprano Sunburst**: R$ 159,90 (ou R$ 151,91 no PIX) — visual bonito em Sunburst e ótimo custo-benefício para começar.
  > * **Kalani KAL-300S Soprano Natural**: R$ 179,90 (ou R$ 170,91 no PIX) — tampo em Spruce, com boa projeção de som.
  > * **Kala KA-15S Soprano Mogno**: R$ 199,90 (ou R$ 189,91 no PIX) — corpo em mogno e cordas Aquila, super tradicional e fácil de tocar.
  >
  > Algum desses modelos te chamou mais atenção ou prefere que eu ajude a escolher?

### 12. guitarra boa pra metal

- **Esperado:** Guitarras adequadas a metal
- **Chamadas ao modelo:** 4
- **search_products #1:** `{"category": "Guitarras", "term": "metal humbucker"}`
- **search_products #2:** `{"category": "Guitarras", "sort": "relevance"}`
- **IDs retornados:** [131, 132, 133, 134, 145]
- **Resposta:**

  > Para quem busca uma guitarra ideal para metal, temos excelentes opções no catálogo:
  >
  > * **Ibanez RG550 Genesis Collection**: R$ 7.500,00 (ou R$ 7.125,00 no PIX)
  >   * Referência para metal e *shred*, com braço Super Wizard super rápido, ponte flutuante Edge tremolo e captadores V7/S1/V8.
  > * **PRS SE Custom 24**: R$ 6.800,00 (ou R$ 6.460,00 no PIX)
  >   * Muito versátil para timbres pesados, com 24 trastes, captadores humbucker 85/15 "S" e defasador de bobina.
  > * **Gibson Les Paul Standard '50s**: R$ 18.900,00 (ou R$ 17.955,00 no PIX)
  >   * Perfeita para um metal mais clássico ou heavy rock, com captadores Burstbucker de alto *sustain* e timbre encorpado.
  >
  > Qual dessas combina mais com o seu estilo ou faixa de preço? Posso te ajudar com mais alguma informação sobre elas?

### 13. vocês têm saxofone?

- **Esperado:** Categoria sem produtos; não inventar
- **Chamadas ao modelo:** 5
- **search_products #1:** `{"category": "Instrumentos de Sopro (Madeiras)", "term": "saxofone"}`
- **search_products #2:** `{"term": "saxofone"}`
- **search_products #3:** `{"category": "Instrumentos de Sopro (Madeiras)"}`
- **search_products #4:** `{"category": "Instrumentos de Sopro (Metais)"}`
- **IDs retornados:** []
- **Resposta:**

  > No momento não temos saxofones disponíveis em nosso catálogo. 
  >
  > Posso te ajudar com algum outro instrumento?

### 14. quanto fica o Crafter HT-100 no pix?

- **Esperado:** Preço promocional R$ 1.967,18, sem somar o desconto do PIX
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"term": "Crafter HT-100"}`
- **IDs retornados:** [90, 97, 102]
- **Resposta:**

  > O Crafter HT-100 Folk Aço Natural já está com uma promoção ativa de 18% de desconto: de R$ 2.399,00 por R$ 1.967,18.
  >
  > Como as promoções não são cumulativas, o desconto de 5% do PIX não se aplica sobre produtos que já estão em promoção. Sendo assim, o valor dele no PIX fica em R$ 1.967,18.
  >
  > Posso te ajudar com mais alguma informação sobre esse violão?

### 15. violão 7 cordas pra choro

- **Esperado:** Shelby SN-7C descontinuado + equivalente
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "term": "7 cordas sete cordas choro"}`
- **IDs retornados:** [83, 86, 98, 109, 110, 111, 112, 113]
- **Resposta:**

  > Temos ótimas opções de violão de 7 cordas de nylon, que é o padrão tradicional para choro e samba. Dá uma olhada nas opções disponíveis no estoque:
  >
  > - **Giannini GWNE-7 Nylon Natural (Acústico)**: R$ 1.149,00 — Ótima opção de entrada, com braço em cedro e excelente resposta nos graves para a baixaria.
  > - **Rozini RV-174 Nylon Natural (Acústico)**: R$ 1.299,00 — Muito tradicional no choro, com tampo em Spruce e braço reforçado.
  > - **Rozini RV-175 Elétrico Natural (Eletroacústico)**: R$ 1.699,00 — Modelo captação integrada, tampo em Spruce sólido e corpo em Jacarandá, ideal para quem vai tocar ao vivo ou gravar.
  >
  > Quer saber mais detalhes de algum deles ou precisa de ajuda para escolher?

### 16. qual o melhor violão que vocês têm? dinheiro não é problema

- **Esperado:** Topo de linha (Martin e Taylor)
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Violões", "sort": "price_desc"}`
- **IDs retornados:** [93, 94, 97, 98, 102, 105, 106, 108]
- **Resposta:**

  > O modelo topo de linha do nosso catálogo é o **Martin D-28E Elétrico Aço Natural**, por R$ 12.000,00.
  >
  > Ele é uma verdadeira referência mundial: conta com tampo sólido em Sitka Spruce, fundo e laterais em East Indian Rosewood e vem equipado com a captação profissional LR Baggs Anthem, entregando um som acústico e amplificado impecável.
  >
  > Se você preferir a versão puramente acústica (sem captação), também temos o lendário **Martin D-28 Dreadnought Natural** por R$ 11.499,00.
  >
  > Posso te passar mais detalhes sobre eles ou ajudar com outro modelo?

### 17. quanto custa uma bateria?

- **Esperado:** Baterias com preços da tool
- **Chamadas ao modelo:** 2
- **search_products #1:** `{"category": "Baterias e Percussão", "sort": "price_asc"}`
- **IDs retornados:** [139, 140, 141]
- **Resposta:**

  > Temos opções de bateria acústica a partir de R$ 4.439,00. Confira os modelos disponíveis no nosso catálogo:
  >
  > - **Bateria Acústica Yamaha Kit 1 Studio**: R$ 4.439,00 (ou R$ 4.217,05 no PIX)
  > - **Bateria Acústica Pearl Kit 2 Studio**: R$ 13.285,00 (ou R$ 12.620,75 no PIX)
  > - **Bateria Acústica Yamaha Kit 3 Studio**: R$ 14.922,00 (ou R$ 14.175,90 no PIX)
  >
  > Procura alguma marca, modelo ou faixa de preço específica? Posso te ajudar com mais detalhes!

### 18. teclado de 88 teclas

- **Esperado:** Teclados de 88 teclas
- **Chamadas ao modelo:** 3
- **search_products #1:** `{"category": "Teclados e Pianos", "term": "88 teclas"}`
- **search_products #2:** `{"category": "Teclados e Pianos"}`
- **IDs retornados:** [142, 143, 144]
- **Resposta:**

  > Temos a seguinte opção em nosso catálogo:
  >
  > - **Teclado Sintetizador Korg Synth 1 Pro**
  >   - **Preço:** R$ 1.127,00
  >   - **Preço no PIX:** R$ 1.070,65
  >   - **Disponibilidade:** Em estoque
  >
  > Sobre a quantidade de teclas, esse detalhe eu prefiro confirmar com a equipe antes de te garantir. Você pode falar com eles pelo WhatsApp (67) 3321-4500.
  >
  > Posso te ajudar com mais alguma informação?

