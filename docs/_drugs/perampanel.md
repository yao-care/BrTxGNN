---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Perampanel
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

Usando o `txgnn-pipeline` para estruturar o relatório de reposicionamento. As instruções de formato já estão no system prompt (v5). Gerando o relatório agora:

---

# Perampanel: Da epilepsia focal à epilepsia visual

## Resumo em Uma Frase

Perampanel é um antiepiléptico de terceira geração — primeiro da classe dos antagonistas AMPA — aprovado para o tratamento de crises de início focal e crises tônico-clônicas generalizadas primárias em pacientes com epilepsia.
O modelo TxGNN prevê que pode ser eficaz para **Epilepsia Visual (Visual Epilepsy)**,
atualmente com **3 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia focal (crises de início focal e GTCS) |
| Nova Indicação Prevista | Epilepsia Visual (Visual Epilepsy) |
| Pontuação de Previsão TxGNN | 99.92% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Research Question |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados neste Evidence Pack. Com base na literatura clínica disponível, Perampanel é um **antagonista seletivo e não competitivo dos receptores AMPA** (α-amino-3-hidroxi-5-metil-4-isoxazolpropionato) — receptores ionotrópicos de glutamato responsáveis pela excitação pós-sináptica rápida. Ao bloquear esses receptores, o fármaco suprime a hiperexcitabilidade neuronal que caracteriza as crises epilépticas, sem afetar receptores NMDA ou canais iônicos. É o primeiro fármaco desta classe aprovado globalmente para epilepsia.

A **epilepsia visual** é uma forma de epilepsia reflexa desencadeada por estímulos visuais (flashes de luz, padrões de contraste, telas piscantes), na qual a hiperexcitabilidade do **córtex occipital/visual** é o mecanismo central. A conexão mecanística é direta: os receptores AMPA do córtex visual mediam a resposta excitatória anômala a estímulos luminosos, e o bloqueio desses receptores pode interromper esse circuito. Tanto a indicação original quanto a nova indicação compartilham o mesmo substrato patofisiológico — descarga neuronal excessiva mediada por AMPA.

Os ensaios clínicos identificados não foram especificamente desenhados para epilepsia visual, tratando-se de extrapolação indireta. No entanto, modelos animais de epilepsia reflexa validam o mecanismo AMPA em epilepsias fotossensíveis e induzidas por estímulos, e a literatura clínica estabelece a eficácia de perampanel em amplo espectro de síndromes epilépticas — o que sustenta a plausibilidade biológica desta previsão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Concluído | 18 | Avaliação de tolerabilidade, segurança e farmacocinética do perampanel (E2007) em pacientes com crises parciais ou generalizadas refratárias em uso de pelo menos um antiepiléptico concomitante |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Concluído | 30 | Efeitos do perampanel sobre cognição e EEG em pacientes com epilepsia; validação do mecanismo como antagonista seletivo não competitivo de receptores AMPA em contexto real |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Concluído | 12 | Efeitos do perampanel sobre testes neurofisiológicos: EEG, potenciais evocados somatossensoriais, auditivos e **visuais (VEP)** — único estudo com avaliação de desfecho no sistema visual |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | RCT + Real-world Review | *Epilepsy & Behavior* | Perampanel aprovado para crises de início focal (monoterapia e adjuvante, ≥4 anos) e GTCS adjuvante (≥12 anos); revisão abrangente de ensaios pivotais e dados do mundo real |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review & Meta-analysis | *Seizure* | Meta-análise de RCTs: perampanel reduz significativamente a frequência de crises focais e generalizadas com perfil de segurança aceitável |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Systematic Review | *Medical Journal of Malaysia* | Revisão sistemática da eficácia e segurança do perampanel como adjuvante para crises generalizadas e focais; confirmação de eficácia ampla |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review | *Brain & Development* | Revisão sistemática e meta-análise sobre eficácia, tolerabilidade e segurança do perampanel especificamente em crianças e adolescentes com epilepsia |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Diretriz Clínica (AAN/AES) | *Neurology* | Atualização de diretrizes da Academia Americana de Neurologia: eficácia e tolerabilidade de antiepilépticos de 2ª e 3ª geração, incluindo perampanel, para epilepsia de novo início |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | RCT (subanálise de 3 ensaios Fase III) | *Neurology* | Impacto de indutores enzimáticos CYP3A4 concomitantes sobre eficácia e segurança do perampanel; análise pooled de três estudos pivotais |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | PK/PD Review | *Expert Opinion on Drug Metabolism & Toxicology* | Avaliação farmacocinética e farmacodinâmica do perampanel para epilepsia focal; discussão do mecanismo AMPA e relevância clínica |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Coorte (Pediátrica) | *Annals of Clinical and Translational Neurology* | Eficácia do perampanel em epilepsia pediátrica com etiologia genética conhecida ou presumida; relevância para síndromes com hiperexcitabilidade glutamatérgica |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | *BMJ* | Manejo de epilepsia na gravidez e lactação; análise do perfil de segurança do perampanel em mulheres em idade fértil — consideração relevante para planejamento de estudos |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Coorte Real-world | *Frontiers in Neurology* | Experiência real com perampanel na epilepsia de ausência infantil como primeira terapia adjuvante e monoterapia de segunda linha; avalia efetividade e tolerabilidade |

---

## Informações de Comercialização no Brasil

O perampanel possui **2 registros ativos** na ANVISA e situação de mercado confirmada como **Comercializado**. Os dados detalhados de nome comercial, forma farmacêutica, fabricante e indicação aprovada não constam neste Evidence Pack. Consulte o portal ANVISA (consultas.anvisa.gov.br) para informações completas sobre os produtos registrados.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Research Question**

**Justificativa:**
O perampanel possui mecanismo de ação (antagonismo seletivo dos receptores AMPA) biologicamente plausível para epilepsia visual — ambas as condições compartilham hiperexcitabilidade cortical mediada por AMPA —, mas nenhum dos ensaios clínicos identificados foi desenhado especificamente para esta indicação. A evidência atual é de nível L3, constituída por extrapolação indireta de estudos sobre epilepsia em geral.

**Para prosseguir, é necessário:**
- Delineamento de estudo clínico específico para epilepsia visual / epilepsia fotossensível (estudo de prova de conceito, Phase 2)
- Confirmação do perfil de ativação de receptores AMPA no córtex visual por neuroimagem funcional ou eletrofisiologia
- Obtenção dos dados completos da bula ANVISA (advertências, contraindicações, interações)
- Avaliação em subgrupos: fotossensibilidade idiopática vs. sintomática, pediátrico vs. adulto
- Revisão de potenciais interações com outros antiepilépticos em uso combinado (CYP3A4 indutores reduzem exposição ao perampanel em até 50%)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

