---
layout: default
title: Sodium Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sodium Acetate: nova indicação prevista, Deficiência congênita de protrombina (congenital prothrombin deficien… (nível de evidência L5). Indicação original: Produtos para hemodiálise"
monitor_inn: "Sodium acetate"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "Ureaplasma urethritis", "gonococcal urethritis", "dyspepsia", "uterine inflammatory disease", "gastroparesis (disease)", "xanthogranulomatous pyelonephritis"]
---

# Sodium Acetate
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

# Acetato de Sódio: De produtos para hemodiálise e reposição hidroeletrolítica para deficiência congênita de protrombina

## Resumo em Uma Frase

Acetato de sódio é uma fonte de eletrólitos e agente alcalinizante sistêmico (o acetato é metabolizado em bicarbonato), originalmente usado em produtos para hemodiálise, reposição hidroeletrolítica e tratamento da acidose metabólica.
O modelo TxGNN prevê que pode ser eficaz para **deficiência congênita de protrombina (congenital prothrombin deficiency)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Produtos para hemodiálise |
| Nova Indicação Prevista | Deficiência congênita de protrombina (congenital prothrombin deficiency) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o acetato de sódio atua como fonte de eletrólitos e agente alcalinizante: o acetato é metabolizado no organismo em bicarbonato, o que explica seu uso em soluções de hemodiálise, em soluções de reposição hidroeletrolítica (como o Ringer com lactato) e no tratamento da acidose metabólica.

A deficiência congênita de protrombina, por sua vez, é uma deficiência do fator de coagulação II e exige reposição do fator. Não há vínculo mecanístico plausível com as propriedades eletrolíticas ou alcalinizantes do acetato de sódio. A pontuação alta (99,98%) reflete uma previsão baseada em grafo de conhecimento, sem respaldo clínico ou da literatura.

Para contexto, as demais indicações previstas também carecem de respaldo: epiglotite, infecção do trato urinário, colangite esclerosante, uretrites por *Ureaplasma* e gonocócica, dispepsia, doença inflamatória uterina, gastroparesia e pielonefrite xantogranulomatosa. Nenhuma tem ensaio clínico. Para dispepsia e gastroparesia, a literatura recuperada trata do acetato de sódio marcado com ¹³C apenas como traçador diagnóstico em testes respiratórios de esvaziamento gástrico, e não como tratamento. Os escores idênticos das uretrites por *Ureaplasma* e gonocócica sugerem um artefato do grafo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação prevista principal (deficiência congênita de protrombina).

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados; não há registro válido no momento. Principais registros (5 de 20):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 132230114 | CIFOBAN | Não informada | Produtos para hemodiálise |
| Registro nº 164000004 | Acetato de Sódio | Não informada | Eletrólitos simples |
| Registro nº 100431323 | TRICIT | Não informada | Produtos para hemodiálise |
| Registro nº 106830184 | REGIOCIT | Não informada | Produtos para hemodiálise |
| Registro nº 100431052 | Solução Fisiológica de Ringer com Lactato | Não informada | Reidratantes parenterais |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: o grafo associa o fármaco a contraindicações em doenças renais (doença renal, insuficiência renal crônica e terminal, anúria, nefrolitíase, nefrocalcinose, nefropatia aguda por urato), cardiovasculares (doença cardíaca, bloqueio atrioventricular, fibrilação ventricular, intoxicação digitálica), distúrbios do cálcio e do fósforo (hipercalcemia, hipercalcemia humoral da malignidade, sarcoidose, doença do metabolismo do fósforo), paralisia periódica hipercalêmica, hipoaldosteronismo, miotonia congênita e fenilcetonúria. Esses itens exigem confirmação na bula.
- **Interações Medicamentosas**: foram identificadas 30 interações, das quais 20 foram detalhadas.
  - Moderadas: doxiciclina, tetraciclina, minociclina, ácido acetilsalicílico, salicilato de colina, efedrina (inclusive nasal), pseudoefedrina, anfetamina, dextroanfetamina, benzfetamina e metenamina.
  - Leves: sulfonilureias (clorpropamida, tolazamida, glipizida, glibenclamida, acetoexamida, tolbutamida), memantina e metotrexato.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é puramente baseada em grafo (nível L5), sem ensaios clínicos nem literatura, e sem vínculo mecanístico plausível com a deficiência de protrombina. Além disso, todos os registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) a partir de fontes como o DrugBank
- Advertências e contraindicações da bula na ANVISA, para a triagem de segurança
- Justificativa biológica para a hipótese de coagulação, com estudos pré-clínicos
- Reavaliar candidatas com mais respaldo ou vínculo mecanístico mais plausível (por exemplo, infecção do trato urinário, ainda que apenas especulativa, via alcalinização urinária)
- Esclarecer a situação regulatória, já que não há registro válido no país
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

