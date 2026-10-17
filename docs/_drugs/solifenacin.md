---
layout: default
title: Solifenacin
parent: Apenas Predição do Modelo (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Solifenacin: nova indicação prevista, Doença renal policística tipo 3… (nível de evidência L5). Indicação original: Bexiga hiperativa (overactive bladder)"
monitor_inn: "Solifenacin"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "thoracic malformation", "renal-hepatic-pancreatic dysplasia", "adult familial nephronophthisis-spastic quadriparesia syndrome", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "low compliance bladder", "polycystic kidney disease", "subarachnoid hemorrhage (disease)", "congenital analbuminemia"]
---

# Solifenacin
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

# Solifenacina: Da bexiga hiperativa à bexiga de baixa complacência

## Resumo em Uma Frase

A solifenacina é um antagonista muscarínico seletivo para o receptor M3, originalmente usado no tratamento da bexiga hiperativa.
O modelo TxGNN prevê que pode ser eficaz para **Doença Renal Policística tipo 3, com ou sem doença hepática policística (polycystic kidney disease 3 with or without polycystic liver disease)**, que é a previsão de maior pontuação, mas sem nenhuma evidência clínica ou da literatura. Já a previsão com algum respaldo na literatura é a **bexiga de baixa complacência (low compliance bladder)**, com **10 publicações** (nenhum ensaio clínico registrado), em grande parte dentro do espaço da indicação original.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Bexiga hiperativa (overactive bladder) |
| Nova Indicação Prevista | Doença renal policística tipo 3, com ou sem doença hepática policística (maior pontuação); bexiga de baixa complacência (única com literatura) |
| Pontuação de Previsão TxGNN | 97,13% (doença renal policística tipo 3); 95,37% (bexiga de baixa complacência) |
| Nível de Evidência | L5 (doença renal policística tipo 3); L3 (bexiga de baixa complacência) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

**Observação:** a indicação original foi extraída do grafo de conhecimento, pois não há registros da ANVISA com texto de indicação aprovada. A previsão de maior pontuação (rank 1) não possui evidências; por isso, as seções de evidências abaixo se concentram na previsão de bexiga de baixa complacência (rank 7), a única com literatura.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a solifenacina é um antagonista muscarínico seletivo M3, que relaxa a musculatura lisa do detrusor, reduzindo contrações involuntárias, urgência e incontinência.

**Doença renal policística tipo 3 (rank 1):** não há vínculo mecanístico estabelecido. A pontuação de 0,971 é apenas uma previsão baseada em grafo. Nenhuma via conhecida liga o bloqueio muscarínico M3 à formação de cistos nessa doença. As demais previsões de alto escore (malformação torácica, displasia renal-hepática-pancreática, síndrome de Joubert com defeito renal, nefrite intersticial cariomegálica, doença renal policística, hemorragia subaracnóidea e analbuminemia congênita) também não têm mecanismo plausível nem evidências. Para a hemorragia subaracnóidea, os efeitos anticolinérgicos poderiam até ser prejudiciais (confusão e efeitos cognitivos).

**Bexiga de baixa complacência (rank 7):** é biologicamente plausível e coerente com a farmacologia do fármaco, pois o bloqueio de M3 no detrusor pode melhorar a capacidade e a complacência vesical. Contudo, a maior parte da literatura trata de bexiga hiperativa ou hiperatividade neurogênica do detrusor, e não da complacência como desfecho definido. A correspondência é, portanto, indireta, e trata-se mais de uma extensão dentro do espaço da indicação original do que de um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Literatura referente à previsão de bexiga de baixa complacência (10 registros fornecidos; os resumos estão truncados, então parte dos delineamentos foi inferida pelos títulos):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25435915](https://pubmed.ncbi.nlm.nih.gov/25435915/) | 2014 | RCT | Therapeutic Advances in Urology | Terapia cíclica versus contínua com combinação de tróspio e solifenacina na bexiga hiperativa grave em idosos, com foco na adesão |
| [27928426](https://pubmed.ncbi.nlm.nih.gov/27928426/) | 2016 | RCT | Therapeutic Advances in Urology | Adesão de pessoas em idade ativa a antimuscarínicos em dose alta |
| [32007426](https://pubmed.ncbi.nlm.nih.gov/32007426/) | 2020 | Estudo aberto de longo prazo (Fase 3) | Journal of Pediatric Urology | Eficácia e segurança de longo prazo da solifenacina em pacientes pediátricos (6 meses a 18 anos) com hiperatividade neurogênica do detrusor |
| [25170796](https://pubmed.ncbi.nlm.nih.gov/25170796/) | 2014 | Estudo clínico comparativo | Urologia Internationalis | Tróspio e solifenacina em combinação (doses baixa e padrão) para bexiga hiperativa moderada em idosos |
| [25656013](https://pubmed.ncbi.nlm.nih.gov/25656013/) | 2015 | Estudo clínico retrospectivo (7 pacientes) | Hinyokika Kiyo | Associação de mirabegrona em bexiga neurogênica resistente a anticolinérgicos, avaliada por videourodinâmica |
| [15716204](https://pubmed.ncbi.nlm.nih.gov/15716204/) | 2005 | Estudo aberto de longo prazo | European Urology | Segurança, tolerabilidade e persistência com solifenacina por até 1 ano na bexiga hiperativa |
| [38256949](https://pubmed.ncbi.nlm.nih.gov/38256949/) | 2024 | Observacional/Coorte | Pharmaceuticals (Basel) | Uso regular e irregular e motivos de descontinuação da solifenacina na bexiga hiperativa |
| [25503446](https://pubmed.ncbi.nlm.nih.gov/25503446/) | 2015 | Observacional prospectivo | International Urology and Nephrology | Associação entre boca seca e tratamento com solifenacina na bexiga hiperativa |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Revisão | British Journal of Pharmacology | Receptores muscarínicos na bexiga, da pesquisa básica à terapêutica |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Revisão | Expert Opinion on Investigational Drugs | Tratamentos da bexiga hiperativa em ensaios clínicos de fase inicial |

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não o texto da bula):** síndrome do QT longo (incluindo a forma familiar), torsades de pointes, insuficiência hepática, doença hepática, doença da vesícula biliar, glaucoma de ângulo fechado e obstrução do colo vesical.
- **Interações medicamentosas** (100 interações identificadas; principais):
  - **Graves (Major):** citrato de potássio, claritromicina e dolasetrona.
  - **Moderadas:** outros anticolinérgicos/antimuscarínicos (atropina, hiosciamina, glicopirrônio, clidínio, diciclomina, tróspio), famotidina, cimetidina, loperamida, aprepitanto, morfina, dexametasona, bisacodil, ácido picossulfúrico, polietilenoglicol com eletrólitos, eluxadolina e palonosetrona.

Consulte a bula para advertências e precauções adicionais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão de maior pontuação (doença renal policística tipo 3) e as demais previsões de alto escore não têm mecanismo plausível nem qualquer evidência clínica (L5). A única previsão com literatura (bexiga de baixa complacência, L3) está, em grande parte, dentro da indicação original e carece de ensaios registrados e de desfechos específicos de complacência. Além disso, o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações) e confirmar a situação de registro no Brasil.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Para bexiga de baixa complacência: revisar os textos completos da literatura e buscar estudos com complacência vesical como desfecho (urodinâmica).
- Avaliar o risco cardíaco (prolongamento do intervalo QT) e as interações graves antes de qualquer estudo.
- Para as previsões de doenças raras ou estruturais, não prosseguir sem uma hipótese mecanística e dados pré-clínicos.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

