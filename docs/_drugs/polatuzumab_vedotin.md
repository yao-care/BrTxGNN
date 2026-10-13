---
layout: default
title: Polatuzumab Vedotin
parent: Apenas Predição do Modelo (L5)
nav_order: 532
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

# Polatuzumabe vedotina: De antineoplásico (B-cell) para carcinoma de mama HER2-positivo

## Resumo em Uma Frase

Polatuzumabe vedotina é um conjugado anticorpo-fármaco (ADC) registrado na ANVISA com a indicação genérica "antineoplásico".
O modelo TxGNN prevê que pode ser eficaz para **carcinoma de mama HER2-positivo (HER2 positive breast carcinoma)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Carcinoma de mama HER2-positivo (HER2 positive breast carcinoma) |
| Pontuação de Previsão TxGNN | 99,34% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o polatuzumabe vedotina é um ADC que tem como alvo o CD79b e entrega o agente desestabilizador de microtúbulos monometil auristatina E (MMAE). Seu uso aprovado é em neoplasias de células B, nas quais o CD79b é expresso.

A pontuação do TxGNN (0,993) é uma previsão baseada em grafo de conhecimento. Os dados compilados não sustentam um vínculo mecanístico direto com o carcinoma de mama HER2-positivo: o CD79b não é um alvo reconhecido em câncer de mama. O sinal do modelo pode refletir a semelhança de carga citotóxica (MMAE, compartilhada com outros ADCs, como brentuximabe vedotina e enfortumabe vedotina) ou de classe do fármaco, e não a biologia do alvo.

Além disso, o câncer de mama HER2-positivo já conta com ADCs estabelecidos que atuam por entrega dirigida ao HER2 (trastuzumabe entansina e trastuzumabe deruxtecana). Qualquer justificativa para o polatuzumabe vedotina nesse contexto seria especulativa e exigiria validação pré-clínica, como o perfil de expressão de CD79b em tumores de mama.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101000674 (cancelado) | ROPOLIVY | Não informada | ANTINEOPLASICO |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Conjugado anticorpo-fármaco (ADC) com carga citotóxica antimicrotúbulos (MMAE) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula; seguir os regulamentos de manuseio de citotóxicos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 131 interações potenciais. Entre as listadas, as de gravidade **maior** incluem:
  - Claritromicina
  - Cobicistate
  - Deferiprona
  - Samário (153Sm) lexidronam

  Há também interações de gravidade **moderada**, entre elas aprepitanto, cimetidina, naltrexona, metronidazol, miconazol, rosuvastatina, sinvastatina, tinidazol, clotrimazol, estrôncio-89, ticagrelor, cloroquina, dissulfiram, secnidazol, hidroxicloroquina e benznidazol.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é sustentada apenas pelo modelo (L5), sem ensaios clínicos nem literatura, e não há vínculo mecanístico plausível entre o alvo CD79b e o câncer de mama HER2-positivo. Além disso, o único registro no Brasil está cancelado e há alternativas já estabelecidas dirigidas ao HER2.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA, para advertências e contraindicações (lacuna que bloqueia a triagem de segurança)
- Obter dados do mecanismo de ação no DrugBank
- Avaliar a expressão de CD79b em tumores de mama (validação pré-clínica)
- Comparar com os ADCs HER2-dirigidos já aprovados, para justificar o valor adicional
- Esclarecer a situação regulatória no Brasil, dado o registro cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

