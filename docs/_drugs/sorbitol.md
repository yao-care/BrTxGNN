---
layout: default
title: Sorbitol
parent: Apenas Predição do Modelo (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Sorbitol
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

# Sorbitol: Da ausência de indicação registrada no Brasil à hipertermia maligna induzida por exercício

## Resumo em Uma Frase

Sorbitol é um álcool de açúcar (poliol) osmótico, sem indicação original registrada na ANVISA e atualmente não comercializado no Brasil como medicamento registrado.
O modelo TxGNN prevê que pode ser eficaz para **hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia)**, mas **não há ensaios clínicos nem publicações** que sustentem essa direção.
A previsão é puramente baseada em grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não informada (nenhuma licença registrada na ANVISA) |
| Nova Indicação Prevista | Hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia) |
| Pontuação de Previsão TxGNN | 99,40% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Sabe-se que o sorbitol é um álcool de açúcar com ação osmótica, usado sobretudo como excipiente, adoçante e laxante osmótico, e que participa da via dos polióis (aldose redutase).

Não foi identificada relação mecanística plausível com a nova indicação. A hipertermia maligna envolve a liberação desregulada de cálcio no músculo esquelético (via RYR1), e o sorbitol não tem ação conhecida sobre essa via. A pontuação elevada do TxGNN reflete apenas proximidade no grafo de conhecimento, não um fundamento biológico ou clínico.

Por isso, a previsão deve ser tratada como hipótese sem sustentação, e não como candidata concreta ao reposicionamento.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação prevista (hipertermia maligna induzida por exercício).

## Outras Indicações Previstas (Contexto)

Entre as demais previsões do modelo, apenas as duas abaixo têm alguma literatura, ainda assim indireta:

| Indicação | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Insuficiência cardíaca congestiva | 98,77% | L5 | Literatura indica o sorbitol como possível marcador/contribuinte patogênico no coração diabético (PMID 33558456), e não como agente terapêutico. Sem evidência clínica de benefício. |
| Otite média infecciosa | 98,74% | L4 | Um ensaio randomizado (PMID 37890960) testou xilitol, não sorbitol, na prevenção de otite média aguda; o sorbitol foi usado como comparador. Extrapolação de classe não sustentada. |

As demais previsões (epiglotite, toxocaríase, cor pulmonale agudo, granuloma de colesterol da orelha média, otossalpingite, otite média alérgica e paralisia periódica familiar) não têm evidências nem plausibilidade mecanística identificadas.

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não bula)**: doença ulcerosa péptica ativa.
- **Interações Medicamentosas** (2 identificadas):
  - **Tolevamer**: gravidade **Maior**.
  - **Lamivudina**: gravidade **Moderada**.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que apoiem o sorbitol na hipertermia maligna induzida por exercício, e não existe vínculo mecanístico plausível. O fármaco não possui registro como medicamento no Brasil, e a previsão (L5) baseia-se apenas no modelo.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação que justifiquem a hipótese, caso ela seja mantida.
- Obtenção e análise da bula (advertências e contraindicações) para a triagem de segurança.
- Estudos pré-clínicos que testem a hipótese antes de qualquer avanço.
- Reavaliação do conjunto de candidatas, pois outras indicações previstas (insuficiência cardíaca e otite média) também carecem de evidência direta e não justificam priorização.
- Definição da situação regulatória no Brasil, já que não há registro vigente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

