---
layout: default
title: Apenas Predição do Modelo (L5)
nav_order: 23
permalink: /evidence-low/
description: "437 medicamentos com nível de evidência L5 neste site (Brasil), p. ex. Metamizole, Amoxicillin, Diclofenac, com a nova indicação principal prevista, os registros da ANVISA e as revisões de cada um."
---

# Apenas Predição do Modelo (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Esta página lista **{{ site.data.evidence_tier_facts.low.count }}** dos **{{ site.data.drug_stats.total_drugs }}** medicamentos com relatório publicado neste site ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Proporção mediana em L5 nos 30 sites TxGNN: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Este site está acima da mediana.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Este site está abaixo da mediana.{% else %}Este site está na mediana.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
Nos dados locais (registros da ANVISA), **{{ site.data.evidence_tier_facts.low.with_current }}** destes medicamentos têm pelo menos um registro ativos, **{{ site.data.evidence_tier_facts.low.none_current }}** têm registros mas nenhum ativos e **{{ site.data.evidence_tier_facts.low.without_data }}** não constam dos dados locais. **{{ site.data.evidence_tier_facts.low.with_reviews }}** têm entradas no registro de revisões (correções de dados regulatórios na página do medicamento). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** têm uma indicação prevista que nenhum outro site TxGNN lista para o mesmo medicamento.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Com registros, mas nenhum ativos: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Os medicamentos com registro local ativos aparecem primeiro.
{% endif %}

Definição de todos os níveis: [Metodologia]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos com apenas predição do modelo e ainda sem evidências em humanos
</p>

---

## Critérios

| Nível | Definição | Significado clínico |
|-------|------------|------------------|
| **L5** | Apenas predição do modelo | Fase de hipótese; ainda sem evidências em humanos |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} medicamentos)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Medicamento | Nível | Nova indicação principal prevista | registros da ANVISA: ativos / total | Registro de revisões | Só neste site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}sim ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
