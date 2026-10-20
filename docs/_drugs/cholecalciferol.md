---
layout: default
title: Cholecalciferol
parent: Apenas Predição do Modelo (L5)
nav_order: 221
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cholecalciferol: nova indicação prevista, Hipoparatireoidismo isolado familiar por secreção deficiente de PTH (nível de evidência L5). Indicação original: Vitamina D e análogos"
monitor_inn: "CHOLECALCIFEROL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

# Colecalciferol: De vitamina D e análogos para hipoparatireoidismo isolado familiar por secreção deficiente de PTH

## Resumo em Uma Frase

Colecalciferol (vitamina D3) é registrado na ANVISA na categoria "vitamina D e análogos".
O modelo TxGNN prevê que pode ser eficaz para **hipoparatireoidismo isolado familiar por secreção deficiente de PTH**, mas até o momento há **0 ensaios clínicos** e **0 publicações** específicas apoiando esta direção. A previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Vitamina D e análogos |
| Nova Indicação Prevista | Hipoparatireoidismo isolado familiar por secreção deficiente de PTH |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o colecalciferol é um pró-hormônio da vitamina D. É convertido no fígado em 25-hidroxivitamina D e, depois, no rim em calcitriol, a forma ativa. O calcitriol atua no intestino, nos ossos e nos rins para regular cálcio e fosfato.

A biologia da previsão é plausível. Metabólitos da vitamina D são usados no hipoparatireoidismo para elevar o cálcio sérico. Nessa condição, porém, há um obstáculo importante: a ativação do colecalciferol nativo depende da 1-alfa-hidroxilação renal, que é estimulada pelo PTH. Quando a secreção de PTH está comprometida, essa conversão fica prejudicada. Por isso, análogos ativos como calcitriol ou alfacalcidol costumam ser preferidos ao colecalciferol nativo.

A ligação entre a indicação original e a nova é, portanto, apenas uma previsão do grafo de conhecimento. Os dados compilados para este relatório não trazem estudos que a confirmem.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os 20 registros localizados estão **cancelados**, e não há registro válido atualmente. Principais registros (5 de 20):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100431390 | OHDE CAPS | Não informada | Vitamina D e análogos |
| Registro 105730171 | VIT. D SOLEIL CAPS | Não informada | Vitamina D e análogos |
| Registro 143810246 | VITAMINA D CIMED | Não informada | Vitamina D e análogos |
| Registro 100380106 | DEFULL | Não informada | Vitamina D e análogos |
| Registro 170420025 | VITAMINA D3 | Não informada | Análogo sintético da vitamina D |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): hipertensão, doença renal, doença hepática, doença da vesícula biliar, gastrite, sarcoidose, diabetes mellitus, cetoacidose diabética, fibrilação atrial, hiperparatireoidismo, osteíte fibrosa, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, distúrbios da coagulação, anemia falciforme, hiperoxalúria primária, hemocromatose hereditária, hemossiderose, doença de Wilson, câncer de mama feminino, câncer de próstata, hiperlipidemia e hiperlipidemia familiar, entre outras.
- **Interações medicamentosas** (56 registradas):
  - **Gravidade maior**: calcifediol, calcitriol, di-hidrotaquisterol e doxercalciferol. Combinar análogos da vitamina D aumenta o risco de hipercalcemia.
  - **Gravidade moderada**: diuréticos tiazídicos (clortalidona, clorotiazida, bendroflumetiazida, benzotiazida), barbitúricos (amobarbital, butabarbital, butalbital), carbamazepina, digoxina e digitoxina, e sequestrantes de ácidos biliares (colestiramina, colesevelam, colestipol).
  - **Gravidade menor**: cimetidina.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do modelo é muito alta (99,79%), mas não há ensaios clínicos nem literatura específica (nível L5).
- A ativação do colecalciferol nativo depende do PTH, o que o torna menos adequado que análogos ativos nessa condição.
- Os 20 registros brasileiros estão cancelados.
- Na mesma lista de previsões, a **doença óssea renal (osteodistrofia renal)** tem muito mais suporte (nível L2). Inclui um ensaio de Fase 3 (NCT00752401, status desconhecido e sem resultados) e um estudo comparativo concluído contra doxercalciferol (NCT00285467). Essa indicação merece avaliação prioritária, com monitoramento de cálcio, fosfato e PTH.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação (MOA) e comparação direta com calcitriol/alfacalcidol no hipoparatireoidismo.
- Revisão dirigida da literatura e dos registros de ensaios para esta doença rara.
- Informações de segurança da bula da ANVISA, incluindo risco de hipercalcemia.
- Verificação do status regulatório, já que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

