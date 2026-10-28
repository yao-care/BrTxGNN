---
layout: default
title: Prilocaine
parent: Apenas Predição do Modelo (L5)
nav_order: 549
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Prilocaine: nova indicação prevista, Conjuntivite papilar (papillary conjunctivitis) (nível de evidência L5). Indicação original: Anestésicos locais"
monitor_inn: "Prilocaine"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
---

# Prilocaine
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

## Prilocaína: De anestésico local para Conjuntivite Papilar (predição principal do modelo)
{: .text-alpha }

## Resumo em Uma Frase

Prilocaína é um anestésico local do tipo amida, registrado na ANVISA na classe dos "anestésicos" e "anestésicos locais".
O modelo TxGNN prevê que pode ser eficaz para **conjuntivite papilar (papillary conjunctivitis)**, mas não há nenhum ensaio clínico nem publicação que apoie essa direção (**0 ensaios clínicos** e **0 publicações**).
Entre as 10 indicações previstas, a única com sinal minimamente plausível é a **neuralgia (neuralgia)**, com **2 ensaios clínicos** listados (apenas 1 diretamente relacionado) e **13 publicações**, em sua maioria sobre neuralgia pós-herpética com o creme EMLA.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos locais |
| Nova Indicação Prevista (1ª colocada) | Conjuntivite papilar (papillary conjunctivitis) |
| Pontuação de Previsão TxGNN | 0,9978 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

> Observação: a indicação em primeiro lugar no ranking do modelo não tem nenhuma evidência. A indicação com mais evidência é a neuralgia (nível L2 segundo a pontuação compilada, com ressalvas importantes; ver abaixo).

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a prilocaína é um anestésico local do tipo amida que bloqueia canais de sódio dependentes de voltagem, e sua eficácia como anestésico local é estabelecida. Mecanisticamente, esse bloqueio poderia aliviar sintomas ligados à ativação de fibras nervosas, como dor ou desconforto.

Para **conjuntivite papilar**, o benefício se limitaria, no máximo, ao alívio do desconforto da superfície ocular. Não trataria a causa alérgica ou mecânica da inflamação, e o uso prolongado de anestésicos locais no olho é prejudicial à córnea. A previsão tem, portanto, baixa plausibilidade biológica e é puramente computacional.

Entre as demais previsões, a **neuralgia** é a mais coerente: a prilocaína, geralmente combinada com lidocaína (creme EMLA), atua nos nociceptores periféricos, e há relatos antigos de alívio na neuralgia pós-herpética. Contudo, isso é mais uma extensão da indicação anestésica existente do que um reposicionamento verdadeiro. Outras previsões (transtorno bipolar maníaco, bronquite, enxaqueca com aura do tronco encefálico, conjuntivite da rosácea) não têm base mecanística clara.

## Evidências de Ensaios Clínicos

A indicação em primeiro lugar (conjuntivite papilar) não tem ensaios clínicos registrados. Abaixo, os ensaios disponíveis para a indicação com maior volume de evidência (neuralgia):

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | Concluído | 20 | Estudo aberto sobre creme de lidocaína 2,5%/prilocaína 2,5% como pré-tratamento do adesivo de capsaicina NGX-4010 em neuralgia pós-herpética. Avalia tolerabilidade, não eficácia contra a neuralgia; pequeno, sem controle e com efeito da combinação não atribuível à prilocaína isolada |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | N/A | Concluído | 38 | Toxina botulínica A vs. prilocaína na síndrome dolorosa miofascial. Relevância baixa para a nova indicação |

Para enxaqueca, o único ensaio listado (NCT02403687, estudo observacional de AINEs tópicos, 300 participantes) não testa prilocaína e tem relevância não confirmada.

## Evidências da Literatura

Publicações mais relevantes para neuralgia (a literatura para as demais indicações é indireta ou sobre segurança):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | Estudo clínico | Pain | EMLA 5% por 24 h em 12 pacientes com neuralgia pós-herpética refratária: melhora significativa da dor em 6 h, com perfil farmacocinético |
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | Estudo clínico | BMJ | Creme de lignocaína-prilocaína em neuralgia pós-herpética (sem resumo disponível) |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | Estudo clínico | BMC Anesthesiology | Tolerabilidade do adesivo de capsaicina 8% após pré-tratamento com creme lidocaína/prilocaína em neuralgia pós-herpética |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | Relato de caso | J Clin Anesth | Tratamento bem-sucedido com EMLA de neuralgia pós-herpética resistente a outras terapias |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Revisão | J Dermatol Surg Oncol | EMLA como anestésico tópico eficaz e seguro; cita uso em neuralgia pós-herpética entre outras indicações |
| [10342425](https://pubmed.ncbi.nlm.nih.gov/10342425/) | 1999 | Estudo experimental | Pain | Resultado negativo: EMLA não reduziu a dor da capsaicina tópica 1% em 9 voluntários saudáveis |
| [41777672](https://pubmed.ncbi.nlm.nih.gov/41777672/) | 2026 | Coorte retrospectiva | Front Aging Neurosci | EMLA isolado vs. bloqueio paravertebral + EMLA para tolerabilidade do adesivo de capsaicina 8% em neuralgia pós-herpética torácica |
| [7897165](https://pubmed.ncbi.nlm.nih.gov/7897165/) | 1995 | Relato de caso | J Allergy Clin Immunol | Dermatite alérgica de contato induzida por EMLA, com papel da prilocaína como imunógeno |

Alertas de segurança vindos da literatura de outras indicações: em dermatite atópica, a pele com barreira comprometida aumenta a absorção sistêmica, com relato de convulsões e metemoglobinemia em criança após EMLA ([27397059](https://pubmed.ncbi.nlm.nih.gov/27397059/)), além de alergia de contato e púrpura. Para enxaqueca, a única publicação listada ([37400308](https://pubmed.ncbi.nlm.nih.gov/37400308/), 2023) trata de função microvascular em mulheres com SOP e não testa prilocaína.

## Informações de Comercialização no Brasil

O medicamento é comercializado no Brasil: os 5 registros existentes (5 de 5) estão válidos.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100850244 | Baritekal Hiperbárica | Não informada | Anestésicos |
| Registro 137640156 | Emla | Não informada | Anestésicos locais |
| Registro 102980033 | Medicaína | Não informada | Anestésicos locais |
| Registro 101770028 | Prilonest | Não informada | Anestésicos locais |
| Registro 102980330 | Citocaína | Não informada | Anestésicos locais |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento do modelo** (relações fármaco-doença, não texto de bula): doenças hipertensivas, epilepsia, doença renal, doença hepática, doença da vesícula biliar, diabetes mellitus e cetoacidose diabética, doença arterial coronariana e infarto do miocárdio, hemoglobinopatias, parada cardíaca súbita, doenças do sistema de condução cardíaco e bloqueio atrioventricular, insuficiência respiratória, glaucoma de ângulo fechado, miastenia gravis e doenças da junção neuromuscular, deficiência de butirilcolinesterase, doenças cardiovasculares, hipertireoidismo e doença de Graves.
- **Interações medicamentosas** (22 registradas; principais):
  - **Gravidade maior**: metoclopramida, sulfassalazina, nitrito de amila, rasburicase, ácido nitroso, óxido nítrico (risco aditivo de metemoglobinemia em vários casos), cloroquina, primaquina, quinina, tafenoquina, lidocaína (sistêmica e tópica), benzocaína tópica, dapsona (sistêmica e tópica), cinchocaína tópica, nitrato de prata tópico, sulfadiazina de prata tópica.
  - **Gravidade moderada**: morfina lipossomal.
  - **Gravidade menor**: hialuronidase.
- **Riscos adicionais descritos na literatura**: metemoglobinemia e toxicidade do sistema nervoso central (convulsões) com absorção sistêmica, especialmente em crianças e em pele com barreira comprometida; alergia de contato à prilocaína.

Os dados de advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A indicação com maior pontuação (conjuntivite papilar) tem apenas previsão computacional, sem estudos, e com baixa plausibilidade biológica. Para neuralgia, a evidência é limitada a estudos pequenos e antigos com a combinação lidocaína/prilocaína, que não permitem atribuir o efeito à prilocaína e representam uma extensão da indicação anestésica, não um reposicionamento verdadeiro. Os 5 registros brasileiros (5 de 5) estão válidos.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que impede a triagem de segurança.
- Obter dados detalhados do mecanismo de ação.
- Se houver interesse em neuralgia, tratá-la como pergunta de pesquisa: revisão sistemática e ensaio controlado moderno que isole o efeito da prilocaína (ou justifique a combinação), com plano de monitoramento de metemoglobinemia.
- Verificar a viabilidade regulatória, dado que não há registro válido de prilocaína no Brasil, e definir via de administração e forma farmacêutica adequadas.
- Para conjuntivite papilar e demais indicações sem evidência, não priorizar investimento sem nova justificativa mecanística.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

