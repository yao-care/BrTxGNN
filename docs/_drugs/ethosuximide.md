---
layout: default
title: Ethosuximide
parent: Apenas Predição do Modelo (L5)
nav_order: 303
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Ethosuximide: nova indicação prevista, Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrom… (nível de evidência L5). Indicação original: Anticonvulsivantes"
monitor_inn: "ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
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

## Etosuximida: Do tratamento anticonvulsivante à síndrome nefrogênica de antidiurese inapropriada
{: .text-alpha }

## Resumo em Uma Frase

Etosuximida é um anticonvulsivante, registrado no Brasil na classe dos anticonvulsivantes.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| Pontuação de Previsão TxGNN | 99,91% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a etosuximida é geralmente descrita como bloqueadora de canais de cálcio do tipo T em neurônios talâmicos, o que explica seu uso em crises anticonvulsivantes (em especial crises de ausência).

A NSIAD é causada por mutações de ganho de função no receptor V2 da vasopressina (AVPR2), que levam à ativação constitutiva do receptor e à retenção de água independentemente da vasopressina. Não há, nos dados disponíveis, nenhuma ligação farmacológica plausível entre o bloqueio de canais de cálcio do tipo T e a hiperatividade do receptor V2.

Assim, a única sustentação da previsão é a pontuação muito alta do modelo (0,999), cuja justificativa não está disponível. Qualquer conexão seria especulativa e exigiria validação mecanística independente. A previsão pode refletir artefatos do grafo de conhecimento, como fenótipos compartilhados (hiponatremia ou crises convulsivas), e não uma relação farmacológica real.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101180141 (cancelado) | ETOXIN | Não informada | Anticonvulsivantes |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento do TxGNN (não são texto de bula)**: ansiedade, transtorno neurótico, transtorno distímico, doença renal, piureter, doença hematológica, doença hepática, doença da vesícula biliar, lúpus eritematoso sistêmico (inclusive pediátrico), neutropenia, agranulocitose e porfiria aguda intermitente.
- **Interações Medicamentosas**: foram identificadas 92 interações no total; entre as listadas, todas de gravidade moderada, estão:
  - Depressores do SNC e opioides: morfina (inclusive lipossomal), ópio, etanol, dronabinol, nabilona, prometazina, clorfeniramina.
  - Antieméticos e outros: aprepitanto, metoclopramida, sibutramina.
  - Antimaláricos: cloroquina, mefloquina, hidroxicloroquina.
  - Outros: cobicistate, ácido fólico, levofolinato, folinato (leucovorina), deferasirox, fostamatinibe.

As advertências e contraindicações da bula brasileira não foram obtidas nos dados compilados; consulte a bula para confirmá-las.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão tem apenas a pontuação do modelo como suporte (nível L5), sem ensaios clínicos nem literatura, e não há ligação mecanística plausível entre a etosuximida e a fisiopatologia da NSIAD. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação documentado (por exemplo, via DrugBank) e avaliar uma possível ligação com a via do receptor V2/AVPR2.
- Fazer busca sistemática de literatura e de ensaios clínicos sobre etosuximida em NSIAD ou hiponatremia relacionada.
- Obter e analisar a bula da ANVISA (advertências e contraindicações) para a triagem de segurança.
- Realizar validação pré-clínica independente do mecanismo, caso se deseje seguir adiante.
- Avaliar a viabilidade regulatória e comercial, dado que o registro no Brasil está cancelado.
- Considerar o perfil de segurança (sinais hematológicos, hepáticos e renais) antes de qualquer uso em população com NSIAD.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

