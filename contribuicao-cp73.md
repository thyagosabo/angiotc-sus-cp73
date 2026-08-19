# Contribuição à Consulta Pública nº 73/2026 — Conitec

**Tema:** angiotomografia coronariana (angioTC) como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de doença arterial coronariana estável.

**Natureza da contribuição:** técnico-científica.

---

## Quadro-resumo

| Pergunta do Comitê | Resposta desta contribuição |
|---|---|
| Capacidade instalada | **432 tomógrafos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS (CNES 06/2026), um piso documentado, já que 2.785 equipamentos ainda não têm o número de canais especificado. Desses, **79 estabelecimentos** reúnem hardware compatível, hemodinâmica e produção coronariana em 2025. Doze UFs não têm nenhum estabelecimento nesse estrato; três não têm sequer um tomógrafo ≥64 confirmado. |
| Custo do percurso atual | R$ 185,46 por episódio de investigação funcional (mix médio, SIA 2025); R$ 730,14 por cateterismo. Ambos são preços de tabela, não custos de produção. |
| Preço admissível | Depende de **qual exame a angioTC substitui e de quanta revascularização induz**, nenhum dos dois identificável nos registros. Nos ensaios com comparador não invasivo, o Δ de cateterismo foi de −6,3 a +4,1 por 100. **Sem protocolo de posicionamento (adoção aditiva), nenhum preço plausível é neutro: teto de R$ 30.** Só com exames e cateterismo, a neutralidade vai de **R$ 139–215** (mix médio) a **R$ 741–817** (cintilografia); incluindo a revascularização observada, o cenário cintilografia cai para **R$ 458–560** e os demais ficam abaixo de R$ 300. O preço proposto de R$ 550 fica **fora do alcance na probabilidade baixa** e só entra na **zona de incerteza, na intermediária, quando substitui cintilografia**. |
| Outro PICO | Em pacientes com cinecoronariografia eletiva já indicada (filtro pré-cateterismo, quatro ensaios), o preço de neutralidade é de **R$ 482–625** só com exames, subindo a **R$ 841–868** com a revascularização observada. É população distinta, não intercambiável com a apreciada. |
| Conclusão | **A sustentabilidade orçamentária depende de três parâmetros que os registros não identificam: o exame substituído, a revascularização induzida e a posição no percurso.** Estratificando por probabilidade pré-teste com o comparador que as diretrizes indicam, a mesma tecnologia ao mesmo preço é expansiva na baixa e incerta na intermediária (quando substitui cintilografia). O PICO submetido reproduz a Diretriz SBC/CBR de TC/RM 2024, que trata "baixa ou intermediária" como faixa única; a Diretriz SBC de SCC 2025, posterior e específica, estratifica (IIb-B na baixa, I-A na intermediária). A evidência econômica não sustenta decisão uniforme para toda a faixa baixa ou intermediária; sustenta condicionar qualquer incorporação ao posicionamento e ao exame substituído, alinhando-a à diretriz mais recente, com protocolo que diga, em cada faixa, o que a angioTC substitui. |

---

## 1. Objeto da contribuição

O Relatório de Recomendação Preliminar^1^ registra que a deliberação desfavorável de 3 de julho de 2026 se fundamentou em incertezas sobre a avaliação econômica, o impacto orçamentário, a capacidade de implementação e a delimitação da população elegível. Entre os pontos que o Comitê destacou como essenciais ao esclarecimento em consulta pública estão a estimativa da capacidade instalada, a necessidade ou não de aquisição de equipamentos e o impacto real sobre angiografias invasivas e testes funcionais.

Esta contribuição responde a esses pontos com uma análise nacional construída sobre bases públicas: CNES, SIA/SUS, SIH/SUS, SIGTAP e IBGE. Vale notar que o relatório preliminar caracteriza a demanda e os preços por DATASUS/TABNET e SIGTAP, mas não usa o CNES para dimensionar a capacidade instalada, justamente o dado cuja ausência motivou parte da recomendação. O dossiê do demandante não é público; esta contribuição trabalha com os dois relatórios disponíveis (o de Recomendação Preliminar e o Relatório para a Sociedade nº 745^30^). O método, os endereços de origem e o código estão no Apêndice A; as seções 2 e 3 são reproduzíveis a partir dos microdados por um único script (`analise_final.py`), e a seção 4 depende adicionalmente de valores extraídos das publicações listadas no Apêndice B.

---

## 2. Capacidade instalada: o que o cadastro nacional já permite responder

*Fonte: CNES, arquivos de equipamentos, competência 06/2026, 27 UFs. Consideramos apenas equipamentos disponíveis ao SUS e em uso; a classificação por canais é autodeclarada pelo estabelecimento.*

A Portaria SAES/MS nº 3.695/2026^2^ desmembrou o código genérico de tomógrafo em cinco categorias por número de canais (4, 16, 32, 64 e 128). Tornou-se assim possível responder diretamente à especificação de ≥64 canais adotada pelas diretrizes citadas no relatório preliminar, ao contrário do que sugeririam as tabelas de conversão ainda distribuídas com os arquivos, que não refletem a portaria.

### 2.1 Estratificação do parque

| Camada | Definição | Estabelecimentos | Equipamentos |
|---|---|---|---|
| **Compatível confirmado (≥64 canais)** | códigos 29 + 30 | **315** | **432** |
| — 64 canais | código 29 | 211 | 293 |
| — 128 canais | código 30 | 123 | 139 |
| **Incompatível confirmado (<64)** | códigos 26–28 | 672 | 736 |
| **Especificação não declarada** | código 11 | 2.534 | 2.785 |
| **Parque total disponível ao SUS** | | **3.395** | **3.953** |

As camadas se sobrepõem por estabelecimento (77 têm equipamentos ≥64 e <64; 49 têm reclassificados e genéricos): a coluna de estabelecimentos soma 3.521 = 3.395 + 77 + 49; a de equipamentos soma exatamente.

### 2.2 A reclassificação está incompleta, e esse é o achado operacional central

Em junho de 2026, apenas 861 estabelecimentos (25,4%) haviam migrado integralmente para os novos códigos, e 2.534 (74,6%) ainda tinham ao menos um equipamento sob o código genérico. O enunciado correto da capacidade é, portanto: **432 equipamentos de ≥64 canais estão documentados como disponíveis ao SUS, e esse é um piso, não uma estimativa da capacidade real.** O número verdadeiro é 432 mais uma fração desconhecida dos 2.785 equipamentos ainda não classificados. Recomenda-se que a apreciação final utilize o cadastro na competência mais recente e registre explicitamente a proporção reclassificada, e que, se a adesão seguir baixa, a SAES considere instrumentos para completá-la.

### 2.3 Estratos de prontidão

Ter hardware compatível não equivale a estar apto. Cruzamos o estrato ≥64 canais com dois marcadores independentes de maturidade cardiovascular: sala de hemodinâmica no mesmo CNES e produção coronariana invasiva efetivamente realizada em 2025.

| Estrato | Estabelecimentos |
|---|---|
| ≥64 canais confirmado | 315 |
| ≥64 canais + hemodinâmica no mesmo CNES | 114 |
| ≥64 canais + produção coronariana documentada em 2025 | 96 |
| **≥64 canais + hemodinâmica + produção coronariana** | **79** |

O estrato de 79 estabelecimentos é o de maior plausibilidade de implantação sem aquisição de tomógrafo. Ressalve-se que software de análise cardíaca, sincronização eletrocardiográfica, bomba injetora e profissionais habilitados em laudo cardiovascular não constam do CNES e não são verificáveis aqui. A co-localização com hemodinâmica não é requisito técnico: é adotada como marcador de maturidade institucional, não como limite inferior de capacidade. O CNES tampouco informa horas de operação ou agenda: o parque tomográfico do SUS realizou cerca de 13,4 milhões de exames em 2025 (cerca de 3.400 por equipamento), e a capacidade em vagas para exames adicionais não foi estimada.

### 2.4 Distribuição e equidade

A densidade nacional é de 2,02 equipamentos compatíveis por milhão de habitantes. Amapá, Piauí e Tocantins não têm nenhum tomógrafo ≥64 confirmado; doze UFs não têm nenhum estabelecimento no estrato de prontidão (AC, AL, AM, AP, GO, MT, PA, PI, RO, RR, SE, TO). São Paulo concentra 164 equipamentos compatíveis e 23 estabelecimentos prontos. A desigualdade sobre o hardware compatível supera a do parque agregado (coeficiente de variação 0,86 contra 0,32; Gini 0,30 contra 0,14): projeções de difusão ancoradas no total de tomógrafos superestimam a capacidade acessível, e o fazem de modo desigual entre regiões.

---

## 3. Cenário atual: o que o SUS efetivamente realiza

*Fonte: SIA/SUS e SIH/SUS, competências 01–12/2025, 27 UFs, todos os arquivos processados sem perda. Códigos conferidos contra a SIGTAP 08/2026.*

### 3.1 A unidade de análise é o episódio, não o procedimento faturado

A cintilografia de perfusão é registrada sob dois códigos, estresse e repouso, que representam etapas de um mesmo exame. Contá-los separadamente infla o denominador em 19%. Adotamos a convenção, coerente com a literatura nacional,^3^ de contar um episódio por código de estresse.

| Episódio de investigação funcional | Episódios | Volume | Gasto | Gasto (%) |
|---|---|---|---|---|
| Teste ergométrico | 598.695 | 76,0% | R$ 19,3 mi | 13,2% |
| Cintilografia de perfusão | 151.784 | 19,3% | R$ 119,4 mi | 81,7% |
| Ecocardiografia de estresse | 33.766 | 4,3% | R$ 6,6 mi | 4,5% |
| Cintilografia de câmaras (esforço) | 3.709 | 0,5% | R$ 0,8 mi | 0,5% |
| **Total** | **787.954** | | **R$ 146,1 mi** | |
| **Custo médio por episódio** | | | **R$ 185,46** | |

O cateterismo (163.803 procedimentos) custou em média R$ 730,14 pelo SIA; o valor da AIH é R$ 772,80, parâmetro que o NATS adotou no relatório preliminar. Ambos são preços de tabela, não custos de produção: comparar uma tecnologia microcusteada contra comparadores remunerados por tabela é assimétrico, e o sentido do viés não é conhecido.

### 3.2 O volume está no exame barato; o dinheiro, no caro

A ergometria custa em média R$ 32 e responde por 76% dos episódios, mas só 13% do gasto; a cintilografia, por 19% dos episódios e 82% do gasto. Esta é uma afirmação sobre registros administrativos, não sobre a população elegível à angioTC: a ergometria tem indicações muito além da investigação inicial de DAC estável (capacidade funcional, arritmias de esforço, estratificação pré-operatória, seguimento). Sem identificação de paciente e indicação clínica, não é possível saber qual exame a angioTC substituiria na população-alvo, e esse é o parâmetro dominante da análise econômica (seção 4).

### 3.2.1 As linhas de cuidado organizadas (OCI de SCC)

O Ministério da Saúde estruturou a investigação da síndrome coronariana crônica em três OCI remuneradas como episódio: avaliação inicial (R$ 270), progressão I com eco de estresse (R$ 250) e progressão II com cintilografia (R$ 840). Quando a OCI é o procedimento principal, seus componentes aparecem zerados no SIA e não são recontados. Em 2025 as OCI de SCC responderam por 0,96% dos episódios (7.616), em 148 estabelecimentos de 13 UFs. Substituir o intercepto do modelo pelo ponderado com OCI move o preço de neutralidade do cenário mix em apenas R$ 2 e não altera nenhuma conclusão.

### 3.3 A angioTC é administrativamente invisível

Não há código para angiotomografia coronariana na SIGTAP (08/2026, 5.023 procedimentos verificados). A produção que exista é registrada sob código genérico de tomografia ou não é registrada. O código de contraste para tomografia, aliás, não registra faturamento em 2025. Consequência: nenhum custo unitário para a angioTC pode ser ancorado em produção histórica do SUS, o que torna o microcusteio contemporâneo uma condição necessária.

### 3.4 A escala da cardiologia intervencionista é contexto, não denominador

Em 2025 o SUS registrou 133.934 angioplastias e 23.290 revascularizações cirúrgicas, em 273 estabelecimentos. Esses números descrevem a escala da rede, não o denominador econômico da estratégia: a população submetida a esses procedimentos inclui infarto, síndrome coronariana aguda e doença conhecida, que não são desfecho da investigação de pacientes estáveis de probabilidade baixa ou intermediária. A sustentabilidade da estratégia não depende de reduzir esse montante.

---

## 4. Análise de limiar: quanto o SUS poderia pagar

### 4.1 Por que limiar, e não estimativa pontual

O SIA não tem identificador de paciente utilizável. Não é possível saber se um cateterismo registrado ocorreu após um teste funcional específico, na mesma pessoa ou na mesma indicação. A razão entre contagens agregadas de cateterismos e de testes funcionais não é uma probabilidade condicional e não pode projetar redução de procedimentos: fazê-lo seria inferência ecológica. Por isso não estimamos quantas angiografias a angioTC evitaria. Respondemos à pergunta inversa:

> **Quantas angiografias por 100 pacientes seria preciso evitar, a cada preço, para que a estratégia fosse orçamentariamente neutra?**

A plausibilidade clínica de cada valor fica a cargo do leitor especializado.

### 4.2 Duas equações, uma por PICO

Sob substituição de um episódio funcional por uma angioTC, o preço de neutralidade é o custo do exame substituído mais o dos cateterismos induzidos. Quando a angioTC filtra um cateterismo já indicado, a investigação prévia é comum aos dois braços e se cancela, restando só o crédito dos cateterismos evitados:

```
P_neutralidade, primeira linha  =  C_substituído  +  (Δ_CATE / 100) × C_CATE
P_neutralidade, filtro          =                    (Δ_CATE / 100) × C_CATE
```

Adotamos C_CATE = R$ 730,14 (SIA 2025) e o Δ como parâmetro declarado; o desenho de cada ensaio determina qual equação se aplica.

O SCOT-HEART tem desenho aditivo (angioTC somada ao cuidado padrão) e por isso não substitui episódio funcional, recaindo na segunda equação embora sua população seja de primeira linha. Esse não é um detalhe de ensaio: é o cenário de referência para uma incorporação que crie o código sem protocolo vinculante e, a juízo dos autores, o mais provável nessas condições. Há 787.954 episódios funcionais por ano em curso e nada que os retire do percurso; a angioTC tende a entrar somada à ergometria, não em seu lugar. É um juízo sobre implementação, não uma medida: o SIA não registra sobreposição de testes por paciente. Nomeamos esse sexto cenário "adoção aditiva (sem protocolo)" e o tratamos como referência.

| Cenário | C_substituído | Origem |
|---|---|---|
| **Adoção aditiva (sem protocolo)** | **R$ 0,00** | angioTC somada ao percurso; nada substituído; desenho do SCOT-HEART |
| Mix médio do SIA | R$ 185,46 | 76% ergometria; equivale ao PICO como submetido, sem estratificar |
| Mix do NATS, como publicado | R$ 316,76 | ergometria + 50% cintilografia + 50% eco, cintilografia só pelo código de estresse |
| Mix do NATS, por episódio | R$ 523,81 | mesmo percurso, cintilografia como episódio (dois códigos) |
| Ecocardiografia de estresse | R$ 196,39 | valor médio aprovado por episódio |
| Cintilografia de perfusão | R$ 786,83 | valor médio aprovado por episódio |

Qual desses corresponde à população elegível não é identificável nos registros. A Diretriz SBC de SCC 2025^21^ posiciona a angioTC por faixa: na intermediária, exame inicial classe I-A ou alternativa à prova funcional; na baixa, classe IIb-B ("ajustar PPT ou angiotomografia"). O exame que ela substituiria é, por recomendação, a prova funcional que o serviço realizaria, e a diretriz condiciona essa escolha à capacidade funcional, ao ECG basal, ao acesso e à função renal, sugerindo começar pela ergometria quando a capacidade funcional é preservada. É o percurso que o SIA mostra (76% do volume). As diretrizes internacionais convergem com essa estratificação: a ESC 2024 recomenda a angioTC como preferida apenas na probabilidade baixa-a-moderada, a AHA/ACC 2021 a trata como co-igual à imagem funcional no risco intermediário (a de 2023 remete à de 2021), e só o NICE a oferece sem estratificar.^25–28^

### 4.3 Δ necessário por preço e por exame substituído

O relatório preliminar adota R$ 550 como preço proposto. Aos preços de referência, o Δ de cateterismo por 100 necessário para neutralidade (só exames e cateterismo):

| Preço da angioTC | aditiva | mix SIA | NATS publicado | NATS por episódio | eco | cintilografia |
|---|---|---|---|---|---|---|
| R$ 196,41 (proxy TC tórax) | 26,9 | 1,5 | neutro | neutro | 0,0 | neutro |
| **R$ 550,00 (demandante)** | **75,3** | **49,9** | **31,9** | **3,6** | 48,4 | **neutro** |
| R$ 622,54 (microcusteio 2022 corrigido) | 85,3 | 59,9 | 41,9 | 13,5 | 58,4 | neutro |
| R$ 1.311,95 (saúde suplementar) | 179,7 | 154,3 | 136,3 | 107,9 | 152,8 | 71,9 |

Ao preço da saúde suplementar substituindo o mix médio, seriam necessárias mais angiografias evitadas do que pacientes investigados: inalcançável neste modelo. Na adoção aditiva, o Δ exigido a R$ 550 é 75,3 por 100, o mesmo limiar do filtro (a equação é a mesma); a diferença é de onde vem o Δ. Em pacientes já indicados a cateterismo, 75 por 100 é o que o DISCHARGE observou; em primeira linha, o melhor Δ observado é 4,1.

### 4.4 O confronto com a evidência depende do exame substituído

Nos ensaios que compararam a angioTC a estratégias não invasivas de primeira linha,^5,7–11^ o Δ de cateterismo (positivo = evitados por 100) foi:

| Ensaio | Comparador | Δ /100 |
|---|---|---|
| CAPP | ergometria | −6,3 |
| PROMISE | funcional | −4,1 |
| Foy 2017 (subgrupo estável) | funcional | −2,9 |
| Foy 2017 (13 ensaios) | funcional | −2,6 |
| CRESCENT-I | funcional | −1,0 |
| CRESCENT-II | funcional | +1,4 |
| PRECISE | usual testing | +4,1 |

Faixa observada: −6,3 a +4,1 por 100. Aplicada a cada C_substituído, a neutralidade (só exames) vai de R$ 139–215 (mix) a R$ 741–817 (cintilografia): uma ordem de grandeza para o mesmo Δ. Se a angioTC substitui o mix médio, o preço de neutralidade fica 2,6 a 4 vezes abaixo do proposto, e o Δ necessário (49,9) é doze vezes o melhor observado. Se substitui exclusivamente a cintilografia, o custo do comparador financia a troca neste modelo restrito. Se não substitui nada, nenhum preço é neutro: mesmo gratuita, a angioTC adicionada ao percurso só é neutra se não induzir cateterismos. Isso não enfraquece a análise; é sua forma mais forte: sem especificação de posicionamento, a tecnologia é expansiva por construção, qualquer que seja o preço.

A pergunta decisiva, portanto, não é o Δ de cateterismos; é qual exame a angioTC substituiria na população elegível, parte do que o Comitê pediu como delimitação da população. Ela não é respondível pelo SIA, mas é respondível por protocolo, e a Diretriz SBC de SCC 2025 já estratifica a indicação por probabilidade pré-teste.

Ressalvas: os horizontes diferem (90 dias a 18 meses) e os pontos não constituem metanálise; o braço de intervenção do PRECISE inclui diferimento em 20% dos pacientes de menor risco (não é substituição 1:1); a metanálise de Foy^11^ inclui 9 de 13 ensaios de emergência, e a faixa usa o subgrupo estável (o Δ dos 13 ensaios, −2,6, entra apenas pareado com a revascularização dos mesmos 13, na seção 4.6); as contagens do CAPP provêm do gráfico de floresta de Foy; em CRESCENT-I e II as diferenças não são estatisticamente significativas. O PRECISE ilustra que reduzir cateterismo não implica reduzir gasto: reduziu o cateterismo total de 16,9% para 12,8%, mas aumentou a revascularização de 5,2% para 9,2%; seu custo diagnóstico caiu 27% e o de revascularização subiu 67%.^10^

### 4.5 O espaço econômico é maior em outro PICO

Os ensaios com comparador invasivo-primeiro (cinecoronariografia já indicada)^12–15^ recaem na equação de filtro:

| Ensaio | Δ /100 | Preço de neutralidade |
|---|---|---|
| CONSERVE | 66,0 | R$ 481,89 |
| Reis 2022 | 72,2 | R$ 526,97 |
| DISCHARGE | 75,1 | R$ 548,25 |
| CAD-MAN | 85,6 | R$ 625,21 |

Nessa indicação o preço de neutralidade é R$ 482–625, independentemente do exame prévio, porque ele cancela. A R$ 550, o limiar é 75,3 por 100: o DISCHARGE fica a 0,2 abaixo. Com C_CATE de R$ 772,80 (AIH), a faixa passa a R$ 510–662. É outra população e outro PICO: a taxa do braço comparador (89% a 100%) decorre do desenho, e não constitui alternativa automaticamente substituível à incorporação analisada. Registre-se que o próprio dossiê e a reanálise do NATS já usaram o DISCHARGE,^14^ ensaio dessa população, como fonte de parâmetros para o PICO de primeira linha.

A mesma transposição está em Shiozaki et al.,^20^ a avaliação econômica na saúde suplementar, o estudo mais recente e o mais presente no debate público sobre o pedido. Ele estima economia de R$ 1.021 por beneficiário em cinco anos numa carteira de 100.000 vidas. Compara a angioTC (R$ 1.311,95) com a angiografia invasiva como estratégia inicial (R$ 1.900,79, único comparador), com eventos do DISCHARGE, e declara não ter comparado com testes funcionais: é um modelo do filtro pré-cateterismo, não da primeira linha em apreciação. Nesse desenho o Δ exigido é 69 por 100 (1.311,95 ÷ 1.900,79) e o DISCHARGE (75,1) o alcança, pelo mecanismo da tabela acima. A economia é por beneficiário de carteira, não por paciente examinado; as projeções de dezenas de bilhões de reais veiculadas na imprensa em agosto de 2026 não constam do artigo, e o próprio material as qualifica como projeção teórica para a saúde suplementar, "sem representar diretamente uma estimativa de impacto" para o SUS.^29^

Recomenda-se que a apreciação final avalie o filtro pré-cateterismo como pergunta separada, com critérios de elegibilidade próprios.

### 4.6 A revascularização não pode ficar fora

As subseções anteriores creditam só exames e cateterismo, mas os ensaios reportam também revascularização, cujo custo unitário o SIH fornece (R$ 7.713 por angioplastia, R$ 25.904 por cirurgia). Incluindo esse componente:

| Cenário | Δ revasc /100 | Neutralidade sem revasc. | **Neutralidade com revasc.** |
|---|---|---|---|
| Cintilografia + PRECISE | +4,0 | R$ 817 | **R$ 458** |
| Cintilografia + Foy 2017 | +2,7 | R$ 768 | **R$ 560** |
| Adoção aditiva + SCOT-HEART | +1,5 / +0,6 | R$ −3 / +4 | **R$ −122 / −41** |
| Filtro, DISCHARGE | −3,8 | R$ 548 | **R$ 841** |
| Filtro, CONSERVE | −5,0 | R$ 482 | **R$ 868** |

Com a revascularização, o cenário mais favorável de primeira linha deixa de superar o preço proposto e passa a cercá-lo (R$ 458–560 contra R$ 550): no par PRECISE, o único ensaio contemporâneo com Δ de cateterismo favorável, R$ 550 excede a neutralidade em R$ 92 por paciente. O filtro, que sem revascularização ficava abaixo, passa a superá-lo com folga (R$ 841 no DISCHARGE, R$ 868 no CONSERVE). O par de Foy usa o Δ de cateterismo (−2,6) e a revascularização (4,5% → 7,2%) dos mesmos 13 ensaios. Há uma assimetria declarada, conservadora contra o filtro: os débitos de primeira linha incluem a parcela cirúrgica, enquanto os créditos do DISCHARGE e do CONSERVE são valorados só como angioplastia, por falta de desagregação. A única análise de custo de ensaio no cenário de substituição de imagem funcional, o PROMISE (comparador majoritariamente cintilografia), não encontrou economia, "associada a mais revascularizações e cateterismos", e sem diferença aos 3 anos.^22^

### 4.7 Por estrato de probabilidade pré-teste

O SIA não distingue a probabilidade pré-teste, mas o modelo distingue por premissa: as diretrizes dizem qual exame a angioTC substituiria em cada faixa, e essa premissa pode ser declarada em vez de escondida numa média.

| Estrato | Comparador (premissa) | C_subst. | Só exames | **Com revasc.** | Δ a R$ 550 |
|---|---|---|---|---|---|
| Qualquer, sem protocolo | adoção aditiva | R$ 0 | R$ −46 a +30 | **R$ −122 a −41** | 75,3 |
| Baixa | diferir / ajustar PPT | R$ 0 | teto R$ 0 | — | — |
| Baixa | ergometria | R$ 32 | R$ −14 a +62 | R$ −297 a −195 | 70,9 |
| Não estratificado (PICO submetido) | mix médio do SIA | R$ 185 | R$ 139 a 215 | R$ −144 a −42 | 49,9 |
| Intermediária | ecocardiografia de estresse | R$ 196 | R$ 150 a 226 | R$ −133 a −31 | 48,4 |
| Intermediária | percurso do NATS por episódio | R$ 524 | R$ 477 a 554 | R$ 195 a 297 | 3,6 |
| Intermediária (com protocolo) | cintilografia de perfusão | R$ 787 | R$ 741 a 817 | **R$ 458 a 560** | já neutro |
| Já indicado a cateterismo | cateterismo direto | cancela | R$ 482 a 625 | **R$ 841 a 868** | 75,3 |

Notas: o débito de revascularização vem do PRECISE (+4,0/100) e de Foy 2017, 13 ensaios (+2,7/100), aplicados como envelope aos cenários de substituição; no aditivo, é a do próprio SCOT-HEART. Na probabilidade baixa esse envelope, de população intermediária, tende a superestimar o débito, sem mudar o sinal. Para o diferimento, o contrafactual não contém cateterismo diagnóstico: Δ ≤ 0 e teto R$ 0. Fonte: `analise_final.py` e `output/out-limiar-por-estrato.csv`.

Três leituras. **Primeira: na probabilidade baixa, nenhum preço plausível fecha.** Com o comparador que as diretrizes indicam (nenhum exame ou ergometria), o teto é R$ 30 a R$ 62 só com exames e negativo com revascularização, abaixo de qualquer preço de referência. **Segunda: na intermediária, o resultado depende de qual imagem funcional sai do percurso.** Substituindo ecocardiografia, R$ 550 fica fora; substituindo cintilografia, entra na zona de incerteza mesmo com revascularização (R$ 458–560). Esse nicho tem no máximo 151.784 episódios/ano (19% do volume), e a fração substituível é menor, porque parte da cintilografia é feita em doença conhecida e parte em pacientes idosos, obesos, com fibrilação atrial ou calcificação extensa, nos quais a angioTC rende pior: justamente os que as diretrizes encaminham à imagem funcional. O percurso misto do NATS, que sem revascularização cercava R$ 550, cai a R$ 195–297 quando ela entra. Se, na prática do SUS, o comparador da intermediária for a ergometria, o resultado colapsa no da baixa. Sem protocolo, o cenário descritivo da rede é a ergometria seguida de imagem numa fração dos pacientes (p ≤ 0,31 pelos volumes do SIA), e ele fica entre o mix médio e a ecocardiografia (≤ R$ 196–273 só com exames, negativo com revascularização). **Terceira: o PICO como submetido, a média não estratificada, é puxado para o estrato baixo**, porque três quartos do volume atual são ergometria. Estratificar não é análise de sensibilidade; é o resultado: no SUS como ele é, "primeira linha" significa substituir a ergometria, e isso não fecha a nenhum preço plausível. A angioTC paga quando entra depois da ergometria, no lugar do encaminhamento à cintilografia (intermediária com protocolo) ou da cinecoronariografia eletiva já indicada (filtro, R$ 482–868). Capacidade e posicionamento apontam para o mesmo lugar: o estrato pronto de 79 são hospitais com hemodinâmica, onde o paciente já referenciado ao cateterismo está.

### 4.8 Um segundo desfecho: eficiência diagnóstica

Apresentamos o cateterismo sem DAC obstrutiva como métrica de eficiência diagnóstica, fora do cálculo econômico (que usa cateterismo total). Pelo IQWiG,^4^ os cateterismos sem doença obstrutiva evitados por 100 pacientes vão de 0,9 a 5,9 contra métodos funcionais (metanálise de alta certeza: OR 0,77, IC95% 0,64–0,94) e de 53,7 a 81,0 contra cateterismo direto. A direção favorece a angioTC em todos os ensaios e nos dois PICOs. É uma afirmação sobre uso de recursos no curto prazo, não sobre o benefício clínico: o SCOT-HEART demonstrou redução de morte coronariana e infarto em 5 e 10 anos,^6,23^ pergunta distinta da neutralidade orçamentária, à qual esta contribuição se restringe.

### 4.9 Limitação desta seção

O código de cateterismo é genérico e não distingue cinecoronariografia de outros cateterismos diagnósticos. Os denominadores do SIA incluem assintomáticos e doença conhecida, fora do PICO. Contraindicações relativas à angioTC (doença renal avançada, alergia a contraste, frequência não controlável, calcificação extensa) reduzem a população elegível e não foram descontadas. Dos 432 equipamentos ≥64 canais, 293 são de 64 canais e o CNES não registra geração nem ano; com aquisição retrospectiva a dose é várias vezes maior. O gargalo previsível de implantação é a equipe, não o tomógrafo. A substituição 1:1 é premissa declarada; complicações, permanência, angioTC não diagnósticas, testes funcionais subsequentes e achados incidentais não foram quantificados. Os Δ utilizados são diferenças aritméticas entre percentuais por braço, não estimativas agrupadas; a metanálise em rede de Siontis^16^ reporta NNT 24 sobre taxa-base de 12,2%, cerca de 4 por 100, coerente com a faixa aqui usada, e a diferença de risco agrupada de Hulten^19^ (+21 por 1.000) refere-se a população de emergência. Sobre fontes secundárias: a revisão de Zito^17^ teve errata publicada e os intervalos indexados no PubMed permanecem desatualizados; a de Hwang^18^ contém erro de extração para o SCOT-HEART e não foi utilizada.

---

## 5. Síntese

1. Desde a Portaria SAES/MS 3.695/2026, o CNES permite identificar tomógrafos por faixa de canais. Em 06/2026 há **432 equipamentos de ≥64 canais em 315 estabelecimentos** disponíveis ao SUS.
2. A reclassificação está 25–27% concluída: os 432 são piso, e ainda há 2.785 equipamentos sem especificação. A apreciação final deveria usar a competência mais recente e registrar a proporção reclassificada.
3. **79 estabelecimentos** reúnem hardware ≥64 canais, hemodinâmica e produção coronariana documentada. Doze UFs não têm nenhum; AP, PI e TO não têm sequer tomógrafo ≥64 confirmado.
4. A investigação funcional do SUS concentra volume na ergometria (76%) e gasto na cintilografia (82%). Qual exame a angioTC substituiria na população elegível não é identificável nos registros: é o parâmetro dominante do modelo.
5. **A sustentabilidade da primeira linha depende de três parâmetros não identificáveis nos registros: o exame substituído, a revascularização induzida e a posição no percurso.** Só com exames e cateterismo, a neutralidade vai de R$ 139–215 (mix) a R$ 741–817 (cintilografia); com a revascularização observada, a cintilografia cai para R$ 458–560 e os demais ficam abaixo de R$ 300. O preço proposto (R$ 550) fica fora do alcance nos cenários de mix, ergometria e ecocardiografia, e só entra na zona de incerteza quando substitui cintilografia.
6. **Sem protocolo de posicionamento, nenhum preço plausível é neutro.** O cenário de referência passa a ser o aditivo, em que a angioTC é somada à ergometria em curso: preço de neutralidade de R$ −46 a +30. A tecnologia é expansiva por construção, qualquer que seja o preço. A condição de sustentabilidade não é o preço, é a especificação do que sai do percurso.
7. **O espaço econômico é maior em outro PICO.** Em pacientes já indicados a cateterismo, a neutralidade é R$ 482–625 só com exames, subindo a R$ 841–868 com a revascularização evitada. É população distinta, não intercambiável com a apreciada, e o relatório preliminar já usa um ensaio dela (DISCHARGE) para o PICO de primeira linha.
8. **Estratificar por probabilidade pré-teste não é sensibilidade, é o resultado.** Com o comparador que as diretrizes indicam, a mesma tecnologia ao mesmo preço é expansiva na baixa e incerta na intermediária (só quando substitui cintilografia). A Diretriz SBC de SCC 2025^21^ já faz essa estratificação (I-A na intermediária, IIb-B na baixa); o PICO submetido reproduz a Diretriz de TC/RM 2024,^24^ que trata "baixa ou intermediária" como faixa única. A evidência econômica não sustenta decisão uniforme para toda a faixa; sustenta condicionar qualquer incorporação ao posicionamento e ao exame substituído, alinhando-a à diretriz mais recente.
9. No horizonte econômico analisado, o benefício mais consistente é o aumento da adequação da indicação de cateterismo, não a redução de volume. Isto não caracteriza o benefício clínico: o SCOT-HEART demonstrou redução de morte coronariana e infarto em 5 e 10 anos.^6,23^
10. Não há código SIGTAP para a tecnologia; o microcusteio contemporâneo da angioTC e dos comparadores é condição necessária para análise simétrica. O instrumento para o protocolo já existe: as OCI de SCC remuneram por episódio e nomeiam o exame de cada progressão. Uma progressão anatômica, em alternativa à progressão II (cintilografia, R$ 840), incorporaria a substituição no próprio código. O protocolo deve excluir o assintomático, indicação de classe III.

Nada nesta contribuição se pronuncia sobre o mérito clínico da tecnologia. As conclusões dizem respeito exclusivamente à capacidade de implementação e à sustentabilidade orçamentária de curto prazo, nos termos em que o Comitê solicitou esclarecimento.

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
10. Douglas PS et al. PRECISE. JAMA Cardiol. 2023;8(10):904-14. PMID 37610731. Desfechos econômicos: Chew DS et al. Circ Cardiovasc Qual Outcomes. 2025;18(2):e011008. PMID 39895495.
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
22. Mark DB et al. Economic outcomes with anatomical versus functional diagnostic testing for coronary artery disease (PROMISE). Ann Intern Med. 2016;165(2):94-102. PMID 27214597.
23. Williams MC et al. SCOT-HEART, 10-year outcomes. Lancet. 2025;405(10475):329-37. PMID 39863372.
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
