---
layout: default
title: Perindopril
parent: Apenas Predição do Modelo (L5)
nav_order: 518
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
description: "Perindopril: nova indicação prevista, Doença renal hipertensiva maligna (malignant hypertensive renal disea… (nível de evidência L4). Indicação original: Anti-hipertensivos"
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Perindopril
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Perindopril: Da hipertensão arterial à doença renal hipertensiva maligna
{: .text-alpha }

## Resumo em Uma Frase

Perindopril é um inibidor da enzima conversora de angiotensina (IECA), originalmente usado como anti-hipertensivo.
O modelo TxGNN prevê que pode ser eficaz para **doença renal hipertensiva maligna (malignant hypertensive renal disease)**,
mas atualmente há **0 ensaios clínicos** e **1 publicação** (sem relevância direta) associados a esta direção. A previsão se apoia essencialmente no modelo e na plausibilidade mecanística.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-hipertensivos |
| Nova Indicação Prevista | Doença renal hipertensiva maligna (malignant hypertensive renal disease) |
| Pontuação de Previsão TxGNN | 0,9977 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 11) |
| Número de Registros | 11 (ativos: 6) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o perindopril é um IECA: bloqueia a formação de angiotensina II, reduzindo a pressão arterial e a pressão intraglomerular. Sua eficácia na hipertensão está estabelecida, e os IECA são amplamente reconhecidos também pela proteção renal.

A hipertensão e a lesão renal hipertensiva compartilham a mesma via fisiopatológica (sistema renina-angiotensina-aldosterona), o que torna a previsão biologicamente plausível. Contudo, não há evidência específica para a nefropatia hipertensiva maligna. A pontuação elevada do modelo provavelmente reflete a indicação já existente para hipertensão e a proximidade na rede de conhecimento, e não evidência nova.

O único artigo associado (PMID 36382821) trata da função do rim único após nefrectomia por câncer renal e não tem relevância direta com esta indicação.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Estudo observacional (inferido pelo título) | Urologiia | Função do rim solitário após nefrectomia por câncer renal; sem relevância direta para o perindopril ou para a nefropatia hipertensiva maligna |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102351261 | PERINDOPRIL ERBUMINA + INDAPAMIDA | EMS S/A | Ativo |
| 112780074 | ACERTIL | LABORATÓRIOS SERVIER DO BRASIL LTDA | Ativo |
| 112780075 | ACERTANLO | LABORATÓRIOS SERVIER DO BRASIL LTDA | Ativo |
| 112780077 | ACERTALIX | LABORATÓRIOS SERVIER DO BRASIL LTDA | Ativo |
| 112780084 | TRIPLIXAM | LABORATÓRIOS SERVIER DO BRASIL LTDA | Ativo |
| 123520206 | PERINDOPRIL ERBUMINA | RANBAXY FARMACÊUTICA LTDA | Ativo |
| 105250036 | PERICOR | TORRENT DO BRASIL LTDA | Cancelado |
| 105250037 | PERINDOPRIL | TORRENT DO BRASIL LTDA | Cancelado |
| 110130257 | PERICARD PLUS | GLENMARK FARMACÊUTICA LTDA | Cancelado |
| 112780051 | COVERSYL | LABORATÓRIOS SERVIER DO BRASIL LTDA | Cancelado |
| 112780056 | COVERSYL PLUS | LABORATÓRIOS SERVIER DO BRASIL LTDA | Cancelado |

Há ainda um sexto registro (TRIPLIXAM, inibidores da ECA, associações), também cancelado.

## Considerações de Segurança

- **Contraindicações e doenças associadas (grafo de conhecimento TxGNN, não extraídas da bula)**: doença renal, doença hepática, doença da vesícula biliar, angioedema (incluindo adquirido, hereditário e induzido por bloqueadores do sistema renina-angiotensina-aldosterona), neutropenia, agranulocitose, distúrbio hipotensivo, doença do tecido conjuntivo, doença óssea, doença da cartilagem, obstrução da artéria renal, piureter.
- **Interações Medicamentosas**: 213 interações registradas. Entre as de gravidade **maior** estão **citrato de potássio** e **bicarbonato de potássio** (risco de hiperpotassemia). As demais amostras são de gravidade moderada, incluindo corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropiona e dronabinol.
- **Pontos de atenção específicos**: em estenose bilateral da artéria renal ou rim único estenótico, os IECA podem precipitar lesão renal aguda. Relatos de caso na literatura descrevem angioedema potencialmente fatal associado a IECA.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo TxGNN (deep learning) (0,9977), mas não há ensaios clínicos nem literatura relevante para a doença renal hipertensiva maligna (nível L4). O medicamento está comercializado no Brasil (6 registros válidos de 6), e a segurança renal exige cautela.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), ainda indisponível.
- Complementar os dados de mecanismo de ação (DrugBank).
- Realizar revisão sistemática da literatura clínica sobre IECA em nefropatia hipertensiva maligna.
- Avaliar o risco renal (estenose de artéria renal, hiperpotassemia) e a situação regulatória, já que não há registro válido no Brasil.
- Se o interesse for mantido, considerar a indicação alternativa: hipertensão pulmonar por doença pulmonar e/ou hipóxia (há apenas estudos pré-clínicos em ratos, nível L4), também em *Hold*.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

