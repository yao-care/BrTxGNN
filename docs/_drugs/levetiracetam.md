---
layout: default
title: Levetiracetam
parent: Apenas Predição do Modelo (L5)
nav_order: 404
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
description: "Levetiracetam: nova indicação prevista, Beta-ketothiolase deficiency (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Levetiracetam
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

## Levetiracetam: Beta-ketothiolase deficiency
{: .text-alpha }

## Resumo em Uma Frase

Levetiracetam é um fármaco antiepiléptico (antiepiléptico de segunda geração), originalmente usado no tratamento da epilepsia parcial.
O modelo TxGNN prevê que pode ser eficaz para **epilepsia visual (visual epilepsy)**, porém, para essa indicação principal, há **0 ensaios clínicos** e apenas evidências indiretas na literatura (**20 publicações recuperadas**, nenhuma tratando diretamente de epilepsia visual).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Beta-ketothiolase deficiency |
| Pontuação de Previsão TxGNN | 0.9990 |
| Nível de Evidência | L5 (para a indicação principal); L1 para o estado de mal epiléptico |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 49 de 54) |
| Número de Registros | 54 (ativos: 49) |
| Decisão Recomendada | Hold (indicação principal); Proceed with Guardrails (estado de mal epiléptico) |


---

## Por que Esta Previsão é Razoável?

Os dados compilados não trazem uma descrição formal do mecanismo de ação. Segundo a literatura recuperada, o levetiracetam liga-se à proteína de vesícula sináptica SV2A e reduz a liberação de neurotransmissores, o que diminui a hiperexcitabilidade neuronal. Esse mecanismo explica seu uso estabelecido em crises focais e generalizadas.

A epilepsia visual (fotossensível) é um tipo de crise reflexa, desencadeada por estímulos luminosos. Como o levetiracetam atua na redução da excitabilidade neuronal de forma geral, existe uma justificativa mecanística plausível. Contudo, a literatura recuperada trata de crises neonatais, profilaxia de crises, encefalopatias genéticas (KCNQ2, STXBP1) e epilepsia felina, e **não aborda a epilepsia reflexa visual**. A pontuação muito alta do TxGNN está, portanto, apoiada apenas em evidência indireta.

O mesmo raciocínio vale para outras crises reflexas previstas (induzidas por micção, pensamento, orgasmo e alimentação), todas com nível de evidência L4 ou L5.

---

## Evidências de Ensaios Clínicos

Para a indicação principal (epilepsia visual), atualmente não há ensaios clínicos relacionados registrados.


| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | Concluído | 478 | Estudo randomizado, cego (ESETT): levetiracetam vs. fosfenitoína vs. valproato no estado de mal epiléptico refratário a benzodiazepínicos |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | Concluído | 203 | Levetiracetam IV associado a clonazepam vs. clonazepam isolado no tratamento pré-hospitalar do estado de mal tônico-clônico generalizado |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | Concluído | 80 | Levetiracetam vs. valproato de sódio em crianças com estado de mal convulsivo generalizado refratário |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | Concluído | 144 | Levetiracetam combinado com midazolam em crianças com estado de mal convulsivo generalizado |
| [NCT00362141](https://clinicaltrials.gov/study/NCT00362141) | Phase 2 | Desconhecido | 12 | Segurança e tolerabilidade do levetiracetam adjuvante no estado de mal epiléptico |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | Recrutando | 124 | Cetamina + levetiracetam vs. levetiracetam isolado em crianças com estado de mal refratário a benzodiazepínicos |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Phase 3 | Recrutando | 770 | KESETT: duas doses de cetamina + levetiracetam vs. levetiracetam isolado |
| [NCT06403150](https://clinicaltrials.gov/study/NCT06403150) | Phase 4 | Concluído | 62 | Levetiracetam vs. fosfenitoína no estado de mal convulsivo (estudo aberto) |
| [NCT04176887](https://clinicaltrials.gov/study/NCT04176887) | Phase 4 | Desconhecido | 60 | Levetiracetam vs. fenitoína no estado de mal pediátrico |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | Não especificada | Concluído | 138 | Levetiracetam vs. ácido valproico em crianças com estado de mal epiléptico |

---

## Evidências da Literatura

Para a epilepsia visual, a literatura recuperada é apenas indireta (crises neonatais, profilaxia, genética e modelos animais). As publicações mais relevantes disponíveis para as indicações previstas com algum respaldo são:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | N Engl J Med | Ensaio randomizado de três anticonvulsivantes no estado de mal epiléptico refratário a benzodiazepínicos |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT (ESETT, análise por faixa etária) | Lancet | Eficácia e segurança de levetiracetam, fosfenitoína e valproato no estado de mal estabelecido, por faixa etária |
| [33190679](https://pubmed.ncbi.nlm.nih.gov/33190679/) | 2020 | RCT | Health Technol Assess | EcLiPSE: levetiracetam como alternativa à fenitoína de segunda linha em crianças |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT Fase 3 | Lancet Neurol | PEACH: levetiracetam profilático para prevenção de crises na fase aguda da hemorragia intracerebral |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs. fenobarbital em crises neonatais |
| [18486495](https://pubmed.ncbi.nlm.nih.gov/18486495/) | 2008 | Coorte (aberto) | Seizure | Eficácia e tolerabilidade do levetiracetam adjuvante na epilepsia por sobressalto |
| [17401745](https://pubmed.ncbi.nlm.nih.gov/17401745/) | 2007 | Série de casos | J Neurol | Efeito do levetiracetam na doença do sobressalto (hiperecplexia) |
| [22386591](https://pubmed.ncbi.nlm.nih.gov/22386591/) | 2012 | Série de casos | Epilepsy Behav | Excelente resposta ao levetiracetam na epilepsia de leitura e remissão espontânea precoce |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | RCT veterinário (aberto) | J Feline Med Surg | Levetiracetam em crises reflexas audiogênicas felinas |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Revisão sistemática/meta-análise | Neurocrit Care | Levetiracetam na profilaxia de crises em cuidados neurocríticos |

---

## Considerações de Segurança

- **Contraindicações (relações do grafo de conhecimento, não texto de bula):** transtornos de ansiedade, transtornos neuróticos, distimia, transtornos psicóticos e esquizoafetivos, transtornos mentais em geral, despersonalização, doença renal, doença hepática, doença da vesícula biliar, neutropenia, agranulocitose, leucopenia e pancitopenia.
- **Eventos adversos descritos na literatura:** hiperplasia gengival (relato de caso), hiponatremia, agravamento de crises induzido pelo levetiracetam (série de casos de 2025) e irritabilidade/alterações comportamentais.
- **Interações medicamentosas:** foram identificadas 100 interações. Entre as de nível **moderado** destacam-se morfina (inclusive lipossomal), dronabinol, nabilona, ópio, metoclopramida e sibutramina (principalmente por efeito aditivo sobre o sistema nervoso central). Outras interações, de nível não classificado, incluem calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, metformina, omeprazol, lansoprazol, vancomicina, atropina, levocarnitina e triancinolona.

Consulte a bula para informações complementares de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, epilepsia visual) 
**Alternativa: Proceed with Guardrails** (para o estado de mal epiléptico)

**Justificativa:**
- O mesmo ocorre com as crises induzidas por micção, pensamento, orgasmo e alimentação, e com a deficiência de beta-cetotiolase (L4/L5).
- O estado de mal epiléptico tem evidência de nível L1 (ensaios de Fase 3, como o ESETT). Porém, o ESETT não mostrou diferença significativa de eficácia entre os três fármacos, de modo que o levetiracetam é uma opção de segunda linha eficaz, não superior. Observe também que se trata de uma indicação já clinicamente consolidada. As indicações por sobressalto e audiogênica (L3) são hipóteses de pesquisa, com evidência pequena, não controlada ou veterinária.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança. Não há registros do medicamento no Brasil nos dados compilados, e a situação regulatória deve ser confirmada.
- Complementar os dados do mecanismo de ação (ex.: consulta ao DrugBank).
- Para epilepsia visual e demais crises reflexas: estudos clínicos específicos (ex.: ensaio de fotossensibilidade com estimulação fótica intermitente).
- Para o estado de mal epiléptico: dosagem adequada à idade, monitoramento de efeitos adversos comportamentais, ajuste de dose na insuficiência renal e alinhamento com as diretrizes locais.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

