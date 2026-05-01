---
layout: default
title: Bendamustina Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 0
---

# Bendamustina Hydrochloride
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

# Bendamustina Hidrocloreto: Agente Alquilante — Avaliação Bloqueada por Ausência de Previsões TxGNN

## Resumo em Uma Frase

Bendamustina Hidrocloreto é um agente alquilante bifuncional utilizado no tratamento de leucemia linfocítica crônica e linfomas de células B. O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco neste ciclo de análise — provavelmente porque o DrugBank ID não foi mapeado com sucesso, inviabilizando a indexação no grafo de conhecimento. Com zero registros na ANVISA e sem indicações previstas, a avaliação completa está bloqueada neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil *(referência externa: leucemia linfocítica crônica, linfoma não Hodgkin de células B)* |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 (sem previsões geradas) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros (ANVISA) | 0 |
| Decisão Recomendada | **Hold** |

---

## Citotoxicidade

Bendamustina é classificada como agente antineoplásico alquilante — esta seção é exibida por critério de classe farmacológica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — agente alquilante bifuncional (mecloretamina + anel benzimidazólico com atividade análoga a purina) |
| Risco de Mielossupressão | **Alto** — neutropenia e trombocitopenia são toxicidades dose-limitantes conhecidas da classe |
| Classificação de Emetogenicidade | Média |
| Itens de Monitoramento | Hemograma completo com diferencial (CBC), função renal (creatinina), função hepática (ALT/AST/bilirrubinas) |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de citotóxicos (preparo em cabine de segurança biológica, EPI completo) |

> ⚠️ Os dados acima baseiam-se em conhecimento farmacológico externo da classe, pois o Evidence Pack não contém dados de toxicidade. Consulte a bula oficial para confirmação.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN nem dados regulatórios brasileiros — o DrugBank ID está ausente (retorno nulo mesmo com 1 resultado na consulta ao DrugBank), o que provavelmente impediu a indexação no grafo de conhecimento e a geração de candidatos de reposicionamento. Sem indicações previstas, não há base para avaliação de eficácia ou segurança na nova indicação.

**Para prosseguir, é necessário:**

- **Corrigir o mapeamento DrugBank**: Confirmar e registrar o DrugBank ID correto para Bendamustina Hidrocloreto *(referência externa provável: DB06769)* e reexecutar o pipeline TxGNN
- **Resolver lacuna de MOA (DG002)**: Consultar DrugBank API para obter mecanismo de ação detalhado — necessário para análise de relevância mecanicista
- **Verificar registro ANVISA**: Pesquisar se há registros ativos ou em tramitação no Brasil para compostos à base de bendamustina
- **Obter dados de segurança (DG001)**: Buscar informações de advertências e contraindicações na bula registrada em países onde o fármaco é comercializado (EUA: Treanda/Bendeka; Europa: Levact)
- **Reprocessar após correções**: Após saneamento dos dados, reiniciar a avaliação a partir da fase de previsão TxGNN
---

