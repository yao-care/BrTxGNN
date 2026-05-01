---
layout: default
title: Cabergolina
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 0
---

# Cabergolina
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

# Cabergolina: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Cabergolina é um agonista dopaminérgico utilizado principalmente no tratamento da hiperprolactinemia e da doença de Parkinson.
O presente Evidence Pack **não contém previsões TxGNN** para novas indicações — o campo `predicted_indications` está vazio — portanto não é possível avaliar candidatos de reposicionamento neste ciclo.
Existem **20 registros** da substância no mercado brasileiro, porém os detalhes dos registros não foram recuperados nesta execução.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste pack (registros sem detalhes) |
| Nova Indicação Prevista | — (sem previsão TxGNN) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Este Relatório Está Incompleto?

Este Evidence Pack foi gerado com **dados parciais**: apenas a consulta ao banco regulatório brasileiro (TFDA/ANVISA) e ao DrugBank foram executadas, mas os campos de retorno dos registros estão em branco (campos `license_number`, `product_name_zh`, `approved_indication_text` todos vazios).

Há dois bloqueios críticos identificados no `meta.data_gaps`:

| ID | Item Faltante | Severidade | Impacto |
|----|--------------|-----------|---------|
| DG001 | TFDA/ANVISA — advertências e contraindicações da bula | **Bloqueante** | Impede avaliação inicial de segurança |
| DG002 | Mecanismo de ação (MOA) | Alta | Impede análise de relevância mecanística |

Adicionalmente, o campo `predicted_indications` retornou **lista vazia**, o que significa que o pipeline TxGNN não gerou candidatos de reposicionamento para CABERGOLINA neste ciclo. Sem candidatos, não há base para avaliação de nova indicação.

---

## Informações de Comercialização no Brasil

Os 20 registros existem no sistema regulatório, mas os detalhes não foram recuperados nesta execução do pipeline. A tabela abaixo não pode ser preenchida:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---|---|---|---|
| — | — | — | — |

> **Ação necessária:** Executar novamente a consulta ao portal ANVISA com extração completa dos campos de cada registro.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações e os dados regulatórios de detalhe não foram recuperados, tornando impossível qualquer análise de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**

1. **Reexecutar a consulta regulatória** — recuperar os campos `license_number`, `product_name_zh`, `dosage_form` e `approved_indication_text` dos 20 registros ANVISA de Cabergolina
2. **Corrigir o pipeline TxGNN** — investigar por que `predicted_indications` retornou vazio; verificar se o mapeamento DrugBank foi bem-sucedido (query_log id=3 indica `success` com 1 resultado, mas o `drugbank_id` ficou `null`)
3. **Preencher o MOA (DG002)** — consultar DrugBank API com o ID recuperado para obter o mecanismo de ação e categorias do fármaco
4. **Baixar e parsear a bula (DG001)** — obter advertências e contraindicações do PDF da bula ANVISA para liberar a avaliação de segurança
5. **Reprocessar o pack** — após as correções acima, gerar novo Evidence Pack versão v5 com dados completos
---

