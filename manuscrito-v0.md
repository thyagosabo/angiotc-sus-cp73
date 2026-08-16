# Onde a angiotomografia coronariana gera valor no Sistema Único de Saúde? Uma análise nacional de capacidade instalada e limiar orçamentário

*Where Does Coronary CT Angiography Create Value in Brazil's Unified Health System? A National Capacity and Budget-Threshold Analysis*

**Rascunho v1 — 16/08/2026 — incorpora a resposta do coautor à v0.** Periódico-alvo decidido: **Arquivos Brasileiros de Cardiologia**, artigo original (público: SBC e Comitê; comparabilidade com os dois estudos econômicos anteriores, ambos na ABC). A versão de método — o cadastro nacional de equipamentos como instrumento de ATS — fica reservada para um segundo artigo internacional, sem competir.

Marcadores de estado por seção:

- 🟢 **PRONTA** — texto final, números reproduzidos por `analise_final.py`, revisado em duas rodadas cegas
- 🟡 **PRÉVIA** — texto completo, mas escrito ou reescrito na v1 e ainda **não** submetido à terceira rodada cega; ou dependente de julgamento clínico do coautor
- 🔴 **A FAZER** — só o esqueleto

Autoria, ordem e afiliações: a definir. Conflitos de interesse: a declarar.

**O que mudou de v0 para v1** (resposta do coautor, 16/08/2026): (1) sexto cenário **"adoção aditiva (sem protocolo)"**, C_substituído = 0, na Tabela 3 e na Tabela 4, ancorando a recomendação (i); (2) **estratificação por probabilidade pré-teste como tese**, não como sensibilidade — comparador realista declarado por faixa (baixa: nenhum exame ou ergometria; intermediária: ecocardiografia ou cintilografia), Tabela 4 nova, débito de revascularização aplicado a todos os cenários; (3) 4.5 com parágrafo próprio confrontando o estudo da saúde suplementar (ABC 2026); (4) microcusteio declarado como limitação e agenda, com desenho mínimo; (5) resumo no formato estruturado da ABC; (6) introdução e conclusão em texto completo. Nenhuma equação, código, janela ou desfecho mudou (`REGRAS-DE-ANALISE.md`, emendas 7–8).

---

## Resumo

🟡 **PRÉVIA** — formato ABC (Fundamento/Objetivos/Métodos/Resultados/Conclusões); conferir limite de palavras nas normas.

**Fundamento:** Em julho de 2026 a Conitec emitiu recomendação preliminar desfavorável à incorporação da angiotomografia coronariana (AngioTC) como exame de primeira linha na suspeita de doença coronariana estável com probabilidade pré-teste baixa ou intermediária, citando incertezas sobre capacidade instalada, população elegível e impacto orçamentário.

**Objetivos:** Caracterizar a capacidade tomográfica do SUS compatível com AngioTC e determinar sob que condições de posicionamento no percurso diagnóstico a tecnologia atinge neutralidade orçamentária.

**Métodos:** Análise nacional sobre bases públicas (CNES 06/2026; SIA/SUS e SIH/SUS 2025; SIGTAP; IBGE). Capacidade por número de canais após a Portaria SAES/MS 3.695/2026. Análise de limiar: Δ de cateterismo total por 100 pacientes necessário para neutralidade a cada preço, para dois PICOs (primeira linha; filtro antes de cateterismo já indicado), seis cenários de exame substituído — incluindo adoção aditiva, sem substituição — e por estrato de probabilidade pré-teste, com e sem revascularização induzida. Δ extraídos de 12 ensaios randomizados. Código e dados públicos.

**Resultados:** 432 tomógrafos de ≥64 canais em 315 estabelecimentos disponíveis ao SUS (piso: 74,6% dos estabelecimentos ainda sob código genérico); 79 reúnem hardware compatível, hemodinâmica e produção coronariana; 12 UFs não têm nenhum. Investigação funcional: 787.954 episódios/ano, R$ 185,46 por episódio, 76% teste ergométrico. Sem substituição (adoção aditiva), nenhum preço é neutro (R$ −46 a +30). Na probabilidade baixa, com o comparador que as diretrizes indicam (nenhum exame ou ergometria), o preço proposto de R$ 550 está fora do alcance; na intermediária, dentro da zona de incerteza apenas quando substitui cintilografia (R$ 458–557 com revascularização). No filtro antes de cateterismo indicado, R$ 482–625, até R$ 841 com revascularização.

**Conclusões:** A sustentabilidade orçamentária depende do exame substituído, da revascularização induzida e da posição no percurso — parâmetros que os registros administrativos não identificam, mas que um protocolo define. A mesma tecnologia, ao mesmo preço, é expansiva na probabilidade baixa e plausivelmente sustentável na intermediária-com-cintilografia e no filtro pré-cateterismo — a estratificação que a Diretriz SBC de Síndrome Coronariana Crônica 2025 já faz e o PICO submetido não.

**Palavras-chave (DeCS):** Angiografia por Tomografia Computadorizada; Doença da Artéria Coronariana; Avaliação da Tecnologia Biomédica; Custos e Análise de Custo; Sistema Único de Saúde.

---

## 1. Introdução

🟡 **PRÉVIA** — texto completo; referências às duas avaliações econômicas brasileiras aguardam citação verificada.

A investigação da dor torácica estável é uma porta de entrada de alto volume: no SUS, em 2025, foram 787.954 episódios de investigação funcional não invasiva, três quartos deles por teste ergométrico. Nas duas últimas décadas, a avaliação anatômica por angiotomografia coronariana (AngioTC) acumulou evidência de ensaios randomizados de estratégia — SCOT-HEART, PROMISE, DISCHARGE — e alcançou recomendação de classe I nas diretrizes internacionais (NICE CG95, 2016; AHA/ACC 2021; ESC 2024) e brasileiras (SBC TC/RM 2024; SBC SCC 2025). Com uma exceção (NICE), todas estratificam a indicação por probabilidade pré-teste — e a diretriz brasileira mais recente distingue a probabilidade baixa (IIb-B) da intermediária (I-A).

No SUS, entretanto, não há código para a AngioTC na tabela de procedimentos (SIGTAP); a produção que porventura exista é registrada sob código genérico de tomografia ou não é registrada, e é administrativamente invisível. Em 2026 a Sociedade Brasileira de Cardiologia submeteu à Conitec pedido de incorporação como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária. A recomendação preliminar, de 3 de julho de 2026, foi desfavorável, e o Comitê listou como pontos a esclarecer em consulta pública a capacidade instalada, a necessidade de aquisição de equipamentos, a delimitação da população elegível, os comparadores e o impacto real sobre cateterismos e testes funcionais.

As avaliações econômicas brasileiras disponíveis — uma análise de custo-efetividade sob a perspectiva do SUS, com a AngioTC microcusteada e os comparadores a preços de tabela [3], e uma análise de impacto na saúde suplementar, com preços daquele sistema [ABC 2026 — verificar] — não modelam a capacidade instalada nem a dependência do resultado em relação ao **posicionamento** da tecnologia: o que ela substitui, e em que ponto do percurso entra. Também não podiam contar tomógrafos por número de canais: até janeiro de 2026 o cadastro nacional registrava todos sob um único código, e a Portaria SAES/MS nº 3.695/2026, que o desmembrou por canais, ainda não havia sido explorada como instrumento de avaliação de tecnologia.

Este estudo responde às perguntas do Comitê com dados públicos e método reproduzível: caracteriza a capacidade tomográfica do SUS compatível com AngioTC e determina, por posição no percurso e por estrato de probabilidade pré-teste, sob que condições a tecnologia atinge neutralidade orçamentária.

---

## 2. Métodos

### 2.1 Desenho e perspectiva

🟢 **PRONTA**

Análise nacional model-based, perspectiva do SUS como pagador público, horizonte de curto prazo (episódio diagnóstico e desfechos invasivos imediatos). Não se modela prognóstico de longo prazo. Regras de análise fixadas antes da extração dos dados de OCI (`REGRAS-DE-ANALISE.md`, repositório); duas apresentações acrescentadas após a v0 estão declaradas como emendas não pré-registradas (idem, emendas 7–8). Estudo com dados públicos agregados, sem identificação individual — dispensado de apreciação por Comitê de Ética (Resolução CNS 510/2016, art. 1º, parágrafo único, incisos III e V) *[coautor: confirmar prática institucional]*.

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

Com `C_CATE = R$ 730,14` (SIA 2025; sensibilidade a R$ 772,80, valor AIH), `C_revasc` do SIH 2025 (R$ 7.713 angioplastia; R$ 25.904 CRM). Preços de referência: R$ 196,41 (TC de tórax + contraste, proxy), R$ 550,00 (proposto pelo demandante), R$ 622,54 (microcusteio 2022 corrigido pelo IPCA), R$ 1.311,95 (CBHPM).

`C_substituído` em **seis cenários**: **adoção aditiva (sem protocolo)** — a AngioTC somada ao percurso atual, nada substituído, `C = 0`, algebricamente a equação de gatekeeping com o Δ dos ensaios de primeira linha (o desenho do SCOT-HEART); mix médio do SIA; mix do NATS como publicado (cintilografia por um código) e por episódio; ecocardiografia de estresse; cintilografia. **Por estrato de probabilidade pré-teste**, o comparador realista foi declarado como premissa a partir das diretrizes (seção 4.2) e do julgamento clínico dos autores: probabilidade baixa → nenhum exame (diferir, ajustar probabilidade, escore de cálcio — isto é, adoção aditiva) ou teste ergométrico; intermediária → ecocardiografia de estresse ou cintilografia de perfusão (ou o percurso do NATS, que as mistura); o mix médio do SIA representa o PICO como submetido, sem estratificar. O débito de revascularização (PRECISE, Foy 2017) foi aplicado a todos os cenários de primeira linha como envelope. Cotas anuais de ordem de grandeza: todos os episódios funcionais (ou todos os cateterismos, no gatekeeping) a R$ 550, no ponto médio da faixa de Δ observada.

### 2.6 Δ observados nos ensaios

🟢 **PRONTA**

Cateterismo total por braço randomizado, extraído das publicações primárias (Apêndice B): PROMISE, CRESCENT-I, CRESCENT-II, CAPP, PRECISE, Foy 2017 (primeira linha); CAD-MAN, CONSERVE, DISCHARGE, Reis 2022 (gatekeeping); SCOT-HEART (aditivo). Cateterismo sem DAC obstrutiva (IQWiG D22-01, Tabela 43) apresentado separadamente como eficiência diagnóstica, fora do cálculo econômico. Revascularização: PRECISE, Foy 2017, DISCHARGE.

### 2.7 Reprodutibilidade

🟢 **PRONTA**

`analise_final.py` regenera todas as tabelas a partir dos microdados versionados — inclusive as cotas anuais e a tabela por estrato (`output/out-limiar-por-estrato.csv`); recusa-se a rodar com cobertura parcial. Repositório: `[URL/DOI]`. Relato conforme CHEERS 2022 no que se aplica a análise de limiar *[checklist a anexar]*.

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
| R$ 1.311,95 | CBHPM 2026 | 179,7 | 154,3 | 136,3 | 107,9 | 152,8 | 71,9 |

Nos ensaios de primeira linha o Δ observado foi de −6,3 (CAPP) a +4,1 (PRECISE) por 100; nos invasivo-primeiro, de 66,0 (CONSERVE) a 85,6 (CAD-MAN). Na adoção aditiva o Δ exigido a R$ 550 (75,3) é numericamente o limiar do gatekeeping — a equação é a mesma; a diferença é que 75 por 100 é o que o DISCHARGE observou em pacientes já indicados a cateterismo, e 4,1 é o melhor já observado em primeira linha. Ao preço da CBHPM, substituindo o mix médio, seriam necessárias mais angiografias evitadas do que pacientes investigados. Preços de neutralidade por cenário e gatekeeping: Tabela 4. **Figura 2** `[refazer para publicação com os seis cenários]`: preço da AngioTC × Δ, duas retas, doze ensaios.

### 3.4 Limiar por estrato de probabilidade pré-teste e posição no percurso

🟡 **PRÉVIA** — números reproduzidos (`analise_final.py` §4.9); texto novo na v1. **É a tabela central do artigo.**

**Tabela 4 — Preço de neutralidade da AngioTC por estrato de probabilidade pré-teste, comparador realista (premissa declarada) e posição no percurso; Δ de cateterismo total observado nos ensaios (−6,3 a +4,1 em primeira linha), com e sem revascularização induzida (PRECISE +4,0/100; Foy 2017 +2,7/100; DISCHARGE −3,8/100).**

| Estrato | Comparador (premissa) | C_substituído | Neutralidade, só exames + cateterismo | Neutralidade com revascularização | Δ exigido a R$ 550 |
|---|---|---|---|---|---|
| Baixa | nenhum exame (diferir/ajustar PPT/escore de cálcio) → **adoção aditiva** | R$ 0 | **R$ −46 a +30** (SCOT-HEART: R$ −9 a +4) | R$ −329 a −229 | 75,3 |
| Baixa | teste ergométrico | R$ 32,20 | R$ −14 a +62 | R$ −297 a −197 | 70,9 |
| Não estratificado (PICO submetido) | mix médio do SIA | R$ 185,46 | R$ 139 a 215 | R$ −144 a −44 | 49,9 |
| Intermediária | ecocardiografia de estresse | R$ 196,39 | R$ 150 a 226 | R$ −133 a −33 | 48,4 |
| Intermediária | percurso do NATS por episódio | R$ 523,81 | R$ 477 a 554 | R$ 195 a 294 | 3,6 |
| Intermediária | cintilografia de perfusão | R$ 786,83 | R$ 741 a 817 | **R$ 458 a 557** | já neutro |
| Já indicado a cateterismo (outro PICO) | cateterismo direto — CONSERVE / Reis 2022 / DISCHARGE / CAD-MAN | cancela | R$ 482 / 527 / 548 / 625 | **R$ 841** (DISCHARGE) | 75,3 |

Notas: mix do NATS como publicado (cintilografia por um código, R$ 316,76): R$ 270–347 só com exames. Débito de revascularização aplicado como envelope a todos os cenários de primeira linha; para a adoção aditiva é um envelope emprestado. Com `C_CATE` = R$ 772,80 (AIH), o gatekeeping vai a R$ 510–662.

Três resultados. **Na probabilidade baixa, nenhum preço fecha**: com o comparador que as diretrizes indicam — nenhum exame ou ergometria —, o preço de neutralidade é negativo ou de dezenas de reais, com ou sem revascularização; sem substituição, mesmo gratuita a AngioTC só é neutra se não induzir cateterismos, e o melhor Δ de primeira linha paga R$ 30. **Na intermediária, o resultado depende de qual imagem funcional sai do percurso**: substituindo ecocardiografia de estresse, R$ 550 está fora do alcance; substituindo cintilografia, dentro da zona de incerteza mesmo com a revascularização observada; o percurso misto do NATS, que sem revascularização cercava R$ 550, cai a R$ 195–294 quando ela entra. **O PICO como submetido — a média não estratificada — herda o pior estrato**, porque três quartos do volume atual são ergometria. No filtro antes de cateterismo indicado (outro PICO), R$ 482–625, e R$ 841 no DISCHARGE com a menor revascularização observada.

### 3.5 Eficiência diagnóstica

🟢 **PRONTA** *(= seção 4.8 da contribuição; IQWiG Tabela 43)*

Cateterismo sem DAC obstrutiva por 100 randomizados, evitados com AngioTC: CARE-CCTA 5,9; CATCH 3,0; SCOT-HEART 1,7; PROMISE 0,9 (funcionais); CAD-MAN 81,0; DISCHARGE 65,7; Reis 2022 53,7; CONSERVE 58,0ᵃ (invasivo-primeiro). Metanálise IQWiG contra funcionais (CATCH, PROMISE): OR 0,77 (IC95% 0,64–0,94). Direção favorável à AngioTC em todos os ensaios, nos dois PICOs; não entra no cálculo econômico. ᵃ ressalva de fonte (denominadores da Tabela 43, não randomizados).

### 3.6 Ordem de grandeza do impacto anual (cotas)

🟡 **PRÉVIA** — números reproduzidos (`analise_final.py` §4.10); texto novo na v1.

Não se estima a população elegível. Como cota, se todos os 787.954 episódios funcionais recebessem AngioTC a R$ 550, no ponto médio da faixa de Δ observada o impacto líquido anual seria de **+R$ 440 mi na adoção aditiva**, +R$ 294 mi substituindo o mix médio, +R$ 285 mi a ecocardiografia, +R$ 27 mi o percurso do NATS por episódio, −R$ 180 mi a cintilografia só com exames e +R$ 33 mi a cintilografia com revascularização; a 10% de adoção, um décimo. No gatekeeping, sobre os 163.803 cateterismos anuais, de +R$ 11 mi (CONSERVE) a −R$ 12 mi (CAD-MAN) só com exames, e **−R$ 48 mi** no DISCHARGE com revascularização. São cotas de ordem de grandeza; a população elegível é uma fração não identificável dos denominadores.

### 3.7 Análise de sensibilidade

🔴 **A FAZER**: tornado univariado sobre C_substituído, C_CATE (730 vs 773), Δ_CATE (faixa observada), Δ_revasc, C_revasc; gerado por `analise_final.py`. Os cenários discretos da Tabela 4 já cobrem C_substituído e Δ_revasc; falta a figura (**Figura 3**).

---

## 4. Discussão

### 4.1 Achado principal

🟡 **PRÉVIA** — reescrito na v1 em torno da estratificação.

Uma mesma tecnologia, ao mesmo preço, é orçamentariamente expansiva ou plausivelmente sustentável dependendo de onde entra no percurso e do que substitui — e nenhum dos três parâmetros que decidem isso é identificável nos registros administrativos brasileiros. O que os registros não dizem, porém, as diretrizes dizem: em cada faixa de probabilidade pré-teste há um comparador realista, e declará-lo como premissa converte a limitação em resultado. Na probabilidade baixa, onde as diretrizes recomendam diferir, ajustar a probabilidade ou usar escore de cálcio, ou onde o SUS hoje faz um teste ergométrico de R$ 32, a AngioTC não substitui nada de valor — e nenhum preço a torna neutra. Na intermediária, onde o comparador é a imagem funcional, o resultado se decide pelo que sai do percurso: a ecocardiografia de estresse, a R$ 196, não financia a troca; a cintilografia, a R$ 787, financia — até que a revascularização adicional observada nos ensaios consuma metade da diferença e deixe R$ 550 dentro da zona de incerteza, não fora dela. Filtrando cateterismos já indicados, o espaço econômico é maior e o DISCHARGE, com a menor revascularização observada, cruza o limiar com folga.

O sexto cenário é o mais provável e o mais desfavorável. Sem código SIGTAP e sem protocolo vinculante, com 787.954 episódios funcionais por ano em curso, a AngioTC tende a entrar somada ao teste ergométrico, não no lugar dele — o desenho do SCOT-HEART transposto para a rotina. Nesse caso `C_substituído = 0`, o preço de neutralidade é de R$ −46 a +30 e a tecnologia é expansiva por construção, independentemente do preço negociado. Isso não enfraquece o argumento a favor da AngioTC; localiza-o: a condição de sustentabilidade não é o preço, é a especificação do que sai do percurso.

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

Pela primeira vez o CNES permite contar tomógrafos por canais — mas três quartos do parque ainda não migraram. Os 432 são piso. O estrato de 79 é o conjunto de maior plausibilidade de implantação sem aquisição de tomógrafo, mas software cardíaco, gating, injetora e leitores treinados não constam do cadastro; a capacidade em vagas depende da carga atual (~3.400 exames/equipamento/ano) e não foi estimada. A desigualdade sobre hardware compatível é maior que sobre o parque agregado, e doze UFs não têm nenhum estabelecimento pronto — a incorporação sem estratégia regional consolidaria a desigualdade que o dado revela. Recomendação administrativa: apreciação sobre a competência mais recente, com a proporção reclassificada declarada, e instrumentos para completar a reclassificação.

### 4.5 Comparação com a literatura econômica

🟡 **PRÉVIA** — texto completo; citação e parâmetros do estudo da saúde suplementar aguardam verificação em texto integral.

A única análise econômica de ensaio no cenário de substituição de imagem funcional — o PROMISE, cujo comparador foi majoritariamente cintilografia — não encontrou economia: US$ 2.494 contra US$ 2.240 aos 90 dias, "associada a mais revascularizações e cateterismos", e sem diferença aos 3 anos [22]. O SCOT-HEART, de desenho aditivo, custou +£462 por paciente aos 6 meses, com custos a jusante sem diferença [6]. O PRECISE reduziu o custo diagnóstico em 27% e aumentou o de revascularização em 67% [10]. Nenhum desses resultados é surpreendente à luz da Tabela 4: são os cenários de substituição de imagem funcional (PROMISE), aditivo (SCOT-HEART) e de primeira linha com revascularização (PRECISE), com o sinal que o modelo prevê.

No Brasil, a análise de custo-efetividade sob a perspectiva do SUS [3] microcusteou a AngioTC (R$ 452, base 2020; R$ 622,54 corrigidos) e precificou os comparadores por tabela — a mesma assimetria que este estudo herda e declara — sem modelar capacidade nem posicionamento. **A narrativa pública que hoje acompanha o pedido apoia-se, porém, em outro estudo: a análise na saúde suplementar [ABC 2026 — verificar], que estima economia média de R$ 1.021 por paciente e mais de R$ 30 bilhões em cinco anos** *[números conforme relatados pelo coautor; confirmar no texto integral]*. O confronto direto é instrutivo, porque é a mesma tecnologia com os preços e comparadores de outro sistema. Naquele sistema a AngioTC é remunerada em torno da CBHPM (R$ 1.311,95) e o cateterismo e a revascularização a preços privados *[verificar os valores usados pelo estudo]*; a economia por paciente decorre da razão entre o preço da AngioTC e o dos procedimentos que ela evita. No SUS essa razão se inverte: ao preço da CBHPM, com o cateterismo a R$ 730,14 e o comparador ao mix médio, a neutralidade exigiria evitar **154 cateterismos por 100 pacientes** (Tabela 3) — mais do que há pacientes; substituindo cintilografia, 72 por 100, dezessete vezes o melhor Δ de primeira linha e da ordem só observada em pacientes já indicados a cateterismo. Ao preço proposto de R$ 550, três vezes o episódio funcional médio e 75% do cateterismo, o resultado é o da Tabela 4. Mesma tecnologia, sinal econômico oposto, porque os preços relativos são opostos — e nenhum dos dois estudos brasileiros anteriores, nem o dossiê, torna essa dependência explícita. O relatório do IQWiG [4], que não faz avaliação econômica, é a fonte da eficiência diagnóstica (seção 3.5) e a única revisão que reporta cateterismo sem DAC obstrutiva com denominador de randomizados.

### 4.6 Limitações

🟡 **PRÉVIA** — texto completo na v1; a agenda de microcusteio é proposta e depende do coautor.

Este estudo tem limitações de dado, de modelo e de evidência. **De dado:** o SIA não tem identificador de paciente — a inferência ecológica foi evitada por desenho, mas a população elegível não é identificável e a análise responde a uma pergunta inversa (quanto seria preciso evitar), não a uma estimativa pontual; a probabilidade pré-teste não está nos registros, e a estratificação da Tabela 4 é por premissa declarada, não por observação; o CNES é autodeclarado, três quartos do parque não migraram para os códigos por canais e software cardíaco, gating, injetora e leitores não constam; a capacidade em vagas não foi estimada; a OCI 0902010026 (77.241 episódios) não foi examinada. **De modelo:** todos os valores são preços de tabela, não custos — inclusive o cateterismo, cujo custo real determina o crédito de cada Δ; a substituição 1:1 é premissa; horizonte curto; componentes não quantificados (complicações, permanência, exames não diagnósticos, testes subsequentes, contraste, achados incidentais). **De evidência:** os Δ são diferenças aritméticas por braço em ensaios de horizontes heterogêneos (90 dias a 5 anos), não metanálise; o CAPP entra via metanálise, não artigo primário; o CONSERVE tem divergência de fonte no desfecho de eficiência; a revascularização vem de três ensaios e é aplicada como envelope.

**Microcusteio.** A limitação metodológica mais importante é a assimetria: a AngioTC entra microcusteada (2022, corrigida) ou pelo preço proposto, e os comparadores e o cateterismo entram por tabela. Não trava a conclusão — o sinal da Tabela 4 depende de razões de preço que um microcusteio dificilmente inverteria na baixa, e a direção na intermediária já é declarada como incerta —, mas um revisor a apontará, com razão. Declara-se, portanto, como agenda, com o desenho mínimo que a corrigiria: microcusteio *time-driven* por absorção, conforme a diretriz metodológica do Ministério da Saúde [verificar ref.], **da AngioTC e dos comparadores no mesmo serviço** — teste ergométrico, ecocardiografia de estresse, cintilografia de perfusão (estresse e repouso) e cateterismo diagnóstico —, em ao menos **seis a oito serviços do SUS** estratificados por região e por natureza (público, filantrópico, universitário), com os componentes: depreciação e manutenção do equipamento (tomógrafo ≥64 canais, gama-câmara, ecocardiógrafo, sala de hemodinâmica); insumos por exame (contraste iodado, betabloqueador e nitrato, radiofármaco, kits e materiais de hemodinâmica); tempo de sala e de pessoal (técnico, enfermagem, médico executor, laudo); software e estação de trabalho; e rateio administrativo. Um estudo desse porte custa uma fração da incerteza que resolve, e é condição para qualquer análise econômica simétrica — inclusive a do demandante.

### 4.7 Implicações para política

🟡 **PRÉVIA** — recomendação (i) reancorada na v1.

A pergunta talvez não seja se o SUS deve ter acesso à AngioTC, mas quais pacientes devem recebê-la primeiro — e o que ela substitui quando os recebe. Uma incorporação mal posicionada pode desperdiçar uma tecnologia boa; uma incorporação alinhada à estratificação da diretriz pode entregar o benefício pretendido. Recomendações:

**(i) Condicionar a incorporação a protocolo que especifique posicionamento e substituição.** Não é uma recomendação de forma: é o resultado da Tabela 4. Sem protocolo, o cenário de adoção mais provável no SUS é o aditivo — a AngioTC somada ao teste ergométrico em curso, sem código próprio e sem substituir nada —, e nesse cenário nenhum preço é neutro (R$ −46 a +30; +R$ 440 mi/ano se aplicada a todo o volume funcional). A sustentabilidade não é uma propriedade do preço negociado; é uma propriedade do protocolo. O protocolo já existe na Diretriz SBC de SCC 2025: probabilidade intermediária, "prova funcional ou angiotomografia", com a substituição explícita da imagem funcional que o serviço realizaria; probabilidade baixa, "ajustar PPT ou angiotomografia", com critérios que evitem que ela substitua "não testar".

**(ii) Avaliar o filtro antes de cateterismo já indicado como pergunta separada**, com critérios de elegibilidade próprios — é a indicação com maior espaço econômico e com respaldo de quatro das cinco diretrizes, e não é a que está sendo requerida.

**(iii) Criar código SIGTAP e microcustear a AngioTC e os comparadores** (seção 4.6), condição para análise econômica simétrica e para que a produção deixe de ser invisível.

**(iv) Completar a reclassificação do CNES antes da apreciação final** e planejar a implantação a partir do estrato pronto, com estratégia regional para as doze UFs sem nenhum estabelecimento.

---

## 5. Conclusão

🟡 **PRÉVIA** — texto completo na v1.

O cadastro nacional de equipamentos, após a Portaria SAES/MS 3.695/2026, permite pela primeira vez responder à pergunta de capacidade que motivou parte da recomendação preliminar: 432 tomógrafos de ≥64 canais em 315 estabelecimentos disponíveis ao SUS, como piso, e 79 estabelecimentos prontos, com forte desigualdade regional. A pergunta orçamentária, por sua vez, não tem resposta única — e isso é o achado, não a limitação. Sem protocolo, a AngioTC entra somada ao percurso e nenhum preço a torna neutra. Com protocolo, a mesma tecnologia ao mesmo preço é expansiva na probabilidade baixa, onde substituiria nada ou um teste ergométrico, e plausivelmente sustentável na intermediária quando substitui cintilografia e no filtro antes de cateterismo já indicado. Essa é exatamente a estratificação que a Diretriz SBC de Síndrome Coronariana Crônica 2025 já adota e que o PICO submetido não adota. A evidência sustenta alinhar a incorporação à diretriz da própria sociedade demandante — não recusar a tecnologia, nem incorporá-la sem dizer o que ela substitui.

---

## Declarações

🟡 **PRÉVIA** — texto proposto; campos entre colchetes são do coautor/autores.

- **Contribuição dos autores (CRediT):** [autor 1] — conceituação, metodologia, curadoria de dados, software, análise formal, redação do rascunho; [coautor] — conceituação, validação clínica (premissas por estrato de probabilidade), revisão crítica; ambos — aprovação da versão final.
- **Conflitos de interesse:** [declarar; incluir eventual participação em sociedade, indústria ou serviço de imagem].
- **Financiamento:** nenhum.
- **Vinculação acadêmica:** [se aplicável].
- **Aprovação ética:** dados públicos agregados, sem identificação individual (Res. CNS 510/2016, art. 1º, parágrafo único, III e V); não submetido a CEP. [confirmar]
- **Disponibilidade de dados e código:** repositório público com microdados intermediários, código (`analise_final.py`, `extrai_dac.py`) e tabelas de saída, licenças CC BY 4.0 (texto/dados) e MIT (código); DOI Zenodo [a gerar].
- **Uso de inteligência artificial:** [declarar conforme política da ABC — assistência de IA na extração de dados, código e redação, sob supervisão e responsabilidade dos autores.]

## Referências

🟢 **PRONTA** *(28 na contribuição; acrescentar: análise da saúde suplementar (ABC 2026) e citação completa da ABC 2022 [3] — em verificação; diretriz metodológica de microcusteio do MS; CHEERS 2022.)*

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

1. **Estudo da saúde suplementar (ABC 2026):** estou verificando a citação e os parâmetros em texto integral; se você tiver o PDF, encurta o caminho. Os números R$ 1.021 e R$ 30 bi estão como você relatou, marcados para confirmação.
2. **Premissas da Tabela 4** e o texto de 4.1 — é o seu julgamento clínico em forma de tabela; corrija o que estiver mal calibrado.
3. **Autoria, ordem, ORCID, conflitos, vinculação, aprovação ética** (Declarações).
4. **Figuras:** mapa (Figura 1), reta preço×Δ com seis cenários (Figura 2), tornado (Figura 3) — faço quando o texto estabilizar.
5. Depois da sua leitura, a v1 passa por uma **terceira rodada cega**, e as seções 🟡 viram 🟢.
