# AngioTC coronariana no SUS — capacidade instalada e impacto orçamentário

Análise nacional reprodutível da **capacidade tomográfica do SUS** e do **preço admissível** da angiotomografia coronariana (AngioTC), construída exclusivamente sobre bases públicas.

Produzida como contribuição técnico-científica à **Consulta Pública nº 73/2026 da Conitec**, que trata da incorporação da AngioTC como exame de primeira linha para pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de DAC estável.

Contexto: em 3 de julho de 2026 (153ª Reunião Ordinária), o Comitê de Produtos e Procedimentos deliberou por **recomendação preliminar desfavorável**, fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à capacidade de implementação e à delimitação da população elegível.

---

## Resultados principais

### Capacidade: o cadastro já responde, mas está incompleto

A **Portaria SAES/MS nº 3.695, de 15/01/2026** desmembrou o código genérico de tomógrafo em categorias por canais (26=4, 27=16, 28=32, 29=64, 30=128). Em 06/2026, disponíveis ao SUS e em uso:

| Camada | Estabelecimentos | Equipamentos |
|---|---|---|
| **Compatível confirmado (≥64 canais)** | **315** | **432** |
| Incompatível confirmado (<64 canais) | 672 | 736 |
| Especificação não declarada (código 11) | 2.534 | 2.785 |
| **Parque total SUS** | **3.395** | **3.953** |

**A reclassificação está 26,8% concluída.** Os 432 são piso de capacidade documentada, não estimativa da capacidade real. A portaria dá prazo de três competências — se ele se encerrar antes da apreciação final, a Conitec terá o inventário nacional completo pela primeira vez.

**Estrato de prontidão:** 83 estabelecimentos reúnem ≥64 canais, hemodinâmica co-localizada e produção coronariana documentada em 2025. **Doze UFs têm zero.** AP, PI e TO não têm nenhum tomógrafo ≥64 canais disponível ao SUS.

### Preço admissível: análise de limiar

O SIA não tem identificador de paciente. Razões entre contagens agregadas não são probabilidades condicionais, então o modelo **não estima** quantas angiografias a AngioTC evitaria. Responde à pergunta inversa:

```
Δ_CATE necessário = (P_angioTC − R$ 185,46) × 100 / R$ 730,14
```

| Referência | Valor | Δ CATE/100 necessário |
|---|---|---|
| TC de tórax + contraste (SIGTAP) | R$ 196,41 | 1,5 |
| Microcusteio SUS 2022 (valores 2020) | R$ 452,05 | 36,5 |
| **Microcusteio corrigido a jul/2026** (IPCA +37,7%) | **R$ 622,54** | **59,9** |
| CBHPM 2026 — saúde suplementar | R$ 1.311,95 | 154,3 — **impossível** |

Ao preço da saúde suplementar seria preciso evitar mais angiografias do que pacientes investigados. Impossível sob qualquer premissa, qualquer base de custo, qualquer população elegível.

O preço de neutralidade é grandeza **por episódio** e, sob substituição 1:1, **independe do tamanho da população elegível** — contornando a incerteza que motivou parte da recomendação preliminar.

### Unidade de análise: episódio, não procedimento

A cintilografia de perfusão tem dois códigos, estresse e repouso. Em 2025: 151.784 e 151.225 — **151.225 pares e 559 órfãos**. São duas etapas do mesmo exame.

Validação externa: o estudo de custo-efetividade no SUS de 2022 (Arq Bras Cardiol) precificou a cintilografia como unidade única em R$ 791,59 (valores 2020); a soma dos dois códigos SIA 2025 é R$ 788,24 — diferença de 0,4%.

Contar procedimentos infla o denominador em 19%: 939.179 procedimentos contra **787.954 episódios**, e o custo médio sobe de R$ 155,60 para **R$ 185,46**.

---

## Duas armadilhas dos dados

**1. As tabelas de conversão do CNES estão defasadas.** Os arquivos `.cnv` em `TAB_CNES.zip` (competência 07/2026) listam apenas `0111 — Tomógrafo Computadorizado` e não refletem a Portaria 3.695/2026, embora os códigos 26–30 já estejam nos microdados. **Derivar a lista de códigos dessas tabelas exclui silenciosamente todo equipamento já reclassificado.** Enumere os valores presentes nos dados.

**2. Arquivos SIA de MG, RJ, RS e SP são particionados** (`PASP2501a.dbc`, `…b`, `…c`, `…d`). Construir nomes de arquivo sem sufixo perde **71 dos 395 arquivos** do ano — as quatro UFs mais populosas — sem emitir erro. `extrai_dac.py` enumera o diretório remoto, verifica presença das 27 UFs e distingue falha de download de arquivo vazio.

Ambas produzem resultados plausíveis e errados, em silêncio. A primeira custou uma versão inteira deste trabalho.

---

## Reprodução

```bash
pip install -r requirements.txt
```

```bash
python3 extrai_dac.py SIH 2025
```

```bash
python3 extrai_dac.py SIA 2025
```

```bash
python3 analise_final.py
```

`extrai_dac.py` aceita subconjunto de UFs e sufixo de saída, para paralelizar:

```bash
python3 extrai_dac.py SIA 2025 SP g1
```

Os arquivos CNES (`cnes/EQ*.dbc`, 06/2026) e a tabela SIGTAP (`sigtap/`, 08/2026) estão versionados para fixar as competências.

## Estrutura

```
extrai_dac.py            extração SIA/SIH por estabelecimento (streaming, pico de disco = 1 arquivo)
analise_final.py         demanda × capacidade → CSVs + resumo
contribuicao-cp73.md     documento da consulta pública
preview-angiotc.html     prévia (CSS de impressão + painéis mobile)
angiotc-preview.pdf      PDF renderizado da prévia
cnes/                    CNES equipamentos, .dbc, 06/2026
sigtap/                  tabela de procedimentos, 08/2026
data/                    intermediários v1 (comparadores + 0206)
data-v2/                 intermediários v2 (+ OCI 0902)
REGRAS-DE-ANALISE.md     regras fixadas antes de olhar o dado
output/                  tabelas finais
```

`analise_final.py` declara a cobertura no cabeçalho e marca `PARCIAL — NÃO EXTRAPOLAR` quando faltam UFs ou competências.

## Fontes

| Base | Endereço | Competência |
|---|---|---|
| CNES — equipamentos | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ/` | 06/2026 |
| SIA/SUS | `.../SIASUS/200801_/Dados/` | 01–12/2025 |
| SIH/SUS | `.../SIHSUS/200801_/Dados/` | 01–12/2025 |
| SIGTAP | `ftp://ftp2.datasus.gov.br/public/sistemas/tup/downloads/` | 08/2026 |
| População | IBGE, agregado 6579, variável 9324 | 2025 |
| IPCA | IBGE, agregado 1737, variável 2266 | 12/2020 → 07/2026 |
| Portaria SAES/MS nº 3.695 | Diário Oficial da União | 15/01/2026 |

Não há API REST para essas bases; o acesso é por FTP com arquivos `.dbc` (DBF comprimido), lidos com `datasus-dbc` + `dbfread`.

### Onde a tecnologia gera valor: a posição no percurso

O Δ de cateterismo foi ancorado em 12 ensaios randomizados, **cateterismo total por braço** (o procedimento que o SUS paga), cada um lido contra a equação do seu próprio desenho — porque no gatekeeping o custo da investigação prévia é comum aos braços e cancela:

| PICO | Equação | Δ observado /100 | Preço de neutralidade |
|---|---|---|---|
| Primeira linha (8 ensaios) | P = 185,46 + (Δ/100)·730,14 | −6,4 a +4,1 | **R$ 139 – 215** |
| Gatekeeping (4 ensaios) | P = (Δ/100)·730,14 | 66,0 a 85,6 | **R$ 482 – 625** |

No melhor caso de primeira linha resta lacuna de R$ 407 por paciente até o microcusteio corrigido. No melhor caso de gatekeeping, o CAD-MAN cruza a neutralidade por R$ 2,67. **A análise não demonstra que gatekeeping economiza; demonstra que o posicionamento muda radicalmente a plausibilidade de a tecnologia se pagar** — e o PICO em apreciação é o de primeira linha.

Cateterismo sem DAC obstrutiva (IQWiG D22-01, Tabela 43) é reportado separadamente como eficiência diagnóstica, fora do cálculo econômico.

### OCI de síndrome coronariana crônica: o cenário mais favorável testado

As OCI `0902010034/42/50` definem o episódio de SCC na própria tabela do SUS. Produção 2025: **7.616 episódios, 0,96% do total**, em 148 estabelecimentos. Componentes com valor zerado dentro de OCI não são somados (regra fixada antes da extração em `REGRAS-DE-ANALISE.md`). Ponderar o intercepto com OCI desloca a reta de primeira linha em +R$ 2,02; nenhuma conclusão muda.

## Pendências

- Microcusteio contemporâneo próprio.
- Preço de aquisição pública em licitação como quarta categoria de benchmark.
- Auditoria final exclusivamente de unidades de análise e dupla contagem (em curso).

## Escopo

Esta análise **não se pronuncia sobre o mérito clínico** da angiotomografia coronariana. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária, nos termos em que o Comitê solicitou esclarecimento.

## Licença

[definir — sugestão: CC BY 4.0 para textos e dados, MIT para código]
