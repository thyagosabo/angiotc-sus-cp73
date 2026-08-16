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
