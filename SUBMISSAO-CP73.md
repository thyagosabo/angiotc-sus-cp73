# Submissão à CP 73/2026 — roteiro do formulário

> **SUBMETIDO em 24/08/2026** (último dia). Confirmação do sistema: "Formulário respondido
> corretamente" / "Respostas enviadas". Página das respostas (requer login gov.br):
> https://brasilparticipativo.presidencia.gov.br/processes/consultas-publicas-conitec/f/5217/surveys/1156
> Contador da CP no momento do envio: 1.893 respostas. Anexo único: `contribuicao-cp73.pdf` (407,98 KB, v6.2).
>
> **Diferenças em relação ao roteiro abaixo, descobertas no formulário real:**
> - O campo 12 tem limite de **2.000 caracteres** (o roteiro previa ~5.000). Foi submetida a
>   versão condensada de 1.966 caracteres registrada em `campo12-colar.txt` (seção nova abaixo).
> - O formulário real tem 27 campos, não 19: perguntas 21/23 ("contribuição técnica sobre
>   evidências clínicas / estudos econômicos?") abrem os campos dissertativos 22/24 (2.000
>   caracteres cada), que foram preenchidos (textos abaixo). Perguntas 13/17 sobre experiência
>   pessoal foram respondidas pelo autor.
> - Campos 26/27 + Termos de Serviço: 5 caixas de declaração marcadas.

> **Errata pós-submissão (24/08, conferência bibliográfica):** iniciais de autores corrigidas nas
> refs 3 (Carmo PBD; Magliano CADS) e 20 (Costa IBSDS; Silva MTD) da contribuição no repositório.
> Nada muda em números ou conclusões; o PDF submetido é o registro do que foi enviado.

## Textos efetivamente submetidos (24/08/2026)

### Campo 12 (1.966/2.000 caracteres)

```
Favorável à incorporação condicionada a protocolo de posicionamento por probabilidade pré-teste (Diretriz SBC de Síndrome Coronariana Crônica 2025) que diga qual exame a angiotomografia substitui, e à avaliação em separado do uso como filtro antes do cateterismo já indicado. Sem essa especificação, na formulação agregada "baixa ou intermediária", a análise anexa mostra que a tecnologia é orçamentariamente expansiva a qualquer preço plausível.

Análise nacional reprodutível, anexa, sobre bases públicas (CNES, SIA/SUS, SIH/SUS, SIGTAP, IBGE). Síntese:

1. CAPACIDADE. Após a Portaria SAES/MS 3.695/2026, o CNES registra 432 tomógrafos de 64 canais ou mais em 315 estabelecimentos (06/2026). É um piso: 74,6% dos estabelecimentos seguem no código genérico. Só 79 reúnem hardware compatível, hemodinâmica e produção coronariana; 12 UFs não têm nenhum nessa condição.

2. LIMIAR. O SIA não tem identificador de paciente; em vez de estimar cateterismos evitados, calculou-se o necessário, por 100 pacientes, para neutralidade a cada preço. Nos ensaios de primeira linha, a variação foi de -6,3 a +4,1 por 100. Substituindo o mix real do SUS (76% ergometria; R$ 185 por episódio), a neutralidade é R$ 139-215; substituindo a cintilografia (R$ 787), R$ 741-817, caindo a R$ 458-560 com a revascularização induzida. Somada ao percurso sem substituir nada (cenário provável sem protocolo), nenhum preço plausível é neutro (teto R$ 30). O preço proposto (R$ 550) só entra na zona de incerteza na intermediária, substituindo cintilografia.

3. OUTRO PICO. Em pacientes já indicados a cateterismo (CAD-MAN, CONSERVE, DISCHARGE, Reis 2022), a neutralidade é R$ 482-625, subindo a R$ 841-868 com a revascularização evitada. Recomenda-se avaliá-lo como pergunta separada.

A evidência econômica não sustenta decisão uniforme para toda a faixa; sustenta condicionar a incorporação ao posicionamento e ao exame substituído. Código e dados: github.com/thyagosabo/angiotc-sus-cp73
```

### Campo 22 — evidências clínicas (1.673/2.000)

```
Evidências clínicas (fontes: PMID). Ensaios randomizados de estratégia com comparador não invasivo mostram variação de cateterismo total entre -6,3 e +4,1 por 100 pacientes: PROMISE (25773919) 12,2% vs 8,1%; PRECISE (37610731) 12,8% vs 16,9%; CAPP (25473041); CRESCENT-I/II (26746631, 29248657); metanálise de Foy (28973101) 11,7% vs 9,1%. No desenho aditivo, SCOT-HEART (27081014, 30145934): 409 vs 401 cateterismos aos 20 meses e 491 vs 502 em 5 anos, com redução de morte coronariana e infarto em 5 e 10 anos (39863372), benefício clínico distinto da questão orçamentária. Nos ensaios com cateterismo já indicado (CAD-MAN 27777234; CONSERVE 30553687; DISCHARGE 35240010; Reis 35226221), a angiotomografia evita 66 a 86 cateterismos por 100. Eficiência diagnóstica (IQWiG D22-01, NBK602895): 0,9 a 5,9 cateterismos sem doença obstrutiva evitados por 100 contra métodos funcionais (OR 0,77; IC95% 0,64-0,94) e 53,7 a 81,0 contra cateterismo direto, direção favorável à angiotomografia nos dois PICOs. Revascularização: PRECISE 9,2% vs 5,2%; Foy 7,2% vs 4,5%; DISCHARGE 14,2% vs 18,0%; CONSERVE 13% vs 18%. Ressalvas: horizontes heterogêneos (90 dias a 18 meses); PRECISE inclui diferimento em 20% dos de menor risco; Foy tem 9 de 13 ensaios de emergência. A Diretriz SBC de Síndrome Coronariana Crônica 2025 (DOI 10.36660/abc.20250619) estratifica a indicação: IIb-B na probabilidade baixa, I-A na intermediária como alternativa à prova funcional, condicionada a capacidade funcional, ECG basal, acesso e função renal. ESC 2024 e AHA/ACC 2021 convergem com essa estratificação. Detalhamento por ensaio no PDF anexo (Apêndice B) e em github.com/thyagosabo/angiotc-sus-cp73.
```

### Campo 24 — estudos econômicos (1.678/2.000)

```
Estudos econômicos. 1) Análise de limiar anexa (bases públicas SIA/SIH/SIGTAP/CNES 2025-2026): preço de neutralidade da angiotomografia por exame substituído e posição no percurso: mix real do SUS R$ 139-215; cintilografia R$ 741-817 (R$ 458-560 com revascularização); adoção aditiva, teto R$ 30; filtro pré-cateterismo R$ 482-625 (R$ 841-868 com revascularização). O preço proposto (R$ 550) só entra na zona de incerteza na intermediária substituindo cintilografia. 2) Análises econômicas de ensaios: PROMISE não encontrou economia (PMID 26857050); SCOT-HEART custou +US$ 462 por paciente aos 6 meses; PRECISE reduziu o custo diagnóstico em 27% e aumentou o de revascularização em 67% (PMID 39895495). 3) Brasil: Carmo 2022 (PMID 35137778) microcusteou a angiotomografia (R$ 452,05) contra comparadores a preços de tabela, assimetria que persiste; Bertoldi 2016/2017 modelam custo-efetividade de longo prazo, pergunta distinta. 4) Shiozaki 2025 (DOI 10.36660/abc.20250204), saúde suplementar: compara a angiotomografia (R$ 1.311,95) apenas com a angiografia invasiva (R$ 1.900,79); é um modelo do filtro pré-cateterismo, não da primeira linha em apreciação; transposto ao SUS, sustenta o filtro, não o PICO submetido. 5) Recomendações: criar código SIGTAP com protocolo que especifique o exame substituído; microcusteio bottom-up da angiotomografia e dos comparadores no mesmo serviço, conforme a diretriz metodológica do Ministério da Saúde, em ao menos 8 serviços; avaliar o filtro pré-cateterismo como pergunta separada; completar a reclassificação do CNES antes da apreciação final. Método reproduzível, código e tabelas: PDF anexo e github.com/thyagosabo/angiotc-sus-cp73.
```

---


Formulário no Brasil Participativo (Decidim). **Exige login gov.br.** Sessão expira em
**30 minutos** após o login — preparar tudo antes de entrar. Prazo: **24/08/2026**.
446 respostas registradas até 16/08.

URL: https://brasilparticipativo.presidencia.gov.br/processes/consultas-publicas-conitec/f/5217/

## Regras de anexo (verificadas)

- Até **dois arquivos** por contribuição.
- **Sem dados pessoais nem imagens que identifiquem pessoas; sem assinaturas.**
- Material de terceiros sem autorização (artigos) é desconsiderado — anexar só o que é seu.
- Formato/tamanho exatos só aparecem no campo depois do login. Preparar **PDF**.

## Campos — o que preencher

| # | Campo | Tipo | Resposta |
|---|---|---|---|
| 1 | Nome completo | curta | *(você)* |
| 2 | Data de nascimento | curta | *(você)* |
| 3 | Identidade de gênero | escolha | *(você)* |
| 4 | Cor/etnia | escolha | *(você)* |
| 5 | Região | escolha | *(você)* |
| 6 | Estado | escolha | *(você)* |
| 7 | Município | curta | *(você)* |
| 8 | Como ficou sabendo | escolha | Site da Conitec |
| 9 | Deseja contribuir como? | escolha | **Profissional de saúde** |
| 10 | CNPJ/razão social (se PJ) | parágrafo | *deixar em branco — pessoa física* |
| 11 | **Opinião sobre a incorporação** | escolha | **"Eu acho que deve ser incorporada"** (decidido em 17/08) — o campo 12 abre com a condição |
| 12 | **Comente sobre a sua opinião** | parágrafo | texto pronto abaixo |
| 13 | Experiência com a tecnologia? | Sim/Não | *(você)* |
| 14 | Experiência com outra tecnologia? | Sim/Não | *(você)* |
| 15 | Contribuição técnica — evidências clínicas? | Sim/Não | **Sim** |
| 16 | Contribuição técnica — estudos econômicos? | Sim/Não | **Sim** |
| 17 | Anexo | arquivo | `contribuicao-cp73.pdf` (só ele — a prévia HTML/PDF é v3, superada; não anexar). O anexo não traz nomes; se o coautor entrar, dizer no campo 12 "elaborada com [coautor]" |
| 18 | Declaração de responsabilidade | caixa | marcar |
| 19 | Termos de serviço | caixa | marcar |

## Campo 11 — decidido: "Eu acho que deve ser incorporada" (17/08/2026)

As três opções são: *Não acho que deve ser incorporada* / *Eu acho que deve ser
incorporada* / *Não tenho opinião formada*.

Nenhuma delas cabe no achado sem ressalva. O documento não diz "não incorpore"; diz que o
PICO submetido (primeira linha) não sustenta neutralidade e que existe outro PICO onde a
conta quase fecha. Duas leituras:

- **Minha (16/08):** "Não tenho opinião formada", com o campo 12 explicando que a resposta é
  condicional ao posicionamento.
- **Do parecer no papel de coautor (17/08):** marcar **"Eu acho que deve ser incorporada"** e
  abrir o campo 12 com a condição — é o que a análise diz ("não recusar a tecnologia"); "não
  tenho opinião" vira ruído na tabulação da Conitec; "não deve" é como a SBC lerá a
  contribuição inteira, e não é o que ela diz. Se marcar "sem opinião", é defensável; "não
  deve" ele não marcaria.

**Decisão do autor (17/08): "deve ser incorporada".** O campo 12 abaixo já começa com a
condição (primeira linha):

> Favorável à incorporação condicionada a protocolo de posicionamento por probabilidade
> pré-teste (Diretriz SBC de Síndrome Coronariana Crônica 2025) que especifique o exame
> substituído, e à avaliação em separado do filtro pré-cateterismo; desfavorável à
> incorporação na formulação agregada "baixa ou intermediária" sem essa especificação, que a
> análise anexa mostra ser orçamentariamente expansiva a qualquer preço plausível.

## Campo 12 — texto pronto (colar)

Opinião: favorável à incorporação, desde que condicionada a um protocolo de posicionamento
por probabilidade pré-teste (Diretriz SBC de Síndrome Coronariana Crônica 2025) que diga
qual exame a angiotomografia substitui, e desde que o uso como filtro antes do cateterismo
já indicado seja avaliado como pergunta separada. Sem essa especificação, na formulação
agregada "baixa ou intermediária", a análise anexa mostra que a tecnologia é
orçamentariamente expansiva a qualquer preço plausível.

Contribuição técnico-científica, com análise nacional reprodutível sobre bases públicas
(CNES, SIA/SUS, SIH/SUS, SIGTAP, IBGE). O documento completo, o código e os dados estão
no anexo e no repositório. Síntese em cinco pontos:

1. CAPACIDADE INSTALADA. A Portaria SAES/MS 3.695/2026 desmembrou o código de tomógrafo
do CNES por número de canais. Em 06/2026 havia 432 equipamentos de 64 canais ou mais, em
315 estabelecimentos disponíveis ao SUS. Esse número é um piso: só 25% dos
estabelecimentos migraram do código genérico, e 2.785 equipamentos seguem sem
especificação. Recomenda-se que a apreciação final use a competência mais recente e
registre a proporção reclassificada. Apenas 79 estabelecimentos reúnem hardware
compatível, hemodinâmica e produção coronariana em 2025. Doze UFs não têm nenhum
estabelecimento nessa condição, e AP, PI e TO não têm nenhum tomógrafo de 64 canais ou
mais.

2. UNIDADE DE ANÁLISE. A cintilografia de perfusão é faturada em dois códigos, estresse
e repouso (151.784 e 151.225 em 2025). Contar procedimentos em vez de exames infla o
denominador em 19%. Por episódio, foram 787.954 investigações funcionais, com custo médio
de R$ 185,46: o teste ergométrico responde por 76% do volume, e a cintilografia por 82%
do gasto. As OCI de síndrome coronariana crônica somaram 7.616 episódios (0,96%). Não há
código SIGTAP para a angiotomografia. Os valores de R$ 185,46 e do cateterismo (R$ 730,14)
são preços de tabela, não custos.

3. LIMIAR ORÇAMENTÁRIO. O SIA não tem identificador de paciente, e razões entre
contagens agregadas não são probabilidades. Por isso, em vez de estimar quantos
cateterismos a angiotomografia evitaria, calculou-se quantos precisariam ser evitados,
por 100 pacientes, para que a estratégia fosse neutra a cada preço. Nos ensaios com
comparador não invasivo (PROMISE, PRECISE, CAPP, CRESCENT I/II, Foy 2017), a variação de
cateterismo total ficou entre −6,3 e +4,1 por 100. O resultado depende de qual exame a
angiotomografia substitui e de quanta revascularização induz. Substituindo o mix médio do
SIA (R$ 185, 76% ergometria), a neutralidade fica em R$ 139–215. Substituindo o percurso
do NATS precificado por episódio (R$ 524), em R$ 477–554. Substituindo a cintilografia
(R$ 787), em R$ 741–817 só com exames, ou R$ 458–560 quando se inclui a revascularização
adicional observada no PRECISE e em Foy 2017 (R$ 7.713 por angioplastia no SIH 2025). Se
a angiotomografia for somada ao percurso atual sem substituir nada, que é o cenário de
referência caso a incorporação crie o código sem dizer o que sai do percurso, nenhum
preço plausível é neutro (R$ −46 a +30; teto R$ 30). Estratificando pelo comparador que
as diretrizes indicam: na probabilidade baixa (nenhum exame ou ergometria), o preço
proposto de R$ 550 está fora do alcance; na intermediária, fica na zona de incerteza
apenas quando substitui a cintilografia. A Diretriz SBC de Síndrome Coronariana Crônica
2025 estratifica a indicação por probabilidade pré-teste (IIb-B na baixa; I-A na
intermediária, como alternativa à prova funcional). O PICO submetido trata "baixa ou
intermediária" como faixa única. A evidência econômica não sustenta decisão uniforme para
toda a faixa; sustenta condicionar a incorporação ao posicionamento e ao exame
substituído, alinhando-a a essa estratificação com protocolo que diga o que a
angiotomografia substitui.

4. OUTRO PICO. Nos quatro ensaios em que o comparador foi o cateterismo direto (CAD-MAN,
DISCHARGE, CONSERVE, Reis 2022), os pacientes já estavam indicados ao cateterismo, uma
população distinta. Nesse caso o custo prévio se cancela, e o preço de neutralidade vai
de R$ 482 a R$ 625 só com exames, chegando a R$ 841–868 (DISCHARGE, CONSERVE) quando se
credita a menor revascularização observada. A análise não demonstra que essa indicação
economiza; demonstra que a posição no percurso muda muito a plausibilidade. O próprio
relatório preliminar usa o DISCHARGE, um ensaio invasivo-primeiro, como fonte para o PICO
de primeira linha. Recomenda-se avaliar essa indicação como pergunta separada.

5. Nada nesta contribuição se pronuncia sobre o mérito clínico da tecnologia. O
SCOT-HEART demonstrou redução de morte coronariana e infarto em 5 e 10 anos. As
conclusões referem-se apenas à capacidade de implementação e à sustentabilidade
orçamentária de curto prazo, nos termos em que o Comitê solicitou esclarecimento.

Código, dados intermediários e tabelas: https://github.com/thyagosabo/angiotc-sus-cp73

---
*Contagem: ≈ 4.800 caracteres, sem travessões. Se o campo tiver limite menor, cortar os itens 2 e 5 primeiro (≈ −1.100); o anexo os cobre.*
