---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Letermovir
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

# Letermovir: Da profilaxia de CMV à modulação da inflamação crônica em HIV/AIDS

## Resumo em Uma Frase

Letermovir é um antiviral aprovado para profilaxia de infecção por Citomegalovírus (CMV) em receptores adultos CMV-soropositivos de transplante alogênico de células-tronco hematopoéticas (TCTH).
O modelo TxGNN prevê potencial eficácia em **AIDS (HIV/AIDS)** por meio de uma estratégia indireta — supressão do CMV como driver de inflamação crônica em pessoas vivendo com HIV —
atualmente com **4 ensaios clínicos** e **7 publicações** apoiando esta direção, representando a indicação com maior suporte de evidências neste pacote.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Profilaxia de infecção e doença por CMV em transplante de células-tronco hematopoéticas |
| Nova Indicação Prevista | AIDS — redução de inflamação crônica mediada por CMV em PVHIV |
| Pontuação de Previsão TxGNN | 97,86% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Letermovir atua inibindo o complexo terminase do DNA do CMV — uma enzima viral altamente específica responsável pelo clivamento e empacotamento do DNA viral em novos vírions durante a replicação. Por ser exclusivamente direcionado ao CMV, o fármaco não tem atividade antirretroviral direta sobre o HIV.

A conexão com HIV/AIDS baseia-se em uma hipótese imunológica e epidemiológica bem estabelecida: a infecção por CMV é praticamente universal entre pessoas vivendo com HIV (PVHIV), e sua reativação silenciosa persiste mesmo em pacientes com carga viral indetectável em uso de terapia antirretroviral (ARV). Essa reativação alimenta a expansão contínua de células T CD8+ CMV-específicas, o aumento de marcadores de senescência imune, o comprometimento da barreira intestinal e a elevação de marcadores inflamatórios sistêmicos (como sCD14 e I-FABP). O resultado é uma inflamação residual que acelera o envelhecimento biológico e aumenta o risco de comorbidades como doenças cardiovasculares, neurocognitivas e metabólicas nas PVHIV.

A hipótese de reposicionamento é, portanto, **indireta**: Letermovir → supressão da replicação do CMV → redução da ativação imune crônica → melhora de desfechos inflamatórios em HIV. Não se trata de uma ação antirretroviral, mas de um manejo do CMV como co-patógeno modificável no contexto do HIV. Esta é uma abordagem emergente com suporte de estudos clínicos já concluídos, notadamente o estudo CIAO (NCT05362916).

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05362916](https://clinicaltrials.gov/study/NCT05362916) | N/A | Concluído | 33 | Estudo CIAO: multicêntrico, randomizado e controlado, avaliou o impacto de Letermovir sobre o marcador de translocação intestinal LPS em PVHIV CMV-soropositivos tratados com ARV. Resultados publicados (PMID 36690406). Representa a evidência clínica mais direta disponível |
| [NCT04840199](https://clinicaltrials.gov/study/NCT04840199) | Phase 2 | Terminado | 44 | RCT aberto avaliando eficácia anti-inflamatória de Letermovir vs. nenhum tratamento anti-CMV por 48 semanas, em adultos HIV+/CMV+ com supressão por ARV; encerrado antecipadamente em nov/2023 — razão não especificada (ponto crítico a verificar) |
| [NCT06626555](https://clinicaltrials.gov/study/NCT06626555) | Phase 2 | Não iniciado | 36 | Piloto randomizado avaliando efeito de Letermovir sobre ativação de células T em HIV-1 tratado; sem resultados disponíveis até o momento |
| [NCT06118515](https://clinicaltrials.gov/study/NCT06118515) | Phase 1 | Recrutando | 12 | Avaliação de farmacocinética e segurança em neonatos com CMV congênito sintomático; dados de PK relevantes para populações imunocomprometidas especiais |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36690406](https://pubmed.ncbi.nlm.nih.gov/36690406/) | 2023 | Estudo Prospectivo Intervencionista | BMJ Open | Protocolo do estudo CIAO publicado: correlação entre títulos IgG anti-CMV, permeabilidade intestinal e inflamação sistêmica em PVHIV com ARV — fundamentação da hipótese central do reposicionamento |
| [41860720](https://pubmed.ncbi.nlm.nih.gov/41860720/) | 2026 | Revisão | Current HIV/AIDS Reports | Revisão abrangente sobre CMV como driver modificável de inflamação, fragilidade e envelhecimento acelerado em PVHIV; resume mecanismos imunes e intervenções emergentes, incluindo Letermovir |
| [25779572](https://pubmed.ncbi.nlm.nih.gov/25779572/) | 2015 | In vitro | Antimicrobial Agents and Chemotherapy | Estudos de combinação in vitro de Letermovir com antivirais aprovados para CMV e anti-HIV; ausência de antagonismo com ARVs, dado de segurança relevante para uso combinado |
| [35343771](https://pubmed.ncbi.nlm.nih.gov/35343771/) | 2022 | Análise Retrospectiva | Microbiology Spectrum | Avaliação de mutações de resistência no UL56 (terminase) em transplantados com CMV refratário; relevante para entender emergência de resistência em uso prolongado |
| [33489928](https://pubmed.ncbi.nlm.nih.gov/33489928/) | 2020 | Mecanístico | Frontiers in Cellular and Infection Microbiology | Novo modelo HCMV trifluorescente para estudar dinâmica de expressão gênica e mecanismos de ação antivirais, incluindo Letermovir; apoia compreensão mecanística |
| [32041199](https://pubmed.ncbi.nlm.nih.gov/32041199/) | 2020 | Revisão | Int. Journal of Molecular Sciences | Leucemia mieloide aguda em PVHIV; contextualiza comorbidades oncohematológicas emergentes com aumento da sobrevida em HIV — população que pode se beneficiar de profilaxia de CMV |
| [30086336](https://pubmed.ncbi.nlm.nih.gov/30086336/) | 2018 | Relato de Conferência | Antiviral Research | Resumo da 31ª ICAR: inclui apresentações sobre Letermovir no contexto de CMV em imunocomprometidos, perspectiva histórica do desenvolvimento |

---

## Informações de Comercialização no Brasil

Letermovir possui **3 registros** na ANVISA com situação **Comercializado**. Os dados detalhados dos registros (número, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis nesta versão do Evidence Pack.

Consulte diretamente o portal [Consulta de Medicamentos da ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/) pelo nome do princípio ativo **Letermovir** para acesso completo aos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota:** Os dados de interação medicamentosa (DDI), advertências principais e contraindicações não estão disponíveis neste Evidence Pack. Dado que PVHIV em uso de ARV utilizam múltiplos medicamentos concomitantes, a avaliação de interações medicamentosas é **prioritária** antes de qualquer uso nesta população.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A hipótese de que Letermovir pode reduzir inflamação crônica em PVHIV — via supressão do CMV como co-patógeno inflamatório — é biologicamente plausível e conta com suporte de ao menos um estudo clínico controlado concluído (CIAO, NCT05362916), um RCT de fase 2 encerrado e um novo estudo de fase 2 em preparação. O nível L3 reflete evidências observacionais e estudos de mecanismo, ainda sem RCT de fase 3 com desfechos clínicos duros. A estratégia é indireta (não antirretroviral), o que limita a amplitude da indicação mas reduz riscos de interferência com terapia base.

**Para prosseguir, é necessário:**
- Acessar e analisar os resultados completos do estudo CIAO (NCT05362916), especialmente desfecho primário (LPS plasmático) e desfechos secundários inflamatórios
- Esclarecer a razão do encerramento antecipado do NCT04840199 — se por falha de eficácia ou evento adverso, isso altera significativamente a avaliação
- Obter dados completos de interações medicamentosas com antirretrovirais (inibidores de protease, NNRTIs, inibidores de integrase)
- Baixar e analisar a bula ANVISA para advertências, contraindicações e populações especiais
- Definir o subgrupo-alvo: PVHIV com títulos elevados de IgG anti-CMV e/ou marcadores inflamatórios (sCD14, IL-6) elevados apesar de ARV supressivo
- Avaliar viabilidade de estudo clínico nacional (fase 2) com desfechos inflamatórios como endpoint primário
---

