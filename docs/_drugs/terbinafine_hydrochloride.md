---
layout: default
title: Terbinafine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 0
---

# Terbinafine Hydrochloride
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

# Terbinafina Cloridrato: Avaliação de Reposicionamento — Previsão Não Gerada Neste Ciclo

---

## Resumo em Uma Frase

Terbinafina (cloridrato) é um antifúngico da classe das alilaminas, amplamente utilizado no tratamento de infecções fúngicas como onicomicose e dermatomicoses por dermatófitos.
Neste ciclo de análise, o modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco, pois o campo `drugbank_id` permanece vazio apesar de a consulta ao DrugBank ter retornado um resultado com sucesso.
Sem previsão de indicação-alvo, a análise de reposicionamento não pode avançar.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções fúngicas (onicomicose, tinea corporis, tinea pedis) |
| Nova Indicação Prevista | — (nenhuma previsão gerada neste ciclo) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem previsão do modelo |
| Situação no Mercado Brasileiro | Não encontrado na fonte consultada (verificar ANVISA) |
| Número de Registros | 0 (consulta atual) |
| Decisão Recomendada | **Hold** |

---

## Por que Não Foi Gerada uma Previsão?

Terbinafina é um fármaco bem caracterizado: inibe seletivamente a enzima **esqualeno epoxidase** fúngica, bloqueando a síntese de ergosterol e causando acúmulo tóxico de esqualeno na célula fúngica. Essa especificidade de mecanismo é bem documentada na literatura. No entanto, o pipeline não conseguiu completar o mapeamento necessário para que o TxGNN processasse este candidato.

O registro de consultas (`query_log`) revela uma inconsistência importante: a consulta ao DrugBank retornou **1 resultado com sucesso**, mas o campo `drugbank_id` no Evidence Pack permanece `null`. Isso indica que o ID DrugBank foi localizado mas não foi propagado corretamente para o JSON de saída — uma falha na etapa de persistência do pipeline de mapeamento.

Adicionalmente, o campo `original_indications` está vazio, o que impede o TxGNN de calcular similaridade entre indicação de origem e candidatos de reposicionamento. Por fim, a consulta regulatória foi direcionada à fonte TFDA (Taiwan), retornando 0 registros — o que não reflete necessariamente a situação regulatória no Brasil, onde Terbinafina possui histórico de comercialização.

---

## Informações de Comercialização no Brasil

Nenhum registro foi encontrado na consulta atual.

> **Atenção:** A fonte de dados regulatórios consultada neste ciclo parece ser a base TFDA (Taiwan Food and Drug Administration), não a ANVISA. Para confirmar a situação de registro no Brasil, consulte diretamente o portal da ANVISA em [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline não completou o mapeamento DrugBank para Terbinafina Cloridrato neste ciclo, resultando em `predicted_indications` vazia e impossibilitando qualquer análise de reposicionamento. A causa raiz identificada é uma falha de persistência do `drugbank_id` — o dado existe na fonte, mas não foi gravado no Evidence Pack.

**Para prosseguir, é necessário:**
- **Corrigir o pipeline de mapeamento**: o DrugBank retornou 1 resultado com sucesso, mas o `drugbank_id` não foi persistido — localizar e corrigir o bug na etapa de integração
- **Preencher `original_indications`**: mapear as indicações aprovadas a partir do DrugBank ou da bula ANVISA
- **Apontar a consulta regulatória para ANVISA**: substituir a fonte TFDA pela base brasileira e re-executar a coleta
- **Re-executar o pipeline completo** após as correções acima para obter previsões TxGNN válidas
- **Coletar dados de MOA e segurança**: obter advertências e contraindicações da bula ANVISA após confirmação do registro
---

