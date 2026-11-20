---
layout: default
title: Modafinil
parent: Apenas Predição do Modelo (L5)
nav_order: 464
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "modafinil"
predicted_indications: ["insomnia (disease)"]
description: "Modafinil: nova indicação prevista, insônia (insomnia (disease)) (nível de evidência L5). No Brasil, registros na ANVISA: 2 (ativos: 1)"
---

# Modafinil
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Modafinil: insônia (insomnia (disease))
{: .text-alpha }

## Resumo em Uma Frase

Modafinil é um agente promotor da vigília, registrado no Brasil sob a marca STAVIGILE.
O modelo TxGNN prevê que pode ser eficaz para **insônia (insomnia (disease))**, mas a previsão tem pouco respaldo: há apenas **2 ensaios clínicos** de Fase 4 (um terminado precocemente com 2 participantes e outro concluído sem resultados publicados) e nenhuma publicação que estude o modafinil na própria insônia. O nível de evidência é **L5**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | insônia (insomnia (disease)) |
| Pontuação de Previsão TxGNN | 0.9985 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Modafinil (tradução não oficial): “O(s) mecanismo(s) pelo(s) qual(is) a modafinila promove a vigília é(são) desconhecido(s). A modafinila tem ações promotoras da vigília semelhantes às de agentes simpatomiméticos, incluindo anfetamina e metilfenidato, embora o perfil farmacológico não seja idêntico ao das aminas simpatomiméticas.” Texto original em inglês: "The mechanism(s) through which modafinil promotes wakefulness is unknown. Modafinil has wake-promoting actions similar to sympathomimetic agents including amphetamine and methylphenidate, although the pharmacologic profile is not identical to that of the sympathomimetic amines." ([DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7), versão de 2026-09-16; acessado em 2026-11-19). De modo geral, entende-se que o modafinil atua por inibição do transportador de dopamina e por efeitos em circuitos promotores da vigília, o que o diferencia de outros estimulantes.

Do ponto de vista mecanístico, um fármaco que promove a vigília não é uma escolha lógica para tratar a insônia, que é um distúrbio de sono insuficiente ou de má qualidade. A pontuação muito alta (0,9985) provavelmente reflete a proximidade, na rede do modelo, com distúrbios do sono e da vigília (narcolepsia, distúrbio do sono do trabalho em turnos, sonolência associada a doenças neurológicas), e não um real ajuste terapêutico.

O vínculo plausível é com a sonolência diurna e a fadiga em condições associadas (doença de Parkinson, lesões cerebrais, idosos), não com o tratamento da insônia em si. A previsão deve ser tratada como hipótese de pesquisa.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Concluído | 40 | Avalia o modafinil, isolado ou com terapia cognitivo-comportamental para insônia (TCC-I), sobre o funcionamento diurno e a gravidade da insônia em insônia primária; sem resultados publicados ou disponibilizados |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Encerrado | 2 | Modafinil para distúrbios do sono/vigília em idosos; encerrado com apenas 2 participantes, sem dados úteis de eficácia ou segurança |

## Evidências da Literatura

Nenhuma publicação estuda diretamente o modafinil na insônia. Os estudos abaixo são os mais relevantes e tratam de sonolência e fadiga em outras condições.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisão sistemática/Meta-análise | PloS one | Eficácia e segurança do modafinil na fadiga e na sonolência diurna excessiva associadas a doenças neurológicas, com resultados prévios inconsistentes |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisão | Drugs | Revisão baseada em evidências dos usos aprovados e experimentais do modafinil em ensaios randomizados |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisão sistemática/Meta-análise | Parkinsonism & Related Disorders | Intervenções farmacológicas para sonolência diurna e distúrbios do sono na doença de Parkinson |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisão | Movement Disorders | Revisão baseada em evidências dos tratamentos para sintomas não motores da doença de Parkinson |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Série de casos | American Journal of Hospice & Palliative Care | Modafinil reduziu a fadiga na doença de Charcot-Marie-Tooth tipo 1A |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisão | Drugs | Carga e manejo do distúrbio do sono do trabalho em turnos |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330145 | STAVIGILE | LIBBS FARMACÊUTICA LTDA | Ativo |
| 104750051 | VIGIL | LUNDBECK BRASIL LTDA | Cancelado |

Há 1 registro válido e 1 cancelado, dos 2 registros totais.

## Considerações de Segurança

Os dados de advertências e contraindicações da bula não estavam disponíveis nos dados compilados para este relatório; consulte a bula para informações de segurança.

- **Interações Medicamentosas**: foram identificadas 249 interações, das quais as de nível moderado incluem omeprazol, esomeprazol, rabeprazol, dexametasona, eliglustat, linagliptina e cisaprida. Entre as de nível leve estão hidrocortisona, pioglitazona, aprepitanto, claritromicina e cimetidina, entre outras.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é mecanisticamente pouco coerente (um promotor da vigília para um distúrbio de sono insuficiente), e não há estudo com resultados que avalie o modafinil na própria insônia. O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Obter os resultados do ensaio NCT00124384 em insônia primária
- Completar os dados de mecanismo de ação
- Obter advertências e contraindicações da bula na ANVISA
- Se houver interesse, reorientar a hipótese para sonolência diurna e fadiga em condições comórbidas, em vez de insônia

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

