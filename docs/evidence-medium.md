---
layout: default
title: Evidência Moderada (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "55 medicamentos com nível de evidência L3–L4 neste site (Brasil), p. ex. Abatacepte, Acitretin, Beclomethasone Dipropionate, com a nova indicação principal prevista, os registros da ANVISA e as revisões de cada um."
---

# Evidência Moderada (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Esta página lista **{{ site.data.evidence_tier_facts.medium.count }}** dos **{{ site.data.drug_stats.total_drugs }}** medicamentos com relatório publicado neste site ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Proporção mediana em L3–L4 nos 30 sites TxGNN: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Este site está acima da mediana.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Este site está abaixo da mediana.{% else %}Este site está na mediana.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
Nos dados locais (registros da ANVISA), **{{ site.data.evidence_tier_facts.medium.with_current }}** destes medicamentos têm pelo menos um registro ativos, **{{ site.data.evidence_tier_facts.medium.none_current }}** têm registros mas nenhum ativos e **{{ site.data.evidence_tier_facts.medium.without_data }}** não constam dos dados locais. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** têm entradas no registro de revisões (correções de dados regulatórios na página do medicamento). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** têm uma indicação prevista que nenhum outro site TxGNN lista para o mesmo medicamento.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Com registros, mas nenhum ativos: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definição de todos os níveis: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos com evidências preliminares que requerem validação adicional
</p>

---

## Critérios

| Nível | Definição | Significado clínico |
|-------|------------|------------------|
| **L3** | Estudos observacionais / grandes séries de casos | Apoio preliminar; necessita validação adicional |
| **L4** | Estudos pré-clínicos / mecanísticos | Apoio teórico; distante do uso clínico |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} medicamentos)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nível | Nova indicação principal prevista | registros da ANVISA: ativos / total | Registro de revisões | Só neste site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sim ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} medicamentos)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nível | Nova indicação principal prevista | registros da ANVISA: ativos / total | Registro de revisões | Só neste site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sim ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
