---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Bisoprolol: Da hipertensão à doença renal hipertensiva maligna

## Resumo em Uma Frase

Bisoprolol é um betabloqueador β1-seletivo amplamente utilizado no tratamento da hipertensão arterial e insuficiência cardíaca. O modelo TxGNN prevê que pode ser eficaz para **Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease)**, com uma pontuação de previsão de 99,94%. Atualmente, não há ensaios clínicos nem publicações específicas para esta indicação, porém a forte base mecanística — sendo o bisoprolol já um anti-hipertensivo de primeira linha — sustenta a razoabilidade desta previsão como extensão natural da indicação existente.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Hipertensão arterial / Insuficiência cardíaca |
| Nova Indicação Prevista | Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Bisoprolol é um bloqueador seletivo dos receptores β1-adrenérgicos. Ao bloquear esses receptores no coração e nos rins, o fármaco reduz o débito cardíaco e suprime a liberação de renina, diminuindo a atividade do sistema renina-angiotensina-aldosterona (SRAA). Esses dois mecanismos convergem para um controle eficaz da pressão arterial, razão pela qual o bisoprolol já é amplamente prescrito como anti-hipertensivo de primeira linha.

A doença renal hipertensiva maligna representa o dano aos órgãos-alvo causado por hipertensão arterial grave e descontrolada, com lesão das arteríolas renais, necrose fibrinoide e insuficiência renal progressiva. Do ponto de vista fisiopatológico, o controle agressivo da pressão arterial é o pilar do tratamento para preservar a função renal. O bisoprolol, ao reduzir a pressão arterial e atenuar a ativação do SRAA, pode contribuir para desacelerar a progressão da nefroesclerose hipertensiva maligna.

É importante notar que esta previsão representa mais uma **extensão natural da indicação existente** do que um reposicionamento de fármaco no sentido estrito. Ainda assim, a validação formal para esta condição específica permanece necessária, especialmente quanto ao manejo da emergência hipertensiva em contexto de lesão renal aguda, onde vasodilatadores intravenosos costumam ser preferidos na fase inicial.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a combinação bisoprolol + doença renal hipertensiva maligna no ClinicalTrials.gov nem no ICTRP.

---

## Evidências da Literatura

Atualmente não há literatura específica relacionando bisoprolol ao tratamento da doença renal hipertensiva maligna indexada no PubMed.

---

## Informações de Comercialização no Brasil

O bisoprolol possui **20 registros** ativos no Brasil com status de comercialização confirmado. Os detalhes específicos dos registros (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estavam disponíveis no Evidence Pack para listagem individual.

---

## Considerações de Segurança

Consulte a bula para informações completas de segurança. Os dados de advertências principais, contraindicações e interações medicamentosas não estavam disponíveis no Evidence Pack atual.

> **Nota:** A obtenção da bula e das advertências regulatórias junto à ANVISA é classificada como lacuna de dados de severidade **Blocking** (DG001), necessária para prosseguir com a avaliação de segurança na etapa S1.

---

## Outras Indicações Previstas pelo TxGNN

Além da indicação principal, o modelo previu outras quatro condições para o bisoprolol. O resumo abaixo contextualiza cada uma:

| Rank | Doença Prevista | Pontuação TxGNN | Nível de Evidência | Recomendação | Justificativa Mecanística |
|------|----------------|-----------------|---------------------|--------------|---------------------------|
| 2 | Hipertensão renovascular maligna | 99,94% | L4 | Hold | Associação moderada, porém controversa. A causa raiz é estenose de artéria renal com hiperativação do SRAA; IECA/BRA são preferidos. β-bloqueador pode ser adjuvante em estenose unilateral, mas requer cautela em estenose bilateral. |
| 3 | Hipertensão pulmonar multifatorial (WHO Grupo 5) | 99,93% | L5 | Hold | Associação fraca com preocupações de segurança. Betabloqueadores são tradicionalmente contraindicados em HAP, pois o ventrículo direito depende do tônus simpático. Estudos iniciais com β1-seletivos são muito preliminares. |
| 4 | Hipertensão pulmonar por doença pulmonar/hipóxia (WHO Grupo 3) | 99,93% | L5 | Hold | Associação fraca com preocupações de segurança. Em altas doses, bisoprolol pode afetar receptores β2, causando broncoconstrição em pacientes com doença pulmonar preexistente. Impacto hemodinâmico no VD comprometido é preocupante. |
| 5 | Síndrome de Braddock | 99,91% | L5 | Hold | Sem associação conhecida. Doença autossômica recessiva rara com anomalias congênitas (megacistis, intestino curto). Sem relação com bloqueio β1-adrenérgico. |

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A previsão de eficácia do bisoprolol na doença renal hipertensiva maligna é mecanisticamente sólida — o fármaco já é um anti-hipertensivo de primeira linha e o controle pressórico é o pilar do tratamento desta condição. Embora não existam ensaios clínicos ou publicações específicas para esta combinação, a base farmacológica é robusta o suficiente para justificar uma exploração cautelosa. As demais indicações previstas (ranks 2-5) apresentam justificativas mais fracas ou preocupações de segurança significativas, sendo recomendado o status **Hold** para todas elas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula junto à ANVISA para completar a avaliação de segurança (lacuna DG001 — severidade Blocking)
- Consultar o DrugBank para dados detalhados do mecanismo de ação (lacuna DG002 — severidade High)
- Realizar busca bibliográfica expandida sobre o uso de betabloqueadores em emergências hipertensivas com comprometimento renal
- Definir critérios de monitoramento renal (TFG, creatinina, proteinúria) para acompanhamento da eficácia
- Avaliar a necessidade de associação com outros anti-hipertensivos (IECA/BRA, bloqueadores de canais de cálcio) no contexto de hipertensão maligna com lesão renal
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

