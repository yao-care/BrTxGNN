---
layout: default
title: Carfilzomibe
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 0
---

# Carfilzomibe
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

# Carfilzomib: Relatório Preliminar — Previsões TxGNN Pendentes

## Resumo em Uma Frase

Carfilzomib (carfilzomibe) é um inibidor de proteassoma de segunda geração, aprovado para o tratamento do mieloma múltiplo recidivante ou refratário.
O pipeline TxGNN **não retornou previsões de novas indicações** para este fármaco no momento da geração deste relatório — o campo `predicted_indications` está vazio.
Desta forma, **não é possível realizar análise de reposicionamento** até que as previsões sejam executadas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mieloma múltiplo recidivante ou refratário |
| Nova Indicação Prevista | — (dados ausentes) |
| Pontuação de Previsão TxGNN | — (pipeline não executado) |
| Nível de Evidência | — (sem previsão disponível) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 5 |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

Carfilzomib é um agente antineoplásico da classe dos inibidores de proteassoma (epoximicina), utilizado exclusivamente em oncologia.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo — inibidor irreversível do proteassoma 26S (subunidade β5, atividade quimotripsina-símile) |
| Risco de Mielossupressão | Médio-alto (anemia, trombocitopenia e neutropenia são toxicidades hematológicas frequentes) |
| Classificação de Emetogenicidade | Baixa a média |
| Itens de Monitoramento | Hemograma completo (CBC com diferencial), função renal (creatinina, clearance), função hepática, pressão arterial, monitoramento cardíaco (eventos cardiopulmonares descritos) |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de citotóxicos injetáveis; preparo em cabine de fluxo laminar vertical |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN (`predicted_indications: []`) nem detalhes dos registros brasileiros, impossibilitando qualquer análise de reposicionamento ou avaliação de força de evidência neste momento.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN para carfilzomib e obter `predicted_indications` com pontuação, ensaios clínicos e literatura associada
- Preencher os detalhes dos 5 registros na ANVISA (número de registro, nome comercial, forma farmacêutica, indicação aprovada)
- Obter MOA completo via DrugBank API (DG002 — severidade High)
- Recuperar advertências, contraindicações e interações da bula ANVISA (DG001 — severidade Blocking)
---

