---
layout: default
title: Evidência Moderada (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Candidatos a reposicionamento de medicamentos L3-L4 no BrTxGNN, respaldados por evidências observacionais ou pré-clínicas."
---

# Evidência Moderada (L3-L4)

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} medicamentos)

| Medicamento | Indicações | Link |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver relatório]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} medicamentos)

| Medicamento | Indicações | Link |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver relatório]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
