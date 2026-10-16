---
layout: default
title: Efavirenz
parent: Evidência Moderada (L3-L4)
nav_order: 283
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Efavirenz: nova indicação prevista, Síndrome de imunodeficiência adquirida felina (feline acquired immuno… (nível de evidência L4). Indicação original: Infecção por HIV e AIDS"
---

# Efavirenz
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **3** 
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

# Efavirenz: Da infecção por HIV/AIDS à síndrome de imunodeficiência adquirida felina

## Resumo em Uma Frase

Efavirenz é um inibidor não nucleosídeo da transcriptase reversa (ITRNN), originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que ele possa ser eficaz para a **síndrome de imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)**, uma indicação veterinária, com **0 ensaios clínicos** e **1 publicação** (estudo bioquímico e estrutural in vitro) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV e AIDS |
| Nova Indicação Prevista | Síndrome de imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome) |
| Pontuação de Previsão TxGNN | 99,80% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o efavirenz é um ITRNN que se liga à transcriptase reversa do HIV-1 e bloqueia a replicação viral. Sua eficácia na infecção por HIV está estabelecida, e mecanisticamente poderia ser aplicável a outros lentivírus com transcriptase reversa relacionada.

O vírus da imunodeficiência felina (FIV) é um lentivírus que causa em gatos uma síndrome semelhante à AIDS. Isso explica, em parte, a proximidade entre as duas doenças no grafo de conhecimento. No entanto, o único estudo disponível (PMID 38031646) comparou bioquímica e estruturalmente ITRNNs contra a transcriptase reversa do FIV e do HIV. Os dados compilados indicam que o bolso de ligação dos ITRNNs na enzima felina difere do da enzima do HIV-1, o que pode reduzir a eficácia.

A pontuação elevada do TxGNN provavelmente reflete a semelhança com o HIV, e não uma validação independente. Trata-se de uma indicação veterinária, sem dados in vivo ou clínicos em gatos.

Outras previsões do modelo, sem ensaios clínicos:
- **Infecção pelo vírus da imunodeficiência símia (SIV):** a pontuação é de 99,80%. O SIV selvagem é naturalmente resistente aos ITRNNs, inclusive ao efavirenz. Os estudos em macacos usam o quimérico RT-SHIV (SIV com transcriptase reversa do HIV-1) como modelo de tratamento do HIV, portanto são evidências indiretas, que repetem a indicação original (nível L4).
- **Transtorno do neurodesenvolvimento com marcha atáxica, ausência de fala e redução da substância branca cortical:** a pontuação é de 99,77%. Não há mecanismo, ensaio nem literatura de apoio (nível L5). Os eventos adversos neuropsiquiátricos do efavirenz são uma preocupação adicional nessa população.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Estudo bioquímico/estrutural in vitro | Journal of Veterinary Science | Comparou nevirapina, efavirenz e rilpivirina contra a transcriptase reversa do FIV e do HIV para avaliar o potencial dos ITRNNs no tratamento da infecção felina. Não há tratamento eficaz estabelecido para gatos infectados. |

## Citotoxicidade

Não se aplica: o efavirenz é antirretroviral, não antineoplásico. Esta seção foi omitida.

## Considerações de Segurança

- **Contraindicações indicadas no grafo de conhecimento (não extraídas da bula):** insuficiência hepática, doença hepática, esteatose hepática e esteato-hepatite não alcoólica, hepatite B crônica, hepatite C (aguda e crônica), doença da vesícula biliar, doença renal, síndrome de Fanconi, acidose láctica, epilepsia, transtornos de ansiedade, transtorno neurótico, transtorno distímico, transtorno delirante, esquizofrenia paranoide, hipertrigliceridemia, obesidade (inclusive monogênica), hipofosfatemia, osteomalácia, raquitismo, piureter e fratura patológica (termo obsoleto).
- **Interações medicamentosas:** foram identificadas 100 interações, e o relatório lista as 20 primeiras. Há uma de nível **grave (Major)**, com a **dolasetrona**. As demais são de nível **moderado**, incluindo acarbose, famotidina, rabeprazol, hidrocortisona, dexametasona, betametasona, triancinolona, pioglitazona, loperamida, bupropiona, aprepitanto, bisacodil, ácido quenodesoxicólico, claritromicina, ácido picossulfúrico, polietilenoglicol (3350 com eletrólitos), saxagliptina, dronabinol e minociclina.

Consulte a bula para as advertências e contraindicações oficiais, que não estão disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal é veterinária e se apoia em um único estudo in vitro, que sugere possível menor eficácia na enzima felina. Não há ensaios clínicos nem dados in vivo, e o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) do efavirenz.
- Estudos de atividade antiviral do efavirenz contra o FIV em cultura celular e, depois, em gatos.
- Texto de bula da ANVISA, com advertências e contraindicações, para a triagem de segurança.
- Avaliação regulatória veterinária, pois não há registro do fármaco no Brasil.
- Revisão da relevância das demais previsões (SIV e transtorno do neurodesenvolvimento), cuja evidência é indireta ou inexistente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

