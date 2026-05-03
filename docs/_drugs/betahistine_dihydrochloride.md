---
layout: default
title: Betahistine Dihydrochloride
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 0
---

# Betahistine Dihydrochloride
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

# Betahistina Dicloridrato: Avaliação de Reposicionamento — Sem Previsões TxGNN Disponíveis

## Resumo

Betahistina Dicloridrato é um análogo da histamina amplamente utilizado no tratamento da Doença de Ménière e síndromes vertiginosas periféricas, com mecanismo de ação relacionado aos receptores histaminérgicos H1 e H3.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise (lista `predicted_indications` vazia).
O fármaco também **não possui registros** no mercado regulatório consultado, o que limita significativamente a avaliação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados regulatórios consultados (0 registros) |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/A (ausência de previsão impede classificação) |
| Situação no Mercado | ✗ Não Comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão?

O Evidence Pack indica que a consulta ao DrugBank retornou 1 resultado (`result_count: 1`), mas o `drugbank_id` permanece nulo no registro do fármaco. Isso sugere que o mapeamento entre o nome **"BETAHISTINE DIHYDROCHLORIDE"** e o identificador DrugBank não foi concluído, o que impede o modelo TxGNN de posicionar o fármaco no grafo de conhecimento e gerar candidatos de reposicionamento.

Uma possível causa é a variação de nomenclatura: o fármaco pode estar registrado no DrugBank como **Betahistine** (base livre, DB00772) em vez de **Betahistine Dihydrochloride** (forma de sal). A resolução deste mapeamento é o pré-requisito para executar qualquer previsão.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Betahistina Dicloridrato, os dados regulatórios locais estão ausentes (0 registros), e as lacunas de dados críticas (MOA e advertências) ainda precisam ser resolvidas antes de qualquer avaliação de segurança ou eficácia.

**Para prosseguir, é necessário:**
- **[DG002 — Alta prioridade]** Resolver o mapeamento `drugbank_id`: verificar se `DB00772` (Betahistine) corresponde a este sal e atualizar o registro para reprocessar as previsões TxGNN
- **[DG001 — Bloqueante]** Obter a bula oficial via TFDA ou equivalente regulatório para extrair advertências e contraindicações
- Confirmar se o fármaco está registrado sob nome alternativo (ex.: "Betahistina", "Betaserc", "Merislon") no mercado consultado
- Após resolução do DrugBank ID, reexecutar o pipeline TxGNN para gerar `predicted_indications`
- Avaliar a necessidade de inclusão de fontes regulatórias adicionais para mercados onde o fármaco está efetivamente comercializado (ex.: UE, Japão)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

