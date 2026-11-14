---
layout: default
title: Evidência Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidatos a reposicionamento de medicamentos L1-L2 no BrTxGNN, apoiados por ensaios clínicos ou revisões sistemáticas."
---

# Evidência Alta (L1-L2)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
Esta página lista **{{ pd_m }}** dos **{{ site.data.drug_stats.total_drugs }}** medicamentos com relatório publicado neste site ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Definição dos níveis: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos que podem ser priorizados para avaliação clínica
</p>

Quais destes medicamentos têm evidência de ensaios para a nova indicação prevista e quantos ensaios registrados são citados? Veja [Medicamentos no Brasil com evidência de ensaios clínicos para uma nova indicação]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Critérios

| Nível | Definição | Significado clínico |
|-------|------------|------------------|
| **L1** | Múltiplos ECRs de Fase 3 / revisões sistemáticas | Apoio forte; o uso clínico pode ser considerado |
| **L2** | Um único ECR ou múltiplos ensaios de Fase 2 | Apoio moderado; ensaios de validação podem ser planejados |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ l1_drugs.size }} medicamentos)

| Medicamento | Indicações | Link |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver relatório]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} medicamentos)

| Medicamento | Indicações | Link |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver relatório]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
