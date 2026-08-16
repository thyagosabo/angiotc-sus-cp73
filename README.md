# AngioTC coronariana no SUS — capacidade instalada e impacto orçamentário

Análise nacional reprodutível da **capacidade tomográfica do SUS** e do **preço de neutralidade orçamentária** da angiotomografia coronariana (AngioTC), construída exclusivamente sobre bases públicas.

Produzida como contribuição técnico-científica à **Consulta Pública nº 73/2026 da Conitec**, que trata da incorporação da AngioTC como exame de primeira linha para pacientes sintomáticos com probabilidade pré-teste baixa ou intermediária e suspeita de DAC estável.

Contexto: em 3 de julho de 2026 (153ª Reunião Ordinária), o Comitê de Produtos e Procedimentos deliberou por **recomendação preliminar desfavorável**, fundamentada em incertezas quanto à avaliação econômica, ao impacto orçamentário, à capacidade de implementação e à delimitação da população elegível. O relatório preliminar não cita o CNES em nenhum ponto.

---

## Resultado principal

> **Preço de neutralidade orçamentária da AngioTC no SUS: R$ 155,60**
> (R$ 219,27 mesmo assumindo eliminação de 50% dos cateterismos)

Sob substituição 1:1 e comportamento downstream constante, esse preço é uma grandeza **por exame** e **independe do tamanho da população elegível** — contornando a incerteza que motivou parte da recomendação preliminar.

Todas as referências de preço disponíveis ficam acima:

| Referência | Valor | Razão |
|---|---|---|
| TC de tórax + contraste (SIGTAP) | R$ 196,41 | 1,26× |
| Microcusteio SUS 2022 (valores 2020) | R$ 452,05 | 2,91× |
| CBHPM / saúde suplementar 2026 | R$ 1.311,95 | 8,43× |

### Achados de suporte

- **O comparador efetivo é o teste ergométrico**, não a cintilografia: 598.695 exames em 2025, 63,7% de toda a investigação funcional não invasiva, a R$ 32,20 médios.
- **A etapa diagnóstica é 14,8%** do gasto da via da DAC (R$ 1,80 bi/ano). A economia projetada depende de reduzir os 85,2% restantes — angioplastia e revascularização —, para os quais a metanálise do parecerista não encontrou diferença em desfechos duros.
- **Capacidade instalada é uma banda, não um número: [216 – 2.534 estabelecimentos].** O limite inferior (tomógrafo + hemodinâmica co-localizados) converge com a rede invasiva efetivamente ativa em 2025 (290 serviços).
- **AC, AM e RR** não possuem nenhum estabelecimento com tomógrafo-SUS e hemodinâmica co-localizados. Roraima não registrou nenhum procedimento coronariano invasivo em 2025.

---

## Duas limitações que definem o método

**1. O CNES não discrimina canais de tomógrafo.** Existe um único código (`TIPEQUIP=01`, `CODEQUIP=11`), sem desdobramento por cortes por rotação. Não é possível estimar de fonte pública quantos equipamentos atendem à especificação de ≥64 canais adotada pelas diretrizes. Daí a análise entregar uma banda com dois limites declarados em vez de uma estimativa pontual.

**2. Não existe código SIGTAP para AngioTC.** Verificado nos 5.023 procedimentos da competência 08/2026. A produção atual do exame é administrativamente invisível, e nenhum custo unitário pode ser ancorado em série histórica do SUS.

Adicionalmente, o código `0206030045 — CONTRASTE PARA TOMOGRAFIA COMPUTADORIZADA` **não registra faturamento no SIA em 2025**, o que o inviabiliza como marcador de serviços com capacidade para exames contrastados. O proxy adotado em seu lugar é a co-localização com sala de hemodinâmica (`CODEQUIP=10`).

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

Os arquivos CNES (`cnes/EQ*.dbc`, competência 06/2026) e a tabela SIGTAP (`sigtap/`, competência 08/2026) estão versionados para fixar as competências usadas. Para atualizá-los, ver endereços na tabela de fontes abaixo.

### Armadilha de particionamento

Arquivos SIA de **MG, RJ, RS e SP são particionados** (`PASP2501a.dbc`, `…b`, `…c`, `…d`). Rotinas que constroem nomes de arquivo sem sufixo perdem silenciosamente **71 dos 395 arquivos** do ano — exatamente as quatro UFs mais populosas, sem emitir erro.

`extrai_dac.py` enumera o diretório remoto em vez de construir nomes, verifica presença das 27 UFs, e distingue falha de download de arquivo vazio. Execução de referência: **395/395 arquivos SIA e 324/324 SIH, sem perdas.**

---

## Estrutura

```
extrai_dac.py            extração SIA/SIH por estabelecimento (streaming, pico de disco = 1 arquivo)
analise_final.py         demanda × banda de capacidade → 4 CSVs + resumo
contribuicao-cp73.md     documento submetido à consulta pública
cnes/                    CNES equipamentos, .dbc, competência 06/2026
sigtap/                  tabela de procedimentos, competência 08/2026
data/                    intermediários agregados por CNES × procedimento
output/                  tabelas finais
```

`analise_final.py` declara a cobertura no cabeçalho e marca `PARCIAL — NÃO EXTRAPOLAR` quando faltam UFs ou competências.

## Fontes

| Base | Endereço | Competência |
|---|---|---|
| CNES — equipamentos | `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ/` | 06/2026 |
| CNES — tabelas de código | `.../CNES/200508_/Auxiliar/TAB_CNES.zip` | 07/2026 |
| SIA/SUS | `.../SIASUS/200801_/Dados/` | 01–12/2025 |
| SIH/SUS | `.../SIHSUS/200801_/Dados/` | 01–12/2025 |
| SIGTAP | `ftp://ftp2.datasus.gov.br/public/sistemas/tup/downloads/` | 08/2026 |
| População | IBGE, agregado 6579, variável 9324 | 2025 |

Não há API REST para essas bases; o acesso é por FTP com arquivos `.dbc` (DBF comprimido), lidos com `datasus-dbc` + `dbfread`.

## Escopo

Esta análise **não se pronuncia sobre o mérito clínico** da angiotomografia coronariana. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária, nos termos em que o Comitê solicitou esclarecimento.

## Licença

[definir — sugestão: CC BY 4.0 para textos e dados, MIT para código]
