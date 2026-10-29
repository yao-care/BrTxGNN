---
layout: default
title: Medicamentos
nav_order: 4
description: "Lista de medicamentos analisados pelo BrTxGNN para reposicionamento."
permalink: /drugs/
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}

# Medicamentos Analisados

<p class="key-answer" data-question="Quais medicamentos são analisados?">
O BrTxGNN analisa medicamentos registrados na ANVISA que possuem mapeamento para o DrugBank, permitindo previsões de reposicionamento baseadas no modelo TxGNN.
</p>

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
Esta lista baseia-se nos dados de registro de [ANVISA](https://www.gov.br/anvisa/) (Brasil).

<!-- local-home:end -->

## Estatísticas

| Métrica | Valor |
|---------|-------|
| Total de medicamentos ANVISA | 42.819 |
| Medicamentos ativos | ~17.210 |
| Com mapeamento DrugBank | A calcular |
| Com previsões TxGNN | {{ listed_drugs.size }} |

---

## Como Pesquisar

Você pode pesquisar medicamentos de várias formas:

1. **Por nome** - Nome comercial ou princípio ativo
2. **Por classe terapêutica** - Ex: ANTICOAGULANTES, ANTI-HIPERTENSIVOS
3. **Por indicação** - Doença ou condição prevista

---

## Categorias por Nível de Evidência

### L1 - Evidência Forte
Medicamentos com ≥2 ensaios clínicos Fase 3/4 para indicações previstas.

### L2 - Evidência Moderada
Medicamentos com ensaios Fase 3/4 ou múltiplos ensaios Fase 2.

### L3 - Evidência Inicial
Medicamentos com pelo menos um ensaio clínico registrado.

### L4 - Evidência Pré-clínica
Medicamentos com literatura científica relevante.

### L5 - Apenas Previsão
Previsões do modelo sem evidência externa ainda.

---

## Lista de Medicamentos

<div class="disclaimer">
A lista completa de medicamentos estará disponível após a execução das previsões do modelo TxGNN. Por enquanto, você pode consultar os dados brutos da ANVISA.
</div>

### Classes Terapêuticas Principais

Com base nos dados da ANVISA, as principais classes terapêuticas incluem:

- ANTI-HIPERTENSIVOS
- ANTIDIABÉTICOS
- ANTI-INFLAMATÓRIOS
- ANTIBIÓTICOS
- ANTICOAGULANTES
- ANTIDEPRESSIVOS
- ANALGÉSICOS
- ANTINEOPLÁSICOS

---

## Fontes de Dados

| Fonte | Descrição | Link |
|-------|-----------|------|
| ANVISA | Registro de medicamentos Brasil | [dados.anvisa.gov.br](https://dados.anvisa.gov.br/) |
| DrugBank | Base de dados farmacológicos | [drugbank.com](https://go.drugbank.com/) |
| TxGNN | Modelo de previsão | [Harvard TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) |

---

## Download de Dados

Os dados processados estão disponíveis para download na página [Downloads](/downloads/).

---

## Lista completa de medicamentos

{{ listed_drugs.size }} relatórios de medicamentos

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Medicamento | Nível de evidência | Indicações |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}
