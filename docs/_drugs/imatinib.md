---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Imatinib
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

A seguir está o relatório completo em formato Markdown, com foco editorial na indicação de evidência mais robusta (Neoplasia Fibrobástica, rank #2) em vez do rank #1 (fibrossarcoma cardíaco), cujas evidências são insuficientes para gerar um relatório acionável. A nota editorial abaixo do resumo explica essa escolha.

---

# Imatinib: Da Leucemia Mieloide Crônica à Neoplasia Fibrobástica

## Resumo em Uma Frase

Imatinib (Glivec®/Gleevec®) é um inibidor de tirosina quinase originalmente aprovado para o tratamento da leucemia mieloide crônica (LMC) e do tumor estromal gastrointestinal (GIST), atuando pela inibição seletiva das quinases BCR-ABL, KIT e PDGFR. O modelo TxGNN prevê eficácia para **Neoplasia Fibrobástica (Fibroblastic Neoplasm)** — categoria que inclui o dermatofibrossarcoma protuberans (DFSP), cujo uso com imatinib foi aprovado pela FDA em 2006 —, com **1 ensaio clínico fase 2** e **20 publicações** apoiando essa direção, incluindo um guideline europeu interdisciplinar de 2025.

> **Nota editorial**: O TxGNN atribuiu o maior score (#1) ao **fibrossarcoma cardíaco (heart fibrosarcoma)**, indicação com evidências muito limitadas (nível L4, recomendação Hold, apenas 1 publicação). A segunda predição — **Neoplasia Fibrobástica (#2, score praticamente idêntico, 99.94%)** — concentra evidências substancialmente mais robustas e constitui o foco principal deste relatório.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Leucemia mieloide crônica (LMC) e tumor estromal gastrointestinal (GIST) |
| Nova Indicação Prevista | Neoplasia Fibrobástica (Fibroblastic Neoplasm) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Imatinib é um inibidor seletivo de tirosina quinase de baixo peso molecular que bloqueia três alvos moleculares centrais: **BCR-ABL** (fusão oncogênica presente na LMC), **KIT** (receptor com mutação de ganho de função em GISTs) e **PDGFR-α/β** (receptores do fator de crescimento derivado de plaquetas). Em todos esses contextos, a eficácia do fármaco decorre diretamente da supressão de quinases constitutivamente ativas — não de citotoxicidade inespecífica, o que confere um perfil de atividade seletiva por biologia molecular.

As neoplasias fibrobásticas, em especial o **dermatofibrossarcoma protuberans (DFSP)**, apresentam uma translocação cromossômica altamente específica: **t(17;22)(q22;q13)**, que funde o gene do colágeno tipo 1 alfa 1 (*COL1A1*) ao gene *PDGFB*. Essa fusão leva à superexpressão de PDGFB, que ativa o PDGFR-β de forma autócrina e parácrina — exatamente um dos alvos primários do imatinib. A conexão molecular é direta, confirmada por patologia molecular, e está presente em mais de 90% dos casos de DFSP.

Esse raciocínio foi validado clinicamente: o imatinib recebeu **aprovação acelerada da FDA para DFSP avançado ou metastático em 2006**, com base em estudos fase 2 demonstrando resposta objetiva. O **guideline europeu interdisciplinar de 2024/2025** (EADO/EDF/UEMS/EADV) recomenda formalmente o uso de imatinib para doença irressecável. O modelo TxGNN está, portanto, reconhecendo uma relação biológica já farmacologicamente estabelecida — o que aumenta substancialmente a confiabilidade desta previsão para o grupo dos tumores fibrobásticos.

---

## Evidências de Ensaios Clínicos

Para a categoria de neoplasia fibrobástica, o ensaio mais diretamente relevante foca especificamente em DFSP e fibrossarcoma de células gigantes com a translocação molecular COL1A1/PDGFB:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Concluído | 17 | Imatinib em DFSP e fibrossarcoma de células gigantes (GCF) localmente avançados ou metastáticos com translocação COL1A1/PDGFB confirmada — constitui a base do racional para a aprovação acelerada pela FDA |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline Clínico | Eur J Cancer | Guideline europeu interdisciplinar de DFSP (EADO/EDF/EADV, atualização 2024): imatinib recomendado formalmente para doença localmente avançada ou irressecável |
| [33449152](https://pubmed.ncbi.nlm.nih.gov/33449152/) | 2021 | Review | Cell Mol Life Sci | Mutações em PDGFRA/PDGFRB em doenças humanas — confirma a base molecular da atividade do imatinib em neoplasias fibrobásticas e mieloides |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Review | Dermatol Clin | DFSP: alta taxa de recorrência local e comportamento infiltrativo; imatinib recomendado para doença avançada e irressecável conforme diretrizes NCCN |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Review | Curr Treat Options Oncol | DFSP: abordagem multidisciplinar; imatinib indicado para casos em que margens cirúrgicas negativas não são factíveis |
| [30297237](https://pubmed.ncbi.nlm.nih.gov/30297237/) | 2018 | Review | Bull Cancer | Translocação t(17;22)(q22;q13) como marcador diagnóstico específico do DFSP; risco de recidiva relacionado à qualidade cirúrgica; imatinib para doença localmente avançada |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Review | Expert Rev Anticancer Ther | Imatinib como tratamento sistêmico de referência para DFSP avançado; revisão crítica das evidências disponíveis e perspectivas terapêuticas |
| [35038826](https://pubmed.ncbi.nlm.nih.gov/35038826/) | 2022 | Phase 2 Trial | Cancer Res Treat | NOTCH2 e HES1 identificados como potenciais biomarcadores de resposta ao imatinib em tumor desmoide (fibromatose agressiva) — relevante para predição de resposta em neoplasias fibrobásticas |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Translacional | Mol Cancer Ther | Perda de CDKN2A/p16 implica CDK4 como alvo terapêutico em DFSP resistente ao imatinib — relevante para estratégias de segunda linha após falha |
| [39580648](https://pubmed.ncbi.nlm.nih.gov/39580648/) | 2025 | Genética Clínica | Genet Med | Variante germline em PDGFRB associada a miofibromatose infantil multifocal e resistência ao imatinib — implicações para triagem genética pré-tratamento |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opin Drug Saf | Desenvolvimento e aplicação clínica do imatinib: mecanismo de inibição de TK, perfil de segurança e expansão para sarcomas de partes moles |

---

## Informações de Comercialização no Brasil

O imatinib possui **20 registros ativos na ANVISA**, confirmando ampla disponibilidade no mercado brasileiro. Os dados individuais de cada licença (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack.

> Recomenda-se consulta direta ao portal ANVISA (https://consultas.anvisa.gov.br/) para verificar quais indicações estão aprovadas nos registros brasileiros vigentes — em especial, se o DFSP já consta nas bulas registradas no Brasil.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — inibidor seletivo de tirosina quinase (BCR-ABL / KIT / PDGFR-α/β); não é citotóxico convencional |
| Risco de Mielossupressão | Médio — neutropenia, trombocitopenia e anemia são efeitos adversos reconhecidos, especialmente em doses mais altas ou em pacientes com doença hematológica de base |
| Classificação de Emetogenicidade | Baixa a média — náusea é frequente, geralmente manejável com administração junto às refeições |
| Itens de Monitoramento | Hemograma completo com diferencial (semanal nas primeiras 4 semanas, depois mensalmente), transaminases (ALT/AST), bilirrubinas, creatinina, peso corporal e sinais clínicos de retenção hídrica/edema periférico |
| Proteção no Manuseio | Seguir protocolos institucionais para antineoplásicos orais; evitar manipulação de comprimidos partidos; descarte como resíduo de quimioterapia conforme ANVISA |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O imatinib possui mecanismo de ação diretamente confirmado para neoplasias fibrobásticas com PDGFR-β ativado pela fusão COL1A1-PDGFB. O DFSP — principal representante dessa categoria — já conta com aprovação regulatória consolidada pela FDA desde 2006 e recomendação formal em guideline europeu de 2025, o que eleva substancialmente a confiança na previsão do TxGNN e abre espaço para exploração em subtipos fibrobásticos relacionados mediante triagem molecular prévia.

**Para prosseguir, é necessário:**
- Consultar o portal ANVISA para confirmar se o DFSP já está incluído nas bulas dos 20 registros brasileiros vigentes; se não estiver, avaliar a viabilidade de extensão de indicação
- Obter os dados formais de MOA completo e advertências da bula ANVISA (identificados como Data Gap neste Evidence Pack) para completar a avaliação de segurança na fase S1
- Para extensão a subtipos sem fusão COL1A1-PDGFB confirmada (fibrossarcoma convencional, fibrossarcoma renal, fibrossarcoma cardíaco), exigir **triagem molecular prévia de expressão de PDGFR/KIT** antes de qualquer inclusão em protocolos clínicos
- Verificar interações medicamentosas via banco de dados DDI atualizado (a consulta retornou "not\_found" neste pacote de evidências)
- Para fibrossarcoma cardíaco (predição TxGNN #1): dado o caráter ultrararo da indicação, considerar série de casos clínicos como primeiro passo investigativo antes de qualquer ensaio clínico formal
---

