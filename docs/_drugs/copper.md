---
layout: default
title: Copper
parent: Apenas Predição do Modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Copper: nova indicação prevista, Esotropia (esotropia) (nível de evidência L5). Indicação original: Polivitamínicos com minerais"
monitor_inn: "Copper"
predicted_indications: ["esotropia", "dermatitis", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "dry eye syndrome", "amyopathic dermatomyositis", "bone Paget disease"]
---

# Copper
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

## Cobre: Do uso em polivitamínicos com minerais à dermatite
{: .text-alpha }

## Resumo em Uma Frase

Cobre (Copper) foi originalmente registrado no Brasil como componente de um produto polivitamínico com minerais (VITERGAN ZINCO), hoje com registro cancelado.
O modelo TxGNN prevê, em primeiro lugar, **esotropia (esotropia)**, mas essa previsão não tem nenhuma evidência de apoio. A direção mais bem sustentada é **dermatite (dermatitis)**, com **2 ensaios clínicos** (um retirado e um piloto muito pequeno) e **20 publicações**, em sua maioria revisões sobre oligoelementos.

## Visão Geral Rápida

A previsão de maior pontuação (esotropia) não possui ensaios nem literatura e é considerada um provável artefato do grafo. Por isso, o relatório detalha também a dermatite (2ª colocada), a indicação com mais evidências disponíveis.

| Item | Conteúdo |
|------|------|
| Indicação Original | Polivitamínicos com minerais |
| Nova Indicação Prevista (1ª colocada) | Esotropia (esotropia) |
| Pontuação de Previsão TxGNN (1ª colocada) | 96,25% |
| Nível de Evidência (1ª colocada) | L5 |
| Indicação com mais evidências | Dermatite (dermatitis), pontuação TxGNN de 95,06%, nível L4 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold (esotropia); dermatite: questão de pesquisa, sem avanço clínico no momento |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o cobre é um oligoelemento essencial, usado como suplemento mineral em polivitamínicos. Seu uso aprovado refere-se à reposição nutricional, e não ao tratamento de doenças específicas.

**Esotropia:** não há relação mecanística identificável entre o cobre e esse distúrbio do alinhamento ocular e da visão binocular. A pontuação alta (96%) parece ser um artefato da previsão baseada em grafo, sem ensaios ou literatura de apoio.

**Dermatite:** a relação é biologicamente plausível, mas bidirecional. O cobre é cofator de enzimas como a lisil oxidase e a superóxido dismutase, e a homeostase de cobre e zinco está ligada à barreira cutânea e à inflamação. Trabalho recente aponta o envolvimento da cuproptose na inflamação crônica da pele (PMID 41064128). Por outro lado, a hipersensibilidade ao cobre é causa descrita de dermatite de contato, ou seja, o cobre pode ser tanto gatilho quanto fator ligado à deficiência. A literatura é composta principalmente por revisões sobre oligoelementos (sobretudo zinco), sem dados diretos de eficácia da suplementação de cobre.

## Evidências de Ensaios Clínicos

Ensaios referentes à dermatite (a esotropia não tem ensaios registrados):

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06726707](https://clinicaltrials.gov/study/NCT06726707) | Phase 2/3 | Retirado | 0 | Avaliaria produtos absorventes para incontinência com substância à base de cobre na dermatite associada à incontinência em idosos. Foi retirado sem inclusão de participantes, portanto não gerou dados. |
| [NCT01291628](https://clinicaltrials.gov/study/NCT01291628) | NA | Desconhecido | 10 | Estudo piloto com meias contendo fibras de cobre para prevenir a síndrome mão-pé induzida por capecitabina. Muito pequeno, sem resultados conclusivos. |

## Evidências da Literatura

Seleção das publicações mais relevantes sobre dermatite (revisões e estudos mecanísticos priorizados):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38612631](https://pubmed.ncbi.nlm.nih.gov/38612631/) | 2024 | Revisão | Int J Mol Sci | Zinco, cobre e ferro em doenças de pele; deficiência ou excesso de oligoelementos pode alterar o risco de doenças cutâneas. |
| [39102684](https://pubmed.ncbi.nlm.nih.gov/39102684/) | 2024 | Revisão sistemática | JMIR Dermatol | Nutrição, obesidade e dermatite seborreica; dieta e suplementos podem modular a doença. |
| [38367035](https://pubmed.ncbi.nlm.nih.gov/38367035/) | 2024 | Revisão | Clin Exp Med | Papel do zinco na saúde e na doença (foco em zinco). |
| [25098945](https://pubmed.ncbi.nlm.nih.gov/25098945/) | 2014 | Revisão | Contact Dermatitis | Hipersensibilidade ao cobre: reações alérgicas são raras apesar da ampla exposição. |
| [37331278](https://pubmed.ncbi.nlm.nih.gov/37331278/) | 2023 | Revisão | J Trace Elem Med Biol | Metais pesados na dermatite de contato. |
| [34264859](https://pubmed.ncbi.nlm.nih.gov/34264859/) | 2023 | Revisão | Altern Ther Health Med | Uso terapêutico de oligoelementos em dermatologia. |
| [41064128](https://pubmed.ncbi.nlm.nih.gov/41064128/) | 2025 | Pré-clínico/mecanístico | MedComm | A cuproptose favorece a inflamação cutânea crônica via via α-cetoglutarato/H3K4me3/FTH1 e ferroptose. |
| [42565357](https://pubmed.ncbi.nlm.nih.gov/42565357/) | 2026 | Pré-clínico | Pharm Dev Technol | Hidrogel ácido à base de cobre para dermatite atópica, com atividade antimicrobiana em avaliação pré-clínica. |
| [38520630](https://pubmed.ncbi.nlm.nih.gov/38520630/) | 2024 | Relato de caso | CEN Case Rep | Anemia por deficiência de cobre causada por suplementação de zinco em paciente em hemodiálise. |
| [14672513](https://pubmed.ncbi.nlm.nih.gov/14672513/) | 2003 | Revisão | Rev Environ Health | Reações de hipersensibilidade ao cobre, imediatas e tardias. |

Para as demais indicações previstas, há pouca ou nenhuma literatura relevante. Para acne queloide, dry eye (olho seco) e doença de Paget óssea, os poucos itens encontrados são indiretos (pesquisas ocupacionais, nanopartículas de cobre-selênio em estudo pré-clínico e biologia estrutural de p97) e não sustentam o uso do cobre.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101550091 (cancelado) | VITERGAN ZINCO | Não informada | Polivitamínicos com minerais |

## Considerações de Segurança

Consulte a bula para informações de segurança.

Observação relevante da literatura: a suplementação de zinco em doses habituais pode causar anemia por deficiência de cobre (PMID 38520630), e o cobre pode induzir hipersensibilidade cutânea e dermatite de contato (PMID 25098945).

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (esotropia) é só do modelo (L5), sem mecanismo plausível, e provavelmente é um artefato do grafo. Para dermatite, há plausibilidade biológica (L4), mas as evidências são revisões, estudos pré-clínicos e um ensaio retirado, sem dados clínicos de eficácia. Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA, para advertências e contraindicações, hoje indisponíveis.
- Complementar os dados de mecanismo de ação (DrugBank).
- Definir qual forma química do cobre e qual via de administração seriam adequadas (tópica, dispositivo ou oral), pois a compatibilidade de via ainda não foi avaliada.
- Realizar ensaios clínicos controlados em dermatite, com atenção ao risco de hipersensibilidade ao cobre.
- Reavaliar a previsão de esotropia somente se surgir justificativa mecanística independente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

