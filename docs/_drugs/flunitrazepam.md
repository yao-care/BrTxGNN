---
layout: default
title: Flunitrazepam
parent: Evidência Moderada (L3-L4)
nav_order: 321
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Flunitrazepam: nova indicação prevista, Insônia (insomnia) (nível de evidência L3). Indicação original: Não informada nos dados compilados"
monitor_inn: "Flunitrazepam"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "anxiety", "anxiety disorder", "alcohol withdrawal delirium", "migraine with or without aura, susceptibility to", "agoraphobia", "benign paroxysmal torticollis of infancy", "atrophoderma vermiculata"]
---

# Flunitrazepam
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **10** 
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

# Flunitrazepam: Da indicação original não registrada à insônia

## Resumo em Uma Frase

Flunitrazepam é um benzodiazepínico com ação sedativo-hipnótica; os dados compilados para este relatório não trazem a indicação original registrada na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **insônia (insomnia)**, atualmente sem ensaios clínicos registrados, mas com **10 publicações** associadas a esta direção (várias delas indiretas ou fora do tema).
Trata-se mais de uma confirmação de uso já conhecido do que de um reposicionamento inédito.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não informada nos dados compilados |
| Nova Indicação Prevista | Insônia (insomnia) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na fonte consultada. Segundo informações farmacológicas conhecidas, o flunitrazepam é um benzodiazepínico que atua como modulador alostérico positivo do receptor GABA-A. Os dados compilados registram ligação às subunidades α1, α2, α3 e α5 desse receptor, e o uso clínico descrito é o tratamento de alguns casos de insônia grave.

Esse mecanismo explica diretamente o efeito hipnótico: ao potencializar a inibição GABAérgica, o fármaco favorece o início e a manutenção do sono. A literatura recuperada inclui estudos comparativos com triazolam e zolpidem, um relato clínico sobre distúrbios do sono orgânicos e funcionais e revisões sobre hipnóticos benzodiazepínicos.

Como a indicação original não consta nos dados e o fármaco já é descrito como hipnótico, a previsão para insônia é plausível, mas representa sobretudo a confirmação de um uso estabelecido.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Revisão | Drugs | Revisão do triazolam como hipnótico; considera-o mais adequado que benzodiazepínicos de ação longa, como o flunitrazepam |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | Estudo clínico | JAMA | Insônia de rebote após suspensão de triazolam, nitrazepam e flunitrazepam, mesmo em curtos períodos |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | Farmacologia clínica | Eur Respir J | Comparação de zolpidem, triazolam e flunitrazepam sobre gases sanguíneos e respiração em DPOC grave |
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | Estudo clínico | La Nouvelle Presse Médicale | Ação do flunitrazepam em distúrbios do sono orgânicos e funcionais |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisão | Acta Psychiatr Scand Suppl | Indicações dos hipnóticos e necessidade de variedade de perfis farmacocinéticos |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Revisão | Acta Psychiatr Scand Suppl | Resposta aumentada aos benzodiazepínicos (incluindo flunitrazepam) em idosos |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Farmacologia clínica | Sleep Med Rev | Hipnóticos prejudicam equilíbrio corporal e estabilidade postural, com risco de quedas |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | Pré-clínico (rato) | Psychopharmacology | Efeitos de três hipnóticos no ciclo sono-vigília em ratos com distúrbio do sono |

---

## Considerações de Segurança

- **Interações e alvos farmacológicos**: o fármaco liga-se às subunidades α1, α2, α3 e α5 do receptor GABA-A, o que explica a depressão do sistema nervoso central.
- **Riscos documentados na literatura**: insônia de rebote após a suspensão, efeitos sobre a respiração (relevante em DPOC), prejuízo do equilíbrio com risco de quedas, maior sensibilidade em idosos, e potencial de abuso e dependência.

Para advertências e contraindicações formais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo é coerente e há literatura clínica de apoio ao uso hipnótico, mas sem ensaios registrados, sem registro no Brasil e com riscos relevantes de abuso, dependência e insônia de rebote.

**Para prosseguir, é necessário:**
- Obter a indicação original e a bula na ANVISA, incluindo advertências e contraindicações (lacuna que bloqueia a triagem de segurança)
- Confirmar o mecanismo de ação em fonte primária (por exemplo, DrugBank)
- Avaliar a situação regulatória e de controle (substância controlada) no Brasil, já que o fármaco não é comercializado
- Definir plano de mitigação de risco para abuso, dependência, uso em idosos e pacientes com doença respiratória
- Comparar com hipnóticos já disponíveis para justificar o valor incremental
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

