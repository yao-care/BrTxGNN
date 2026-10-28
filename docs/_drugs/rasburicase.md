---
layout: default
title: Rasburicase
parent: Apenas Predição do Modelo (L5)
nav_order: 560
evidence_level: L5
indication_count: 10
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
last_modified_at: 2026-10-28
description: "Rasburicase: nova indicação prevista, Hipouricemia Renal (hypouricemia, renal) (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Rasburicase
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

## Rasburicase: Hipouricemia Renal (hypouricemia, renal)
{: .text-alpha }

## Resumo em Uma Frase

Rasburicase é uma enzima urato oxidase recombinante, originalmente associada ao tratamento da hiperuricemia.
O modelo TxGNN prevê que pode ser eficaz para **Hipouricemia Renal (hypouricemia, renal)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão não tem respaldo mecanístico plausível.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Hipouricemia Renal (hypouricemia, renal) |
| Pontuação de Previsão TxGNN | 0.9999 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a rasburicase é uma urato oxidase recombinante que converte o ácido úrico em alantoína, reduzindo o ácido úrico sérico. Sua eficácia na hiperuricemia decorre exatamente dessa ação.

A hipouricemia renal é uma condição em que o ácido úrico sérico já é baixo, por defeito na reabsorção renal de urato (por exemplo, variantes de SLC22A12/URAT1 ou SLC2A9). Reduzir ainda mais o urato seria mecanisticamente contraproducente e potencialmente prejudicial. **A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica**, e não um vínculo terapêutico racional.

As demais previsões entre as dez primeiras também carecem de respaldo. A deficiência parcial de HPRT (rank 2) é a única com relação conceitual com o ácido úrico, mas a rasburicase não corrige o defeito enzimático nem as manifestações neurológicas. Além disso, é de uso intravenoso, com limitações de imunogenicidade e risco de hemólise e metemoglobinemia na deficiência de G6PD. As previsões para porfiria hepática, esclerose hepatoportal, síndrome hepatopulmonar, hipertensão portal familiar de início precoce, trombose primária da veia porta, cirrose associada ao cobre, acidose tubular renal e distúrbios do metabolismo da fenilalanina não têm mecanismo identificado e parecem refletir associações de rede.

## Previsões Adicionais do Modelo (sem evidências)

| Posição | Doença prevista | Pontuação TxGNN | Avaliação |
|------|------|------|------|
| 2 | Deficiência parcial de HPRT | 0,9997 | Relevância conceitual limitada; uso crônico impraticável |
| 3 | Porfiria hepática | 0,9997 | Sem vínculo mecanístico |
| 4 | Esclerose hepatoportal | 0,9997 | Sem mecanismo plausível |
| 5 | Síndrome hepatopulmonar | 0,9997 | Sem mecanismo conhecido |
| 6 | Hipertensão portal familiar não cirrótica de início precoce | 0,9997 | Sem racional |
| 7 | Trombose primária da veia porta | 0,9997 | Sem vínculo com urato oxidase |
| 8 | Cirrose idiopática associada ao cobre | 0,9997 | Sem efeito conhecido no metabolismo do cobre |
| 9 | Acidose tubular renal | 0,9985 | Sem ação conhecida; associação indireta |
| 10 | Distúrbio do metabolismo da fenilalanina | 0,9983 | Sem suporte mecanístico ou clínico |

## Considerações de Segurança

- **Interações Medicamentosas** (13 registradas, fonte: DDInter):
  - **Maior gravidade**: prilocaína e ácido nitroso.
  - **Gravidade moderada**: idelalisibe e anestésicos locais, como tetracaína (oftálmica e tópica), lidocaína (tópica e oftálmica), benzocaína, cocaína (tópica e nasal), proparacaína, oxibuprocaína e cinchocaína.
- **Riscos adicionais** (do raciocínio da previsão): risco de hemólise e metemoglobinemia em pacientes com deficiência de G6PD, e imunogenicidade (anticorpos antifármaco) em uso repetido.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para nenhuma das indicações previstas (nível L5). Para a principal (hipouricemia renal), o mecanismo indica efeito contraproducente, e a pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), hoje uma lacuna bloqueante.
- Obter dados do mecanismo de ação na DrugBank.
- Reavaliar as previsões de forma crítica, e só considerar a deficiência parcial de HPRT, se houver, com revisão de especialista e evidência pré-clínica ou clínica.
- Avaliar a viabilidade regulatória e de acesso, já que não há registro no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

