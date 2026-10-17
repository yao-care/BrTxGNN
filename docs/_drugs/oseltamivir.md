---
layout: default
title: Oseltamivir
parent: Apenas Predição do Modelo (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Oseltamivir: nova indicação prevista, Pneumonia (Pneumonia)… (nível de evidência L5). Indicação original: Influenza"
monitor_inn: "Oseltamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "disorder of phenylalanine metabolism", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "staphylococcus aureus infection", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency", "pneumonia", "streptococcal pneumonia", "susceptibility to HIV infection"]
---

# Oseltamivir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

# Oseltamivir: Da influenza à pneumonia (associada à influenza)

## Resumo em Uma Frase

Oseltamivir é um inibidor da neuraminidase viral, originalmente usado no tratamento da influenza.
O modelo TxGNN prevê, em primeira posição, **Pielonefrite (Pyelonephritis)**, mas essa previsão não tem respaldo clínico. A direção com maior sustentação nos dados compilados é **Pneumonia (Pneumonia)**, restrita ao contexto de influenza, com **15 ensaios clínicos** e **20 publicações** apoiando essa direção.

> Observação: a indicação de maior pontuação (pielonefrite) não conta com ensaios clínicos nem mecanismo plausível. Por isso, este relatório destaca a pneumonia, a única previsão com evidência clínica relevante.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Influenza |
| Nova Indicação Prevista | Pneumonia (Pneumonia), na prática restrita à pneumonia associada à influenza |
| Pontuação de Previsão TxGNN | 92,14% (a previsão de maior pontuação, pielonefrite, tem 97,85%, mas sem evidência) |
| Nível de Evidência | L1 (ensaios de Phase 3 concluídos, porém com ressalvas quanto à especificidade para pneumonia) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

O oseltamivir inibe a neuraminidase viral, reduzindo a liberação e a disseminação do vírus influenza. Não há dados detalhados sobre o mecanismo de ação no material compilado, mas essa é a função conhecida da classe dos inibidores da neuraminidase.

A influenza é causa frequente de pneumonia viral e porta de entrada para pneumonia bacteriana secundária. Tratar o vírus precocemente pode, em teoria, reduzir a ocorrência e a gravidade da pneumonia. Estudos observacionais, como o retrospectivo no México com a pandemia de H1N1 de 2009, sugerem menor risco de pneumonia com oseltamivir administrado cedo.

O benefício é plausível apenas para a pneumonia associada à influenza. Em outras pneumonias virais, como a COVID-19, não há alvo de neuraminidase, e o oseltamivir aparece nos ensaios sobretudo como comparador ou terapia de base. A indicação não deve ser estendida à pneumonia em geral.

Outras previsões do modelo parecem artefatos de proximidade no grafo de conhecimento: pielonefrite (infecção bacteriana urinária), distúrbios do metabolismo da tirosina e da fenilalanina, síndrome de Pierre Robin teratogênica e suscetibilidade ao HIV não têm mecanismo plausível. As previsões para infecção por *Staphylococcus aureus* e pneumonia estreptocócica têm apenas ligação indireta, via coinfecção pós-influenza.

## Evidências de Ensaios Clínicos

Os ensaios abaixo estão ligados à previsão de pneumonia. Os mais relevantes para o oseltamivir estão no topo.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00707941](https://clinicaltrials.gov/study/NCT00707941) | Phase 3 | Concluído | 1190 | Eficácia do oseltamivir na duração da doença, na eliminação viral e na transmissão domiciliar da influenza em Dhaka (Bangladesh). Diretamente relevante ao mecanismo, mas pneumonia pode não ser o desfecho primário |
| [NCT01248715](https://clinicaltrials.gov/study/NCT01248715) | Phase 4 | Concluído | 1107 | Efetividade do tratamento antiviral empírico em pneumonia comunitária hospitalizada durante a temporada de influenza |
| [NCT00936013](https://clinicaltrials.gov/study/NCT00936013) | Phase 4 | Desconhecido | 400 | Oseltamivir combinado com ervas medicinais chinesas versus oseltamivir isolado em pneumonia por H1N1 |
| [NCT04558463](https://clinicaltrials.gov/study/NCT04558463) | Phase 3 | Desconhecido | 100 | Favipiravir versus oseltamivir como terapia adjuvante na COVID-19 (oseltamivir como comparador) |
| [NCT04973462](https://clinicaltrials.gov/study/NCT04973462) | Phase 4 | Desconhecido | 80 | Triazavirina versus oseltamivir na COVID-19 (oseltamivir como comparador) |
| [NCT04338698](https://clinicaltrials.gov/study/NCT04338698) | Phase 3 | Concluído | 550 | Hidroxicloroquina, oseltamivir e azitromicina, isolados e combinados, na COVID-19; oseltamivir sem alvo no SARS-CoV-2 |
| [NCT04255017](https://clinicaltrials.gov/study/NCT04255017) | Phase 4 | Desconhecido | 400 | Comparação de arbidol, oseltamivir e lopinavir/ritonavir na pneumonia por 2019-nCoV |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recrutando | 20000 | REMAP-CAP: plataforma adaptativa para pneumonia comunitária em terapia intensiva |
| [NCT04381936](https://clinicaltrials.gov/study/NCT04381936) | Phase 3 | Recrutando | 70000 | RECOVERY: avalia, entre vários tratamentos, oseltamivir e baloxavir na influenza hospitalizada |
| [NCT04516915](https://clinicaltrials.gov/study/NCT04516915) | Phase 2 | Concluído | 38 | IMU-838 associado a oseltamivir na COVID-19 (outro agente em estudo) |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24718923](https://pubmed.ncbi.nlm.nih.gov/24718923/) | 2014 | Revisão sistemática (Cochrane) | Cochrane Database Syst Rev | Inibidores da neuraminidase para prevenção e tratamento da influenza em adultos e crianças |
| [23082123](https://pubmed.ncbi.nlm.nih.gov/23082123/) | 2012 | RCT em clusters | PLoS One | Tratamento versus tratamento mais profilaxia com oseltamivir em surtos de influenza em casas de repouso |
| [36752709](https://pubmed.ncbi.nlm.nih.gov/36752709/) | 2023 | Revisão | Curr Opin Infect Dis | Revisão das terapias antivirais para influenza (inibidores da neuraminidase e baloxavir) |
| [40050867](https://pubmed.ncbi.nlm.nih.gov/40050867/) | 2025 | Revisão | Virol J | Antivirais para pneumonia viral, incluindo o oseltamivir |
| [21760915](https://pubmed.ncbi.nlm.nih.gov/21760915/) | 2011 | Retrospectivo | PLoS One | Oseltamivir precoce reduziu a ocorrência e a gravidade da pneumonia por H1N1 de 2009 no México |
| [15969875](https://pubmed.ncbi.nlm.nih.gov/15969875/) | 2005 | Observacional | Curr Med Res Opin | Risco de pneumonia e outras complicações da síndrome gripal em pacientes tratados com oseltamivir |
| [28480248](https://pubmed.ncbi.nlm.nih.gov/28480248/) | 2017 | Observacional | Open Forum Infect Dis | Uso de oseltamivir em crianças e adultos hospitalizados com pneumonia comunitária |
| [35993199](https://pubmed.ncbi.nlm.nih.gov/35993199/) | 2022 | Revisão | J Glob Health | Papel do oseltamivir e de outros tratamentos adjuvantes na pneumonia grave infantil em países de baixa e média renda |
| [15243927](https://pubmed.ncbi.nlm.nih.gov/15243927/) | 2004 | Pré-clínico (camundongos) | J Infect Dis | Oseltamivir elevou a sobrevida de 0% para 75% na pneumonia pneumocócica secundária à influenza |
| [12660947](https://pubmed.ncbi.nlm.nih.gov/12660947/) | 2003 | Pré-clínico (camundongos) | J Infect Dis | Oseltamivir melhorou a sobrevida no sinergismo letal entre influenza e *S. pneumoniae* |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento)**: *delirium* aparece como doença associada a contraindicação. Um relato de caso na literatura descreve "delirium induzido por oseltamivir" em paciente com pneumonia por H1N1 (PMID 21108186).
- **Interações Medicamentosas**: foram identificadas 66 interações potenciais, todas com nível de gravidade não classificado. Entre as listadas estão pantoprazol, vancomicina, lactulose, prednisona, sinvastatina, cloreto de potássio, claritromicina, morfina, metformina, omeprazol e ondansetrona.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Para pneumonia, há ensaios de Phase 3 concluídos com oseltamivir em influenza, além de estudos observacionais e pré-clínicos coerentes com o mecanismo. A evidência, porém, refere-se à doença influenza, não a desfechos específicos de pneumonia, e a indicação deve ficar restrita à pneumonia associada à influenza. As demais previsões (inclusive a de maior pontuação, pielonefrite) devem permanecer em **Hold**, por falta de mecanismo e de evidência.

**Para prosseguir, é necessário:**
- Verificar desfechos específicos de pneumonia nos ensaios de Phase 3 (por exemplo, NCT00707941) e em revisões sistemáticas.
- Obter dados detalhados do mecanismo de ação.
- Obter a bula oficial (advertências e contraindicações), pois esses dados de segurança não estavam disponíveis.
- Esclarecer a situação regulatória no Brasil, pois não há registro ativo no material compilado.
- Definir um plano de monitoramento de eventos neuropsiquiátricos, como o *delirium*, e de interações medicamentosas.
- Excluir da análise as previsões sem sustentação mecanística (pielonefrite, distúrbios metabólicos, síndrome de Pierre Robin teratogênica, HIV).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

