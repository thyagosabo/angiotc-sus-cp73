# Contribuição à Consulta Pública nº 73/2026 — Conitec

**Tema:** Angiotomografia coronariana como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de doença arterial coronariana estável.

**Natureza da contribuição:** técnico-científica.

> **VERSÃO 2 — RASCUNHO.** Duas dependências abertas, marcadas no texto como `[PENDENTE]`:
> extração das OCI de síndrome coronariana crônica no SIA 2025, e ancoragem do Δ de
> angiografias evitadas na literatura de ensaios. Nenhuma conclusão da síntese depende delas.

---

## 1. Objeto da contribuição

O Relatório de Recomendação Preliminar registra que a deliberação desfavorável de 3 de julho de 2026 (153ª Reunião Ordinária) foi fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à **capacidade de implementação da tecnologia no SUS** e à delimitação da população elegível. O Comitê destacou como essenciais ao esclarecimento em consulta pública, entre outros pontos, "a estimativa da capacidade instalada", "a necessidade ou não de aquisição de equipamentos" e "o impacto real sobre a realização de angiografias invasivas e testes funcionais".

Esta contribuição responde a esses pontos com análise nacional construída **exclusivamente sobre bases públicas** — CNES, SIA/SUS, SIH/SUS, SIGTAP e IBGE. Nenhuma dessas bases é citada no relatório preliminar para caracterização de capacidade instalada.

Método, endereços de origem e código no Apêndice A. Todos os números são reprodutíveis.

---

## 2. Capacidade instalada: o que o cadastro nacional já permite responder

**Fonte:** CNES, arquivos de equipamentos (`EQ`), competência 06/2026, 27 UFs. Considerados apenas equipamentos com `IND_SUS=1` e `QT_USO>0`.

A **Portaria SAES/MS nº 3.695, de 15 de janeiro de 2026** desmembrou o código genérico `11 — Tomógrafo Computadorizado` em categorias por número de canais: `26` (4 canais), `27` (16), `28` (32), `29` (64) e `30` (128). O código `31` corresponde a Tomógrafo Simulador para Radioterapia, de uso exclusivo, e não integra capacidade diagnóstica.

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

### 2.2 A reclassificação está incompleta — e isso é o achado operacional central

Em 06/2026, apenas **26,8% dos estabelecimentos** haviam migrado do código genérico para as categorias por canal. Dos 3.395 estabelecimentos com tomógrafo disponível ao SUS, **2.534 permanecem sem especificação declarada**.

A portaria concede prazo de **três competências** a contar da implementação no sistema CNES para que gestores realizem a reclassificação.

O enunciado correto da capacidade é, portanto:

> **432 equipamentos de ≥64 canais estão documentados como disponíveis ao SUS. Esse é um piso de capacidade documentada, não uma estimativa da capacidade real** — o número verdadeiro é 432 somado a uma fração desconhecida dos 2.785 equipamentos ainda não classificados.

**Recomendação operacional:** a apreciação final deve ocorrer sobre o cadastro reclassificado. Se o prazo regulamentar se encerrar antes da deliberação, a Conitec disporá, pela primeira vez, do inventário nacional completo de tomógrafos por faixa de canais — precisamente o dado cuja ausência motivou parte da recomendação preliminar. Recomenda-se condicionar a análise de capacidade a essa competência.

### 2.3 Estratos de prontidão para implementação

Possuir hardware compatível não equivale a estar apto. Cruzando o estrato confirmado ≥64 canais com dois marcadores independentes — sala de hemodinâmica no mesmo CNES (código `10`) e produção coronariana efetivamente realizada em 2025 (SIH, angioplastia ou revascularização) — obtém-se:

| Estrato | Estabelecimentos |
|---|---|
| ≥64 canais confirmado | 315 |
| ≥64 canais **+ hemodinâmica no mesmo CNES** | 114 |
| ≥64 canais **+ produção coronariana documentada em 2025** | 101 |
| **≥64 canais + hemodinâmica + produção coronariana** | **83** |

O estrato de 83 estabelecimentos reúne hardware comprovadamente compatível, infraestrutura cardiovascular instalada e atividade coronariana documentada. É o conjunto com maior plausibilidade de implantação imediata sem investimento adicional.

A co-localização com hemodinâmica **não é requisito técnico** para angiotomografia — um serviço de radiologia com tomógrafo de 128 canais e cardiologista habilitado realiza o exame sem sala de hemodinâmica, e um hospital com hemodinâmica e tomógrafo de 16 canais não está tecnicamente apto. O cruzamento é adotado como marcador de maturidade cardiovascular institucional, não como limite inferior de capacidade.

### 2.4 Distribuição e equidade

Densidade nacional de equipamentos compatíveis confirmados: **2,02 por milhão de habitantes** (IBGE 2025, 213.421.037 hab.).

- **Amapá, Piauí e Tocantins não possuem nenhum tomógrafo de ≥64 canais confirmado** disponível ao SUS.
- **Doze unidades federativas não possuem nenhum estabelecimento no estrato de prontidão:** AC, AL, AM, AP, GO, MT, PA, PI, RO, RR, SE e TO.
- São Paulo concentra 164 equipamentos compatíveis e 24 estabelecimentos prontos; o Distrito Federal lidera em densidade (6,01 por milhão).

A desigualdade medida sobre hardware efetivamente compatível é **mais acentuada** do que a medida sobre o parque tomográfico agregado. Projeções de difusão ancoradas no total de tomógrafos superestimam a capacidade acessível, e o fazem de modo desigual entre regiões.

Tabela completa por UF: `output/out-capacidade-canais-uf.csv`.

---

## 3. Cenário atual: o que o SUS efetivamente realiza

**Fonte:** SIA/SUS e SIH/SUS, competências 01–12/2025, 27 UFs, 395 arquivos processados sem perda. Códigos conferidos contra SIGTAP competência 08/2026.

### 3.1 A unidade de análise é o episódio, não o procedimento faturado

A cintilografia miocárdica de perfusão é registrada sob dois códigos distintos — estresse (`0208010025`) e repouso (`0208010033`). Em 2025 o SUS registrou 151.784 e 151.225 respectivamente: **151.225 pares e apenas 559 registros de estresse sem repouso correspondente**. Esse pareamento é a assinatura de um exame executado em duas etapas, não de dois exames independentes.

Validação externa: a análise de custo-efetividade da angiotomografia no SUS publicada em 2022 (Arquivos Brasileiros de Cardiologia) precificou a cintilografia miocárdica como **unidade única, R$ 791,59 a valores de 2020**. A soma dos dois códigos no SIA 2025 é **R$ 788,24** — diferença de 0,4%.

Contar procedimentos faturados infla o denominador em 19%. A análise abaixo usa episódios.

| Episódio de investigação funcional | Episódios | Participação |
|---|---|---|
| Teste ergométrico | 598.695 | 76,0% |
| Cintilografia de perfusão (estresse + repouso) | 151.784 | 19,3% |
| Ecocardiografia de estresse | 33.766 | 4,3% |
| Cintilografia de câmaras — esforço | 3.709 | 0,5% |
| **Total** | **787.954** | |
| **Gasto** | **R$ 146,1 mi** | **R$ 185,46 por episódio** |

Cateterismo cardíaco (`0211020010`), registrado no SIA: 163.803 procedimentos, R$ 119,6 mi, custo médio **R$ 730,14**.

### 3.2 Composição da investigação funcional

O teste ergométrico responde por **76,0% dos episódios de investigação funcional identificados nos códigos selecionados do SIA em 2025**, a custo médio de R$ 32,20.

Esta é uma afirmação sobre **registros administrativos selecionados**, não sobre a população elegível à angiotomografia. O teste ergométrico possui indicações além da investigação inicial de doença arterial coronariana estável — avaliação de capacidade funcional, arritmias de esforço, estratificação pré-operatória e acompanhamento de doença conhecida. Não é possível, sem identificação de paciente e indicação clínica, afirmar que essa proporção se reproduz na população-alvo da tecnologia.

A implicação que resiste a essa limitação é mais restrita e ainda assim relevante: **a avaliação econômica submetida comparou a angiotomografia predominantemente a exames funcionais de custo médio-alto, enquanto o gasto observado do SUS concentra-se no exame de menor custo da tabela.** Qualquer modelo que assuma substituição majoritária de cintilografia superestima a economia.

`[PENDENTE]` As Ordens de Cuidado Integrado (OCI) de síndrome coronariana crônica — `0902010034` (avaliação diagnóstica inicial, R$ 270,00), `0902010042` (progressão I, R$ 250,00) e `0902010050` (progressão II, R$ 840,00) — definem, na própria tabela do SUS, o episódio diagnóstico para essa condição. Sua produção em 2025 está em extração e permitirá caracterizar a população contemporânea de investigação de SCC de forma muito mais específica do que a soma de testes cardiovasculares. Se o volume for relevante, essas OCI substituem a reconstrução por pareamento acima.

### 3.3 Angiotomografia coronariana é administrativamente invisível

Não existe código para angiotomografia coronariana na Tabela de Procedimentos do SUS (SIGTAP 08/2026, 5.023 procedimentos verificados). A produção atual não é mensurável: ou é registrada sob código genérico de tomografia, ou não é registrada. Isso é coerente com o registro, no relatório preliminar, de que o exame ocorre em serviços públicos e conveniados sem utilização estruturada e sem procedimento específico.

Verificou-se adicionalmente que o código `0206030045 — CONTRASTE PARA TOMOGRAFIA COMPUTADORIZADA` **não registra faturamento no SIA em 2025**, o que impede seu uso como marcador de serviços com capacidade para exames contrastados.

**Consequência:** nenhum custo unitário para a angiotomografia pode ser ancorado em produção histórica do SUS. O microcusteio contemporâneo, com abertura completa de componentes, é condição necessária.

### 3.4 Escala da cardiologia intervencionista — contexto, não denominador

Em 2025 o SUS registrou 137.595 angioplastias coronarianas (R$ 1.112 mi, 289 estabelecimentos) e 16.991 revascularizações miocárdicas (R$ 423 mi, 219 estabelecimentos), em uma rede de 290 estabelecimentos.

**Estes números são apresentados como contexto de escala e não como denominador econômico da estratégia.** A população submetida a esses procedimentos inclui infarto agudo do miocárdio, síndrome coronariana aguda, doença coronariana previamente conhecida e doença multiarterial — populações que não são desfecho da investigação de pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária. Atribuir esse gasto à via diagnóstica da doença estável seria erro de denominador.

Conceitualmente, a angiotomografia pode reduzir angiografias invasivas **diagnósticas** de resultado negativo sem reduzir revascularizações, e pode inclusive aumentar revascularizações apropriadas ao identificar doença antes não detectada. A sustentabilidade orçamentária da estratégia não depende de reduzir este montante.

---

## 4. Análise de limiar: quanto o SUS poderia pagar

### 4.1 Por que limiar e não estimativa pontual

O SIA não possui identificador de paciente utilizável. Não é possível determinar se um cateterismo registrado ocorreu após um teste funcional específico, na mesma pessoa, ou na mesma indicação clínica. A razão entre contagens agregadas de cateterismos e de testes funcionais **não é uma probabilidade condicional** e não pode ser usada para projetar redução de procedimentos: fazê-lo seria inferência ecológica.

A análise abaixo não estima quantas angiografias a angiotomografia evitaria. Ela responde à pergunta inversa, que os dados sustentam:

> **Quantas angiografias diagnósticas por 100 pacientes seria necessário evitar, a cada preço, para que a estratégia fosse orçamentariamente neutra?**

O julgamento sobre a plausibilidade clínica de cada valor permanece com o leitor especializado — não é produzido por este modelo.

### 4.2 Formulação

Sob substituição de um episódio funcional por uma angiotomografia:

```
P_angioTC  =  C_episódio_atual  +  (Δ_CATE / 100) × C_CATE
Δ_CATE     =  (P_angioTC − C_episódio_atual) × 100 / C_CATE
```

com `C_episódio_atual = R$ 185,46` e `C_CATE = R$ 730,14`, ambos observados no SIA 2025. `Δ_CATE` é parâmetro declarado, não quantidade estimada dos dados.

### 4.3 Resultado

| Referência de preço | Valor | Natureza | Δ CATE/100 necessário |
|---|---|---|---|
| TC de tórax + contraste (SIGTAP) | R$ 196,41 | tabela SUS, proxy inferior | 1,5 |
| Microcusteio SUS 2022, valores de 2020 | R$ 452,05 | custo, não corrigido | 36,5 |
| **Microcusteio SUS 2022 corrigido a jul/2026** (IPCA +37,7%) | **R$ 622,54** | custo, base comparável | **59,9** |
| CBHPM 2026 | R$ 1.311,95 | preço de saúde suplementar | 154,3 — **impossível** |

**Resultado robusto:** ao preço praticado na saúde suplementar, a neutralidade exigiria evitar mais angiografias do que pacientes investigados. É logicamente impossível sob qualquer premissa de comportamento downstream, qualquer base de custo e qualquer tamanho de população elegível. A CBHPM não constitui referência admissível de custo de oportunidade do SUS.

Ao custo microcusteado e corrigido monetariamente, o requisito é de **59,9 angiografias evitadas por 100 pacientes**. A seção seguinte confronta esse requisito com o observado em ensaios randomizados.

### 4.4 Confronto com a evidência: o Δ observado e o Δ necessário

Ensaios randomizados de estratégia diagnóstica reportam taxas absolutas de angiografia invasiva por braço. Convertendo para a convenção desta análise (Δ positivo = angiografias evitadas por 100 pacientes):

| Ensaio | Comparador | Δ observado /100 | Preço de neutralidade correspondente |
|---|---|---|---|
| CAPP (1 ano) | funcional-primeiro (ergometria) | **−6,4** | R$ 138,73 |
| PROMISE (90 dias) | funcional-primeiro | **−4,1** | R$ 155,52 |
| Foy 2017, subgrupo estável | funcional-primeiro | **−2,9** | R$ 164,29 |
| Foy 2017, 13 ensaios | funcional-primeiro | −2,6 | R$ 166,48 |
| SCOT-HEART (6 meses) | usual care | −1,2 | R$ 176,70 |
| CRESCENT-I (1 ano) | funcional-primeiro | −1,0 | R$ 178,16 |
| SCOT-HEART (5 anos) | usual care | +0,5 | R$ 189,11 |
| CRESCENT-II (6 meses) | funcional-primeiro | +1,4 | R$ 195,68 |
| PRECISE (11,8 meses) | usual care | +4,1 | R$ 215,40 |

**Contra comparadores não invasivos, a angiotomografia não reduz de forma consistente o número total de angiografias invasivas — na maioria dos ensaios o aumenta.** A faixa observada vai de −6,4 a +4,1 por 100, e a metanálise de Foy (2017), no subgrupo de dor torácica estável, aponta aumento de 2,9 por 100.

O preço de neutralidade correspondente a toda a faixa observada situa-se entre **R$ 138,73 e R$ 215,40**.

O requisito de 59,9 angiografias evitadas por 100, necessário para sustentar o custo microcusteado corrigido de R$ 622,54, é **14,6 vezes maior que o melhor resultado observado em qualquer ensaio com comparador não invasivo**. A distância não é de magnitude discutível; é de ordem de grandeza.

### 4.4.1 O protocolo importa: gatekeeping por escore de cálcio

Os dois ensaios CRESCENT aplicaram **escore de cálcio como filtro antes da angiotomografia**, realizando o exame contrastado apenas em pacientes com cálcio detectável (Agatston 1–400); o CRESCENT-II acrescentou perfusão por TC antes do encaminhamento invasivo. O CAPP realizou angiotomografia em todos os pacientes do braço de intervenção, independentemente do escore de cálcio.

| Protocolo | Δ observado /100 | Preço de neutralidade |
|---|---|---|
| Angiotomografia em todos (CAPP) | −6,4 | R$ 138,73 |
| Filtrada por escore de cálcio (CRESCENT-I e II) | −1,0 a +1,4 | R$ 178,16 a R$ 195,68 |

A diferença de desenho é a explicação mais plausível para a divergência de direção entre ensaios com o mesmo comparador. **A especificação do protocolo altera o resultado orçamentário em cerca de R$ 50 por episódio** — magnitude comparável à de vários dos parâmetros discutidos na avaliação econômica.

Isso responde diretamente a um dos pontos que o Comitê listou como essencial ao esclarecimento: "os critérios para evitar uso inadequado da tecnologia". Recomenda-se que qualquer incorporação especifique o protocolo, e não apenas a tecnologia.

**Ressalvas.** PROMISE contabiliza janela de 90 dias, e SCOT-HEART demonstra dependência do horizonte — aumento em 6 meses, nulo em 5 anos (HR 1,00). O braço de intervenção do PRECISE não é angiotomografia pura, incluindo diferimento de teste em pacientes de risco mínimo. A metanálise de Foy inclui 9 de 13 ensaios em população de emergência; utilizou-se o subgrupo estável. As contagens por braço do CAPP não constam do artigo primário, que reporta angiografias apenas estratificadas por resultado do teste índice; os totais provêm do gráfico de floresta de Foy (2017). Em CRESCENT-I e CRESCENT-II as diferenças de angiografia total não são estatisticamente significativas (p = 0,843 e p = 0,860).

### 4.5 O caso econômico existe — para outra indicação

Ensaios com comparador **invasivo-primeiro**, isto é, pacientes já encaminhados para cateterismo, produzem resultado inteiramente distinto:

| Ensaio | Δ observado /100 | Preço de neutralidade |
|---|---|---|
| DISCHARGE (manejo inicial) | **+75,1** | **R$ 733,80** |
| CONSERVE (1 ano) | **+66,0** | **R$ 667,35** |

Nessa indicação, o preço de neutralidade **supera o custo microcusteado corrigido de R$ 622,54**. A angiotomografia como filtro anterior a um cateterismo já indicado é, pelos dados disponíveis, orçamentariamente neutra ou economizadora.

Estes Δ não são intercambiáveis com os da seção anterior: a população já estava referenciada para procedimento invasivo, e a taxa do braço comparador é de 97% por construção do desenho. Trata-se de pergunta clínica diferente.

**A implicação é direta para esta consulta.** A proposta em apreciação é de incorporação como exame de **primeira linha**, substituindo investigação funcional. É precisamente a indicação para a qual a evidência não sustenta neutralidade orçamentária. A indicação para a qual a economia se sustenta — filtro antes de cateterismo já indicado — não é a que está sendo requerida.

Recomenda-se que a apreciação final considere explicitamente essa distinção, inclusive a possibilidade de incorporação restrita à indicação de gatekeeping, com critérios de elegibilidade correspondentes.

### 4.6 O benefício que a evidência sustenta não é orçamentário

Há um desfecho em que a angiotomografia é consistente em **todos** os ensaios que o reportam, independentemente do comparador: a redução de angiografias invasivas sem doença obstrutiva.

| Ensaio | AngioTC | Comparador | Evitadas /100 |
|---|---|---|---|
| PRECISE — cateterismo sem DAC obstrutiva | 2,6% | 10,2% | **7,6** |
| CRESCENT-II — ICA sem indicação classe I | 1,5% | 7,2% | **5,7** |
| PROMISE — cateterismo sem obstrução | 3,4% | 4,3% | 0,9 |
| SCOT-HEART — artérias normais ao cateterismo | 20 casos | 56 casos | HR 0,39 (0,23–0,68) |

O ganho de rendimento diagnóstico é o achado robusto da literatura; a redução de volume total, não. Avaliado ao valor SIA do cateterismo, o resultado do PRECISE corresponde a R$ 55,49 por paciente investigado — insuficiente para fechar a diferença de preço, mas relevante como argumento de adequação de indicação e de exposição do paciente a procedimento invasivo desnecessário.

Esta contribuição registra o ponto porque a decisão de incorporação não se esgota em impacto orçamentário: evitar cateterismo sem achado obstrutivo é benefício clínico e de segurança que a análise econômica, isoladamente, não captura.

### 4.4 Independência em relação à população elegível

O preço de neutralidade é grandeza **por episódio**. Sob substituição 1:1, **independe do tamanho da população elegível**. A magnitude da população determina *quanto* se gasta a mais, não *se* se gasta a mais.

Este resultado contorna diretamente a incerteza que motivou parte da recomendação preliminar: não é necessário resolver a população elegível para delimitar o preço admissível.

### 4.5 Observação sobre a base de comparação

O estudo de 2022 microcusteou a cintilografia miocárdica em R$ 791,59 a valores de 2020 — aproximadamente R$ 1.090 corrigidos. O SUS remunera hoje R$ 788,24 pelo mesmo exame, em valores nominais, isto é, cerca de 72% do custo estimado.

O `C_episódio_atual` de R$ 185,46 é, portanto, **preço de tabela, não custo de produção**. Comparar uma tecnologia microcusteada a valores contemporâneos contra comparadores remunerados abaixo do custo e sem correção é comparação assimétrica. Registra-se explicitamente para que a apreciação final possa ponderá-la, em vez de deixá-la implícita no denominador.

---

## 5. Síntese

1. **O CNES permite, desde a Portaria SAES/MS nº 3.695/2026, identificar tomógrafos por faixa de canais.** Em 06/2026 há **432 equipamentos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS.
2. **A reclassificação está 26,8% concluída.** Os 432 são piso de capacidade documentada; 2.785 equipamentos permanecem sem especificação. Recomenda-se que a análise de capacidade da apreciação final seja realizada sobre o cadastro reclassificado.
3. **83 estabelecimentos** reúnem hardware ≥64 canais, hemodinâmica co-localizada e produção coronariana documentada — o estrato de maior plausibilidade de implantação imediata.
4. **Doze UFs não possuem nenhum estabelecimento nesse estrato**; AP, PI e TO não possuem nenhum tomógrafo de ≥64 canais confirmado disponível ao SUS.
5. A investigação funcional do SUS concentra-se no **teste ergométrico (76,0% dos episódios identificados, R$ 32,20)**, e não em exames de custo médio-alto — ressalvado que a composição da população elegível não é identificável nos registros administrativos.
6. **A neutralidade orçamentária como exame de primeira linha não é sustentada pela evidência.** O requisito de 59,9 angiografias evitadas por 100 pacientes, ao custo microcusteado corrigido de R$ 622,54, é **14,6 vezes maior que o melhor resultado observado** em ensaios com comparador não invasivo. A faixa observada na literatura (−6,4 a +4,1 por 100) corresponde a preços de neutralidade entre R$ 138,73 e R$ 215,40. Ao preço da saúde suplementar, a neutralidade é logicamente impossível.
7. **O caso econômico existe, mas para outra indicação.** Em ensaios com comparador invasivo-primeiro — pacientes já encaminhados a cateterismo — o Δ observado é de +66 a +75 por 100, e o preço de neutralidade (R$ 667 a R$ 734) **supera** o custo microcusteado corrigido. A indicação de gatekeeping antes de cateterismo já indicado é orçamentariamente sustentável; a de primeira linha, que é a requerida, não é. Recomenda-se que a apreciação final considere explicitamente a incorporação restrita a essa indicação.
8. **O protocolo altera o resultado.** Angiotomografia filtrada por escore de cálcio (CRESCENT) e aplicada universalmente (CAPP) diferem em cerca de R$ 50 por episódio no preço de neutralidade. Qualquer incorporação deve especificar o protocolo, não apenas a tecnologia.
9. **O benefício robusto da tecnologia não é orçamentário, é de adequação.** A redução de cateterismos sem doença obstrutiva é consistente em todos os ensaios que a reportam (5,7 a 7,6 por 100), ao contrário da redução de volume total. A decisão de incorporação não deveria se esgotar em impacto orçamentário.
10. Não há código SIGTAP para a tecnologia; microcusteio contemporâneo é condição necessária para qualquer análise econômica reprodutível.

Nada nesta contribuição se pronuncia sobre o mérito clínico da tecnologia. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária, nos termos em que o Comitê solicitou esclarecimento.

---

## Apêndice A — Reprodutibilidade

| Fonte | Endereço | Competência |
|---|---|---|
| CNES — equipamentos | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ/` | 06/2026 |
| SIA/SUS — produção ambulatorial | `.../SIASUS/200801_/Dados/` | 01–12/2025 |
| SIH/SUS — internações | `.../SIHSUS/200801_/Dados/` | 01–12/2025 |
| SIGTAP | `ftp://ftp2.datasus.gov.br/public/sistemas/tup/downloads/` | 08/2026 |
| População | IBGE, agregado 6579, variável 9324 | 2025 |
| IPCA (correção monetária) | IBGE, agregado 1737, variável 2266 | 12/2020 → 07/2026 |
| Portaria SAES/MS nº 3.695 | Diário Oficial da União | 15/01/2026 |

**Advertência sobre tabelas de conversão.** As tabelas `.cnv` distribuídas em `CNES/200508_/Auxiliar/TAB_CNES.zip` (competência 07/2026) listam apenas o código `0111 — Tomógrafo Computadorizado` e **não refletem o desmembramento por canais** estabelecido pela Portaria 3.695/2026, embora os códigos 26–30 já estejam presentes nos arquivos de dados. Análises que derivem a lista de códigos dessas tabelas, em vez de enumerar os valores efetivamente presentes nos microdados, excluirão silenciosamente todos os equipamentos já reclassificados.

**Nota de processamento.** Arquivos SIA de MG, RJ, RS e SP são particionados (`PASP2501a.dbc`, `…b`, `…c`, `…d`). Rotinas que constroem nomes de arquivo sem sufixo de partição perdem silenciosamente 71 dos 395 arquivos do ano — as quatro UFs mais populosas. O código enumera o diretório remoto, verifica presença das 27 UFs e distingue falha de download de arquivo vazio. Total processado: **395/395 arquivos SIA e 324/324 SIH, sem perdas**.

Leitura de `.dbc`: bibliotecas `datasus-dbc` e `dbfread` (Python).
Scripts e tabelas intermediárias: [inserir DOI/URL do repositório antes de submeter].

---

**Autor:** [nome, titulação, afiliação, ORCID]
**Conflitos de interesse:** [declarar]
**Data:** agosto de 2026

---

## Apêndice B — Ensaios randomizados utilizados na ancoragem do Δ

| Ensaio | Ano / periódico | Comparador | N (int/ctrl) | ICA int | ICA ctrl | Janela |
|---|---|---|---|---|---|---|
| PROMISE | 2015 NEJM · PMID 25773919 | funcional-primeiro | 4996 / 5007 | 609 (12,2%) | 406 (8,1%) | 90 dias |
| SCOT-HEART | 2018 NEJM · PMID 30145934 | usual care | 2073 / 2073 | 491 (23,7%) | 502 (24,2%) | 5 anos |
| SCOT-HEART | 2016 JACC · PMID 27081014 | usual care | 2073 / 2073 | 17,5% | 16,3% | 6 meses |
| CRESCENT-I | 2016 Eur Heart J · PMID 26746631 | funcional-primeiro | 239 / 108 | 29 (12,1%) | 12 (11,1%) | 1 ano |
| CRESCENT-II | 2018 JACC Img · PMID 29248657 | funcional-primeiro | 130 / 138 | 17 (13,1%) | 20 (14,5%) | 6 meses |
| CAPP | 2015 EHJ-CI · PMID 25473041 | ergometria | 243 / 245 | 66 | 51 | 1 ano |
| PRECISE | 2023 JAMA Cardiol · PMID 37610731 | usual testing | 1057 / 1046 | 135 (12,8%) | 177 (16,9%) | 11,8 meses |
| Foy (metanálise) | 2017 JAMA Intern Med · PMID 28973101 | funcional | 10 315 / 9 777 | 11,7% | 9,1% | 18 meses |
| **DISCHARGE** | 2022 NEJM · PMID 35240010 | **invasivo-primeiro** | 1808 / 1753 | 404 (22,3%) | 1708 (97,4%) | manejo inicial |
| **CONSERVE** | 2019 JACC Img · PMID 30553687 | **invasivo-primeiro** | 823 / 808 | 23% | 89% | 1 ano |

Os dois últimos não são comparáveis aos demais: a população já estava referenciada para procedimento invasivo e a taxa do braço controle é determinada pelo desenho.

**Cateterismos sem doença obstrutiva evitados** — desfecho consistente em todos os ensaios que o reportam:

| Ensaio | Intervenção | Controle | Evitados /100 |
|---|---|---|---|
| PRECISE | 2,6% | 10,2% | 7,6 |
| CRESCENT-II (sem indicação classe I) | 1,5% | 7,2% | 5,7 |
| PROMISE | 3,4% | 4,3% | 0,9 |
| CONSERVE (% dos cateterismos) | 24,6% | 61,1% | — |
| SCOT-HEART | 20 casos | 56 casos | HR 0,39 (0,23–0,68) |
