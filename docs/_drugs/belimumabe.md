---
layout: default
title: Belimumabe
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 0
---

# Belimumabe
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

# BELIMUMABE: Avaliação de Reposicionamento — Dados Insuficientes para Previsão Completa

## Resumo em Uma Frase

Belimumabe é um biológico (anticorpo monoclonal) registrado no mercado brasileiro, cujo mecanismo de ação não consta no Evidence Pack atual. O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco nesta execução, e os dados de registro regulatório estão incompletos — tornando impossível concluir uma avaliação de reposicionamento nesta fase.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Não disponível (nenhuma previsão TxGNN retornada) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsões nem estudos associados) |
| Situação no Mercado Brasileiro | ✓ Já Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Segundo informações conhecidas, belimumabe é um anticorpo monoclonal IgG1λ que inibe o estimulador de linfócitos B (BLyS/BAFF), reduzindo a sobrevivência de células B autorreativas — mecanismo relevante para doenças autoimunes. No entanto, como o campo `original_moa` está ausente e `predicted_indications` está vazio, **não é possível estabelecer a relação mecanística entre indicação original e nova indicação** nesta avaliação.

> **Nota:** O Evidence Pack está incompleto. Os dados necessários para análise de reposicionamento — indicação original, MOA detalhado e previsões TxGNN — precisam ser obtidos antes de prosseguir.

---

## Informações de Comercialização no Brasil

O fármaco possui **1 registro ativo** com status "Já Comercializado". Os detalhes individuais do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não foram populados** no Evidence Pack atual e precisam ser recuperados via download da bula na ANVISA.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|--------------------|----------------|--------------------|--------------------|
| *(não disponível)* | *(não disponível)* | *(não disponível)* | *(não disponível)* |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está estruturalmente incompleto — ausência de previsões TxGNN (`predicted_indications: []`), dados de MOA ausentes e detalhes de registro regulatório não populados. Não existe base de evidências suficiente para emitir recomendação de reposicionamento.

**Para prosseguir, é necessário:**

- **\[Bloqueante\]** Baixar e analisar a bula em PDF no portal ANVISA para obter advertências, contraindicações e indicação aprovada
- **\[Alta prioridade\]** Consultar DrugBank API com o INN "belimumab" para obter `drugbank_id`, MOA e categorias farmacológicas
- **\[Alta prioridade\]** Reexecutar o pipeline TxGNN para gerar previsões de novas indicações — verificar se o fármaco está presente no vocabulário do modelo (`drugbank_vocab.csv`)
- **\[Médio\]** Popular os campos de registro regulatório: número de registro ANVISA, nome comercial, forma farmacêutica e texto completo da indicação aprovada
- **\[Médio\]** Revisar a busca de DDI (resultado `not_found`) — confirmar se a ausência é real ou se o identificador usado na busca estava incorreto
---

