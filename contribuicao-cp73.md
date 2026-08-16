# Contribuição à Consulta Pública nº 73/2026 — Conitec

**Tema:** Angiotomografia coronariana como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de doença arterial coronariana estável.

**Natureza da contribuição:** técnico-científica.

---

## Quadro-resumo

| Pergunta do Comitê | Resposta desta contribuição |
|---|---|
| Capacidade instalada | **432 tomógrafos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS (CNES 06/2026) — piso documentado; 2.785 equipamentos ainda sem especificação de canais. **79 estabelecimentos** reúnem hardware compatível, hemodinâmica e produção coronariana em 2025. 12 UFs não têm nenhum. |
| Custo do percurso atual | R$ 185,46 por episódio de investigação funcional (mix médio observado no SIA 2025); cateterismo R$ 730,14. Ambos são preços de tabela, não custos de produção. |
| Preço admissível | Depende de **qual exame a AngioTC substitui**. Nos ensaios com comparador não invasivo, o Δ de cateterismo total foi de −6,3 a +4,1 por 100. Se substitui o mix médio: neutralidade a **R$ 139–215**. Se substitui cintilografia: **R$ 741–817**. O preço proposto pelo demandante é R$ 550,00. |
| Outro PICO | Em pacientes já indicados a cateterismo (4 ensaios), o preço de neutralidade é de **R$ 482–625**; um ensaio (CAD-MAN) cruza R$ 622,54 por R$ 2,67. População distinta, não intercambiável com a apreciada. |
| Conclusão | **A sustentabilidade orçamentária depende de onde a tecnologia entra no percurso e de qual exame substitui — e a população elegível não é identificável nos registros administrativos.** A análise não demonstra que nenhuma indicação economiza; demonstra que o posicionamento muda radicalmente a plausibilidade. |

---

## 1. Objeto da contribuição

O Relatório de Recomendação Preliminar registra que a deliberação desfavorável de 3 de julho de 2026 (153ª Reunião Ordinária) foi fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à **capacidade de implementação da tecnologia no SUS** e à delimitação da população elegível. O Comitê destacou como essenciais ao esclarecimento em consulta pública, entre outros pontos, "a estimativa da capacidade instalada", "a necessidade ou não de aquisição de equipamentos" e "o impacto real sobre a realização de angiografias invasivas e testes funcionais".

Esta contribuição responde a esses pontos com análise nacional construída sobre bases públicas — CNES, SIA/SUS, SIH/SUS, SIGTAP e IBGE. O relatório preliminar utiliza DATASUS/TABNET e SIGTAP para demanda e preços; **não utiliza o CNES para caracterizar a capacidade instalada**.

Método, endereços de origem e código no Apêndice A. As seções 2 e 3 são integralmente reproduzíveis a partir dos microdados; a seção 4 depende adicionalmente de valores extraídos de publicações listadas no Apêndice B e nas Referências.

---

## 2. Capacidade instalada: o que o cadastro nacional já permite responder

**Fonte:** CNES, arquivos de equipamentos (`EQ`), competência 06/2026, 27 UFs. Considerados apenas equipamentos com `IND_SUS=1` e `QT_USO>0`. A classificação é autodeclarada pelo estabelecimento.

A **Portaria SAES/MS nº 3.695, de 15 de janeiro de 2026** (DOU nº 18, 27/01/2026, Seção 1, p. 89–90; republicada com correções em 18/05/2026) desmembrou o código genérico `11 — Tomógrafo Computadorizado` em categorias por número de canais: `26` (4 canais), `27` (16), `28` (32), `29` (64) e `30` (128). O código `31` corresponde a Tomógrafo Simulador para Radioterapia, de uso exclusivo; os códigos `32` a `35` são equipamentos de ressonância magnética. Nenhum deles integra capacidade tomográfica diagnóstica.

É portanto possível — ao contrário do que se poderia supor a partir das tabelas de conversão ainda distribuídas com os arquivos, que não refletem a portaria — responder diretamente à especificação de **64 canais ou mais** adotada pelas diretrizes citadas no relatório preliminar.

### 2.1 Estratificação do parque tomográfico do SUS

| Camada | Definição | Estabelecimentos | Equipamentos |
|---|---|---|---|
| **Compatível confirmado (≥64 canais)** | códigos 29 + 30 | **315** | **432** |
| — 64 canais | código 29 | 211 | 293 |
| — 128 canais | código 30 | 123 | 139 |
| **Incompatível confirmado (<64 canais)** | códigos 26 + 27 + 28 | 672 | 736 |
| **Especificação não declarada** | código 11 | 2.534 | 2.785 |
| **Parque total disponível ao SUS** | | **3.395** | **3.953** |

As camadas se sobrepõem por estabelecimento: 77 estabelecimentos possuem equipamentos em ≥64 e em <64 canais simultaneamente, e 19 possuem 64 e 128. A coluna de estabelecimentos por isso não soma 3.395; a de equipamentos, sim.

### 2.2 A reclassificação está incompleta — e isso é o achado operacional central

Em 06/2026, **910 estabelecimentos (26,8%)** possuíam ao menos um equipamento já reclassificado por canais; **861 (25,4%)** haviam migrado integralmente; **2.534 (74,6%)** ainda possuíam ao menos um equipamento sob o código genérico. As duas primeiras definições se sobrepõem parcialmente à terceira (49 estabelecimentos têm equipamentos nas duas situações).

A portaria concede prazo de **três competências** a contar da implementação no sistema CNES para que gestores realizem a reclassificação. O art. 9º prevê efeitos operacionais a partir da competência seguinte à publicação; se a implementação ocorreu em 02/2026, o prazo regulamentar já se encerrou antes da competência aqui analisada, e a reclassificação de 25% reflete adesão incompleta, não prazo em curso. Se a implementação foi posterior à republicação de maio, o prazo pode ainda estar aberto. **A data efetiva de implementação no sistema não é verificável nos microdados** e deve ser confirmada pela SAES.

O enunciado correto da capacidade é, em qualquer caso:

> **432 equipamentos de ≥64 canais estão documentados como disponíveis ao SUS. Esse é um piso de capacidade documentada, não uma estimativa da capacidade real** — o número verdadeiro é 432 somado a uma fração desconhecida dos 2.785 equipamentos ainda não classificados.

**Recomendação operacional:** que a apreciação final utilize o cadastro na competência mais recente disponível e registre explicitamente a proporção reclassificada nessa data. Se a adesão permanecer baixa, recomenda-se que a SAES considere instrumentos para completá-la — o inventário por canais é o dado cuja ausência motivou parte da recomendação preliminar.

### 2.3 Estratos de prontidão para implementação

Possuir hardware compatível não equivale a estar apto. Cruzando o estrato confirmado ≥64 canais com dois marcadores independentes — sala de hemodinâmica no mesmo CNES (código `10`) e produção coronariana invasiva efetivamente realizada em 2025 (SIH: angioplastia coronariana, códigos `0406030014/22/30/49/65/73`, ou revascularização miocárdica, códigos `0406010927/35/43/51`) — obtém-se:

| Estrato | Estabelecimentos |
|---|---|
| ≥64 canais confirmado | 315 |
| ≥64 canais **+ hemodinâmica no mesmo CNES** | 114 |
| ≥64 canais **+ produção coronariana documentada em 2025** | 96 |
| **≥64 canais + hemodinâmica + produção coronariana** | **79** |

O estrato de 79 estabelecimentos reúne hardware comprovadamente compatível, infraestrutura cardiovascular instalada e atividade coronariana documentada. É o conjunto com maior plausibilidade de implantação **sem aquisição de tomógrafo**. Software de análise cardíaca, sincronização eletrocardiográfica, bomba injetora e profissionais habilitados em laudo cardiovascular **não constam do CNES** e não são verificáveis por esta análise.

A co-localização com hemodinâmica **não é requisito técnico** para angiotomografia — um serviço de radiologia com tomógrafo de 128 canais e cardiologista habilitado realiza o exame sem sala de hemodinâmica, e um hospital com hemodinâmica e tomógrafo de 16 canais não está tecnicamente apto. O cruzamento é adotado como marcador de maturidade cardiovascular institucional, não como limite inferior de capacidade.

O CNES tampouco informa horas de operação ou agenda. A carga atual do parque tomográfico do SUS (SIA 2025, grupo `0206` exceto PET-CT) é de aproximadamente 13,4 milhões de exames — cerca de 3.400 por equipamento sobre o parque total de 3.953, ou 4.800 sobre os 2.785 sob código genérico; a capacidade em *vagas* para exames adicionais não foi estimada nesta contribuição.

### 2.4 Distribuição e equidade

Densidade nacional de equipamentos compatíveis confirmados: **2,02 por milhão de habitantes** (IBGE 2025, 213.421.037 hab.).

- **Amapá, Piauí e Tocantins não possuem nenhum tomógrafo de ≥64 canais confirmado** disponível ao SUS.
- **Doze unidades federativas não possuem nenhum estabelecimento no estrato de prontidão:** AC, AL, AM, AP, GO, MT, PA, PI, RO, RR, SE e TO.
- São Paulo concentra 164 equipamentos compatíveis e 23 estabelecimentos prontos; o Distrito Federal lidera em densidade (6,01 por milhão).

A desigualdade medida sobre hardware efetivamente compatível é mais acentuada do que a medida sobre o parque agregado: coeficiente de variação da densidade por UF de 0,86 (≥64 canais) contra 0,32 (todos os tomógrafos); índice de Gini ponderado por população de 0,30 contra 0,14. Projeções de difusão ancoradas no total de tomógrafos superestimam a capacidade acessível, e o fazem de modo desigual entre regiões.

Tabela completa por UF: `output/out-capacidade-canais-uf.csv`.

---

## 3. Cenário atual: o que o SUS efetivamente realiza

**Fonte:** SIA/SUS e SIH/SUS, competências 01–12/2025, 27 UFs, 395 arquivos SIA e 324 SIH processados sem perda. Códigos conferidos contra SIGTAP competência 08/2026.

### 3.1 A unidade de análise é o episódio, não o procedimento faturado

A cintilografia miocárdica de perfusão é registrada sob dois códigos distintos — estresse (`0208010025`) e repouso (`0208010033`). Em 2025 o SUS registrou 151.784 e 151.225 respectivamente. A diferença líquida nacional é de 559; por estabelecimento-mês há 3.215 estresses a mais que repousos e 2.656 repousos a mais que estresses. **O número exato de pares não é observável sem identificador de paciente**; a convenção adotada — contar episódios de cintilografia pelo código de estresse — trata os dois registros como etapas de um exame, o que é coerente com o desenho do procedimento e com a literatura nacional (o estudo de custo-efetividade no SUS de 2022 também tratou os dois códigos como um exame, R$ 791,59 = 408,52 + 383,07 da SIGTAP).

Contar procedimentos faturados infla o denominador em 19%. A análise abaixo usa episódios.

| Episódio de investigação funcional | Episódios | Participação (volume) | Gasto | Participação (gasto) |
|---|---|---|---|---|
| Teste ergométrico | 598.695 | 76,0% | R$ 19,3 mi | 13,2% |
| Cintilografia de perfusão (estresse + repouso) | 151.784 | 19,3% | R$ 119,4 mi | 81,7% |
| Ecocardiografia de estresse | 33.766 | 4,3% | R$ 6,6 mi | 4,5% |
| Cintilografia de câmaras — esforço | 3.709 | 0,5% | R$ 0,8 mi | 0,5% |
| **Total** | **787.954** | | **R$ 146,1 mi** | |
| **Custo médio por episódio** | | | **R$ 185,46** | |

Cateterismo cardíaco (`0211020010`), registrado no SIA: 163.803 procedimentos, R$ 119,6 mi, custo médio **R$ 730,14**. O valor da AIH para cateterismo (SH + SP) é R$ 772,80, parâmetro adotado pelo NATS no relatório preliminar.

**Ambos os valores — R$ 185,46 e R$ 730,14 — são preços de tabela, não custos de produção.** Nenhum microcusteio contemporâneo dos comparadores foi localizado; a comparação de uma tecnologia microcusteada contra comparadores remunerados por tabela é assimétrica, e o sentido do viés depende de a tabela estar acima ou abaixo do custo real, o que não é conhecido.

### 3.2 Composição da investigação funcional

O teste ergométrico responde por **76,0% dos episódios** identificados nos códigos selecionados do SIA em 2025, a custo médio de R$ 32,20 — mas por apenas **13,2% do gasto**. A cintilografia, com 19,3% dos episódios, concentra **81,7% do gasto**. O volume está no exame barato; o dinheiro está no exame caro.

Esta é uma afirmação sobre **registros administrativos selecionados**, não sobre a população elegível à angiotomografia. O teste ergométrico possui indicações além da investigação inicial de DAC estável — capacidade funcional, arritmias de esforço, estratificação pré-operatória, acompanhamento de doença conhecida. Não é possível, sem identificação de paciente e indicação clínica, saber qual exame a angiotomografia substituiria na população-alvo. **Este é o parâmetro dominante da análise econômica, e é desconhecido** (seção 4.4).

### 3.2.1 As linhas de cuidado organizadas: OCI de síndrome coronariana crônica

O Ministério da Saúde estruturou a investigação da síndrome coronariana crônica em Ordens de Cuidado Integrado próprias, remuneradas como episódio: `0902010034` — avaliação diagnóstica inicial, pacote com consulta especializada, ECG, ecocardiograma, teste ergométrico, exames laboratoriais e retorno, R$ 270,00; `0902010042` — progressão I, incorporando ecocardiografia de estresse, R$ 250,00; `0902010050` — progressão II, incorporando cintilografia de perfusão em estresse e repouso, R$ 840,00.

**Regra de análise, fixada antes da extração:** quando a OCI é registrada como procedimento principal, os componentes aparecem no SIA com valor zerado e **não são somados novamente** — o custo do episódio é o valor da OCI. Verificou-se que o mecanismo está no dado: ao menos 3.266 procedimentos funcionais em chaves estabelecimento-mês com `PA_VALAPR = 0` em 2025 (1.997 ergometrias, 522 + 559 cintilografias, 188 ecos de estresse) — limite inferior, pois a agregação é por chave e não por registro. Procedimentos com valor positivo seguem no *legacy pathway*.

**Produção em 2025, 27 UFs:**

| Pathway | Episódios | Gasto | R$ por episódio |
|---|---|---|---|
| Legacy — procedimentos isolados com valor > 0 | 785.247 | R$ 146,1 mi | 186,10 |
| **OCI de SCC** (0034 · 0042 · 0050) | **7.616** | R$ 2,51 mi | 329,75 |
| **Ponderado nacional** | **792.863** | R$ 148,6 mi | **187,48** |

As OCI de SCC respondem por **0,96% dos episódios** — 6.505 avaliações iniciais, 302 progressões I e 809 progressões II, em 148 estabelecimentos de 13 UFs. A OCI `0902010026 — Avaliação Cardiológica` (R$ 200,00), com 77.241 episódios em 2025, não foi examinada quanto à sua composição; se incluir exames funcionais, a fração organizada é maior que 0,96%.

A tabela da seção 3.1 (787.954 episódios) inclui os componentes zerados na contagem; o legacy pathway (785.247) os exclui. A diferença de 2.707 corresponde exatamente aos 1.997 + 522 + 188 componentes zerados na convenção de contagem por estresse.

**Sensibilidade do intercepto às OCI.** O modelo da seção 4 usa R$ 185,46 (seção 3.1). Substituindo pelo ponderado nacional com OCI, todos os preços de neutralidade de primeira linha sobem R$ 2,02; a reta de gatekeeping não se altera. Nenhuma conclusão muda. Esta sensibilidade é pequena; a que importa está na seção 4.4.

### 3.3 Angiotomografia coronariana é administrativamente invisível

Não existe código para angiotomografia coronariana na Tabela de Procedimentos do SUS (SIGTAP 08/2026, 5.023 procedimentos verificados). A produção atual não é mensurável: ou é registrada sob código genérico de tomografia, ou não é registrada. Isso é coerente com o registro, no relatório preliminar, de que o exame ocorre em serviços públicos e conveniados sem utilização estruturada e sem procedimento específico.

Verificou-se adicionalmente que o código `0206030045 — CONTRASTE PARA TOMOGRAFIA COMPUTADORIZADA` **não registra faturamento no SIA em 2025**, o que impede seu uso como marcador de serviços com capacidade para exames contrastados.

**Consequência:** nenhum custo unitário para a angiotomografia pode ser ancorado em produção histórica do SUS. O microcusteio contemporâneo, com abertura completa de componentes, é condição necessária.

### 3.4 Escala da cardiologia intervencionista — contexto, não denominador

Em 2025 o SUS registrou **133.934 angioplastias coronarianas** (códigos `0406030014/22/30/49/65/73`; R$ 1.033 mi; 268 estabelecimentos) e **23.290 revascularizações miocárdicas** (códigos `0406010927/35/43/51`; R$ 603 mi; 230 estabelecimentos), em uma rede coronariana invasiva de 273 estabelecimentos.

**Estes números são apresentados como contexto de escala e não como denominador econômico da estratégia.** A população submetida a esses procedimentos inclui infarto agudo do miocárdio, síndrome coronariana aguda, doença coronariana previamente conhecida e doença multiarterial — populações que não são desfecho da investigação de pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária.

Conceitualmente, a angiotomografia pode reduzir angiografias invasivas **diagnósticas** de resultado negativo sem reduzir revascularizações, e pode aumentar revascularizações apropriadas ao identificar doença antes não detectada. A sustentabilidade orçamentária da estratégia não depende de reduzir este montante.

---

## 4. Análise de limiar: quanto o SUS poderia pagar

### 4.1 Por que limiar e não estimativa pontual

O SIA não possui identificador de paciente utilizável. Não é possível determinar se um cateterismo registrado ocorreu após um teste funcional específico, na mesma pessoa, ou na mesma indicação clínica. A razão entre contagens agregadas de cateterismos e de testes funcionais **não é uma probabilidade condicional** e não pode ser usada para projetar redução de procedimentos: fazê-lo seria inferência ecológica.

A análise abaixo não estima quantas angiografias a angiotomografia evitaria. Ela responde à pergunta inversa:

> **Quantas angiografias diagnósticas por 100 pacientes seria necessário evitar, a cada preço, para que a estratégia fosse orçamentariamente neutra?**

O julgamento sobre a plausibilidade clínica de cada valor permanece com o leitor especializado.

### 4.2 Formulação — duas equações, uma por PICO

Sob substituição de um episódio funcional por uma angiotomografia:

```
P_neutralidade,primeira linha  =  C_substituído  +  (Δ_CATE / 100) × C_CATE
```

Quando a angiotomografia filtra um cateterismo já indicado, a investigação prévia já ocorreu antes da randomização, é comum aos dois braços e cancela:

```
P_neutralidade,gatekeeping     =                    (Δ_CATE / 100) × C_CATE
```

com `C_CATE = R$ 730,14` (SIA 2025) e `Δ_CATE` como parâmetro declarado. O desenho de cada ensaio determina qual equação se aplica. **O SCOT-HEART, cujo desenho é aditivo — angiotomografia somada ao cuidado padrão contra cuidado padrão —, não substitui episódio funcional e recai na segunda equação**, embora sua população seja de primeira linha; seus preços de neutralidade (R$ −8,76 aos 6 meses; R$ 3,65 aos 5 anos) refletem apenas o custo dos cateterismos induzidos ou evitados, e o ensaio é apresentado à parte.

`C_substituído` é o parâmetro dominante e desconhecido para a população elegível (seção 3.2). A análise é apresentada para três valores: o mix médio observado no SIA (R$ 185,46); o mix adotado pelo NATS no relatório preliminar (R$ 316,76: teste ergométrico seguido de 50% cintilografia e 50% ecocardiografia de estresse); e a cintilografia de perfusão (R$ 786,83, valor médio aprovado por episódio), cenário em que a angiotomografia substitui o exame de imagem funcional — o mais plausível na probabilidade pré-teste intermediária.

### 4.3 Δ necessário por preço e por exame substituído

O relatório preliminar adota **R$ 550,00** como preço da angiotomografia proposto pelo demandante. Os demais preços de referência são o proxy de tabela para TC de tórax com contraste, o microcusteio de 2022 corrigido monetariamente, e a CBHPM.

| Preço da AngioTC | Natureza | Δ necessário — mix SIA | Δ necessário — mix NATS | Δ necessário — cintilografia |
|---|---|---|---|---|
| R$ 196,41 | TC tórax + contraste, proxy SIGTAP | 1,5 | já neutro | já neutro |
| **R$ 550,00** | **proposto pelo demandante** | **49,9** | **31,9** | **já neutro** |
| R$ 622,54 | microcusteio 2022 corrigido a jul/2026 (IPCA 12/2020→07/2026, ×1,3771) | 59,9 | 41,9 | já neutro |
| R$ 1.311,95 | CBHPM 2026, saúde suplementar | 154,3 | 136,3 | 71,7 |

Ao preço da CBHPM e substituindo o mix médio, seriam necessárias mais angiografias evitadas do que pacientes investigados — **inalcançável neste modelo**, em que o único crédito a jusante é o cateterismo evitado ao valor de tabela. Créditos por outros recursos evitados ou um `C_CATE` microcusteado superior alterariam esse limite.

### 4.4 Confronto com a evidência — o resultado depende do exame substituído

Ensaios randomizados de estratégia diagnóstica reportam taxas absolutas de cateterismo total por braço. Convertendo para a convenção desta análise (Δ positivo = cateterismos evitados por 100 pacientes), nos ensaios que compararam a angiotomografia a estratégias não invasivas de primeira linha:

| Ensaio | Comparador | Janela | Δ observado /100 |
|---|---|---|---|
| CAPP | teste ergométrico | 1 ano | −6,3 |
| PROMISE | funcional-primeiro | 90 dias | −4,1 |
| Foy 2017, subgrupo estável (metanálise) | funcional-primeiro | média 18 meses | −2,9 |
| Foy 2017, 13 ensaios (metanálise) | funcional-primeiro | média 18 meses | −2,6 |
| CRESCENT-I | funcional-primeiro | 1 ano | −1,0 |
| CRESCENT-II | funcional-primeiro | 6 meses | +1,4 |
| PRECISE | usual testing | 11,8 meses | +4,1 |

Faixa observada: **−6,3 a +4,1 por 100**. Aplicando a equação de primeira linha a cada valor de `C_substituído`:

| Exame substituído | C | Preço de neutralidade para Δ de −6,3 a +4,1 | vs R$ 550 | vs R$ 622,54 |
|---|---|---|---|---|
| Mix médio do SIA | R$ 185,46 | **R$ 139 – 215** | abaixo | abaixo |
| Mix do NATS | R$ 316,76 | **R$ 270 – 347** | abaixo | abaixo |
| Cintilografia de perfusão | R$ 786,83 | **R$ 741 – 817** | **acima** | **acima** |

**O sinal da conclusão inverte com o exame substituído.** Se a angiotomografia substitui o mix médio do SUS — majoritariamente teste ergométrico —, o preço de neutralidade fica três a quatro vezes abaixo do proposto, e o Δ necessário (49,9 a R$ 550) é doze vezes o melhor Δ observado. Se substitui a cintilografia de perfusão, a estratégia é neutra ou economizadora em **toda** a faixa observada, mesmo ao custo microcusteado corrigido.

Nos ensaios que compararam estratégias não invasivas iniciais, a magnitude da redução observada na angiografia invasiva foi ausente, variável ou insuficiente para sustentar, isoladamente, neutralidade orçamentária aos custos estimados para o SUS — **quando o exame substituído é o mix médio ou o mix do NATS**. Quando o exame substituído é a cintilografia, o próprio custo do comparador financia a substituição.

**A pergunta decisiva, portanto, não é o Δ de cateterismos. É qual exame a angiotomografia substituiria na população elegível — e essa pergunta é a mesma que o Comitê formulou como "definição precisa da população elegível".** Ela não é respondível a partir do SIA. É respondível por protocolo: se a incorporação especificar que a angiotomografia substitui a imagem funcional na probabilidade intermediária, o cenário econômico é o da última linha; se substituir a investigação inicial de forma indistinta, é o da primeira.

**Ressalvas.** Os horizontes diferem (90 dias a 18 meses) e os pontos não constituem metanálise. PROMISE contabiliza 90 dias; o efeito é dependente do horizonte, como o SCOT-HEART demonstra (aumento em 6 meses, nulo em 5 anos, HR 1,00). O braço de intervenção do PRECISE inclui diferimento de teste em 20% dos pacientes de menor risco — não é substituição 1:1. A metanálise de Foy inclui 9 de 13 ensaios em população de emergência; utilizou-se o subgrupo estável. As contagens do CAPP não constam do artigo primário; provêm do gráfico de floresta de Foy (2017). Em CRESCENT-I e II as diferenças de cateterismo total não são estatisticamente significativas (p = 0,843 e 0,860). O PROMISE ilustra a dissociação entre volume e adequação — aumentou o cateterismo total de 8,1% para 12,2% e reduziu o cateterismo sem doença obstrutiva de 4,3% para 3,4%; o PRECISE reduziu o cateterismo total de 16,9% para 12,8% com aumento de revascularização de 5,2% para 9,2%, custo diagnóstico −27% e custo de revascularização +67% (Circ Cardiovasc Qual Outcomes, PMID 39895495). **Reduzir cateterismo não implica reduzir gasto.**

Os CRESCENT aplicaram filtro por escore de cálcio antes da angiotomografia; o CAPP realizou angiotomografia em todos. A heterogeneidade entre estratégias sugere que o impacto orçamentário depende também dos critérios de seleção e do protocolo — mas comparações indiretas entre ensaios não permitem quantificar isoladamente esse efeito.

### 4.5 O espaço econômico é maior em outro PICO

Ensaios com comparador **invasivo-primeiro** — pacientes já referenciados para cateterismo — recaem na equação de gatekeeping. Todos os Δ abaixo são de **cateterismo total por braço randomizado**, extraídos das publicações primárias.

| Ensaio | Cateterismo, AngioTC | Cateterismo, controle | Janela | Δ /100 | Preço de neutralidade |
|---|---|---|---|---|---|
| CONSERVE | 23% | 89% | 1 ano | 66,0 | R$ 481,89 |
| Reis 2022 | 32/115 (27,8%) | 105/105 (100%) | ≤ 3 meses | 72,2 | R$ 526,97 |
| DISCHARGE | 404/1808 (22,3%) | 1708/1753 (97,4%) | manejo inicial | 75,1 | R$ 548,25 |
| CAD-MAN | 24/167 (14,4%) | 162/162 (100%) | índice | **85,6** | **R$ 625,21** |

Nessa indicação o preço de neutralidade é de **R$ 482 a R$ 625**, independentemente do exame prévio — porque ele cancela. Ao preço proposto de R$ 550,00, o limiar é 75,3 por 100: o DISCHARGE fica a 0,2 abaixo, o CAD-MAN acima. Ao custo microcusteado corrigido, o limiar é 85,3: **um único ensaio, o CAD-MAN, o alcança, por R$ 2,67 por paciente** — margem inferior a qualquer incerteza de parâmetro deste modelo, apoiada em um ensaio de 340 pacientes cujo braço comparador é 100% invasivo por desenho. Com `C_CATE` de R$ 772,80 (AIH), a faixa passa a R$ 510–662.

**Trata-se de outra população e de outro PICO.** A taxa do braço comparador — 89% a 100% — decorre do desenho. Não constitui alternativa automaticamente substituível à incorporação ora analisada.

O mecanismo explica a divergência de espaço econômico:

| População | Trajetória | Espaço econômico |
|---|---|---|
| Investigação não invasiva inicial | teste funcional → angiotomografia | O exame substituído custa R$ 32 (ergometria) a R$ 787 (cintilografia). O espaço depende inteiramente de qual. |
| Já indicada a cateterismo | cateterismo direto → angiotomografia → cateterismo seletivo | Há um procedimento de R$ 730 a R$ 773 que pode sair do percurso, independentemente do que veio antes. |

Registra-se que o próprio dossiê e a reanálise do NATS utilizaram o DISCHARGE — ensaio de população invasivo-primeiro — como fonte de parâmetros para o PICO de primeira linha. O desalinhamento de PICO aqui descrito já está, portanto, no relatório preliminar.

**Recomenda-se que a apreciação final considere avaliar a indicação de filtro anterior a cateterismo já indicado como pergunta separada, com critérios de elegibilidade próprios.**

### 4.6 O modelo inclui apenas o custo dos exames

Componentes não quantificados — a menor frequência de complicações maiores relacionadas ao procedimento no DISCHARGE (0,5% contra 1,9%) e a redução da permanência no CAD-MAN (mediana de 52,9 para 30,0 horas) — tenderiam a favorecer o gatekeeping. Em sentido contrário, alterações em revascularização e outros recursos a jusante podem compensar parcial ou integralmente esses ganhos. **O impacto líquido não foi estimado.**

### 4.7 Um segundo desfecho, apresentado como eficiência diagnóstica

> Esta seção apresenta **cateterismo sem DAC obstrutiva** como métrica de eficiência diagnóstica, **não utilizada como unidade do cálculo econômico**. Seus valores não entram nas seções 4.3 a 4.5, que usam cateterismo total.

O IQWiG (relatório final D22-01, 08/03/2024, por encomenda do G-BA) reporta cateterismos sem doença obstrutiva com denominador de **pacientes randomizados** (Tabela 43):

| Ensaio | Comparador | AngioTC | Controle | Evitados /100 |
|---|---|---|---|---|
| CARE-CCTA | funcional | 4/460 (0,9%) | 30/443 (6,8%) | 5,9 |
| CATCH | funcional (dor torácica aguda, SCA excluída) | 14/285 (4,9%) | 23/291 (7,9%) | 3,0 |
| SCOT-HEART | usual care (aditivo) | 20/2073 (1,0%) | 56/2073 (2,7%) | 1,7 |
| PROMISE | funcional | 170/4996 (3,4%) | 213/5007 (4,3%) | 0,9 |
| CAD-MAN | cateterismo direto | 6/167 (3,6%) | 137/162 (84,6%) | 81,0 |
| DISCHARGE | cateterismo direto | 111/1808 (6,1%) | 1260/1753 (71,9%) | 65,7 |
| Reis 2022 | cateterismo direto | 5/115 (4,3%) | 61/105 (58,1%) | 53,7 |
| CONSERVE | cateterismo direto | 24/784 (3,1%) | 439/719 (61,1%) | 58,0 |

Para o CONSERVE, os denominadores 784 e 719 correspondem aos pacientes efetivamente avaliados por estratégia, não aos randomizados (823/808); os percentuais 3,1% e 61,1% são os do abstract do ensaio, cujo denominador exato não pôde ser confirmado no texto completo. Adicionalmente: PRECISE 2,6% vs 10,2% (evitados 7,6/100); CRESCENT-II, cateterismo sem indicação classe I, 1,5% vs 7,2% (5,7/100).

Metanálise do IQWiG para os estudos de alta certeza contra métodos funcionais (CATCH e PROMISE): OR 0,77 (IC95% 0,64–0,94; p = 0,011). Contra cateterismo direto, OR de 0,01 a 0,03, sem estimativa agrupada por heterogeneidade.

**No horizonte econômico analisado nesta contribuição, o benefício mais consistente diretamente relacionado à utilização de recursos é o aumento da adequação da indicação de angiografia invasiva.** A direção é favorável à angiotomografia em todos os ensaios aqui listados, nos dois PICOs.

Esta é uma afirmação sobre utilização de recursos no curto prazo, **não uma caracterização do benefício clínico da tecnologia**. O SCOT-HEART demonstrou redução de morte coronariana e infarto não fatal em 5 anos com a angiotomografia associada ao cuidado padrão, resultado mantido na análise de 10 anos. Benefício clínico em desfechos duros e neutralidade orçamentária de curto prazo são perguntas distintas; esta contribuição responde apenas à segunda.

### 4.8 Limitação metodológica desta seção

Os Δ utilizados são diferenças aritméticas entre percentuais publicados por braço, não estimativas agrupadas de diferença absoluta. A metanálise em rede de Siontis (BMJ 2018) reporta NNT 24 (16 a 92) para teste funcional contra angiotomografia sobre taxa-base de 12,2% — equivalente a diferença absoluta de cerca de 4 por 100, coerente com a faixa aqui utilizada; a diferença de risco agrupada de Hulten (JACC 2013, +21 por 1.000) refere-se a população de emergência.

Advertências sobre fontes secundárias: a revisão de Zito (Ann Intern Med 2023) teve errata publicada (2024;177:991-2), e os intervalos indexados no PubMed permanecem desatualizados; a revisão de Hwang (Clin Cardiol 2017) contém erro de extração para SCOT-HEART — os valores 94 e 8 são exames recém-solicitados, não totais por braço (491 e 502) — e **não foi utilizada**.

---

## 5. Síntese

1. **O CNES permite, desde a Portaria SAES/MS nº 3.695/2026, identificar tomógrafos por faixa de canais.** Em 06/2026 há **432 equipamentos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS.
2. **A reclassificação está 25–27% concluída.** Os 432 são piso documentado; 2.785 equipamentos permanecem sem especificação. Recomenda-se que a apreciação final utilize a competência mais recente e registre a proporção reclassificada.
3. **79 estabelecimentos** reúnem hardware ≥64 canais, hemodinâmica co-localizada e produção coronariana documentada. **Doze UFs não possuem nenhum**; AP, PI e TO não possuem tomógrafo de ≥64 canais confirmado.
4. A investigação funcional do SUS concentra-se em **volume no teste ergométrico (76%) e em gasto na cintilografia (82%)**. Qual exame a angiotomografia substituiria na população elegível **não é identificável nos registros administrativos** — e é o parâmetro dominante do modelo.
5. **A sustentabilidade orçamentária da primeira linha depende do exame substituído.** Substituindo o mix médio, o preço de neutralidade é de R$ 139–215 e o Δ necessário ao preço proposto (R$ 550) é 49,9 por 100, doze vezes o melhor observado. Substituindo a cintilografia, é de R$ 741–817 e a estratégia é neutra em toda a faixa observada.
6. **O espaço econômico é maior em outro PICO.** Em pacientes já indicados a cateterismo, o preço de neutralidade é de R$ 482–625 independentemente do exame prévio; um ensaio (CAD-MAN) alcança o custo microcusteado corrigido por R$ 2,67. População distinta, **não intercambiável** com a apreciada. O relatório preliminar já utiliza um ensaio dessa população (DISCHARGE) para o PICO de primeira linha.
7. **O protocolo importa.** Se a incorporação especificar que a angiotomografia substitui a imagem funcional na probabilidade intermediária, o cenário econômico é favorável; se substituir a investigação inicial indistintamente, não é. Comparações indiretas entre ensaios não quantificam esse efeito, mas a especificação é o instrumento de política disponível.
8. **No horizonte econômico analisado, o benefício mais consistente é o aumento da adequação da indicação de cateterismo**, não a redução de volume. Isto não caracteriza o benefício clínico: o SCOT-HEART demonstrou redução de morte coronariana e infarto em 5 e 10 anos.
9. Não há código SIGTAP para a tecnologia; microcusteio contemporâneo da angiotomografia **e dos comparadores** é condição necessária para análise econômica simétrica.

Nada nesta contribuição se pronuncia sobre o mérito clínico da tecnologia. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária de curto prazo, nos termos em que o Comitê solicitou esclarecimento.

---

## Apêndice A — Reprodutibilidade

| Fonte | Endereço | Competência |
|---|---|---|
| CNES — equipamentos | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ/` | 06/2026 |
| SIA/SUS — produção ambulatorial | `.../SIASUS/200801_/Dados/` | 01–12/2025 |
| SIH/SUS — internações (RD) | `.../SIHSUS/200801_/Dados/` | 01–12/2025 |
| SIGTAP | `ftp://ftp2.datasus.gov.br/public/sistemas/tup/downloads/` | 08/2026 |
| População | IBGE, agregado 6579, variável 9324, período 2025 | 2025 |
| IPCA (número-índice) | IBGE, agregado 1737, variável 2266 | 12/2020 → 07/2026 |
| Portaria SAES/MS nº 3.695 | DOU nº 18, 27/01/2026, Seção 1, p. 89–90; republicação 18/05/2026 | |

**Códigos SIGTAP utilizados.** Investigação funcional: `0211020060`, `0205010016`, `0208010025`, `0208010033`, `0208010076`. Cateterismo: `0211020010`. OCI de SCC: `0902010034`, `0902010042`, `0902010050`. Angioplastia coronariana (SIH): `0406030014`, `0406030022`, `0406030030`, `0406030049`, `0406030065`, `0406030073`. Revascularização miocárdica (SIH): `0406010927`, `0406010935`, `0406010943`, `0406010951`. Tomografia (proxy de carga): grupo `0206` exceto `0206010095` (PET-CT). CNES: `TIPEQUIP=01`, `CODEQUIP` 10 (hemodinâmica), 11 e 26–30 (tomógrafos).

**Advertência sobre tabelas de conversão.** As tabelas `.cnv` distribuídas em `CNES/200508_/Auxiliar/TAB_CNES.zip` (07/2026) listam apenas o código `0111` e **não refletem o desmembramento por canais**, embora os códigos 26–30 estejam nos arquivos de dados. Análises que derivem a lista de códigos dessas tabelas excluirão silenciosamente todo equipamento reclassificado.

**Nota de processamento.** Arquivos SIA de MG, RJ, RS e SP são particionados (`PASP2501a.dbc`, `…b`, `…c`, `…d`). Rotinas que constroem nomes sem sufixo perdem silenciosamente 71 dos 395 arquivos do ano. O código enumera o diretório remoto, verifica presença das 27 UFs e distingue falha de download de arquivo vazio. Total processado: **395/395 SIA e 324/324 SIH, sem perdas**.

Leitura de `.dbc`: `datasus-dbc` e `dbfread` (Python). Regras de análise fixadas antes da extração das OCI: `REGRAS-DE-ANALISE.md`. Scripts, dados intermediários e tabelas: [inserir DOI/URL do repositório antes de submeter].

---

## Apêndice B — Ensaios randomizados utilizados

| Ensaio | Publicação | Comparador | N (int/ctrl) | Cateterismo int | Cateterismo ctrl | Janela |
|---|---|---|---|---|---|---|
| PROMISE | NEJM 2015 · PMID 25773919 | funcional-primeiro | 4996 / 5007 | 609 (12,2%) | 406 (8,1%) | 90 dias |
| SCOT-HEART | JACC 2016 · PMID 27081014; NEJM 2018 · PMID 30145934 | usual care (aditivo) | 2073 / 2073 | 17,5% (6 m); 491 (23,7%) (5 a) | 16,3%; 502 (24,2%) | 6 m; 5 a |
| CRESCENT-I | Eur Heart J 2016 · PMID 26746631 | funcional-primeiro | 239 / 108 | 29 (12,1%) | 12 (11,1%) | 1 ano |
| CRESCENT-II | JACC Img 2018 · PMID 29248657 | funcional-primeiro | 130 / 138 | 17 (13,1%) | 20 (14,5%) | 6 meses |
| CAPP | EHJ-CI 2015 · PMID 25473041 | ergometria | 243 / 245 | 66 | 51 | 1 ano |
| PRECISE | JAMA Cardiol 2023 · PMID 37610731 | usual testing | 1057 / 1046 | 135 (12,8%) | 177 (16,9%) | 11,8 meses |
| Foy (metanálise) | JAMA Intern Med 2017 · PMID 28973101 | funcional | 10 315 / 9 777 | 11,7% | 9,1% | média 18 m |
| **CAD-MAN** | BMJ 2016 · PMID 27777234 | **invasivo-primeiro** | 167 / 162 | 24 (14,4%) | 162 (100%) | índice |
| **CONSERVE** | JACC Img 2019 · PMID 30553687 | **invasivo-primeiro** | 823 / 808 | 23% | 89% | 1 ano |
| **DISCHARGE** | NEJM 2022 · PMID 35240010 | **invasivo-primeiro** | 1808 / 1753 | 404 (22,3%) | 1708 (97,4%) | manejo inicial |
| **Reis 2022** | Int J Cardiovasc Imaging 2022 · PMID 35226221 | **invasivo-primeiro** | 115 / 105 | 32 (27,8%) | 105 (100%) | ≤ 3 meses |
| CATCH | (via IQWiG D22-01) | funcional; dor torácica aguda | 285 / 291 | — | — | — |
| CARE-CCTA | (via IQWiG D22-01) | funcional | 460 / 443 | — | — | — |

Os quatro invasivo-primeiro não são comparáveis aos demais: a população já estava referenciada para procedimento invasivo e a taxa do braço controle é determinada pelo desenho. CATCH e CARE-CCTA entram apenas no desfecho de cateterismo sem DAC obstrutiva (seção 4.7).

---

## Referências

1. Brasil. Ministério da Saúde. Conitec. Relatório de Recomendação Preliminar — Angiotomografia coronariana como exame de primeira linha. CP nº 73/2026. Disponível em: gov.br/conitec.
2. Brasil. Ministério da Saúde. Portaria SAES/MS nº 3.695, de 15 de janeiro de 2026. DOU nº 18, 27 jan 2026, Seção 1, p. 89–90. Republicada em 18 mai 2026.
3. Análise de custo-efetividade da angiotomografia coronariana no SUS, em comparação com outros métodos não invasivos na suspeita de DAC estável. Arq Bras Cardiol. 2022. PMC8959029.
4. IQWiG. Coronary computed tomography angiography (with or without functional evaluation) for the diagnosis of chronic coronary heart disease. Final report D22-01, 8 Mar 2024. English extract: NBK602895. Full report (German): iqwig.de.
5. Douglas PS et al. PROMISE. N Engl J Med. 2015;372:1291-300. PMID 25773919.
6. SCOT-HEART Investigators. Lancet 2015;385:2383-91; JACC 2016;67:1759-68 (PMID 27081014); N Engl J Med. 2018;379:924-33 (PMID 30145934).
7. Lubbers M et al. CRESCENT. Eur Heart J. 2016;37:1232-43. PMID 26746631.
8. Lubbers M et al. CRESCENT-II. JACC Cardiovasc Imaging. 2018;11:1625-36. PMID 29248657.
9. McKavanagh P et al. CAPP. Eur Heart J Cardiovasc Imaging. 2015;16:441-8. PMID 25473041.
10. Douglas PS et al. PRECISE. JAMA Cardiol. 2023. PMID 37610731. Economic outcomes: Circ Cardiovasc Qual Outcomes. 2025. PMID 39895495.
11. Foy AJ et al. JAMA Intern Med. 2017;177:1623-31. PMID 28973101.
12. Dewey M et al. CAD-Man. BMJ. 2016;355:i5441. PMID 27777234.
13. Chang HJ et al. CONSERVE. JACC Cardiovasc Imaging. 2019;12:1303-12. PMID 30553687.
14. DISCHARGE Trial Group. N Engl J Med. 2022;386:1591-602. PMID 35240010.
15. Reis JF et al. Int J Cardiovasc Imaging. 2022;38:883-93. PMID 35226221.
16. Siontis GCM et al. BMJ. 2018;360:k504. PMID 29467161.
17. Zito A et al. Ann Intern Med. 2023;176:817-26. PMID 37276592. Erratum: 2024;177:991-2. PMID 38830226.
18. Hwang IC et al. Clin Cardiol. 2017;40:1129-38. PMID 28914973. [não utilizado — erro de extração para SCOT-HEART]
19. Hulten E et al. J Am Coll Cardiol. 2013;61:880-92. PMID 23395069.
20. Associação Médica Brasileira. CBHPM 2026.

---

**Autor:** [nome, titulação, afiliação, ORCID]
**Conflitos de interesse:** [declarar]
**Data:** agosto de 2026
