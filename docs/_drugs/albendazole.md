---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Albendazole
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

# Albendazole: Da Helmintíase Intestinal à Equinococose Alveolar

## Resumo em Uma Frase

Albendazole é um antiparasitário de amplo espectro da classe benzimidazol, reconhecido globalmente como tratamento de primeira linha para helmintíases intestinais e integrante da lista de medicamentos essenciais da OMS — porém sem registro comercial no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Equinococose Alveolar (Alveolar Echinococcosis)**, atualmente com **5 ensaios clínicos** e **20 publicações** apoiando esta direção.
As evidências disponíveis indicam que albendazole já é reconhecido pelas diretrizes internacionais (WHO/ECTM) como principal opção farmacológica para essa condição parasitária grave, conferindo alta plausibilidade clínica à previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Helmintíase intestinal (uso global reconhecido; sem registro no Brasil) |
| Nova Indicação Prevista | Equinococose Alveolar (Alveolar Echinococcosis) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Albendazole é um benzimidazol que, após absorção oral, é convertido em seu metabólito ativo — o **Albendazole Sulfóxido (ABZSO)**. Este metabólito inibe seletivamente a polimerização da β-tubulina nos parasitas, comprometendo a integridade do citoesqueleto, bloqueando a captação de glicose e levando à falência metabólica e paralisia dos vermes. Esse mecanismo é eficaz tanto contra nematoides intestinais quanto contra cestoides do gênero *Echinococcus* e *Taenia*.

A equinococose alveolar é causada pelo estágio metacestóide de *Echinococcus multilocularis*, que forma lesões hepáticas pseudotumorais infiltrativas com evolução potencialmente fatal (mortalidade próxima a 100% em 10–15 anos sem tratamento). O ABZSO atua inibindo a polimerização da β-tubulina dos protoescólex deste parasita, interrompendo a captação de glicose e o metabolismo lipídico da vesícula — configurando clara base mecanística para a eficácia nessa indicação, conforme documentado também em modelos animais (PMID 38501660).

É importante destacar que albendazole exerce efeito **parasitostático** (retarda o crescimento, mas não elimina o parasita de forma definitiva), o que demanda tratamento contínuo e de longa duração. Quando a ressecção cirúrgica radical não é viável, albendazole é a única opção farmacológica recomendada pelas diretrizes da WHO/ECTM, respaldada por consenso internacional e um ensaio clínico de Fase 2 concluído com 194 pacientes.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Fase 2 | Concluído | 194 | Maior ensaio de intervenção direta para esta indicação: avaliação de albendazole no tratamento da equinococose alveolar em estágio inicial no Quirguistão, região com prevalência de ~6% identificada por vigilância ultrassonográfica |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Concluído | 50 | Estudo prospectivo observacional (EchinoVISTA) para definição de marcadores de viabilidade parasitária e indicadores inovadores de acompanhamento em pacientes com equinococose hepática alveolar tratados com albendazole |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Estado Desconhecido | 24 | ECR avaliando o papel do albendazole adjuvante após ressecção de cisto hidático pulmonar versus placebo, com seguimento de 6 meses para redução de recorrência |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Em Recrutamento | 43 | Avaliação de nova técnica de PCR quantitativa multiplex para diagnóstico de equinococose; albendazole citado como base do tratamento farmacológico de referência no contexto do estudo |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Consenso de Especialistas | Acta Tropica | Diretrizes de consenso WHO-IWGE para diagnóstico, tratamento e seguimento da equinococose humana; albendazole como tratamento farmacológico de referência para a forma alveolar |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revisão Clínica | World J Gastroenterol | Recomendações mais recentes (2025) sobre manejo da equinococose hepática; ressecção cirúrgica como pilar principal, albendazole como adjuvante essencial pré e pós-operatório |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revisão Abrangente | Clin Microbiol Rev | Panorama dos avanços do século XXI em genética, epidemiologia molecular, ferramentas diagnósticas e tratamento da equinococose; albendazole como pilar farmacológico insubstituível |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Revisão de Quimioterapia | Parasite (Paris) | Estado atual da quimioterapia com benzimidazóis para equinococose alveolar; discussão das limitações do efeito parasitostático, toxicidade hepática e busca por novas opções terapêuticas |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Revisão Terapêutica | Parasite (Paris) | Comparação de albendazole e mebendazol no tratamento da equinococose; estratégias de triagem de novos compostos para superar as limitações dos benzimidazóis atuais |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Estudo Farmacológico | Antimicrob Agents Chemother | Mecanismo metabólico e estudo farmacológico do albendazole em modelo de equinococose alveolar hepática em ratos; formulações com biodisponibilidade aprimorada (nanocristais, dispersão cristalina, sal hidroxietilsulfonato) avaliadas |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Reposicionamento de Fármacos | Parasitology | Estratégia de drug repurposing identifica pirronaridina como candidata promissora para equinococose alveolar; albendazole destacado como único tratamento antiparasitário disponível atualmente |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Revisão | Acta Tropica | Status e perspectivas de novas opções de tratamento para equinococose cística e alveolar; albendazole e mebendazol como únicas opções não-cirúrgicas aprovadas, com necessidade urgente de alternativas |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Revisão Clínica | Semin Liver Dis | Equinococose alveolar hepática como zoonose rara e grave com ressurgência global; albendazole como tratamento vitalício de manutenção quando ressecção completa não é possível |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Revisão | Chin J Schistosomiasis Control | Progressos recentes na aplicação do albendazole para equinococose alveolar em pacientes inoperáveis; mecanismo parasitostático e avanços em novas formulações para melhorar desfechos |

---

## Informações de Comercialização no Brasil

Albendazole **não possui registros ativos na ANVISA**. O medicamento não está comercializado no Brasil conforme dados regulatórios consultados em 2026-04-04. Qualquer uso no país requereria processo formal de registro ou autorização especial junto à agência reguladora.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Albendazole é reconhecido pelas diretrizes internacionais (WHO, ECTM) como o tratamento farmacológico de escolha para equinococose alveolar, respaldado por um ensaio clínico de Fase 2 concluído (n=194), múltiplos consensos de especialistas e extensa literatura de revisão. A ausência total de registro no Brasil e a falta de dados de segurança localmente validados (advertências, contraindicações, interações medicamentosas) exigem cautela e planejamento regulatório estruturado antes de qualquer iniciativa de introdução clínica.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) e perfil de segurança via DrugBank API (prioridade alta)
- Baixar e analisar a bula oficial (SmPC/PI) para extrair advertências, contraindicações e interações medicamentosas relevantes
- Avaliar viabilidade de processo de registro regulatório na ANVISA, potencialmente pela via de medicamento órfão para doença negligenciada
- Acompanhar publicação dos dados finais do ensaio NCT07182305 para consolidação das evidências de eficácia em estágio inicial da doença
- Considerar formulações com biodisponibilidade oral aprimorada (nanocristais, dispersão cristalina), dado o impacto documentado da solubilidade limitada do albendazole nos desfechos clínicos
---

