---
layout: default
title: Risperidone
parent: Apenas Predição do Modelo (L5)
nav_order: 569
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Risperidone: nova indicação prevista, Paralisia do olhar horizontal familiar com escoliose progressiva (gaz… (nível de evidência L5). Indicação original: Neurolépticos (antipsicótico)"
monitor_inn: "RISPERIDONE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
---

# Risperidone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

# Risperidona: De neurolépticos à paralisia familiar do olhar horizontal com escoliose progressiva

## Resumo em Uma Frase

A risperidona é um antipsicótico atípico, registrado no Brasil na classe dos neurolépticos.
O modelo TxGNN prevê que ela poderia ser eficaz para **paralisia do olhar horizontal familiar com escoliose progressiva (gaze palsy, familial horizontal, with progressive scoliosis)**.
Atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Neurolépticos (antipsicótico) |
| Nova Indicação Prevista | Paralisia do olhar horizontal familiar com escoliose progressiva (gaze palsy, familial horizontal, with progressive scoliosis) |
| Pontuação de Previsão TxGNN | 99,76% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nas fontes compiladas. A risperidona é conhecida por antagonizar os receptores de dopamina D2 e de serotonina 5-HT2A. Essa ação sustenta seu uso em esquizofrenia, mania bipolar e irritabilidade associada ao autismo.

A nova indicação prevista é uma doença genética rara, relacionada ao gene ROBO3, que afeta a orientação dos axônios no tronco encefálico. Ela causa limitação dos movimentos oculares horizontais e escoliose progressiva. Não há vínculo mecanístico plausível entre o bloqueio D2/5-HT2A e essa patologia.

A pontuação alta do TxGNN (99,76%) é uma associação calculada pelo grafo de conhecimento. Ela não é respaldada por nenhum ensaio clínico ou publicação. Portanto, deve ser tratada como um sinal computacional, não como uma hipótese terapêutica sustentada.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Dos 20 registros localizados, todos estão cancelados. Não há registro vigente de risperidona isolada nem em associação. Abaixo estão 5 dos registros, incluindo os nomes comerciais distintos.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105730599 | ZARGUS | Não informada | Neurolépticos |
| Registro nº 125680292 | PERLID | Não informada | Neurolépticos |
| Registro nº 104971134 | VIVERDAL | Não informada | Neurolépticos |
| Registro nº 155370028 | RISPERAC | Não informada | Neurolépticos |
| Registro nº 104971412 | RISPERIDONA | Não informada | Neurolépticos |

## Considerações de Segurança

Não há advertências nem contraindicações de bula nas fontes compiladas. Consulte a bula para as informações de segurança oficiais.

- **Contraindicações e precauções do grafo de conhecimento** (relações fármaco-doença do TxGNN, que não são texto de bula): hipotensão ortostática e outras condições hipotensivas, epilepsia, doença hepática e insuficiência hepática, diabetes, hiperglicemia e cetoacidose diabética, neutropenia e agranulocitose, hiperlipidemia, obesidade, AVC e doenças cerebrovasculares, infarto do miocárdio e outras doenças cardiovasculares e de condução cardíaca, e carcinoma de mama feminino.
- **Interações medicamentosas:** foram identificadas 100 interações, das quais 20 foram detalhadas.
  - **Graves:** bupropiona e morfina.
  - **Moderadas (exemplos):** metformina, acarbose, alogliptina, albiglutida, canagliflozina, epinefrina, hidrocortisona, anfotericina B, atropina, loperamida, hiosciamina, glicopirrônio, clidínio, bisacodil, lorcasserina e famotidina.
  - **Leve:** ranitidina.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações, e o nível de evidência é L5.
- Não existe vínculo mecanístico plausível entre a ação da risperidona e a fisiopatologia da doença.
- Todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação documentados e uma justificativa biológica para a doença ligada ao ROBO3.
- Estudos pré-clínicos ou relatos de casos que indiquem algum benefício.
- Bula e informações de segurança atualizadas, e confirmação de disponibilidade regulatória, já que não há registro vigente no Brasil.

**Observação sobre outras previsões do modelo:** para o mesmo fármaco, o TxGNN apontou indicações com evidência bem mais robusta.
- O **transtorno afetivo maior (depressão resistente ao tratamento e transtorno bipolar)** tem nível L1, com dois ensaios de Fase 3 concluídos e metanálises de apoio.
  - Os ensaios são NCT00095134 (630 participantes) e NCT00044681 (258 participantes), ambos sobre risperidona como adjuvante a antidepressivos.
  - Esse caminho é recomendado como Proceed with Guardrails, com monitoramento de efeitos metabólicos, prolactina, sintomas extrapiramidais e ganho de peso.
- A **tricotilomania** tem nível L4, com apenas relatos e séries de casos.
- A **síndrome de Phelan-McDermid** tem nível L4, com revisão e estudo pré-clínico em peixe-zebra.

Se o objetivo é reposicionar a risperidona, essas indicações merecem prioridade sobre a paralisia do olhar horizontal familiar.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

