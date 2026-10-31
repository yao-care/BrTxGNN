---
layout: default
title: Enflurane
parent: Apenas Predição do Modelo (L5)
nav_order: 289
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
description: "Enflurane: nova indicação prevista, Transtorno Afetivo Bipolar Maníaco (Manic Bipolar Affective Disorder) (nível de evidência L5). Indicação original: Anestésicos gerais voláteis e gasosos"
monitor_inn: "enflurane"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "dysthymic disorder", "Prinzmetal angina", "myofascial pain syndrome", "migraine disorder", "bipolar disorder"]
---

# Enflurane
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Enflurano: Da anestesia geral ao Transtorno Afetivo Bipolar Maníaco
{: .text-alpha }

## Resumo em Uma Frase

Enflurano é um anestésico geral volátil (éter halogenado), originalmente usado para anestesia geral por inalação.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno Afetivo Bipolar Maníaco (Manic Bipolar Affective Disorder)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção: trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos gerais voláteis e gasosos |
| Nova Indicação Prevista | Transtorno Afetivo Bipolar Maníaco (Manic Bipolar Affective Disorder) |
| Pontuação de Previsão TxGNN | 0,9969 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 4) |
| Número de Registros | 4 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este fármaco. Segundo informações conhecidas, o enflurano é um anestésico inalatório halogenado que potencializa os receptores GABA-A e modula a atividade de canais de glicina, NMDA e potássio.

A ligação com o transtorno bipolar é especulativa: a modulação gabaérgica e glutamatérgica poderia, em tese, relacionar-se à estabilização do humor. No entanto, não há ensaios clínicos nem literatura que sustentem essa indicação, e a pontuação alta do TxGNN (0,9969) é apenas uma previsão computacional.

Há ainda fatores que limitam a viabilidade: o enflurano tem perfil pró-convulsivante no EEG e seu registro no Brasil está cancelado.

### Outras indicações previstas (todas nível L5, decisão Hold)

| Posição | Doença prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Síndrome de Tourette | 0,9947 | Sem racional mecanístico direto; apenas hipótese via depressão do SNC e modulação gabaérgica |
| 3 | Tricotilomania | 0,9938 | Condição crônica e comportamental, pouco adequada a um anestésico inalatório de ação curta |
| 4 | Transtorno distímico | 0,9914 | Sem uso plausível para um anestésico inalatório |
| 5 | Angina de Prinzmetal | 0,9914 | Efeito vasodilatador teórico, mas o enflurano causa depressão miocárdica e hipotensão |
| 6 | Síndrome dolorosa miofascial | 0,9911 | Relaxamento muscular transitório, ligado à anestesia geral |
| 7 | Enxaqueca | 0,9908 | Sem suporte; pode até provocar cefaleia |
| 8 | Transtorno bipolar | 0,9905 | Sobreposta à previsão de mania bipolar; sem validação |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102980157 | ENFLURAN | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 100630217 | ENURAN | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100630220 | ENFLURANO | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 105530138 | ETRANE | ABBOTT LABORATÓRIOS DO BRASIL LTDA | Cancelado |

## Considerações de Segurança

- **Contraindicações (com base no grafo de conhecimento, não em bula)**: epilepsia, hipertermia maligna da anestesia, hipertermia maligna induzida por exercício, distrofia muscular de Duchenne, distrofia muscular e distrofia muscular de Becker.
- **Interações Medicamentosas** (13 interações registradas):
  - **Grave**: epinefrina.
  - **Moderadas**: opioides (morfina, ópio, codeína, hidrocodona); aminoglicosídeos (amicacina, amicacina lipossomal, gentamicina, canamicina, neomicina, paromomicina, estreptomicina); ceritinibe.

Consulte a bula para demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é puramente computacional (L5), sem ensaios clínicos nem publicações. Além disso, o fármaco tem registro cancelado no Brasil, perfil pró-convulsivante e contraindicações relevantes (epilepsia, hipertermia maligna), o que reduz muito a viabilidade.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos ou revisão da literatura que sustentem a ligação com o transtorno bipolar
- Avaliar a compatibilidade de via de administração e a justificativa para um anestésico inalatório em condição crônica
- Considerar alternativas já comercializadas com mecanismo semelhante, dado o cancelamento do registro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

