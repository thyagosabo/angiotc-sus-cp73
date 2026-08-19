# Material suplementar

**Onde a angiotomografia coronariana gera valor no Sistema Único de Saúde? Capacidade instalada, limiar orçamentário e o caso do filtro pré-cateterismo** — material suplementar (v1.3, 18/08/2026). Todos os números são reproduzidos por `analise_final.py` a partir dos microdados versionados no repositório [URL/DOI]; a contribuição técnica à Consulta Pública Conitec nº 73/2026 (`contribuicao-cp73.pdf`) contém a versão extensa das seções 2–4.

## Tabela S1 — Fontes de dados, endereços e competências; e Tabela S2 — códigos SIGTAP e CNES utilizados

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

## Tabela S3 — Δ de cateterismo total por 100 pacientes necessário para neutralidade, por preço da angioTC e por exame substituído (só exames e cateterismo)

| Preço da angioTC | Natureza | **adoção aditiva** | mix SIA | NATS publicado | NATS por episódio | eco de estresse | cintilografia |
|---|---|---|---|---|---|---|---|
| R$ 196,41 | TC tórax + contraste, proxy SIGTAP | 26,9 | 1,5 | já neutro | já neutro | 0,0 | já neutro |
| **R$ 550,00** | **proposto pelo demandante** | **75,3** | **49,9** | **31,9** | **3,6** | 48,4 | **já neutro** |
| R$ 622,54 | microcusteio 2022 (Carmo et al.) corrigido a jul/2026 (IPCA 12/2020→07/2026, ×1,3771; ano-base não explicitado no artigo, 12/2020 é o limite otimista) | 85,3 | 59,9 | 41,9 | 13,5 | 58,4 | já neutro |
| R$ 1.311,95 | saúde suplementar (Shiozaki et al. 2025: referência ANS, 100% CBHPM) | 179,7 | 154,3 | 136,3 | 107,9 | 152,8 | 71,9 |

Valores: Δ de cateterismo total por 100 pacientes necessário para neutralidade, considerando apenas o custo dos exames e do cateterismo; "já neutro" = preço abaixo do custo do exame substituído. Faixa observada em primeira linha: −6,3 a +4,1; contra cateterismo direto: 66,0 a 85,6.

## Tabela S4 — Ensaios utilizados: cateterismo total por braço, janelas e revascularização

| Ensaio | Publicação | Comparador | N (int/ctrl) | Cateterismo int | Cateterismo ctrl | Janela |
|---|---|---|---|---|---|---|
| PROMISE | NEJM 2015 · PMID 25773919 | funcional-primeiro | 4996 / 5007 | 609 (12,2%) | 406 (8,1%) | 90 dias |
| SCOT-HEART | JACC 2016 · PMID 27081014; NEJM 2018 · PMID 30145934 | usual care (aditivo) | 2073 / 2073 | 409 (19,7%) (mediana 20 m); 491 (23,7%) (5 a) | 401 (19,3%); 502 (24,2%) | 20 m; 5 a |
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

Os quatro invasivo-primeiro não são comparáveis aos demais: a população já estava referenciada para procedimento invasivo e a taxa do braço controle é determinada pelo desenho. CATCH e CARE-CCTA entram apenas no desfecho de cateterismo sem DAC obstrutiva (Tabela S6). As contagens do CAPP (66/51) não constam do artigo primário; provêm do gráfico de floresta de Foy 2017. Revascularização por braço, usada na Tabela S7: PRECISE 9,2% vs 5,2%; Foy 2017 (13 ensaios) 7,2% vs 4,5%; SCOT-HEART 233 vs 201 (20 m) e 279 vs 267 (5 a); DISCHARGE 14,2% vs 18,0%; CONSERVE 13% vs 18%. Nos ensaios em que a revascularização não é desagregada, ela é valorada como angioplastia. Os Δ de cateterismo provêm de 10 ensaios e 1 metanálise; CATCH e CARE-CCTA (12 estudos ao todo) só entram na eficiência diagnóstica.

---

## Tabela S5 — Posição da angiotomografia coronariana nas diretrizes vigentes, por probabilidade pré-teste

Cinco diretrizes verificadas em texto integral (SBC/CBR TC/RM 2024; SBC SCC 2025; ESC 2024; AHA/ACC 2021; NICE CG95). Nenhuma diretriz AHA/ACC posterior a 2021 sobre dor torácica ou doença coronariana crônica existe (a de 2023 remete à de 2021). Célula AHA/ACC de probabilidade baixa: classe da recomendação de diferimento a conferir na prova.

| Diretriz | Probabilidade baixa | Intermediária | Alta | Filtro antes de cateterismo |
|---|---|---|---|---|
| **SBC SCC 2025** (Arq Bras Cardiol 2025;122(9)) | primeira opção **IIb-B**; "ajustar PPT ou angiotomografia" | exame inicial **I-A**; "prova funcional ou angiotomografia" | prova funcional (I-B para eco, SPECT/PET, RMC) | "alternativa ao estudo invasivo" após teste funcional conflitante (IIa-B baixa; I-A intermediária) |
| **SBC TC/RM 2024** (Arq Bras Cardiol 2024;121(9)) | opção inicial **I-A** (baixa e intermediária, sem distinção) | opção inicial **I-A** | **III-C** | **I-A** — "alternativa … com probabilidade pré-teste intermediária e indicação de cinecoronariografia invasiva" |
| **ESC 2024** (Eur Heart J 2024;45:3415) | ≤5% diferir (IIa-B); 5–15% escore de cálcio (IIa-B) | >5–50%: CCTA **preferida** para excluir DAC (I-B), diagnóstico e risco (I-A); >15–85%: imagem funcional (I-B), "melhor poder de confirmação" | >85%: cateterismo direto (I-C) | sequência da Tabela 13: CCTA → funcional se incerta → cateterismo se ainda incerto (I-B) |
| **AHA/ACC 2021** (Circulation 2021;144:e368) | modelo de PPT para identificar baixo risco em quem o teste pode ser diferido; no baixo risco, escore de cálcio ou teste ergométrico sem imagem como primeira linha (2a B-NR) *[classe do diferimento a conferir na prova]* | risco intermediário-alto: CCTA **1-A** e imagem de estresse **1 B-R** co-iguais; CCTA preferível <65 anos, estresse ≥65 | — | "candidatos a cateterismo eletivo podem ser triados com segurança por CCTA ou teste de estresse" |
| **NICE CG95** (2016) | CCTA ≥64 cortes a toda angina típica/atípica, sem PPT | idem | idem | funcional 2ª linha se CCTA incerta; cateterismo 3ª linha |

Texto da SBC SCC 2025 (seção 3.1.7, "Resumo com sugestão de como investigar com métodos diagnósticos"): "A escolha do exame inicial deve levar em conta: Capacidade funcional: se preservada, iniciar com TE ou ecocardiograma de estresse; ECG basal interpretável: se não for interpretável, preferir métodos de imagem (ecocardiograma, cintilografia, RMC); Acesso local e disponibilidade: considerar custo, tempo de realização e familiaridade da equipe; DRC ou alergia a contraste: pode haver restrição para realização de angioTC." E: "Pacientes com PPT < 5% não requerem investigação adicional. Aqueles entre 5 e 15% devem ser avaliados individualmente. PPT entre 15 e 85% indica a necessidade de testes funcionais ou anatômicos".

## Tabela S6 — Eficiência diagnóstica: cateterismo sem DAC obstrutiva por 100 randomizados (IQWiG D22-01, Tabela 43)

Métrica de eficiência diagnóstica, **não utilizada no cálculo econômico**.

| Ensaio | Comparador | angioTC | Controle | Evitados /100 |
|---|---|---|---|---|
| CARE-CCTA | funcional | 4/460 (0,9%) | 30/443 (6,8%) | 5,9 |
| CATCH | funcional (dor torácica aguda, SCA excluída) | 14/285 (4,9%) | 23/291 (7,9%) | 3,0 |
| SCOT-HEART | usual care (aditivo) | 20/2073 (1,0%) | 56/2073 (2,7%) | 1,7 |
| PROMISE | funcional | 170/4996 (3,4%) | 213/5007 (4,3%) | 0,9 |
| CAD-MAN | cateterismo direto | 6/167 (3,6%) | 137/162 (84,6%) | 81,0 |
| DISCHARGE | cateterismo direto | 111/1808 (6,1%) | 1260/1753 (71,9%) | 65,7 |
| Reis 2022 | cateterismo direto | 5/115 (4,3%) | 61/105 (58,1%) | 53,7 |
| CONSERVE | cateterismo direto | 24/784 (3,1%)ᵃ | 439/719 (61,1%)ᵃ | 58,0ᵃ |

ᵃ CONSERVE: valores da Tabela 43 do IQWiG (denominadores de pacientes avaliados por estratégia, 784/719, não os randomizados, 823/808); o abstract do ensaio reporta 24,6% e 61,1% como taxas de cateterismo normal entre os cateterismos realizados, não por paciente. Adicionalmente: PRECISE 2,6% vs 10,2%; CRESCENT-II (cateterismo sem indicação classe I) 1,5% vs 7,2%. Metanálise do IQWiG para os estudos de alta certeza contra métodos funcionais (CATCH e PROMISE): OR 0,77 (IC95% 0,64–0,94; p = 0,011). Contra cateterismo direto, OR de 0,01 a 0,03, sem estimativa agrupada por heterogeneidade.

## Tabela S7 — Revascularização no modelo e cotas anuais de ordem de grandeza

Custo unitário observado no SIH 2025: R$ 7.713 por angioplastia coronariana; R$ 25.904 por revascularização cirúrgica.

| Cenário | Δ revascularização /100 | Ajuste por paciente | Neutralidade sem revasc. | **Neutralidade com revasc.** |
|---|---|---|---|---|
| Cintilografia + PRECISE (Δ CATE +4,1; revasc. 5,2% → 9,2%, ~3,75 PCI + 0,27 CRM) | +4,0 | −R$ 359 | R$ 817 | **R$ 458** |
| Cintilografia + Foy 2017, 13 ensaios, 9 de emergência (Δ CATE −2,6; revasc. 4,5% → 7,2%, RR agrupado 1,86, IC95% 1,43–2,43) | +2,7 | −R$ 208 | R$ 768 | **R$ 560** |
| Adoção aditiva + SCOT-HEART (Δ CATE −0,4 em 20 m / +0,5 em 5 a; revasc. 233 vs 201 / 279 vs 267) | +1,5 / +0,6 | −R$ 119 / −R$ 45 | R$ −3 / +4 | **R$ −122 / −41** |
| Gatekeeping, DISCHARGE (Δ CATE 75,1; revasc. 18,0% → 14,2%) | −3,8 | +R$ 293 | R$ 548 | **R$ 841** |
| Gatekeeping, CONSERVE (Δ CATE 66,0; revasc. 18% → 13%) | −5,0 | +R$ 386 | R$ 482 | **R$ 868** |

Cotas anuais a R$ 550, no ponto médio da faixa de Δ observada (`analise_final.py`):

| Cenário | P de neutralidade médio | Por 100 mil pacientes | Sobre o volume que pode substituir (2025) |
|---|---|---|---|
| Adoção aditiva (sem protocolo) | R$ −8 | +R$ 55,8 mi | +R$ 440 mi sobre 787.954 episódios |
| Teste ergométrico | R$ 24 | +R$ 52,6 mi | +R$ 315 mi sobre 598.695 |
| Mix médio do SIA | R$ 177 | +R$ 37,3 mi | +R$ 294 mi sobre 787.954 |
| Ecocardiografia de estresse | R$ 188 | +R$ 36,2 mi | +R$ 12 mi sobre 33.766 |
| Mix do NATS como publicado | R$ 309 | +R$ 24,1 mi | (sem volume próprio) |
| Mix do NATS por episódio | R$ 516 | +R$ 3,4 mi | (sem volume próprio) |
| Cintilografia, só exames | R$ 779 | −R$ 22,9 mi | −R$ 35 mi sobre 151.784 |
| Cintilografia com revascularização | R$ 509 | +R$ 4,1 mi | +R$ 6 mi sobre 151.784 |
| Filtro — CONSERVE / Reis / DISCHARGE / CAD-MAN (só exames) | R$ 482 / 527 / 548 / 625 | +6,8 / +2,3 / +0,2 / −7,5 mi | +11 / +4 / 0 / −12 mi sobre 163.803 cateterismos |
| Filtro — DISCHARGE com revascularização | R$ 841 | −R$ 29,1 mi | −R$ 48 mi sobre 163.803 |

Não constitui análise de impacto orçamentário: não há população elegível nem curva de difusão; são cotas de ordem de grandeza.

## Tabela S8 — Preço de neutralidade por estrato de probabilidade pré-teste, tabela completa (inclui os cenários omitidos da Tabela 2 do artigo)

| Estrato | Comparador (premissa) | C_substituído | Só exames + cateterismo | Com revascularização | Δ exigido a R$ 550 (só exames) |
|---|---|---|---|---|---|
| Qualquer estrato, sem protocolo | adoção aditiva (nada substituído) | R$ 0 | R$ −46 a +30 (SCOT-HEART: −3 a +4) | R$ −122 a −41 (revasc. do próprio SCOT-HEART) | 75,3 |
| Baixa | diferir / ajustar PPT (contrafactual sem teste) | R$ 0 | teto R$ 0 (Δ ≤ 0 por construção) | — | — |
| Baixa | teste ergométrico | R$ 32,20 | R$ −14 a +62 | R$ −297 a −195 | 70,9 |
| Não estratificado (PICO submetido) | mix médio do SIA | R$ 185,46 | R$ 139 a 215 | R$ −144 a −42 | 49,9 |
| Intermediária, sensibilidade | ecocardiografia de estresse | R$ 196,39 | R$ 150 a 226 | R$ −133 a −31 | 48,4 |
| Intermediária, sensibilidade | percurso do NATS por episódio | R$ 523,81 | R$ 477 a 554 | R$ 195 a 297 | 3,6 |
| Intermediária, com protocolo (cenário-base do estrato) | cintilografia de perfusão | R$ 786,83 | R$ 741 a 817 | **R$ 458 a 560** | já neutro |
| Intermediária, descritivo sem protocolo (sensibilidade) | teste ergométrico seguido de imagem em fração p dos pacientes; teto p ≤ 0,31 pelos volumes do SIA (toda cintilografia e eco a jusante de um TE), imagem a R$ 679 em média | ≤ R$ 242,75 | ≤ R$ 196 a 273 | ≤ R$ −87 a +16 | ≥ 42,1 |
| Já indicado a cateterismo (outro PICO) | cateterismo direto | cancela | R$ 482 a 625 | **R$ 841** (DISCHARGE) / **R$ 868** (CONSERVE) | 75,3 |

Fonte: `analise_final.py` e `output/out-limiar-por-estrato.csv`. Δ de cateterismo de primeira linha de −6,3 a +4,1 por 100. O débito de revascularização vem do PRECISE (+4,0/100) e de Foy 2017, 13 ensaios (+2,7/100, pareado com o Δ de cateterismo dos mesmos 13, −2,6), aplicados como envelope aos cenários de substituição; para a adoção aditiva usa-se a revascularização do próprio SCOT-HEART (+1,5/100 em 20 meses e +0,6/100 em 5 anos). O débito absoluto escala com a prevalência de doença: na probabilidade baixa, o envelope PRECISE/Foy (população intermediária) tende a superestimá-lo, sem alterar o sinal. Para o diferimento, o contrafactual não contém cateterismo diagnóstico, logo Δ ≤ 0 e o teto é R$ 0. O cenário descritivo supõe que todo exame de imagem funcional do SUS seja a jusante de um teste ergométrico: p = (151.784 cintilografias + 33.766 ecos) ÷ 598.695 ergometrias = 0,31 no máximo; é limite superior de volumes, não inferência ecológica sobre pacientes. Com C_CATE = R$ 772,80 (AIH), o filtro vai a R$ 510–662.

## Figura S1 — Análise de sensibilidade univariada (tornado)

*[A gerar por `analise_final.py`: variação de C_substituído (R$ 0 a 787), C_CATE (730 vs 773), Δ_CATE (−6,3 a +4,1; 66 a 86 no filtro), Δ_revasc (−5,0 a +4,0), C_revasc (angioplastia vs cirurgia) sobre o preço de neutralidade.]*

## Texto S1 — Desenho mínimo do microcusteio proposto

A limitação metodológica mais importante é a assimetria: a angioTC entra microcusteada (2022, corrigida) ou pelo preço proposto, e os comparadores e o cateterismo entram por tabela. Não trava a conclusão — o sinal da Tabela 2 do artigo depende de razões de preço que um microcusteio dificilmente inverteria na baixa, e a direção na intermediária já é declarada como incerta —, mas um revisor a apontará, com razão. Declara-se, portanto, como agenda, com o desenho mínimo que a corrigiria: microcusteio *bottom-up* na perspectiva do prestador — incluindo contraste iodado (o código de contraste tem faturamento zero: R$ 550 tem de embutir contraste, bomba injetora e acesso venoso), betabloqueador e nitrato para controle de frequência (condição de exame diagnóstico em 64 canais; exame não diagnóstico é cateterismo induzido) —, pelo método de custeio baseado em atividades e tempo (TDABC) ou por absorção — um só método, escolhido a priori conforme a Diretriz Metodológica de Estudos de Microcusteio do Ministério da Saúde (referência 29 do artigo) —, **da angioTC e dos comparadores no mesmo serviço** (teste ergométrico, ecocardiografia de estresse, cintilografia de perfusão em estresse e repouso, cateterismo diagnóstico), em ao menos **oito serviços do SUS**, cobrindo as cinco regiões e as três naturezas (público, filantrópico, universitário) sem exigir célula cheia e incluindo serviços do estrato pronto de 79. Componentes: depreciação e manutenção do equipamento (tomógrafo ≥64 canais, gama-câmara, ecocardiógrafo, sala de hemodinâmica); insumos por exame (contraste iodado, betabloqueador e nitrato, radiofármaco, kits e materiais de hemodinâmica); tempo de sala e de pessoal por etapa (preparo, aquisição, pós-processamento, laudo, enfermagem, técnico, médico executor); software e estação de trabalho; rateio administrativo; **exames não diagnósticos e repetições** (que diluem o custo por diagnóstico útil); e, decisivamente, **a dependência do custo unitário do volume** — custo fixo dividido por *throughput*, que decide se um tomógrafo do estrato pronto absorve a angioTC à margem ou exige turno adicional. Custo do prestador não é preço do pagador; o estudo deve reportar ambos. Um estudo desse porte custa uma fração da incerteza que resolve, e é condição para qualquer análise econômica simétrica — inclusive a do demandante.

## Texto S2 — Regras de análise pré-registradas e emendas declaradas

# Regras de análise fixadas antes de olhar o dado

Registradas em 16/08/2026 com a extração das OCI em 72%, para evitar o padrão dos
três erros anteriores (fórmula correta aplicada fora do domínio).

## Unidade de análise: episódio remunerado

1. **OCI como episódio principal.** Se a OCI (`0902*`) é registrada como procedimento
   principal e os componentes aparecem com valor zerado, o custo do episódio é o
   valor da OCI. **Os componentes não são somados novamente.** Confirmado no PA:
   963 ergometrias, 832 cintilografias e 134 ecos de estresse com `PA_VALAPR = 0`
   em 25 UFs — o mecanismo APAC previsto na regulamentação está no dado.

2. **Procedimentos isolados fora da OCI** continuam entrando separadamente no mix,
   pareados por episódio (cintilografia estresse + repouso = 1).

3. **Dois pathways, reportados separadamente e depois ponderados:**
   - legacy pathway: custo médio dos episódios fora da OCI
   - OCI pathway: custo médio das linhas organizadas de SCC (0034/0042/0050)
   - ponderado nacional: intercepto da reta de primeira linha

4. **O intercepto só entra na reta de primeira linha.** No gatekeeping o custo
   prévio é comum aos braços e cancela — a reta inferior não muda com as OCI.

## Desfecho econômico: cateterismo total

5. Todo Δ da figura de neutralidade é **cateterismo total por braço randomizado**.
   Cateterismo sem DAC obstrutiva é eficiência diagnóstica, seção própria, fora
   do cálculo.

6. Cada Δ carrega sua janela temporal. Os pontos não são metanálise.

## Auditoria final (após a extração fechar)

Exclusivamente de **unidades de análise e dupla contagem**. Não buscar novos desfechos.

## Emendas posteriores (não pré-registradas — declaradas como tal)

**v5, 16/08/2026, após leitura da v4 pelo coautor sênior.** Nenhuma equação, código,
janela ou desfecho mudou. Duas apresentações novas dos mesmos parâmetros:

7. **Cenário "adoção aditiva (sem protocolo)"**: `C_substituído = 0` — a angiotomografia
   somada ao percurso atual, sem substituir exame. Algebricamente é a equação de
   gatekeeping com o Δ dos ensaios de primeira linha. Motivo: sem código SIGTAP e sem
   protocolo vinculante, é o cenário de adoção mais provável, e estava implícito
   (SCOT-HEART "à parte") em vez de nomeado. Sexto cenário da Tabela 4.
8. **Estratificação por probabilidade pré-teste como premissa declarada**: baixa →
   comparador realista "nenhum exame" (diferir/ajustar PPT/escore de cálcio) ou
   ergometria; intermediária → ecocardiografia de estresse ou cintilografia (ou o
   percurso do NATS por episódio); mix médio do SIA = PICO como submetido, sem
   estratificar. O SIA não distingue estratos; o modelo distingue por premissa. O
   débito de revascularização (PRECISE, Foy 2017) passa a ser aplicado a **todos** os
   cenários de primeira linha, não só ao mais favorável.

**v5.1, 16/08/2026, após a terceira rodada cega.** Correções de proveniência e pareamento,
sem mudança de equação:

9. **SCOT-HEART com os dados primários**: cateterismo 409 vs 401 (JACC 2016, mediana
   20 meses) e 491 vs 502 (NEJM 2018, 5 anos); revascularização 233 vs 201 e 279 vs 267.
   O valor "17,5% vs 16,3% aos 6 meses" usado até a v5 não tem proveniência nas
   publicações primárias e foi retirado. Para o cenário aditivo, a revascularização é a
   do próprio SCOT-HEART, não o envelope PRECISE/Foy.
10. **CONSERVE entra na revascularização** (13% vs 18%, abstract) como segundo ensaio de
    gatekeeping com crédito (R$ 868), ao lado do DISCHARGE (R$ 841).
11. **Foy 2017 pareado 13-com-13**: o Δ de cateterismo dos 13 ensaios (−2,6) acompanha a
    revascularização dos mesmos 13 (7,2% vs 4,5%); o subgrupo estável (−2,9) continua na
    faixa de Δ, mas não é pareado com revascularização de outra população.
12. Revascularização sem desagregação angioplastia/cirurgia é valorada como angioplastia;
    débitos de primeira linha incluem CRM (PRECISE) — assimetria conservadora contra o
    gatekeeping, declarada.
13. Cotas anuais ancoradas no volume que cada cenário pode substituir (cintilografia
    sobre 151.784, não sobre 787.954) e expressas também por 100 mil pacientes.

**v5.2, 17/08/2026, após leitura no papel de coautor.** Sem mudança de equação:

14. **Cenário descritivo da intermediária sem protocolo:** teste ergométrico seguido de
    imagem funcional em fração p dos pacientes; p tem teto pelos volumes do SIA,
    p ≤ (cintilografias + ecos) ÷ ergometrias = 0,31 (supõe toda imagem a jusante de um TE),
    com a imagem ao preço médio ponderado (R$ 679): C ≤ R$ 242,75. É limite superior de
    volumes, não inferência ecológica sobre pacientes. Sensibilidade, não cenário-base.
15. **Recalibração das premissas por estrato (juízo clínico declarado):** baixa = ergometria
    (o "nenhum exame" é normativo; diferimento vira nota, teto R$ 0); aditiva = cenário de
    referência de qualquer estrato sem protocolo (linha própria); intermediária com
    protocolo = cintilografia (cenário-base); eco e NATS = sensibilidade.



## Checklist CHEERS 2022

*[A anexar na submissão: itens aplicáveis a análise de limiar; itens não aplicáveis (horizonte de longo prazo, desconto, QALY, análise probabilística) marcados como tal.]*
