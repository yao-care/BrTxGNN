---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Com base no Evidence Pack, a indicação com nível de evidência acionável é **Leucemia Mieloide** (rank 7, L2, "Proceed with Guardrails"), pois concentra 30 ensaios clínicos e 20 publicações. O relatório foca nesta indicação.

---

# Plerixafor: Da Mobilização de Células-Tronco à Leucemia Mieloide

## Resumo em Uma Frase

Plerixafor (Mozobil) é um antagonista seletivo do receptor CXCR4, aprovado para mobilização de células-tronco hematopoéticas em pacientes com linfoma não-Hodgkin e mieloma múltiplo antes do transplante autólogo de células-tronco, em combinação com G-CSF.
O modelo TxGNN prevê que pode ser eficaz para **Leucemia Mieloide (Myeloid Leukemia)**, atualmente com **30 ensaios clínicos** e **20 publicações** apoiando esta direção de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mobilização de células-tronco hematopoéticas (NHL / mieloma múltiplo + transplante autólogo) |
| Nova Indicação Prevista | Leucemia Mieloide (Myeloid Leukemia) |
| Pontuação de Previsão TxGNN | 99.02% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Plerixafor é um antagonista seletivo e reversível do receptor de quimiocina CXCR4. Seu mecanismo de ação aprovado baseia-se no bloqueio do eixo CXCL12/CXCR4 (também conhecido como SDF-1α/CXCR4), responsável pela ancoragem das células-tronco hematopoéticas na medula óssea. Ao bloquear este eixo, o Plerixafor desloca as células-tronco para a circulação periférica, onde podem ser coletadas para transplante. Embora os dados detalhados de MOA não estejam disponíveis no presente pacote, o mecanismo molecular é amplamente descrito na literatura e constitui a base científica desta análise.

Na leucemia mieloide aguda (LMA), os blastos leucêmicos e as células-tronco leucêmicas (LSCs) expressam intensamente o receptor CXCR4. O eixo CXCL12/CXCR4 ancora as células de LMA no microambiente protetor da medula óssea, que fornece sinais de sobrevivência e confere resistência à quimioterapia — fenômeno denominado resistência ao fármaco mediada pelo nicho (EMDR). Ao bloquear este mesmo eixo nas células leucêmicas, o Plerixafor pode: (1) deslocar células de LMA do nicho protetor para a circulação periférica; (2) eliminar o efeito protetor das células do estroma; e (3) aumentar significativamente a sensibilidade dessas células à quimioterapia, estratégia denominada **quimiossensibilização**.

A conexão entre a indicação original e a nova indicação é mecanisticamente direta: o mesmo receptor (CXCR4) e o mesmo eixo molecular (CXCL12/CXCR4) operam em ambas as situações. Trata-se de uma extensão lógica e não de uma extrapolação especulativa — o alvo farmacológico é idêntico, e sua relevância em LMA foi diretamente testada em múltiplos ensaios clínicos de Fase 1/2 já concluídos, envolvendo centenas de pacientes.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Concluído | 39 | Quimiossensibilização com Plerixafor + G-CSF em LMA recidivante/refratária — validação direta da estratégia de bloqueio CXCR4 para aumentar eficácia da quimioterapia |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Concluído | 52 | AMD3100 (Plerixafor) + MEC (Mitoxantrona, Etoposídeo, Citarabina) em R/R AML — testa hipótese de que romper a interação dos blastos com o microambiente aumenta a citotoxicidade |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Concluído | 55 | Estudo multicêntrico prospectivo (PLERIFLAG): Fludarabina, Idarrubicina, Citarabina, G-CSF + Plerixafor IV em pacientes jovens (≤65 anos) com LMA em primeira recidiva precoce ou refratária |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Concluído | 36 | Plerixafor + Citarabina + Daunorubicina (esquema 7+3 padrão) ± G-CSF em LMA recém-diagnosticada — estabelece dose segura de Plerixafor combinada com indução de primeira linha |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | Concluído | 113 | AML18 Pilot Trial (NCRI): avalia factibilidade de combinar inibidor de CXCR4 (Plerixafor) com quimioterapia DAE padrão em pacientes idosos com LMA e SMD de alto risco |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Concluído | 71 | Decitabina + Plerixafor (escalada de dose) como terapia de indução em pacientes ≥60 anos com LMA — combina agente hipometilante com mobilização de LSCs pelo CXCR4 |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Concluído | 33 | G-CSF + Plerixafor + Sorafenibe em LMA com mutação FLT3-ITD — combinação de inibidor de FLT3, mobilizador CXCR4 e G-CSF para superar resistência mediada pelo estroma |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Concluído | 47 | G-CSF + Plerixafor com Busulfano/Fludarabina para transplante alogênico em leucemias mieloides (LMA/SMD/LMC) — dados de segurança em contexto pré-SCT |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | Status Desconhecido | 28 | Plerixafor + Infusão de Linfócitos do Doador (DLI) para leucemia aguda (LMA/LLA) recidivante pós-transplante alogênico — explora bloqueio de CXCR4 para expor células leucêmicas ao efeito enxerto-versus-leucemia |
| [NCT00241358](https://clinicaltrials.gov/study/NCT00241358) | Phase 1/2 | Concluído | 92 | AMD3100 para mobilização e transplante de células-tronco de doadores HLA-compatíveis em malignidades hematológicas — maior base de dados de segurança disponível para este agente em contexto hematológico |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Revisão Sistemática + Meta-análise | Leukemia Research | Compilação de estudos pré-clínicos e clínicos de Plerixafor + quimioterapia e/ou transplante em leucemia aguda; identificou 19 estudos relevantes e apoia design de ensaios clínicos definitivos |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Revisão | Leukemia | Revisão abrangente e atualizada do eixo CXCL12-CXCR4 em LMA: papel na proliferação autônoma, resistência à apoptose, quimiorresistência e estratégias terapêuticas com Plerixafor e novos agentes |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Ensaio Clínico Phase 1/2 | Blood | 52 pacientes com R/R AML tratados com Plerixafor + MEC; demonstra factibilidade da quimiossensibilização via bloqueio do eixo CXCR4/CXCL12 — estudo pivô seminal |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Ensaio Clínico Phase I-II | Annals of Hematology | Esquema PLERIFLAG (Plerixafor IV em alta dose + FLAG-Ida) em LMA primariamente refratária ou com primeira recidiva precoce; relata resultados de resposta e tolerabilidade |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Ensaio Clínico Phase I | Haematologica | Decitabina + Plerixafor (escalada de dose 320–810 mcg/kg) em 69 pacientes idosos com LMA recém-diagnosticada; avalia efeito sobre células-tronco leucêmicas e perfil de segurança |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Ensaio Clínico Phase 1 | American Journal of Hematology | Sorafenibe + Plerixafor + G-CSF em 28 pacientes com LMA FLT3-ITD R/R; aborda resistência mediada pelo estroma via CXCR4, CD44 e VLA4 como mecanismo de escape |
| [28282031](https://pubmed.ncbi.nlm.nih.gov/28282031/) | 2017 | Ensaio Clínico Phase 1/2 | Blood Cancer Journal | Atualização de resultados de Plerixafor + G-CSF para quimiossensibilização em R/R AML; consolida dados de eficácia e segurança do estudo NCT00906945 |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Revisão | Biology | Antagonistas de CXCR4 como mobilizadores de células-tronco e sensibilizadores de terapia para LMA e glioblastoma — análise comparativa mecanística com base nos nichos perivasculares hipóxicos |
| [29140182](https://pubmed.ncbi.nlm.nih.gov/29140182/) | 2018 | Ciência Translacional | Hematology (Amsterdam) | TGF-β1 e CXCL12 modulam proliferação e sensibilidade à quimioterapia de células de LMA em co-cultura com células estromais mesenquimais — base experimental para a estratégia de quimiossensibilização por CXCR4 |
| [33080779](https://pubmed.ncbi.nlm.nih.gov/33080779/) | 2020 | Revisão | Cells | Hiperleucocitose e leucostase em LMA: papel do eixo CXCR4 na patofisiologia molecular e potencial terapêutico de novas abordagens moleculares |

---

## Informações de Comercialização no Brasil

O Plerixafor está registrado na ANVISA com **3 registros ativos** e situação de comercialização confirmada. Os detalhes individuais de cada registro (número oficial, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis neste pacote de evidências. Recomenda-se consulta direta ao portal de **Consulta de Produtos Registrados da ANVISA** para obtenção dos dados completos antes de qualquer avaliação regulatória ou decisão de reposicionamento.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O Plerixafor possui mecanismo de ação diretamente aplicável à leucemia mieloide aguda — o mesmo eixo CXCR4/CXCL12 bloqueado na indicação aprovada é o principal responsável pela resistência à quimioterapia em LMA. Múltiplos ensaios clínicos de Fase 1/2 já concluídos, com centenas de pacientes, validaram a segurança e demonstraram sinais consistentes de eficácia da estratégia de quimiossensibilização. A base de evidências é robusta o suficiente para avançar com cautela, mas ausência de ensaios de Fase 3 e lacunas nos dados regulatórios brasileiros impõem guardrails importantes.

**Para prosseguir, é necessário:**
- Recuperar dados completos dos registros ANVISA (número, indicação aprovada, forma farmacêutica) — dados indisponíveis no pacote atual
- Obter advertências e contraindicações da bula ANVISA/TFDA para iniciar avaliação de segurança S1 (DG001 — severidade Blocking)
- Confirmar dados de MOA detalhados via DrugBank API (DG002 — severidade High)
- Avaliar se a posologia aprovada para mobilização de células-tronco é compatível com os esquemas de quimiossensibilização em LMA utilizados nos ensaios clínicos
- Planejar estudo de Fase 2/3 randomizado para elevar o nível de evidência de L2 para L1 e viabilizar aprovação regulatória formal na nova indicação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

