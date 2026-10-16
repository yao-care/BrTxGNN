---
layout: default
title: Elafibranor
parent: Apenas Predição do Modelo (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Elafibranor: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L5). Indicação original: Não há indicação registrada na ANVISA (internacionalmente: colangite…"
monitor_inn: "Elafibranor"
predicted_indications: ["amenorrhea (disease)", "non-syndromic esophageal malformation", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma", "rectal cloacogenic carcinoma", "gallbladder adenosquamous carcinoma", "deafness, autosomal dominant 39, with dentinogenesis imperfecta 1", "acantholytic variant squamous cell breast carcinoma", "adenosquamous breast carcinoma"]
---

# Elafibranor
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

# Elafibranor: Da indicação original não registrada no Brasil à amenorreia

## Resumo em Uma Frase

Elafibranor é um agonista duplo dos receptores PPARα e PPARδ, desenvolvido inicialmente para esteato-hepatite não alcoólica (NASH) e posteriormente aprovado para colangite biliar primária (FDA em junho de 2024; EMA em setembro de 2024). Não há indicação aprovada registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **amenorreia (amenorrhea)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não há indicação registrada na ANVISA (internacionalmente: colangite biliar primária) |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 99,86% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no conjunto de dados compilado. Segundo os dados farmacológicos disponíveis, o elafibranor é um agonista dos receptores PPARα (gene *PPARA*) e PPARβ/δ (gene *PPARD*). É convertido no fígado em seu principal metabólito ativo, o GFT-1007. Em estudos pré-clínicos, reduziu o acúmulo de gordura hepática, a inflamação e a fibrose.

A sinalização PPAR tem papel teórico na regulação metabólica e endócrina. No entanto, não há ligação direta estabelecida entre o fármaco e o eixo hipotálamo-hipófise-ovário, que é central na amenorreia. A pontuação elevada do TxGNN (0,9986) reflete uma inferência computacional baseada no grafo de conhecimento, sem respaldo de ensaios clínicos ou literatura.

Portanto, a previsão deve ser tratada como uma hipótese a explorar, e não como evidência de eficácia. A relação com a indicação original (doenças hepáticas colestáticas e metabólicas) ainda não foi analisada.

## Considerações sobre Outras Previsões do Modelo

Além da amenorreia, o modelo listou outras previsões de alta pontuação, todas de nível L5, sem ensaios clínicos nem literatura, e todas com recomendação Hold:

| Posição | Doença prevista | Pontuação TxGNN | Observação sobre plausibilidade |
|------|------|------|------|
| 2 | Malformação esofágica não sindrômica | 98,92% | Sem ligação mecanística plausível; defeito de desenvolvimento embrionário |
| 3 | Doença de Paget óssea | 98,86% | Possível papel dos PPAR no remodelamento ósseo, mas já existem terapias eficazes (bisfosfonatos) |
| 4 | Dentinogênese imperfeita | 98,52% | Doença genética (DSPP); sem base biológica evidente |
| 5 | Carcinoma de células escamosas | 98,47% | PPARδ pode ter papel pró-tumoral; efeito potencialmente prejudicial |
| 6 | Carcinoma cloacogênico retal | 98,46% | Previsão provavelmente por associação no grafo; incerteza ou risco pró-tumoral |
| 7 | Carcinoma adenoescamoso da vesícula biliar | 98,45% | Apenas associação anatômica hepatobiliar tangencial |
| 8 | Surdez autossômica dominante 39 com dentinogênese imperfeita 1 | 98,44% | Doença monogênica; pontuação reflete similaridade no grafo |
| 9 | Carcinoma mamário escamoso variante acantolítica | 98,44% | Sem evidência específica; papel do PPARδ no câncer é dependente do contexto |
| 10 | Carcinoma mamário adenoescamoso | 98,44% | Mesma inferência do grafo que a variante acantolítica |

## Informações de Comercialização no Brasil

O elafibranor não possui registros ativos ou cancelados na ANVISA nos dados compilados (0 registros). Portanto, não está comercializado no Brasil.

## Considerações de Segurança

- **Interações medicamentosas**: a consulta foi concluída, mas retornou apenas dois registros de farmacologia (alvos PPARα e PPARβ/δ), sem interações medicamentosas clínicas classificadas por nível de gravidade. Nos estudos de fase 1/2, não foram detectados sinais de segurança específicos.

Para advertências e contraindicações, consulte a bula do produto.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para amenorreia baseia-se apenas na pontuação do modelo (nível L5), sem ensaios clínicos, literatura ou ligação mecanística estabelecida. Além disso, o fármaco não tem registro no Brasil e faltam dados regulatórios de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações) para a triagem de segurança
- Complementar os dados de mecanismo de ação a partir do DrugBank
- Investigar a plausibilidade biológica da ligação entre PPARα/δ e o eixo hipotálamo-hipófise-ovário, com revisão sistemática da literatura
- Avaliar a similaridade com a indicação original e a compatibilidade de vias de administração
- Considerar estudos pré-clínicos antes de qualquer ensaio clínico
- Verificar a situação regulatória do elafibranor no Brasil (pedido de registro ou aprovação futura)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

