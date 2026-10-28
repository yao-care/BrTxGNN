---
layout: default
title: "Apenas usos conhecidos (sem novas previsões)"
nav_order: 24
permalink: /known-uses/
description: "Para estes medicamentos, todos os candidatos do modelo TxGNN já são usos conhecidos (registrados no grafo de conhecimento ou em um registro sanitário), por…"
---

# Apenas usos conhecidos (sem novas previsões)

Para estes medicamentos, todos os candidatos do modelo TxGNN já são usos conhecidos (registrados no grafo de conhecimento ou em um registro sanitário), portanto não há nova indicação prevista. Cada página lista os usos conhecidos e a situação de comercialização local.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} medicamentos**

| Medicamento | Relatório |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Ver página]({{ drug.url | relative_url }}) |
{% endfor %}
