---
layout: default
title: Biotin
parent: Apenas Predição do Modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Biotin: nova indicação prevista, Dispepsia (Dyspepsia) (nível de evidência L5). Indicação original: Deficiência nutricional de biotina"
monitor_inn: "Biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "familial visceral myopathy", "anemia of prematurity", "congenital prothrombin deficiency", "vitamin deficiency disorder", "biotin metabolic disease", "cystinosis", "obsolete contact dermatitis caused by poison oak"]
---

# Biotin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Biotina: Da deficiência nutricional de biotina à dispepsia

## Resumo em Uma Frase

Biotina (vitamina B7) foi originalmente usada no tratamento da deficiência nutricional de biotina.
O modelo TxGNN prevê que pode ser eficaz para **dispepsia (dyspepsia)**, mas a previsão não tem respaldo clínico: **0 ensaios clínicos** e **6 publicações**, nenhuma delas testando a biotina como tratamento para essa condição.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Deficiência nutricional de biotina |
| Nova Indicação Prevista | Dispepsia (Dyspepsia) |
| Pontuação de Previsão TxGNN | 99,43% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, a biotina é um cofator de carboxilases envolvidas no metabolismo de ácidos graxos, aminoácidos e gliconeogênese. Sua eficácia na reposição da deficiência de biotina está bem estabelecida.

Não foi identificada uma ligação mecanística crível entre a biotina e a dispepsia. A pontuação alta do TxGNN (0,994) vem de uma previsão baseada em grafo de conhecimento e não de dados clínicos. A literatura recuperada trata de deficiência de biotina em um lactente alimentado com fórmula de aminoácidos (em que a dispepsia era apenas um diagnóstico neonatal prévio), de células endócrinas gástricas na síndrome do intestino irritável, de correção da microbiota intestinal e de gastrite por *H. pylori*. Nenhum desses trabalhos avalia a biotina como tratamento da dispepsia.

Portanto, a previsão deve ser tratada como uma hipótese a ser testada e não como uma indicação respaldada.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Relato de caso | The Journal of Dermatology | Deficiência de biotina em lactente de 5 meses alimentado só com fórmula de aminoácidos, com diagnóstico neonatal de dispepsia; apresentou alopecia e dermatite descamativa |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Revisão | Eksperimental'naia i klinicheskaia gastroenterologiia | Suplemento com fibras, vitaminas (incluindo biotina) e minerais na prevenção de distúrbios da microbiota em pacientes com doença pulmonar tratados com antibióticos; a biotina é apenas um componente |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Coorte | International Journal of Molecular Medicine | Células endócrinas do antro gástrico em 76 pacientes com síndrome do intestino irritável; sem relação com biotina |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Coorte | World Journal of Gastrointestinal Endoscopy | Células endócrinas da mucosa oxíntica gástrica na síndrome do intestino irritável; sem relação com biotina |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Coorte | Journal of Clinical Pathology | Origem celular da interleucina 10 na gastrite por *H. pylori*; sem relação com biotina |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Coorte | Kidney International | Linfócitos T do intestino delgado na nefropatia por IgA; sem relação com biotina |

## Informações de Comercialização no Brasil

Não há registros de biotina como medicamento na ANVISA nos dados compilados para este relatório (situação: não comercializado; 0 registros).

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento (não extraídas da bula):** o grafo de conhecimento do TxGNN associa o fármaco a condições como doença renal, nefrolitíase, nefrocalcinose, hipercalcemia, hiperparatireoidismo, sarcoidose, distúrbio do metabolismo do fósforo, nefropatia aguda por urato, constipação e lesões ósseas metastáticas líticas. Esses dados são indicativos e precisam ser confirmados na bula.
- **Interações medicamentosas:** nenhuma interação foi encontrada na consulta realizada.
- **Interferência laboratorial:** doses altas de biotina podem interferir em imunoensaios baseados em estreptavidina-biotina (por exemplo, troponina e testes de tireoide).

As advertências e contraindicações da bula da ANVISA não estavam disponíveis. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para dispepsia se baseia apenas na pontuação do modelo (L5), sem ensaios clínicos e com literatura que não testa a biotina como tratamento. Além disso, o produto não tem registro no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) da biotina, via DrugBank
- Bula da ANVISA, com advertências e contraindicações, para a triagem de segurança
- Evidência clínica ou pré-clínica que ligue a biotina à fisiopatologia da dispepsia
- Esclarecimento da situação regulatória no Brasil (produto não comercializado como medicamento)

**Observação sobre outras previsões:** entre as demais indicações previstas, a **doença metabólica da biotina** (pontuação de 92,14%) foi a que apresentou o maior respaldo, nível L2 e recomendação *Proceed with Guardrails*. Esse respaldo é principalmente mecanístico e de revisões. Os ensaios Phase 2 e Phase 2/3 com biotina em altas doses (MD1003) foram realizados em outras doenças, como esclerose lateral amiotrófica e adrenomieloneuropatia. Como essa indicação reafirma em grande parte o uso nutricional original, a novidade para reposicionamento é limitada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

