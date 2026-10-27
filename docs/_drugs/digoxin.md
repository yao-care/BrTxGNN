---
layout: default
title: Digoxin
parent: Apenas Predição do Modelo (L5)
nav_order: 269
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Digoxin: nova indicação prevista, Angina de Prinzmetal (Prinzmetal angina) (nível de evidência L5). Indicação original: Fibrilação atrial"
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
---

# Digoxin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Digoxina: Da fibrilação atrial à angina de Prinzmetal
{: .text-alpha }

## Resumo em Uma Frase

A digoxina é um glicosídeo cardíaco, originalmente usado no tratamento da fibrilação atrial e da intoxicação digitálica.
O modelo TxGNN prevê que ela possa ser eficaz para **Angina de Prinzmetal (Prinzmetal angina)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão sem relação direta com o fármaco) associadas a esta previsão.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrilação atrial; intoxicação digitálica (conforme o grafo de conhecimento TxGNN, pois não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Angina de Prinzmetal (Prinzmetal angina) |
| Pontuação de Previsão TxGNN | 99,81% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a digoxina inibe a Na⁺/K⁺-ATPase das células miocárdicas, o que aumenta a contratilidade (efeito inotrópico positivo) e reduz a condução atrioventricular, sendo útil no controle da frequência na fibrilação atrial.

A angina de Prinzmetal, por sua vez, é causada por vasoespasmo coronariano e costuma ser tratada com bloqueadores de canal de cálcio e nitratos. Não há um vínculo mecanístico evidente entre a digoxina e essa condição: o efeito inotrópico positivo não traz benefício claro contra o vasoespasmo e, teoricamente, poderia até piorá-lo.

Assim, apesar da pontuação muito alta do modelo (99,81%), a previsão não é sustentada por evidências biológicas ou clínicas. A única publicação associada trata de cronofarmacologia no tratamento anti-hipertensivo e não aborda a digoxina nem a angina vasoespástica. A pontuação provavelmente reflete proximidade na rede do grafo de conhecimento, e não um racional terapêutico.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Revisão | Acta Physiol Pharmacol Bulg | Revisão sobre cronofarmacologia e ritmos circadianos no tratamento anti-hipertensivo; não aborda digoxina nem angina de Prinzmetal |

Atualmente não há ensaios clínicos relacionados registrados.

---

## Considerações de Segurança

- **Contraindicações descritas no grafo de conhecimento** (relações fármaco-doença do TxGNN, não texto de bula): doença renal, deficiência de potássio, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, infarto do miocárdio, trombose coronariana, hemoglobinopatia, cor pulmonale, síndrome de Wolff-Parkinson-White, doença do nó sinusal (inclusive familiar), fibrilação ventricular, cardiomiopatia hipertrófica (inclusive familiar), bloqueio atrioventricular, mixedema, hipotireoidismo (inclusive congênito), miocardite, pericardite constritiva e cardiomiopatia restritiva.
- **Interações medicamentosas**: foram identificadas 100 interações; entre as listadas, a maioria é de gravidade moderada, por exemplo:
  - Acarbose, rabeprazol, doxiciclina, epinefrina, hidrocortisona
  - Colecalciferol, metformina, anfotericina B (inclusive complexo lipídico), bupropiona, triancinolona
  - Ácido acetilsalicílico, dexametasona, betametasona, tetraciclina, fosfato de cálcio
  - De gravidade leve: albiglutida, hiosciamina, atropina, glicopirrônio

Para advertências e demais informações de segurança, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta, mas nenhum ensaio clínico, nenhuma literatura relevante e nenhum racional mecanístico plausível (nível L5). Além disso, o fármaco tem índice terapêutico estreito e várias contraindicações cardiovasculares, e não está registrado no Brasil nos dados compilados.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (por exemplo, via DrugBank) e analisar um possível vínculo com o vasoespasmo coronariano.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), bem como confirmar a situação de registro no Brasil.
- Realizar busca sistemática na literatura e em registros de ensaios sobre digoxina e angina vasoespástica.
- Se houver avanço, avaliar estudos pré-clínicos antes de qualquer estudo clínico.
- As demais previsões (obstrução duodenal, úlcera duodenal, refluxo duodenogástrico, hipoalfalipoproteinemia) também não têm evidências e permanecem em Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

