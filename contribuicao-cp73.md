# Contribuição à Consulta Pública nº 73/2026 — Conitec

**Tema:** Angiotomografia coronariana como exame de primeira linha em pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de doença arterial coronariana estável.

**Natureza da contribuição:** técnico-científica.

---

## 1. Objeto da contribuição

O Relatório de Recomendação Preliminar registra que a deliberação desfavorável de 3 de julho de 2026 (153ª Reunião Ordinária) foi fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à **capacidade de implementação da tecnologia no SUS** e à delimitação da população elegível. O Comitê destacou como essenciais ao esclarecimento em consulta pública, entre outros pontos, "a estimativa da capacidade instalada", "a necessidade ou não de aquisição de equipamentos" e "o impacto real sobre a realização de angiografias invasivas e testes funcionais".

Esta contribuição responde a esses pontos com uma análise nacional construída **exclusivamente sobre bases públicas** — CNES, SIA/SUS, SIH/SUS, SIGTAP e IBGE. Nenhuma dessas bases é citada no relatório preliminar para caracterização de capacidade instalada; a sigla CNES não aparece no documento.

Método, endereços de origem e código no Apêndice A. Todos os números são reprodutíveis.

---

## 2. Capacidade instalada: uma banda, não um número

**Fonte:** CNES, arquivos de equipamentos (`EQ`), competência 06/2026, 27 UFs. Tomógrafo = `TIPEQUIP=01`, `CODEQUIP=11`. Sala de hemodinâmica = `CODEQUIP=10`. Considerados apenas equipamentos com `IND_SUS=1` e `QT_USO>0`.

A pergunta "quantos serviços poderiam realizar angiotomografia coronariana hoje" não admite resposta pontual a partir de dados públicos. Admite uma **banda com dois limites reprodutíveis**:

| Camada | Definição operacional | N |
|---|---|---|
| **Teto** | Estabelecimentos com tomógrafo em uso e disponível ao SUS | **2.534** (2.785 equipamentos) |
| **Piso** | Estabelecimentos com tomógrafo **e** sala de hemodinâmica no mesmo CNES | **216** (8,5% do teto) |
| *Referência* | Estabelecimentos que efetivamente realizaram angioplastia ou revascularização (SIH 2025) | *290* |

O **teto** superestima: possuir tomógrafo não implica sincronização eletrocardiográfica, protocolo, bomba injetora, controle de qualidade de imagem ou profissional habilitado em laudo cardiovascular — nenhum desses atributos consta do CNES.

O **piso** subestima deliberadamente: um serviço de radiologia com tomógrafo adequado e cardiologista treinado pode realizar o exame sem sala de hemodinâmica. A co-localização é adotada como marcador conservador de maturidade cardiovascular institucional, não como requisito técnico.

A convergência entre o piso (216) e a rede invasiva efetivamente ativa (290) sugere que a ordem de grandeza dos serviços com maturidade cardiovascular instalada está nas **centenas, não nos milhares**.

**Implicação para a análise de impacto orçamentário:** projeções de difusão ancoradas na disponibilidade agregada de equipamentos operam próximas ao teto da banda. Recomenda-se que a apreciação final exija a declaração explícita de qual camada de capacidade sustenta cada cenário de market share.

### 2.1 Distribuição e equidade

Densidade nacional: **13,05 tomógrafos-SUS por milhão de habitantes** (IBGE 2025, 213.421.037 hab.). Variação entre UFs de **6,1 vezes** — de 4,06 (Roraima) a 24,58 (Tocantins).

**Acre, Amazonas e Roraima não possuem nenhum estabelecimento com tomógrafo-SUS e hemodinâmica co-localizados.** Roraima não registrou nenhum procedimento coronariano invasivo em todo o ano de 2025.

Observa-se ainda relação **inversa** entre tamanho do parque e disponibilidade pública:

| UF | Tomógrafos em uso | Disponíveis ao SUS | % SUS | Densidade SUS/milhão |
|---|---|---|---|---|
| São Paulo | 1.201 | 446 | 37,1% | 9,68 |
| Rio de Janeiro | 590 | 200 | 33,9% | 11,61 |
| Distrito Federal | 156 | 37 | 23,7% | 12,35 |
| Tocantins | 57 | 39 | 68,4% | 24,58 |
| Amapá | 27 | 19 | 70,4% | 23,56 |

São Paulo concentra o maior parque do país e apresenta densidade de tomógrafos-SUS **abaixo da média nacional** — o gargalo é maior onde a população é maior.

---

## 3. Limitação do registro nacional e recomendação administrativa

**O CNES não permite identificar o número de canais/detectores dos tomógrafos.** Existe um único código para o item (`0111 — TOMÓGRAFO COMPUTADORIZADO`), sem desdobramento por cortes por rotação.

Não é possível, portanto, estimar a partir de fonte pública nacional quantos equipamentos atendem à especificação de **64 canais ou mais** — adotada pelas diretrizes citadas no próprio relatório preliminar, inclusive a recomendação do NICE ali transcrita.

Qualquer estimativa de capacidade apta, apresentada por qualquer parte, é necessariamente derivada de proxy ou de coleta primária, e deve declarar isso.

> **Recomendação, independente do mérito desta incorporação:** incluir desdobramento por faixa de canais no cadastro de equipamentos do CNES. Medida de baixo custo administrativo que instrumentaria esta e futuras avaliações de tecnologias dependentes de tomografia avançada.

---

## 4. Cenário atual: o que o SUS efetivamente realiza

**Fonte:** SIA/SUS e SIH/SUS, competências 01–12/2025, 27 UFs, 395 arquivos processados sem perda. Códigos conferidos contra SIGTAP competência 08/2026.

### 4.1 Investigação diagnóstica ambulatorial

| Procedimento | Código | Quantidade | Valor aprovado | Estab. | R$ médio |
|---|---|---|---|---|---|
| Teste ergométrico | 0211020060 | 598.695 | R$ 19,3 mi | 1.110 | 32,20 |
| Cateterismo cardíaco | 0211020010 | 163.803 | R$ 119,6 mi | 235 | 730,14 |
| Cintilografia perfusão — estresse | 0208010025 | 151.784 | R$ 61,8 mi | 358 | 406,99 |
| Cintilografia perfusão — repouso | 0208010033 | 151.225 | R$ 57,7 mi | 362 | 381,25 |
| Ecocardiografia de estresse | 0205010016 | 33.766 | R$ 6,6 mi | 308 | 196,39 |
| Cintilografia câmaras — esforço | 0208010076 | 3.709 | R$ 0,8 mi | 7 | 214,85 |
| **Investigação funcional não invasiva** | | **939.179** | **R$ 146,1 mi** | | **155,60** |
| **Total diagnóstico ambulatorial** | | **1.102.982** | **R$ 265,7 mi** | | |

**Achado central: o teste ergométrico responde por 63,7% de toda a investigação funcional não invasiva do SUS**, a um custo médio de R$ 32,20. O comparador efetivo da angiotomografia coronariana no SUS não é a cintilografia miocárdica — é o exame mais barato da tabela.

### 4.2 Desfecho invasivo

| Procedimento | Quantidade | Valor | Estabelecimentos |
|---|---|---|---|
| Angioplastia coronariana (0406030*) | 137.595 | R$ 1.112 mi | 289 |
| Revascularização miocárdica | 16.991 | R$ 423 mi | 219 |
| **Rede invasiva total** | | **R$ 1.535 mi** | **290** |

A via completa da DAC consome **R$ 1,80 bilhão/ano**, dos quais a etapa diagnóstica representa **14,8%**. A economia projetada pelo demandante depende de reduzir a fração de R$ 1,53 bilhão — precisamente aquela para a qual a metanálise do parecerista não encontrou diferença estatisticamente significativa em eventos cardiovasculares maiores, infarto, mortalidade ou hospitalização.

### 4.3 Angiotomografia coronariana é administrativamente invisível

Não existe código para angiotomografia coronariana na Tabela de Procedimentos do SUS (SIGTAP 08/2026, 5.023 procedimentos verificados). A produção atual do exame não é mensurável: ou é registrada sob código genérico de tomografia, ou não é registrada. Isso é coerente com o registro, no relatório preliminar, de que o exame ocorre em serviços públicos e conveniados sem utilização estruturada e sem procedimento específico.

Verificou-se adicionalmente que o código `0206030045 — CONTRASTE PARA TOMOGRAFIA COMPUTADORIZADA` **não registra faturamento no SIA em 2025**, o que impede seu uso como marcador de serviços com capacidade para exames contrastados.

**Consequência:** nenhum parâmetro de custo unitário para a angiotomografia coronariana pode ser ancorado em produção histórica do SUS. O microcusteio contemporâneo, com abertura completa de componentes, não é refinamento metodológico — é condição necessária.

### 4.4 Preço de neutralidade orçamentária

Sob a premissa conservadora de **substituição 1:1** (uma angiotomografia no lugar de um exame funcional) e comportamento downstream constante, o preço máximo pagável pelo SUS para que a estratégia seja neutra é o custo médio do exame que ela substitui:

> ### **P_neutralidade = R$ 155,60**

Sensibilidade, admitindo que a angiotomografia também evite parte dos cateterismos (razão CATE/exame funcional observada = 0,174):

| Redução de cateterismos | P_neutralidade |
|---|---|
| 0% | R$ 155,60 |
| 10% | R$ 168,33 |
| 20% | R$ 181,06 |
| 30% | R$ 193,80 |
| **50%** | **R$ 219,27** |

Confrontando com os preços de referência disponíveis:

| Referência de preço | Valor | Razão sobre P_neutralidade |
|---|---|---|
| TC de tórax + contraste (SIGTAP) | R$ 196,41 | 1,26× |
| Microcusteio SUS 2022 (valores 2020) | R$ 452,05 | 2,91× |
| CBHPM / saúde suplementar 2026 | R$ 1.311,95 | 8,43× |

Impacto incremental anual, por cenário de substituição:

| Preço adotado | 25% da demanda funcional | 50% da demanda funcional |
|---|---|---|
| Microcusteio 2022 (R$ 452,05) | +R$ 69,6 mi/ano | +R$ 139,2 mi/ano |
| CBHPM 2026 (R$ 1.311,95) | +R$ 271,5 mi/ano | +R$ 543,0 mi/ano |

**Observação metodológica relevante.** O preço de neutralidade é uma grandeza **por exame** e, sob substituição 1:1, **independe do tamanho da população elegível**. Esse resultado contorna precisamente a incerteza que motivou parte da recomendação preliminar: não é necessário resolver a magnitude da população elegível para concluir que, a qualquer preço acima de R$ 155,60–219,27, a estratégia é orçamentariamente expansiva, e não neutra. A população elegível determina *quanto* se gasta a mais, não *se* se gasta a mais.

---

## 5. Síntese

1. A capacidade instalada deve ser tratada como **banda [216 – 2.534 estabelecimentos]**, com definições declaradas, e não como número pontual. A rede invasiva efetivamente ativa (290 serviços) converge com o limite inferior.
2. **O CNES não discrimina canais.** Estimativas de aptidão técnica exigem proxy declarada ou coleta primária. Recomenda-se o desdobramento do cadastro por faixa de canais.
3. A distribuição é **fortemente desigual (6,1×)**, e as UFs de maior parque instalado têm as menores proporções de disponibilidade ao SUS. **AC, AM e RR não têm nenhum serviço com tomógrafo-SUS e hemodinâmica co-localizados.**
4. O comparador efetivo no SUS é o **teste ergométrico (63,7% da investigação funcional, R$ 32,20)**, não a cintilografia miocárdica.
5. A etapa diagnóstica representa **14,8%** do gasto da via da DAC. A economia projetada depende de reduzir os 85,2% restantes, para os quais a metanálise do parecerista não encontrou diferença em desfechos duros.
6. O **preço de neutralidade orçamentária é R$ 155,60** (R$ 219,27 no cenário mais favorável testado), abaixo de todas as referências de preço disponíveis. Este resultado **independe da população elegível**.

Nada nesta contribuição se pronuncia sobre o mérito clínico da tecnologia. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária, nos termos em que o Comitê solicitou esclarecimento.

---

## Apêndice A — Reprodutibilidade

| Fonte | Endereço | Competência |
|---|---|---|
| CNES — equipamentos | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ/` | 06/2026 |
| CNES — tabelas de código | `.../CNES/200508_/Auxiliar/TAB_CNES.zip` | 07/2026 |
| SIA/SUS — produção ambulatorial | `.../SIASUS/200801_/Dados/` | 01–12/2025 |
| SIH/SUS — internações | `.../SIHSUS/200801_/Dados/` | 01–12/2025 |
| SIGTAP | `ftp://ftp2.datasus.gov.br/public/sistemas/tup/downloads/` | 08/2026 |
| População | IBGE, agregado 6579, variável 9324 | 2025 |

**Nota de processamento.** Arquivos SIA de MG, RJ, RS e SP são particionados (`PASP2501a.dbc`, `…b`, `…c`, `…d`). Rotinas que constroem nomes de arquivo sem sufixo de partição perdem silenciosamente 71 dos 395 arquivos do ano — correspondentes às quatro UFs mais populosas. O código utilizado enumera o diretório remoto, verifica presença de todas as 27 UFs e distingue falha de download de arquivo vazio. Total processado: **395/395 arquivos SIA e 324/324 arquivos SIH, sem perdas**.

Leitura de `.dbc`: bibliotecas `datasus-dbc` e `dbfread` (Python).
Scripts e tabelas intermediárias: [inserir DOI/URL do repositório antes de submeter].

---

**Autor:** [nome, titulação, afiliação, ORCID]
**Conflitos de interesse:** [declarar]
**Data:** agosto de 2026
