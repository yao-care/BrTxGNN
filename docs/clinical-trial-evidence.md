---
layout: default
title: "Medicamentos no Brasil com ensaios para nova indicação"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Medicamentos registrados na ANVISA cuja nova indicação prevista pelo TxGNN tem evidência de ensaios clínicos (L1-L2): indicação, nível e ensaios."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「ver relatório」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Nova Indicação Prevista" | split: "|" -%}
{%- assign lev_labels = "Nível de Evidência" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Medicamentos no Brasil com evidência de ensaios clínicos para uma nova indicação

<p class="key-answer" data-question="Quais medicamentos no Brasil têm evidência de ensaios clínicos para uma nova indicação?">
<strong>{{ trial_drugs.size }}</strong> dos {{ listed.size }} medicamentos com relatório no BrTxGNN têm uma nova indicação prevista pelo TxGNN com nível de evidência <strong>L1 ou L2</strong> ({{ l1.size }} em L1, {{ l2.size }} em L2), ou seja, foram encontradas evidências de ensaios clínicos (ensaios randomizados, ensaios de fase 2–3 ou revisões sistemáticas).
</p>

Os medicamentos vêm de os dados de registro da [ANVISA](https://www.gov.br/anvisa/) (medicamentos registrados no Brasil; a situação de cada registro aparece no relatório do medicamento); a lista reflete os relatórios de medicamentos atualizados pela última vez em {{ latest_date }}.

<div class="key-takeaway">
Evidência de ensaios para uma indicação prevista não comprova eficácia. Todos os candidatos abaixo ainda <strong>requerem validação clínica</strong> e avaliação regulatória antes de qualquer uso clínico.
</div>

---

## Medicamentos com evidência de ensaios (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Medicamento</th><th>Nova indicação prevista</th><th>Nível de evidência</th><th>Ensaios registrados citados (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}ver relatório{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(com ressalva)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Como ler esta lista

- **Nível de evidência** segue os [critérios]({{ '/evidence-high/' | relative_url }}) do site: L1 = Múltiplos ECRs de Fase 3 / revisões sistemáticas; L2 = Um único ECR ou múltiplos ensaios de Fase 2. «(com ressalva)» indica que o relatório faz uma ressalva sobre o nível; leia a nota do relatório antes de se basear nele.
- **Nova indicação prevista** é a previsão principal de cada relatório. As indicações e contraindicações já registradas no grafo de conhecimento do TxGNN são excluídas, mas algumas previsões ainda podem coincidir com um uso já estabelecido; o relatório explica isso quando se aplica.
- **Ensaios registrados citados** conta os números do ClinicalTrials.gov (NCT) citados no relatório. Os relatórios citam uma seleção dos ensaios encontrados; 0 significa que o relatório não cita nenhum ensaio registrado, e a seção de evidências da literatura mostra a base do nível.
- Para todos os níveis e o método completo, veja [Evidência Alta (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Medicamentos]({{ '/drugs/' | relative_url }}) e a [metodologia]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. Siga sempre as orientações do seu médico; nunca ajuste a medicação por conta própria. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>
