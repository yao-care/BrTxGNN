---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

O skill `txgnn-pipeline` confirma o contexto do projeto. Agora gero o relatório com base no Evidence Pack fornecido:

---

# Sinvastatina: Da Dislipidemia à Hipercolesterolemia Familiar

## Resumo em Uma Frase

Sinvastatina é um inibidor da HMG-CoA redutase, amplamente reconhecido no tratamento da dislipidemia e hipercolesterolemia primária em todo o mundo.
O modelo TxGNN prevê que pode ser eficaz para a **Hipercolesterolemia Familiar (Familial Hypercholesterolemia)**,
atualmente com **19 ensaios clínicos** e **18 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dislipidemia / Hipercolesterolemia (inibidor da HMG-CoA redutase) |
| Nova Indicação Prevista | Hipercolesterolemia Familiar (Familial Hypercholesterolemia) |
| Pontuação de Previsão TxGNN | 99.63% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não registrado na ANVISA |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Sinvastatina é um inibidor da enzima 3-hidroxi-3-metilglutaril-coenzima A (HMG-CoA) redutase, enzima-chave na via do mevalonato responsável pela síntese hepática endógena de colesterol. Ao bloquear esta etapa, a sinvastatina reduz a produção hepática de colesterol e, compensatoriamente, induz as células hepáticas a superexpressar receptores de LDL — resultando em captação aumentada de LDL circulante e redução significativa dos níveis séricos de LDL-C.

A Hipercolesterolemia Familiar (FH) é uma doença genética monogênica causada por mutações nos genes *LDLR*, *APOB* ou *PCSK9*, que comprometem a clearance do LDL circulante. Embora a sinvastatina não corrija o defeito genético subjacente, ela atua na fonte do problema ao reduzir a quantidade de LDL produzida pelo fígado — diminuindo a carga sobre os receptores funcionalmente deficientes e, consequentemente, o risco de doença coronariana prematura. Pacientes com a forma heterozigótica (HeFH) respondem bem a estatinas em monoterapia, com redução média de 40–50% no LDL-C.

A relação mecanística é direta e há décadas consolidada: estudos de Phase 3 demonstraram eficácia de sinvastatina em FH tanto em adultos quanto em adolescentes, e diretrizes internacionais (ACC/AHA 2026, AACE/ACE 2017) recomendam estatinas como base do tratamento de FH. A previsão do modelo TxGNN é, portanto, altamente coerente com o conhecimento farmacológico estabelecido.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Concluído | 720 | ENHANCE Trial: ezetimiba + sinvastatina em alta dose vs. sinvastatina isolada em HeFH — avaliou progressão da aterosclerose carotídea (espessura íntima-média); maior estudo direto de sinvastatina em FH. |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Concluído | 248 | Eficácia e segurança de ezetimiba em coadministração com sinvastatina em adolescentes (10–17 anos) com HeFH; estudo randomizado duplo-cego multicêntrico comparando monoterapia vs. combinação. |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Concluído | 199 | SUPREME: Niacin ER + sinvastatina vs. atorvastatina em hiperlipidemia tipo II ou dislipidemia mista; sinvastatina como braço comparador principal em estudo de não inferioridade para HDL-C. |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Concluído | 442 | Efeitos renais de rosuvastatina e sinvastatina em dislipidemia Fredrickson Tipo IIa/IIb, incluindo HeFH; estudo randomizado paralelo de 6 semanas avaliando segurança renal comparativa. |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Concluído | 50 | Eficácia e segurança de ezetimiba (SCH 58235) adicionada a atorvastatina ou sinvastatina em HoFH; estudo duplo-cego randômico de 12 semanas. |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Concluído | 44 | Segurança e tolerabilidade de longo prazo (24 meses) de ezetimiba + atorvastatina ou sinvastatina em HoFH; extensão aberta do estudo NCT03884452. |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Concluído | 486 | Alirocumab vs. placebo em HeFH não controlada com terapia modificadora de lipídios; sinvastatina como terapia de base, avaliando benefício adicional do inibidor de PCSK9. |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Concluído | 249 | Alirocumab (REGN727) em HeFH inadequadamente controlada com terapia lipídica modificadora; estudo duplo-cego multinacional com sinvastatina como fundo terapêutico. |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Concluído | 216 | Alirocumab adicionado à terapia estável com estatina em HeFH ou pacientes de alto risco cardiovascular; avaliação de redução de LDL-C após 24 semanas. |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Concluído | 194 | Colesevelam em pacientes pediátricos (10–17 anos) com HeFH em dose estável de estatina (incluindo sinvastatina) ou virgens de tratamento; avaliação do efeito redutor de lipídios em combinação. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | Sinvastatina ± ezetimiba em FH (ENHANCE): combinação reduziu LDL-C em maior extensão, mas sem diferença significativa na progressão da espessura íntima-média carotídea em 2 anos; referência metodológica central em FH. |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | RCT | J Am Coll Cardiol | Eficácia e segurança da coadministração de ezetimiba e sinvastatina em adolescentes com HeFH: combinação demonstrou redução adicional de LDL-C com perfil de segurança aceitável em longo prazo. |
| [2405804](https://pubmed.ncbi.nlm.nih.gov/2405804/) | 1990 | RCT | Arch Intern Med | Sinvastatina vs. colestiramina em hipercolesterolemia familiar e não familiar (251 pacientes, multicêntrico): sinvastatina 40 mg/dia reduziu LDL-C em 40%, demonstrando eficácia superior ao controle ativo. |
| [8770319](https://pubmed.ncbi.nlm.nih.gov/8770319/) | 1995 | RCT | Atherosclerosis | Comparação dos efeitos de sinvastatina e pravastatina na biossíntese de colesterol em hipercolesterolemia primária; estudo cruzado randomizado (26 pacientes, 6 semanas). |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisão Sistemática | Cochrane Database Syst Rev | Cochrane 2019: estatinas para crianças com FH; análise sistemática confirmando eficácia e segurança do uso de estatinas (incluindo sinvastatina) na população pediátrica com FH. |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Diretriz Clínica | Circulation | Diretriz 2026 ACC/AHA sobre Manejo da Dislipidemia: substitui a diretriz de 2018; referência atual de evidência para o uso de estatinas em FH com recomendações baseadas nas evidências mais recentes. |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Diretriz Clínica | J Am Coll Cardiol | Publicação simultânea da Diretriz 2026 ACC/AHA sobre Manejo da Dislipidemia no JACC; recomendações de tratamento lipídico para hipercolesterolemia familiar (publicação dupla conjunta). |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Diretriz Clínica | Endocrine Practice | Diretrizes AACE/ACE para Manejo da Dislipidemia e Prevenção de Doenças Cardiovasculares; inclui recomendações de estatinas como cornerstone do tratamento em FH. |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Revisão | Expert Opin Drug Saf | Avaliação de benefícios e riscos da sinvastatina em hipercolesterolemia familiar: expectativa de vida reduzida em 15–30 anos sem tratamento adequado; sinvastatina muda a história natural da doença com perfil de segurança favorável em longo prazo. |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisão | Drug Safety | Benefícios e riscos da sinvastatina em FH: introdução dos inibidores de HMG-CoA redutase como transformação no tratamento desta doença; análise de segurança e tolerabilidade de longo prazo. |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existem múltiplos ensaios clínicos de Phase 3 concluídos — incluindo estudos que avaliaram sinvastatina diretamente em FH heterozigótica e homozigótica — corroborados pelas diretrizes internacionais mais recentes (ACC/AHA 2026, AACE/ACE 2017) e por revisão sistemática Cochrane. A pontuação TxGNN de 99,63% e o nível de evidência L1 (≥2 Phase 3 RCTs concluídos) conferem alta confiança à previsão; trata-se da indicação com suporte científico mais robusto no portfólio previsto para este fármaco.

**Para prosseguir, é necessário:**
- Verificar o status de registro na ANVISA: os dados disponíveis indicam ausência de produtos de sinvastatina registrados no Brasil (0 licenças), o que requer investigação e eventual processo de regularização regulatória
- Obter dados completos de segurança (advertências, contraindicações, interações medicamentosas) a partir da bula aprovada por agência regulatória de referência (FDA/EMA/ANVISA)
- Definir protocolo de monitoramento para populações especiais: crianças e adolescentes (10–17 anos) e pacientes com HoFH (onde a resposta à sinvastatina em monoterapia é limitada e estratégias combinadas são necessárias)
- Considerar interações medicamentosas clinicamente relevantes (ex.: inibidores de CYP3A4, fibratos, niacina) no contexto de uso combinado frequente em FH
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

