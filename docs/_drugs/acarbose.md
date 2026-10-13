---
layout: default
title: Acarbose
parent: Apenas Predição do Modelo (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

# Acarbose: Do diabetes mellitus tipo 2 à síndrome do membro rígido focal

## Resumo em Uma Frase

Acarbose é um inibidor da alfa-glicosidase intestinal, originalmente usado no tratamento do diabetes mellitus tipo 2.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome do Membro Rígido Focal (Focal Stiff Limb Syndrome)**, mas, até o momento, **não há ensaios clínicos nem publicações** que apoiem esta direção; trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diabetes mellitus tipo 2 |
| Nova Indicação Prevista | Síndrome do membro rígido focal (Focal Stiff Limb Syndrome) |
| Pontuação de Previsão TxGNN | 99,65% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a acarbose é um inibidor da alfa-glicosidase que atua localmente no intestino, retardando a digestão de carboidratos e reduzindo a glicemia pós-prandial. Sua eficácia no diabetes tipo 2 é conhecida.

A síndrome do membro rígido focal é uma condição neurológica rara, relacionada ao espectro da síndrome da pessoa rígida (frequentemente com mecanismo autoimune e envolvimento do sistema GABAérgico). Não há uma conexão mecanística plausível com a inibição da alfa-glicosidase intestinal.

A pontuação alta (99,65%) reflete provavelmente apenas proximidades no grafo de conhecimento, como o contexto autoimune compartilhado (anticorpos anti-GAD ligados tanto ao diabetes quanto às síndromes de rigidez). Isso não constitui justificativa terapêutica. A previsão deve ser tratada como hipótese, não como achado.

**Outras previsões do modelo** (todas com nível L5 e decisão Hold):

| Posição | Doença prevista | Pontuação TxGNN |
|------|------|------|
| 2 | Síndrome da pessoa rígida clássica | 99,65% |
| 3 | Síndrome de disfunção responsiva à tiamina | 99,62% |
| 4 | Opsismodisplasia | 99,62% |
| 5 | Lipodistrofia localizada induzida por fármacos | 99,24% |
| 6 | Lipodistrofia centrífuga | 99,22% |
| 7 | Lipoatrofia localizada induzida por pressão | 99,20% |
| 8 | Lipodistrofia localizada idiopática | 99,17% |
| 9 | Agenesia pancreática | 99,16% |

Entre elas, apenas a agenesia pancreática tem literatura associada, mas esta é indireta (diabetes em geral) e não sustenta a indicação, pois essa condição exige reposição de insulina.

## Informações de Comercialização no Brasil

Segundo os dados compilados, a acarbose não possui registros ativos no Brasil (0 registros).

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (derivadas do TxGNN, não do texto de bula): doença renal, piureter, doença hepática, doença da vesícula biliar, cirrose hepática, doença inflamatória intestinal, hipoglicemia e lesão.
- **Interações Medicamentosas**: foram identificadas 100 interações; as 20 listadas incluem:
  - *Moderadas*: acetazolamida, salbutamol, babosa (folha de Aloe vera), alpelisibe, amprenavir, aripiprazol, asenapina, asparaginase (Erwinia chrysanthemi e E. coli), atazanavir, bedaquilina, bendroflumetiazida, benzfetamina, benztiazida, betametasona.
  - *Leves*: albiglutida, alclometasona (tópica), ácido lipoico, amcinonida, anisindiona.

Consulte a bula para advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a indicação principal prevista, e não há mecanismo plausível que a sustente. A previsão baseia-se apenas no modelo (L5). Além disso, o fármaco não tem registro comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (por exemplo, via DrugBank) e avaliar se há alguma ligação biológica real com a síndrome do membro rígido.
- Realizar revisão sistemática da literatura e de bases de ensaios para a síndrome do membro rígido e a síndrome da pessoa rígida.
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa necessária para a triagem de segurança.
- Esclarecer a situação regulatória no Brasil, já que não há registros.
- Considerar estudos pré-clínicos de mecanismo antes de qualquer investimento clínico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

