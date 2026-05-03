---
layout: default
title: Estazolam
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Estazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Estazolam: De hipnótico de curto prazo à Insônia

## Resumo em Uma Frase

Estazolam é um triazolobenzodiazepínico aprovado para o tratamento de curto prazo da insônia, atuando no sistema GABAérgico central. O modelo TxGNN prevê que pode ser eficaz para **Insônia (Insomnia Disease)** — indicação que coincide com a sua própria aprovação regulatória, configurando uma validação computacional da indicação estabelecida e não um cenário clássico de reposicionamento. Atualmente, há **0 ensaios clínicos** registrados no ClinicalTrials.gov e **18 publicações** na literatura apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Tratamento de curto prazo da insônia (hipnótico) |
| Nova Indicação Prevista | Insônia (Insomnia Disease) |
| Pontuação de Previsão TxGNN | 99,48% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 7 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Estazolam é um triazolobenzodiazepínico que se liga ao sítio específico das benzodiazepinas no receptor GABA-A, potencializando a entrada de íons Cl⁻ na célula e reduzindo a excitabilidade dos neurônios do sistema nervoso central. Na prática clínica, este mecanismo se traduz em encurtamento da latência para início do sono, aumento do tempo total de sono, redução dos despertares noturnos e melhora da qualidade subjetiva do sono — exatamente os parâmetros avaliados nos ensaios clínicos históricos do fármaco.

É fundamental destacar que, neste caso, o modelo TxGNN prediz a **insônia** como principal indicação candidata — que corresponde precisamente à **indicação já aprovada pelo FDA** para o estazolam (tratamento de curto prazo da insônia). Portanto, este não é um cenário clássico de reposicionamento de fármaco. O campo `original_indications` do Evidence Pack encontra-se vazio por lacuna de dados (DG001/DG002), mas o próprio `repurposing_rationale` confirma que se trata de uma validação da indicação estabelecida.

A alta pontuação TxGNN (99,48%) para a indicação original reflete a robustez do modelo em identificar associações bem fundamentadas. Esse resultado fornece confiança metodológica e serve de base para avaliar as previsões de rank 2 em diante (epilepsia visual, delirium de abstinência alcoólica), estas sim representando oportunidades genuínas de reposicionamento a explorar.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados no ClinicalTrials.gov ou ICTRP para a combinação Estazolam + Insônia.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | RCT (multicêntrico) | American Journal of Medicine | Estazolam 1,0 mg e 2,0 mg melhoram significativamente latência do sono, tempo total, despertares noturnos e qualidade do sono em adultos com insônia crônica; eficácia sustentada por ≥6 semanas de uso contínuo |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | RCT (acupuntura + estazolam) | Acupuncture Research | Terapia de agulha superficial combinada com estazolam mostrou eficácia clínica superior na insônia por padrão de estagnação hepática, com redução de ACTH e cortisol como biomarcadores do mecanismo de ação |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | RCT | Chinese Acupuncture & Moxibustion | Acupuntura baseada em diferenciação de síndromes comparada ao estazolam no tratamento de insônia crônica; avaliou também impacto na função cognitiva |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revisão (guia terapêutico) | Medical Letter on Drugs | Revisão abrangente de hipnóticos disponíveis para insônia crônica, incluindo benzodiazepinas como o estazolam, com perfis de eficácia e segurança comparados |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Revisão sistemática | Integrative Medicine Research | Mais de 20% dos adultos com insônia apresentam dor crônica associada (ICCP); revisa abordagens transdiagnósticas com medicina herbal e acupuntura |
| [31013432](https://pubmed.ncbi.nlm.nih.gov/31013432/) | 2019 | Revisão sistemática / Meta-análise | J Alternative & Complementary Medicine | Revisão atualizada de ECAs sobre eficácia da acupuntura para insônia primária, com busca em 11 bases de dados (jan/2008–out/2017) |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Observação clínica controlada | Chinese Acupuncture & Moxibustion | Baduanjin + acupressão auricular versus estazolam oral para insônia em pacientes com COVID-19; comparou efeito terapêutico sobre tratamento convencional |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Estudo transversal | Medicine | Prevalência e fatores associados à insônia em sobreviventes de COVID-19 (dez/2022–fev/2023), avaliada pelo Insomnia Severity Index (ISI) |
| [40827342](https://pubmed.ncbi.nlm.nih.gov/40827342/) | 2025 | Estudo transversal retrospectivo | Psychiatry & Clinical Psychopharmacology | Padrões de uso de medicamentos para insônia em hospital de medicina integrativa em Shenzhen; avalia racionalidade da prescrição na prática real |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Análise de mundo real | China Journal of Chinese Materia Medica | Análise de comorbidades e uso concomitante de medicamentos em 1.067 pacientes com insônia em 20 hospitais; comorbidades mais frequentes: hipertensão (26,9%), insuficiência cerebrovascular (24,93%) |

---

## Informações de Comercialização no Brasil

O estazolam possui **7 registros** com situação **Comercializado**. Os dados individuais de cada registro (número, nome comercial, forma farmacêutica, indicação aprovada) não foram recuperados nesta extração. Consulte a base de dados da ANVISA para informações completas dos registros vigentes.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A previsão TxGNN para insônia coincide com a indicação já aprovada pelo FDA e respaldada por múltiplos ECAs publicados desde 1990, justificando o nível de evidência L1. O principal guardrail é a ausência de dados de segurança estruturados no presente Evidence Pack (advertências, contraindicações e interações medicamentosas ainda não recuperados).

**Para prosseguir, é necessário:**
- Acessar a bula ANVISA para recuperar advertências, contraindicações e precauções especiais (DG001 — Blocking)
- Consultar a API do DrugBank para dados completos de mecanismo de ação (DG002 — High)
- Recuperar os detalhes individuais dos 7 registros ANVISA (número, nome comercial, forma farmacêutica, indicação aprovada)
- Avaliar as previsões de rank 2 (epilepsia visual — L4) e rank 3 (delirium de abstinência alcoólica — L4) como candidatos genuínos a reposicionamento, dado que o estazolam possui mecanismo GABAérgico potencialmente aplicável a ambas as condições
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

