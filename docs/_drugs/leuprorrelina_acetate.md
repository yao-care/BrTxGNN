---
layout: default
title: Leuprorrelina Acetate
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 0
---

# Leuprorrelina Acetate
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

# LEUPRORRELINA ACETATE: Avaliação Inconclusiva — Dados Insuficientes para Análise de Reposicionamento

## Resumo em Uma Frase

Leuprorrelina (Leuprorelin) é um agonista do hormônio liberador de gonadotrofinas (GnRH), amplamente utilizado no tratamento de cânceres hormônio-sensíveis, endometriose e puberdade precoce.
O modelo TxGNN **não gerou indicações previstas** para este fármaco neste ciclo de avaliação, possivelmente devido ao nome incorreto na consulta ("LEUPRORRELINA" em vez do INN padronizado "LEUPRORELIN").
Sem previsão de nova indicação e sem registros no Brasil, não é possível avançar para análise de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma (modelo TxGNN retornou lista vazia) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | **L5** — Sem previsão de modelo, sem estudos reais |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão não foi Gerada?

Há dois prováveis motivos para o modelo TxGNN não ter retornado indicações previstas:

1. **Erro tipográfico no INN**: O nome consultado foi `LEUPRORRELINA ACETATE` (com duplo "R"), enquanto o INN padronizado é `LEUPRORELIN ACETATE`. Isso pode ter impedido o mapeamento correto ao DrugBank e, consequentemente, ao grafo de conhecimento.

2. **DrugBank ID ausente**: O campo `drugbank_id` está vazio, o que impede o pipeline de conhecimento de localizar as relações do fármaco no grafo. O log indica que a consulta ao DrugBank retornou 1 resultado (`result_count: 1`), mas o ID não foi transferido para o Evidence Pack — indicando falha na extração ou integração.

Esses dois fatores combinados impedem a execução do modelo de previsão, tornando o relatório de reposicionamento inaplicável neste ciclo.

---

## Informações de Comercialização no Brasil

O fármaco não possui registros ativos no Brasil. Nenhuma licença foi identificada na consulta à ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem indicações previstas pelo TxGNN e sem registros regulatórios no Brasil, não há base suficiente para iniciar a análise de reposicionamento. O problema é de ordem técnica e pode ser resolvido antes da próxima execução.

**Para prosseguir, é necessário:**

- [ ] **Corrigir o INN**: Usar o nome padronizado `LEUPRORELIN ACETATE` (remover o "R" duplicado) em todos os campos de consulta
- [ ] **Recuperar o DrugBank ID**: O log indica que o DrugBank retornou 1 resultado — extrair e registrar o `drugbank_id` correspondente (provavelmente `DB00007`)
- [ ] **Re-executar o pipeline TxGNN** com os dados corrigidos para obter `predicted_indications`
- [ ] **Coletar dados de segurança (DG001)**: Baixar a bula ANVISA/FDA para extrair advertências e contraindicações
- [ ] **Coletar MOA (DG002)**: Consultar DrugBank API com o ID correto para obter o mecanismo de ação formal
---

