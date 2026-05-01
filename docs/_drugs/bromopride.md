---
layout: default
title: Bromopride
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 0
---

# Bromopride
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

# Bromopride: Avaliação de Reposicionamento — Sem Previsões Identificadas

## Resumo em Uma Frase

Bromopride (DB09018) é um fármaco da classe das benzamidas substituídas, utilizado como procinético e antiemético. O modelo TxGNN **não gerou nenhuma previsão de nova indicação** para este fármaco, e **não foram identificados ensaios clínicos ou publicações** que sustentem um cenário de reposicionamento. A avaliação permanece em estágio preliminar, com lacunas de dados críticas a serem resolvidas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (apenas dados de base, sem previsões) |
| Situação no Mercado | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsões?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) de Bromopride registrados no Evidence Pack. Bromopride é conhecido como um antagonista do receptor dopaminérgico D2, pertencente à classe das benzamidas substituídas (análogo estrutural da metoclopramida), utilizado clinicamente como procinético gastrointestinal e antiemético.

A ausência de previsões do TxGNN pode estar relacionada a dois fatores principais:

1. **Cobertura do grafo de conhecimento (KG):** O mapeamento de Bromopride ao DrugBank (DB09018) foi bem-sucedido, porém o fármaco pode não possuir ligações suficientes no grafo de conhecimento do TxGNN para gerar pontuações de reposicionamento significativas.

2. **Ausência no mercado regulatório avaliado:** Com zero registros na base de dados regulatória consultada, o fármaco não possui indicações aprovadas documentadas que sirvam como âncora para a predição de novas indicações.

---

## Considerações de Segurança

> Consulte a bula para informações de segurança. Os dados de advertências, contraindicações e interações medicamentosas não estão disponíveis no Evidence Pack atual.

---

## Lacunas de Dados Identificadas

| ID | Categoria | Item em Falta | Severidade | Impacto | Fonte para Remediação |
|----|-----------|---------------|------------|---------|----------------------|
| DG001 | Nível do Fármaco | Advertências e contraindicações da bula | **Bloqueante** | Impede a avaliação inicial de segurança (S1) | Órgão regulatório — download e análise da bula em PDF |
| DG002 | Nível do Fármaco | Mecanismo de Ação (MOA) | Alta | Compromete a análise de correlação mecanística | DrugBank — consulta via API |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para Bromopride, e existem lacunas de dados de severidade bloqueante (advertências/contraindicações da bula) que impedem a avaliação de segurança. Sem previsões e sem dados de segurança, não há base para avançar neste momento.

**Para prosseguir, é necessário:**
- Resolver a lacuna **DG001** (Bloqueante): obter e analisar a bula oficial junto ao órgão regulatório para extrair advertências e contraindicações
- Resolver a lacuna **DG002** (Alta): consultar a API do DrugBank para obter o mecanismo de ação detalhado
- Investigar por que o TxGNN não gerou previsões — verificar a conectividade de DB09018 no grafo de conhecimento (node.csv / kg.csv)
- Avaliar se o fármaco possui indicações aprovadas em outros países (ex.: Brasil/ANVISA, Itália/AIFA) que possam servir como âncora para uma nova rodada de predição
- Considerar a inclusão manual de relações fármaco–doença no KG, caso Bromopride tenha indicações documentadas não capturadas pelo grafo atual
---

