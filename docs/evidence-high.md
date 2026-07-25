---
layout: default
title: Evidência Alta (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidatos a reposicionamento de medicamentos L1-L2 no BrTxGNN, apoiados por ensaios clínicos ou revisões sistemáticas."
---

# Evidência Alta (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos que podem ser priorizados para avaliação clínica
</p>

---

## Critérios

| Nível | Definição | Significado clínico |
|-------|------------|------------------|
| **L1** | Múltiplos ECRs de Fase 3 / revisões sistemáticas | Apoio forte; o uso clínico pode ser considerado |
| **L2** | Um único ECR ou múltiplos ensaios de Fase 2 | Apoio moderado; ensaios de validação podem ser planejados |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

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
