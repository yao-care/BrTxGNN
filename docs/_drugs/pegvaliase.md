---
layout: default
title: Pegvaliase
parent: Apenas Predição do Modelo (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pegvaliase: nova indicação prevista, Retinopatia diabética (diabetic retinopathy) (nível de evidência L5). Indicação original: Não disponível nos dados de registro da ANVISA (o uso conhecido do fá…"
monitor_inn: "Pegvaliase"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract", "nuclear senile cataract", "cortical cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "tetanic cataract", "craniostenosis cataract", "immature cataract"]
---

# Pegvaliase
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

# Pegvaliase: Da fenilcetonúria à retinopatia diabética

## Resumo em Uma Frase

Pegvaliase é uma enzima fenilalanina amônia-liase peguilada, que degrada a fenilalanina e cujo uso aprovado em outros países é a fenilcetonúria. Não há indicação original registrada no Brasil nos dados compiládos para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **retinopatia diabética (diabetic retinopathy)**, porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro da ANVISA (o uso conhecido do fármaco é fenilcetonúria) |
| Nova Indicação Prevista | Retinopatia diabética (diabetic retinopathy) |
| Pontuação de Previsão TxGNN | 99,17% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, pegvaliase é uma fenilalanina amônia-liase peguilada que degrada a fenilalanina, e seu uso aprovado é a fenilcetonúria.

Não foi estabelecida nenhuma relação mecanística entre a depleção de fenilalanina e a patologia microvascular da retina diabética. A pontuação elevada do TxGNN (0,992) é uma previsão derivada do grafo de conhecimento e, por si só, não constitui prova de plausibilidade biológica.

As demais previsões do modelo seguem o mesmo padrão: retinopatia diabética não proliferativa grave (99,16%) e vários tipos de catarata (diabética, nuclear senil, cortical, madura, imatura, entre outras; 98,9% a 99,1%). Todas sem ensaios ou literatura. Pontuações idênticas entre subtipos de catarata sugerem um artefato de proximidade no grafo, e não uma biologia específica de cada doença.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 16 interações de nível moderado (fonte: DDInter), principalmente com outros fármacos peguilados ou biológicos:
  - Fatores de coagulação: fator anti-hemofílico recombinante humano e fator IX de coagulação humano
  - Fármacos peguilados: certolizumabe pegol, pegaptanibe (oftálmico), pegloticase, pegademase, pegaspargase, pegfilgrastim, peginesatida, peginterferona alfa-2a, alfa-2b e beta-1a, pegvisomanto
  - Outros: doxorrubicina lipossomal, acetato de medroxiprogesterona e naloxegol

Não há dados disponíveis sobre advertências principais e contraindicações da bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é baseada apenas no modelo (L5), sem ensaios clínicos, sem literatura e sem mecanismo plausível. Além disso, o fármaco não é comercializado no Brasil e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula e os dados de segurança (advertências e contraindicações), etapa bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação (MOA) via DrugBank
- Propor e testar uma hipótese biológica que ligue a degradação de fenilalanina à retinopatia diabética, com estudos pré-clínicos
- Avaliar a viabilidade da via de administração (a via sistêmica peguilada versus a necessidade de acesso ocular) e a situação regulatória no Brasil
- Buscar sinais clínicos ou de literatura antes de qualquer reavaliação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

