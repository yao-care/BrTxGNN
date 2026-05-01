---
layout: default
title: Otilônio Bromide
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 0
---

# Otilônio Bromide
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

# OTILÔNIO BROMIDE: Avaliação de Reposicionamento — Dados Insuficientes para Análise Completa

## Resumo em Uma Frase

OTILÔNIO BROMIDE é um fármaco com histórico de uso como antiespasmódico gastrointestinal em diversos países, porém sem registro ativo no Brasil.
No presente Evidence Pack, **nenhuma previsão de reposicionamento foi gerada pelo modelo TxGNN**, pois o fármaco não possui DrugBank ID associado — pré-requisito obrigatório para o mapeamento ao grafo de conhecimento.
Sem candidatos gerados, não é possível conduzir análise de indicação, evidências clínicas ou justificativa mecanística neste ciclo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (modelo não gerou candidatos; sem estudos mapeados) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão Não Está Disponível?

O pipeline TxGNN requer que o fármaco esteja mapeado a um **DrugBank ID** para ser posicionado no grafo de conhecimento biológico e gerar previsões de reposicionamento. No Evidence Pack atual, o campo `drugbank_id` retornou **nulo**, apesar de a consulta ao DrugBank ter retornado 1 resultado no log de queries (Query ID 3).

Isso indica que o resultado foi encontrado, mas não foi parseado ou vinculado ao registro do fármaco — possivelmente por variação ortográfica do nome (note o acento em "OTILÔNIO", forma em português do nome DCI "Otilonium Bromide" em inglês). Este é um problema de normalização de nome que precisa ser resolvido antes de qualquer análise subsequente.

Adicionalmente, a ausência de indicação aprovada registrada impossibilita a etapa de comparação mecanística entre indicação original e nova indicação prevista.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em todos os níveis críticos — sem DrugBank ID, sem previsões TxGNN, sem registros ANVISA e sem dados de segurança — tornando inviável qualquer análise de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- **[Crítico]** Mapear o DrugBank ID correto para "Otilonium Bromide" (nome DCI em inglês), resolvendo a inconsistência de nome causada pela variante em português "OTILÔNIO BROMIDE"
- **[Crítico]** Reexecutar o pipeline TxGNN com o DrugBank ID correto para gerar candidatos de reposicionamento
- **[Alto]** Obter dados regulatórios da ANVISA: registros ativos, indicação aprovada, forma farmacêutica
- **[Alto]** Obter dados de segurança (advertências, contraindicações) da bula ANVISA ou do DrugBank
- **[Alto]** Identificar o mecanismo de ação (MOA) via DrugBank após correção do ID
---

