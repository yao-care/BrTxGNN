---
layout: default
title: Acetazolamida
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 0
---

# Acetazolamida
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

# Acetazolamida: Avaliação de Reposicionamento — Previsões TxGNN Não Disponíveis

## Resumo

Acetazolamida (ACETAZOLAMIDA) é um inibidor da anidrase carbônica classicamente utilizado no tratamento do glaucoma de ângulo aberto, edema e epilepsia do tipo ausência. Nesta execução do pipeline TxGNN, **não foram geradas previsões de novas indicações** para este fármaco. A avaliação completa de reposicionamento não pode ser concluída até que os dados ausentes sejam complementados e o modelo reprocessado.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Fármaco | Acetazolamida (ACETAZOLAMIDA) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 5 |
| Previsões TxGNN Disponíveis | Nenhuma |
| Nível de Evidência | Não aplicável |
| Decisão Recomendada | Hold |

---

## Por que Esta Avaliação Está Incompleta?

O Evidence Pack recebido apresenta lacunas em três camadas distintas que, em conjunto, inviabilizam a avaliação padrão de reposicionamento:

**1. Ausência de previsões do modelo TxGNN**
O campo `predicted_indications` está vazio. Isso pode decorrer de falha no mapeamento do nome do fármaco: o pipeline recebeu "ACETAZOLAMIDA" (grafia em português/espanhol), mas o DrugBank e o grafo de conhecimento TxGNN indexam o composto como "acetazolamide" (INN em inglês). A ausência de `drugbank_id` no pacote confirma que o mapeamento DrugBank não foi resolvido nesta execução.

**2. Detalhes regulatórios incompletos**
Embora o sistema confirme **5 registros ativos** na ANVISA, todos os campos de detalhe (número de registro, nome comercial, forma farmacêutica, indicação aprovada) constam como vazios. Os dados foram coletados do portal TFDA/ANVISA, mas a extração dos metadados dos registros individuais não foi concluída.

**3. Dados de segurança e mecanismo ausentes**
As advertências, contraindicações e o mecanismo de ação (MOA) são classificados como lacunas de dados com severidade **Bloqueante (DG001)** e **Alta (DG002)**, respectivamente, impedindo a avaliação de segurança preliminar.

---

## Lacunas de Dados Críticas

| Código | Item Ausente | Severidade | Impacto | Fonte Recomendada |
|--------|-------------|-----------|---------|-------------------|
| DG001 | Advertências e contraindicações (bula ANVISA) | Bloqueante | Sem avaliação de segurança S1 | ANVISA — baixar PDF da bula e processar |
| DG002 | Mecanismo de ação (MOA) | Alta | Sem análise de relevância mecanística | DrugBank API — buscar por "acetazolamide" |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não gerou candidatos de reposicionamento para Acetazolamida nesta execução, possivelmente por falha no mapeamento do nome INN (português → inglês). Sem previsões de novas indicações, a estrutura central do relatório de reposicionamento não pode ser preenchida.

**Para prosseguir, é necessário:**
- Resolver o **mapeamento DrugBank**: buscar "acetazolamide" (INN em inglês) no DrugBank API para obter o `drugbank_id` correto (esperado: DB00819)
- **Reexecutar o pipeline TxGNN** após confirmação do `drugbank_id`, com normalização do nome INN para inglês
- **Coletar detalhes dos 5 registros ANVISA**: nome comercial, forma farmacêutica e indicação aprovada para cada registro
- **Baixar e processar a bula ANVISA** para advertências e contraindicações (remediar DG001)
- **Consultar DrugBank API** para obter o mecanismo de ação completo (remediar DG002)
- Após reprocessamento, verificar se `predicted_indications` foi populado e reemitir o relatório completo
---

