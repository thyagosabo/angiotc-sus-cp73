# Onde a angiotomografia coronariana gera valor no Sistema Único de Saúde? Uma análise nacional de capacidade instalada e limiar orçamentário

*Where Does Coronary CT Angiography Create Value in Brazil's Unified Health System? A National Capacity and Budget-Threshold Analysis*

**Rascunho v1 — 16/08/2026 — incorpora a resposta do coautor à v0.** Periódico-alvo decidido: **Arquivos Brasileiros de Cardiologia**, artigo original (público: SBC e Comitê; comparabilidade com os dois estudos econômicos anteriores, ambos na ABC). A versão de método — o cadastro nacional de equipamentos como instrumento de ATS — fica reservada para um segundo artigo internacional, sem competir.

Marcadores de estado por seção:

- 🟢 **PRONTA** — texto final, números reproduzidos por `analise_final.py`, revisado em duas rodadas cegas
- 🟡 **PRÉVIA** — texto completo, mas escrito ou reescrito na v1 e ainda **não** submetido à terceira rodada cega; ou dependente de julgamento clínico do coautor
- 🔴 **A FAZER** — só o esqueleto

Autoria, ordem e afiliações: a definir. Conflitos de interesse: a declarar.

**O que mudou de v0 para v1** (resposta do coautor, 16/08/2026): (1) sexto cenário **"adoção aditiva (sem protocolo)"**, C_substituído = 0, na Tabela 3 e na Tabela 4, ancorando a recomendação (i); (2) **estratificação por probabilidade pré-teste como tese**, não como sensibilidade — comparador realista declarado por faixa (baixa: nenhum exame ou ergometria; intermediária: ecocardiografia ou cintilografia), Tabela 4 nova, débito de revascularização aplicado a todos os cenários; (3) 4.5 com parágrafo próprio confrontando o estudo da saúde suplementar (ABC 2026); (4) microcusteio declarado como limitação e agenda, com desenho mínimo; (5) resumo no formato estruturado da ABC; (6) introdução e conclusão em texto completo. Nenhuma equação, código, janela ou desfecho mudou (`REGRAS-DE-ANALISE.md`, emendas 7–8). **v1.1 (mesmo dia, após a terceira rodada cega):** SCOT-HEART com os dados primários (409 vs 401 em 20 meses; 491 vs 502 em 5 anos; revascularização 233 vs 201 e 279 vs 267) em vez de um valor de 6 meses sem proveniência; CONSERVE com revascularização (R$ 868); Foy pareado 13-com-13 (R$ 560); "cenário mais provável" reenquadrado como cenário de referência com código sem protocolo, declarado como juízo; "nenhum preço" → "nenhum preço plausível (teto R$ 30–62)"; "plausivelmente sustentável" → "zona de incerteza"; cotas anuais reancoradas no volume de cada exame; US$ 462 (não £); ética com incisos II, III e V.

---

## Resumo

🟡 **PRÉVIA** — formato ABC (Fundamento/Objetivos/Métodos/Resultados/Conclusões); 250 palavras (limite 250).

**Fundamento:** A Conitec recomendou preliminarmente contra a angiotomografia coronariana (AngioTC) como primeira linha na doença coronariana estável de probabilidade pré-teste baixa ou intermediária, citando capacidade instalada e impacto orçamentário.

**Objetivos:** Caracterizar a capacidade tomográfica do SUS compatível com AngioTC e as condições de posicionamento no percurso diagnóstico em que a tecnologia é orçamentariamente neutra.

**Métodos:** Análise nacional sobre bases públicas (CNES, SIA/SUS, SIH/SUS, SIGTAP); capacidade por número de canais após a Portaria SAES/MS 3.695/2026. Análise de limiar: Δ de cateterismo necessário para neutralidade por preço, em dois PICOs (primeira linha; filtro pré-cateterismo), seis cenários de exame substituído (inclusive adoção aditiva) e por estrato de probabilidade pré-teste, com e sem revascularização; Δ de 10 ensaios randomizados e uma metanálise.

**Resultados:** 432 tomógrafos ≥64 canais em 315 estabelecimentos (piso; 74,6% ainda sob código genérico); 79 reúnem hardware, hemodinâmica e produção coronariana, 12 UFs sem nenhum; 787.954 episódios funcionais/ano, R$ 185,46 cada, 76% ergometria. Sem substituição, nenhum preço plausível é neutro (teto R$ 30). Na probabilidade baixa (comparador: nenhum exame ou ergometria), R$ 550 está fora do alcance; na intermediária, na zona de incerteza só substituindo cintilografia (R$ 458–560 com revascularização); no filtro pré-cateterismo, R$ 482–625 (R$ 841–868 com revascularização).

**Conclusões:** A sustentabilidade depende do exame substituído, da revascularização induzida e da posição no percurso — parâmetros que os registros não identificam, mas o protocolo define. A tecnologia é expansiva na probabilidade baixa, incerta na intermediária-com-cintilografia e tem espaço no filtro pré-cateterismo: a estratificação da Diretriz SBC de Síndrome Coronariana Crônica 2025, não a do PICO submetido.

**Palavras-chave (DeCS):** Angiografia por Tomografia Computadorizada; Doença da Artéria Coronariana; Avaliação da Tecnologia Biomédica; Custos e Análise de Custo; Sistema Único de Saúde.

---

## 1. Introdução

🟡 **PRÉVIA** — texto completo; as quatro avaliações econômicas brasileiras citadas foram verificadas em texto integral (16/08/2026).

A investigação da dor torácica estável é uma porta de entrada de alto volume: no SUS, em 2025, foram 787.954 episódios de investigação funcional não invasiva, três quartos deles por teste ergométrico. Nas duas últimas décadas, a avaliação anatômica por angiotomografia coronariana (AngioTC) acumulou evidência de ensaios randomizados de estratégia — SCOT-HEART, PROMISE, DISCHARGE — e alcançou recomendação de classe I nas diretrizes internacionais (NICE CG95, 2016; AHA/ACC 2021; ESC 2024) e brasileiras (SBC TC/RM 2024; SBC SCC 2025). Com uma exceção (NICE), todas estratificam a indicação por probabilidade pré-teste — e a diretriz brasileira mais recente distingue a probabilidade baixa (IIb-B) da intermediária (I-A).

No SUS, entretanto, não há código para a AngioTC na tabela de procedimentos (SIGTAP); a produção que porventura exista é registrada sob código genérico de tomografia ou não é registrada, e é administrativamente invisível. Em 2026 a Sociedade Brasileira de Cardiologia submeteu à Conitec pedido de incorporação como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária. A recomendação preliminar, de 3 de julho de 2026, foi desfavorável, e o Comitê listou como pontos a esclarecer em consulta pública a capacidade instalada, a necessidade de aquisição de equipamentos, a delimitação da população elegível, os comparadores e o impacto real sobre cateterismos e testes funcionais.

As avaliações econômicas brasileiras disponíveis — dois modelos de custo-efetividade na perspectiva do sistema público [30,31]; a análise de custo-efetividade publicada nesta revista, também na perspectiva do SUS, com a AngioTC microcusteada e os comparadores a preços de tabela [3]; e a análise na saúde suplementar, também nesta revista, com preços daquele sistema e a angiografia invasiva como único comparador [20] — não modelam a capacidade instalada nem a dependência do resultado em relação ao **posicionamento** da tecnologia: o que ela substitui, e em que ponto do percurso entra. Também não podiam contar tomógrafos por número de canais: até janeiro de 2026 o cadastro nacional registrava todos sob um único código, e a Portaria SAES/MS nº 3.695/2026, que o desmembrou por canais, ainda não havia sido explorada como instrumento de avaliação de tecnologia.

Este estudo responde às perguntas do Comitê com dados públicos e método reproduzível: caracteriza a capacidade tomográfica do SUS compatível com AngioTC e determina, por posição no percurso e por estrato de probabilidade pré-teste, sob que condições a tecnologia atinge neutralidade orçamentária.

---

## 2. Métodos

### 2.1 Desenho e perspectiva

🟢 **PRONTA**

Análise nacional model-based, perspectiva do SUS como pagador público, horizonte de curto prazo (episódio diagnóstico e desfechos invasivos imediatos). Não se modela prognóstico de longo prazo. Regras de análise fixadas antes da extração dos dados de OCI (`REGRAS-DE-ANALISE.md`, repositório); duas apresentações acrescentadas após a v0 estão declaradas como emendas não pré-registradas (idem, emendas 7–8). Aprovação ética: não se aplica — dados públicos de acesso irrestrito (Lei 12.527/2011), agregados (CNES, SIA) ou desidentificados (SIH-RD), sem possibilidade de identificação individual (Resolução CNS 510/2016, art. 1º, parágrafo único, incisos II, III e V; formulário da ABC: "não se aplica a artigos cuja pesquisa não envolve seres humanos"); carta de dispensa do CEP a obter *[coautor]*.

### 2.2 Fontes de dados

🟢 **PRONTA**

| Fonte | Conteúdo | Competência |
|---|---|---|
| CNES — arquivos `EQ` | equipamentos por estabelecimento, tipo, código, disponibilidade ao SUS, em uso | 06/2026 |
| SIA/SUS — arquivos `PA` | produção ambulatorial por estabelecimento e procedimento, quantidade e valor aprovados | 01–12/2025 |
| SIH/SUS — arquivos `RD` | internações por estabelecimento e procedimento principal, valor | 01–12/2025 |
| SIGTAP | tabela de procedimentos, valores | 08/2026 |
| IBGE | população por UF (agregado 6579); IPCA (agregado 1737) | 2025; 12/2020→07/2026 |

Acesso por FTP público (`ftp.datasus.gov.br`), arquivos `.dbc` lidos com `datasus-dbc` e `dbfread`. Os arquivos SIA de MG, RJ, RS e SP são particionados; a rotina enumera o diretório remoto em vez de construir nomes, verifica presença das 27 UFs e distingue falha de download de arquivo vazio. Processados 395/395 arquivos SIA e 324/324 SIH.

### 2.3 Capacidade instalada

🟢 **PRONTA**

A Portaria SAES/MS nº 3.695 (15/01/2026; DOU 27/01/2026; republicada 18/05/2026) desmembrou o código genérico de tomógrafo (`11`) em categorias por canais: `26` (4), `27` (16), `28` (32), `29` (64), `30` (128). Equipamentos com `IND_SUS=1` e `QT_USO>0`, `TIPEQUIP=01`, foram classificados em três camadas: compatível confirmado (29+30), incompatível confirmado (26–28), especificação não declarada (11). As tabelas de conversão `.cnv` distribuídas com os arquivos não refletem a portaria e foram ignoradas; os códigos foram enumerados a partir dos microdados.

Estratos de prontidão: interseção do estrato ≥64 canais com (a) sala de hemodinâmica no mesmo CNES (`CODEQUIP=10`) e (b) produção coronariana invasiva no SIH 2025 (angioplastia coronariana `0406030014/22/30/49/65/73` ou revascularização miocárdica `0406010927/35/43/51`). Densidade por milhão de habitantes; desigualdade por coeficiente de variação e Gini ponderado por população.

### 2.4 Cenário atual: unidade de análise

🟢 **PRONTA**

Investigação funcional: `0211020060` (teste ergométrico), `0205010016` (eco de estresse), `0208010025` e `0208010033` (cintilografia de perfusão, estresse e repouso), `0208010076` (cintilografia de câmaras). Cateterismo: `0211020010`. A cintilografia de perfusão é registrada em dois códigos que correspondem a etapas de um exame; episódios foram contados pelo código de estresse. Ordens de Cuidado Integrado de síndrome coronariana crônica (`0902010034/42/50`) tratadas como episódio próprio; componentes com valor zerado dentro de OCI não somados. Custo por episódio = valor aprovado ÷ episódios. Todos os valores são preços de tabela, não custos de produção.

### 2.5 Análise de limiar

🟢 **PRONTA** (equações, parâmetros) · 🟡 (sexto cenário e estratificação, acrescentados na v1)

O SIA não possui identificador de paciente; razões entre contagens agregadas de cateterismos e testes não são probabilidades condicionais. Em vez de estimar cateterismos evitados, calculou-se o Δ de cateterismo total por 100 pacientes necessário para neutralidade a cada preço:

- Primeira linha (substituição de episódio funcional): `P = C_substituído + (Δ_CATE/100)·C_CATE − (Δ_revasc/100)·C_revasc`
- Gatekeeping (filtro antes de cateterismo já indicado; custo prévio comum aos braços cancela): `P = (Δ_CATE/100)·C_CATE − (Δ_revasc/100)·C_revasc`

Com `C_CATE = R$ 730,14` (SIA 2025; sensibilidade a R$ 772,80, valor AIH), `C_revasc` do SIH 2025 (R$ 7.713 angioplastia; R$ 25.904 CRM). Preços de referência: R$ 196,41 (TC de tórax + contraste, proxy), R$ 550,00 (proposto pelo demandante), R$ 622,54 (microcusteio de Carmo et al. [3] corrigido pelo IPCA de 12/2020 a 07/2026, ×1,3771 — o ano-base não é explicitado no artigo, e 12/2020 é o limite otimista), R$ 1.311,95 (valor da AngioTC na saúde suplementar usado por Shiozaki et al. [20], "referência da ANS", apresentado como 100% da CBHPM).

`C_substituído` em **seis cenários**: **adoção aditiva (sem protocolo)** — a AngioTC somada ao percurso atual, nada substituído, `C = 0`, algebricamente a equação de gatekeeping com o Δ dos ensaios de primeira linha (o desenho do SCOT-HEART); mix médio do SIA; mix do NATS como publicado (cintilografia por um código) e por episódio; ecocardiografia de estresse; cintilografia. **Por estrato de probabilidade pré-teste**, o comparador realista foi declarado como premissa a partir das diretrizes (seção 4.2) e do julgamento clínico dos autores: probabilidade baixa → nenhum exame (diferir, ajustar probabilidade, escore de cálcio — isto é, adoção aditiva) ou teste ergométrico; intermediária → ecocardiografia de estresse ou cintilografia de perfusão (ou o percurso do NATS, que as mistura); o mix médio do SIA representa o PICO como submetido, sem estratificar. O débito de revascularização (PRECISE, Foy 2017) foi aplicado a todos os cenários de primeira linha como envelope. Cotas anuais de ordem de grandeza: todos os episódios funcionais (ou todos os cateterismos, no gatekeeping) a R$ 550, no ponto médio da faixa de Δ observada.

### 2.6 Δ observados nos ensaios

🟢 **PRONTA**

Cateterismo total por braço randomizado, extraído das publicações primárias (Apêndice B): PROMISE, CRESCENT-I, CRESCENT-II, CAPP, PRECISE, Foy 2017 (primeira linha); CAD-MAN, CONSERVE, DISCHARGE, Reis 2022 (gatekeeping); SCOT-HEART (aditivo). Cateterismo sem DAC obstrutiva (IQWiG D22-01, Tabela 43) apresentado separadamente como eficiência diagnóstica, fora do cálculo econômico. Revascularização por braço: PRECISE, Foy 2017 (13 ensaios, pareada com o Δ dos mesmos 13), SCOT-HEART (para o cenário aditivo), DISCHARGE e CONSERVE; sem desagregação angioplastia/cirurgia, valorada como angioplastia. Ao todo, 10 ensaios e 1 metanálise fornecem Δ; CATCH e CARE-CCTA (12 estudos) só entram na eficiência diagnóstica.

### 2.7 Reprodutibilidade

🟢 **PRONTA**

`analise_final.py` regenera todas as tabelas a partir dos microdados versionados — inclusive as cotas anuais e a tabela por estrato (`output/out-limiar-por-estrato.csv`); recusa-se a rodar com cobertura parcial. Repositório: `[URL/DOI]`. Relato conforme CHEERS 2022 [33] no que se aplica a análise de limiar (a ABC adota CHEERS para avaliações econômicas) *[checklist a anexar]*.

---

## 3. Resultados

### 3.1 Capacidade instalada

🟢 **PRONTA** *(tabela por UF em `output/out-capacidade-canais-uf.csv`; texto = seções 2.1–2.4 da contribuição)*

**Tabela 1 — Parque tomográfico disponível ao SUS por camada de especificação e estratos de prontidão (CNES 06/2026).**

| Camada / estrato | Estabelecimentos | Equipamentos |
|---|---|---|
| Compatível confirmado (≥64 canais; códigos 29+30) | **315** | **432** (293 de 64; 139 de 128) |
| Incompatível confirmado (<64; códigos 26–28) | 672 | 736 |
| Especificação não declarada (código 11) | 2.534 | 2.785 |
| Parque total | 3.395 | 3.953 |
| ≥64 + hemodinâmica no mesmo CNES | 114 | — |
| ≥64 + produção coronariana invasiva em 2025 | 96 | — |
| **≥64 + hemodinâmica + produção coronariana** | **79** | — |

Reclassificação: 910 estabelecimentos (26,8%) com ≥1 equipamento reclassificado, 861 (25,4%) integralmente migrados; os 432 são piso documentado, não estimativa da capacidade real. Densidade 2,02 equipamentos ≥64 por milhão de habitantes; AP, PI e TO sem nenhum ≥64 confirmado; doze UFs sem estabelecimento no estrato pronto (AC, AL, AM, AP, GO, MT, PA, PI, RO, RR, SE, TO). A desigualdade é maior sobre o hardware compatível do que sobre o parque agregado: CV 0,86 vs 0,32; Gini ponderado 0,30 vs 0,14. Carga do parque: 13,4 milhões de exames de TC em 2025, cerca de 3.400 por equipamento.

**Figura 1** `[A FAZER]`: mapa por UF, densidade ≥64 canais e estrato pronto.

### 3.2 Cenário atual

🟢 **PRONTA** *(texto = seções 3.1–3.4 da contribuição)*

**Tabela 2 — Investigação funcional e procedimentos invasivos no SUS, 2025.**

| Item | Volume | Valor aprovado | Por unidade |
|---|---|---|---|
| Episódios de investigação funcional | 787.954 | R$ 146,1 mi | R$ 185,46 |
| — teste ergométrico | 76% do volume | 13% do gasto | R$ 32,20 |
| — cintilografia de perfusão (episódio = estresse + repouso) | 19% do volume | 82% do gasto | R$ 786,83 |
| — ecocardiografia de estresse | — | — | R$ 196,39 |
| OCI de síndrome coronariana crônica | 7.616 (0,96%) | — | 148 estabelecimentos |
| Cateterismo | 163.803 | R$ 119,6 mi | R$ 730,14 |
| Angioplastia coronariana (SIH) | 133.934 | R$ 1.033 mi | R$ 7.713 (268 estab.) |
| Revascularização cirúrgica (SIH) | 23.290 | R$ 603 mi | R$ 25.904 (230 estab.) |

Não há código SIGTAP para AngioTC; o código de contraste para TC tem faturamento zero. Contar procedimentos em vez de episódios inflaria o denominador funcional em 19% (cintilografia em dois códigos).

### 3.3 Análise de limiar: Δ necessário por preço e por cenário

🟢 **PRONTA** (cinco cenários) · 🟡 (sexto cenário) *(texto = seções 4.3–4.6 da contribuição)*

**Tabela 3 — Δ de cateterismo total por 100 pacientes necessário para neutralidade, por preço da AngioTC e por exame substituído (só exames e cateterismo).**

| Preço | Natureza | adoção aditiva | mix SIA | NATS publicado | NATS por episódio | eco de estresse | cintilografia |
|---|---|---|---|---|---|---|---|
| R$ 196,41 | TC tórax + contraste, proxy | 26,9 | 1,5 | já neutro | já neutro | 0,0 | já neutro |
| **R$ 550,00** | **proposto** | **75,3** | **49,9** | 31,9 | **3,6** | 48,4 | já neutro |
| R$ 622,54 | microcusteio 2022 corrigido | 85,3 | 59,9 | 41,9 | 13,5 | 58,4 | já neutro |
| R$ 1.311,95 | saúde suplementar (Shiozaki 2025) | 179,7 | 154,3 | 136,3 | 107,9 | 152,8 | 71,9 |

Nos ensaios de primeira linha o Δ observado foi de −6,3 (CAPP) a +4,1 (PRECISE) por 100; nos invasivo-primeiro, de 66,0 (CONSERVE) a 85,6 (CAD-MAN). Na adoção aditiva o Δ exigido a R$ 550 (75,3) é numericamente o limiar do gatekeeping — a equação é a mesma; a diferença é que 75 por 100 é o que o DISCHARGE observou em pacientes já indicados a cateterismo, e 4,1 é o melhor já observado em primeira linha. Ao preço da saúde suplementar, substituindo o mix médio, seriam necessárias mais angiografias evitadas do que pacientes investigados. Preços de neutralidade por cenário e gatekeeping: Tabela 4. **Figura 2** `[refazer para publicação com os seis cenários]`: preço da AngioTC × Δ, duas retas, dez ensaios e uma metanálise.

### 3.4 Limiar por estrato de probabilidade pré-teste e posição no percurso

🟡 **PRÉVIA** — números reproduzidos (`analise_final.py` §4.9); texto novo na v1. **É a tabela central do artigo.**

**Tabela 4 — Preço de neutralidade da AngioTC por estrato de probabilidade pré-teste, comparador realista (premissa declarada) e posição no percurso; Δ de cateterismo total observado nos ensaios (−6,3 a +4,1 em primeira linha), com e sem revascularização induzida (PRECISE +4,0/100; Foy 2017, 13 ensaios, +2,7/100 pareada com Δ −2,6; SCOT-HEART +1,5/+0,6 por 100; DISCHARGE −3,8/100; CONSERVE −5,0/100).**

| Estrato | Comparador (premissa) | C_substituído | Neutralidade, só exames + cateterismo | Neutralidade com revascularização | Δ exigido a R$ 550 (só exames) |
|---|---|---|---|---|---|
| Baixa | nenhum exame (diferir/ajustar PPT/escore de cálcio) → **adoção aditiva** | R$ 0 | **R$ −46 a +30** (SCOT-HEART: R$ −3 a +4) | R$ −122 a −41 (revasc. do próprio SCOT-HEART) | 75,3 |
| Baixa | teste ergométrico | R$ 32,20 | R$ −14 a +62 | R$ −297 a −195 | 70,9 |
| Não estratificado (PICO submetido) | mix médio do SIA | R$ 185,46 | R$ 139 a 215 | R$ −144 a −42 | 49,9 |
| Intermediária | ecocardiografia de estresse | R$ 196,39 | R$ 150 a 226 | R$ −133 a −31 | 48,4 |
| Intermediária | percurso do NATS por episódio | R$ 523,81 | R$ 477 a 554 | R$ 195 a 297 | 3,6 |
| Intermediária | cintilografia de perfusão | R$ 786,83 | R$ 741 a 817 | **R$ 458 a 560** | já neutro |
| Já indicado a cateterismo (outro PICO) | cateterismo direto — CONSERVE / Reis 2022 / DISCHARGE / CAD-MAN | cancela | R$ 482 / 527 / 548 / 625 | **R$ 841** (DISCHARGE) / **R$ 868** (CONSERVE) | 75,3 |

Notas: mix do NATS como publicado (cintilografia por um código, R$ 316,76): R$ 270–347 só com exames. Débito de revascularização PRECISE/Foy aplicado como envelope aos cenários de substituição — escala com a prevalência de doença e tende a superestimar o débito na probabilidade baixa, sem alterar o sinal; para a adoção aditiva usa-se o SCOT-HEART. Para o diferimento propriamente dito o contrafactual não contém cateterismo diagnóstico (Δ ≤ 0; teto R$ 0). Débitos incluem a parcela cirúrgica (PRECISE); créditos do DISCHARGE e do CONSERVE valorados só como angioplastia — conservador contra o gatekeeping. Com `C_CATE` = R$ 772,80 (AIH), o gatekeeping vai a R$ 510–662.

Três resultados. **Na probabilidade baixa, nenhum preço plausível fecha**: com o comparador que as diretrizes indicam — nenhum exame ou ergometria —, o teto de neutralidade é R$ 30 a R$ 62 só com exames e negativo com revascularização, abaixo do menor preço de referência (R$ 196); sem substituição, mesmo gratuita a AngioTC só é neutra se não induzir cateterismos, e o melhor Δ de primeira linha paga R$ 30. **Na intermediária, o resultado depende de qual imagem funcional sai do percurso**: substituindo ecocardiografia de estresse, R$ 550 está fora do alcance; substituindo cintilografia, dentro da zona de incerteza mesmo com a revascularização observada (R$ 458–560; no par PRECISE, R$ 550 excede a neutralidade em R$ 92) — nicho de no máximo 151.784 episódios/ano, 19% do volume; o percurso misto do NATS, que sem revascularização cercava R$ 550, cai a R$ 195–297 quando ela entra. A premissa é normativa: se na prática do SUS o comparador da probabilidade intermediária for a ergometria (76% de todo o volume; IIb-B na ESC 2024 quando a imagem não está disponível), o resultado colapsa no da baixa — o resultado intermediário exige protocolo que nomeie o exame deslocado, não só a faixa. **O PICO como submetido — a média não estratificada — é puxado para o estrato baixo** (R$ 139–215, próximo da ecocardiografia e longe da cintilografia), porque três quartos do volume atual são ergometria. No filtro antes de cateterismo indicado (outro PICO), R$ 482–625, e R$ 841 (DISCHARGE) a R$ 868 (CONSERVE) com a menor revascularização observada.

### 3.5 Eficiência diagnóstica

🟢 **PRONTA** *(= seção 4.8 da contribuição; IQWiG Tabela 43)*

Cateterismo sem DAC obstrutiva por 100 randomizados, evitados com AngioTC: CARE-CCTA 5,9; CATCH 3,0; SCOT-HEART 1,7; PROMISE 0,9 (funcionais); CAD-MAN 81,0; DISCHARGE 65,7; Reis 2022 53,7; CONSERVE 58,0ᵃ (invasivo-primeiro). Metanálise IQWiG contra funcionais (CATCH, PROMISE): OR 0,77 (IC95% 0,64–0,94). Direção favorável à AngioTC em todos os ensaios, nos dois PICOs; não entra no cálculo econômico. ᵃ ressalva de fonte (denominadores da Tabela 43, não randomizados).

### 3.6 Ordem de grandeza do impacto anual (cotas)

🟡 **PRÉVIA** — números reproduzidos (`analise_final.py` §4.10); texto novo na v1.

Não se estima a população elegível. Como ordem de grandeza, a R$ 550 e no ponto médio da faixa de Δ observada, o impacto líquido anual **por 100 mil pacientes** seria de +R$ 55,8 mi na adoção aditiva, +R$ 52,6 mi substituindo ergometria, +R$ 37,3 mi o mix médio, +R$ 36,2 mi a ecocardiografia, +R$ 3,4 mi o percurso do NATS por episódio, −R$ 22,9 mi a cintilografia só com exames e +R$ 4,1 mi a cintilografia com revascularização; no gatekeeping, de +R$ 6,8 mi (CONSERVE) a −R$ 7,5 mi (CAD-MAN) só com exames, e −R$ 29,1 mi no DISCHARGE com revascularização. Ancorando cada cenário no volume que ele pode substituir em 2025: **+R$ 440 mi/ano se a AngioTC fosse somada a todos os 787.954 episódios funcionais** (adoção aditiva) e +R$ 294 mi se os substituísse ao mix médio; +R$ 315 mi sobre as 598.695 ergometrias; +R$ 12 mi sobre as 33.766 ecocardiografias; −R$ 35 mi (só exames) ou +R$ 6 mi (com revascularização) sobre as 151.784 cintilografias; e, sobre os 163.803 cateterismos, +R$ 11 mi (CONSERVE) a **−R$ 48 mi** (DISCHARGE com revascularização). São cotas de ordem de grandeza; a população elegível é uma fração não identificável dos denominadores.

### 3.7 Análise de sensibilidade

🔴 **A FAZER**: tornado univariado sobre C_substituído, C_CATE (730 vs 773), Δ_CATE (faixa observada), Δ_revasc, C_revasc; gerado por `analise_final.py`. Os cenários discretos da Tabela 4 já cobrem C_substituído e Δ_revasc; falta a figura (**Figura 3**).

---

## 4. Discussão

### 4.1 Achado principal

🟡 **PRÉVIA** — reescrito na v1 em torno da estratificação.

Uma mesma tecnologia, ao mesmo preço, é orçamentariamente expansiva ou fica na zona de incerteza dependendo de onde entra no percurso e do que substitui — e nenhum dos três parâmetros que decidem isso é identificável nos registros administrativos brasileiros. O que os registros não dizem, porém, as diretrizes dizem: em cada faixa de probabilidade pré-teste há um comparador realista, e declará-lo como premissa converte a limitação em resultado. Na probabilidade baixa, onde as diretrizes recomendam diferir, ajustar a probabilidade ou usar escore de cálcio, ou onde o SUS hoje faz um teste ergométrico de R$ 32, a AngioTC não substitui nada de valor — e nenhum preço plausível a torna neutra (teto R$ 30 a R$ 62). Na intermediária, onde o comparador é a imagem funcional, o resultado se decide pelo que sai do percurso: a ecocardiografia de estresse, a R$ 196, não financia a troca; a cintilografia, a R$ 787, financia — até que a revascularização adicional observada nos ensaios (débito de R$ 208 a R$ 359 por paciente, 44% do preço de neutralidade de R$ 817 e mais do que a margem de R$ 267 acima de R$ 550) a traga a R$ 458–560, dentro da zona de incerteza, não acima dela. Filtrando cateterismos já indicados, o espaço econômico é maior e o DISCHARGE, com a menor revascularização observada, cruza o limiar com folga.

O sexto cenário é o mais desfavorável e, a juízo dos autores, o mais provável se a incorporação criar o código sem protocolo vinculante de posicionamento. Com 787.954 episódios funcionais por ano em curso e nada que os retire do percurso, a AngioTC tende a entrar somada ao teste ergométrico, não no lugar dele — o desenho do SCOT-HEART transposto para a rotina; nos próprios ensaios de substituição, 3% a 13% dos pacientes fizeram testes funcionais subsequentes (PRECISE, CRESCENT-II). É um juízo sobre implementação, não uma medida: o SIA não registra sobreposição de testes por paciente. Nesse caso `C_substituído = 0`, o preço de neutralidade é de R$ −46 a +30 (R$ −3 a +4 com o Δ do próprio SCOT-HEART; R$ −122 a −41 com a sua revascularização) e a tecnologia é expansiva por construção, independentemente do preço negociado. Isso não enfraquece o argumento a favor da AngioTC; localiza-o: a condição de sustentabilidade não é o preço, é a especificação do que sai do percurso.

A capacidade instalada, por sua vez, deixou de ser desconhecida: pela primeira vez o cadastro nacional permite contar tomógrafos por canais, e o resultado — 432 equipamentos ≥64 canais como piso, 79 estabelecimentos prontos, doze UFs sem nenhum — é ao mesmo tempo maior do que a ausência de dado sugeria e mais desigual do que o parque agregado.

### 4.2 Diretrizes: o PICO submetido versus a estratificação recomendada

🟢 **PRONTA** — cinco diretrizes verificadas em texto integral (SBC 2024, SBC 2025, ESC 2024, AHA/ACC 2021, NICE CG95); nenhuma diretriz AHA/ACC de 2025–26 sobre dor torácica ou doença coronariana crônica existe — a de 2023 remete explicitamente à de 2021.

Nenhuma das cinco diretrizes posiciona a angiotomografia como primeira linha uniforme na faixa "baixa ou intermediária" — exceto o NICE, que a oferece a toda angina típica ou atípica sem estratificar por probabilidade e, ao fazê-lo, coloca a imagem funcional em segunda linha e o cateterismo em terceira, o modelo mais puro de gatekeeping. As demais estratificam, e convergem:

**Tabela 5 — Posição da AngioTC nas diretrizes vigentes, por probabilidade pré-teste.**

| Diretriz | Probabilidade baixa | Intermediária | Alta | Filtro antes de cateterismo |
|---|---|---|---|---|
| **SBC SCC 2025** (Arq Bras Cardiol 2025;122(9)) | primeira opção **IIb-B**; "ajustar PPT ou angiotomografia" | exame inicial **I-A**; "prova funcional ou angiotomografia" | prova funcional (I-B para eco, SPECT/PET, RMC) | "alternativa ao estudo invasivo" após teste funcional conflitante (IIa-B baixa; I-A intermediária) |
| **SBC TC/RM 2024** (Arq Bras Cardiol 2024;121(9)) | opção inicial **I-A** (baixa e intermediária, sem distinção) | opção inicial **I-A** | **III-C** | **I-A** — "alternativa … com probabilidade pré-teste intermediária e indicação de cinecoronariografia invasiva" |
| **ESC 2024** (Eur Heart J 2024;45:3415) | ≤5% diferir (IIa-B); 5–15% escore de cálcio (IIa-B) | >5–50%: CCTA **preferida** para excluir DAC (I-B), diagnóstico e risco (I-A); >15–85%: imagem funcional (I-B), "melhor poder de confirmação" | >85%: cateterismo direto (I-C) | sequência da Tabela 13: CCTA → funcional se incerta → cateterismo se ainda incerto (I-B) |
| **AHA/ACC 2021** (Circulation 2021;144:e368) | diferir/escore de cálcio/ergometria (1 B-NR; 2a) | risco intermediário-alto: CCTA **1-A** e imagem de estresse **1 B-R** co-iguais; CCTA preferível <65 anos, estresse ≥65 | — | "candidatos a cateterismo eletivo podem ser triados com segurança por CCTA ou teste de estresse" |
| **NICE CG95** (2016) | CCTA ≥64 cortes a toda angina típica/atípica, sem PPT | idem | idem | funcional 2ª linha se CCTA incerta; cateterismo 3ª linha |

Três observações decorrem para o PICO em apreciação.

**Primeira: a estratificação por probabilidade é a regra, e a diretriz da própria sociedade demandante é a mais conservadora na faixa baixa.** A SBC 2024 (TC/RM) dá I-A para "baixa ou intermediária" sem distinção — o texto do PICO submetido reproduz essa formulação. A SBC 2025 (SCC), posterior e específica para a condição, separa: IIb-B na baixa, I-A na intermediária, e no algoritmo coloca a angiotomografia como *alternativa* à prova funcional ("prova funcional ou angiotomografia"), não como substituta. A ESC 2024 é a única que usa a palavra "preferida" — e restrita a >5–50%, com imagem funcional recomendada a partir de >15% pelo maior poder de confirmação. Ou seja: a faixa em que a angiotomografia é preferencial é estreita e sobreposta à faixa em que a imagem funcional também é classe I.

**Segunda: a análise econômica depende de qual exame a angiotomografia substitui — e as diretrizes dizem qual.** Na probabilidade intermediária, ela substituiria a prova funcional que o serviço realizaria (SBC 2025), a imagem funcional (ESC, AHA/ACC) ou nada, sendo co-igual. Na baixa, substituiria "ajustar PPT" (SBC 2025), diferimento ou escore de cálcio (ESC, AHA/ACC) — isto é, **em muitos casos substituiria não testar**, o cenário economicamente menos favorável possível, pois C_substituído tende a zero. É essa a premissa declarada na Tabela 4: "primeira linha em baixa e intermediária" agrega dois cenários econômicos opostos.

**Terceira: o gatekeeping antes de cateterismo já indicado é endossado explicitamente por quatro das cinco diretrizes** — SBC 2024 (I-A), ESC 2024 (sequência da Tabela 13), AHA/ACC 2021 (texto), NICE (estrutura) — e implicitamente pela SBC 2025 ("alternativa ao estudo invasivo"). É a indicação em que esta análise encontrou maior espaço econômico, e é uma indicação com respaldo de diretriz — mas não é a que está sendo requerida.

Sobre equipamento: apenas o NICE (na própria recomendação, "64-slice or above") e a ESC (no texto, "64-slice technology or above … must be considered a pre-requisite") fixam piso de detectores. Nenhuma diretriz brasileira o faz nas tabelas de recomendação. A análise de capacidade adotou o piso de 64 canais por coerência com as diretrizes internacionais e com o relatório preliminar, que transcreve a recomendação do NICE.

**Implicação para a incorporação.** As diretrizes fornecem o protocolo que a análise econômica pede: estratificar por probabilidade pré-teste, com a angiotomografia como opção classe I na intermediária e como filtro antes de cateterismo já indicado, e com critérios explícitos na baixa (onde a SBC 2025 e a ESC convergem em "avaliar antes de testar"). Uma incorporação que espelhe essa estratificação — em vez da faixa agregada "baixa ou intermediária" — alinha o PICO à diretriz da própria sociedade demandante e às três internacionais, e restringe o cenário econômico desfavorável (substituição de ergometria ou de "não testar") por desenho.

### 4.3 O desalinhamento de PICO no processo

🟡 **PRÉVIA**

O dossiê e a reanálise do NATS utilizam o DISCHARGE, ensaio de população já referenciada a cateterismo, como fonte de parâmetros para o PICO de primeira linha. O NATS precifica a cintilografia por um único código (R$ 408,52), contra dois na prática. Ambos os desalinhamentos estão no relatório preliminar e alteram o resultado em ordem de grandeza. Um terceiro está implícito: nenhum dos documentos especifica o que a AngioTC substitui — e, sem especificação, o cenário de referência é o aditivo (Tabela 4, primeira linha).

### 4.4 Capacidade: o que o cadastro responde e o que não responde

🟡 **PRÉVIA**

Pela primeira vez o CNES permite contar tomógrafos por canais — mas 74,6% dos estabelecimentos (70,5% dos equipamentos) ainda não migraram. Os 432 são piso. O estrato de 79 é o conjunto de maior plausibilidade de implantação sem aquisição de tomógrafo, mas software cardíaco, gating, injetora e leitores treinados não constam do cadastro; a capacidade em vagas depende da carga atual (~3.400 exames/equipamento/ano) e não foi estimada. A desigualdade sobre hardware compatível é maior que sobre o parque agregado, e doze UFs não têm nenhum estabelecimento pronto — a incorporação sem estratégia regional consolidaria a desigualdade que o dado revela. Recomendação administrativa: apreciação sobre a competência mais recente, com a proporção reclassificada declarada, e instrumentos para completar a reclassificação.

### 4.5 Comparação com a literatura econômica

🟡 **PRÉVIA** — texto completo; citação e parâmetros do estudo da saúde suplementar aguardam verificação em texto integral.

A única análise econômica de ensaio no cenário de substituição de imagem funcional — o PROMISE, cujo comparador foi majoritariamente cintilografia — não encontrou economia: US$ 2.494 contra US$ 2.240 aos 90 dias, "associada a mais revascularizações e cateterismos", e sem diferença aos 3 anos [22]. O SCOT-HEART, de desenho aditivo, custou +US$ 462 por paciente aos 6 meses (US$ 1.900 contra 1.438), com custos a jusante sem diferença [6]. O PRECISE reduziu o custo diagnóstico em 27% e aumentou o de revascularização em 67% [10]. Nenhum desses resultados é surpreendente à luz da Tabela 4: são os cenários de substituição de imagem funcional (PROMISE), aditivo (SCOT-HEART) e de primeira linha com revascularização (PRECISE), com o sinal que o modelo prevê.

No Brasil, quatro avaliações econômicas precedem esta. Bertoldi et al. modelaram, na perspectiva do sistema público, o custo-efetividade de estratégias anatômicas e funcionais em Markov de longo prazo [30] e em árvore de decisão com custo por diagnóstico correto [31], concluindo pela custo-efetividade da AngioTC; Carmo et al. [3], nesta revista, microcustearam a AngioTC (R$ 452,05; R$ 622,54 corrigidos) e precificaram os comparadores por tabela — a mesma assimetria que este estudo herda e declara —, sem modelar capacidade nem posicionamento. **A narrativa pública que hoje acompanha o pedido apoia-se, porém, no quarto estudo: a análise na saúde suplementar de Shiozaki et al. [20], também nesta revista, que estima economia de R$ 1.021 "por vida" em cinco anos para uma carteira de 100.000 beneficiários.** O confronto direto é instrutivo, porque é a mesma tecnologia com os preços e o comparador de outro sistema — e o comparador é o ponto. Aquele modelo compara a AngioTC, a R$ 1.311,95, com **a angiografia invasiva como estratégia inicial, a R$ 1.900,79, único comparador**, em população de probabilidade intermediária, com eventos do DISCHARGE, e declara nas limitações não ter comparado com testes funcionais. É, portanto, um modelo do PICO de filtro pré-cateterismo: o Δ exigido naquele sistema é de 69 por 100 (1.311,95 ÷ 1.900,79) e o DISCHARGE (75,1) o alcança — o mesmo mecanismo da Tabela 4, última linha, onde no SUS a R$ 550 o limiar é 75,3 e o DISCHARGE fica a 0,2 dele. O que aquele resultado sustenta, transposto ao SUS, é o gatekeeping (R$ 482–625; R$ 841 com revascularização), não a primeira linha. Para a primeira linha ao preço da saúde suplementar, a Tabela 3 responde: substituindo o mix médio, seriam necessários 154 cateterismos evitados por 100 pacientes — mais do que há pacientes; substituindo cintilografia, 72 por 100, dezessete vezes o melhor Δ de primeira linha e da ordem só observada contra cateterismo direto. Ao preço proposto de R$ 550 — três vezes o episódio funcional médio e 75% do cateterismo — o resultado é o da Tabela 4. Mesma tecnologia, sinal econômico oposto — não porque os preços relativos difiram (a razão AngioTC/cateterismo é 0,69 naquele estudo e 0,75 no SUS ao preço proposto), mas porque o comparador difere; a razão só se inverte (1,80) se o preço da saúde suplementar for transplantado ao SUS. Nem os estudos anteriores nem o dossiê tornam essa dependência explícita. Registre-se ainda que a economia de Shiozaki et al. é por beneficiário da carteira, não por paciente examinado, e que a projeção de "mais de R$ 30 bilhões em cinco anos", difundida na imprensa em agosto de 2026, não consta do artigo — o próprio material de imprensa a qualifica como projeção teórica para a saúde suplementar, "sem representar diretamente uma estimativa de impacto" para o SUS [29]. O relatório do IQWiG [4], que não faz avaliação econômica, é a fonte da eficiência diagnóstica (seção 3.5) e a única revisão que reporta cateterismo sem DAC obstrutiva com denominador de randomizados.

### 4.6 Limitações

🟡 **PRÉVIA** — texto completo na v1; a agenda de microcusteio é proposta e depende do coautor.

Este estudo tem limitações de dado, de modelo e de evidência. **De dado:** o SIA não tem identificador de paciente — a inferência ecológica foi evitada por desenho, mas a população elegível não é identificável e a análise responde a uma pergunta inversa (quanto seria preciso evitar), não a uma estimativa pontual; a probabilidade pré-teste não está nos registros, e a estratificação da Tabela 4 é por premissa declarada, não por observação; o CNES é autodeclarado, 70,5% dos equipamentos não migraram para os códigos por canais e software cardíaco, gating, injetora e leitores não constam; a capacidade em vagas não foi estimada; a OCI 0902010026 (77.241 episódios) não foi examinada. **De modelo:** todos os valores são preços de tabela, não custos — inclusive o cateterismo, cujo custo real determina o crédito de cada Δ; o microcusteio de 2022 foi corrigido a partir de 12/2020 sem que o artigo explicite o ano-base, o que é o limite otimista; a substituição 1:1 é premissa; horizonte curto; componentes não quantificados (complicações, permanência, exames não diagnósticos, testes subsequentes, contraste, achados incidentais). **De evidência:** os Δ são diferenças aritméticas por braço em ensaios de horizontes heterogêneos (90 dias a 5 anos), não metanálise; o CAPP entra via metanálise, não artigo primário; o CONSERVE tem divergência de fonte no desfecho de eficiência; a revascularização vem de cinco ensaios (PRECISE, Foy 2017, SCOT-HEART, DISCHARGE, CONSERVE) e é aplicada como envelope, sem desagregação angioplastia/cirurgia onde a publicação não a traz.

**Microcusteio.** A limitação metodológica mais importante é a assimetria: a AngioTC entra microcusteada (2022, corrigida) ou pelo preço proposto, e os comparadores e o cateterismo entram por tabela. Não trava a conclusão — o sinal da Tabela 4 depende de razões de preço que um microcusteio dificilmente inverteria na baixa, e a direção na intermediária já é declarada como incerta —, mas um revisor a apontará, com razão. Declara-se, portanto, como agenda, com o desenho mínimo que a corrigiria: microcusteio *bottom-up* na perspectiva do prestador, pelo método de custeio baseado em atividades e tempo (TDABC) ou por absorção — um só método, escolhido a priori conforme a Diretriz Metodológica de Estudos de Microcusteio do Ministério da Saúde [32] —, **da AngioTC e dos comparadores no mesmo serviço** (teste ergométrico, ecocardiografia de estresse, cintilografia de perfusão em estresse e repouso, cateterismo diagnóstico), em ao menos **oito serviços do SUS**, cobrindo as cinco regiões e as três naturezas (público, filantrópico, universitário) sem exigir célula cheia e incluindo serviços do estrato pronto de 79. Componentes: depreciação e manutenção do equipamento (tomógrafo ≥64 canais, gama-câmara, ecocardiógrafo, sala de hemodinâmica); insumos por exame (contraste iodado, betabloqueador e nitrato, radiofármaco, kits e materiais de hemodinâmica); tempo de sala e de pessoal por etapa (preparo, aquisição, pós-processamento, laudo, enfermagem, técnico, médico executor); software e estação de trabalho; rateio administrativo; **exames não diagnósticos e repetições** (que diluem o custo por diagnóstico útil); e, decisivamente, **a dependência do custo unitário do volume** — custo fixo dividido por *throughput*, que decide se um tomógrafo do estrato pronto absorve a AngioTC à margem ou exige turno adicional. Custo do prestador não é preço do pagador; o estudo deve reportar ambos. Um estudo desse porte custa uma fração da incerteza que resolve, e é condição para qualquer análise econômica simétrica — inclusive a do demandante.

### 4.7 Implicações para política

🟡 **PRÉVIA** — recomendação (i) reancorada na v1.

A pergunta talvez não seja se o SUS deve ter acesso à AngioTC, mas quais pacientes devem recebê-la primeiro — e o que ela substitui quando os recebe. Uma incorporação mal posicionada pode desperdiçar uma tecnologia boa; uma incorporação alinhada à estratificação da diretriz pode entregar o benefício pretendido. Recomendações:

**(i) Condicionar a incorporação a protocolo que especifique posicionamento e substituição.** Não é uma recomendação de forma: é o resultado da Tabela 4. Se a incorporação criar o código sem protocolo, o cenário de referência — e, a juízo dos autores, o mais provável — é o aditivo: a AngioTC somada ao teste ergométrico em curso, sem substituir nada. Nesse cenário nenhum preço plausível é neutro (teto R$ 30; +R$ 440 mi/ano se somada a todo o volume funcional). A sustentabilidade não é uma propriedade do preço negociado; é uma propriedade do protocolo. O protocolo já existe na Diretriz SBC de SCC 2025: probabilidade intermediária, "prova funcional ou angiotomografia", com a substituição explícita da imagem funcional que o serviço realizaria; probabilidade baixa, "ajustar PPT ou angiotomografia", com critérios que evitem que ela substitua "não testar".

**(ii) Avaliar o filtro antes de cateterismo já indicado como pergunta separada**, com critérios de elegibilidade próprios — é a indicação com maior espaço econômico e com respaldo de quatro das cinco diretrizes, e não é a que está sendo requerida.

**(iii) Criar código SIGTAP e microcustear a AngioTC e os comparadores** (seção 4.6), condição para análise econômica simétrica e para que a produção deixe de ser invisível.

**(iv) Completar a reclassificação do CNES antes da apreciação final** e planejar a implantação a partir do estrato pronto, com estratégia regional para as doze UFs sem nenhum estabelecimento.

---

## 5. Conclusão

🟡 **PRÉVIA** — texto completo na v1.

O cadastro nacional de equipamentos, após a Portaria SAES/MS 3.695/2026, permite pela primeira vez responder à pergunta de capacidade que motivou parte da recomendação preliminar: 432 tomógrafos de ≥64 canais em 315 estabelecimentos disponíveis ao SUS, como piso, e 79 estabelecimentos prontos, com forte desigualdade regional. A pergunta orçamentária, por sua vez, não tem resposta única — e isso é o achado, não a limitação. Sem protocolo, a AngioTC entra somada ao percurso e nenhum preço plausível a torna neutra. Com protocolo, a mesma tecnologia ao mesmo preço é expansiva na probabilidade baixa, onde substituiria nada ou um teste ergométrico; fica na zona de incerteza na intermediária quando substitui cintilografia — e só cintilografia —; e tem espaço no filtro antes de cateterismo já indicado. Essa é exatamente a estratificação que a Diretriz SBC de Síndrome Coronariana Crônica 2025 já adota e que o PICO submetido não adota. A evidência sustenta alinhar a incorporação à diretriz da própria sociedade demandante — não recusar a tecnologia, nem incorporá-la sem dizer o que ela substitui.

---

## Declarações

🟡 **PRÉVIA** — texto proposto; campos entre colchetes são do coautor/autores.

- **Contribuição dos autores (categorias da ABC/ICMJE):** concepção e desenho da pesquisa — [autor 1], [coautor]; obtenção de dados — [autor 1]; análise e interpretação dos dados — [autor 1], [coautor]; análise estatística — [autor 1]; redação do manuscrito — [autor 1]; revisão crítica quanto ao conteúdo intelectual importante — [coautor]. (A ABC usa sete categorias, não CRediT.)
- **Conflitos de interesse:** [declarar; incluir eventual participação em sociedade, indústria ou serviço de imagem].
- **Financiamento:** nenhum.
- **Vinculação acadêmica:** [se aplicável].
- **Aprovação ética:** não se aplica — dados públicos agregados, sem seres humanos identificáveis (Res. CNS 510/2016, art. 1º, parágrafo único, III e V).
- **Disponibilidade de dados e código:** repositório público com microdados intermediários, código (`analise_final.py`, `extrai_dac.py`) e tabelas de saída, licenças CC BY 4.0 (texto/dados) e MIT (código); DOI Zenodo [a gerar].
- **Uso de inteligência artificial:** [obrigatório no formulário da ABC — assistência de IA na extração de dados, código e redação, sob supervisão e responsabilidade dos autores.]
- **Ciência aberta (formulário ABC):** dados e código em repositório público (URL/DOI); sem preprint [decidir].
- **Figura central:** obrigatória para artigo original — proposta: a Tabela 4 em forma gráfica (preço de neutralidade por estrato e posição no percurso, com a faixa de R$ 550).

## Referências

🟢 **PRONTA** — 1–29 = lista da contribuição (com [3] Carmo 2022 e [20] Shiozaki 2025 já completas e verificadas; [29] release de imprensa de 11/08/2026). Adicionais do manuscrito:

30. Bertoldi EG, Stella SF, Rohde LE, Polanczyk CA. Long-term cost-effectiveness of diagnostic tests for assessing stable chest pain: modeled analysis of anatomical and functional strategies. Clin Cardiol. 2016;39(5):249-56. DOI 10.1002/clc.22532. PMID 27080921.
31. Bertoldi EG, Stella SF, Rohde LEP, Polanczyk CA. Cost-effectiveness of anatomical and functional test strategies for stable chest pain: public health perspective from a middle-income country. BMJ Open. 2017;7(4):e012652. DOI 10.1136/bmjopen-2016-012652. PMID 28473507.
32. Brasil. Ministério da Saúde. Secretaria de Ciência, Tecnologia, Inovação e Insumos Estratégicos em Saúde. Departamento de Gestão e Incorporação de Tecnologias e Inovação em Saúde. Diretriz Metodológica: estudos de microcusteio aplicados a avaliações econômicas em saúde. Brasília: Ministério da Saúde; 2021. 71 p. ISBN 978-65-5993-199-6.
33. Husereau D, Drummond M, Augustovski F, de Bekker-Grob E, Briggs AH, Carswell C, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations. Value Health. 2022;25(1):3-9. DOI 10.1016/j.jval.2021.11.1351. PMID 35031096.
34. Brasil. Ministério da Saúde. Secretaria de Ciência, Tecnologia e Insumos Estratégicos. Departamento de Ciência e Tecnologia. Diretrizes metodológicas: análise de impacto orçamentário: manual para o Sistema de Saúde do Brasil. Brasília: Ministério da Saúde; 2012. 76 p. ISBN 978-85-334-1945-2.

Formato ABC: Vancouver, numeração por ordem de aparecimento em sobrescrito, até seis autores + et al., 40 referências sugeridas (a lista tem 34 — dentro).

## Apêndices

- A — Reprodutibilidade e códigos 🟢
- B — Ensaios utilizados 🟢
- C — Tabela por UF 🟢 (`out-capacidade-canais-uf.csv`)
- D — Regras pré-registradas e emendas 🟢 (`REGRAS-DE-ANALISE.md`)
- E — Tabela por estrato 🟢 (`out-limiar-por-estrato.csv`)

---

## Nota para o coautor — v1

**Decidido com a sua resposta de 16/08:** periódico (ABC); parte clínica como premissa declarada por estrato (Tabela 4 — reveja as premissas: baixa = nenhum exame ou ergometria; intermediária = eco ou cintilografia); microcusteio como limitação + agenda com desenho mínimo (4.6 — ajuste n de serviços e componentes conforme sua experiência); estratificação como tese (3.4, 4.1, 5); sexto cenário aditivo (Tabelas 3 e 4, recomendação (i)); parágrafo ABC 2026 (4.5).

**O que ainda depende de você:**

1. **Estudo da saúde suplementar — verificado em texto integral.** É Shiozaki A, Torreão J, Costa IBSS, Suarez AB, Silva MT, Oliveira TG, Lopes LES, Nita ME, Trad H, Rochitte CE. Arq Bras Cardiol **2025;122(12)**:e20250204 (epub 9/1/2026; não "2026"). Perspectiva suplementar; **único comparador = angiografia invasiva como estratégia inicial** (o próprio artigo admite nas limitações não ter comparado com testes funcionais); PPT intermediária; eventos do DISCHARGE; AngioTC R$ 1.311,95 ("referência da ANS"), cateterismo R$ 1.900,79; coorte de 100.000 beneficiários; difusão 5%→25% em 5 anos. **R$ 1.021 "por vida"** está no resumo; a tabela da Figura 1 e a discussão trazem R$ 766 e R$ 776; total 5 anos R$ 102,1 mi (resumo) vs R$ 76,6 mi (Fig. 1). **"Mais de R$ 30 bilhões" não está no artigo** — vem de release de imprensa de 11/08/2026 (Jornal do Brás e outros; autor do release ligado a agência de comunicação), que o qualifica como projeção teórica para a suplementar. Financiamento declarado: "parcialmente financiado por Siemens"; dois autores com vínculo empregatício e três com suporte financeiro da Siemens (declaração de COI do artigo). O último autor é o editor-chefe da ABC. **Escrevi a 4.5 só com o argumento metodológico (comparador = ACI → PICO de gatekeeping; por vida ≠ por paciente; R$ 30 bi não é do artigo).** As inconsistências internas e o financiamento estão aqui para a sua decisão, não no texto. O relatório preliminar da Conitec não cita esse artigo (nem Carmo 2022).
1b. **Consequência para nós:** eu rotulava R$ 1.311,95 como "CBHPM 2026" — o artigo o chama de referência da ANS e "100% da CBHPM"; relabelado em todos os documentos como "saúde suplementar (Shiozaki 2025)". E existem mais duas avaliações brasileiras (Bertoldi 2016, 2017 — IATS/UFRGS, perspectiva SUS): "os dois estudos anteriores" vale para *nesta revista*, não para o Brasil; corrigido na introdução e na 4.5.
1c. **Normas da ABC (verificadas):** resumo ≤ 250 palavras em cinco seções (feito; conferir contagem); **corpo ≤ 5.000 palavras contando título, folha de rosto, resumo, referências, legendas e conteúdo das tabelas** — a v1 está muito acima; plano de corte: Tabela 3, seção 3.5 (eficiência diagnóstica), Apêndices e a tabela de diretrizes viram material suplementar, 4.2 encurta, 3.1–3.2 ficam em prosa curta com a Tabela 1; ≤ 8 tabelas+figuras (v1: Tabelas 1–5 + Figuras 1–3 = 8, no limite; com a figura central obrigatória, 9 → cortar a Tabela 3 para o suplemento); referências 40 (temos 34); introdução ≤ 350 palavras (ok); título ≤ 150 caracteres (ok), título resumido ≤ 50 ("AngioTC no SUS: capacidade e limiar orçamentário", 48); 3–5 descritores DeCS (5); submissão preferencialmente em inglês (ambos os idiomas sugeridos); CHEERS; contribuição dos autores em 7 categorias; declaração de uso de IA; taxa R$ 2.000 se o primeiro autor não for sócio da SBC.
2. **Premissas da Tabela 4** e o texto de 4.1 — é o seu julgamento clínico em forma de tabela; corrija o que estiver mal calibrado.
3. **Autoria, ordem, ORCID, conflitos, vinculação, aprovação ética** (Declarações).
4. **Figuras:** mapa (Figura 1), reta preço×Δ com seis cenários (Figura 2), tornado (Figura 3) — faço quando o texto estabilizar.
5. Depois da sua leitura, a v1 passa por uma **terceira rodada cega**, e as seções 🟡 viram 🟢.
