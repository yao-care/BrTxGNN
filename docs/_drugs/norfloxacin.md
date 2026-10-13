---
layout: default
title: Norfloxacin
parent: Apenas Predição do Modelo (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacino: De infecções bacterianas à hiperamilasemia

## Resumo em Uma Frase

Norfloxacino é um antibacteriano da classe das fluoroquinolonas, originalmente usado no tratamento de infecções como infecção do trato urinário, febre tifoide, disenteria e pneumonia bacteriana.
O modelo TxGNN prevê que pode ser eficaz para **Hiperamilasemia (Hyperamylasemia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (febre tifoide, salmonelose, infecção do trato urinário, bronquite, pneumonia bacteriana, disenteria, entre outras) |
| Nova Indicação Prevista | Hiperamilasemia (Hyperamylasemia) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o norfloxacino é uma fluoroquinolona que inibe a DNA girase e a topoisomerase IV bacterianas, e sua eficácia em infecções bacterianas, sobretudo urinárias e gastrointestinais, é conhecida.

A hiperamilasemia, porém, é um achado laboratorial (elevação da amilase sérica) e não uma doença infecciosa. Não se identifica um vínculo mecanístico plausível entre um inibidor antibacteriano da DNA girase e essa condição. A pontuação alta (99,70%) reflete uma previsão baseada em grafo de conhecimento, sem respaldo de ensaios ou literatura.

Portanto, a previsão deve ser tratada como hipótese computacional, não como indicação com racionalidade farmacológica estabelecida.

## Outras Indicações Previstas (Contexto)

Outras indicações previstas também têm evidência fraca. A única com algum grau de plausibilidade é a peste septicêmica.

| Doença prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade policlonal) | 99,70% | L5 | Sem mecanismo plausível |
| Analbuminemia congênita | 99,67% | L5 | Sem mecanismo plausível |
| Incompatibilidade de grupo sanguíneo | 99,55% | L5 | Sem relevância conhecida |
| Ceratoconjuntivite epitelial puntacta | 99,54% | L4 | Apenas casos de ceratoconjuntivite microsporidiana, sem evidência de que o norfloxacino tenha sido o agente estudado |
| Doença hematológica pré-maligna | 99,48% | L5 | Sem mecanismo ou evidência |
| Esclerodermia difusa | 99,44% | L5 | Sem mecanismo imunomodulador conhecido |
| Gamopatia monoclonal | 99,42% | L5 | O único artigo trata de resistência bacteriana, não de tratamento |
| Doença hematológica associada a neuropatia periférica adquirida | 99,38% | L5 | Fluoroquinolonas causam neuropatia periférica, o que desaconselha o uso |
| Peste septicêmica | 99,37% | L4 | Racional antibacteriano plausível (Yersinia pestis); evidência pré-clínica indireta |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a hiperamilasemia.

## Considerações de Segurança

- **Contraindicações e condições de risco (grafo de conhecimento, não texto de bula)**: síndrome do QT longo (inclusive familiar) e torsades de pointes; insuficiência e doenças hepáticas, cirrose; doença renal; epilepsia; transtornos psiquiátricos (ansiedade, psicose, esquizofrenia e transtornos afins); tendinite e outras afecções de tendões e articulações; neuropatia periférica; rabdomiólise; diabetes mellitus e cetoacidose diabética; deficiência de potássio; trombocitopenia; anemia.
- **Interações medicamentosas** (100 interações registradas; exemplos):
  - **Gravidade maior**: hidrocortisona, dexametasona, betametasona, triamcinolona (corticosteroides, com risco aumentado de lesão de tendão), bupropiona e clorpropamida.
  - **Gravidade moderada**: antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodil e sais de cálcio e potássio.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hiperamilasemia tem apenas respaldo do modelo (L5), sem ensaios, sem literatura e sem vínculo mecanístico plausível. Além disso, o norfloxacino não é comercializado no Brasil e tem um perfil de segurança com muitas condições de risco.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) obtidos do DrugBank.
- Bula da ANVISA com advertências e contraindicações, hoje ausente.
- Justificativa biológica para a associação com hiperamilasemia, seguida de estudos pré-clínicos, caso haja interesse.
- Se o objetivo for priorizar candidatos, avaliar a peste septicêmica (única previsão com racional antibacteriano), comparando o norfloxacino com fluoroquinolonas de dados mais sólidos, como ciprofloxacino, levofloxacino e moxifloxacino.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

