---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

O skill confirma o contexto TxGNN. Prossigo com a geração do relatório baseado no Evidence Pack, seguindo o formato v5 especificado.

---

# Topiramate: Da Epilepsia à Neoplasia do Nervo Trigêmeo

## Resumo em Uma Frase

Topiramate é um antiepiléptico de segunda geração de amplo espectro, reconhecido pelo tratamento de crises epilépticas parciais e generalizadas e pela prevenção de enxaqueca.
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)**, porém atualmente **nenhum ensaio clínico nem publicação científica** sustenta diretamente esta direção terapêutica.
O alto score preditivo (99,70%) é interpretado pelo próprio sistema como artefato de proximidade no grafo de conhecimento, sem respaldo clínico ou mecanístico direto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Epilepsia (crises parciais e generalizadas) e prevenção de enxaqueca |
| Nova Indicação Prevista | Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais de mecanismo de ação disponíveis no Evidence Pack. Com base nas informações conhecidas na literatura científica, o topiramate é uma sulfonamida derivada da D-frutose estruturalmente única entre os antiepilépticos, com perfil de ação multifacetado: (1) bloqueio de canais de Na⁺ voltagem-dependentes, suprimindo disparos repetitivos de alta frequência; (2) potenciação da inibição mediada pelo receptor GABA-A; (3) antagonismo dos receptores AMPA/kainato do glutamato, reduzindo a transmissão excitatória; (4) inibição da anidrase carbônica. Esses mecanismos justificam sua eficácia estabelecida em epilepsia focal e generalizada e na prevenção de enxaqueca.

A neoplasia do nervo trigêmeo é uma condição essencialmente oncológica — tumor primário ou secundário que compromete o quinto nervo craniano — cujo manejo requer intervenção cirúrgica, radioterapia e/ou quimioterapia específica. O mecanismo antiepiléptico do topiramate não possui relação direta com a biologia tumoral desta neoplasia: o bloqueio de canais iônicos pode ter relevância sintomática na neuralgia do trigêmeo, mas não no controle do crescimento ou progressão tumoral.

O alto score do TxGNN (0,997) para esta indicação é atribuído pelo próprio sistema de análise a um **efeito de proximidade no grafo de conhecimento** (*graph proximity artifact*): o nó "nervo trigêmeo" compartilha vizinhança estrutural com nós de canalopatias e epilepsia no grafo, inflacionando artificialmente a pontuação sem implicação terapêutica real. Não existe qualquer evidência pré-clínica ou clínica que sustente esta previsão, e a lógica mecanística não oferece base para seu desenvolvimento clínico como indicação oncológica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há nenhuma evidência clínica ou pré-clínica que suporte o uso de topiramate para neoplasia do nervo trigêmeo; o score elevado do TxGNN é interpretado como artefato de proximidade no grafo de conhecimento, e a natureza oncológica da condição diverge fundamentalmente do mecanismo antiepiléptico do fármaco.

**Para prosseguir, é necessário:**
- Revisão crítica do nó "trigeminal nerve neoplasm" no grafo TxGNN para identificar e mitigar artefatos de proximidade antes de qualquer avaliação clínica
- Obtenção de dados completos de mecanismo de ação via DrugBank API (DG002)
- Download e análise da bula disponível em agência regulatória de referência para preenchimento das lacunas de segurança (DG001)
- Caso haja interesse terapêutico sintomático (controle de neuralgia do trigêmeo associada ao tumor), redefinir a indicação alvo como "neuralgia do trigêmeo" para uma busca de evidências mais específica e clinicamente relevante
- Verificar possibilidade de registro do fármaco na ANVISA, dado que nenhum registro ativo foi encontrado no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

