---
layout: default
title: Entacapone
parent: Apenas Predição do Modelo (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Entacapone: nova indicação prevista, Neurodegeneração associada ao PLA2G6 (PLA2G6-associated neurodegenera… (nível de evidência L5). Indicação original: Antiparkinsonianos"
monitor_inn: "ENTACAPONE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
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

## Entacapona: De antiparkinsoniano à neurodegeneração associada ao PLA2G6
{: .text-alpha }

## Resumo em Uma Frase

Entacapona é um fármaco antiparkinsoniano, usado originalmente como terapia adjuvante no tratamento da doença de Parkinson.
O modelo TxGNN prevê que pode ser eficaz para **neurodegeneração associada ao PLA2G6 (PLA2G6-associated neurodegeneration)**, mas até o momento **não há ensaios clínicos nem publicações** que apoiem essa direção; trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiparkinsonianos |
| Nova Indicação Prevista | Neurodegeneração associada ao PLA2G6 (PLA2G6-associated neurodegeneration) |
| Pontuação de Previsão TxGNN | 99,76% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a entacapona é um inibidor da COMT (catecol-O-metiltransferase), que prolonga a ação da levodopa, e sua utilidade como adjuvante em Parkinson está estabelecida. Essa descrição vem de conhecimento geral, não dos dados fornecidos.

A neurodegeneração associada ao PLA2G6 (PLAN) pode incluir um fenótipo de distonia-parkinsonismo, o que torna plausível um vínculo dopaminérgico: a entacapona poderia, em tese, contribuir para o alívio sintomático do componente parkinsoniano.

Há, porém, uma limitação importante. A entacapona não atua sobre o defeito de base (metabolismo lipídico relacionado ao gene PLA2G6). Portanto, no máximo se esperaria efeito sintomático, e a previsão do modelo carece de qualquer confirmação clínica ou da literatura.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os registros de entacapona no Brasil constam como cancelados; não há registro válido atualmente.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100470633 (cancelado) | COMTAN | Não informada | Antiparkinsonianos |
| Registro 135690587 (cancelado) | ENTARKIN | Não informada | Antiparkinsonianos |
| Registro 100470632 (cancelado) | STALEVO | Não informada | Antiparkinsonianos |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento (não extraídas da bula)**: o grafo de conhecimento do TxGNN (PrimeKG) associa a entacapona a contraindicações em diversas condições, entre elas:
  - Neurológicas e psiquiátricas: epilepsia, discinesia induzida por medicamentos, atrofia de múltiplos sistemas, transtornos psicóticos e esquizoafetivos, transtornos de ansiedade.
  - Cardiovasculares: hipotensão ortostática, síndrome de taquicardia postural ortostática, infarto do miocárdio, trombose coronariana, parada cardíaca súbita, doenças da condução cardíaca.
  - Hepáticas, renais e digestivas: doença hepática, doença renal, doença da vesícula biliar, úlcera gástrica e péptica, doenças diarreicas.
  - Outras: glaucoma de ângulo aberto e de ângulo fechado, diabetes mellitus, cetoacidose diabética, melanoma, hemoglobinopatia.
- **Interações Medicamentosas**: foram identificadas 82 interações. As listadas como de nível moderado incluem:
  - Epinefrina (incluindo as formas oftálmica e tópica)
  - Morfina (incluindo a forma lipossomal) e ópio
  - Dronabinol e nabilona
  - Metoclopramida
  - Ferro

  Há ainda interações de nível desconhecido, como as com inibidores da bomba de prótons (pantoprazol, omeprazol, lansoprazol), doxiciclina, metformina, atropina, lactulose, prednisona, sinvastatina e cloreto de potássio.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura. A entacapona não atua sobre o defeito de base da doença, e todos os registros brasileiros estão cancelados.
- Entre as demais previsões analisadas, a demência com corpos de Lewy (nível L4) tem apenas evidência indireta pré-clínica; ela merece ser tratada como pergunta de pesquisa, não como candidata a uso.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) da entacapona.
- Bula da ANVISA com advertências e contraindicações, hoje ausentes, o que bloqueia a triagem de segurança.
- Evidências de literatura ou relatos de caso em PLAN, especialmente em fenótipos com distonia-parkinsonismo.
- Avaliação de viabilidade regulatória e comercial, dado que não há registro válido no Brasil.
- Análise de risco-benefício frente às contraindicações do grafo, em especial as cardiovasculares, hepáticas e psiquiátricas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

