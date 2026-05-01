---
layout: default
title: Agomelatina
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 0
---

# Agomelatina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Agomelatina: Avaliação de Reposicionamento Pendente — Predições TxGNN Não Disponíveis

---

## Resumo

Agomelatina é um fármaco psicotrópico comercializado no Brasil com **7 registros ativos** na ANVISA.
No ciclo de análise atual, o pipeline TxGNN **não gerou predições de reposicionamento** para este fármaco — possivelmente devido a falhas no mapeamento do DrugBank ID e na recuperação do mecanismo de ação.
Sem predições disponíveis, não é possível realizar a avaliação de reposicionamento neste ciclo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não recuperada neste Evidence Pack |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 — sem predições do modelo |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 7 |
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
- Verificar a fonte dos dados regulatórios: o `query_log` indica fonte `tfda` (Taiwan FDA) — confirmar se os registros correspondem efetivamente à base ANVISA brasileira
---

