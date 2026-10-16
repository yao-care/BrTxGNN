---
layout: default
title: Telmisartan
parent: Apenas Predição do Modelo (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Telmisartan: nova indicação prevista, Oclusão de Artéria Cerebral (Cerebral Artery Occlusion) (nível de evidência L5). Indicação original: Hipertensão arterial (também AVC e infarto cerebral…"
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "malignant renovascular hypertension", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Telmisartana: Da hipertensão arterial ao acidente vascular cerebral por oclusão de artéria cerebral

## Resumo em Uma Frase

Telmisartana é um bloqueador do receptor de angiotensina II tipo 1 (BRA), originalmente usado no tratamento da hipertensão arterial e na prevenção de acidente vascular cerebral (AVC).
O modelo TxGNN prevê que pode ser eficaz para **Oclusão de Artéria Cerebral (Cerebral Artery Occlusion)**, a indicação prevista com maior volume de evidências entre as candidatas de maior pontuação. Atualmente há **3 ensaios clínicos** (de baixo valor informativo) e **20 publicações** (quase todas pré-clínicas) apoiando esta direção.

> Observação: a indicação de maior pontuação do modelo é a angina de Prinzmetal (99,98%), mas sem nenhuma evidência real. Este relatório foca em oclusão de artéria cerebral, que tem a maior base de evidências entre as candidatas. A hemorragia intracerebral, com evidência de nível L2, é discutida na conclusão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial (também AVC e infarto cerebral, segundo o grafo de conhecimento) |
| Nova Indicação Prevista | Oclusão de Artéria Cerebral (Cerebral Artery Occlusion) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L3 (atribuído de forma conservadora; apoio majoritariamente pré-clínico e indireto) |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a telmisartana bloqueia o receptor AT1 da angiotensina II e tem atividade agonista parcial sobre o PPARγ, o que lhe rendeu o apelido de "metabosartan". Sua eficácia na hipertensão arterial é estabelecida.

A hipertensão e o AVC compartilham a mesma fisiopatologia vascular, e a oclusão de artéria cerebral é uma causa direta de infarto cerebral, indicação já associada ao fármaco no grafo de conhecimento. Por isso, a previsão é biologicamente coerente.

A literatura pré-clínica indica que a telmisartana reduz o volume de infarto cerebral, o estresse oxidativo e a neuroinflamação em modelos de oclusão da artéria cerebral média em roedores. Os mecanismos descritos incluem inibição de Egr-1 mediada por PPARγ, modulação da via Nrf2/HO-1 e sinergia com nimodipina. Esses achados vêm de animais e ainda não foram confirmados em humanos.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Concluído | 1228 | Telmisartana vs. terapia habitual na prevenção de doença cardiovascular em hipertensos de alto risco; relevância indireta para o risco cerebrovascular |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Encerrado | 4 | Subestudo de RM do TRIDENT (pílula tripla anti-hipertensiva após hemorragia intracerebral); amostra pequena demais para gerar dados úteis |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Encerrado | 1 | Subestudo cognitivo do TRIDENT; apenas 1 participante, sem dados interpretáveis |

## Evidências da Literatura

Todas as publicações abaixo são estudos pré-clínicos em animais, sem ensaios clínicos randomizados específicos para oclusão de artéria cerebral.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Pré-clínico (animal) | J Neurotrauma | Telmisartana reduziu o volume de infarto cerebral e os níveis de cPLA2 peri-infarto na oclusão da artéria cerebral média em ratos |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Pré-clínico (animal) | Pharmacol Biochem Behav | Dose não hipotensiva de telmisartana com nimodipina teve efeito neuroprotetor sinérgico, reduzindo citocinas cerebrais |
| [28699721](https://pubmed.ncbi.nlm.nih.gov/28699721/) | 2016 | Pré-clínico (animal) | Indian J Exp Biol | Comparou tratamento pré e pós-isquemia com telmisartana e nimodipina em isquemia cerebral experimental |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Pré-clínico (animal) | J Stroke Cerebrovasc Dis | A ativação de PPARγ pela telmisartana inibiu Egr-1 e reduziu a lesão cerebral em modelo de AVC isquêmico |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Pré-clínico (animal) | PLoS One | Telmisartana, ramipril e a combinação foram comparados na prevenção de AVC e na neuroproteção em modelos de ratos |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Pré-clínico (animal) | Toxicol Rep | Atenuação da neurotoxicidade da isquemia-reperfusão cerebral via Nrf2/HO-1 |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | Pré-clínico (animal) | J Stroke Cerebrovasc Dis | Telmisartana reduziu respostas inflamatórias cerebrais em SHR-SR após oclusão transitória da artéria cerebral média |
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | Pré-clínico (animal) | J Stroke Cerebrovasc Dis | Redução do estresse oxidativo e do acúmulo de α-sinucleína fosforilada em ratos após oclusão transitória |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | Pré-clínico (animal) | J Stroke Cerebrovasc Dis | Melhora de moléculas relacionadas à síndrome metabólica a longo prazo (IR, PPAR-γ, AT1R) |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | Pré-clínico (animal) | J Hypertens | Dose baixa de telmisartana preveniu dano cerebral isquêmico com ativação de PPARγ em camundongos diabéticos |

## Considerações de Segurança

Não há dados de advertências e contraindicações da bula nos dados compilados; consulte a bula para essas informações.

- **Contraindicações e condições de risco (grafo de conhecimento, não texto de bula)**: insuficiência hepática, doença hepática, colestase (incluindo formas intra-hepáticas familiares e recorrente benigna), encefalopatia/coma hepático, doença renal, anúria, obstrução da artéria renal, pancreatite, doença da vesícula biliar, lúpus eritematoso sistêmico, diabetes mellitus e cetoacidose diabética, gota e hiperuricemia, hipocalemia (deficiência de potássio), hipercalcemia, nefrocalcinose, hiperparatireoidismo, distúrbios do metabolismo do fósforo e hipotensão.
- **Interações Medicamentosas** (100 interações registradas; principais):
  - **Maiores (Major)**: citrato de potássio e bicarbonato de potássio, com risco de hipercalemia.
  - **Moderadas**: corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), ácido acetilsalicílico, morfina, bupropiona, inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), exenatida, insulinas, dronabinol e preparos de limpeza intestinal (ácido picossulfúrico, sulfato de sódio, polietilenoglicol).

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para oclusão de artéria cerebral, o apoio é quase todo pré-clínico, e os três ensaios clínicos associados são indiretos ou com amostras mínimas (1 a 4 participantes). Além disso, o fármaco não está comercializado no Brasil e faltam dados de bula e de mecanismo, o que impede a triagem de segurança.

**Observação sobre outras indicações previstas:**
- **Hemorragia intracerebral** tem o maior nível de evidência (L2): o ensaio TRIDENT (Phase 3, 1671 participantes, concluído) e uma publicação de 2026 no NEJM testaram uma pílula única com três anti-hipertensivos em baixa dose. Porém, o efeito não pode ser atribuído à telmisartana isolada, e o resultado principal não consta nos dados compilados.
- As demais indicações (angina de Prinzmetal, infarto de tronco encefálico, amiloidose ABri, hipertensão pulmonar, hipertensão maligna renal/renovascular e síndrome de Braddock) têm apenas previsão do modelo (L5) ou apoio indireto (L4), sem ensaios clínicos.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada (advertências e contraindicações) para liberar a triagem de segurança.
- Complementar os dados de mecanismo de ação (MOA), por exemplo, consultando o DrugBank.
- Obter o resultado principal do TRIDENT e avaliar a contribuição específica da telmisartana na combinação.
- Buscar evidência clínica humana direta (ensaios de fase 2/3) em AVC isquêmico/oclusão arterial cerebral.
- Verificar a situação regulatória no Brasil, já que não há registro vigente nos dados compilados.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

