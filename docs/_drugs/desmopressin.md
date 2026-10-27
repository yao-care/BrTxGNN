---
layout: default
title: Desmopressin
parent: Apenas Predição do Modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Desmopressin: nova indicação prevista, Deficiência congênita de protrombina (congenital prothrombin deficien… (nível de evidência L5). Indicação original: Outros hormônios mediadores e produtos equiv…"
monitor_inn: "desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
---

# Desmopressin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Desmopressina: De "outros hormônios mediadores" para deficiência congênita de protrombina
{: .text-alpha }

## Resumo em Uma Frase

Desmopressina é um análogo sintético da vasopressina, registrado na ANVISA na categoria "outros hormônios mediadores e produtos equivalentes".
O modelo TxGNN prevê que pode ser eficaz para **deficiência congênita de protrombina (congenital prothrombin deficiency)**, mas não há **nenhum ensaio clínico** e apenas **1 publicação** (uma revisão geral de 1993) ligada a essa direção. A previsão não é sustentada por mecanismo plausível.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros hormônios mediadores e produtos equivalentes |
| Nova Indicação Prevista | Deficiência congênita de protrombina (congenital prothrombin deficiency) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 5 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a desmopressina aumenta os níveis plasmáticos do fator de von Willebrand (VWF) e do fator VIII por liberação mediada pelo receptor V2 a partir dos estoques endoteliais.

A protrombina (fator II) não é um fator sabidamente responsivo à desmopressina. Portanto, **não há justificativa mecanística clara** para esta indicação. A pontuação elevada do TxGNN provavelmente reflete a proximidade na rede de conhecimento com outros distúrbios hemorrágicos, e não um vínculo farmacológico direto.

Vale notar que a desmopressina é bem estabelecida em outros distúrbios hemorrágicos (hemofilia A leve e certos subtipos da doença de von Willebrand), o que explica a proximidade na rede, mas não sustenta por si só a deficiência de protrombina.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Revisão | Drugs | Revisão das opções racionais de tratamento de distúrbios hemorrágicos hereditários (hemofilia A, doença de von Willebrand), avaliando segurança, eficácia e custo; não aborda especificamente a desmopressina na deficiência de protrombina |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 110390115 | FURP-DESMOPRESSINA | Não informada | Outros hormônios mediadores e produtos equivalentes (cancelado) |
| Registro nº 128760021 | EPONIM | Não informada | Outros hormônios mediadores e produtos equivalentes (cancelado) |
| Registro nº 128760015 | DDAVP | Não informada | Outros hormônios mediadores e produtos equivalentes (cancelado) |
| Registro nº 106460172 | ACETATO DE DESMOPRESSINA | Não informada | Outros hormônios mediadores e produtos equivalentes (cancelado) |
| Registro nº 106460234 | DOSYX | Não informada | Outros hormônios mediadores e produtos equivalentes (cancelado) |

## Considerações de Segurança

- **Contraindicações (com base em associações do grafo de conhecimento, não em bula)**: hipertensão, rinite alérgica, rinite vasomotora, doença arterial coronariana, insuficiência renal, faringite, resfriado comum, fibrose cística, infecções do trato respiratório, doença de von Willebrand, diabetes insípido dipsogênico, polidipsia e intoxicação hídrica.
- **Interações medicamentosas**: foram identificadas 172 interações. Entre as de gravidade **maior** estão os corticosteroides (hidrocortisona, triancinolona, dexametasona, beclometasona, betametasona, budesonida, prednisolona e prednisona). Entre as de gravidade **moderada** estão epinefrina, loperamida, morfina (inclusive lipossomal), ópio e clorpropamida. Há ainda uma interação **menor** com ácido acetilsalicílico.
- **Risco geral do fármaco**: a literatura compilada menciona hiponatremia e, raramente, eventos trombóticos arteriais, o que é especialmente relevante diante da previsão de "trombofilia hereditária" (estado pró-trombótico).

As advertências e contraindicações da bula brasileira não estavam disponíveis; consulte a bula para informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos, a única publicação é uma revisão geral antiga e não existe vínculo mecanístico plausível entre a desmopressina e a deficiência de protrombina. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) no DrugBank.
- Bula da ANVISA com advertências e contraindicações (lacuna que bloqueia a triagem de segurança).
- Justificativa mecanística ou dados pré-clínicos que sustentem o uso na deficiência de protrombina.

**Observações sobre as demais previsões do modelo (todas sem ensaios clínicos registrados):**

| Indicação prevista | Pontuação | Nível | Avaliação |
|------|------|------|------|
| Trombofilia hereditária | 99,44% | L5 | Mecanisticamente implausível; pode representar risco de segurança, pois a desmopressina é pró-coagulante |
| Trombastenia de Glanzmann | 99,30% | L4 | Apoio apenas indireto e anedótico (revisões e relatos de caso); a desmopressina não corrige o defeito da integrina αIIbβ3. Questão de pesquisa |
| Distúrbio primário de liberação plaquetária | 99,26% | L3 | Observações clínicas pequenas, incluindo estudo pediátrico em defeito tipo aspirina (PMID 21509710) e revisão de 2023 (PMID 36656570); resposta variável. É a previsão com mais apoio. Questão de pesquisa |
| Pseudo-doença de von Willebrand | 99,16% | L4 | Conflita com a fisiopatologia; considerada relativamente contraindicada |
| Síndrome de Scott | 99,16% | L4 | Sem dados clínicos com desmopressina; mecanismo não corrige o defeito |
| "Flood factor deficiency" | 99,15% | L5 | Provável erro de mapeamento do nome da doença; requer curadoria antes de qualquer avaliação |
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

