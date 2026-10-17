---
layout: default
title: Idursulfase
parent: Apenas Predição do Modelo (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Idursulfase: nova indicação prevista, Síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ect… (nível de evidência L5). Indicação original: Mucopolissacaridose"
monitor_inn: "Idursulfase"
predicted_indications: ["ptosis-strabismus-ectopic pupils syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "jaw-winking syndrome", "congenital entropion", "epiblepharon", "congenital ectropion"]
---

# Idursulfase
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Idursulfase: Da mucopolissacaridose à síndrome de ptose-estrabismo-pupilas ectópicas

## Resumo em Uma Frase

Idursulfase é uma enzima recombinante (iduronato-2-sulfatase) usada originalmente no tratamento da mucopolissacaridose (MPS II, síndrome de Hunter).
O modelo TxGNN prevê que possa ser eficaz para a **síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ectopic pupils syndrome)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mucopolissacaridose |
| Nova Indicação Prevista | Síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ectopic pupils syndrome) |
| Pontuação de Previsão TxGNN | 97,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a idursulfase é uma enzima recombinante que substitui a iduronato-2-sulfatase deficiente na síndrome de Hunter (MPS II), degradando glicosaminoglicanos (GAGs) acumulados nos lisossomos.

Para a síndrome prevista, **não se identifica um vínculo mecanístico plausível**. Trata-se de uma síndrome ocular e neuromuscular de origem congênita e do desenvolvimento, sem relação conhecida com acúmulo de GAGs ou deficiência de iduronato-2-sulfatase. A pontuação elevada parece refletir proximidade no grafo de conhecimento, e não plausibilidade biológica.

O mesmo vale para as demais previsões de maior pontuação (ranks 2 a 9): síndrome de camptodactilia-miopia-fibrose do reto medial, síndrome de Horner congênita, síndrome de ptose-paralisia de corda vocal, síndrome de ptose-limitação do movimento ocular superior-ausência de ponto lacrimal, síndrome de jaw-winking (Marcus Gunn), entrópio congênito, epibléfaro e ectrópio congênito. Em todas, a análise não encontrou vínculo mecanístico nem qualquer evidência clínica ou da literatura.

A única previsão com algum sentido biológico é a **síndrome de Scheie** (forma atenuada da MPS I, por deficiência de alfa-L-iduronidase), com pontuação de 94,79%. As duas enzimas atuam em sequência na degradação de dermatan sulfato e heparan sulfato, então a associação é coerente. Contudo, a idursulfase não substitui a enzima ausente nessa doença; o tratamento aprovado é a laronidase. A literatura recuperada trata de MPS em geral, dessensibilização e biomarcadores, sem demonstrar eficácia da idursulfase na MPS I.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Para a indicação de maior pontuação, atualmente não há literatura relacionada.

Para fins de contexto, a previsão de rank 10 (síndrome de Scheie) possui as seguintes publicações, todas de evidência indireta:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [22210671](https://pubmed.ncbi.nlm.nih.gov/22210671/) | 2011 | Revisão | Rheumatology (Oxford) | Visão geral das terapias para MPS, incluindo reposição enzimática para MPS I (laronidase) e MPS II (idursulfase) |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Revisão | La Revue de Médecine Interne | Revisão da terapia de reposição enzimática em doenças de depósito lisossômico |
| [36329518](https://pubmed.ncbi.nlm.nih.gov/36329518/) | 2022 | Série de casos | Orphanet J Rare Dis | Dessensibilização a idursulfase e laronidase em MPS II e MPS I-S |
| [39731157](https://pubmed.ncbi.nlm.nih.gov/39731157/) | 2024 | Coorte/seguimento | Orphanet J Rare Dis | Seguimento de dois anos após dessensibilização em MPS, para restabelecer a terapia enzimática após reações de hipersensibilidade |
| [21732093](https://pubmed.ncbi.nlm.nih.gov/21732093/) | 2012 | Coorte | J Inherit Metab Dis | Observações longitudinais do complexo cofator II da heparina–trombina como biomarcador em pacientes tratados com MPS I e II |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão principal tem nível de evidência L5: apenas pontuação do modelo, sem ensaios, sem literatura e sem vínculo mecanístico plausível. A pontuação alta provavelmente reflete proximidade no grafo de conhecimento, e não plausibilidade biológica. Além disso, o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) confirmados, por exemplo, via consulta ao DrugBank
- Bula da ANVISA com advertências e contraindicações, para triagem de segurança (lacuna bloqueante)
- Racional biológico que ligue a deficiência enzimática à fisiopatologia da síndrome prevista, ou evidência pré-clínica que o sustente
- Se houver interesse em MPS I/síndrome de Scheie, estudos que avaliem diretamente a idursulfase nessa condição (a terapia aprovada é a laronidase)
- Definição de compatibilidade de via de administração e de situação regulatória no Brasil (sem registro atualmente)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

