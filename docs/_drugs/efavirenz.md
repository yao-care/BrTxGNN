---
layout: default
title: Efavirenz
parent: Apenas Predição do Modelo (L5)
nav_order: 283
evidence_level: L5
indication_count: 3
monitor_inn: "EFAVIRENZ"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-20
description: "Efavirenz: nova indicação prevista, síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome) (nível de evidência L5). No Brasil, registros na ANVISA: 6 (ativos: 3)"
---

# Efavirenz
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Efavirenz: inibidor não nucleosídico da transcriptase reversa (ITRNN) → síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumo em Uma Frase

Efavirenz é um inibidor não nucleosídico da transcriptase reversa do HIV-1, usado em esquemas antirretrovirais.
O modelo TxGNN prevê que pode ser eficaz para **síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)**, mas a previsão conta com apenas **1 publicação** (estudo bioquímico e estrutural in vitro) e **nenhum ensaio clínico**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome) |
| Pontuação de Previsão TxGNN | 0,9980 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 6) |
| Número de Registros | 6 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Efavirenz (tradução não oficial): “O efavirenz é um medicamento antiviral. […] O efavirenz é um ITRNN do HIV-1. A atividade do efavirenz é mediada predominantemente pela inibição não competitiva da transcriptase reversa do HIV-1. A transcriptase reversa do HIV-2 e as DNA polimerases celulares humanas α,β, γ e δ não são inibidas pelo efavirenz.” Texto original em inglês: "Efavirenz is an antiviral drug. […] Efavirenz is an NNRTI of HIV-1. Efavirenz activity is mediated predominantly by noncompetitive inhibition of HIV-1 reverse transcriptase. HIV-2 reverse transcriptase and human cellular DNA polymerases α,β, γ, and δ are not inhibited by efavirenz." ([DailyMed: efavirenz prescribing information, Macleods Pharmaceuticals Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13ca3456-e5bf-4bb1-af95-b1378658a358), versão de 2024-06-28; acessado em 2026-11-19). Segundo informações conhecidas, o efavirenz é um inibidor não nucleosídico da transcriptase reversa (ITRNN) que atua sobre a transcriptase reversa do HIV-1. O vírus da imunodeficiência felina (FIV) é um lentivírus com transcriptase reversa relacionada, o que explica, em parte, a pontuação alta do modelo.

Há, porém, um sinal de cautela: a comparação bioquímica e estrutural de ITRNN contra a transcriptase reversa do FIV e do HIV (PMID 38031646) sugere que o bolso de ligação dos ITRNN na enzima felina difere do da enzima do HIV-1, o que pode reduzir a eficácia. A pontuação elevada provavelmente reflete a semelhança com o HIV, e não uma validação independente.

Trata-se ainda de uma indicação veterinária. Não há dados in vivo ou clínicos em gatos, e o estudo disponível não analisa o efavirenz isoladamente com desfechos de eficácia no animal. Por isso, o nível de evidência é L5: o único estudo citado é in vitro e não demonstra benefício na doença em si.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Estudo bioquímico/estrutural in vitro | Journal of Veterinary Science | Compara nevirapina, efavirenz e rilpivirina contra a transcriptase reversa do FIV e do HIV, para avaliar o potencial dos ITRNN no tratamento da infecção felina; não há tratamento eficaz estabelecido para gatos infectados. |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações nos dados compilados. Entre as listadas, a de gravidade maior é com **dolasetrona**. Interações moderadas incluem acarbose, famotidina, rabeprazol, hidrocortisona, pioglitazona, loperamida, bupropiona, aprepitanto, triancinolona, dexametasona, betametasona, bisacodil, ácido quenodesoxicólico, claritromicina, ácido picosulfúrico, polietilenoglicol (3350 com eletrólitos), saxagliptina, dronabinol e minociclina.

Consulte a bula para advertências e contraindicações.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia em um único estudo in vitro, sem ensaios clínicos nem dados em gatos, e o próprio estudo sugere diferenças no sítio de ligação que podem limitar a eficácia. Além disso, a indicação é veterinária.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação do efavirenz
- Estudos de atividade antiviral do efavirenz contra o FIV em cultura celular e, depois, em gatos (eficácia, farmacocinética e segurança)
- Avaliação regulatória e de segurança em medicina veterinária, incluindo os efeitos neuropsiquiátricos conhecidos do fármaco
- Revisão das advertências e contraindicações na bula registrada na ANVISA

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: efavirenz prescribing information, Macleods Pharmaceuticals Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13ca3456-e5bf-4bb1-af95-b1378658a358) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

