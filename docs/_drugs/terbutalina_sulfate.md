---
layout: default
title: Terbutalina Sulfate
parent: Apenas Predição do Modelo (L5)
nav_order: 614
evidence_level: L5
indication_count: 2
drugbank_id: DB00871
monitor_inn: "Terbutaline"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
last_modified_at: 2026-11-16
description: "Terbutalina Sulfate: nova indicação prevista, Respiratory malformation (nível de evidência L5). Indicação original: BRONCODILATADORES"
---

# Terbutalina Sulfate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Terbutalina Sulfate: Respiratory malformation
{: .text-alpha }

## Resumo em Uma Frase

Terbutalina sulfato é um broncodilatador agonista beta-2 adrenérgico, usado no Brasil como broncodilatador.
O modelo TxGNN prevê que pode ser eficaz para **Doença pulmonar obstrutiva (obstructive lung disease)**,
com **14 ensaios clínicos** e **20 publicações** compilados para esta direção, embora a maior parte dos ensaios use a terbutalina apenas como comparador ou medicação de resgate.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | BRONCODILATADORES |
| Nova Indicação Prevista | Respiratory malformation |
| Pontuação de Previsão TxGNN | 0.9952 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 6) |
| Número de Registros | 6 (ativos: 5) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação na base compilada para este relatório. Pelo conhecimento farmacológico estabelecido, a terbutalina é um agonista beta-2 adrenérgico seletivo: ao ativar o receptor acoplado à proteína Gs, aumenta o AMP cíclico e relaxa a musculatura lisa brônquica, produzindo broncodilatação.

Esse mecanismo é exatamente o que se espera para aliviar a obstrução reversível das vias aéreas, como na asma e na doença pulmonar obstrutiva crônica. Por isso, a previsão do modelo é coerente, mas deve ser vista como uma confirmação de uso já conhecido ou muito próximo do já conhecido, e não como uma oportunidade de reposicionamento realmente nova.

Cuidados que acompanham o uso: efeitos cardiovasculares (taquicardia, arritmia), hipopotassemia e tremor; status de controle antidoping em atletas; e uso em gestantes e crianças, que exige doses específicas para cada população.

## Evidências de Ensaios Clínicos

Os ensaios abaixo estudam asma ou DPOC, que são doenças obstrutivas. Em vários deles a terbutalina é apenas comparador ou resgate, portanto a evidência é parcialmente indireta. Foram selecionados os 10 mais relevantes.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Concluído | 24 | Terbutalina Turbuhaler 0,4 mg vs salbutamol pMDI 200 μg, cruzado, em adultos japoneses com asma; avalia eficácia relativa e segurança |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Concluído | 120 | Sulfato de magnésio intravenoso vs terbutalina em crianças com exacerbação aguda de asma |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Concluído | 3850 | Symbicort conforme necessário vs terbutalina conforme necessário vs Pulmicort 2x/dia + terbutalina, em asma leve |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Concluído | 4215 | Symbicort conforme necessário vs Pulmicort 2x/dia + terbutalina conforme necessário em asma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Concluído | 2091 | Symbicort SMART vs Symbicort + terbutalina conforme necessário (terbutalina como resgate comparador) |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Concluído | 1970 | Custos de saúde e controle da asma com Symbicort vs combinação livre com Bricanyl (terbutalina) como resgate |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | Concluído | 1600 | Symbicort em terapia de inalador único vs melhor prática convencional em asma persistente |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Concluído | 860 | Budesonida/formoterol conforme necessário vs regular + terbutalina conforme necessário em asma leve a moderada |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Concluído | 95 | Bricanyl Turbuhaler M3 vs M2: proteção contra broncoconstrição induzida por metacolina em asma estável |
| [NCT00421122](https://clinicaltrials.gov/study/NCT00421122) | Phase 3 | Concluído | 315 | Symbicort + Bricasol (terbutalina) vs Pulmicort + Bricasol em pacientes chineses com DPOC |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | Budesonida-formoterol conforme necessário como alternativa às estratégias convencionais na asma leve (a terbutalina compõe o comparador) |
| [3281307](https://pubmed.ncbi.nlm.nih.gov/3281307/) | 1988 | RCT | Thorax | Adrenalina vs terbutalina subcutâneas em 20 pacientes com asma aguda grave |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | Terbutalina oral aumentou a força diafragmática em 10 pacientes com DPOC moderada a grave |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revisão sistemática | Naunyn-Schmiedeberg's Arch Pharmacol | Farmacocinética da terbutalina em humanos; usada em broncoespasmo de asma, bronquite, enfisema e DPOC |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revisão | Am J Respir Crit Care Med | Terapia com beta-2 agonistas em doenças pulmonares; terbutalina como agonista de curta duração |
| [4571398](https://pubmed.ncbi.nlm.nih.gov/4571398/) | 1973 | Estudo clínico | Arch Dis Child | Terbutalina oral em 30 crianças asmáticas: ação ventilatória prolongada sem efeitos cardiovasculares na dose maior |
| [326244](https://pubmed.ncbi.nlm.nih.gov/326244/) | 1977 | Estudo clínico | Aust N Z J Med | Aerossóis de terbutalina e salbutamol em 16 pacientes; salbutamol com broncodilatação maior na primeira hora |
| [373786](https://pubmed.ncbi.nlm.nih.gov/373786/) | 1979 | Estudo cruzado | Br J Dis Chest | Fenoterol e terbutalina aumentaram o pico de fluxo expiratório vs placebo em 17 asmáticos |
| [26963310](https://pubmed.ncbi.nlm.nih.gov/26963310/) | 2015 | Revisão | Tuberk Toraks | Síndrome de sobreposição asma-DPOC, com limitação do fluxo aéreo parcialmente reversível |
| [1478020](https://pubmed.ncbi.nlm.nih.gov/1478020/) | 1992 | Revisão | Clin Chest Med | Asma na gestação: agonista beta-adrenérgico inalado (terbutalina) como opção de manejo |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104971176 | TERBUTIL | Não informada | Broncodilatadores |
| Registro 113430176 | Sulfato de Terbutalina | Não informada | Broncodilatadores |
| Registro 120190142 | Sulfato de Terbutalina | Não informada | Broncodilatadores |
| Registro 125680088 | Sulfato de Terbutalina | Não informada | Broncodilatadores |
| Registro 167730050 | BRONQUITOSS | Não informada | Broncodilatadores |

## Considerações de Segurança

Consulte a bula para informações de segurança. Entre os cuidados apontados na análise do mecanismo: efeitos cardiovasculares (taquicardia, arritmia), hipopotassemia, tremor, controle antidoping em atletas e dosagem específica em gestantes e crianças.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há vários ensaios de Phase 3 concluídos em asma e DPOC, com a terbutalina como intervenção ou comparador, e o mecanismo beta-2 agonista é bem estabelecido. A previsão é, na prática, uma confirmação de uso já conhecido, e não um reposicionamento novo.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações) para a triagem de segurança.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Definir um plano de monitoramento cardiovascular e de potássio, com dosagem específica para gestantes e crianças, e orientação sobre o controle antidoping.
- Priorizar ensaios em que a terbutalina seja a intervenção testada, e não apenas o resgate comparador.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A ausência de registro no Brasil, de dados de mecanismo de ação e de indicação primária documentada no pack inviabiliza uma avaliação comple” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “e o fármaco não possui qualquer registro ativo na ANVISA segundo os dados consultados em 26/03/2026” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “⚠️ **Nota metodológica:** A ausência de resultados na consulta TFDA/ANVISA é inconsistente com o conhecimento farmacológico estabelecido sob” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

