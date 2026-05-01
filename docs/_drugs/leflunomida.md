---
layout: default
title: Leflunomida
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 0
---

# Leflunomida
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

# Leflunomida: Avaliação de Reposicionamento — Dados Insuficientes para Previsão Completa

## Resumo

Leflunomida (LEFLUNOMIDA) é um fármaco com 19 registros ativos no Brasil, confirmado como comercializado. No entanto, o Evidence Pack recebido não contém indicações originais registradas, mecanismo de ação (MOA) nem previsões de novas indicações pelo modelo TxGNN. Sem o campo `predicted_indications` preenchido, não é possível gerar um relatório completo de reposicionamento neste momento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados recebidos |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos reais associados a nenhuma previsão) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 19 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. O DrugBank foi consultado com resultado positivo (1 registro encontrado), mas o `drugbank_id` não foi retornado no Evidence Pack, impedindo a recuperação do MOA. Adicionalmente, o campo `original_indications` está vazio e nenhuma indicação aprovada foi extraída dos 19 registros de licença.

Sem MOA e sem `predicted_indications`, não é possível construir uma justificativa mecanística para nenhuma nova indicação candidata.

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN (`predicted_indications` está vazio) nem dados regulatórios detalhados das 19 licenças, o que impede qualquer análise de reposicionamento ou avaliação de segurança neste estágio.

**Para prosseguir, é necessário:**
- **[Bloqueante — DG001]** Baixar e analisar as bulas das 19 licenças registradas via ANVISA para extrair indicações aprovadas, advertências e contraindicações
- **[Alta prioridade — DG002]** Recuperar o `drugbank_id` correto e obter o MOA via DrugBank API (a consulta retornou 1 resultado, mas o ID não foi capturado)
- **[Bloqueante para o relatório]** Executar o pipeline TxGNN para gerar `predicted_indications` com pontuações, ensaios clínicos e literatura associada — sem esse campo, o relatório de reposicionamento não pode ser produzido
- Reprocessar o Evidence Pack com os dados complementados e resubmeter para geração do relatório completo
---

