---
layout: default
title: Inositol
parent: Apenas Predição do Modelo (L5)
nav_order: 368
evidence_level: L5
indication_count: 9
monitor_inn: "INOSITOL"
predicted_indications: ["idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatic porphyria", "congestive heart failure", "acute pulmonary heart disease", "glycogen storage disease due to hepatic glycogen synthase deficiency"]
last_modified_at: 2026-10-31
description: "Inositol: nova indicação prevista, Cirrose associada ao cobre idiopática (idiopathic copper-associated c… (nível de evidência L5). Indicação original: Sem texto de indicação aprovada nos registros. N…"
---

# Inositol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Inositol: Cirrose associada ao cobre idiopática
{: .text-alpha }

## Resumo em Uma Frase

O inositol é uma substância de tipo vitamínico, que na base de conhecimento do modelo aparece associada a condições como pelagra, beribéri e dislipidemias (hipertrigliceridemia, hiperlipidemia familiar combinada e hipoalfalipoproteinemia).
O modelo TxGNN prevê, entre as indicações com alguma literatura, que possa ser útil para **insuficiência cardíaca congestiva (Congestive Heart Failure)**, com **0 ensaios clínicos** e **20 publicações** (todas indiretas, sobretudo pré-clínicas e de revisão) nessa direção.
As previsões de maior pontuação (doenças hepáticas e da circulação portal) não têm nenhum estudo de apoio.

> Observação: as indicações originais acima são relações registradas na base de conhecimento, não indicações aprovadas. Os registros brasileiros do inositol não trazem texto de indicação aprovada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem texto de indicação aprovada nos registros. Na base de conhecimento: pelagra, beribéri, hipertrigliceridemia, hiperlipidemia familiar combinada, hipoalfalipoproteinemia |
| Nova Indicação Prevista (maior pontuação) | Cirrose associada ao cobre idiopática (idiopathic copper-associated cirrhosis) |
| Nova Indicação Prevista (com literatura) | Insuficiência cardíaca congestiva (congestive heart failure) |
| Pontuação de Previsão TxGNN | 0,9998 (cirrose associada ao cobre); 0,9944 (insuficiência cardíaca congestiva) |
| Nível de Evidência | L5 (cirrose associada ao cobre); L5 (insuficiência cardíaca congestiva, ver justificativa abaixo) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 29) |
| Número de Registros | 29 (ativos: 1) |
| Decisão Recomendada | Hold |

Nota sobre o nível de evidência: embora o conjunto de dados classifique a insuficiência cardíaca como L4, nenhuma das publicações recuperadas testa o inositol como intervenção nessa doença. O estudo mais próximo (PMID 39121579) é uma coorte que mede o mielo-inositol plasmático como biomarcador, sem avaliar tratamento. Pela regra de teto de evidência, o nível aplicável é L5.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação do inositol nos dados compilados para este relatório. Sabe-se, de forma geral, que o mielo-inositol é precursor de fosfoinositídeos e do inositol 1,4,5-trisfosfato (IP3), segundo mensageiro que controla a liberação de cálcio intracelular. Isso é conhecimento geral, não consta como dado do fármaco no material analisado.

A literatura recuperada relaciona a sinalização de cálcio dependente de IP3 à hipertrofia cardíaca e à insuficiência cardíaca (por exemplo, PMID 22834797 e PMID 9476544). Isso é um caminho plausível, mas não comprovado. Além disso, um estudo de coorte (PMID 39121579) mostrou mielo-inositol **elevado** no plasma de pacientes com insuficiência cardíaca e sugeriu que ele pode induzir estresse oxidativo e ser prejudicial à função cardíaca. Ou seja, o sentido do efeito é incerto e pode até ser contrário ao terapêutico.

Para as demais previsões de topo (hipertensão portal familiar não cirrótica de início precoce, síndrome hepatopulmonar, esclerose hepatoportal, trombose da veia porta primitiva, porfiria hepática), a pontuação de 0.9998 é idêntica entre doenças hepáticas e vasculares portais; essa pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Não há ensaios nem publicações que as sustentem.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para insuficiência cardíaca congestiva (as demais previsões de topo não têm literatura). Seleção das publicações mais próximas ao inositol:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39121579](https://pubmed.ncbi.nlm.nih.gov/39121579/) | 2024 | Coorte | EBioMedicine | Mielo-inositol plasmático elevado em pacientes com insuficiência cardíaca (FEr e FEp), com possível valor prognóstico; dados prévios sugerem estresse oxidativo e efeito potencialmente deletério |
| [22834797](https://pubmed.ncbi.nlm.nih.gov/22834797/) | 2012 | Revisão | Current Medicinal Chemistry | Cromograninas e sinalização de Ca²⁺ dependente de IP3 na cardiomiopatia e na insuficiência cardíaca |
| [9476544](https://pubmed.ncbi.nlm.nih.gov/9476544/) | 1997 | Revisão/mecanismo | Heart and Vessels | Papel dos receptores de IP3 na apoptose e na regulação em insuficiência cardíaca |
| [28303572](https://pubmed.ncbi.nlm.nih.gov/28303572/) | 2017 | Revisão/mecanismo | The Journal of Physiology | Canais de liberação de cálcio (RyR e IP3R) como alvos possíveis em insuficiência cardíaca, hipertensão e diabetes |
| [38254653](https://pubmed.ncbi.nlm.nih.gov/38254653/) | 2023 | Pré-clínico | Biomolecules | Em coelhos com insuficiência cardíaca, CaMKII e sinalização de IP3 aumentam o risco de alternância atrial |
| [20531218](https://pubmed.ncbi.nlm.nih.gov/20531218/) | 2010 | Mecanismo | J Cardiovasc Pharmacol | Hipertrofia e insuficiência cardíaca via Gq, IP3 e CaMKII |
| [11273716](https://pubmed.ncbi.nlm.nih.gov/11273716/) | 2001 | Revisão | J Mol Cell Cardiol | Canais de liberação de cálcio (RyR/IP3R) em insuficiência cardíaca e morte súbita |
| [19232951](https://pubmed.ncbi.nlm.nih.gov/19232951/) | 2008 | Revisão | Trends Cardiovasc Med | Vias de sobrevivência celular da endotelina no coração, incluindo a via PI3K-AKT |

Várias outras publicações recuperadas (estresse nitrosativo, FMO2, coesinopatias, toxicidade de inibidores de PI3Kα) parecem apenas vagamente relacionadas ao inositol. Para a previsão de doença cardíaca pulmonar aguda, a literatura é igualmente indireta e pré-clínica.

## Informações de Comercialização no Brasil

Os registros não trazem texto de indicação aprovada nem forma farmacêutica, e são produtos de composição multivitamínica ou associada.

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 167730285 | NATUS GERIN | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100020031 | HEPACHOFRIL | LABORATORIO SEDABEL LTDA | Cancelado |
| 100020089 | TIAMINA + ASSOCIAÇÕES | LABORATORIO SEDABEL LTDA | Cancelado |
| 100320047 | HECROSINE | ORTOQUIMICA INDUSTRIA QUÍMICO-FARMACÊUTICA LTDA | Cancelado |
| 100380001 | AMINOLYSIN | BRASTERAPICA PHARMACEUTICA LTDA. | Cancelado |
| 100380017 | BIOLIP | BRASTERAPICA PHARMACEUTICA LTDA. | Cancelado |
| 101550042 | POLIVITAMINICOS E MINERAIS ASSOCIADOS | MARJAN INDÚSTRIA E COMÉRCIO LTDA | Cancelado |
| 101830011 | LAFEPE POLIVITAMINAS | LABORATORIO FARMACEUTICO DO ESTADO DE PERNAMBUCO G | Cancelado |
| 101910297 | LIPOSITOL | THERASKIN FARMACEUTICA LTDA. | Cancelado |
| 102160245 | CLUSIVOL COMPOSTO | LABORATÓRIOS PFIZER LTDA | Cancelado |
| 102680024 | METISIL B 12 | LABORSIL IND FTCA LTDA | Cancelado |
| 103200001 | ANECROSAN B12 | INSTITUTO BIOCHIMICO MARAGLIANO LTDA | Cancelado |
| 103940479 | METIOCOLIN B 12 | LABORATÓRIO AMERICANO DE FARMACOTERAPIA S/A | Cancelado |
| 104340006 | HEPATOGENOL | PROFARB LTDA | Cancelado |
| 104650405 | GERIVIX | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 105530115 | METIOCOLIN B12 | ABBOTT LABORATÓRIOS DO BRASIL LTDA | Cancelado |
| 105730072 | GERIATON | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Cancelado |
| 105830085 | NATUS GERIN | GERMED FARMACEUTICA LTDA | Cancelado |
| 106390119 | XANTINON | TAKEDA PHARMA LTDA. | Cancelado |
| 113050021 | MULTIVIMS PLUS | LUMA INDUSTRIA FARMACEUTICA LTDA | Cancelado |
| 115570055 | ANEMIX | INFAN INDUSTRIA QUIMICA FARMACEUTICA NACIONAL S/A | Cancelado |
| 116950033 | VITFORTE | LABORATÓRIO FARMACÊUTICO VITAMED LTDA | Cancelado |
| 126140006 | PLUSVITAM | QUIMIFAR LTDA. | Cancelado |
| 127020020 | VITAMIN FOR HAIR | BIOWELL AMERICA LTDA | Cancelado |
| 136310009 | NATURAL WEALTH PARA O CABELO | TRANSCONTINENTAL TRADING LTDA | Cancelado |
| 136310011 | POLIVITAMINAS E POLIMINERAIS PARA CABELOS E UNHAS | TRANSCONTINENTAL TRADING LTDA | Cancelado |
| 172870347 | GERIVIX | HYPERA S.A. | Cancelado |
| 172870421 | METIOCOLIN B 12 | HYPERA S.A. | Cancelado |
| 178170106 | METIOCOLIN B 12 | COSMED INDUSTRIA DE COSMETICOS E MEDICAMENTOS S.A. | Cancelado |

## Considerações de Segurança

Os dados de advertências, contraindicações e interações medicamentosas da bula não estão disponíveis nos dados compilados; consulte a bula para informações de segurança.

Como sinal adicional, a base de conhecimento registra relações de contraindicação (não é texto de bula) com as seguintes condições, que pedem cautela e verificação em fonte regulatória:
- Hepáticas e biliares: doença hepática, doença da vesícula biliar
- Metabólicas: hiperglicemia, diabetes mellitus, cetoacidose diabética, gota, hipofosfatemia
- Hematológicas: trombocitopenia, doenças da coagulação, hemoglobinopatia
- Cardiovasculares e cerebrovasculares: síndrome coronariana aguda, doença arterial coronariana, infarto do miocárdio, trombose coronariana, AVC, doença cerebrovascular, infarto cerebral, oclusão de artéria cerebral, infarto de tronco encefálico, distúrbio hipotensivo
- Outras: úlcera péptica, abuso/dependência de substâncias

Chama atenção que várias dessas relações são cardiovasculares, o que merece análise cuidadosa antes de qualquer hipótese em insuficiência cardíaca.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- As previsões de maior pontuação não têm nenhum ensaio ou publicação, e a única com literatura (insuficiência cardíaca) traz apenas dados indiretos, com um sinal que sugere elevação do mielo-inositol como possivelmente deletéria. Faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA para advertências e contraindicações (lacuna que impede a triagem de segurança)
- Obter dados do mecanismo de ação do inositol (por exemplo, no DrugBank)
- Investigar se o mielo-inositol elevado na insuficiência cardíaca é causa, consequência ou biomarcador, com estudos mecanísticos e, depois, pré-clínicos de intervenção
- Verificar a situação regulatória atual do inositol no Brasil
- Não priorizar as previsões hepáticas e portais sem alguma evidência de apoio independente do modelo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

