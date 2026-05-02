---
layout: default
title: Tetracaine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 0
---

# Tetracaine Hydrochloride
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

# Tetracaine Hydrochloride: Avaliação de Reposicionamento — Previsões Indisponíveis

---

## Resumo em Uma Frase

Tetracaine Hydrochloride é um anestésico local da classe éster, utilizado classicamente em anestesia oftalmológica, raquianestesia e anestesia tópica de mucosas.
Nesta versão do pipeline, o modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco, e **nenhum registro ativo foi localizado na ANVISA**.
A ausência de dados preditivos, evidências clínicas e registro regulatório resulta em avaliação **Hold**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia local (dados de registros ANVISA não disponíveis) |
| Nova Indicação Prevista | Sem previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 (sem estudos reais associados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não gerou previsões de reposicionamento para Tetracaine Hydrochloride nesta execução, e o fármaco não possui registros ativos na ANVISA. Sem dados preditivos nem base regulatória brasileira estabelecida, não há substrato suficiente para avançar à avaliação clínica.

**Para prosseguir, é necessário:**
- Verificar se Tetracaine Hydrochloride consta no grafo de conhecimento TxGNN sob nome alternativo (ex.: *tetracaína*, *amethocaine*, *tetracaine*) e reprocessar a predição com o termo correto
- Obter o **DrugBank ID** correspondente para viabilizar o enriquecimento de MOA, categorias farmacológicas e dados de segurança estruturados
- Investigar registros na ANVISA sob sinônimos: **Tetracaína**, **Cloridrato de Tetracaína**, **Amethocaine Hydrochloride**
- Baixar a bula disponível no portal da ANVISA (caso exista produto registrado sob outro nome) para preencher advertências, contraindicações e interações medicamentosas
- Considerar re-execução do pipeline após correção do identificador do fármaco, pois a consulta ao DrugBank retornou 1 resultado (ver `query_log` id=3), indicando que o mapeamento pode ser recuperável
---

