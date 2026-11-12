---
noindex: true
sitemap: false
layout: default
title: Betaxolol Hydrochloride
parent: Apenas Predição do Modelo (L5)
nav_order: 131
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Betaxolol Hydrochloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Betaxolol Hidrocloro: Avaliação Incompleta — Dados Insuficientes para Análise de Reposicionamento
{: .text-alpha }

## Resumo em Uma Frase

Betaxolol Hidrocloro é um bloqueador beta-1 adrenérgico seletivo, historicamente indicado no tratamento da hipertensão arterial e do glaucoma/hipertensão ocular.
O Evidence Pack atual **não contém previsões do modelo TxGNN** para novas indicações terapêuticas, impossibilitando a condução de análise formal de reposicionamento.

<!-- review:begin br-lic-20261106-betaxolol_hydrochloride-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O Evidence Pack atual **não contém previsões do modelo TxGNN** para novas indicações terapêuticas, impossibilitando a condução de análise formal de reposicionamento. / A ausência de registros no mercado, de informações de segurança e de dados de mecanismo de ação torna esta avaliação classificada como **Hold** até que as lacunas críticas sejam sanadas.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 2 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betaxolol_hydrochloride-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Sem previsões TxGNN disponíveis |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 (apenas pipeline, sem estudos reais associados) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão É Razoável?

Atualmente, não há dados de previsão disponíveis no Evidence Pack para o Betaxolol Hidrocloro. O modelo TxGNN não retornou candidatos de reposicionamento nesta rodada de consulta, o que pode decorrer de cobertura incompleta do mapeamento DrugBank ou de ausência do fármaco na rede do grafo de conhecimento.

Do ponto de vista farmacológico geral, o betaxolol é um antagonista seletivo de receptores beta-1 adrenérgicos. Sua seletividade para receptores cardíacos (beta-1) em detrimento dos receptores brônquicos (beta-2) confere um perfil de segurança diferenciado em relação a betabloqueadores não seletivos. Na forma sistêmica (comprimidos), é utilizado para hipertensão; na forma tópica oftálmica (colírio), reduz a pressão intraocular no glaucoma de ângulo aberto e na hipertensão ocular.

Contudo, **sem dados de mecanismo de ação (MOA) validados no Evidence Pack e sem previsões do TxGNN**, qualquer hipótese de reposicionamento permanece especulativa. A consulta ao DrugBank retornou 1 resultado (ver Query Log), mas os dados correspondentes não foram integrados ao pacote — o que representa uma lacuna sanável antes de prosseguir.

---

## Considerações de Segurança

Consulte a bula do produto para informações completas de segurança.

> As lacunas de dados de segurança (DG001) têm severidade **Bloqueante** para qualquer avanço na avaliação.

<!-- review:begin br-lic-20261106-betaxolol_hydrochloride-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “> **Nota:** A consulta às fontes DDI e TFDA não retornou dados de advertências, contraindicações ou interações medicamentosas para este fármaco no Evidence Pack atual. As lacunas de dados de segurança (DG001) têm severidade **Bloqueante** para qualquer avanço na avaliação.” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betaxolol_hydrochloride-2 -->

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações pelo modelo TxGNN, e os campos críticos de segurança, mecanismo de ação e registro regulatório estão ausentes — tornando inviável qualquer análise estruturada de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- 🔴 **(Bloqueante — DG001)** Obter advertências, contraindicações e informações de bula via ANVISA (download e parsing do PDF da bula)
- 🟠 **(Alta — DG002)** Integrar dados de mecanismo de ação (MOA) do DrugBank — a consulta já retornou 1 resultado pendente de extração
- 🟡 Executar ou revisar o pipeline TxGNN para gerar previsões de reposicionamento para o Betaxolol Hidrocloro
- 🟡 Verificar mapeamento para DrugBank ID (atualmente nulo) para garantir cobertura no grafo de conhecimento

<!-- review:begin br-lic-20261106-betaxolol_hydrochloride-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “🔴 **(Bloqueante — DG001)** Obter advertências, contraindicações e informações de bula via TFDA/ANVISA (download e parsing do PDF da bula)” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betaxolol_hydrochloride-3 -->

<!-- review:begin br-lic-20261106-betaxolol_hydrochloride-4 -->

> **Correção de verificação (2026-11-06)**: Texto original: “🟡 Verificar mapeamento para DrugBank ID (atualmente nulo) para garantir cobertura no grafo de conhecimento / 🟡 Investigar por que a consulta TFDA retornou 0 registros — o fármaco pode estar cadastrado sob variantes de nome (ex: "betaxolol", sem o sufixo "hydrochloride")” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betaxolol_hydrochloride-4 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A ausência de registros no mercado, de informações de segurança e de dados de mecanismo de ação torna esta avaliação classificada como **Hol” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “**Nota:** A consulta às fontes DDI e TFDA não retornou dados de advertências, contraindicações ou interações medicamentosas para este fármac” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “TFDA/” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “🟡 Investigar por que a consulta TFDA retornou 0 registros — o fármaco pode estar cadastrado sob variantes de nome (ex: "betaxolol", sem o su” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

