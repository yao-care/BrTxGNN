---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamina A: De suplemento nutricional à deficiência congênita de protrombina

## Resumo em Uma Frase

Vitamina A (retinol) é um micronutriente essencial amplamente utilizado como suplemento para prevenir e tratar deficiências nutricionais e suas complicações, como cegueira noturna, xeroftalmia e imunossupressão.
O modelo TxGNN prevê que pode ser eficaz para **Deficiência Congênita de Protrombina (Congenital Prothrombin Deficiency)**,
atualmente sem nenhum ensaio clínico diretamente relevante e sem nenhuma publicação científica apoiando esta direção específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|---------|
| Indicação Original | Suplemento vitamínico / deficiência de vitamina A (texto de indicação não disponível no registro ANVISA consultado) |
| Nova Indicação Prevista | Deficiência Congênita de Protrombina (Congenital Prothrombin Deficiency) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos registros consultados. Com base em informações conhecidas, Vitamina A (retinol) é o protótipo dos retinoides — micronutriente lipossolúvel que, metabolizado a ácido retinoico, atua como ligante dos receptores nucleares RAR (*Retinoic Acid Receptor*) e RXR (*Retinoid X Receptor*). Por meio dessa via hormonal, regula a transcrição de genes envolvidos na diferenciação e proliferação celular, manutenção da integridade epitelial e resposta imunológica inata e adaptativa. Clinicamente, é empregada para prevenir e tratar a deficiência vitamínica e suas manifestações.

A relação mecanística entre Vitamina A e a Deficiência Congênita de Protrombina, no entanto, é indireta e sem suporte causal estabelecido. A protrombina (Fator II da coagulação) é uma proteína dependente de **vitamina K** para sofrer γ-carboxilação pós-translacional — etapa essencial para sua atividade biológica. Vitamina A não participa dessa via bioquímica. A única conexão biológica remota seria uma disfunção hepática grave secundária à deficiência extrema de vitamina A, que comprometeria a síntese de proteínas hepáticas em geral; contudo, isso representa uma complicação inespecífica, não uma indicação terapêutica direcionada.

A alta pontuação do TxGNN (99,97%) provavelmente reflete conexões indiretas no grafo de conhecimento entre os nós de "deficiência vitamínica", "disfunção hepática" e "coagulopatia" — um caminho de associação estatística, não de causalidade farmacológica. Não existem ensaios clínicos registrados nem publicações científicas que investiguem Vitamina A como tratamento para esta condição.

---

## Evidências de Ensaios Clínicos

> Nenhum dos estudos identificados utiliza Vitamina A como intervenção terapêutica para deficiência congênita de protrombina. Os ensaios encontrados tratam de outras condições hemorrágicas ou doenças metabólicas, sem sobreposição com a indicação prevista.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|:----:|---------|
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recrutando | 480 | Estudo observacional de perda óssea em hemofilia (ausência de fator VIII ou IX); sem intervenção com vitamina A e sem relação com deficiência de protrombina |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Concluído | 220 | Registro retrospectivo de adultos com erros inatos do metabolismo na Suíça francófona; estudo observacional, não é ensaio de intervenção com vitamina A |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Concluído | 40 | Concentrado de complexo protrombínico BERIPLEX P/N para reversão rápida de anticoagulação oral; o agente testado é PCC, não vitamina A |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Concluído | 90 | "Vitalliver" em cirrose descompensada (n=90); possível formulação vitamínica, mas sem foco em deficiência congênita de protrombina |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Concluído | 25 | Suplemento dietético com L-arginina, vitamina K2, B6, B12 e ácido fólico em hipertensão leve a moderada; sem relação com deficiência de protrombina |

---

## Evidências da Literatura

Atualmente não há literatura relacionada ao uso de Vitamina A no tratamento da Deficiência Congênita de Protrombina.

---

## Informações de Comercialização no Brasil

Consta **1 registro ativo** na ANVISA com situação de comercialização confirmada. Os dados detalhados do registro (número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis no conjunto de dados atual e deverão ser consultados diretamente no portal ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN não é sustentada por evidências clínicas nem mecanísticas — a protrombina é uma proteína dependente de vitamina K, não de vitamina A, e nenhum ensaio clínico ou publicação científica apoia este reposicionamento. A pontuação elevada do modelo reflete provavelmente um artefato de caminhamento no grafo de conhecimento, sem correspondência com biologia causal.

**Para prosseguir, é necessário:**
- Identificar mecanismo biológico plausível que conecte o retinol (ou seus metabólitos) à síntese ou função do Fator II (protrombina)
- Obter evidências pré-clínicas — estudos in vitro ou in vivo — demonstrando efeito mensurável sobre a coagulação
- Revisar se a associação no grafo do TxGNN representa causalidade real ou co-ocorrência estatística entre nós de deficiência vitamínica e coagulopatia
- Recuperar dados completos de registro ANVISA (indicação aprovada, forma farmacêutica) para contextualização regulatória
---

