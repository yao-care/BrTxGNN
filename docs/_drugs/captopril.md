---
layout: default
title: Captopril
parent: Apenas Predição do Modelo (L5)
nav_order: 188
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Captopril: nova indicação prevista, Doença renal hipertensiva maligna (malignant hypertensive renal disea… (nível de evidência L5). Indicação original: Hipertensão arterial e nefropatia diabética (se…"
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Captopril
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

# Captopril: Da hipertensão arterial à doença renal hipertensiva maligna

## Resumo em Uma Frase

Captopril é um inibidor da enzima conversora de angiotensina (ECA), originalmente usado no tratamento de hipertensão arterial e nefropatia diabética.
O modelo TxGNN prevê que pode ser eficaz para **doença renal hipertensiva maligna (malignant hypertensive renal disease)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (um relato de caso diagnóstico, sem valor terapêutico) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial e nefropatia diabética (segundo o grafo de conhecimento do TxGNN; não há texto de indicação aprovado no Brasil) |
| Nova Indicação Prevista | Doença renal hipertensiva maligna (malignant hypertensive renal disease) |
| Pontuação de Previsão TxGNN | 99,28% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o captopril inibe a ECA, reduzindo a formação de angiotensina II (vasoconstritora) e a liberação de aldosterona. Sua eficácia na hipertensão e na nefropatia diabética já é reconhecida.

Na hipertensão maligna com comprometimento renal, a ativação do sistema renina-angiotensina-aldosterona (SRAA) contribui para a lesão vascular. Por isso, bloquear esse eixo é biologicamente plausível.

Ressalva importante: a nova indicação prevista é, em grande parte, uma extensão das indicações já existentes (hipertensão e doença renal), e não um sinal de reposicionamento genuíno. A pontuação alta do TxGNN é apenas uma previsão computacional. A única publicação disponível trata do uso diagnóstico da renografia com captopril, não de benefício terapêutico.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Relato de caso (diagnóstico) | Clinical Nuclear Medicine | Renografia com captopril positiva sem estenose de artéria renal; a causa foi um carcinoma de células renais cromófobo, e a hipertensão dependente de renina melhorou após a nefrectomia. Não é evidência terapêutica. |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento TxGNN, não texto de bula)**: angioedema (incluindo hereditário, adquirido e induzido por bloqueadores do SRAA), doença renal, doença hepática e encefalopatia hepática, pancreatite, doença da vesícula biliar, lúpus eritematoso sistêmico e doenças do tecido conjuntivo, neutropenia e agranulocitose, estenose aórtica e doença da valva aórtica, hipotensão, deficiência de potássio, diabetes mellitus e cetoacidose diabética, hiperparathyroidismo e doença óssea, além de hiperuricemia.
- **Interações Medicamentosas** (100 interações registradas; principais de gravidade moderada): corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), antidiabéticos (metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, exenatida, clorpropamida, acetoexamida), bupropiona, morfina, ácido acetilsalicílico e dronabinol. De gravidade leve: hidróxido de alumínio e carbonato de cálcio.
- **Atenção específica à indicação**: inibidores da ECA podem precipitar insuficiência renal aguda em estenose bilateral de artéria renal ou rim único.

Para advertências e contraindicações oficiais, consulte a bula; os dados da bula da ANVISA não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta, mas se apoia apenas no modelo (L5): não há ensaios clínicos e a única publicação é um relato de caso diagnóstico. Além disso, o fármaco não é comercializado no Brasil e já é indicado para hipertensão e nefropatia diabética.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (por exemplo, via DrugBank).
- Obter e analisar a bula da ANVISA (advertências e contraindicações) para a triagem de segurança.
- Buscar evidências clínicas terapêuticas (ensaios ou estudos observacionais) em hipertensão maligna com comprometimento renal.
- Esclarecer a situação regulatória do captopril no Brasil, já que não há registros nos dados compilados.
- Definir um plano de monitoramento de função renal e potássio, dado o risco em populações com estenose de artéria renal.

---

**Outras previsões do modelo (todas com decisão Hold):**

| Indicação Prevista | Pontuação TxGNN | Nível de Evidência | Observação |
|------|------|------|------|
| Hipertensão renovascular maligna | 99,28% | L4 | Sem ensaios; literatura majoritariamente diagnóstica ou de relatos de caso, com um relato antigo (1984) sobre captopril em hipertensão maligna. |
| Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,15% | L5 | Literatura pré-clínica ou fora do tema; vasodilatadores sistêmicos podem piorar a relação ventilação-perfusão. |
| Hipertensão pulmonar de mecanismo multifatorial incerto | 99,15% | L5 | Sem ensaios nem literatura; baseada apenas na previsão do modelo. |
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

