---
layout: default
title: Inositol
parent: Apenas Predição do Modelo (L5)
nav_order: 368
evidence_level: L5
indication_count: 9
monitor_inn: "INOSITOL"
predicted_indications: ["idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatic porphyria", "congestive heart failure", "acute pulmonary heart disease", "glycogen storage disease due to hepatic glycogen synthase deficiency"]
last_modified_at: 2026-10-23
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
| Situação no Mercado Brasileiro | Desconhecida (lista parcial); todos os 20 registros listados estão cancelados |
| Número de Registros | Pelo menos 20 (a lista pode estar incompleta) |
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

A lista abaixo é parcial (há pelo menos 20 registros) e todos os registros listados constam como cancelados. Os registros não trazem texto de indicação aprovada nem forma farmacêutica, e são produtos de composição multivitamínica ou associada.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101830011 | LAFEPE POLIVITAMINAS | Não informada | Não informada |
| Registro 101910297 | LIPOSITOL | Não informada | Não informada |
| Registro 115570055 | ANEMIX | Não informada | Não informada |
| Registro 172870347 | GERIVIX | Não informada | Não informada |
| Registro 172870421 | METIOCOLIN B 12 | Não informada | Não informada |

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
- As previsões de maior pontuação não têm nenhum ensaio ou publicação, e a única com literatura (insuficiência cardíaca) traz apenas dados indiretos, com um sinal que sugere elevação do mielo-inositol como possivelmente deletéria. Todos os registros brasileiros listados estão cancelados e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA para advertências e contraindicações (lacuna que impede a triagem de segurança)
- Obter dados do mecanismo de ação do inositol (por exemplo, no DrugBank)
- Investigar se o mielo-inositol elevado na insuficiência cardíaca é causa, consequência ou biomarcador, com estudos mecanísticos e, depois, pré-clínicos de intervenção
- Verificar a situação regulatória atual do inositol no Brasil, já que a lista é parcial e todos os registros listados estão cancelados
- Não priorizar as previsões hepáticas e portais sem alguma evidência de apoio independente do modelo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

