---
layout: default
title: Orphenadrine Citrate
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 0
---

# Orphenadrine Citrate
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

# Orphenadrine Citrate: Relaxante Muscular Sem Indicações de Reposicionamento Previstas pelo TxGNN

---

## Resumo em Uma Frase

Orphenadrine citrate é um fármaco relaxante muscular de ação central com propriedades anticolinérgicas, historicamente utilizado no alívio de espasmos musculares associados a condições musculoesqueléticas agudas e como adjuvante no tratamento da doença de Parkinson.
O modelo TxGNN **não gerou nenhuma previsão de nova indicação** para este fármaco no ciclo atual de análise.
Adicionalmente, o fármaco **não possui registros ativos no Brasil**, e os dados de segurança e mecanismo de ação não estão disponíveis neste pacote de evidências, o que inviabiliza uma avaliação completa.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Espasmos musculares / Doença de Parkinson (uso histórico internacional; sem registro no Brasil) |
| Nova Indicação Prevista | Nenhuma — TxGNN não gerou previsões para este fármaco |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Insuficiente (abaixo de L5 — sem previsão gerada) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não gerou nenhuma indicação de reposicionamento para orphenadrine citrate neste ciclo, e o fármaco não possui qualquer registro ativo na ANVISA. A combinação de ausência de previsão, falta de dados de mecanismo de ação e lacunas nas informações de segurança impede qualquer avaliação de viabilidade clínica ou regulatória no momento.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) via consulta à API do DrugBank — pendente resolução do Data Gap DG002
- Baixar e analisar a bula TFDA para mapear advertências e contraindicações — pendente resolução do Data Gap DG001 (bloqueante)
- Investigar junto à equipe de modelagem por que o TxGNN não gerou previsões para este fármaco (possível ausência do nó no grafo de conhecimento ou baixa conectividade)
- Avaliar se há interesse regulatório em solicitar registro na ANVISA antes de iniciar qualquer análise de reposicionamento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

