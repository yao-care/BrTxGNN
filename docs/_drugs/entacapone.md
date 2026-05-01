---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Entacapone: De Parkinson à Neurodegeneração Associada a PLA2G6

## Resumo em Uma Frase

Entacapone é um inibidor de COMT (Catecol-O-metiltransferase), utilizado como terapia adjuvante da levodopa no tratamento da doença de Parkinson.
O modelo TxGNN prevê que pode ser eficaz para **Neurodegeneração Associada a PLA2G6 (PLA2G6-associated neurodegeneration)**,
atualmente **sem ensaios clínicos** e **sem publicações** apoiando diretamente esta direção. A previsão baseia-se exclusivamente no modelo de grafos de conhecimento, sem validação experimental disponível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson (terapia adjuvante da levodopa) |
| Nova Indicação Prevista | Neurodegeneração Associada a PLA2G6 (PLA2G6-associated neurodegeneration) |
| Pontuação de Previsão TxGNN | 99,76% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados no sistema. Segundo informações farmacológicas conhecidas, Entacapone é um inibidor periférico seletivo e reversível da COMT, enzima responsável pela degradação da levodopa antes que ela atravesse a barreira hematoencefálica. Ao bloquear a COMT, Entacapone prolonga a meia-vida plasmática da levodopa e aumenta a disponibilidade de dopamina no sistema nigroestriatal — este é o mecanismo central de sua eficácia na doença de Parkinson.

A Neurodegeneração Associada a PLA2G6 (PLAN) é causada por mutações no gene PLA2G6, que codifica uma fosfolipase independente de cálcio (iPLA2β). A deficiência dessa enzima leva ao acúmulo de lisofosfolipídeos na membrana neuronal, causando disfunção mitocondrial e morte neuronal progressiva. O subtipo PLAN Type III (também conhecido como PARK14) apresenta características parkinsonianas marcantes — incluindo perda de neurônios dopaminérgicos na substância negra — criando uma sobreposição patológica significativa com a doença de Parkinson clássica.

A lógica do modelo TxGNN apoia-se nessa sobreposição: se PLAN Type III envolve déficit dopaminérgico análogo ao Parkinson, inibir a COMT poderia, em tese, potencializar a via dopaminérgica residual. No entanto, conforme explicitado no próprio Evidence Pack, esta conexão mecanística é **puramente inferencial** — a lógica é plausível, mas sem evidência bioquímica direta, estudos pré-clínicos ou ensaios clínicos que a confirmem nesta condição específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Entacapone não possui registro na ANVISA e não é comercializado no Brasil.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para PLAN baseia-se exclusivamente em inferência por grafos de conhecimento (L5, Decisão S0), sem suporte de ensaios clínicos ou literatura científica específica. A conexão mecanística, embora biologicamente plausível para o subtipo parkinsoniano (PLAN Type III), permanece especulativa.

**Para prosseguir, é necessário:**
- Confirmar presença e extensão do déficit dopaminérgico documentado em pacientes com PLAN Type III através de revisão da literatura especializada
- Buscar modelos pré-clínicos (murinos ou in vitro) de PLA2G6 para testes de prova de conceito com COMT inibidores
- Obter dados completos de mecanismo de ação via DrugBank API (DG002)
- Obter informações de segurança e contraindicações via bula oficial (DG001)
- Regularizar situação regulatória no Brasil (nenhum registro ANVISA encontrado)

> **Nota sobre outras indicações avaliadas neste pacote:** O Evidence Pack é do tipo *multi*, cobrindo 10 indicações previstas. Entre elas, **Demência com Corpos de Lewy** (Rank 7, score 99,25%) apresenta o maior suporte evidencial disponível — 1 ensaio clínico e 3 publicações (Nível L4, Research Question) — e pode ser o candidato mais promissor para próximas etapas de pesquisa neste fármaco.
---

