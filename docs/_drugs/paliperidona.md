---
layout: default
title: Paliperidona
parent: Apenas Predição do Modelo (L5)
nav_order: 504
evidence_level: L5
indication_count: 9
drugbank_id: DB01267
monitor_inn: "Paliperidone"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-24
description: "Paliperidona: nova indicação prevista, distrofia retiniana com ou sem anomalias extraoculares (retinal dystrophy with or without extraocular anomalies) (nível de evidência L5)."
---

# Paliperidona
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

## Paliperidona: distrofia retiniana com ou sem anomalias extraoculares (retinal dystrophy with or without extraocular anomalies)
{: .text-alpha }

## Resumo em Uma Frase

Paliperidona é um antipsicótico comercializado no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **distrofia retiniana com ou sem anomalias extraoculares (retinal dystrophy with or without extraocular anomalies)**, mas **não há ensaios clínicos nem publicações** que apoiem esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | distrofia retiniana com ou sem anomalias extraoculares (retinal dystrophy with or without extraocular anomalies) |
| Pontuação de Previsão TxGNN | 0.9992 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 4 de 4) |
| Número de Registros | 4 (ativos: 4) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Paliperidona (tradução não oficial): “A paliperidona é o principal metabólito ativo da risperidona. O mecanismo de ação da paliperidona na esquizofrenia não está claro. No entanto, o efeito terapêutico do medicamento na esquizofrenia pode ser mediado por uma combinação de antagonismo dos receptores centrais de dopamina tipo 2 (D 2 ) e de serotonina tipo 2 (5HT 2A ).” Texto original em inglês: "Paliperidone is the major active metabolite of risperidone. The mechanism of action of paliperidone in schizophrenia is unclear. However, the drug's therapeutic effect in schizophrenia could be mediated through a combination of central dopamine Type 2 (D 2 ) and serotonin Type 2 (5HT 2A ) receptor antagonism." ([DailyMed: Invega (paliperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7b8e5b26-b9e4-4704-921b-3c3c0d159916), versão de 2025-01-31; acessado em 2026-11-19). Segundo informações conhecidas, a paliperidona (9-hidroxirrisperidona) é um antipsicótico que atua por antagonismo dos receptores dopaminérgicos D2 e serotoninérgicos 5-HT2A.

Não se identifica uma ligação plausível entre esse antagonismo e a degeneração retiniana hereditária. A distrofia retiniana é, em geral, de origem genética e estrutural, e um antipsicótico sintomático não tem efeito conhecido sobre os mecanismos que a causam.

A pontuação elevada provavelmente reflete um artefato da rede de relações do modelo, e não uma base farmacológica ou clínica. Esta previsão deve ser tratada como hipótese sem sustentação, não como direção promissora.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 112363388 | INVEGA | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 112363398 | INVEGA | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 122140135 | PALMITATO DE PALIPERIDONA | ADIUM S.A. | Ativo |
| 122140136 | VEGAPALI | ADIUM S.A. | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos, publicações ou racional mecanístico que sustentem o uso da paliperidona nesta doença; a previsão é apenas do modelo (nível L5).

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (por exemplo, consulta ao DrugBank).
- Informações de segurança da bula na ANVISA (advertências e contraindicações).
- Qualquer evidência pré-clínica ou clínica que ligue a farmacologia da paliperidona à distrofia retiniana antes de reconsiderar a avaliação.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Os dados de suporte — mecanismo de ação, detalhes dos registros e informações de segurança — estão todos ausentes neste pacote de evidências” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “> Para completar esta seção, é necessário re-executar a consulta TFDA/ANVISA com retorno dos campos de produto” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Invega (paliperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7b8e5b26-b9e4-4704-921b-3c3c0d159916) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

