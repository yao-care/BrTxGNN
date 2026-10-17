---
layout: default
title: Galsulfase
parent: Apenas Predição do Modelo (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Galsulfase: nova indicação prevista, Síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ect… (nível de evidência L5). Indicação original: Mucopolissacaridose"
monitor_inn: "Galsulfase"
predicted_indications: ["ptosis-strabismus-ectopic pupils syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "jaw-winking syndrome", "congenital entropion", "epiblepharon", "congenital ectropion"]
---

# Galsulfase
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Galsulfase: Da mucopolissacaridose à síndrome de ptose-estrabismo-pupilas ectópicas

## Resumo em Uma Frase

Galsulfase é uma enzima recombinante (N-acetilgalactosamina-4-sulfatase), originalmente usada no tratamento da mucopolissacaridose (MPS VI).
O modelo TxGNN prevê que pode ser eficaz para a **síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ectopic pupils syndrome)**,
porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão baseia-se apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mucopolissacaridose |
| Nova Indicação Prevista | Síndrome de ptose-estrabismo-pupilas ectópicas (ptosis-strabismus-ectopic pupils syndrome) |
| Pontuação de Previsão TxGNN | 97,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a galsulfase é uma sulfatase recombinante que degrada o dermatan sulfato nos lisossomos, e sua eficácia na mucopolissacaridose tipo VI é a base de seu uso.

Na prática, **a previsão não é sustentada mecanisticamente**. A síndrome de ptose-estrabismo-pupilas ectópicas é um distúrbio congênito do desenvolvimento craniofacial e ocular, sem acúmulo conhecido de glicosaminoglicanos. Não há plausibilidade biológica para que a reposição enzimática atue nessa condição.

A pontuação alta do TxGNN (97,89%) provavelmente é um artefato do grafo de conhecimento, sem respaldo em evidências clínicas ou na literatura.

### Outras previsões de destaque (todas sem evidências)

Os demais candidatos de maior pontuação também carecem de justificativa mecanística e de qualquer estudo:

| Posição | Doença prevista | Pontuação | Comentário |
|------|------|------|------|
| 2 | Camptodactilia, miopia e fibrose do músculo reto medial | 97,87% | Distúrbio congênito raro; sem mecanismo de armazenamento de GAG |
| 3 | Síndrome de Horner congênita | 97,84% | Alteração da inervação simpática, não deficiência enzimática |
| 4 | Síndrome de ptose-paralisia de prega vocal | 97,83% | Síndrome neuromuscular/do desenvolvimento, sem vínculo com dermatan sulfato |
| 5 | Síndrome de ptose-limitação do movimento ocular superior-ausência de ponto lacrimal | 97,67% | Malformação congênita, sem envolvimento de GAG |
| 6 | Síndrome de piscar-mandíbula (jaw-winking) | 97,65% | Sincinesia por conexões nervosas aberrantes |
| 7 | Entrópio congênito | 97,64% | Malformação palpebral, tratada cirurgicamente |
| 8 | Epibléfaro | 97,55% | Anomalia anatômica da prega palpebral |
| 9 | Ectrópio congênito | 97,48% | Malformação palpebral estrutural |
| 10 | Síndrome de Scheie | 94,79% | Única com literatura (revisões gerais); ver abaixo |

A síndrome de Scheie (MPS IS) é a única com alguma relação biológica, por pertencer à família das MPS. No entanto, é causada pela deficiência de alfa-L-iduronidase, enzima que a galsulfase não substitui, e o tratamento aprovado é a laronidase. Assim, o benefício da galsulfase é improvável. Seu nível de evidência é L4 (apenas revisões gerais sobre terapia de MPS).

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (síndrome de ptose-estrabismo-pupilas ectópicas), atualmente não há literatura relacionada.

Para a síndrome de Scheie (posição 10), foram encontradas apenas revisões gerais, sem dados sobre galsulfase nessa doença:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [22210671](https://pubmed.ncbi.nlm.nih.gov/22210671/) | 2011 | Revisão | Rheumatology (Oxford) | Revisão das terapias para mucopolissacaridoses, incluindo reposição enzimática (por exemplo, laronidase na MPS I) e o papel do cuidado multidisciplinar |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Revisão | La Revue de Médecine Interne | Revisão da terapia de reposição enzimática em doenças de depósito lisossômico (Gaucher, Fabry, entre outras) |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a indicação prevista, e não existe vínculo mecanístico plausível entre a galsulfase e a síndrome de ptose-estrabismo-pupilas ectópicas. A alta pontuação do TxGNN parece ser um artefato do grafo de conhecimento. O mesmo vale para as demais previsões oculares/craniofaciais; a síndrome de Scheie, embora relacionada às MPS, tem a laronidase como tratamento adequado.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação consultados na base DrugBank, para permitir análise mecanística formal
- Texto de bula da ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança
- Evidência biológica ou pré-clínica que demonstre acúmulo de glicosaminoglicanos ou outro alvo da galsulfase na doença prevista
- Observação: o medicamento não possui registro no Brasil (0 registros), o que exigiria avaliação regulatória adicional antes de qualquer uso em nova indicação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

