---
layout: default
title: Evidência Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "29 medicamentos com nível de evidência L1–L2 neste site (Brasil), p. ex. Atorvastatin Calcium, Bendamustina Hydrochloride, Busulfan, com a nova indicação principal prevista, os registros da ANVISA e as revisões de cada um."
---

# Evidência Alta (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Esta página lista **{{ site.data.evidence_tier_facts.high.count }}** dos **{{ site.data.drug_stats.total_drugs }}** medicamentos com relatório publicado neste site ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Proporção mediana em L1–L2 nos 30 sites TxGNN: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Este site está acima da mediana.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Este site está abaixo da mediana.{% else %}Este site está na mediana.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
Nos dados locais (registros da ANVISA), **{{ site.data.evidence_tier_facts.high.with_current }}** destes medicamentos têm pelo menos um registro ativos, **{{ site.data.evidence_tier_facts.high.none_current }}** têm registros mas nenhum ativos e **{{ site.data.evidence_tier_facts.high.without_data }}** não constam dos dados locais. **{{ site.data.evidence_tier_facts.high.with_reviews }}** têm entradas no registro de revisões (correções de dados regulatórios na página do medicamento). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** têm uma indicação prevista que nenhum outro site TxGNN lista para o mesmo medicamento.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Com registros, mas nenhum ativos: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definição de todos os níveis: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} medicamentos)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nível | Nova indicação principal prevista | registros da ANVISA: ativos / total | Registro de revisões | Só neste site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sim ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} medicamentos)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nível | Nova indicação principal prevista | registros da ANVISA: ativos / total | Registro de revisões | Só neste site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sim ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
