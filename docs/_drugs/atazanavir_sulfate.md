---
layout: default
title: Atazanavir Sulfate
parent: Apenas Predição do Modelo (L5)
nav_order: 83
evidence_level: L5
indication_count: 4
drugbank_id: DB01072
monitor_inn: "Atazanavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-20
description: "Atazanavir Sulfate: nova indicação prevista, Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection) (nível de evidência L5)."
---

# Atazanavir Sulfate
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

## Atazanavir Sulfate: Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection)
{: .text-alpha }

## Resumo em Uma Frase

Atazanavir (sulfato de atazanavir) é um antiviral inibidor de protease, registrado no Brasil como antirretroviral.
O modelo TxGNN prevê que pode ser eficaz para **infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection)**, mas há apenas **1 publicação** (estudo pré-clínico em macacos) e **nenhum ensaio clínico** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTIVIROTICOS (INIBE REPLICACAO VIROTICA) |
| Nova Indicação Prevista | Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection) |
| Pontuação de Previsão TxGNN | 0.9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Atazanavir Sulfate (tradução não oficial): “O atazanavir é um fármaco antirretroviral contra o HIV-1. […] O atazanavir (ATV) é um inibidor da protease (IP) do HIV-1 do tipo azapeptídeo. O composto inibe seletivamente o processamento vírus-específico das poliproteínas virais Gag e Gag-Pol em células infectadas pelo HIV-1, impedindo assim a formação de vírions maduros.” Texto original em inglês: "Atazanavir is an HIV-1 antiretroviral drug. […] Atazanavir (ATV) is an azapeptide HIV-1 protease inhibitor (PI). The compound selectively inhibits the virus-specific processing of viral Gag and Gag-Pol polyproteins in HIV-1-infected cells, thus preventing formation of mature virions." ([DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8), versão de 2024-12-05; acessado em 2026-11-19). Sabe-se que o atazanavir é um inibidor da protease do HIV-1. O vírus da imunodeficiência símia (SIV) é um parente lentiviral próximo do HIV e codifica uma protease homóloga, de modo que a inibição é biologicamente plausível.

A única publicação disponível (2010) é um estudo em macacos tratados com terapia antirretroviral altamente ativa (HAART), que mostrou menor replicação viral e inflamação no sistema nervoso central, mas persistência de DNA viral. Esse estudo avalia um esquema combinado, e não isola a contribuição do atazanavir. Trata-se de um modelo animal do HIV, e não de uma nova indicação para uso humano.

Por isso, embora a pontuação do modelo seja alta, o nível de evidência é L5: nenhuma das fontes citadas estuda o atazanavir isoladamente nessa doença.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Estudo pré-clínico em animais | The Journal of Infectious Diseases | Macacos infectados por SIV e tratados com HAART tiveram menor replicação viral e inflamação no sistema nervoso central, mas o DNA viral persistiu |

Não há ensaios clínicos registrados relacionados a esta previsão.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 110630133 | Sulfato de Atazanavir | Não informada | Antivirótico (inibe a replicação viral) |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se em um único estudo em macacos com esquema combinado, sem ensaios clínicos, e trata de um modelo animal do HIV, não de uma nova indicação humana.

**Para prosseguir, é necessário:**
- Estudos que avaliem o atazanavir isoladamente no modelo de SIV
- Dados do mecanismo de ação e da bula (advertências e contraindicações)
- Definição clara da relevância da indicação (veterinária/pré-clínica) para o contexto regulatório brasileiro

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Foram identificadas **lacunas críticas de dados** — incluindo ausência de registros regulatórios brasileiros e de mecanismo de ação document” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “e o fármaco não possui registros ativos na base de dados regulatória consultada — impossibilitando qualquer análise de indicação original, m” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

