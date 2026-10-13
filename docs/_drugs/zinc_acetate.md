---
layout: default
title: Zinc Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Zinc Acetate
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

# Acetato de zinco: De soluções que ajustam o balanço eletrolítico para retinopatia diabética não proliferativa grave

## Resumo em Uma Frase

O acetato de zinco foi originalmente registrado no Brasil como solução que ajusta o balanço eletrolítico.
O modelo TxGNN prevê que pode ser eficaz para **retinopatia diabética não proliferativa grave (severe nonproliferative diabetic retinopathy)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Soluções que ajustam o balanço eletrolítico |
| Nova Indicação Prevista | Retinopatia diabética não proliferativa grave (severe nonproliferative diabetic retinopathy) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o acetato de zinco é um sal de zinco usado para reposição do mineral e ajuste eletrolítico. Sua eficácia como fonte de zinco é conhecida, e mecanisticamente poderia ser aplicável à nova indicação, mas isso é hipotético.

O zinco atua como cofator antioxidante (por exemplo, da superóxido dismutase) e poderia, em tese, modular o estresse oxidativo na retina diabética. Não há, porém, nenhum ensaio ou publicação nos dados compilados para este relatório que sustente essa hipótese. A pontuação elevada do TxGNN é apenas uma previsão computacional.

A relação entre a indicação original (reposição eletrolítica) e a nova (doença microvascular da retina) é indireta. Previsões vizinhas, como retinopatia diabética (99,92%), compartilham a mesma lógica e a mesma ausência de evidências.

## Outras Indicações Previstas

| Posição | Indicação | Pontuação TxGNN | Evidências | Nível |
|------|------|------|------|------|
| 2 | Bronquite | 99,97% | 1 publicação (estudo in vitro/materiais, indireto) | L5 |
| 3 | Retinopatia diabética | 99,92% | Nenhuma | L5 |
| 4 | Acrodermatite crônica atrófica | 99,83% | Nenhuma | L5 |
| 5 | Dermatomiosite neonatal | 99,81% | Nenhuma | L5 |
| 6 | Acne queloidiana | 99,80% | Nenhuma | L5 |
| 7 | Hidroa vaciniforme familiar | 99,79% | Nenhuma | L5 |
| 8 | Doença pulmonar intersticial infantil associada a doença do tecido conjuntivo | 99,78% | Nenhuma | L5 |
| 9 | Dermatomiosite amiopática | 99,77% | Nenhuma | L5 |
| 10 | Infecção do trato urinário | 99,57% | 1 publicação (indireta, 1999) | L4 |

A previsão de acrodermatite crônica atrófica (doença cutânea da borreliose de Lyme, tratada com antibióticos) pode refletir confusão com a acrodermatite enteropática, que é responsiva ao zinco, mas é outra doença.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (retinopatia diabética não proliferativa grave), atualmente não há literatura relacionada. Para as demais indicações previstas, há apenas duas publicações, ambas indiretas:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10398312](https://pubmed.ncbi.nlm.nih.gov/10398312/) | 1999 | Provável estudo clínico de suplementação (desenho não confirmado) | American Journal of Hematology | Suplementação de zinco e incidência de infecções e internações em doença falciforme; população e desfecho indiretos para infecção urinária |
| [32679246](https://pubmed.ncbi.nlm.nih.gov/32679246/) | 2020 | In vitro / ciência de materiais | Microbial Pathogenesis | Comparação da síntese de nanopartículas de óxido de zinco (método biogênico vs. químico) contra *Staphylococcus aureus*; não é estudo clínico do acetato de zinco em bronquite |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 164000011 (cancelado) | ACETATO DE ZINCO 0,5 MEQ/ML | Não informada | Soluções que ajustam o balanço eletrolítico |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não bula)**: o grafo de conhecimento do TxGNN associa o fármaco a contraindicações em porfiria, porfiria hereditária e doenças do metabolismo das porfirinas. Isso deve ser confirmado na bula.
- **Interações Medicamentosas**: foram identificadas 100 interações; entre as listadas, a maioria é de gravidade leve (por exemplo, abatacepte, adalimumabe, hidrocortisona, dexametasona, betametasona, triancinolona, azatioprina, baricitinibe). As de gravidade **moderada** incluem:
  - Ácido alendrônico, ácido risedrônico e ibandronato (bisfosfonatos)
  - Tetraciclina
  - Baloxavir marboxil

  Essas interações moderadas provavelmente se devem à quelação do zinco, que reduz a absorção; recomenda-se espaçar as administrações.

As advertências principais e as contraindicações de bula não estavam disponíveis; consulte a bula para essas informações.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é puramente computacional (L5), sem ensaios clínicos nem literatura para a indicação principal. O único registro brasileiro está cancelado, e faltam dados de segurança de bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que impede a triagem de segurança
- Obter dados do mecanismo de ação no DrugBank
- Fazer revisão sistemática da literatura sobre zinco e retinopatia diabética
- Definir via de administração e formulação compatíveis com uso oftalmológico/sistêmico, já que o único registro é de solução eletrolítica
- Avaliar a contraindicação sugerida em porfiria e as interações com bisfosfonatos e tetraciclina
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

