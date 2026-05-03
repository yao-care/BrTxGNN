---
layout: default
title: Prednisolone
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone: Das Doenças Inflamatórias à Alopecia Areata

## Resumo em Uma Frase

Prednisolone é um corticosteroide sintético historicamente utilizado no controle de condições inflamatórias, alérgicas e autoimunes.
O modelo TxGNN prevê que pode ser eficaz para **Alopecia Areata (alopecia areata)**,
atualmente com **18 ensaios clínicos** e **20 publicações** apoiando essa direção.
As evidências incluem uma meta-análise em rede Cochrane, revisões sistemáticas e um estudo placebo-controlado com prednisolone oral em pulso diretamente nesta condição.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doenças inflamatórias, alérgicas e autoimunes (corticosteroide sistêmico) |
| Nova Indicação Prevista | Alopecia Areata (alopecia areata) |
| Pontuação de Previsão TxGNN | 99.99% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado (0 registros encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

A alopecia areata (AA) é uma doença autoimune mediada por células T CD8+, que atacam os folículos pilosos e destroem o "privilégio imunológico" local — uma proteção imunológica normalmente presente no folículo. O processo envolve a suprarregulação de MHC I na superfície celular folicular e a expressão excessiva de IFN-γ pelos linfócitos infiltrantes, sinalando os folículos como alvos autoimunes. Prednisolone atua por meio dos receptores de glucocorticoides (GR), suprimindo citocinas Th1 (IFN-γ, IL-2, TNF-α), reduzindo a expressão de MHC I e restaurando o estado de privilégio imunológico do folículo. Esse mecanismo é diretamente compatível com a fisiopatologia da AA.

A relação entre a indicação original (doenças autoimunes inflamatórias) e a nova indicação prevista é fisiopatologicamente coerente: ambas envolvem desregulação imune mediada por células T, com inflamação perifolicular como denominador comum. De fato, o uso de corticosteroides sistêmicos em pulso para alopecia areata está documentado na literatura clínica desde a década de 1950, foi avaliado em estudo placebo-controlado publicado no *Journal of the American Academy of Dermatology* (PMID 15692475), e consta de revisões sistemáticas contemporâneas e meta-análises em rede Cochrane (PMID 37870096, PMID 30191561) como opção terapêutica reconhecida.

As principais limitações desta previsão são a ausência de um Phase 2/3 RCT dedicado exclusivamente ao prednisolone oral em AA — a maioria dos ensaios recentes foca em inibidores de JAK (baricitinib, ruxolitinib) como alternativas de segunda linha — e os efeitos adversos conhecidos do uso prolongado, que incluem supressão do eixo HPA, osteoporose, hiperglicemia e ganho de peso. Por esse motivo, a decisão é "Proceed with Guardrails", condicionada a protocolos de monitoramento rigoroso.

---

## Evidências de Ensaios Clínicos

Dos 18 ensaios clínicos recuperados pela coleta automática, os três mais relevantes para prednisolone em alopecia areata são apresentados abaixo. A maioria dos demais ensaios na coleção refere-se a lúpus eritematoso sistêmico (LES) ou a fármacos distintos (inibidores de JAK, agentes biológicos), sendo identificados como ruído de coleta por sobreposição de nós de doenças autoimunes no grafo de conhecimento.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Concluído | 42 | Avalia segurança e eficácia da megapulse oral de metilprednisolona em AA severa refratária (incluindo alopecia totalis e universalis); testa doses mais altas e pulsos mais frequentes do que os protocolos anteriores para superar a falta de resposta |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Desconhecido | 20 | Comparação de dois métodos de injeção intralesional de corticosteroide em AA — seringa convencional versus DERMOJET (seringa sem agulha) — avaliando eficácia, segurança e conveniência de uso para médico e paciente |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Concluído | 296 | Estudo observacional prospectivo de tofacitinib em alopecia; participantes receberam tofacitinib com ou sem prednisolone adjuvante, permitindo avaliação do perfil de segurança e efetividade da combinação em ambiente clínico real |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Meta-análise em Rede | Cochrane Database Syst Rev | NMA Cochrane comparando múltiplos tratamentos para AA; síntese mais abrangente disponível sobre eficácia relativa das intervenções, incluindo corticosteroides sistêmicos |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Revisão Sistemática | Australasian J Dermatology | Revisão de literatura (1946–2018) sobre tratamentos sistêmicos para AA, AT e AU; consolida corticosteroides sistêmicos como opção terapêutica com base em evidências |
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | ECR Placebo-Controlado | J Am Acad Dermatology | Primeiro estudo randomizado placebo-controlado de prednisolone oral em pulso para AA; evidência direta de eficácia do prednisolone nesta indicação específica |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Estudo Clínico | Dermato-endocrinology | Prednisolone em dose média em pulso para AA; confirma eficácia em fases iniciais, com nota sobre efeitos colaterais significativos que podem levar à descontinuação do tratamento |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisão Narrativa | Dermatology Pract Conceptual | Revisão de eficácia, taxas de recaída, efeitos adversos e fatores prognósticos dos diferentes regimes de pulsoterapia com corticosteroide em AA |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Coorte Retrospectiva | Dermatologic Therapy | Análise de 26 pacientes com AA extensa tratados com metilprednisolona ± metotrexato; avalia se a terapia combinada é superior à monoterapia com corticosteroide |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisão Clínica | Pediatric Dermatology | Revisão de regimes de pulsoterapia com corticosteroide em crianças com AA; consolida evidências sobre dosagem pediátrica e efeitos adversos nesta faixa etária |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Coorte Retrospectiva | JDDG | Corticoterapia sistêmica sequencial (alta dose → dose subterapêutica) em crianças com AA severa; sugere que manter dose baixa abaixo do limiar de Cushing após pulsoterapia pode reduzir recaídas |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Estudo de Acompanhamento | Dermatologic Therapy | Acompanhamento de longo prazo (mediana 96 meses) de 65 crianças com AA severa (>30% do couro cabeludo) tratadas com dexametasona oral em pulso equivalente + corticosteroide tópico |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Estudo Retrospectivo | J Eur Acad Dermatol Venereol | Análise de 138 pacientes com AA crônica; compara taxas de continuidade de agentes poupadores de esteroides (azatioprina, metotrexato, ciclosporina) usados como adjuvantes ao prednisolone sistêmico |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A fisiopatologia da alopecia areata é diretamente compatível com o mecanismo de ação dos corticosteroides, e há evidências de nível L3 — incluindo uma meta-análise em rede Cochrane, revisões sistemáticas e um estudo placebo-controlado com prednisolone oral em pulso — que apoiam o uso nesta indicação. O prednisolone integra o arsenal dermatológico para AA em prática clínica global e é considerado opção de resgate nos casos em que os inibidores de JAK são contraindicados ou inacessíveis.

**Para prosseguir, é necessário:**
- Dados completos de segurança (advertências, contraindicações, interações medicamentosas) da bula ou monografia oficial
- Dados de mecanismo de ação (MOA) formais obtidos via DrugBank API para formalizar a análise mecanística
- Verificação independente do status regulatório junto à ANVISA — os 0 registros encontrados podem refletir limitação de busca e não a ausência real do produto no mercado brasileiro
- Plano estruturado de monitoramento de efeitos adversos de longo prazo, abrangendo: supressão do eixo HPA, densidade mineral óssea (osteoporose), glicemia (hiperglicemia/diabetes), pressão intraocular (catarata/glaucoma) e composição corporal
- Definição de protocolo de dosagem (dose, frequência e duração da pulsoterapia) alinhado com os estudos disponíveis (PMID 15692475; PMID 21572877) e adaptado ao perfil do paciente (adulto vs. pediátrico, extensão da alopecia)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

