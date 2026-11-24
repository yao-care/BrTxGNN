---
layout: default
title: Amlodipine Besylate
parent: Apenas Predição do Modelo (L5)
nav_order: 60
evidence_level: L5
indication_count: 9
drugbank_id: DB00381
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-24
description: "Amlodipine Besylate: nova indicação prevista, Infarto do tronco encefálico (brain stem infarction) (nível de evidência L5). Indicação original: ANTI-HIPERTENSIVOS SIMPLES"
---

# Amlodipine Besylate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Amlodipine Besylate: Infarto do tronco encefálico (brain stem infarction)
{: .text-alpha }

## Resumo em Uma Frase

Besilato de anlodipino é um bloqueador dos canais de cálcio usado no tratamento da pressão alta.
O modelo TxGNN prevê que pode ser eficaz para **Infarto do tronco encefálico (brain stem infarction)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTI-HIPERTENSIVOS SIMPLES; ANTI-HIPERTENSIVOS |
| Nova Indicação Prevista | Infarto do tronco encefálico (brain stem infarction) |
| Pontuação de Previsão TxGNN | 0.9994 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | pelo menos 20 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Amlodipine Besylate (tradução não oficial): “A anlodipina é um antagonista do cálcio di-hidropiridínico (antagonista do íon cálcio ou bloqueador dos canais lentos) que inibe o influxo transmembrana de íons cálcio para o músculo liso vascular e para o músculo cardíaco. Dados experimentais sugerem que a anlodipina se liga tanto a sítios de ligação di-hidropiridínicos quanto não di-hidropiridínicos.” Texto original em inglês: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), versão de 2026-09-28; acessado em 2026-11-19). Sabe-se que o anlodipino é um bloqueador dos canais de cálcio do tipo L, da classe das di-hidropiridinas, que relaxa a musculatura lisa das artérias e reduz a pressão arterial.

A hipótese do modelo é que a redução da pressão arterial e uma possível neuroproteção, plausíveis em outros acidentes vasculares cerebrais isquêmicos, também possam ser relevantes para o infarto do tronco encefálico. Trata-se de uma inferência a partir de condições cerebrovasculares relacionadas, e não de evidência direta.

Nenhum ensaio clínico ou publicação foi associado especificamente a esta doença. Por isso, a previsão não pode ser considerada respaldada por estudos reais, e a pontuação alta reflete apenas a proximidade do fármaco com condições cerebrovasculares nos dados do modelo.

## Informações de Comercialização no Brasil

O fármaco consta como comercializado, com registros válidos de produtos de princípio ativo único. A lista abaixo pode ser parcial, pois há pelo menos 20 registros.

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 100470275 | AMLOVASC | Ativo |
| 100630261 | BESILATO DE ANLODIPINO | Ativo |
| 100890273 | BESILATO DE ANLODIPINO | Ativo |
| 100890387 | ROXFLAN | Ativo |
| 102980341 | BESILATO DE ANLODIPINO | Ativo |
| 103700372 | BESILATO DE ANLODIPINO | Ativo |
| 103920150 | AMLODIL | Ativo |
| 103920187 | BESILATO DE ANLODIPINO | Ativo |
| 104300018 | NEMODINE | Ativo |
| 104810103 | BESILATO DE ANLODIPINO | Ativo |
| 105730584 | CORDAREX | Ativo |
| 105730597 | BESILATO DE ANLODIPINO | Ativo |
| 109740310 | BESILATO DE ANLODIPINO | Ativo |
| 118190274 | ANLUSBED | Ativo |
| 125680197 | BESILATO DE ANLODIPINO | Ativo |
| 135690680 | ANLO | Ativo |
| 143810161 | BESILATO DE ANLODIPINO | Ativo |
| 151670029 | BESILATO DE ANLODIPINO | Ativo |
| 154230207 | BESILATO DE ANLODIPINO | Ativo |
| 188300080 | NORVASC | Ativo |

Os dados contêm apenas parte dos registros; a lista pode estar incompleta.

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que estudem diretamente o infarto do tronco encefálico; a previsão tem nível de evidência L5 e depende apenas do modelo.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos ou clínicos que avaliem diretamente o anlodipino em infarto do tronco encefálico
- Dados do mecanismo de ação e informações de segurança da bula da ANVISA
- Revisão por especialistas para confirmar a plausibilidade biológica da previsão

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

