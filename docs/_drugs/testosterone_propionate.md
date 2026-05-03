---
layout: default
title: Testosterone Propionate
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 0
---

# Testosterone Propionate
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

# Propionato de Testosterona: Sem Previsões de Reposicionamento Disponíveis

## Resumo

Propionato de Testosterona (Testosterone Propionate) é um éster de testosterona de ação curta, pertencente à classe dos androgênios/esteroides anabólicos, historicamente utilizado em reposição hormonal e tratamento de hipogonadismo masculino.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco na rodada atual de análise.
Há lacunas críticas de dados — incluindo ausência de MOA e de registros regulatórios — que limitam a capacidade preditiva do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrada neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que não há previsões?

O modelo TxGNN não identificou candidatos de reposicionamento para o Propionato de Testosterona nesta rodada. As razões prováveis são:

**Ausência de mecanismo de ação (MOA):** O mecanismo de ação não está disponível neste Evidence Pack (Data Gap DG002). O MOA é um insumo importante para o mapeamento no grafo de conhecimento do TxGNN — sem ele, as conexões entre o fármaco e potenciais novas indicações ficam comprometidas.

**Ausência de registros regulatórios:** O fármaco não possui registros ativos no Brasil, o que elimina a possibilidade de usar indicações aprovadas como ponto de partida para o modelo. A combinação de MOA ausente com indicações originais não registradas resulta em um nó de baixa conectividade no grafo.

**Contexto histórico do fármaco:** O Propionato de Testosterona é um éster de ação curta com uso clínico consolidado em reposição hormonal masculina, hipogonadismo e — em contextos terapêuticos mais antigos — no tratamento paliativo de carcinoma mamário avançado em mulheres pós-menopáusicas. Sua aplicação foi amplamente substituída por formulações de ação prolongada (cipionato, enantato) e por novas terapias. Esse perfil "maduro" pode reduzir a geração de previsões novas pelo modelo.

---

## Informações de Comercialização no Brasil

Este fármaco **não possui registro ativo no Brasil**. A consulta ao banco de dados regulatório não retornou nenhuma licença registrada para Propionato de Testosterona.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para este fármaco, e dois Data Gaps críticos — ausência de MOA (severidade Alta) e ausência de advertências/contraindicações (severidade Bloqueante) — impedem qualquer avaliação de viabilidade ou segurança neste momento.

**Para prosseguir, é necessário:**
- Consultar a DrugBank API para obter o mecanismo de ação completo (DrugBank ID: DB01420) — resolve DG002
- Baixar e analisar a bula oficial na fonte regulatória competente para advertências e contraindicações — resolve DG001
- Verificar registros em outras jurisdições (FDA, EMA, ANVISA) para identificar indicações aprovadas que possam alimentar o modelo
- Re-executar o pipeline TxGNN com os dados complementados para verificar se novas previsões emergem
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

