---
noindex: true
sitemap: false
layout: default
title: Agomelatina
parent: Apenas Predição do Modelo (L5)
nav_order: 32
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Agomelatina
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

## Agomelatina: Avaliação de Reposicionamento Pendente — Predições TxGNN Não Disponíveis
{: .text-alpha }

---

## Resumo

No ciclo de análise atual, o pipeline TxGNN **não gerou predições de reposicionamento** para este fármaco — possivelmente devido a falhas no mapeamento do DrugBank ID e na recuperação do mecanismo de ação.
Sem predições disponíveis, não é possível realizar a avaliação de reposicionamento neste ciclo.

<!-- review:begin br-lic-20261106-agomelatina-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Agomelatina é um fármaco psicotrópico comercializado no Brasil com **7 registros ativos** na ANVISA. / No ciclo de análise atual, o pipeline TxGNN **não gerou predições de reposicionamento** para este fármaco — possivelmente devido a falhas no mapeamento do DrugBank ID e na recuperação do mecanismo de ação.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 7 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-agomelatina-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não recuperada neste Evidence Pack |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 — sem predições do modelo |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 7) |
| Número de Registros | 7 (ativos: 5) |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

7 registros foram confirmados na fonte regulatória, porém os campos de detalhe (nome comercial, forma farmacêutica, indicação aprovada) não foram recuperados neste Evidence Pack. Os registros constam como comercializados, mas sem conteúdo identificável nos campos individuais.

> Para consulta direta dos registros, acesse: [ANVISA — Consulta de Medicamentos](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém predições TxGNN nem dados regulatórios detalhados, o que torna inviável qualquer avaliação de reposicionamento neste ciclo. Os gaps identificados são classificados como **Blocking** e **High** pelo próprio pipeline.

**Para prosseguir, é necessário:**

- **[Blocking]** Recuperar as advertências e contraindicações da bula ANVISA — baixar o PDF do produto e extrair as seções de segurança
- **[High]** Obter o DrugBank ID e o mecanismo de ação (MOA) via DrugBank API — o query retornou 1 resultado, mas o ID não foi mapeado para o Evidence Pack
- Recuperar os detalhes dos 7 registros ANVISA: nome comercial, forma farmacêutica e indicação aprovada
- Re-executar o pipeline de predição TxGNN após correção do mapeamento DrugBank para obter candidatos de reposicionamento

<!-- review:begin br-lic-20261106-agomelatina-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Re-executar o pipeline de predição TxGNN após correção do mapeamento DrugBank para obter candidatos de reposicionamento / Verificar a fonte dos dados regulatórios: o `query_log` indica fonte `tfda` (Taiwan FDA) — confirmar se os registros correspondem efetivamente à base ANVISA brasileira” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-agomelatina-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Agomelatina é um fármaco psicotrópico comercializado no Brasil com **7 registros ativos** na ANVISA” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Verificar a fonte dos dados regulatórios: o `query_log` indica fonte `tfda` (Taiwan FDA) — confirmar se os registros correspondem efetivamen” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

