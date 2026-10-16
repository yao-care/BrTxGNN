---
layout: default
title: Perampanel
parent: Apenas Predição do Modelo (L5)
nav_order: 517
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Perampanel: nova indicação prevista, Epilepsia Visual (Visual Epilepsy) (nível de evidência L5). Indicação original: Epilepsia parcial / epilepsia motora parcial"
---

# Perampanel
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

# Perampanel: Da epilepsia parcial ao estado de mal epiléptico

## Resumo em Uma Frase

Perampanel é um antagonista seletivo e não competitivo do receptor AMPA, originalmente usado no tratamento da epilepsia parcial (incluindo epilepsia motora parcial).
O modelo TxGNN prevê que pode ser eficaz para **Epilepsia Visual (Visual Epilepsy)**, a indicação de maior pontuação, mas sem ensaios clínicos e com **20 publicações** gerais (nenhuma específica para essa condição). Entre as indicações previstas, a única com respaldo clínico mais concreto é o **Estado de Mal Epiléptico (Status Epilepticus)**, com **4 ensaios clínicos** e **18 publicações**, detalhado abaixo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia parcial / epilepsia motora parcial |
| Nova Indicação Prevista | Epilepsia Visual (Visual Epilepsy) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L4 (para epilepsia visual); L3 para o estado de mal epiléptico |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo a literatura recuperada, perampanel é um antagonista seletivo e não competitivo do receptor AMPA, que reduz a hiperexcitabilidade neuronal mediada por glutamato. Já foi aprovado em vários países como terapia adjuvante de crises focais.

A epilepsia visual (fotossensível) é uma epilepsia reflexa, ou seja, desencadeada por estímulos. Um fármaco com atividade antiepiléptica de amplo espectro pode, em tese, ser aplicável. Contudo, nenhuma das publicações recuperadas trata de crises desencadeadas por estímulos visuais. A pontuação muito alta do modelo provavelmente reflete a proximidade, na rede de conhecimento, com a indicação focal já aprovada, e não evidência direta.

O mesmo raciocínio vale para outras epilepsias reflexas previstas (crises de pensamento, de micção, de sobressalto, audiogênicas, de alimentação, de orgasmo e de leitura). Já o estado de mal epiléptico tem racionalidade biológica mais sólida: na crise prolongada, os receptores AMPA sinápticos aumentam e os receptores GABA-A são internalizados, reduzindo a eficácia dos benzodiazepínicos. Isso sustenta o antagonismo AMPA como estratégia complementar.

## Evidências de Ensaios Clínicos

Não há ensaios clínicos registrados para epilepsia visual. Os ensaios abaixo se referem à indicação com maior respaldo clínico entre as previstas, o estado de mal epiléptico.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04309721](https://clinicaltrials.gov/study/NCT04309721) | Phase 3 | Encerrado | 1 | Ensaio randomizado de perampanel enteral adicional a antiepiléptico intravenoso em estado de mal motor focal; encerrado com 1 participante, sem dados de eficácia |
| [NCT05684978](https://clinicaltrials.gov/study/NCT05684978) | Phase 4 | Encerrado | 1 | Perampanel no estado de mal refratário; encerrado com 1 participante, sem dados analisáveis |
| [NCT06401707](https://clinicaltrials.gov/study/NCT06401707) | Phase 2 | Recrutando | 52 | Estudo-piloto randomizado e controlado por placebo de perampanel para profilaxia de estado de mal após parada cardíaca |
| [NCT05756621](https://clinicaltrials.gov/study/NCT05756621) | N/A | Concluído | 84 | Coorte retrospectiva de estado de mal super-refratário pós-parada cardíaca com terapia anti-glutamato dupla (cetamina + perampanel); observacional |

## Evidências da Literatura

Para epilepsia visual, a literatura recuperada é geral (revisões, diretrizes e metanálises sobre perampanel e epilepsia). Abaixo, as publicações mais relevantes para o estado de mal epiléptico, priorizando revisões sistemáticas.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35151187](https://pubmed.ncbi.nlm.nih.gov/35151187/) | 2022 | Revisão sistemática | Epilepsy & Behavior | Avalia eficácia e segurança do perampanel em estado de mal, refratário e super-refratário |
| [30076046](https://pubmed.ncbi.nlm.nih.gov/30076046/) | 2018 | Revisão sistemática | Epilepsy & Behavior | Avalia eficácia e tolerabilidade do perampanel no estado de mal refratário e super-refratário |
| [30613951](https://pubmed.ncbi.nlm.nih.gov/30613951/) | 2019 | Coorte retrospectiva | Acta Neurol Scand | Casos multinacionais de uso do perampanel em estado de mal |
| [33754209](https://pubmed.ncbi.nlm.nih.gov/33754209/) | 2021 | Coorte | J Neurol | Coorte de 81 pacientes com estado de mal refratário e super-refratário, com revisão da literatura |
| [39436521](https://pubmed.ncbi.nlm.nih.gov/39436521/) | 2025 | Série de casos | Neurol Sci | Eficácia e segurança do perampanel em estado de mal refratário |
| [38761446](https://pubmed.ncbi.nlm.nih.gov/38761446/) | 2024 | Estudo clínico | Epilepsy & Behavior | Dose ideal e segurança da suspensão oral em estado de mal refratário e super-refratário |
| [30891695](https://pubmed.ncbi.nlm.nih.gov/30891695/) | 2019 | Estudo clínico | Neurocritical Care | Perampanel no estado de mal refratário em UTI neurológica |
| [25962657](https://pubmed.ncbi.nlm.nih.gov/25962657/) | 2015 | Estudo clínico | Epilepsy & Behavior | Uso em estado de mal refratário e super-refratário em UTI neurológica |
| [29663350](https://pubmed.ncbi.nlm.nih.gov/29663350/) | 2018 | Revisão | Epilepsia | Papel dos receptores AMPA e seus antagonistas no estado de mal |
| [32915470](https://pubmed.ncbi.nlm.nih.gov/32915470/) | 2020 | Estudo animal | Ann N Y Acad Sci | Perampanel e alopregnanolona como adjuvantes do midazolam em estado de mal induzido por DFP em ratos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 56 interações. Entre as listadas, a maioria é de gravidade moderada, incluindo morfina, codeína, hidrocodona, dexametasona, difenoxina, difenoxilato, dronabinol, nabilona, metoclopramida, ópio, sibutramina, etanol, prometazina, cloroquina, hidroxicloroquina, clorfeniramina, azelastina nasal e dextrometorfano. A claritromicina tem interação leve.
- **Eventos adversos descritos na literatura**: a literatura recuperada relata eventos psiquiátricos e comportamentais (irritabilidade, psicose, aversão alimentar), e menciona advertência de tarja preta para reações psiquiátricas graves, como agressividade.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Para epilepsia visual e demais epilepsias reflexas previstas, as evidências se limitam à previsão do modelo e a literatura indireta (L4/L5), sem estudos específicos. O estado de mal epiléptico (L3) tem séries de casos e revisões sistemáticas, mas os dois ensaios de fase 3 e 4 foram encerrados com 1 participante cada, sem evidência randomizada utilizável. Além disso, o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada (advertências e contraindicações), ainda não disponível.
- Esclarecer o mecanismo de ação em fonte detalhada (por exemplo, DrugBank).
- Para epilepsia visual: buscar evidência específica (séries de casos ou estudos em epilepsia fotossensível) antes de qualquer avanço.
- Para estado de mal epiléptico: acompanhar os resultados do ensaio de fase 2 NCT06401707 e avaliar um ensaio randomizado adequadamente dimensionado.
- Avaliar a situação regulatória no Brasil (sem registro vigente) e as formas farmacêuticas disponíveis, incluindo a via de administração necessária em contexto agudo.
- Definir plano de monitoramento de eventos psiquiátricos e de interações medicamentosas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

