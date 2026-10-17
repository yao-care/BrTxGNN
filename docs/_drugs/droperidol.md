---
layout: default
title: Droperidol
parent: Apenas Predição do Modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Droperidol: nova indicação prevista, Síndrome de Tourette (Tourette syndrome) (nível de evidência L5). Indicação original: Não disponível"
monitor_inn: "Droperidol"
predicted_indications: ["Tourette syndrome", "trichotillomania", "manic bipolar affective disorder", "attention deficit hyperactivity disorder, inattentive type", "nephrogenic syndrome of inappropriate antidiuresis", "attention deficit-hyperactivity disorder", "headache disorder", "common cold", "hypertrichosis (disease)", "specific developmental disorder"]
---

# Droperidol
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

# Droperidol: Do uso em anestesia e antiemese à síndrome de Tourette

> Observação: a indicação prevista de maior posição (rank 1) é a síndrome de Tourette, mas ela não tem nenhuma evidência clínica. A indicação com maior volume de evidências nos dados compilados é **transtorno de cefaleia (headache disorder)**, discutida em destaque ao longo do relatório.

## Resumo em Uma Frase

Droperidol é um neuroléptico da classe das butirofenonas, com forte antagonismo dopaminérgico D2. Os dados compilados não trazem indicação aprovada no Brasil, pois o fármaco não possui registro ativo na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Tourette (Tourette syndrome)**, atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção (apenas previsão computacional).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (nenhuma licença brasileira registrada) |
| Nova Indicação Prevista | Síndrome de Tourette (Tourette syndrome) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

**Outras indicações previstas (resumo):**

| Posição | Indicação | Pontuação TxGNN | Nível de Evidência | Recomendação |
|------|------|------|------|------|
| 2 | Tricotilomania | 99,89% | L5 | Hold |
| 3 | Transtorno bipolar maníaco | 99,82% | L3 | Questão de pesquisa |
| 4 | TDAH, tipo desatento | 99,68% | L5 | Hold |
| 5 | Síndrome de antidiurese inapropriada nefrogênica | 99,63% | L5 | Hold |
| 6 | TDAH | 99,54% | L5 | Hold |
| 7 | Transtorno de cefaleia | 99,47% | L3 | Questão de pesquisa |
| 8 | Resfriado comum | 99,46% | L5 | Hold |
| 9 | Hipertricose | 99,46% | L5 | Hold |
| 10 | Transtorno específico do desenvolvimento | 99,40% | L5 | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o droperidol é uma butirofenona com potente antagonismo do receptor dopaminérgico D2, a mesma classe mecanística de haloperidol e pimozida, que são usados na síndrome de Tourette. Por isso, o vínculo mecanístico é plausível.

Contudo, a previsão se apoia apenas no modelo TxGNN, sem ensaios ou literatura. Na prática, o droperidol é pouco adequado: é parenteral, de ação curta e tem risco de prolongamento do intervalo QT, o que inviabiliza o uso crônico exigido em Tourette.

Entre as demais previsões, duas têm respaldo parcial:
- **Mania bipolar:** o antagonismo D2 produz tranquilização rápida na agitação aguda e na mania. A literatura (revisões Cochrane sobre psicose aguda e agitação, relatos de casos de mania grave) trata sobretudo de agitação e psicose, não de transtorno bipolar como diagnóstico definido.
- **Cefaleia/enxaqueca:** o antagonismo D2, associado ao efeito antiemético e central, fundamenta o uso de neurolépticos na enxaqueca aguda no pronto-socorro.

Várias previsões (TDAH, resfriado comum, hipertricose, antidiurese nefrogênica, transtorno do desenvolvimento) não têm justificativa mecanística plausível e provavelmente são artefatos do modelo. No TDAH, o bloqueio dopaminérgico vai contra a farmacologia dos tratamentos padrão.

## Evidências de Ensaios Clínicos

Para a indicação de maior posição (Tourette), atualmente não há ensaios clínicos relacionados registrados.

Para a indicação com mais evidências (transtorno de cefaleia):

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | NA | Encerrado | 19 | Droperidol vs. metoclopramida + difenidramina em cefaleias primárias no pronto-socorro (randomizado, duplo-cego). Encerrado precocemente, não permite conclusões de eficácia. |

## Evidências da Literatura

Para Tourette, atualmente não há literatura relacionada.

**Transtorno de cefaleia (indicação com mais literatura):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12552051](https://pubmed.ncbi.nlm.nih.gov/12552051/) | 2003 | RCT | Neurology | Droperidol vs. placebo no tratamento da enxaqueca aguda (ensaio randomizado, duplo-cego) |
| [11781912](https://pubmed.ncbi.nlm.nih.gov/11781912/) | 2002 | RCT | Am J Emerg Med | Eficácia do droperidol intramuscular na enxaqueca aguda em PS comunitário |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Diretriz | Headache | Avaliação de evidências da American Headache Society sobre o tratamento agudo da enxaqueca |
| [25416184](https://pubmed.ncbi.nlm.nih.gov/25416184/) | 2015 | Revisão | Ann Pharmacother | Segurança e eficácia do droperidol na enxaqueca aguda |
| [21435315](https://pubmed.ncbi.nlm.nih.gov/21435315/) | 2011 | Revisão sistemática | CJEM | Eficácia de butirofenonas em cefaleia primária no pronto-socorro |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revisão sistemática | Cephalalgia | Recomendações da Sociedade Canadense de Cefaleia para dor de enxaqueca em emergência |
| [32839811](https://pubmed.ncbi.nlm.nih.gov/32839811/) | 2020 | Revisão | Am J Health Syst Pharm | Reintrodução do droperidol na medicina de emergência: segurança, indicações e dosagem |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Revisão | Headache | Terapia de resgate na enxaqueca aguda, parte 2: neurolépticos, anti-histamínicos e outros |
| [9237411](https://pubmed.ncbi.nlm.nih.gov/9237411/) | 1997 | Coorte/Observacional | Headache | Estudo-piloto com droperidol intravenoso em 35 pacientes com estado de mal migranoso ou enxaqueca refratária |
| [10452443](https://pubmed.ncbi.nlm.nih.gov/10452443/) | 1999 | Série de casos | Am J Emerg Med | Revisão retrospectiva do droperidol intramuscular na enxaqueca aguda |

**Mania bipolar (evidência indireta):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27976370](https://pubmed.ncbi.nlm.nih.gov/27976370/) | 2016 | Revisão Cochrane | Cochrane Database Syst Rev | Droperidol para agitação ou agressividade induzida por psicose |
| [15495037](https://pubmed.ncbi.nlm.nih.gov/15495037/) | 2004 | Revisão Cochrane | Cochrane Database Syst Rev | Droperidol na psicose aguda |
| [9789713](https://pubmed.ncbi.nlm.nih.gov/9789713/) | 1998 | Relatos de casos e revisão | Clin Neuropharmacol | Droperidol oral no manejo provisório de mania grave (3 casos refratários) |
| [321727](https://pubmed.ncbi.nlm.nih.gov/321727/) | 1977 | Duplo-cego, controlado por placebo | J Nerv Ment Dis | Em 41 pacientes agitados, menos pacientes do grupo droperidol precisaram de haloperidol adicional |
| [10460140](https://pubmed.ncbi.nlm.nih.gov/10460140/) | 1999 | Relato de caso (segurança) | Ann Emerg Med | Desconforto respiratório após uso de droperidol para agitação |

## Informações de Comercialização no Brasil

O droperidol não possui registro ativo na ANVISA nos dados compilados (0 registros) e não é comercializado no Brasil.

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (TxGNN/PrimeKG, não texto de bula):**
  - Cardiovasculares: hipertensão, hipotensão ortostática, síndrome do QT longo (incluindo familiar), torsades de pointes, síndrome de taquicardia postural ortostática, atrofia de múltiplos sistemas.
  - Neurológicas: doenças dos núcleos da base, distonia focal da mão, blefaroespasmo.
  - Respiratórias: DPOC, insuficiência respiratória.
  - Psiquiátricas: transtornos de ansiedade, neuróticos e distímicos; abuso/dependência de substâncias.
  - Outras: doença renal, doença hepática, doença da vesícula biliar, doença inflamatória intestinal, deficiência de potássio, hiperplasia prostática benigna, feocromocitoma e alguns tumores (duodeno, intestino delgado, coração).
- **Interações medicamentosas** (100 interações encontradas; exemplos):
  - **Graves:** hidrocortisona, anfotericina B (e formulações lipídicas, lipossomal e sulfato de colesterila), morfina, naloxona, claritromicina, dolasetrona, ácido picossulfúrico, polietilenoglicol com eletrólitos.
  - **Moderadas:** famotidina, epinefrina, loperamida, lorcasserina, bisacodil, difenoxina, difenoxilato, dronabinol, óleo de rícino.
- **Preocupações de segurança na literatura:** prolongamento do intervalo QT e desconforto respiratório (PMID 10460140).

Não há dados de advertências e contraindicações da bula brasileira; consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para Tourette (maior pontuação), há apenas previsão computacional (L5), sem ensaios ou literatura, e o perfil do droperidol (parenteral, ação curta, risco de QT) é inadequado para uso crônico. Não há registro no Brasil.
- Cefaleia/enxaqueca (L3) e mania/agitação (L3) são as linhas mais promissoras e podem ser tratadas como questões de pesquisa, mas as evidências são sobretudo revisões e dados observacionais, sem RCT de Fase 3 concluído nos dados compilados. O único ensaio registrado foi encerrado com 19 participantes.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (consulta ao DrugBank).
- Verificar a situação regulatória e a disponibilidade da forma injetável no Brasil, já que não há registro ativo.
- Avaliar de forma sistemática os RCTs de enxaqueca (PMIDs 12552051 e 11781912) e a segurança cardíaca (QT), com plano de monitoramento por ECG.
- Para mania/agitação, esclarecer se a evidência se aplica a transtorno bipolar definido, e não apenas a agitação inespecífica.
- Confirmar a compatibilidade da via de administração com as indicações pretendidas (status ainda pendente).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

