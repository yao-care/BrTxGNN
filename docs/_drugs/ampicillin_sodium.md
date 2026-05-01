---
layout: default
title: Ampicillin Sodium
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 0
---

# Ampicillin Sodium
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

# Ampicillin Sódico: Avaliação de Reposicionamento — Sem Predição Disponível

## Resumo em Uma Frase

Ampicillin Sódico é um antibiótico de amplo espectro da classe das aminopenicilinas, classicamente utilizado no tratamento de infecções bacterianas como pneumonia, infecções urinárias e meningite bacteriana.
No ciclo de processamento atual, o modelo TxGNN **não gerou nenhuma predição** de nova indicação para este fármaco.
A avaliação está comprometida pela ausência de registros no mercado brasileiro e pela inexistência de candidatos de reposicionamento no pack de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (amplo espectro — penicilina do grupo aminopenicilinas) |
| Nova Indicação Prevista | Nenhuma predição disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✗ Não encontrado na base consultada (0 registros) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por Que Não Há Predições?

O pipeline TxGNN depende de três etapas encadeadas para gerar candidatos de reposicionamento: (1) mapeamento do fármaco ao identificador DrugBank, (2) localização do nó correspondente no grafo de conhecimento e (3) propagação de score pelo modelo de aprendizado profundo. Neste caso, o campo `drugbank_id` está ausente e o mecanismo de ação (MOA) não foi recuperado, o que impede o modelo de posicionar o fármaco no grafo e calcular qualquer pontuação.

Ampicillin Sódico é o sal sódico da ampicilina, enquanto o grafo TxGNN tipicamente indexa o composto-pai pela forma de base livre (ampicillin, DrugBank DB00415). A discrepância de nomenclatura entre o nome submetido ("AMPICILLIN SODIUM") e o identificador canônico no DrugBank pode explicar o resultado `success / 0 registros` na consulta ANVISA e a ausência de mapeamento automático. Uma re-submissão usando o nome INN simplificado **ampicillin** ou o DrugBank ID `DB00415` provavelmente resolverá o problema.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não produziu nenhuma predição de reposicionamento para este fármaco no ciclo atual, muito provavelmente devido a falha de mapeamento de nomenclatura (sal sódico vs. base livre) que impediu a localização do nó no grafo de conhecimento. Não há base de evidências computacionais para avançar neste momento.

**Para prosseguir, é necessário:**
- **Resolver o mapeamento DrugBank**: Re-submeter a consulta com o nome INN canônico `ampicillin` ou com o ID `DB00415` para localizar corretamente o nó no grafo TxGNN
- **Re-executar o pipeline de predição** após confirmação do mapeamento, a fim de obter scores TxGNN válidos
- **Consultar ANVISA diretamente**: Verificar se há registros sob variações do nome (ampicilina, ampicillin trihydrate, ampicillin sodium) para atualizar o campo `market_status`
- **Recuperar MOA e dados de segurança**: Preencher mecanismo de ação via DrugBank API (`DB00415`) e obter advertências/contraindicações da bula ANVISA para viabilizar a análise de segurança da fase S1
---

