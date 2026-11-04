---
layout: default
title: Reposicionamento de Medicamentos
nav_order: 1
description: "BrTxGNN - Sistema de predição de reposicionamento de medicamentos para o Brasil usando IA. Previsões baseadas no modelo TxGNN de Harvard."
permalink: /
image: /assets/images/og-default.png
---

# Reposicionamento de Medicamentos com IA

<p class="key-answer" data-question="O que é o BrTxGNN?">
<strong>BrTxGNN</strong> é uma plataforma de predição de reposicionamento de medicamentos baseada no modelo TxGNN de Harvard. Analisamos medicamentos registrados na ANVISA para identificar potenciais novas indicações terapêuticas.
</p>

<div class="key-takeaway">
Usando inteligência artificial para descobrir novos usos para medicamentos existentes, acelerando a pesquisa e desenvolvimento de tratamentos.
</div>

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Brasil: o que este site abrange

Este site publica relatórios de **{{ site.data.drug_stats.total_drugs }}** medicamentos que constam nos dados de registro de [ANVISA](https://www.gov.br/anvisa/) (Brasil).

Conjunto de dados: [ANVISA: DADOS_ABERTOS_MEDICAMENTOS.csv](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv); é baixado e comparado automaticamente toda semana (às segundas-feiras). Detalhes: [Fontes de Dados]({{ '/sources/' | relative_url }}).

Relatórios por nível de evidência:

| Nível de evidência | Relatórios | Proporção |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

12 pares medicamento–doença previstos neste site não aparecem em nenhum outro dos 30 sites TxGNN.

### Medicamentos com maior nível de evidência neste site

| Medicamento | Nível de evidência |
|---|---|
| [Busulfan](/drugs/busulfan/) | L1 |
| [Potassium](/drugs/potassium/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Acetylcysteine](/drugs/acetylcysteine/) | L2 |
| [Diazepam](/drugs/diazepam/) | L2 |
| [Ledipasvir](/drugs/ledipasvir/) | L2 |
| [Polidocanol](/drugs/polidocanol/) | L2 |
| [Clozapine](/drugs/clozapine/) | L2 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L2 |

### Medicamentos abrangidos apenas por este site entre os 30 sites TxGNN

| Medicamento | Nível de evidência |
|---|---|
| [Clobutinol](/drugs/clobutinol/) | L5 |
| [Cobalamin](/drugs/cobalamin/) | L5 |
| [Cefdinir](/drugs/cefdinir/) | N/A |
| [Metaraminol](/drugs/metaraminol/) | N/A |
| [Nimesulide](/drugs/nimesulide/) | N/A |
| [Potassium Hydroxide](/drugs/potassium-hydroxide/) | N/A |
| [Potassium Sulfate](/drugs/potassium-sulfate/) | N/A |

<!-- local-home:end -->

## O que é Reposicionamento de Medicamentos?

<p class="key-answer" data-question="O que é reposicionamento de medicamentos?">
<strong>Reposicionamento de medicamentos (Drug Repurposing)</strong> é a descoberta de novas indicações terapêuticas para medicamentos já aprovados. Esta abordagem reduz significativamente o tempo e custo de desenvolvimento comparado ao desenvolvimento de novos medicamentos.
</p>

| Comparação | Novo Medicamento | Reposicionamento |
|-----------|-----------------|------------------|
| Tempo de desenvolvimento | 10-15 anos | 3-5 anos |
| Custo estimado | US$ 1-2 bilhões | US$ 100-300 milhões |
| Dados de segurança | Necessário estabelecer | Já disponíveis |
| Risco de falha | Muito alto (>90%) | Menor |

---

## Estatísticas do Sistema

| Item | Quantidade |
|------|-----------|
| Medicamentos ANVISA | 42.819 |
| Medicamentos ativos | 17.210 |
| Classes terapêuticas | 493 |

---

## Fontes de Dados

<p class="key-answer" data-question="Quais são as fontes de dados do BrTxGNN?">
A plataforma integra múltiplas fontes de dados públicas autorizadas para garantir a rastreabilidade e valor acadêmico das previsões.
</p>

| Tipo de Dados | Fonte | Descrição |
|--------------|-------|-----------|
| Previsão IA | [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) | Modelo de Harvard |
| Ensaios Clínicos | [ClinicalTrials.gov](https://clinicaltrials.gov/) | Registro global |
| Literatura | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Base biomédica |
| Medicamentos | [DrugBank](https://go.drugbank.com/) | Base de medicamentos |
| Registro Brasil | [ANVISA](https://dados.anvisa.gov.br/) | Dados abertos ANVISA |

---

## Sobre o TxGNN

<p class="key-answer" data-question="O que é TxGNN?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> é um modelo de aprendizado profundo desenvolvido pelo Zitnik Lab da Harvard Medical School, publicado na <em>Nature Medicine</em>. É o primeiro modelo fundamental projetado para reposicionamento de medicamentos centrado no clínico.
</p>

<blockquote class="expert-quote">
"TxGNN integra um grafo de conhecimento que abrange 17.080 doenças, usando redes neurais de grafos para aprender relações complexas entre nós, podendo prever a eficácia potencial de medicamentos para doenças raras."
<cite>— Huang et al., Nature Medicine (2024)</cite>
</blockquote>

---

## Navegação Rápida

| Categoria | Descrição | Link |
|-----------|-----------|------|
| **Sobre** | Informações do projeto | [Ver mais]({{ '/about/' | relative_url }}) |
| **FHIR API** | Recursos FHIR | [API]({{ '/fhir/metadata' | relative_url }}) |
| **SMART App** | Aplicação SMART on FHIR | [Lançar]({{ '/smart/launch.html' | relative_url }}) |
| **GitHub** | Código fonte | [Repositório](https://github.com/yao-care/BrTxGNN) |

---

<div class="disclaimer">
<strong>Aviso Legal</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. O uso de medicamentos deve seguir orientação médica. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
<small>Última revisão: 2026-03 | Equipe BrTxGNN</small>
</div>

---

## Sobre o Desenvolvedor

Esta plataforma é desenvolvida e operada pela **藥提醒科技有限公司** (yao.care). Veja a página <a href="{{ '/about/' | relative_url }}">Sobre o Projeto</a> para o histórico completo da empresa e da metodologia.
