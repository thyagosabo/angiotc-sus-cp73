# Onde a angiotomografia coronariana gera valor no Sistema Único de Saúde? Uma análise nacional de capacidade instalada e limiar orçamentário

*Where Does Coronary CT Angiography Create Value in Brazil's Unified Health System? A National Capacity and Budget-Threshold Analysis*

**Rascunho v0 — para leitura do coautor.** Cada seção traz um marcador de estado no cabeçalho:

- 🟢 **PRONTA** — texto final, números reproduzidos por `analise_final.py`, revisado em duas rodadas cegas
- 🟡 **PRÉVIA** — estrutura e argumento definidos, texto a lapidar, pode conter lacunas marcadas `[…]`
- 🔴 **A FAZER** — só o esqueleto do que a seção precisa conter

Autoria, ordem e afiliações: a definir. Conflitos de interesse: a declarar.

---

## Resumo

🟡 **PRÉVIA**

**Contexto.** Em julho de 2026, a Conitec emitiu recomendação preliminar desfavorável à incorporação da angiotomografia coronariana (AngioTC) como exame de primeira linha para pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária de doença arterial coronariana estável, citando incertezas sobre capacidade instalada, população elegível e impacto orçamentário.

**Objetivo.** Caracterizar a capacidade tomográfica do SUS compatível com AngioTC e determinar sob que condições de posicionamento no percurso diagnóstico a tecnologia atinge neutralidade orçamentária.

**Métodos.** Análise nacional sobre bases públicas: CNES (equipamentos por número de canais, competência 06/2026), SIA/SUS e SIH/SUS (produção 2025, 27 UFs, 395 + 324 arquivos sem perdas), SIGTAP e IBGE. Análise de limiar: em vez de estimar cateterismos evitados — impossível sem identificador de paciente —, calculou-se o Δ de cateterismo total por 100 pacientes necessário para neutralidade a cada preço, para dois PICOs (substituição de teste não invasivo; filtro antes de cateterismo já indicado), cinco cenários de exame substituído, e com e sem revascularização induzida. Os Δ observados foram extraídos de 12 ensaios randomizados. Regras de análise pré-registradas; código e dados públicos.

**Resultados.** 432 tomógrafos de ≥64 canais em 315 estabelecimentos disponíveis ao SUS (piso; 74,6% dos estabelecimentos ainda sob código genérico); 79 reúnem hardware declarado compatível, hemodinâmica e produção coronariana. Investigação funcional: 787.954 episódios/ano, R$ 185,46/episódio, 76% teste ergométrico em volume e 82% do gasto em cintilografia. Nos ensaios de primeira linha, Δ de −6,3 a +4,1 por 100. O preço de neutralidade varia de R$ 139–215 (substituindo o mix médio) a R$ 741–817 (substituindo cintilografia, só exames), caindo a R$ 458–557 com a revascularização observada. O preço proposto (R$ 550) está fora do alcance nos cenários de mix médio e ecocardiografia, e dentro da zona de incerteza nos demais. No gatekeeping (4 ensaios), R$ 482–625, subindo a R$ 841 com revascularização.

**Conclusões.** A sustentabilidade orçamentária da AngioTC no SUS depende de três parâmetros que os registros administrativos não identificam: o exame substituído, a revascularização induzida e a posição no percurso. A Diretriz SBC de Síndrome Coronariana Crônica 2025 estratifica a indicação por probabilidade pré-teste (IIb na baixa, I-A na intermediária); o PICO submetido não. A pergunta de política não é se o SUS deve ter acesso à tecnologia, mas quais pacientes devem recebê-la primeiro.

**Palavras-chave:** angiotomografia coronariana; avaliação de tecnologias em saúde; impacto orçamentário; capacidade instalada; SUS; síndrome coronariana crônica.

---

## 1. Introdução

🔴 **A FAZER** — esqueleto:

1. Carga da DAC no Brasil; investigação de dor torácica estável como porta de entrada de alto volume (787.954 episódios funcionais/ano no SUS em 2025 — número próprio, pode abrir o parágrafo).
2. Mudança internacional para avaliação anatômica: SCOT-HEART, PROMISE, DISCHARGE; NICE CG95 (2016) como primeira diretriz a recomendar AngioTC de primeira linha; ESC 2024 e AHA/ACC 2021 `[agente ainda buscando texto exato — inserir classe/nível]`.
3. Diretriz brasileira: SBC TC/RM 2024 (Classe I, A para PPT baixa/intermediária) e **SBC SCC 2025** (IIb na baixa, I-A na intermediária, "prova funcional ou angioTC") — notar que a diretriz mais recente estratifica.
4. Ausência de acesso estruturado no SUS: sem código SIGTAP; produção administrativamente invisível.
5. O processo Conitec: submissão da SBC, recomendação preliminar desfavorável de 03/07/2026, os pontos que o Comitê listou como essenciais (capacidade instalada, população elegível, comparadores, impacto real sobre cateterismos e testes funcionais).
6. Lacuna: análises de custo-efetividade prévias (Arq Bras Cardiol 2022, SUS; ABC 2026, suplementar) não modelam capacidade instalada nem a dependência do resultado em relação ao **posicionamento** da tecnologia no percurso.
7. Objetivo em uma frase: caracterizar capacidade e determinar as condições de neutralidade orçamentária por posição no percurso, com dados públicos e método reproduzível.

---

## 2. Métodos

### 2.1 Desenho e perspectiva

🟢 **PRONTA**

Análise nacional model-based, perspectiva do SUS como pagador público, horizonte de curto prazo (episódio diagnóstico e desfechos invasivos imediatos). Não se modela prognóstico de longo prazo. Regras de análise fixadas antes da extração dos dados de OCI (`REGRAS-DE-ANALISE.md`, repositório).

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

🟢 **PRONTA**

O SIA não possui identificador de paciente; razões entre contagens agregadas de cateterismos e testes não são probabilidades condicionais. Em vez de estimar cateterismos evitados, calculou-se o Δ de cateterismo total por 100 pacientes necessário para neutralidade a cada preço:

- Primeira linha (substituição de episódio funcional): `P = C_substituído + (Δ_CATE/100)·C_CATE − (Δ_revasc/100)·C_revasc`
- Gatekeeping (filtro antes de cateterismo já indicado; custo prévio comum aos braços cancela): `P = (Δ_CATE/100)·C_CATE − (Δ_revasc/100)·C_revasc`

Com `C_CATE = R$ 730,14` (SIA 2025; sensibilidade a R$ 772,80, valor AIH), `C_revasc` do SIH 2025 (R$ 7.713 angioplastia; R$ 25.904 CRM). `C_substituído` em cinco cenários: mix médio do SIA; mix do NATS como publicado (cintilografia por um código) e por episódio; ecocardiografia de estresse; cintilografia. Preços de referência: R$ 196,41 (TC de tórax + contraste, proxy), R$ 550,00 (proposto pelo demandante), R$ 622,54 (microcusteio 2022 corrigido pelo IPCA), R$ 1.311,95 (CBHPM). O SCOT-HEART, de desenho aditivo, não substitui episódio e é apresentado à parte.

### 2.6 Δ observados nos ensaios

🟢 **PRONTA**

Cateterismo total por braço randomizado, extraído das publicações primárias (Apêndice B): PROMISE, CRESCENT-I, CRESCENT-II, CAPP, PRECISE, Foy 2017 (primeira linha); CAD-MAN, CONSERVE, DISCHARGE, Reis 2022 (gatekeeping). Cateterismo sem DAC obstrutiva (IQWiG D22-01, Tabela 43) apresentado separadamente como eficiência diagnóstica, fora do cálculo econômico. Revascularização: PRECISE, Foy 2017, DISCHARGE.

### 2.7 Reprodutibilidade

🟢 **PRONTA**

`analise_final.py` regenera todas as tabelas a partir dos microdados versionados; recusa-se a rodar com cobertura parcial. Repositório: `[URL/DOI]`.

---

## 3. Resultados

### 3.1 Capacidade instalada

🟢 **PRONTA**

*(texto = seções 2.1–2.4 da contribuição; tabela por UF em `output/out-capacidade-canais-uf.csv`)*

432 equipamentos ≥64 canais (293 de 64, 139 de 128) em 315 estabelecimentos; 736 confirmados <64 em 672; 2.785 sem especificação em 2.534; parque total 3.953 em 3.395. Reclassificação: 910 estabelecimentos (26,8%) com ≥1 equipamento reclassificado, 861 (25,4%) integralmente migrados. Estratos: ≥64 + hemodinâmica 114; + produção coronariana 96; **os três, 79**. Densidade 2,02/milhão; AP, PI e TO sem nenhum ≥64; doze UFs sem estabelecimento pronto (AC, AL, AM, AP, GO, MT, PA, PI, RO, RR, SE, TO). CV 0,86 vs 0,32; Gini 0,30 vs 0,14 (≥64 vs todos). Carga do parque: 13,4 mi exames de TC em 2025, ~3.400/equipamento.

**Figura 1** `[A FAZER]`: mapa por UF, densidade ≥64 canais e estrato pronto.

### 3.2 Cenário atual

🟢 **PRONTA**

*(texto = seções 3.1–3.4 da contribuição)*

787.954 episódios funcionais, R$ 146,1 mi, R$ 185,46/episódio; ergometria 76% do volume e 13% do gasto, cintilografia 19% do volume e 82% do gasto. Cateterismo 163.803, R$ 730,14. OCI de SCC 7.616 episódios (0,96%), 148 estabelecimentos. Angioplastia coronariana 133.934 (R$ 1.033 mi, 268 estab.); revascularização 23.290 (R$ 603 mi, 230). Sem código SIGTAP para AngioTC; contraste para TC com faturamento zero.

### 3.3 Análise de limiar

🟢 **PRONTA**

*(texto = seções 4.3–4.6 da contribuição)*

**Tabela 3** — Δ necessário por preço e por exame substituído (5 × 4). **Tabela 4** — preço de neutralidade por cenário para o Δ observado (−6,3 a +4,1), com e sem revascularização. **Tabela 5** — gatekeeping. **Figura 2** `[EXISTE na prévia HTML; refazer para publicação com os 5 cenários]`: preço da AngioTC × Δ, duas retas, doze ensaios.

### 3.4 Eficiência diagnóstica

🟢 **PRONTA**

*(= seção 4.7 da contribuição; IQWiG Tabela 43)*

### 3.5 Ordem de grandeza do impacto anual (cotas superiores)

🟡 **PRÉVIA** — números calculados, texto a escrever:

Não se estima a população elegível. Como cota superior, se todos os 787.954 episódios funcionais fossem substituídos por AngioTC a R$ 550, o impacto líquido anual seria de +R$ 294 mi (mix médio), +R$ 27 mi (NATS por episódio) ou +R$ 33 mi (cintilografia com revascularização); a 10% de adoção, um décimo disso. No gatekeeping, sobre os 163.803 cateterismos anuais, de +R$ 11 mi (CONSERVE) a **−R$ 48 mi** (DISCHARGE com revascularização). São cotas; a população elegível é uma fração não identificável dos denominadores.

### 3.6 Análise de sensibilidade

🔴 **A FAZER**: tornado univariado sobre C_substituído, C_CATE (730 vs 773), Δ_CATE (faixa observada), Δ_revasc, C_revasc; gerado por `analise_final.py`. Os cinco cenários discretos já existem; falta a figura.

---

## 4. Discussão

### 4.1 Achado principal

🟡 **PRÉVIA**

Uma mesma tecnologia é orçamentariamente expansiva ou plausivelmente sustentável dependendo de onde entra no percurso e do que substitui — e nenhum dos três parâmetros que decidem isso é identificável nos registros administrativos brasileiros. Substituindo o mix médio observado no SUS, majoritariamente teste ergométrico a R$ 32, a AngioTC a R$ 550 exigiria evitar 50 cateterismos por 100 pacientes, doze vezes o melhor Δ já observado. Substituindo a cintilografia, o próprio custo do comparador financia a troca — mas a revascularização adicional observada nos ensaios consome a diferença. Filtrando cateterismos já indicados, o espaço econômico é maior e o DISCHARGE, com a menor revascularização observada, cruza o limiar com folga.

### 4.2 Diretrizes: o PICO submetido versus a estratificação recomendada

🟡 **PRÉVIA** — SBC 2025 verificada; ESC/AHA/NICE `[agente em curso]`

A Diretriz SBC de SCC 2025 estratifica a indicação por probabilidade pré-teste: IIb-B como primeira opção na baixa ("ajustar PPT ou angiotomografia"), I-A como exame inicial na intermediária ("prova funcional ou angiotomografia"), prova funcional na alta. `[ESC 2024: CCTA preferencial em likelihood baixa-moderada, imagem funcional em moderada-alta — inserir texto e classe]`. `[AHA/ACC 2021: CCTA razoável em risco intermediário-alto — inserir]`. `[NICE CG95: primeira linha para angina típica/atípica, ≥64 detectores]`. O PICO submetido à Conitec trata "baixa ou intermediária" como faixa única; a economia difere entre as faixas, e a diretriz da própria sociedade demandante também. Alinhar a incorporação à estratificação da diretriz — e não à faixa agregada — é o instrumento que a evidência sustenta.

### 4.3 O desalinhamento de PICO no processo

🟡 **PRÉVIA**

O dossiê e a reanálise do NATS utilizam o DISCHARGE, ensaio de população já referenciada a cateterismo, como fonte de parâmetros para o PICO de primeira linha. O NATS precifica a cintilografia por um único código (R$ 408,52), contra dois na prática. Ambos os desalinhamentos estão no relatório preliminar e alteram o resultado em ordem de grandeza.

### 4.4 Capacidade: o que o cadastro responde e o que não responde

🟡 **PRÉVIA**

Pela primeira vez o CNES permite contar tomógrafos por canais — mas três quartos do parque ainda não migraram. Os 432 são piso. O estrato de 79 é o conjunto de maior plausibilidade de implantação sem aquisição de tomógrafo, mas software cardíaco, gating, injetora e leitores não constam do cadastro. A desigualdade sobre hardware compatível é maior que sobre o parque agregado. Recomendação administrativa: apreciação sobre a competência mais recente, com a proporção reclassificada declarada.

### 4.5 Comparação com a literatura econômica

🔴 **A FAZER**: PROMISE (Mark 2016, sem economia aos 90 dias e 3 anos); SCOT-HEART 6 meses (+£462, downstream sem diferença); Arq Bras Cardiol 2022 (custo-efetividade SUS, R$ 452 microcusteio, comparadores por tabela); ABC 2026 (suplementar, CBHPM, sem capacidade); IQWiG D22-01. Posicionar: nenhum modela capacidade instalada nem a dependência do posicionamento.

### 4.6 Limitações

🟡 **PRÉVIA** — lista, texto a compor:

Sem identificador de paciente (inferência ecológica evitada por desenho, mas população elegível não identificável); preços de tabela, não custos, para todos os comparadores; horizontes heterogêneos nos ensaios (90 dias a 5 anos); Δ como diferença aritmética, não metanálise; substituição 1:1 como premissa; componentes não quantificados (complicações, permanência, exames não diagnósticos, testes subsequentes, contraste); CNES autodeclarado; capacidade em vagas não estimada; OCI 0902010026 (77.241 episódios) não examinada; CONSERVE com divergência de fonte no desfecho de eficiência; contagens do CAPP via metanálise, não artigo primário; sem microcusteio próprio.

### 4.7 Implicações para política

🟡 **PRÉVIA**

A pergunta talvez não seja se o SUS deve ter acesso à AngioTC, mas quais pacientes devem recebê-la primeiro. Uma incorporação mal posicionada pode desperdiçar uma tecnologia boa; uma incorporação alinhada à estratificação da diretriz pode entregar o benefício pretendido. Recomendações: (i) especificar o protocolo por probabilidade pré-teste; (ii) avaliar o gatekeeping como pergunta separada; (iii) criar código SIGTAP e microcustear AngioTC **e** comparadores; (iv) completar a reclassificação do CNES antes da apreciação final.

---

## 5. Conclusão

🟡 **PRÉVIA**

*(= parágrafo de conclusão do quadro-resumo da contribuição, expandido)*

---

## Declarações

🔴 **A FAZER**: autoria (CRediT), conflitos, financiamento (nenhum), disponibilidade de dados e código (repositório + DOI), aprovação ética (não aplicável — dados públicos agregados, sem identificação).

## Referências

🟢 **PRONTA** *(23 na contribuição; adicionar as diretrizes internacionais quando o agente fechar)*

## Apêndices

- A — Reprodutibilidade e códigos 🟢
- B — Ensaios utilizados 🟢
- C — Tabela por UF 🟢 (`out-capacidade-canais-uf.csv`)
- D — Regras pré-registradas 🟢 (`REGRAS-DE-ANALISE.md`)

---

## Nota para o coautor

O que este rascunho **não** decide e depende de você:

1. **Periódico-alvo.** Arq Bras Cardiol (público natural, português/inglês, já publicou os dois estudos econômicos anteriores) ou revista internacional de ATS/economia da saúde (Value in Health Regional, Int J Technol Assess Health Care, BMC Health Serv Res). Muda o enquadramento da introdução.
2. **A parte clínica.** O algoritmo de elegibilidade e a plausibilidade de cada cenário de exame substituído por faixa de probabilidade — é o julgamento que a base de dados não faz e a diretriz só esboça.
3. **Microcusteio.** Sem ele, o paper compara AngioTC microcusteada (2022, corrigida) contra comparadores de tabela. É a maior limitação metodológica que sobrou, e é trabalho de campo.
4. **A distinção baixa/intermediária.** A SBC 2025 dá IIb e I-A. Vale a pena o paper rodar os cenários separadamente por faixa? Os dados do SIA não distinguem, mas a discussão pode.
