---
layout: default
title: Valganciclovir
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Valganciclovir
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

# Valganciclovir: Da retinite por CMV à artrite reumatoide

## Resumo em Uma Frase

Valganciclovir é um pró-fármaco oral do ganciclovir, aprovado para o tratamento da retinite por citomegalovírus (CMV) em pacientes com AIDS e para a profilaxia de CMV em receptores de transplante de órgãos sólidos.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, porém esta previsão é provavelmente um **falso positivo**: toda a literatura disponível descreve Valganciclovir sendo utilizado para tratar infecções oportunistas por CMV *em* pacientes com AR imunossuprimidos — e não para tratar a AR em si.
Atualmente, há **0 ensaios clínicos** e **13 publicações** identificadas para esta direção, predominantemente relatos de caso e revisões sobre complicações infecciosas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Retinite por CMV em pacientes com AIDS; profilaxia de CMV em transplante de órgão sólido |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 98,97% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações farmacológicas conhecidas, Valganciclovir é um pró-fármaco oral do ganciclovir — um análogo nucleosídico que, após absorção, é rapidamente convertido em ganciclovir pela ação de esterases intestinais e hepáticas. O ganciclovir bloqueia a replicação do DNA do CMV por inibição competitiva da DNA polimerase viral (UL54) e por incorporação à cadeia de DNA em elongação, interrompendo sua síntese. Não há target imunológico ou antiinflamatório conhecido neste mecanismo.

A artrite reumatoide (AR) é uma doença inflamatória autoimune crônica tratada com imunossupressores como metotrexato, inibidores de TNF-α e inibidores de JAK (tofacitinib, upadacitinib, baricitinib). Esses agentes reduzem substancialmente a imunidade celular mediada por linfócitos T CD4+, criando condições favoráveis à reativação de vírus herpéticos latentes, em especial o CMV. A literatura identificada documenta de forma consistente que pacientes com AR em uso de JAK inibidores ou metotrexato desenvolvem infecções oportunistas por CMV (retinite, enterocolite, gastrite), nas quais Valganciclovir é o tratamento antiviral de escolha.

Entretanto, este cenário **não representa reposicionamento terapêutico**: Valganciclovir é administrado para tratar a complicação infecciosa, e não para modificar o curso da AR. A alta pontuação do TxGNN (98,97%) é interpretada como **falso positivo** gerado pela co-ocorrência frequente no grafo de conhecimento — pacientes com nó "AR" e nó "Valganciclovir" conectados pelo nó intermediário "infecção por CMV". Não existe plausibilidade mecanística direta para o uso de Valganciclovir como terapia da AR em si.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18068874](https://pubmed.ncbi.nlm.nih.gov/18068874/) | 2008 | Review/Guidelines | La Revue de medecine interne | Ausência de diretrizes para manejo de infecção por CMV em pacientes com AR e LES sob imunossupressão; discute quando iniciar antivirais |
| [41792858](https://pubmed.ncbi.nlm.nih.gov/41792858/) | 2026 | Review | Int J Retina Vitreous | Revisão das evidências recentes sobre retinite viral induzida por inibidores de JAK; risco crescente de CMV em pacientes com AR tratados com tofacitinib e outros JAKi |
| [11465875](https://pubmed.ncbi.nlm.nih.gov/11465875/) | 2001 | Drug Review | Drugs | Revisão farmacológica do Valganciclovir; demonstração de bioequivalência oral com ganciclovir IV 5 mg/kg para retinite por CMV em pacientes com AIDS |
| [15155152](https://pubmed.ncbi.nlm.nih.gov/15155152/) | 2004 | Review | Expert Opinion on Drug Safety | Revisão de toxicidade retiniana por fármacos; contextualiza hidroxicloroquina em AR e implicações oculares; relevância indireta |
| [41779881](https://pubmed.ncbi.nlm.nih.gov/41779881/) | 2025 | Case Series | Retinal Cases & Brief Reports | Dois pacientes com AR em uso prolongado de tofacitinib desenvolveram retinite por CMV; ambos tratados com Valganciclovir |
| [28389165](https://pubmed.ncbi.nlm.nih.gov/28389165/) | 2017 | Case Report | J Infect Chemother | Retinite por CMV seguida de uveíte de recuperação imune em paciente de 78 anos com AR em MTX + tofacitinib; CD4+ baixo (196 células) no momento do diagnóstico |
| [41526852](https://pubmed.ncbi.nlm.nih.gov/41526852/) | 2026 | Case Report | BMC Ophthalmology | Retinite por CMV com isquemia retiniana e hemorragia vítrea em paciente com AR em uso de upadacitinib; complicações raras e mal caracterizadas |
| [15494900](https://pubmed.ncbi.nlm.nih.gov/15494900/) | 2004 | Case Report | Clinical Infectious Diseases | Retinite por CMV em paciente com AR em anticorpos anti-TNF-α; relata imunossupressão grave como fator determinante |
| [26150269](https://pubmed.ncbi.nlm.nih.gov/26150269/) | 2015 | Case Report | Reumatismo | Ileocolite por CMV em paciente de 64 anos com AR sob imunossupressão; diarreia e dor abdominal persistentes como apresentação |
| [20711100](https://pubmed.ncbi.nlm.nih.gov/20711100/) | 2010 | Case Report/Review | Acta Reumatologica Portuguesa | Doença de Still do adulto e infecção por CMV; paciente iniciou Valganciclovir para hepatite por CMV, com posterior diagnóstico de doença inflamatória |

---

## Informações de Comercialização no Brasil

O Valganciclovir possui **4 registros ativos** no Brasil, com situação de comercialização confirmada. Os dados individuais dos registros (número, nome comercial, forma farmacêutica e texto de indicação aprovada) não constavam preenchidos neste Evidence Pack. Recomenda-se consultar o portal de consulta de medicamentos da ANVISA ([consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/)) para obter os detalhes completos de cada registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota clínica:** Embora os dados de segurança não tenham sido recuperados neste pack, o perfil de toxicidade de Valganciclovir é bem estabelecido na literatura e inclui mielossupressão (neutropenia, trombocitopenia, anemia) como efeito adverso clinicamente relevante. Esta informação deve ser considerada em qualquer avaliação clínica futura.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para artrite reumatoide é interpretada como **falso positivo estrutural**: todo o corpus de literatura identificado documenta Valganciclovir sendo utilizado para tratar complicações oportunistas por CMV *em* pacientes com AR imunossuprimidos, sem nenhuma evidência de que o fármaco trate ou modifique a AR em si. Não existe plausibilidade mecanística, nem ensaio clínico, nem hipótese biológica para este reposicionamento.

**Para reavaliar este candidato, seria necessário:**
- Evidências de que o CMV desempenhe papel causal na patogênese da AR (ex.: hipótese de gatilho viral autoimune)
- Estudos pré-clínicos demonstrando que a supressão do CMV modifica marcadores inflamatórios articulares
- Ensaios clínicos controlados em pacientes com AR CMV-soropositivos de difícil controle avaliando Valganciclovir como adjuvante
- Dados de MOA completos do DrugBank (DB01610) para confirmar ausência de targets imunológicos relevantes para AR
- Dados de segurança completos (advertências, contraindicações) via download da bula no portal ANVISA
---

