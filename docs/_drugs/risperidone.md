---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Com base no Evidence Pack fornecido, utilizando as diretrizes do `txgnn-pipeline` e o formato de relatório de reposicionamento especificado, aqui está o relatório completo:

---

# Risperidona: Do Transtorno Psicótico ao Transtorno Afetivo Maior

## Resumo em Uma Frase

Risperidona é um antipsicótico atípico de segunda geração globalmente estabelecido para o tratamento de esquizofrenia e transtorno bipolar, porém sem registro identificado na ANVISA com base nos dados disponíveis.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno Afetivo Maior (Major Affective Disorder)** — englobando depressão resistente ao tratamento (TRD) e episódios maníacos bipolares —, atualmente com **36 ensaios clínicos** (incluindo 4 estudos de Fase 3 concluídos) e **20 publicações** (incluindo revisão Cochrane e meta-análises de rede) apoiando esta direção.

> **Nota de escopo:** Este é um pacote multi-indicação (`TW-DB00734-multi`) com 6 indicações previstas pelo TxGNN. O relatório foca na indicação com maior suporte de evidências clínicas (Transtorno Afetivo Maior, Nível L1). Um panorama das demais indicações consta ao final do documento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Esquizofrenia / Transtorno Bipolar (uso global consolidado; sem registro ANVISA identificado) |
| Nova Indicação Prevista | Transtorno Afetivo Maior (Major Affective Disorder) |
| Pontuação de Previsão TxGNN | 99,11% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, os dados formais de mecanismo de ação não estão disponíveis neste pacote de evidências. Com base no conhecimento publicado amplamente documentado, risperidona é um antagonista de múltiplos receptores: **D2 (dopamina)**, **5-HT2A (serotonina)** e **α1-adrenérgico**. O bloqueio D2 no estriado ventral controla a hiperatividade dopaminérgica associada à mania; o antagonismo 5-HT2A desinibe a liberação de dopamina no córtex pré-frontal, potencializando o efeito antidepressivo quando associado a inibidores da recaptação de serotonina (SRI/SNRI); e o bloqueio α1 modula o sistema noradrenérgico, contribuindo para a estabilização do humor.

O transtorno afetivo maior e o espectro psicótico compartilham circuitos dopaminérgicos e serotoninérgicos desregulados — o que torna o perfil farmacológico da risperidona biologicamente plausível em ambos os contextos. A drug já é amplamente empregada como agente de *augmentation* (associação com antidepressivos) no TRD e como estabilizador de humor no transtorno bipolar, contextos que o modelo TxGNN detectou a partir das conexões da rede de conhecimento. Mecanisticamente, o triplo antagonismo D2/5-HT2A/α1 confere à risperidona um perfil de ação sobre os três principais sistemas de neurotransmissores implicados nos transtornos afetivos maiores.

O nível de evidência L1 é o mais robusto deste pacote: quatro ensaios de Fase 3 concluídos e múltiplas revisões sistemáticas com meta-análise — incluindo uma revisão Cochrane e uma meta-análise de rede — sustentam a eficácia da risperidona em transtornos afetivos maiores. Em muitos países (EUA, Europa), a indicação para mania aguda bipolar e TRD já é reconhecida na prática clínica e em diretrizes terapêuticas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|--------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Concluído | 630 | Risperidona adjuvante vs. placebo em TDM com resposta subótima a antidepressivos — maior ensaio de Fase 3 direto em TRD |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Concluído | 585 | Risperidona LAI vs. placebo (com olanzapina como controle ativo) na prevenção de episódios de humor em transtorno bipolar I |
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | Concluído | 453 | Licarbazepina adjuvante a antipsicótico atípico (incluindo risperidona) em episódios maníacos do transtorno bipolar I — estudo duplo-cego multicêntrico |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Concluído | 379 | Estudo TEAM: lítio vs. valproato vs. risperidona em mania precoce (crianças e adolescentes) |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Concluído | 258 | Eficácia e manutenção de risperidona como augmentation de SSRI em depressão resistente vs. placebo |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Concluído | 111 | Risperidona em monoterapia para transtorno bipolar ambulatorial com ansiedade comórbida (pânico/TAG) — duplo-cego controlado por placebo |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Concluído | 46 | Ensaio controlado de valproato vs. risperidona em crianças de 3–7 anos com transtorno bipolar |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Concluído | 42 | Piloto duplo-cego: risperidona vs. olanzapina como adjuvante a SSRI em depressão resistente — comparação direta head-to-head |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | Concluído | 283 | Estudo LiTMUS: efetividade de lítio vs. tratamento otimizado (com risperidona como referência) em transtorno bipolar — dados de mundo real |
| [NCT02870283](https://clinicaltrials.gov/study/NCT02870283) | Phase 4 | Concluído | 107 | Custo-efetividade e qualidade de vida de intervenções para episódios mistos de transtorno bipolar no SUS — relevância direta ao contexto brasileiro |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + Network Meta-analysis | Journal of Affective Disorders | Comparação de estratégias de augmentation em TRD em adultos — risperidona incluída entre os agentes avaliados |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review + Meta-analysis | Journal of Psychopharmacology | Eficácia de tratamentos de augmentation/combinação em TRD inicial — risperidona avaliada entre antipsicóticos |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review + Meta-analysis | Psychological Medicine | Meta-análise abrangente de antipsicóticos (monoterapia e adjuvância) em TDM — avaliação de eficácia e tolerabilidade |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Revisão Cochrane: antipsicóticos de segunda geração em TDM e distimia — referência de mais alta qualidade metodológica |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematic Review | Journal of Psychopharmacology | Eficácia e tolerabilidade de antidepressivos + SGAs vs. esketamina vs. lítio em TDM |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review / Practice Guideline | Acta Psychiatrica Scandinavica | Revisão de tratamento baseado em evidências para mania bipolar — risperidona citada entre opções de primeira linha |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Population-based Study | Journal of Clinical Psychiatry | Efetividade de aripiprazol, olanzapina, quetiapina e risperidona em augmentation para TDM — estudo de base populacional nacional |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Ensaio randomizado de risperidona para TDM refratário — publicado em periódico clínico de alto impacto |
| [7545159](https://pubmed.ncbi.nlm.nih.gov/7545159/) | 1995 | Early Clinical Study | Journal of Clinical Psychiatry | Estudo clínico pioneiro de risperidona em transtornos afetivos e TOC — base histórica da indicação |
| [40430486](https://pubmed.ncbi.nlm.nih.gov/40430486/) | 2025 | Review | Pharmaceuticals (Basel) | Novos agentes e novas indicações em transtornos psiquiátricos — contextualização atual da risperidona no cenário terapêutico |

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Os dados de advertências principais, contraindicações e interações medicamentosas não foram disponibilizados neste pacote de evidências e devem ser obtidos diretamente junto à ANVISA ou à bula internacional (FDA/EMA) como passo imediato antes da avaliação clínica.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Múltiplos ensaios de Fase 3 concluídos — incluindo o maior estudo de TRD (N=630) e o maior estudo de prevenção de episódios bipolares (N=585) — somados a uma revisão Cochrane e meta-análises de rede confirmam a eficácia da risperidona em transtornos afetivos maiores. A ausência de registro ANVISA é a principal barreira operacional, não uma barreira de evidências clínicas.

**Para prosseguir, é necessário:**
- Verificar o registro ANVISA atualizado via portal de consultas (https://consultas.anvisa.gov.br/) — possível discrepância na base de dados utilizada
- Obter bula ANVISA ou bula internacional (FDA label) para mapeamento de advertências e contraindicações **[DG001 — bloqueante para avaliação S1]**
- Consultar DrugBank API para dados formais de MOA **[DG002 — impacto na análise mecanicista]**
- Definir estratégia regulatória: importação por vias legais, pedido de novo registro ou petição para extensão de indicação
- Avaliar caminho de acesso via SUS para transtorno bipolar (existe dado de custo-efetividade favorável no contexto brasileiro, NCT02870283)
- Para tricotilomania (L3): desenvolver protocolo prospectivo de Fase 2 como próximo passo clínico
- Para Síndrome de Phelan-McDermid (L4): avaliar estudo iniciado por investigador com base no modelo pré-clínico shank3/zebrafish

---

## Panorama das Demais Indicações Previstas

| Rank TxGNN | Indicação | Score | Nível | Recomendação | Observações |
|-----------|-----------|-------|-------|--------------|-------------|
| 1 | Gaze palsy familiar horizontal com escoliose progressiva | 99,76% | L5 | Hold | Provável falso-positivo topológico: mutação ROBO3 causa defeito anatômico no cruzamento axonal — nenhuma conexão mecanicista D2/5-HT2A documentada |
| 2 | Síndrome de Asperger (susceptibilidade) | 99,74% | L5* | Hold | **Atenção — viés de dados:** risperidona é aprovada pelo FDA para irritabilidade em TEA; Asperger integra o TEA no DSM-5. O nível L5 reflete ausência de dados no banco de busca, não ausência de evidências reais. Recomenda-se reavaliação após complementação bibliográfica (esperado L2–L3) |
| 3 | Síndrome amelocerebrohipoidrótica | 99,69% | L5 | Hold | Doença ultra-rara (defeito em canais Ca²⁺/Mg²⁺); nenhuma hipótese mecanicista plausível com perfil D2/5-HT2A |
| 4 | Síndrome de Phelan-McDermid (22q13.3) | 99,59% | L4 | Research Question | 3 publicações; modelo zebrafish *shank3* suporta efeito de risperidona em comportamentos sensoriais; conexão via circuito ASD/D2 biologicamente plausível |
| 5 | Tricotilomania | 99,51% | L3 | Research Question | 10 publicações (série de casos consistente + revisão 2025); estratégia de augmentation SRI + risperidona descrita em múltiplos relatos; ausência de RCT é o principal gargalo |
| **6** | **Transtorno Afetivo Maior** *(foco deste relatório)* | **99,11%** | **L1** | **Proceed with Guardrails** | **36 ensaios clínicos, 4 de Fase 3 concluídos, revisão Cochrane e meta-análises de rede — maior base de evidências do pacote** |
---

