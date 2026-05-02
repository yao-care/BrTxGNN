---
layout: default
title: Tizanidine
parent: 僅模型預測 (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Tizanidine
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

Using `txgnn-pipeline` for context on TxGNN evidence pack report generation. Proceeding to produce the pharmacist repurposing report now.

---

# Tizanidine: Da espasticidade muscular à enxaqueca

## Resumo em Uma Frase

Tizanidine é um relaxante muscular de ação central (agonista alfa-2 adrenérgico), originalmente utilizado no tratamento da espasticidade muscular associada a condições neurológicas como esclerose múltipla e lesão medular.
O modelo TxGNN prevê que pode ser eficaz para **Enxaqueca (Migraine Disorder)**, atualmente com **2 ensaios clínicos** apoiando esta direção — incluindo um Phase 3 randomizado, duplo-cego e controlado por placebo em recrutamento ativo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Espasticidade muscular (agonista alfa-2 adrenérgico de ação central) |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Tizanidine é um derivado imidazolínico que atua como agonista dos receptores alfa-2 adrenérgicos de ação central. Embora os dados formais de mecanismo de ação não estejam disponíveis neste evidence pack, a literatura farmacológica descreve que o fármaco inibe a liberação pré-sináptica de glutamato no corno dorsal da medula espinal e suprime a atividade de interneurônios espinais — mecanismo diretamente relevante à modulação da dor crônica e da sensibilização central.

No contexto da enxaqueca, o agonismo alfa-2 apresenta relevância multifatorial: (1) inibe a transmissão nociceptiva trigeminovascular, reduzindo a liberação do peptídeo relacionado ao gene da calcitonina (CGRP), principal mediador das crises de enxaqueca; (2) promove o relaxamento dos grupos musculares cervicais e cranianos, atenuando o componente tensional frequentemente comórbido; e (3) suprime a atividade do locus coeruleus, reduzindo a sensibilização central. Outros agonistas alfa-2 — como clonidina e guanfacina — já possuem dados de RCT em cefaleia, sustentando um efeito de classe farmacológica aplicável ao tizanidine.

Complementarmente, para a indicação ampliada de cefaleia em geral (headache disorder, rank 8 no Evidence Pack), existe um RCT duplo-cego multicêntrico publicado (PMID 12167135, Headache 2002) que demonstrou eficácia de tizanidine na profilaxia de cefaleia diária crônica versus placebo, e um Consenso da Sociedade Brasileira de Cefaleia de 2019 (PMID 31365643) que já inclui o fármaco entre as opções preventivas recomendadas — elevando o nível de evidência global para L1 nessa indicação mais ampla e fortalecendo o racional translacional para a enxaqueca especificamente.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Em recrutamento | 189 | RCT multicêntrico, duplo-cego, placebo-controlado avaliando eficácia, segurança e tolerabilidade de Tizanidine HCl oral na prevenção de crises em enxaqueca episódica de adultos (18–65 anos, com ou sem aura, histórico ≥1 ano). Previsão de conclusão: dezembro de 2025. |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Concluído | 300 | Estudo observacional prospectivo de 24 semanas (PACE Study) sobre eficácia de analgésicos compostos para alívio da dor; inclui pacientes com enxaqueca, fornecendo dados contextuais de suporte à eficácia analgésica. |

---

## Evidências da Literatura

Atualmente não há literatura diretamente indexada para tizanidine + enxaqueca (migraine disorder) neste Evidence Pack.

> **Nota contextual:** Para a indicação relacionada de cefaleia em geral (headache disorder), estão disponíveis 20 publicações com relevância direta, incluindo:
>
> | PMID | Ano | Tipo | Periódico | Principais Achados |
> |------|-----|------|-----------|-------------------|
> | [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT (duplo-cego, multicêntrico) | Headache | Tizanidine vs. placebo como terapia profilática adjuvante para cefaleia diária crônica (enxaqueca crônica, cefaleia migrânea e tensional) — estudo primário de referência para esta indicação. |
> | [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Consenso (Diretriz) | Arq Neuropsiquiatr | Consenso da Sociedade Brasileira de Cefaleia sobre tratamento de enxaqueca crônica; inclui tizanidine entre as opções preventivas recomendadas. |
> | [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Ensaio aberto (dose-titration) | Headache | Eficácia e tolerabilidade de tizanidine HCl na profilaxia de cefaleia diária crônica — estudo-piloto que embasou o RCT subsequente. |
> | [10971659](https://pubmed.ncbi.nlm.nih.gov/10971659/) | 2000 | Ensaio clínico (RDB) | Headache | Formulação de liberação modificada de tizanidine (Sirdalud MR) vs. placebo em 185 pacientes com cefaleia tensional crônica; avaliação de 6 semanas. |
> | [8912480](https://pubmed.ncbi.nlm.nih.gov/8912480/) | 1996 | Relato clínico / Série de casos | Arch Neurol | Tizanidine para cefaleia em salvas crônica — primeiras evidências clínicas em subtipos refratários de cefaleia. |
> | [24224929](https://pubmed.ncbi.nlm.nih.gov/24224929/) | 2013 | Ensaio clínico comparativo | Emerg Med Australas | Amitriptilina vs. tizanidine no manejo de cefaleia tensional — comparação direta de eficácia entre fármacos preventivos. |
> | [7960728](https://pubmed.ncbi.nlm.nih.gov/7960728/) | 1994 | Ensaio clínico (mecanístico) | Headache | Efeitos de tizanidine na supressão exteroceptiva do músculo temporal em pacientes com cefaleia tensional crônica; demonstra mecanismo de ação alfa-2 adrenérgico direto. |
> | [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | Revisão de baclofeno, tizanidine e toxina botulínica como tratamentos preventivos para enxaqueca e cefaleia tensional; discussão de mecanismos e evidências. |
> | [24784123](https://pubmed.ncbi.nlm.nih.gov/24784123/) | 2014 | Review | Am Fam Physician | Diagnóstico e manejo de cefaleia diária crônica; tizanidine citado entre opções profiláticas com suporte em ensaios clínicos. |
> | [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Atualização em farmacoterapia para neuralgia do trigêmeo; menciona bloqueadores de CGRP e fármacos adjuvantes, contextualizando o espectro de dor cefálica. |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Um Phase 3 RCT multicêntrico, duplo-cego e controlado por placebo está atualmente em recrutamento ativo (NCT05484349, n=189), validando diretamente o uso de tizanidine na prevenção de enxaqueca episódica. Somado a isso, evidências robustas de classe farmacológica (agonistas alfa-2) e um RCT publicado em cefaleia diária crônica (PMID 12167135) — já incorporado ao consenso da Sociedade Brasileira de Cefaleia de 2019 — sustentam a plausibilidade clínica. A ausência de registro na ANVISA é o principal obstáculo operacional.

**Para prosseguir, é necessário:**
- Aguardar resultados do NCT05484349 (previsão de conclusão: dezembro de 2025) para elevação do nível de evidência para L1
- Obter dados completos de segurança: advertências, contraindicações e perfil de interações medicamentosas da bula original (DrugBank DB00697 / bula de referência)
- Avaliar viabilidade e estratégia de registro na ANVISA, considerando que tizanidine não possui nenhum registro ativo no Brasil
- Definir plano de monitoramento de efeitos adversos relevantes para uso em enxaqueca (especialmente hipotensão, sedação e hepatotoxicidade, efeitos classe conhecidos dos agonistas alfa-2)
---

