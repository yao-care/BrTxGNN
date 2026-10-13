---
layout: default
title: Rutin
parent: Apenas Predição do Modelo (L5)
nav_order: 575
evidence_level: L5
indication_count: 8
---

# Rutin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

# Rutina: Da indicação antivaricosa à doença fibrocística da mama

## Resumo em Uma Frase

A rutina (rutin) foi registrada no Brasil em produtos como a "Castanha da Índia Composta", usada como antivaricoso de ação sistêmica, e em um polivitamínico com minerais.
O modelo TxGNN prevê que ela possa ser eficaz para **doença fibrocística da mama (breast fibrocystic disease)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antivaricosos de ação sistêmica |
| Nova Indicação Prevista | Doença fibrocística da mama (breast fibrocystic disease) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a rutina é um flavonoide com propriedades antioxidantes, anti-inflamatórias e venoativas. Sua eficácia como antivaricoso foi a base de seu uso, e mecanisticamente poderia ser aplicável a condições benignas da mama, embora esse vínculo seja plausível, mas não comprovado pelos dados compilados.

A relação entre a indicação original (insuficiência venosa) e a nova (alteração benigna do tecido mamário) é distante. Não há similaridade formal verificada entre as duas, e nenhuma ponte mecanística pôde ser confirmada.

Vale notar que as quatro primeiras previsões (doença fibrocística, adenose apócrina, adenose de ductos obtusos e displasia mamária benigna) pertencem à mesma família de condições mamárias benignas. Pontuações idênticas ou sinônimas indicam um sinal derivado do mesmo grafo de conhecimento, e não evidências independentes.

## Outras Previsões do Modelo

| Posição | Doença prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Adenose apócrina da mama | 99,64% | Sem evidências; sinal compartilhado com outras condições mamárias benignas |
| 3 | Adenose de ductos obtusos da mama | 99,64% | Pontuação idêntica à anterior |
| 4 | Displasia mamária benigna | 99,42% | Sinônimo da doença fibrocística; não independente |
| 5 | Candidíase vulvovaginal | 99,22% | Atividade antifúngica de flavonoides in vitro; vínculo especulativo |
| 6 | Abscesso mamário | 99,11% | Condição infecciosa tratada com antibióticos e drenagem; justificativa fraca |
| 7 | Necrose gordurosa da mama | 99,11% | Racional anti-inflamatório hipotético |
| 8 | Vaginite | 99,09% | Duas publicações recuperadas, mas fora do tema (ver abaixo) |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (doença fibrocística da mama), atualmente não há literatura relacionada.

Para a oitava previsão (vaginite), foram recuperadas duas publicações, mas nenhuma trata de rutina ou de vaginite:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38024692](https://pubmed.ncbi.nlm.nih.gov/38024692/) | 2023 | Pré-clínico (modelo animal, extrato vegetal) | ACS Omega | Extrato etanólico de *Saraca asoca* avaliado em ratas com síndrome do ovário policístico induzida por letrozol |
| [37063342](https://pubmed.ncbi.nlm.nih.gov/37063342/) | 2023 | Pré-clínico (modelo animal, extrato vegetal) | Dose-Response | Extrato aquoso de *Garcinia cambogia* em ratas com síndrome do ovário policístico induzida por letrozol |

Esses estudos estão fora do tema e não oferecem apoio direto nem indireto relevante, de modo que o nível de evidência permanece L5.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 111990004 (cancelado) | Castanha da Índia Composta | Não informada | Antivaricosos de ação sistêmica |
| Registro 102350339 (cancelado) | Gerovital | Não informada | Polivitamínicos com minerais |

## Considerações de Segurança

Não há dados de bula disponíveis sobre advertências e contraindicações; consulte a bula para informações de segurança.

- **Contraindicações no grafo de conhecimento** (relações fármaco-doença do grafo de conhecimento do modelo, não texto de bula): anemia falciforme, persistência hereditária da hemoglobina fetal, hiperoxalúria primária, hemocromatose hereditária, hemossiderose, doenças do metabolismo do ferro e doença de Wilson.
- **Interações medicamentosas**: nenhuma interação foi encontrada nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia apenas na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura sobre a rutina para essas indicações. Além disso, os dois registros brasileiros estão cancelados e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar o mecanismo de ação a partir do DrugBank para avaliar a ponte mecanística
- Realizar busca dirigida de literatura e ensaios sobre rutina em doença fibrocística da mama e condições mamárias benignas
- Avaliar as contraindicações do grafo de conhecimento (distúrbios do metabolismo do ferro e anemia falciforme) quanto à relevância clínica
- Verificar a viabilidade regulatória e de via de administração, já que não há registro vigente no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

