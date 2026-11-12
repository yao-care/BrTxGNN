---
noindex: true
sitemap: false
layout: default
title: Axitinibe
parent: Apenas Predição do Modelo (L5)
nav_order: 96
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Axitinibe
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

## Axitinibe: Avaliação de Reposicionamento — Dados Insuficientes para Previsão Completa
{: .text-alpha }

## Resumo em Uma Frase

Axitinibe é um fármaco registrado no Brasil com 2 licenças na ANVISA (1 ativa e 1 cancelada), porém os dados de indicação original e mecanismo de ação não estão disponíveis neste Evidence Pack.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados atuais, tornando inviável a análise de novas indicações.
Para avançar na avaliação, é necessário complementar os dados faltantes identificados em dois gaps críticos.

<!-- review:begin br-lic-20261112-axitinibe-1 -->

> **Correção de verificação (2026-11-12)**: Texto original: “com 2 licenças ativas na ANVISA” Corrigido conforme os dados abertos de medicamentos da ANVISA (2026-11-05): 2 registros para este medicamento, 1 válidos e 1 cancelados ou caducos; os números atuais estão no Resumo rápido. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261112-axitinibe-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Sem previsões disponíveis |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão do modelo com dados atuais) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

No entanto, os detalhes individuais de cada registro (número oficial, nome comercial, forma farmacêutica e texto da indicação aprovada) não constam nos dados recebidos neste Evidence Pack.

<!-- review:begin br-lic-20261106-axitinibe-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Foram identificados **2 registros ativos** de Axitinibe na ANVISA. No entanto, os detalhes individuais de cada registro (número oficial, nome comercial, forma farmacêutica e texto da indicação aprovada) não constam nos dados recebidos neste Evidence Pack.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-axitinibe-1 -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 121100452 | INLYTA | PFIZER BRASIL LTDA | Ativo |
| 102160240 | INLYTA | LABORATÓRIOS PFIZER LTDA | Cancelado |

> Recomenda-se consulta direta à base ANVISA para recuperar esses dados.

<!-- review:begin br-lic-20261106-axitinibe-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “> Os registros existem conforme confirmado pelo query TFDA (resultado: 2 licenças), mas os campos de detalhamento não foram retornados. Recomenda-se consulta direta à base ANVISA para recuperar esses dados.” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-axitinibe-2 -->

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack apresenta lacunas de dados em nível **Blocking** e **High** que impedem a execução completa do pipeline de avaliação: estão ausentes as advertências e contraindicações da bula ANVISA, o mecanismo de ação (MOA) e, sobretudo, qualquer previsão de reposicionamento gerada pelo TxGNN — tornando inviável a análise de novas indicações neste momento.

**Para prosseguir, é necessário:**
- **[DG001 — Blocking]** Baixar e analisar as bulas ANVISA dos 2 registros, extraindo indicações aprovadas, advertências principais e contraindicações
- **[DG002 — High]** Consultar a DrugBank API para recuperar o mecanismo de ação (MOA) do Axitinibe e categorias farmacológicas — nota: o query DrugBank retornou 1 resultado, mas os dados não foram incluídos no Evidence Pack atual
- Complementar os campos vazios dos 2 registros ANVISA (número de registro, nome comercial, forma farmacêutica, texto completo da indicação)
- Reexecutar o pipeline TxGNN com os dados de MOA e indicação preenchidos para gerar previsões de reposicionamento válidas

<!-- review:begin br-lic-20261106-axitinibe-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**[DG001 — Blocking]** Baixar e analisar as bulas ANVISA dos 2 registros, extraindo indicações aprovadas, advertências principais e contraindicações (fonte: TFDA/ANVISA, método: download e parse do PDF da bula)” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-axitinibe-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Foram identificados **2 registros ativos** de Axitinibe na ANVISA” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Os registros existem conforme confirmado pelo query TFDA (resultado: 2 licenças), mas os campos de detalhamento não foram retornados” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(fonte: TFDA/ANVISA, método: download e parse do PDF da bula)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-12 | Licenças ativas: 2 → 1 (de 2) | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

