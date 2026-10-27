---
layout: default
title: Metaraminol
parent: Apenas Predição do Modelo (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metaraminol: nova indicação prevista, Síndrome da Taquicardia Postural Ortostática (Postural Orthostatic Ta… (nível de evidência L5). Indicação original: Distúrbio hipotensivo (hipotensão)"
monitor_inn: "Metaraminol"
predicted_indications: ["postural orthostatic tachycardia syndrome", "urticaria (disease)", "variably protease-sensitive prionopathy", "mitral valve prolapse (disease)", "common cold", "MVP1", "irritable bowel syndrome", "familial mitral valve prolapse", "multiple system atrophy", "angioedema"]
---

# Metaraminol
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

## Metaraminol: Da hipotensão à síndrome da taquicardia postural ortostática
{: .text-alpha }

## Resumo em Uma Frase

Metaraminol é um simpaticomimético de ação direta e indireta, originalmente usado no tratamento de distúrbios hipotensivos (hipotensão).
O modelo TxGNN prevê que pode ser eficaz para **Síndrome da Taquicardia Postural Ortostática (Postural Orthostatic Tachycardia Syndrome, POTS)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção: trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Distúrbio hipotensivo (hipotensão) |
| Nova Indicação Prevista | Síndrome da Taquicardia Postural Ortostática (Postural Orthostatic Tachycardia Syndrome) |
| Pontuação de Previsão TxGNN | 98,03% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o metaraminol é um simpaticomimético de ação direta e indireta, com atividade predominantemente agonista alfa-1 adrenérgica, que produz vasoconstrição e elevação da pressão arterial. Sua eficácia em hipotensão é conhecida, e mecanisticamente pode ser aplicável a quadros de intolerância ortostática.

Na POTS, o retorno venoso comprometido e a vasoconstrição periférica insuficiente contribuem para a intolerância ortostática. Um agente vasoconstritor poderia, em teoria, atuar sobre esse componente, o que explica a pontuação elevada do modelo.

Há, porém, um contraponto importante: muitos pacientes com POTS apresentam estado hiperadrenérgico, e um pressor que aumente a frequência cardíaca ou a pressão arterial poderia piorar os sintomas. A previsão é puramente computacional, sem apoio de ensaios ou literatura.

### Outras indicações previstas

Além da POTS, o modelo gerou outras previsões, todas com nível de evidência L5 e sem ensaios ou publicações:

| Posição | Indicação prevista | Pontuação TxGNN | Avaliação |
|------|------|------|------|
| 2 | Urticária | 95,33% | Sem fundamento mecanístico claro; urticária é mediada por mastócitos/histamina |
| 3 | Prionopatia variavelmente sensível à protease | 94,69% | Sem conexão mecanística identificável; provável artefato da rede |
| 4 | Prolapso da valva mitral | 93,94% | Distúrbio estrutural; o pressor não trata a causa e pode provocar arritmias |
| 5 | Resfriado comum | 93,86% | Racional farmacológico frouxo (descongestionante); alternativas mais bem caracterizadas |
| 6 | MVP1 (prolapso mitral genético) | 93,56% | Essencialmente duplicata do prolapso mitral; sem base mecanística |
| 7 | Síndrome do intestino irritável | 93,25% | Sem vínculo estabelecido; efeitos pressores sistêmicos seriam indesejáveis |
| 8 | Prolapso familiar da valva mitral | 93,18% | Outra entrada de prolapso mitral hereditário; sem apoio clínico |
| 9 | Atrofia de múltiplos sistemas | 92,97% | Racional sintomático plausível para hipotensão ortostática neurogênica; risco de hipertensão supina |
| 10 | Angioedema | 92,88% | Racional distante por classe; formas mediadas por bradicinina não respondem |

Entre elas, a atrofia de múltiplos sistemas (hipotensão ortostática neurogênica) é a mais coerente com a indicação original, embora seja um benefício apenas sintomático.

## Informações de Comercialização no Brasil

O metaraminol não possui registros ativos nem comercialização no Brasil segundo os dados compilados para este relatório (0 registros).

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 65 interações no total; entre as listadas, todas de gravidade **moderada**. Os principais grupos são:
  - **Antidiabéticos**: acarbose, metformina, clorpropamida, pioglitazona, insulinas (asparte, degludeca, detemir, glargina), inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), inibidores de DPP-4 (alogliptina, linagliptina, saxagliptina) e agonistas de GLP-1 (albiglutida, dulaglutida, liraglutida, semaglutida). Vasopressores simpaticomiméticos podem alterar o controle glicêmico.
  - **Anorexígenos/simpaticomiméticos**: dietilpropiona e fentermina, com possível efeito aditivo sobre a pressão arterial e a frequência cardíaca.
- **Riscos teóricos nas novas indicações**: hipertensão supina (em atrofia de múltiplos sistemas), piora do estado hiperadrenérgico (em POTS) e arritmias (em prolapso mitral).

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para POTS tem pontuação alta (98,03%), mas é exclusivamente computacional (L5), sem ensaios clínicos nem literatura. O fármaco não é comercializado no Brasil, e o risco de agravar um estado hiperadrenérgico exige cautela. Os dados de mecanismo de ação e de bula também estão ausentes.

**Para prosseguir, é necessário:**
- Obter dados detalhados do mecanismo de ação (MOA), por exemplo, via DrugBank
- Obter e analisar a bula (advertências e contraindicações) no site da ANVISA, etapa bloqueante para a triagem de segurança
- Realizar revisão sistemática da literatura sobre vasopressores alfa-1 em POTS e em hipotensão ortostática neurogênica (atrofia de múltiplos sistemas)
- Avaliar a viabilidade regulatória e de via de administração, dado que não há registro no Brasil
- Se houver interesse, priorizar a atrofia de múltiplos sistemas como hipótese complementar, por sua maior coerência com a indicação original
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

