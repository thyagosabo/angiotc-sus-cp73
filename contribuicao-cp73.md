# Contribuição à Consulta Pública nº 73/2026 — Conitec

**Tema:** Angiotomografia coronariana como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de doença arterial coronariana estável.

**Natureza da contribuição:** técnico-científica.

---

## Quadro-resumo

| Pergunta do Comitê | Resposta desta contribuição |
|---|---|
| Capacidade instalada | **432 tomógrafos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS (CNES 06/2026) — piso documentado; 2.785 equipamentos ainda sem especificação de canais. **79 estabelecimentos** reúnem hardware declarado compatível, hemodinâmica e produção coronariana em 2025. 12 UFs não têm nenhum estabelecimento nesse estrato; 3 não têm tomógrafo ≥64 confirmado. |
| Custo do percurso atual | R$ 185,46 por episódio de investigação funcional (mix médio observado no SIA 2025); cateterismo R$ 730,14. Ambos são preços de tabela, não custos de produção. |
| Preço admissível | Depende de **qual exame a AngioTC substitui e de quanta revascularização induz** — ambos não identificáveis nos registros. Nos ensaios com comparador não invasivo, o Δ de cateterismo total foi de −6,3 a +4,1 por 100. **Sem protocolo de posicionamento (adoção aditiva — a AngioTC somada ao percurso, nada substituído: o cenário de referência se a incorporação criar o código sem dizer o que sai do percurso), nenhum preço plausível é neutro: R$ −46 a +30, teto de R$ 30.** Só com exames e cateterismo, a neutralidade vai de **R$ 139–215** (mix médio do SIA) a **R$ 741–817** (cintilografia). Incluindo a revascularização observada nos ensaios, o cenário cintilografia cai para **R$ 458–560** e os demais ficam abaixo de R$ 300. O preço proposto pelo demandante, R$ 550,00, está **fora do alcance na probabilidade baixa** (comparador: nenhum exame ou ergometria) e **dentro da zona de incerteza na intermediária apenas quando substitui cintilografia**. |
| Outro PICO | Em pacientes com cinecoronariografia eletiva já indicada — filtro pré-cateterismo (4 ensaios), o preço de neutralidade é de **R$ 482–625** só com exames; incluindo a menor revascularização observada, sobe a **R$ 841** (DISCHARGE) e **R$ 868** (CONSERVE). População distinta, não intercambiável com a apreciada. |
| Conclusão | **A sustentabilidade orçamentária depende de três parâmetros que os registros administrativos não identificam — o exame substituído, a revascularização induzida e a posição no percurso.** Estratificando por probabilidade pré-teste com o comparador que as diretrizes indicam, a mesma tecnologia ao mesmo preço é expansiva na baixa, fica na zona de incerteza na intermediária quando substitui cintilografia, e tem espaço no filtro pré-cateterismo. O PICO submetido reproduz a formulação da Diretriz SBC/CBR de TC/RM 2024, que trata "baixa ou intermediária" como faixa única; a Diretriz SBC de Síndrome Coronariana Crônica 2025, posterior e específica, estratifica (IIb na baixa; I-A na intermediária) e condiciona a escolha do exame inicial à capacidade funcional, ao ECG basal, ao acesso local e à função renal. Alinhar a incorporação à diretriz mais recente — e condicioná-la a protocolo que diga, em cada faixa, o que a AngioTC substitui — é o instrumento que a evidência sustenta. |

---

## 1. Objeto da contribuição

O Relatório de Recomendação Preliminar registra que a deliberação desfavorável de 3 de julho de 2026 (153ª Reunião Ordinária) foi fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à **capacidade de implementação da tecnologia no SUS** e à delimitação da população elegível. O Comitê destacou como essenciais ao esclarecimento em consulta pública, entre outros pontos, "a estimativa da capacidade instalada", "a necessidade ou não de aquisição de equipamentos" e "o impacto real sobre a realização de angiografias invasivas e testes funcionais". O Relatório para a Sociedade nº 745 descreve a indicação proposta pelo demandante como "diagnóstico e predição de desfechos clínicos da doença arterial coronariana estável através de uma avaliação não invasiva" e registra, entre os fundamentos da recomendação preliminar, "a necessidade de melhor delimitação dos critérios de uso e da população elegível" [30] — o dossiê em si não é público, e esta contribuição trabalha com os dois relatórios.

Esta contribuição responde a esses pontos com análise nacional construída sobre bases públicas — CNES, SIA/SUS, SIH/SUS, SIGTAP e IBGE. O relatório preliminar utiliza DATASUS/TABNET e SIGTAP para demanda e preços; **não utiliza o CNES para caracterizar a capacidade instalada**.

Método, endereços de origem e código no Apêndice A. As seções 2 e 3 são reproduzíveis a partir dos microdados por `analise_final.py`; a seção 4 depende adicionalmente de valores extraídos de publicações listadas no Apêndice B e nas Referências.

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

As camadas se sobrepõem por estabelecimento: 77 estabelecimentos possuem equipamentos em ≥64 e em <64 canais simultaneamente, e 49 possuem equipamentos reclassificados e sob o código genérico. A coluna de estabelecimentos soma 3.521 = 3.395 + 77 + 49; a de equipamentos soma exatamente.

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

O estrato de 79 estabelecimentos reúne hardware declarado como compatível (autodeclaração no CNES), infraestrutura cardiovascular instalada e atividade coronariana documentada. É o conjunto com maior plausibilidade de implantação **sem aquisição de tomógrafo**. Software de análise cardíaca, sincronização eletrocardiográfica, bomba injetora e profissionais habilitados em laudo cardiovascular **não constam do CNES** e não são verificáveis por esta análise.

A co-localização com hemodinâmica **não é requisito técnico** para angiotomografia — um serviço de radiologia com tomógrafo de 128 canais e cardiologista habilitado realiza o exame sem sala de hemodinâmica, e um hospital com hemodinâmica e tomógrafo de 16 canais não está tecnicamente apto. O cruzamento é adotado como marcador de maturidade cardiovascular institucional, não como limite inferior de capacidade.

O CNES tampouco informa horas de operação ou agenda. A carga atual do parque tomográfico do SUS (SIA 2025, grupo `0206` exceto PET-CT) é de aproximadamente 13,4 milhões de exames — cerca de 3.400 por equipamento sobre o parque total de 3.953; a capacidade em *vagas* para exames adicionais não foi estimada nesta contribuição.

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

**Regra de análise, fixada antes da extração:** quando a OCI é registrada como procedimento principal, os componentes aparecem no SIA com valor zerado e **não são somados novamente** — o custo do episódio é o valor da OCI. O dado é compatível com o mecanismo (limite inferior): ao menos 3.266 procedimentos funcionais em chaves estabelecimento-mês com `PA_VALAPR = 0` em 2025 (1.997 ergometrias, 522 + 559 cintilografias, 188 ecos de estresse) — limite inferior, pois a agregação é por chave e não por registro. Procedimentos com valor positivo seguem no *legacy pathway*.

**Produção em 2025, 27 UFs:**

| Pathway | Episódios | Gasto | R$ por episódio |
|---|---|---|---|
| Legacy — procedimentos isolados com valor > 0 | 785.247 | R$ 146,1 mi | 186,10 |
| **OCI de SCC** (0034 · 0042 · 0050) | **7.616** | R$ 2,51 mi | 329,75 |
| **Ponderado nacional** | **792.863** | R$ 148,6 mi | **187,48** |

As OCI de SCC respondem por **0,96% dos episódios** — 6.505 avaliações iniciais, 302 progressões I e 809 progressões II, em 148 estabelecimentos de 13 UFs. A OCI `0902010026 — Avaliação Cardiológica` (R$ 200,00), com 77.241 episódios em 2025, não foi examinada quanto à sua composição; se incluir exames funcionais, a fração organizada é maior que 0,96%.

A tabela da seção 3.1 (787.954 episódios) inclui os componentes zerados na contagem; o legacy pathway (785.247) os exclui. A diferença de 2.707 corresponde exatamente aos 1.997 + 522 + 188 componentes zerados na convenção de contagem por estresse.

**Sensibilidade do intercepto às OCI.** O modelo da seção 4 usa R$ 185,46 (seção 3.1). Substituindo pelo ponderado nacional com OCI, o preço de neutralidade do cenário mix médio (o único que usa esse intercepto) sobe R$ 2,02; a reta de gatekeeping não se altera. Nenhuma conclusão muda. Esta sensibilidade é pequena; a que importa está na seção 4.4.

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

com `C_CATE = R$ 730,14` (SIA 2025) e `Δ_CATE` como parâmetro declarado. O desenho de cada ensaio determina qual equação se aplica. **O SCOT-HEART, cujo desenho é aditivo — angiotomografia somada ao cuidado padrão contra cuidado padrão —, não substitui episódio funcional e recai na segunda equação**, embora sua população seja de primeira linha; seus preços de neutralidade (R$ −2,82 no seguimento mediano de 20 meses, 409 contra 401 cateterismos; R$ +3,87 aos 5 anos, 491 contra 502) refletem apenas o custo dos cateterismos induzidos ou evitados.

Esse desenho não é uma curiosidade de ensaio: **é o cenário de referência para uma incorporação que crie o código SIGTAP sem protocolo vinculante de posicionamento** — e, a juízo dos autores, o mais provável nessas condições. Com 787.954 episódios funcionais por ano em curso e nada que os retire do percurso, a angiotomografia tende a entrar *somada* ao teste ergométrico, não no lugar dele; nos próprios ensaios de substituição, 3% a 13% dos pacientes fizeram testes funcionais subsequentes mesmo com a angiotomografia como estratégia inicial (PRECISE, CRESCENT-II), e o único ensaio de desenho aditivo é o que reproduz esse cenário. Isto é um juízo sobre implementação, não uma medida — o SIA não registra sobreposição de testes por paciente. Nesse caso `C_substituído = 0` e a primeira equação colapsa na segunda — com o Δ dos ensaios de primeira linha, não o dos ensaios invasivo-primeiro. Esta contribuição o nomeia como sexto cenário, **"adoção aditiva (sem protocolo)"**, e o trata como o cenário de referência para uma incorporação que não especifique o que a tecnologia substitui.

`C_substituído` é o parâmetro dominante e desconhecido para a população elegível (seção 3.2). A análise é apresentada para seis valores:

| Cenário | C_substituído | Origem |
|---|---|---|
| **Adoção aditiva (sem protocolo)** | **R$ 0,00** | angiotomografia somada ao percurso atual; nada substituído; desenho do SCOT-HEART |
| Mix médio do SIA | R$ 185,46 | seção 3.1 — 76% ergometria; equivale ao PICO como submetido, sem estratificar |
| Mix do NATS, como publicado | R$ 316,76 | relatório preliminar: TE + 50% cintilografia + 50% eco de estresse, **com a cintilografia precificada só pelo código de estresse (R$ 408,52)** |
| Mix do NATS, por episódio | R$ 523,81 | mesmo percurso, com a cintilografia como episódio (dois códigos) e valores médios observados no SIA |
| Ecocardiografia de estresse | R$ 196,39 | valor médio aprovado por episódio |
| Cintilografia de perfusão | R$ 786,83 | valor médio aprovado por episódio |

Os valores "médios aprovados por episódio" são os do SIA 2025 e superam o valor SIGTAP (ecocardiografia R$ 165,00; ergometria R$ 30,00) em 19% e 7%, por complementações e incentivos locais registrados no valor aprovado — continuam sendo preços pagos, não custos. O parâmetro do NATS é reproduzido como publicado e também recalculado sob a convenção desta contribuição — o relatório preliminar precifica a cintilografia por um único código, o que contradiz o pareamento estresse–repouso que este documento adota na seção 3.1. A diferença (R$ 316,76 contra R$ 523,81) é material para o resultado.

**Qual desses cenários corresponde à população elegível não é identificável nos registros administrativos.** A Diretriz SBC de Síndrome Coronariana Crônica 2025 (Arq Bras Cardiol 2025;122(9), DOI 10.36660/abc.20250619) posiciona a angiotomografia, na probabilidade pré-teste intermediária, como exame inicial de classe I-A **ou** alternativa à prova funcional (Figura 16: "prova funcional ou angiotomografia"); na baixa, como primeira opção de classe IIb-B, com o algoritmo indicando "ajustar PPT ou angiotomografia". O exame que a angiotomografia substituiria, por recomendação, é portanto a prova funcional que o serviço realizaria naquela faixa — e a diretriz diz de que depende, não qual: no resumo de como investigar (seção 3.1.7), "a escolha do exame inicial deve levar em conta: capacidade funcional: se preservada, iniciar com TE ou ecocardiograma de estresse; ECG basal interpretável: se não for interpretável, preferir métodos de imagem (ecocardiograma, cintilografia, RMC); acesso local e disponibilidade: considerar custo, tempo de realização e familiaridade da equipe; DRC ou alergia a contraste: pode haver restrição para realização de angioTC". O "ou" do algoritmo é escolha condicionada ao serviço e ao paciente, não preferência — e a própria diretriz sugere começar pelo teste ergométrico quando a capacidade funcional é preservada, o que é o percurso que o SIA mostra (76% do volume).

As diretrizes internacionais convergem com essa estratificação. A ESC 2024 recomenda a angiotomografia como modalidade **preferida** apenas na probabilidade baixa-a-moderada (>5–50%; I-B para excluir DAC, I-A para diagnóstico e risco) e a imagem funcional na moderada-a-alta (>15–85%; I-B), pelo maior poder de confirmação; abaixo de 5% recomenda diferir, e entre 5 e 15% considerar escore de cálcio antes de qualquer exame (IIa-B). A AHA/ACC 2021 dá angiotomografia (1-A) e imagem de estresse (1-B-R) como opções co-iguais no risco intermediário-alto, com preferência etária (<65 anos angiotomografia, ≥65 estresse), e recomenda diferir ou usar escore de cálcio no risco baixo. Nenhuma diretriz AHA/ACC posterior a 2021 sobre dor torácica ou doença coronariana crônica existe; a de 2023 remete à de 2021. Apenas o NICE CG95 (2016) oferece angiotomografia sem estratificar por probabilidade — a toda angina típica ou atípica, com equipamento de ≥64 cortes —, colocando a imagem funcional em segunda linha e o cateterismo em terceira. **Em síntese: na probabilidade baixa, as diretrizes recomendam majoritariamente reavaliar, diferir ou usar escore de cálcio — o exame que a angiotomografia substituiria ali tende a ser nenhum, o cenário economicamente menos favorável. Na intermediária, ela é opção classe I ao lado da imagem funcional.**

### 4.3 Δ necessário por preço e por exame substituído

O relatório preliminar adota **R$ 550,00** como preço da angiotomografia proposto pelo demandante. Os demais preços de referência são o proxy de tabela para TC de tórax com contraste, o microcusteio de 2022 corrigido monetariamente, e o valor da angiotomografia na saúde suplementar usado por Shiozaki et al. (Arq Bras Cardiol 2025;122(12):e20250204) — R$ 1.311,95, "conforme referência da ANS", apresentado como 100% da CBHPM.

| Preço da AngioTC | Natureza | **adoção aditiva** | mix SIA | NATS publicado | NATS por episódio | eco de estresse | cintilografia |
|---|---|---|---|---|---|---|---|
| R$ 196,41 | TC tórax + contraste, proxy SIGTAP | 26,9 | 1,5 | já neutro | já neutro | 0,0 | já neutro |
| **R$ 550,00** | **proposto pelo demandante** | **75,3** | **49,9** | **31,9** | **3,6** | 48,4 | **já neutro** |
| R$ 622,54 | microcusteio 2022 (Carmo et al.) corrigido a jul/2026 (IPCA 12/2020→07/2026, ×1,3771; ano-base não explicitado no artigo, 12/2020 é o limite otimista) | 85,3 | 59,9 | 41,9 | 13,5 | 58,4 | já neutro |
| R$ 1.311,95 | saúde suplementar (Shiozaki et al. 2025: referência ANS, 100% CBHPM) | 179,7 | 154,3 | 136,3 | 107,9 | 152,8 | 71,9 |

Valores: Δ de cateterismo total por 100 pacientes necessário para neutralidade, **considerando apenas o custo dos exames e do cateterismo**.

Ao preço da saúde suplementar e substituindo o mix médio, seriam necessárias mais angiografias evitadas do que pacientes investigados — **inalcançável neste modelo**, em que o único crédito a jusante é o cateterismo evitado ao valor de tabela. Créditos por outros recursos evitados ou um `C_CATE` microcusteado superior alterariam esse limite.

Na adoção aditiva, o Δ exigido a R$ 550 é 75,3 por 100 — **numericamente o mesmo limiar do gatekeeping (seção 4.5), porque a equação é a mesma**. A diferença é de onde vem o Δ: em pacientes já indicados a cateterismo, 75 por 100 é o que o DISCHARGE observou; em pacientes de primeira linha, o melhor Δ já observado é 4,1.

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

| Exame substituído | C | Neutralidade, só exames + cateterismo (Δ −6,3 a +4,1) | vs R$ 550 |
|---|---|---|---|
| **Adoção aditiva (sem protocolo)** | **R$ 0,00** | **R$ −46 – +30** (com o Δ do próprio SCOT-HEART: R$ −3 – +4) | **teto de R$ 30** |
| Mix médio do SIA | R$ 185,46 | **R$ 139 – 215** | abaixo |
| Mix do NATS, como publicado | R$ 316,76 | **R$ 270 – 347** | abaixo |
| Mix do NATS, por episódio | R$ 523,81 | **R$ 477 – 554** | **dentro** |
| Ecocardiografia de estresse | R$ 196,39 | **R$ 150 – 226** | abaixo |
| Cintilografia de perfusão | R$ 786,83 | **R$ 741 – 817** | acima |

**O resultado é sensível ao exame substituído em uma ordem de grandeza** — de R$ 139 a R$ 817 para o mesmo Δ observado. Se a angiotomografia substitui o mix médio do SUS, majoritariamente teste ergométrico, o preço de neutralidade fica 2,6 a 4 vezes abaixo do proposto e o Δ necessário (49,9 a R$ 550) é doze vezes o melhor observado. Se substitui exclusivamente a cintilografia de perfusão, o custo do comparador financia a substituição neste modelo restrito. Se substitui o percurso do NATS precificado por episódio, **o preço proposto cai dentro da faixa de neutralidade** e o Δ necessário (3,6 por 100) é 0,9 vez o melhor observado.

**Se não substitui nada — adoção aditiva —, nenhum preço plausível é neutro.** O preço de neutralidade vai de R$ −46 a R$ +30 (com o Δ do único ensaio aditivo, o SCOT-HEART, R$ −3 a +4): mesmo gratuita, a angiotomografia adicionada ao percurso só é neutra se não induzir cateterismos, e o melhor Δ de primeira linha (+4,1) paga R$ 30 por exame — abaixo do menor preço de referência (R$ 196). Isso não enfraquece a análise; é a sua forma mais forte: **sem especificação de posicionamento, a tecnologia é orçamentariamente expansiva por construção**, independentemente do preço negociado. Os outros cinco cenários descrevem quanto se recupera quando um protocolo diz o que sai do percurso.

Nos ensaios que compararam estratégias não invasivas iniciais, a magnitude da redução observada na angiografia invasiva foi ausente, variável ou insuficiente para sustentar, isoladamente, neutralidade orçamentária aos custos estimados para o SUS — quando o exame substituído é o mix médio observado, a ecocardiografia de estresse, ou o mix do NATS como publicado. Quando o exame substituído é a cintilografia de perfusão — e apenas ela; a ecocardiografia de estresse, também imagem funcional, custa R$ 196 —, o modelo restrito a exames e cateterismo indica neutralidade. A seção 4.6 mostra que essa conclusão não sobrevive à inclusão da revascularização.

**A pergunta decisiva, portanto, não é o Δ de cateterismos. É qual exame a angiotomografia substituiria na população elegível — e essa pergunta é parte da que o Comitê formulou como "definição precisa da população elegível".** Ela não é respondível a partir do SIA. É respondível por protocolo: a Diretriz SBC de SCC 2025 já estratifica a indicação por probabilidade pré-teste, e a incorporação pode espelhar essa estratificação em vez de tratar "baixa ou intermediária" como uma faixa única.

**Ressalvas.** Os horizontes diferem (90 dias a 18 meses) e os pontos não constituem metanálise. PROMISE contabiliza 90 dias; o efeito é dependente do horizonte, como o SCOT-HEART demonstra (mais cateterismos nos primeiros meses — 94 contra 8 novos pedidos em 6 semanas —, 409 contra 401 no seguimento mediano de 20 meses e HR 1,00 aos 5 anos). O braço de intervenção do PRECISE inclui diferimento de teste em 20% dos pacientes de menor risco — não é substituição 1:1. A metanálise de Foy inclui 9 de 13 ensaios em população de emergência; utilizou-se o subgrupo estável. As contagens do CAPP não constam do artigo primário; provêm do gráfico de floresta de Foy (2017). Em CRESCENT-I e II as diferenças de cateterismo total não são estatisticamente significativas (p = 0,843 e 0,860). O PROMISE ilustra a dissociação entre volume e adequação — aumentou o cateterismo total de 8,1% para 12,2% e reduziu o cateterismo sem doença obstrutiva de 4,3% para 3,4%; o PRECISE reduziu o cateterismo total de 16,9% para 12,8% com aumento de revascularização de 5,2% para 9,2%, custo diagnóstico −27% e custo de revascularização +67% (Circ Cardiovasc Qual Outcomes, PMID 39895495). **Reduzir cateterismo não implica reduzir gasto.**

Os CRESCENT aplicaram filtro por escore de cálcio antes da angiotomografia; o CAPP realizou angiotomografia em todos. A heterogeneidade entre estratégias sugere que o impacto orçamentário depende também dos critérios de seleção e do protocolo — mas comparações indiretas entre ensaios não permitem quantificar isoladamente esse efeito.

### 4.5 O espaço econômico é maior em outro PICO

Ensaios com comparador **invasivo-primeiro** — pacientes com cinecoronariografia eletiva já indicada — recaem na equação de gatekeeping (filtro pré-cateterismo). Todos os Δ abaixo são de **cateterismo total por braço randomizado**, extraídos das publicações primárias.

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

Registra-se que o próprio dossiê e a reanálise do NATS utilizaram o DISCHARGE — ensaio de população invasivo-primeiro — como fonte de parâmetros para o PICO de primeira linha. A transposição de parâmetros entre PICOs aqui descrita já está, portanto, no relatório preliminar.

A mesma transposição está na única avaliação econômica brasileira publicada da angiotomografia na saúde suplementar (Shiozaki et al., Arq Bras Cardiol 2025;122(12):e20250204, epub jan/2026) — o estudo mais recente e o mais presente no debate público sobre o pedido —, que estima economia de R$ 1.021 por beneficiário em cinco anos numa carteira de 100.000 vidas. Ele responde a outra pergunta, e o confronto é instrutivo por isso. O artigo compara a angiotomografia, a R$ 1.311,95, com **a angiografia invasiva como estratégia inicial, a R$ 1.900,79 — único comparador** —, em população de probabilidade intermediária, com eventos do DISCHARGE, e declara nas limitações não ter comparado com testes funcionais. É, portanto, um modelo do PICO de filtro pré-cateterismo, no qual o Δ exigido naquele sistema é de 69 por 100 (1.311,95 ÷ 1.900,79) e o DISCHARGE (75,1) o alcança — o mesmo mecanismo da tabela acima —, não do PICO de primeira linha em apreciação. A economia é por beneficiário de uma carteira de 100.000 vidas, não por paciente examinado. Projeções de impacto de dezenas de bilhões de reais veiculadas em material de imprensa em agosto de 2026 não constam do artigo, e o próprio material as qualifica como projeção teórica para a saúde suplementar, "sem representar diretamente uma estimativa de impacto" para o SUS [29].

**Recomenda-se que a apreciação final considere avaliar a indicação de filtro anterior a cateterismo já indicado como pergunta separada, com critérios de elegibilidade próprios.**

### 4.6 A revascularização não pode ficar fora de uma análise de neutralidade

As seções 4.3 a 4.5 creditam e debitam apenas exames e cateterismo. Mas os ensaios reportam também revascularização, e o SIH 2025 fornece o custo unitário observado: **R$ 7.713 por angioplastia coronariana e R$ 25.904 por revascularização cirúrgica** (seção 3.4). Incluindo esse componente:

| Cenário | Δ revascularização /100 | Ajuste por paciente | Neutralidade sem revasc. | **Neutralidade com revasc.** |
|---|---|---|---|---|
| Cintilografia + PRECISE (Δ CATE +4,1; revasc. 5,2% → 9,2%, ~3,75 PCI + 0,27 CRM) | +4,0 | −R$ 359 | R$ 817 | **R$ 458** |
| Cintilografia + Foy 2017, 13 ensaios, 9 de emergência (Δ CATE −2,6; revasc. 4,5% → 7,2%, RR agrupado 1,86, IC95% 1,43–2,43) | +2,7 | −R$ 208 | R$ 768 | **R$ 560** |
| Adoção aditiva + SCOT-HEART (Δ CATE −0,4 em 20 m / +0,5 em 5 a; revasc. 233 vs 201 / 279 vs 267) | +1,5 / +0,6 | −R$ 119 / −R$ 45 | R$ −3 / +4 | **R$ −122 / −41** |
| Gatekeeping, DISCHARGE (Δ CATE 75,1; revasc. 18,0% → 14,2%) | −3,8 | +R$ 293 | R$ 548 | **R$ 841** |
| Gatekeeping, CONSERVE (Δ CATE 66,0; revasc. 18% → 13%) | −5,0 | +R$ 386 | R$ 482 | **R$ 868** |

**Com a revascularização, o cenário mais favorável de primeira linha deixa de superar o preço proposto e passa a cercá-lo** — R$ 458 a R$ 560 contra R$ 550: no par PRECISE, o único ensaio contemporâneo com Δ de cateterismo favorável, R$ 550 excede a neutralidade em R$ 92 por paciente; só o par Foy, misto e majoritariamente de emergência, o cobre. E o gatekeeping, que sem revascularização ficava abaixo, passa a superá-lo com folga no DISCHARGE (R$ 841) e no CONSERVE (R$ 868). A omissão da revascularização favorecia a primeira linha e penalizava o gatekeeping simultaneamente. Assimetria declarada: os débitos de primeira linha incluem a parcela cirúrgica (PRECISE, 0,27 CRM), enquanto os créditos do DISCHARGE e do CONSERVE são valorados só como angioplastia, por falta de desagregação — conservador contra o gatekeeping. O par de Foy usa o Δ de cateterismo e a revascularização dos mesmos 13 ensaios.

A única análise econômica de ensaio no cenário de substituição de imagem funcional — o PROMISE, cujo comparador foi majoritariamente cintilografia — **não encontrou economia**: US$ 2.494 contra US$ 2.240 aos 90 dias, "associada a mais revascularizações e cateterismos", e sem diferença aos 3 anos (Mark DB et al., Ann Intern Med 2016; PMID 26857050). O SCOT-HEART, na análise de custos aos 6 meses, encontrou +US$ 462 por paciente (US$ 1.900 contra 1.438), com custos a jusante sem diferença.

Componentes ainda não quantificados: a menor frequência de complicações maiores relacionadas ao procedimento no DISCHARGE (0,5% contra 1,9%) e a redução da permanência no CAD-MAN (mediana de 52,9 para 30,0 horas), que tenderiam a favorecer o gatekeeping; angiotomografias não diagnósticas, testes funcionais subsequentes (13% no CRESCENT-II; 3,4% contra 9,9% no PRECISE, favorável à angiotomografia), achados incidentais e uso de contraste e betabloqueador. A premissa de substituição 1:1 é declarada como tal. **O impacto líquido de todos os componentes não foi estimado.**

### 4.7 Por estrato de probabilidade pré-teste — o comparador realista como premissa declarada

O SIA não distingue a probabilidade pré-teste dos pacientes investigados. O modelo, porém, distingue por premissa: as diretrizes (seção 4.2) dizem qual exame a angiotomografia substituiria em cada faixa, e essa premissa pode ser declarada em vez de escondida numa média. Na **probabilidade baixa**, o comparador realista é o teste ergométrico — ou nenhum exame, quando a diretriz recomenda diferir, ajustar a probabilidade ou usar escore de cálcio (SBC 2025, ESC 2024, AHA/ACC 2021); "nenhum exame" é a adoção aditiva. Na **intermediária**, é a imagem funcional que o serviço realizaria: ecocardiografia de estresse ou cintilografia de perfusão (ou o percurso do NATS, que as mistura). O mix médio do SIA corresponde ao PICO como submetido — "baixa ou intermediária" sem estratificar. Aplicando os mesmos Δ da seção 4.4 e o mesmo débito de revascularização da seção 4.6 (PRECISE e Foy 2017) a **todos** os cenários de primeira linha:

| Estrato | Comparador (premissa) | C_substituído | Neutralidade, só exames | **Neutralidade com revascularização** | Δ exigido a R$ 550 (só exames) |
|---|---|---|---|---|---|
| Qualquer estrato, sem protocolo | adoção aditiva (nada substituído) | R$ 0 | R$ −46 – +30 (SCOT-HEART: −3 – +4) | R$ −122 – −41 (revasc. do próprio SCOT-HEART) | 75,3 |
| Baixa | diferir / ajustar PPT (contrafactual sem teste) | R$ 0 | teto R$ 0 (Δ ≤ 0 por construção) | — | — |
| Baixa | teste ergométrico | R$ 32,20 | R$ −14 – +62 | R$ −297 – −195 | 70,9 |
| Não estratificado (PICO submetido) | mix médio do SIA | R$ 185,46 | R$ 139 – 215 | R$ −144 – −42 | 49,9 |
| Intermediária | ecocardiografia de estresse | R$ 196,39 | R$ 150 – 226 | R$ −133 – −31 | 48,4 |
| Intermediária | percurso do NATS por episódio | R$ 523,81 | R$ 477 – 554 | R$ 195 – 297 | 3,6 |
| Intermediária, com protocolo (cenário-base do estrato) | cintilografia de perfusão | R$ 786,83 | R$ 741 – 817 | **R$ 458 – 560** | já neutro |
| Intermediária, descritivo sem protocolo (sensibilidade) | teste ergométrico seguido de imagem em fração p dos pacientes; teto p ≤ 0,31 pelos volumes do SIA (toda cintilografia e eco a jusante de um TE), imagem a R$ 679 em média | ≤ R$ 242,75 | ≤ R$ 196 – 273 | ≤ R$ −87 – +16 | ≥ 42,1 |
| Já indicado a cateterismo (outro PICO) | cateterismo direto | cancela | R$ 482 – 625 | **R$ 841** (DISCHARGE) / **R$ 868** (CONSERVE) | 75,3 |

`analise_final.py`, seção 4.9; `output/out-limiar-por-estrato.csv`. Débito de revascularização: PRECISE (+4,0/100) e Foy 2017, 13 ensaios (+2,7/100, pareado com o Δ de cateterismo dos mesmos 13, −2,6), aplicados como envelope aos cenários de substituição; para a adoção aditiva usa-se a revascularização do próprio SCOT-HEART (+1,5/100 em 20 meses; +0,6/100 em 5 anos). O débito absoluto escala com a prevalência de doença: na probabilidade baixa, o envelope PRECISE/Foy (população intermediária) tende a superestimá-lo — o que não altera o sinal, negativo de qualquer modo. Para o diferimento propriamente dito, o contrafactual não contém cateterismo diagnóstico, logo Δ ≤ 0 e o teto é R$ 0, não R$ 30. O cenário descritivo da intermediária sem protocolo é um teto: p = (151.784 cintilografias + 33.766 ecos) ÷ 598.695 ergometrias = 0,31 supõe que todo exame de imagem funcional do SUS seja a jusante de um teste ergométrico — sem inferência ecológica sobre pacientes individuais, apenas um limite superior de volumes.

Três leituras. **Primeira: na probabilidade baixa, nenhum preço plausível fecha** — com o comparador que as diretrizes indicam (nenhum exame ou ergometria), o teto de neutralidade é R$ 30 a R$ 62 só com exames e negativo com revascularização, abaixo de qualquer preço de referência (R$ 196 a R$ 1.312). **Segunda: na intermediária, o resultado depende de qual imagem funcional sai do percurso.** Substituindo a ecocardiografia de estresse, R$ 550 está fora do alcance; substituindo a cintilografia, R$ 550 está dentro da zona de incerteza mesmo com a revascularização observada (R$ 458–560) — um nicho de no máximo 151.784 episódios por ano, 19% do volume, e a fração substituível é menor: parte da cintilografia do SUS é feita em pacientes com DAC conhecida ou revascularizada, fora do PICO, e parte em pacientes idosos, obesos, com fibrilação atrial ou calcificação coronariana extensa, nos quais a angiotomografia tem menor acurácia e mais exames não diagnósticos — justamente os que as diretrizes encaminham à imagem funcional; o percurso misto do NATS, que sem revascularização cercava R$ 550, cai a R$ 195–297 quando ela entra. A premissa é normativa, não observada: o SIA mostra 76% de ergometria em todo o volume, e a ESC 2024 admite ergometria (IIb-B) quando a imagem não está disponível — se, na prática do SUS, o comparador da probabilidade intermediária for a ergometria, o resultado colapsa no da baixa. O resultado intermediário exige, portanto, protocolo que nomeie o exame deslocado (cintilografia), não só a faixa de probabilidade. Sem protocolo, o cenário descritivo da rede — teste ergométrico seguido de imagem numa fração dos pacientes — fica entre o mix médio e a ecocardiografia (≤ R$ 196–273 só com exames; negativo com revascularização). **Terceira: o PICO como submetido — a média não estratificada — é puxado para o estrato baixo**, porque três quartos do volume atual são ergometria (mix R$ 139–215, próximo da ecocardiografia, R$ 150–226, e longe da cintilografia). Estratificar não é análise de sensibilidade; é o resultado: no SUS como é, "primeira linha" significa substituir o teste ergométrico — e isso não fecha a nenhum preço plausível; a angiotomografia paga quando entra *depois* do teste ergométrico, no lugar do encaminhamento à cintilografia (intermediária com protocolo, zona de incerteza) ou no lugar da cinecoronariografia eletiva já indicada (filtro, R$ 482–868). Capacidade e posicionamento apontam para o mesmo lugar: o estrato pronto de 79 são hospitais com hemodinâmica, onde o paciente já referenciado ao cateterismo está. Essa estratificação já está escrita na Diretriz SBC de SCC 2025 (IIb-B na baixa; I-A na intermediária; alternativa ao estudo invasivo após teste conflitante), posterior à formulação que o PICO reproduz.

### 4.8 Um segundo desfecho, apresentado como eficiência diagnóstica

> Esta seção apresenta **cateterismo sem DAC obstrutiva** como métrica de eficiência diagnóstica, **não utilizada como unidade do cálculo econômico**. Seus valores não entram nas seções 4.3 a 4.7, que usam cateterismo total.

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
| CONSERVE | cateterismo direto | 24/784 (3,1%)ᵃ | 439/719 (61,1%)ᵃ | 58,0ᵃ |

ᵃ Para o CONSERVE, os valores são os da Tabela 43 do IQWiG (cálculo próprio da agência, denominadores de pacientes avaliados por estratégia, 784/719, não os randomizados, 823/808). O abstract do ensaio reporta 24,6% e 61,1% como taxas de cateterismo normal **entre os cateterismos realizados**, não por paciente; os dois números não são diretamente comparáveis, e a linha é mantida com essa ressalva. Não entra em nenhum cálculo. Adicionalmente: PRECISE 2,6% vs 10,2% (evitados 7,6/100); CRESCENT-II, cateterismo sem indicação classe I, 1,5% vs 7,2% (5,7/100).

Metanálise do IQWiG para os estudos de alta certeza contra métodos funcionais (CATCH e PROMISE): OR 0,77 (IC95% 0,64–0,94; p = 0,011). Contra cateterismo direto, OR de 0,01 a 0,03, sem estimativa agrupada por heterogeneidade.

**No horizonte econômico analisado nesta contribuição, o benefício mais consistente diretamente relacionado à utilização de recursos é o aumento da adequação da indicação de angiografia invasiva.** A direção é favorável à angiotomografia em todos os ensaios aqui listados, nos dois PICOs — com a ressalva de fonte para o CONSERVE.

Esta é uma afirmação sobre utilização de recursos no curto prazo, **não uma caracterização do benefício clínico da tecnologia**. O SCOT-HEART demonstrou redução de morte coronariana e infarto não fatal em 5 anos com a angiotomografia associada ao cuidado padrão, resultado mantido na análise de 10 anos. Benefício clínico em desfechos duros e neutralidade orçamentária de curto prazo são perguntas distintas; esta contribuição responde apenas à segunda.

### 4.9 Limitação metodológica desta seção

Limitações de escopo e de dado que um leitor clínico notará: o código `0211020010` é genérico e não distingue cinecoronariografia de outros cateterismos diagnósticos; os denominadores do SIA incluem assintomáticos (teste ergométrico pré-operatório, esportivo, de seguimento) e DAC conhecida (cintilografia de seguimento), fora do PICO; contraindicações relativas à angiotomografia (doença renal crônica avançada, alergia a contraste, frequência cardíaca não controlável, calcificação extensa) reduzem a população elegível e não foram descontadas; dos 432 equipamentos ≥64 canais, 293 são de 64 canais e o CNES não registra geração nem ano — com aquisição retrospectiva a dose é várias vezes a de um equipamento atual, e este é mais um motivo pelo qual "≥64 canais" é piso, não estimativa; leitores habilitados, técnicos treinados em aquisição sincronizada e enfermagem para controle de frequência não constam do cadastro, e o gargalo previsível de implantação é a equipe, não o tomógrafo. A dor torácica aguda não é objeto desta contribuição nem do PICO.

Os Δ utilizados são diferenças aritméticas entre percentuais publicados por braço, não estimativas agrupadas de diferença absoluta. A metanálise em rede de Siontis (BMJ 2018) reporta NNT 24 (16 a 92) para teste funcional contra angiotomografia sobre taxa-base de 12,2% — equivalente a diferença absoluta de cerca de 4 por 100, coerente com a faixa aqui utilizada; a diferença de risco agrupada de Hulten (JACC 2013, +21 por 1.000) refere-se a população de emergência.

Advertências sobre fontes secundárias: a revisão de Zito (Ann Intern Med 2023) teve errata publicada (2024;177:991-2), e os intervalos indexados no PubMed permanecem desatualizados; a revisão de Hwang (Clin Cardiol 2017) contém erro de extração para SCOT-HEART — os valores 94 e 8 são exames recém-solicitados, não totais por braço (491 e 502) — e **não foi utilizada**.

---

## 5. Síntese

1. **O CNES permite, desde a Portaria SAES/MS nº 3.695/2026, identificar tomógrafos por faixa de canais.** Em 06/2026 há **432 equipamentos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS.
2. **A reclassificação está 25–27% concluída.** Os 432 são piso documentado; 2.785 equipamentos permanecem sem especificação. Recomenda-se que a apreciação final utilize a competência mais recente e registre a proporção reclassificada.
3. **79 estabelecimentos** reúnem hardware ≥64 canais, hemodinâmica co-localizada e produção coronariana documentada. **Doze UFs não possuem nenhum**; AP, PI e TO não possuem tomógrafo de ≥64 canais confirmado.
4. A investigação funcional do SUS concentra-se em **volume no teste ergométrico (76%) e em gasto na cintilografia (82%)**. Qual exame a angiotomografia substituiria na população elegível **não é identificável nos registros administrativos** — e é o parâmetro dominante do modelo.
5. **A sustentabilidade orçamentária da primeira linha depende de três parâmetros não identificáveis nos registros: o exame substituído, a revascularização induzida e a posição no percurso.** Só com exames e cateterismo, a neutralidade vai de R$ 139–215 (mix médio do SIA) a R$ 741–817 (cintilografia). Incluindo a revascularização observada nos ensaios, o cenário cintilografia cai para R$ 458–560 e os demais cenários de primeira linha ficam abaixo de R$ 300. O preço proposto (R$ 550) está fora do alcance nos cenários de mix médio, ergometria e ecocardiografia, e **dentro da zona de incerteza** apenas quando a AngioTC substitui cintilografia.
6. **Sem protocolo de posicionamento, nenhum preço plausível é neutro.** Se a incorporação criar o código sem protocolo vinculante que diga o que sai do percurso, o cenário de referência — e, a juízo dos autores, o mais provável — é o aditivo: a AngioTC somada ao teste ergométrico em curso, não no lugar dele. Com nada substituído, o preço de neutralidade é de R$ −46 a +30 (com o Δ do próprio SCOT-HEART, R$ −3 a +4; com a sua revascularização, R$ −122 a −41): a tecnologia é orçamentariamente expansiva por construção, independentemente do preço negociado. A condição de sustentabilidade não é o preço; é a especificação do que sai do percurso.
7. **O espaço econômico é maior em outro PICO.** Em pacientes já indicados a cateterismo, o preço de neutralidade é de R$ 482–625 só com exames, independentemente do exame prévio, e sobe a R$ 841 (DISCHARGE) e R$ 868 (CONSERVE) quando a menor revascularização observada é creditada. Nesse PICO o custo da investigação prévia é comum aos braços e não pode ser creditado. População distinta, **não intercambiável** com a apreciada. O relatório preliminar já utiliza um ensaio dessa população (DISCHARGE) para o PICO de primeira linha.
8. **Estratificar por probabilidade pré-teste não é sensibilidade; é o resultado.** Com o comparador que as diretrizes indicam em cada faixa (seção 4.7), a mesma tecnologia ao mesmo preço é expansiva na baixa — onde o exame substituído é nenhum ou a ergometria — e fica na zona de incerteza na intermediária quando substitui cintilografia (e só cintilografia: se o comparador real for a ergometria, o resultado colapsa no da baixa). A média não estratificada é puxada para o estrato baixo, porque três quartos do volume atual são ergometria. A Diretriz SBC de SCC 2025 já faz essa estratificação (I-A na intermediária, IIb-B na baixa; algoritmo com a angiotomografia como alternativa à prova funcional, não substituta). O PICO submetido reproduz a formulação da Diretriz SBC/CBR de TC/RM 2024, que trata "baixa ou intermediária" como faixa única, e a indicação proposta pelo demandante ("diagnóstico e predição de desfechos clínicos da DAC estável através de uma avaliação não invasiva") não traz protocolo; a Diretriz de SCC 2025, posterior e específica, estratifica e condiciona a escolha ao serviço e ao paciente. Alinhar a incorporação à diretriz mais recente é o instrumento que a evidência sustenta.
9. **No horizonte econômico analisado, o benefício mais consistente é o aumento da adequação da indicação de cateterismo**, não a redução de volume. Isto não caracteriza o benefício clínico: o SCOT-HEART demonstrou redução de morte coronariana e infarto em 5 e 10 anos.
10. Não há código SIGTAP para a tecnologia; microcusteio contemporâneo da angiotomografia **e dos comparadores** é condição necessária para análise econômica simétrica. O instrumento administrativo para o protocolo já existe: as OCI de síndrome coronariana crônica remuneram por episódio e nomeiam o exame de cada progressão (progressão II, R$ 840,00, cintilografia) — uma progressão anatômica (angiotomografia), em alternativa à progressão II, incorpora a substituição no próprio código; e o protocolo deve excluir explicitamente o assintomático, indicação de classe III em todas as diretrizes, porque código novo sem protocolo vira rastreamento.

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

Os quatro invasivo-primeiro não são comparáveis aos demais: a população já estava referenciada para procedimento invasivo e a taxa do braço controle é determinada pelo desenho. CATCH e CARE-CCTA entram apenas no desfecho de cateterismo sem DAC obstrutiva (seção 4.8). Revascularização por braço, usada na seção 4.6: PRECISE 9,2% vs 5,2%; Foy 2017 (13 ensaios) 7,2% vs 4,5%; SCOT-HEART 233 vs 201 (20 m) e 279 vs 267 (5 a); DISCHARGE 14,2% vs 18,0%; CONSERVE 13% vs 18%. Nos ensaios em que a revascularização não é desagregada, ela é valorada como angioplastia. Os Δ de cateterismo provêm de 10 ensaios e 1 metanálise; CATCH e CARE-CCTA (12 estudos ao todo) só entram na eficiência diagnóstica.

---

## Referências

1. Brasil. Ministério da Saúde. Conitec. Relatório de Recomendação Preliminar — Angiotomografia coronariana como exame de primeira linha. CP nº 73/2026. Disponível em: gov.br/conitec.
2. Brasil. Ministério da Saúde. Portaria SAES/MS nº 3.695, de 15 de janeiro de 2026. DOU nº 18, 27 jan 2026, Seção 1, p. 89–90. Republicada em 18 mai 2026.
3. Carmo PB, Magliano CAS, Rey HCV, Camargo GC, Trocado LFL, Gottlieb I. Análise da Custo-Efetividade da Angiotomografia Coronariana no SUS, em Comparação com Outros Métodos Não Invasivos na Suspeita de DAC Estável. Arq Bras Cardiol. 2022;118(3):578-85. DOI 10.36660/abc.20201050. PMID 35137778. PMC8959029.
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
20. Shiozaki A, Torreão J, Costa IBSS, Suarez AB, Silva MT, Oliveira TG, et al. Análise de Custo-Efetividade da Angiotomografia Coronária como Exame Preferencial na Investigação de Dor Torácica Estável na Saúde Suplementar no Brasil. Arq Bras Cardiol. 2025;122(12):e20250204 (epub 9 jan 2026). DOI 10.36660/abc.20250204. PMID 41637322. [fonte do preço da angiotomografia na saúde suplementar, R$ 1.311,95, "referência da ANS", e do cateterismo, R$ 1.900,79; baseada na CBHPM 2022 (AMB)]
21. Cesar LAM, Gowdak LHW, Pavanello R et al. Diretriz de Síndrome Coronariana Crônica – 2025. Arq Bras Cardiol. 2025;122(9):e20250619. DOI 10.36660/abc.20250619. PMID 41294178. Erratum 2026;123(7):e20260565 (autoria apenas).
22. Mark DB et al. Economic outcomes with anatomical versus functional diagnostic testing for coronary artery disease (PROMISE). Ann Intern Med. 2016;165:94-102. PMID 26857050.
23. SCOT-HEART Investigators. 10-year outcomes. N Engl J Med. 2025. PMID 39863372.
24. Magalhães TA, Carneiro ACC, Moreira VM et al. Diretriz de Tomografia Computadorizada e Ressonância Magnética Cardiovascular da SBC e do CBR – 2024. Arq Bras Cardiol. 2024;121(9):e20240608. DOI 10.36660/abc.20240608. PMID 39475988.
25. Vrints C, Andreotti F, Koskinas KC et al. 2024 ESC Guidelines for the management of chronic coronary syndromes. Eur Heart J. 2024;45(36):3415-537. DOI 10.1093/eurheartj/ehae177. PMID 39210710.
26. Gulati M, Levy PD, Mukherjee D et al. 2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain. Circulation. 2021;144(22):e368-454. DOI 10.1161/CIR.0000000000001029. PMID 34709879.
27. Virani SS et al. 2023 AHA/ACC/ACCP/ASPC/NLA/PCNA Guideline for the Management of Patients With Chronic Coronary Disease. Circulation. 2023;148:e9-e119. DOI 10.1161/CIR.0000000000001168.
28. NICE. Recent-onset chest pain of suspected cardiac origin: assessment and diagnosis. Clinical guideline CG95. 2010, atualizada 30 nov 2016. NCBI Bookshelf NBK553650.
29. Duarte M. Doenças cardiovasculares causam mais de 300 mil mortes por ano no Brasil; Conitec abre Consulta pública sobre angiotomografia coronariana no SUS [release de imprensa]. Jornal do Brás, 11 ago 2026. Disponível em: https://jornaldobras.com.br/noticia/133881/ (acesso em 16 ago 2026).
30. Brasil. Ministério da Saúde. Conitec. Relatório para a Sociedade nº 745 — Angiotomografia coronariana como exame de primeira linha em pacientes sintomáticos e probabilidade pré-teste baixa ou intermediária com suspeita de doença arterial coronariana estável. Brasília, ago 2026. Disponível em: gov.br/conitec (acesso em 17 ago 2026).

---

**Autoria e conflitos de interesse:** conforme identificação no formulário da consulta pública (o anexo não contém dados pessoais nem assinaturas, por exigência do formulário).
**Data:** agosto de 2026
