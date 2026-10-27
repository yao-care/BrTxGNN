---
layout: default
title: Ticagrelor
parent: Apenas Predição do Modelo (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ticagrelor: nova indicação prevista, Arteriosclerose Intracraniana (Intracranial Arteriosclerosis) (nível de evidência L5). Indicação original: Síndrome coronariana aguda (e doença vascular periféric…"
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
---

# Ticagrelor
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

## Ticagrelor: Da síndrome coronariana aguda à arteriosclerose intracraniana
{: .text-alpha }

## Resumo em Uma Frase

Ticagrelor é um antiagregante plaquetário que inibe de forma reversível o receptor P2Y12, originalmente usado no tratamento da síndrome coronariana aguda e de doenças vasculares periféricas.
O modelo TxGNN prevê que pode ser eficaz para **Arteriosclerose Intracraniana (Intracranial Arteriosclerosis)**,
atualmente com **2 ensaios clínicos** e **2 publicações** diretamente associados a esta direção, ainda sem resultados conclusivos.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Síndrome coronariana aguda (e doença vascular periférica, claudicação intermitente, doença arterial periférica, segundo o grafo de conhecimento) |
| Nova Indicação Prevista | Arteriosclerose Intracraniana (Intracranial Arteriosclerosis) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L2 (limitado: o único ensaio de Phase 3 ainda está em andamento e não tem resultados; ver nota abaixo) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

> Nota: o nível L2 segue a classificação dos dados compilados. Em termos estritos, o ensaio de Phase 3 (CAPTIVA) ainda não foi concluído, de modo que a evidência direta para esta indicação é, na prática, inferior ao previsto para L2.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base consultada. Segundo informações conhecidas, o ticagrelor é um inibidor reversível do receptor plaquetário P2Y12, reduzindo a agregação plaquetária e os eventos trombóticos. Diferentemente do clopidogrel, não depende de ativação pela enzima CYP2C19.

A estenose aterosclerótica intracraniana sintomática envolve trombose mediada por plaquetas e embolia artéria-artéria. Como o ticagrelor já é usado em doença aterosclerótica coronariana (síndrome coronariana aguda), é mecanisticamente plausível estender o uso à circulação cerebral.

A ausência de dependência de CYP2C19 é uma vantagem potencial em pacientes com perda de função desta enzima, que respondem mal ao clopidogrel. O ensaio CHANCE-2 (publicado no NEJM, em AVC/AIT) apoia essa lógica em doença cerebrovascular de forma mais ampla.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Ativo, sem recrutamento | 1683 | CAPTIVA: avalia se rivaroxabana, ticagrelor ou ambos são superiores ao clopidogrel na redução de AVC isquêmico, hemorragia intracerebral ou morte vascular em 1 ano. Sem resultados ainda. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recrutando | 100 | Estudo piloto de seleção de inibidor de P2Y12 guiada por genótipo (inclui ticagrelor) versus clopidogrel em doença aterosclerótica intracraniana sintomática. Sem resultados ainda. |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Coorte | Journal of NeuroInterventional Surgery | Experiência com ticagrelor 60 mg duas vezes ao dia + AAS 81 mg versus AAS + clopidogrel em stent intracraniano |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Revisão | International Journal of Stroke | Desenho e progresso inicial do ensaio CAPTIVA em estenose aterosclerótica intracraniana |

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não texto de bula)**: insuficiência hepática, doença hepática, doença da vesícula biliar e hemorragia intracraniana. A hemorragia intracraniana é particularmente relevante para a nova indicação cerebrovascular.
- **Interações Medicamentosas**: foram identificadas 100 interações; as principais incluem:
  - **Grave**: claritromicina.
  - **Moderada**: ácido acetilsalicílico, morfina, aprepitanto, dexametasona, budesonida, sinvastatina, saxagliptina, miconazol, cisaprida, clotrimazol, entre outros.
  - **Leve**: naloxegol, prucaloprida.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- A previsão é mecanisticamente plausível e há um ensaio de Phase 3 (CAPTIVA) em andamento na indicação, mas ainda sem resultados. O ticagrelor não é comercializado no Brasil (0 registros), o que exige cautela adicional.

**Para prosseguir, é necessário:**
- Aguardar os resultados do CAPTIVA (conclusão prevista para 2027) e do estudo guiado por genótipo.
- Obter a bula da ANVISA com advertências e contraindicações oficiais.
- Obter dados detalhados do mecanismo de ação.
- Definir plano de mitigação do risco de hemorragia intracraniana e das interações medicamentosas (especialmente inibidores potentes de CYP3A4, como a claritromicina).
- Avaliar a viabilidade regulatória no Brasil, dado que não há registro vigente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

