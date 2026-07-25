---
layout: default
title: Apenas Predição do Modelo (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidatos L5 no BrTxGNN: apenas predição do modelo, ainda sem evidências clínicas ou de literatura."
---

# Apenas Predição do Modelo (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidatos com apenas predição do modelo e ainda sem evidências em humanos
</p>

---

## Critérios

| Nível | Definição | Significado clínico |
|-------|------------|------------------|
| **L5** | Apenas predição do modelo | Fase de hipótese; ainda sem evidências em humanos |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} medicamentos)

| Medicamento | Indicações | Link |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Ver relatório]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
