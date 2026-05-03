---
layout: default
title: Testosterone Decanoate
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 0
---

# Testosterone Decanoate
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

# Testosterona Decanoato: Dados Insuficientes para Avaliação de Reposicionamento

## Resumo

Testosterona Decanoato é um éster de testosterona de ação prolongada, pertencente à classe dos androgênios e esteroides anabólicos, classicamente utilizado em terapias de reposição hormonal masculina (hipogonadismo). O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise — nenhuma nova indicação candidata foi identificada. A ausência de registro brasileiro e a indisponibilidade de dados de mecanismo de ação (MOA) e segurança limitam qualquer avaliação aprofundada neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não identificada nos dados disponíveis |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Informações de Comercialização no Brasil

Não há registros ativos de Testosterona Decanoato na ANVISA. A consulta realizada em 26/03/2026 retornou **zero resultados**, indicando que o fármaco não possui registro vigente como produto independente no Brasil.

> Observação: Testosterona Decanoato pode estar comercializada no Brasil como componente de combinações de ésteres de testosterona (ex.: Sustanon). Uma consulta específica por produto combinado pode ser necessária para esclarecer a situação regulatória real.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma previsão de reposicionamento para este fármaco no ciclo atual. A combinação de ausência de registro regulatório no Brasil, dados de mecanismo de ação indisponíveis e ausência de informações de segurança torna inviável qualquer análise de viabilidade clínica ou regulatória neste momento.

**Para prosseguir, é necessário:**
- Integrar os dados do DrugBank (consulta retornou 1 resultado em 26/03/2026, mas o conteúdo ainda não foi processado) para obter MOA, categorias terapêuticas e perfil de segurança
- Verificar se o fármaco está registrado na ANVISA como componente de formulações combinadas (ex.: misturas de ésteres de testosterona)
- Obter a bula oficial para extrair advertências, contraindicações e interações medicamentosas
- Reexecutar o pipeline TxGNN com o `drugbank_id` e dados de MOA completos para que o modelo possa gerar previsões de reposicionamento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

