---
layout: default
title: Biperiden Lactate
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 0
---

# Biperiden Lactate
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

# Biperiden Lactato: Avaliação Preliminar — Dados Insuficientes para Previsão de Reposicionamento

## Resumo

Biperiden Lactato é um fármaco anticolinérgico utilizado no tratamento da doença de Parkinson e de distúrbios extrapiramidais induzidos por medicamentos.
O Evidence Pack recebido **não contém previsões de novas indicações geradas pelo modelo TxGNN**, e o fármaco não possui registro ativo no Brasil, tornando inviável uma avaliação completa de reposicionamento neste momento.
Para avançar na análise, são necessários o processamento das previsões do modelo e a obtenção dos dados regulatórios e de segurança identificados como lacunas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson; distúrbios extrapiramidais induzidos por medicamentos |
| Nova Indicação Prevista | — (sem previsão disponível neste Evidence Pack) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem previsão do modelo nem estudos associados |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados de previsão disponíveis para este fármaco neste Evidence Pack, pois o campo `predicted_indications` está vazio. Portanto, não é possível analisar a relação entre indicação original e uma nova indicação sem que o modelo TxGNN gere previsões com base no perfil completo do fármaco.

Com base em informações farmacológicas conhecidas, Biperiden Lactato é um **antagonista muscarínico (anticolinérgico)** pertencente à classe dos antiparkinsonianos. Atua bloqueando receptores de acetilcolina do tipo muscarínico no sistema nervoso central e periférico, com indicações tradicionais para:

- Doença de Parkinson (formas idiopática, pós-encefalítica e arteriosclerótica)
- Distúrbios extrapiramidais induzidos por fármacos, como aqueles causados por antipsicóticos (neurolépticos)

O mecanismo de ação detalhado (MOA formal via DrugBank) foi identificado como lacuna de dados de alta prioridade e deverá ser obtido para análises subsequentes — a consulta ao DrugBank já retornou 1 resultado e os dados precisam ser processados e incorporados ao pack.

---

## Informações de Comercialização no Brasil

Biperiden Lactato **não possui registros ativos na ANVISA** conforme os dados consultados (data de corte: 05/04/2026). Nenhuma licença foi localizada sob esta denominação salina.

> **Nota importante:** O biperideno está disponível em alguns mercados sob a forma de **cloridrato de biperideno** (Biperiden HCl). Recomenda-se verificar se há registros ativos na ANVISA sob denominações alternativas antes de concluir pela ausência total do fármaco no mercado brasileiro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações pelo TxGNN, não há registros ANVISA ativos e os dados de segurança (advertências, contraindicações e interações) estão ausentes — condições que impossibilitam qualquer avaliação de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN para gerar previsões de novas indicações para Biperiden Lactato e popular o campo `predicted_indications`
- Processar o resultado já obtido do DrugBank (1 resultado retornado) e extrair MOA, categorias terapêuticas e dados de segurança
- Verificar registros ANVISA sob denominações alternativas (ex.: Biperideno, Biperiden Cloridrato, Biperiden HCl)
- Obter advertências e contraindicações via bula (ANVISA, FDA ou EMA) para preencher as lacunas de segurança classificadas como **Blocking (DG001)**
---

