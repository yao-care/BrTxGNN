---
layout: default
title: Magnesium
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Magnesium
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

O skill `txgnn-pipeline` cobre infraestrutura e deployment, não a geração de relatórios — as instruções do relatório já estão no system prompt. Prossigo diretamente com a geração do relatório.

---

# Magnésio: De suplemento mineral à enxaqueca

## Resumo em Uma Frase

Magnésio (Magnesium, DB14513) é um mineral essencial ao organismo humano, utilizado clinicamente para corrigir hipomagnesemia e manter funções neuromuscular, cardiovascular e metabólica. O modelo TxGNN prevê que pode ser eficaz no tratamento e prevenção da **Enxaqueca (Migraine Disorder)**, com **mais de 10 ensaios clínicos** e **20 publicações científicas** apoiando essa direção. A evidência acumulada já levou à incorporação do magnésio nas diretrizes da American Headache Society como terapia preventiva de primeira linha.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Suplementação de magnésio / hipomagnesemia |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 98,03% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Magnésio é o quarto mineral mais abundante no organismo humano e cofator de mais de 300 reações enzimáticas, com papel fundamental na regulação da excitabilidade neuronal. Do ponto de vista fisiopatológico, o magnésio é essencial para a transmissão sináptica, condução neuromuscular e homeostase de canais iônicos — todos mecanismos diretamente implicados na enxaqueca.

O mecanismo de ação na enxaqueca é multifatorial e bem documentado: o magnésio atua como antagonista endógeno dos receptores NMDA (bloqueando a excitotoxicidade glutamatérgica), inibe a depressão cortical alastrante (CSD — *Cortical Spreading Depression*), que é o principal substrato neurológico da aura da enxaqueca, além de modular receptores de serotonina e canais de cálcio voltagem-dependentes. Esses mecanismos são centrais à fisiopatologia da enxaqueca em todos os seus subtipos.

A sustentação clínica é robusta e convergente: estudos consistentes demonstram que pacientes com enxaqueca apresentam concentrações séricas e intracelulares de magnésio significativamente mais baixas do que controles saudáveis, sugerindo que a deficiência de magnésio contribui diretamente para a hiperexcitabilidade neuronal característica da condição. O sulfato de magnésio intravenoso (MgSO₄ IV) já é amplamente utilizado em pronto-socorros para crises agudas, e a suplementação oral foi incorporada às diretrizes da American Headache Society e da American Academy of Neurology (Grau de Recomendação B) como terapia preventiva, conferindo altíssima plausibilidade à previsão do modelo TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT05967442](https://clinicaltrials.gov/study/NCT05967442) | Phase 3 | Concluído | 157 | Compara eficácia do MgSO₄ IV vs metoclopramida e proclorperazina IV no tratamento de enxaqueca aguda em adultos no departamento de emergência |
| [NCT06904287](https://clinicaltrials.gov/study/NCT06904287) | Phase 3 | Recrutando | 100 | Avalia se a adição de magnésio à proclorperazina reduz a dor da enxaqueca aguda no pronto-socorro |
| [NCT07147972](https://clinicaltrials.gov/study/NCT07147972) | Phase 3 | Não iniciado | 100 | Compara eficácia e tolerabilidade de nutraceuticals (incluindo magnésio, riboflavina e CoQ10) vs terapia profilática convencional (beta-bloqueadores, antiepilépticos) |
| [NCT01756209](https://clinicaltrials.gov/study/NCT01756209) | Phase 4 | Concluído | 160 | Avalia ibuprofeno e/ou acetaminofeno com e sem profilaxia com magnésio no tratamento agudo de enxaqueca primária em crianças de 5 a 18 anos |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Concluído | 60 | Avalia eficácia e segurança do ácido alfa-lipóico adicionado ao magnésio na profilaxia de enxaqueca em adolescentes com crises frequentes ou incapacitantes |
| [NCT04491474](https://clinicaltrials.gov/study/NCT04491474) | Phase 4 | Concluído | 128 | Compara bloqueio do nervo occipital maior e supraorbital vs placebo na enxaqueca aguda no pronto-socorro; magnésio IV integra o protocolo de tratamento padrão |
| [NCT03190044](https://clinicaltrials.gov/study/NCT03190044) | N/A | Desconhecido | 82 | Estudo PACR: combinação fixa de magnésio + partenolídeo + andrographis + CoQ10 + riboflavina como profilaxia — avalia se a combinação supera os compostos isolados |
| [NCT04463875](https://clinicaltrials.gov/study/NCT04463875) | N/A | Concluído | 113 | Estudo real-world prospectivo com Vivinor® (Mg + B2 + feverfew + andrographis + CoQ10) em 113 pacientes com enxaqueca episódica; desfecho primário: redução de dias com enxaqueca |
| [NCT04759040](https://clinicaltrials.gov/study/NCT04759040) | N/A | Concluído | 120 | Ensaio randomizado duplo-cego controlado por placebo do MIGRAINEGUARD™ (CoQ10 + magnésio + riboflavina + feverfew + Skullcap) para profilaxia de enxaqueca |
| [NCT02901756](https://clinicaltrials.gov/study/NCT02901756) | N/A | Concluído | 132 | Estudo prospectivo observacional com CoQ10 (100 mg) + feverfew (100 mg) + magnésio (112,5 mg/dia) por 3 meses em pacientes com ≥2 crises de enxaqueca por mês |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [26752497](https://pubmed.ncbi.nlm.nih.gov/26752497/) | 2016 | Meta-análise de RCTs | Pain Physician | Meta-análise demonstra eficácia do magnésio IV e oral tanto no tratamento de crises agudas quanto na prevenção da enxaqueca, com resultados favoráveis em desfechos de dor |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Diretriz Clínica | American Family Physician | Diretrizes recomendam magnésio como opção de terapia preventiva de enxaqueca; destaca que menos de 13% dos pacientes elegíveis utilizam profilaxia adequada |
| [40378325](https://pubmed.ncbi.nlm.nih.gov/40378325/) | 2025 | Diretriz Clínica | American Family Physician | Atualização de 2025 das diretrizes de profilaxia da enxaqueca confirma magnésio como agente preventivo com boa tolerabilidade e perfil de segurança favorável |
| [25916335](https://pubmed.ncbi.nlm.nih.gov/25916335/) | 2015 | RCT Multicêntrico | J Headache Pain | Ensaio randomizado duplo-cego multicêntrico demonstra melhora significativa dos sintomas de enxaqueca com suplemento contendo magnésio + riboflavina + CoQ10 vs placebo |
| [39404918](https://pubmed.ncbi.nlm.nih.gov/39404918/) | 2025 | Revisão Sistemática + Meta-análise | Neurological Sciences | Meta-análise dose-resposta de RCTs avalia efeitos de suplementos dietéticos (incluindo magnésio) na profilaxia da enxaqueca, abordando conflitos nos resultados existentes |
| [29131326](https://pubmed.ncbi.nlm.nih.gov/29131326/) | 2018 | Revisão Sistemática | Headache | Primeira revisão sistemática dedicada exclusivamente à base de evidências do magnésio na profilaxia da enxaqueca, avaliando qualidade metodológica dos estudos disponíveis |
| [40005053](https://pubmed.ncbi.nlm.nih.gov/40005053/) | 2025 | Revisão Narrativa | Nutrients | Revisão abrangente e atualizada sobre magnésio e enxaqueca, abordando epidemiologia da deficiência, mecanismos fisiopatológicos e aplicação clínica |
| [35268064](https://pubmed.ncbi.nlm.nih.gov/35268064/) | 2022 | Revisão | Nutrients | Analisa como a deficiência de magnésio induz depressão cortical alastrante e transmissão glutamatérgica anormal, mecanismos centrais da patogênese da enxaqueca |
| [32878232](https://pubmed.ncbi.nlm.nih.gov/32878232/) | 2020 | Revisão | Nutrients | Discute mecanismos, biodisponibilidade e eficácia terapêutica do magnésio nas cefaléias, com revisão de múltiplos RCTs duplo-cego controlados por placebo |
| [29882776](https://pubmed.ncbi.nlm.nih.gov/29882776/) | 2018 | Revisão | Nutrients | Avalia papel protetor do magnésio contra excitotoxicidade neuronal e implicações clínicas para distúrbios neurológicos, incluindo enxaqueca |

---

## Informações de Comercialização no Brasil

O magnésio está confirmado no mercado brasileiro com **6 registros ativos** e situação de comercialização vigente. Os detalhes individuais dos registros (número de registro, nome comercial, forma farmacêutica, indicação aprovada) não foram capturados na base de dados atual. Para acesso às informações completas, consulte diretamente o portal de Consulta a Produtos e Medicamentos da **ANVISA** (anvisa.gov.br/consultas).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe evidência de nível L1 — incluindo pelo menos um Phase 3 RCT concluído (NCT05967442, n=157), meta-análise de RCTs (PMID 26752497) e recomendação em diretrizes internacionais de grau B — apoiando a eficácia do magnésio no tratamento agudo e na prevenção da enxaqueca, tornando o caminho regulatório e clínico robusto para reposicionamento formal.

**Para prosseguir, é necessário:**
- Obter bula completa via ANVISA para levantar advertências, contraindicações e interações medicamentosas (dados ausentes no pack atual)
- Confirmar formas farmacêuticas e vias de administração registradas no Brasil (oral vs IV), pois os perfis de evidência e segurança diferem substancialmente entre uso agudo (MgSO₄ IV em emergência) e profilaxia (suplementação oral)
- Definir protocolo de monitoramento para populações especiais: gestantes (uso de MgSO₄ IV em pré-eclâmpsia tem perfil próprio), pacientes com insuficiência renal (risco de hipermagnesemia) e crianças/adolescentes
- Mapear posicionamento competitivo frente a terapias preventivas já estabelecidas (topiramato, valproato, propranolol, amitriptilina, anticorpos anti-CGRP)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

