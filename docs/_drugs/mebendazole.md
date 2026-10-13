---
layout: default
title: Mebendazole
parent: Apenas Predição do Modelo (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

# Mebendazol: De anti-helmíntico gastrointestinal para acne (previsão principal do modelo)

## Resumo em Uma Frase

Mebendazol é um anti-helmíntico do trato gastrointestinal, originalmente usado no tratamento de infecções por vermes intestinais.
A previsão de maior pontuação do modelo TxGNN é **acne (acne disease)**, mas ela conta com **0 ensaios clínicos** e apenas **1 publicação** (um relato de caso sobre uma doença parasitária não relacionada), ou seja, sem apoio real. Entre as 10 previsões analisadas, a mais bem sustentada é **equinococose alveolar**, com **19 publicações** (sobretudo revisões e estudos observacionais) e nenhum ensaio registrado.

> Observação: a previsão principal (acne) é, com grande probabilidade, um artefato do grafo de conhecimento. Por isso, a seção de mecanismo e a conclusão também discutem a indicação mais plausível (equinococose alveolar) e a segunda (equinococose por *E. granulosus*).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-helmínticos do trato gastrointestinal |
| Nova Indicação Prevista | Acne (acne disease) |
| Pontuação de Previsão TxGNN | 99,20% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 11 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o mebendazol é um anti-helmíntico benzimidazólico que se liga à beta-tubulina do parasita, impedindo a formação de microtúbulos e prejudicando a captação de glicose e a sobrevivência do verme.

**Para acne, não há relação mecanística plausível.** A acne é uma doença inflamatória da unidade pilossebácea, sem envolvimento de helmintos. A pontuação alta provavelmente decorre de associações do grafo de conhecimento, e a única publicação encontrada trata de esparganose proliferativa, uma doença parasitária sem relação com acne.

Outras previsões do modelo têm lógica bem diferente:
- **Equinococose alveolar (pontuação 94,20%) e equinococose por *E. granulosus* (95,61%)**: encaixe mecanístico forte, pois o mebendazol é um benzimidazol reconhecido para essas doenças. Trata-se, porém, de uso próximo da classe terapêutica original (anti-helmíntico), e não de reposicionamento propriamente dito. O albendazol costuma ser preferido na prática, e a cirurgia continua sendo a opção curativa quando viável.
- **Demodicidose da glândula sebácea (93,0%)**: plausível em teoria (ácaro ectoparasita), mas sem evidência recuperada; a penetração cutânea baixa e a via sistêmica seriam obstáculos.
- **Leishmaniose cutânea difusa, hordéolo, botulismo, impetigo e distrofia de Sorsby**: sem apoio mecanístico ou de evidência.

## Evidências da Literatura

**Para a previsão principal (acne):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Relato de caso | Am J Trop Med Hyg | Caso de esparganose proliferativa na Venezuela, com lesões nodulares semelhantes a acne; não trata de acne nem de mebendazol |

**Para a indicação mais bem sustentada (equinococose alveolar), principais publicações:**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8789923](https://pubmed.ncbi.nlm.nih.gov/8789923/) | 1996 | Diretriz (OMS) | Bull World Health Organ | Diretrizes para tratamento de equinococose cística e alveolar; benzimidazóis (albendazol ou mebendazol) como quimioterapia |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Estudo comparativo observacional | J Antimicrob Chemother | 35 pacientes tratados com mebendazol ou albendazol por cerca de 39 meses; ambos considerados fármacos de escolha |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Estudo clínico/relato | J Hepatol | Paciente com equinococose alveolar hepática tratado por 13 anos com mebendazol; sugere possível efeito parasiticida |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Revisão | Parasite | Benzimidazóis são parasitostáticos; podem causar disfunção hepática |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Revisão | World J Hepatol | Panorama atual da terapia medicamentosa para equinococose alveolar |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revisão | World J Gastroenterol | Manejo atual da equinococose hepática; a cirurgia é a base do tratamento |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Revisão | Acta Trop | Albendazol e mebendazol continuam sendo os únicos fármacos licenciados; novas opções são buscadas |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Revisão | Parasite | Alternativas terapêuticas além de albendazol e mebendazol |
| [15532108](https://pubmed.ncbi.nlm.nih.gov/15532108/) | 2004 | Análise de longo prazo | J Hepatol | Acompanhamento imunológico no estudo suíço de quimioterapia (1976-2001) |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Farmacologia | Eur J Clin Pharmacol | Concentrações plasmáticas de mebendazol em animais e humanos; doses orais altas só parcialmente eficazes |

**Para equinococose por *E. granulosus*:** destaca-se uma série de tratamento de 1989 com 70 pacientes e 150 cistos hidáticos tratados com mebendazol segundo protocolos da OMS ([PMID 2585032](https://pubmed.ncbi.nlm.nih.gov/2585032/)), com modificações morfológicas e/ou volumétricas em 64,3% dos cistos. Os demais itens são pré-clínicos, relatos de caso ou estudos com albendazol/nanoformulações.

Não há ensaios clínicos registrados para nenhuma das indicações previstas.

## Informações de Comercialização no Brasil

Todos os 11 registros de mebendazol estão **cancelados**. Principais registros (máximo de 5):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102980263 | Mebendazol | Não informada | Anti-helmínticos do trato gastrointestinal |
| Registro nº 105710032 | Belmirax | Não informada | Anti-helmínticos do trato gastrointestinal |
| Registro nº 154230210 | Mebendazol | Não informada | Anti-helmínticos do trato gastrointestinal |
| Registro nº 100431253 | Helmiben Meb | Não informada | Anti-helmínticos do trato gastrointestinal |
| Registro nº 154230030 | Menbel | Não informada | Anti-helmínticos do trato gastrointestinal |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (não são texto de bula): doença hepática e doença da vesícula biliar.
- **Interações medicamentosas** (10 registradas): 
  - Moderadas: metronidazol, iodeto I-131, iodeto I-123, fenobarbital, carbamazepina, ritonavir, fosfenitoína, fenitoína e primidona (os anticonvulsivantes indutores enzimáticos podem reduzir os níveis de mebendazol).
  - Leve: cimetidina.
- Em uso prolongado (como na equinococose alveolar), a literatura aponta risco de disfunção hepática, exigindo monitoramento hepático e hematológico.

## Conclusão e Próximos Passos

**Decisão: Hold** (para acne, a previsão principal)

**Justificativa:**
- A previsão de acne tem nível de evidência L5: sem ensaios, sem mecanismo plausível e com uma única publicação não relacionada. A pontuação alta do TxGNN parece ser artefato do grafo.
- Para equinococose alveolar e por *E. granulosus* (nível L3, "Proceed with Guardrails"), o mebendazol já é reconhecido como opção terapêutica, ainda que em geral secundária ao albendazol; isso representa uso próximo da indicação original, e não reposicionamento propriamente dito. A demodicidose permanece apenas como questão de pesquisa.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois esses dados estão ausentes.
- Obter os dados de mecanismo de ação no DrugBank.
- Verificar a disponibilidade do produto no Brasil, já que todos os registros estão cancelados.
- Para equinococose: definir plano de monitoramento hepático e hematológico de longo prazo e de manejo das interações medicamentosas, e comparar com albendazol.
- Para acne e as demais previsões sem evidência: não priorizar, a menos que surjam dados pré-clínicos ou clínicos que sustentem um mecanismo.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

