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

**Estrato de prontidão:** 79 estabelecimentos reúnem ≥64 canais, hemodinâmica co-localizada e produção coronariana documentada em 2025. **Doze UFs têm zero.** AP, PI e TO não têm nenhum tomógrafo ≥64 canais disponível ao SUS.

### Preço admissível: análise de limiar — e três parâmetros que os registros não identificam

O SIA não tem identificador de paciente. Razões entre contagens agregadas não são probabilidades condicionais, então o modelo **não estima** quantas angiografias a AngioTC evitaria. Responde à pergunta inversa: quantas seria preciso evitar, por 100 pacientes, para neutralidade a cada preço.

```
P_neutralidade = C_substituído + (Δ_CATE/100) × R$ 730,14 − (Δ_revasc/100) × C_revasc
```

Nos ensaios com comparador não invasivo, o Δ de cateterismo total foi de **−6,3 a +4,1 por 100**. Aplicando a cada cenário de exame substituído:

| Estrato de PPT | Exame substituído (premissa) | C | Só exames + cateterismo | Com revascularização observada (PRECISE / Foy) |
|---|---|---|---|---|
| Baixa | **nenhum — adoção aditiva (sem protocolo)** | R$ 0 | **R$ −46 – +30** (SCOT-HEART: −3 – +4) | R$ −122 – −41 (revasc. do próprio SCOT-HEART) |
| Baixa | teste ergométrico | R$ 32,20 | R$ −14 – +62 | R$ −297 – −195 |
| Não estratificado (PICO submetido) | mix médio do SIA (76% ergometria) | R$ 185,46 | R$ 139 – 215 | R$ −144 – −42 |
| Intermediária | eco de estresse | R$ 196,39 | R$ 150 – 226 | R$ −133 – −31 |
| Intermediária | mix do NATS por episódio (dois códigos, valores SIA) | R$ 523,81 | R$ 477 – 554 | R$ 195 – 297 |
| Intermediária | cintilografia | R$ 786,83 | R$ 741 – 817 | **R$ 458 – 560** |

(Mix do NATS como publicado, cintilografia só pelo código de estresse, R$ 316,76: R$ 270 – 347 só com exames.)

O preço proposto pelo demandante é **R$ 550,00**. **Sem protocolo de posicionamento — a AngioTC somada ao percurso atual, o cenário de referência se a incorporação criar o código sem dizer o que sai do percurso — nenhum preço plausível é neutro (teto R$ 30).** Na probabilidade baixa (comparador: nenhum exame ou ergometria) R$ 550 está fora do alcance; na intermediária, dentro da zona de incerteza **apenas quando substitui cintilografia**. Estratificar não é sensibilidade: é o resultado — a média não estratificada é puxada para o estrato baixo porque três quartos do volume atual são ergometria.

A revascularização não pode ficar fora: o SIH dá R$ 7.713/angioplastia e R$ 25.904/CRM. PRECISE aumenta revasc em +4,0/100 (−R$ 359/paciente); DISCHARGE e CONSERVE, no gatekeeping, reduzem em −3,8 e −5,0/100 (+R$ 293 e +R$ 386) — o que leva o DISCHARGE de R$ 548 a **R$ 841** e o CONSERVE de R$ 482 a **R$ 868**.

**A Diretriz SBC de Síndrome Coronariana Crônica 2025** (Arq Bras Cardiol 2025;122(9)) estratifica: AngioTC como primeira opção é **IIb-B na probabilidade baixa** e **I-A na intermediária**, e o algoritmo a coloca como *alternativa* à prova funcional ("prova funcional ou angiotomografia"). O PICO submetido trata "baixa ou intermediária" como faixa única. Alinhar a incorporação à estratificação da própria diretriz é o instrumento que a evidência sustenta.

### Onde a tecnologia gera valor: a posição no percurso

O Δ de cateterismo foi ancorado em 10 ensaios randomizados e uma metanálise (12 estudos com CATCH e CARE-CCTA, que só entram na eficiência diagnóstica), **cateterismo total por braço** (o procedimento que o SUS paga), cada um lido contra a equação do seu próprio desenho — porque no gatekeeping o custo da investigação prévia é comum aos braços e cancela:

| PICO | Equação | Δ observado /100 | Preço de neutralidade |
|---|---|---|---|
| Primeira linha (6 ensaios + metanálise de Foy; SCOT-HEART à parte, aditivo) | P = C_subst + (Δ/100)·730,14 | −6,3 a +4,1 | **R$ 139 – 215** (mix médio) a **R$ 741 – 817** (cintilografia) |
| Gatekeeping (4 ensaios) | P = (Δ/100)·730,14 | 66,0 a 85,6 | **R$ 482 – 625** (R$ 841–868 com revasc., DISCHARGE e CONSERVE) |

Substituindo o mix médio, no melhor caso de primeira linha resta lacuna de R$ 407 por paciente até o microcusteio corrigido. No melhor caso de gatekeeping, o CAD-MAN cruza por R$ 2,67. O SCOT-HEART, de desenho aditivo, não substitui episódio: é o cenário "adoção aditiva" (R$ −3 a +4 com o seu próprio Δ, 409 vs 401 cateterismos em 20 meses e 491 vs 502 em 5 anos; R$ −46 a +30 com o envelope de primeira linha; R$ −122 a −41 com a sua própria revascularização). **A análise não demonstra que gatekeeping economiza; demonstra que o posicionamento muda radicalmente a plausibilidade de a tecnologia se pagar** — e o PICO em apreciação é o de primeira linha.

Cateterismo sem DAC obstrutiva (IQWiG D22-01, Tabela 43) é reportado separadamente como eficiência diagnóstica, fora do cálculo econômico.

### OCI de síndrome coronariana crônica: o cenário mais favorável testado

As OCI `0902010034/42/50` definem o episódio de SCC na própria tabela do SUS. Produção 2025: **7.616 episódios, 0,96% do total**, em 148 estabelecimentos. Componentes com valor zerado dentro de OCI não são somados (regra fixada antes da extração em `REGRAS-DE-ANALISE.md`). Ponderar o intercepto com OCI desloca a reta de primeira linha em +R$ 2,02; nenhuma conclusão muda.

## Documentos

- `contribuicao-cp73.md` — contribuição à CP 73/2026 (v6, 18/08/2026: corpo condensado e reescrito pelos autores; apêndices e referências inalterados), a peça a anexar (PDF).
- `gera_figuras.py` → `figuras/` — Figura central, Figuras 1–2 e Figura S1 (PNG 300 dpi + PDF), geradas a partir de `output/`; embutidas nos PDFs dos manuscritos.
- `manuscrito-abc.md` — manuscrito no formato da Arq Bras Cardiol (artigo original; corpo ≤ 5.000 palavras contando tudo; v1.3, redação revista pelos autores em 18/08/2026), com `manuscrito-suplemento.md` (Tabelas S1–S8, Figura S1, Textos S1–S2). `manuscrito-v0.md` — versão integral de trabalho (v1.2, arquivo do argumento completo; a prosa vigente é a de `manuscrito-abc.md`).
- `SUBMISSAO-CP73.md` — roteiro do formulário; `REGRAS-DE-ANALISE.md` — regras pré-registradas e emendas.
- `preview-angiotc.html` / `angiotc-preview.pdf` — prévia de leitura da **v3**, superada; mantida por histórico, não anexar.

## Pendências

- Microcusteio contemporâneo próprio (desenho mínimo em `manuscrito-v0.md`, 4.6).
- Preço de aquisição pública em licitação como quarta categoria de benchmark.
- Auditoria final exclusivamente de unidades de análise e dupla contagem (em curso).

## Escopo

Esta análise **não se pronuncia sobre o mérito clínico** da angiotomografia coronariana. As conclusões dizem respeito exclusivamente a capacidade de implementação e sustentabilidade orçamentária, nos termos em que o Comitê solicitou esclarecimento.

## Licença

Texto, tabelas e dados derivados: **CC BY 4.0**. Código: **MIT** (`LICENSE-CODE`). Ver `LICENSE`.
