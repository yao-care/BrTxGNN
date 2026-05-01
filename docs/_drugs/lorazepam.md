---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

---

# Lorazepam: Da ansiedade e sedação ao neoplasma do nervo trigêmeo

## Resumo em Uma Frase

Lorazepam é um benzodiazepínico clássico utilizado há décadas no tratamento de ansiedade, insônia e sedação pré-operatória, com ampla presença no mercado brasileiro. O modelo TxGNN prevê que pode ser eficaz para **Neoplasma do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)** como previsão de maior pontuação — porém atualmente **sem nenhum ensaio clínico nem publicação** apoiando diretamente esta direção terapêutica. A ausência total de evidências clínicas e a ausência de mecanismo antineoplásico plausível resultam na recomendação de suspensão da avaliação neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|---------|
| Indicação Original | Ansiedade, insônia e sedação (benzodiazepínico clássico) |
| Nova Indicação Prevista | Neoplasma do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Lorazepam pertence à classe dos benzodiazepínicos e atua como modulador alostérico positivo dos receptores GABA-A no sistema nervoso central. Seu mecanismo aumenta a frequência de abertura dos canais de cloro, promovendo hiperpolarização neuronal e produzindo efeitos ansiolítico, sedativo-hipnótico, anticonvulsivante e relaxante muscular. Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack — os dados completos de MOA devem ser consultados via DrugBank (DB00186).

O neoplasma do nervo trigêmeo é uma neoplasia rara do sistema nervoso periférico. Em oncologia, lorazepam é utilizado de forma paliativa — para controle de ansiedade, agitação e náuseas induzidas por quimioterapia —, mas não possui ação antineoplásica direta sobre células tumorais. Não existe mecanismo biológico conhecido que sustente seu uso como agente terapêutico direto para este tipo de tumor.

A alta pontuação do TxGNN (99,87%) provavelmente reflete uma conexão indireta no grafo de conhecimento entre nós de "tumores neurais" e "fármacos do sistema nervoso central", ou resulta de ruído nos dados de treinamento do modelo. A ausência completa de ensaios clínicos e publicações sobre este uso específico confirma que esta previsão não possui embasamento clínico ou mecanístico sólido no momento atual, e a elevada pontuação não deve ser interpretada como sinal de eficácia terapêutica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Lorazepam possui **20 registros ativos** no Brasil (situação: comercializado). Os detalhes individuais dos registros — número, nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis nesta versão do Evidence Pack. Consulte diretamente o sistema de busca de medicamentos da **ANVISA** para acesso às informações completas de cada produto.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe nenhum ensaio clínico, publicação científica ou mecanismo de ação plausível que suporte o uso de lorazepam como agente terapêutico para neoplasma do nervo trigêmeo. A alta pontuação TxGNN (99,87%) é quase certamente um artefato de conectividade no grafo de conhecimento, sem relevância clínica translacional no momento atual.

**Para prosseguir, seria necessário:**
- Identificar qualquer base mecanística que ligue a modulação GABA-A à biologia do neoplasma do nervo trigêmeo
- Conduzir estudos pré-clínicos em modelos de schwannoma ou meningioma trigeminal
- Obter dados completos de MOA e perfil de segurança via bula oficial (ANVISA) e DrugBank
- Considerar a avaliação das indicações previstas com evidência mais robusta neste perfil — notadamente **insônia** (Rank 2, Nível L2, Proceed with Guardrails) e **epilepsias reflexas** (Ranks 3–8, Nível L4, Research Question), que apresentam suporte mecanístico direto pela modulação GABA-A
---

