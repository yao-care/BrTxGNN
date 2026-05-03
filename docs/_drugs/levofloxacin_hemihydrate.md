---
layout: default
title: Levofloxacin Hemihydrate
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 0
---

# Levofloxacin Hemihydrate
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

# Levofloxacin Hemihydrate: Avaliação Inconclusiva — Sem Predições de Reposicionamento Disponíveis

## Resumo em Uma Frase

Levofloxacin Hemihydrate é a forma de sal hemihidratada da levofloxacina, antibiótico da classe das fluoroquinolonas amplamente utilizado no tratamento de infecções bacterianas graves.
O modelo TxGNN **não gerou nenhuma predição de reposicionamento** para este fármaco nesta análise, impossibilitando a avaliação de novas indicações terapêuticas.
Há **0 ensaios clínicos** e **0 publicações** vinculados a candidatos de reposicionamento neste Evidence Pack — a análise está bloqueada por ausência de dados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no registro regulatório brasileiro |
| Nova Indicação Prevista | Nenhuma predição gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (ausência de estudos vinculados) |
| Situação no Mercado Brasileiro | Não comercializado (formulação hemihydrate não encontrada) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Predição Disponível?

A ausência de predições TxGNN para este fármaco decorre de dois fatores identificados no pipeline:

**1. Falta de mapeamento para o DrugBank ID.** A consulta ao DrugBank retornou 1 resultado (`result_count: 1`), mas o `drugbank_id` não foi preenchido no Evidence Pack. Sem o DrugBank ID, o modelo TxGNN não consegue posicionar o fármaco no grafo de conhecimento (Knowledge Graph) e, portanto, não gera predições de reposicionamento.

**2. Formulação específica não encontrada na ANVISA.** A busca pela forma exata "LEVOFLOXACIN HEMIHYDRATE" não retornou registros no banco regulatório brasileiro (`result_count: 0`). É provável que os registros existam sob o nome "LEVOFLOXACINA" (sem especificação do sal hemihydrate), o que pode ter impedido o correto mapeamento regulatório e a extração da indicação original.

Ressalta-se que a levofloxacina em outras formulações é um antibiótico fluoroquinolônico de amplo espectro com aplicações clínicas bem estabelecidas — a ausência de predições não reflete ausência de relevância clínica, mas sim uma lacuna de dados no pipeline de ingestão.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem predições TxGNN e sem indicação original mapeada, não há base analítica para avançar com avaliação de reposicionamento. O problema é de ingestão de dados, não de ausência de potencial terapêutico do fármaco.

**Para prosseguir, é necessário:**
- **[Crítico]** Repetir a busca regulatória usando o nome simplificado `LEVOFLOXACINA` (sem especificação do sal) para recuperar os registros ANVISA e as indicações aprovadas
- **[Crítico]** Preencher o `drugbank_id` a partir do resultado já obtido na consulta DrugBank (`result_count: 1`), permitindo que o TxGNN posicione o fármaco no KG e gere predições
- **[Alto]** Consultar a bula disponível na ANVISA para preencher os dados de segurança (advertências, contraindicações, interações medicamentosas)
- **[Alto]** Reexecutar o pipeline completo (KG + DL + Mapping) após correção do mapeamento de nome para obter `predicted_indications`
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

