---
layout: default
title: Tapentadol
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Tapentadol
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

Usando o skill `txgnn-pipeline` para orientar a geração do relatório de reposicionamento de fármacos TxGNN.

---

# Tapentadol: Da dor moderada a grave para o transtorno de enxaqueca

## Resumo em Uma Frase

Tapentadol é um analgésico opioide de nova geração com mecanismo dual — agonismo µ-opioide (MOR) e inibição da recaptação de noradrenalina (NRI) —, aprovado para o tratamento de dor moderada a grave, aguda e crônica.
O modelo TxGNN prevê que pode ser eficaz para o **Transtorno de Enxaqueca (Migraine Disorder)**, contudo atualmente há **0 ensaios clínicos** específicos e apenas **2 publicações** tangencialmente relacionadas apoiando esta direção.
A plausibilidade clínica desta previsão é muito baixa, configurando provável falso positivo do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dor moderada a grave (aguda e crônica) |
| Nova Indicação Prevista | Transtorno de Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações conhecidas, Tapentadol é um analgésico de ação central pertencente à classe dos opioides de nova geração, com mecanismo dual único: **agonista do receptor µ-opioide (MOR)** — responsável pela analgesia central clássica — e **inibidor da recaptação de noradrenalina (NRI)**, que potencializa o controle descendente da dor, especialmente em componentes neuropáticos. Esta dupla ação distingue-o dos opioides tradicionais (como morfina e oxicodona) e aproxima-o, em parte, dos antidepressivos SNRIs como duloxetina e venlafaxina.

A enxaqueca é uma condição neurovascular episódica complexa, cujos mecanismos centrais envolvem sensibilização do nervo trigêmio, liberação de peptídeo relacionado ao gene da calcitonina (CGRP), disfunção do sistema serotonérgico e ativação cortical. A alta pontuação computacional do TxGNN pode refletir sobreposições no grafo de conhecimento entre dor, cefaleia e receptores opioides, capturando associações estruturais sem validação clínica.

No entanto, existe uma **contraindicação mecanística crítica**: as principais diretrizes internacionais de neurologia (IHS, AAN, EHF) contra-indicam explicitamente o uso de opioides no tratamento da enxaqueca. O risco de **cefaleia por uso excessivo de medicamento (MOH — Medication Overuse Headache)** é elevado com opioides: o uso frequente paradoxalmente cronifica e agrava a cefaleia. Adicionalmente, o componente NRI não possui mecanismo protetor reconhecido para enxaqueca — diferentemente dos betabloqueadores, antiepilépticos ou antidepressivos tricíclicos usados na profilaxia. Esta previsão configura, portanto, um **provável falso positivo do modelo TxGNN**.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Cochrane Review | Cochrane Database Syst Rev | Revisão de dipirona (metamizol) para dor pós-operatória aguda; menciona enxaqueca como contexto de uso da dipirona — não avalia Tapentadol |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Cochrane Review | Cochrane Database Syst Rev | Sumatriptano + naproxeno para enxaqueca aguda em adultos; estudo de referência sobre tratamento da enxaqueca com triptanos e AINEs — não relacionado a Tapentadol |

> **Nota importante**: Nenhuma das publicações identificadas avalia Tapentadol para o tratamento de enxaqueca. Ambas tratam de outros fármacos, e a associação com Tapentadol é apenas contextual via termos de busca. A ausência de literatura direta confirma o nível de evidência L5.

---

## Informações de Comercialização no Brasil

O fármaco possui **4 registros** ativos na ANVISA, confirmando sua comercialização no mercado brasileiro. Os detalhes individuais dos registros (números de registro, nomes comerciais, formas farmacêuticas e indicações aprovadas) não foram recuperados neste Evidence Pack e devem ser consultados diretamente no [portal de consulta da ANVISA](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da alta pontuação computacional do TxGNN (99,67%), não há nenhum ensaio clínico específico para esta indicação, e a base mecanística é **ativamente desfavorável**: opioides são desaconselhados pelas diretrizes internacionais para enxaqueca pelo alto risco de MOH, e o componente NRI não possui eficácia estabelecida para cefaleia primária. Esta previsão representa um provável artefato do modelo — a alta pontuação decorre de sobreposições genéricas no grafo de conhecimento entre dor e cefaleia, não de uma relação farmacológica real.

**Para prosseguir com qualquer investigação, seria necessário:**
- Evidência pré-clínica demonstrando efeito específico de Tapentadol em modelos animais de enxaqueca (ex.: modelo de estimulação do gânglio trigeminal ou modelo de depressão alastrante cortical)
- Hipótese mecanística que explique como MOR/NRI poderia modular a cascata do CGRP ou a sensibilização central trigeminal sem induzir MOH
- Dados de farmacovigilância ou coortes retrospectivas de pacientes com enxaqueca que usaram Tapentadol para dor comórbida

> **Nota sobre outras previsões do modelo**: Das 10 indicações previstas neste Evidence Pack, aquelas com melhor relação evidência/mecanismo incluem **insônia** (rank 6, L3, 6 ensaios clínicos indiretos) e **ansiedade** (rank 10, L4, 7 ensaios e 19 publicações), onde o componente NRI apresenta sobreposição com antidepressivos SNRI — indicações mais adequadas para investigação futura comparadas ao transtorno de enxaqueca.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

