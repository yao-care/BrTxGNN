---
layout: default
title: Carvedilol
parent: Apenas Predição do Modelo (L5)
nav_order: 199
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Carvedilol: nova indicação prevista, Hipertensão renovascular maligna (Malignant Renovascular Hypertension) (nível de evidência L5). Indicação original: Hipertensão arterial (transtorno hipertensivo)"
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Carvedilol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

# Carvedilol: Da hipertensão à hipertensão renovascular maligna

## Resumo em Uma Frase

Carvedilol é um betabloqueador não seletivo com atividade bloqueadora alfa-1, originalmente usado no tratamento da hipertensão arterial.
O modelo TxGNN prevê que pode ser eficaz para **hipertensão renovascular maligna (malignant renovascular hypertension)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia exclusivamente no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial (transtorno hipertensivo) |
| Nova Indicação Prevista | Hipertensão renovascular maligna (Malignant Renovascular Hypertension) |
| Pontuação de Previsão TxGNN | 99,55% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

> Observação: a indicação original vem das relações de indicação do grafo de conhecimento do TxGNN, pois não há registros brasileiros com texto de indicação aprovada nos dados compilados.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o carvedilol é um betabloqueador não seletivo com bloqueio alfa-1 adicional, com eficácia comprovada na hipertensão, e mecanisticamente pode ser aplicável a formas graves da doença.

A hipertensão renovascular maligna é conduzida em grande parte pela ativação do sistema renina-angiotensina. O betabloqueio reduz a liberação de renina, e o efeito vasodilatador do bloqueio alfa-1 contribui para a redução da pressão arterial. Por isso, existe plausibilidade teórica.

Porém, esta previsão é basicamente uma extensão da indicação original (hipertensão) para um subtipo grave, e não um sinal independente de reposicionamento. Não há ensaios nem literatura que a sustentem. Além disso, crises hipertensivas malignas geralmente exigem tratamento parenteral agudo e titulável, de modo que o carvedilol oral não seria abordagem de primeira linha.

### Outras indicações previstas (todas sem ensaios clínicos)

| Indicação prevista | Pontuação TxGNN | Nível de evidência | Observação |
|------|------|------|------|
| Doença renal hipertensiva maligna | 99,55% | L5 | Sem estudos; o tratamento costuma exigir terapia parenteral titulável |
| Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,54% | L4 | Apenas evidência pré-clínica indireta (p. ex., reversão da hipertensão induzida por hipóxia intermitente crônica em ratos, PMID 26291659); estudos em modelos de hipertensão pulmonar e hipóxia com bloqueio adrenérgico; nenhum ensaio clínico |
| Hipertensão pulmonar de mecanismo multifatorial incerto | 99,54% | L5 | Betabloqueadores exigem cautela pelo risco de redução da função ventricular direita; direção do benefício incerta |
| Síndrome de Braddock | 99,37% | L5 | Sem justificativa mecanística; provável artefato de propagação do grafo |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação principal prevista.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal prevista.

## Considerações de Segurança

- **Contraindicações (relações do grafo de conhecimento, não texto de bula)**: insuficiência hepática, asma (incluindo intrínseca e alérgica), bronquite, doença brônquica, enfisema pulmonar, diabetes mellitus, cetoacidose diabética, hipotensão, doença vascular periférica (incluindo claudicação intermitente e doença arterial periférica), bloqueio atrioventricular, angina de Prinzmetal, síndrome do nó sinusal (incluindo a forma familiar), anafilaxia e síndrome da íris flácida intraoperatória.
- **Interações Medicamentosas**: foram identificadas 100 interações; entre as 20 listadas, a de maior gravidade é com **epinefrina (Major)**. A maioria é de gravidade moderada, incluindo corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), anticolinérgicos (atropina, hiosciamina), bupropiona, morfina, lorcaserina, canagliflozina, acetoexamida e sais de cálcio (carbonato, citrato, acetato e fosfato). Interações menores incluem ácido acetilsalicílico, hidróxido de alumínio e atapulgita.
- **Atenção específica**: em pacientes com doença pulmonar, o betabloqueio não seletivo pode piorar o broncoespasmo; em hipertensão pulmonar, pode reduzir o débito cardíaco e a função do ventrículo direito.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para hipertensão renovascular maligna (99,55%) é sustentada apenas pelo modelo (nível L5), sem ensaios ou publicações, e representa em grande parte uma extensão da indicação original de hipertensão. Além disso, o fármaco não possui registro comercializado no Brasil, segundo os dados compilados.

**Para prosseguir, é necessário:**
- Obter a bula aprovada pela ANVISA (advertências e contraindicações) e verificar a situação regulatória do carvedilol no Brasil, pois os dados compilados indicam ausência de registros
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca dirigida de literatura e ensaios sobre carvedilol em hipertensão renovascular e emergências hipertensivas
- Avaliar a viabilidade da via de administração oral frente à necessidade de terapia parenteral titulável em quadros malignos
- Se houver interesse em hipertensão pulmonar, tratá-la como questão de pesquisa (L4), com avaliação criteriosa de segurança ventricular direita e respiratória
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

