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
| Classes terapêuticas | ~200 |

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
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> é um modelo de aprendizado profundo desenvolvido pelo Zitnik Lab da Harvard Medical School, publicado na <em>Nature Medicine</em>. É o primeiro modelo fundamental projetado para reposicionamento de medicamentos centrado no clínico.
</p>

<blockquote class="expert-quote">
"TxGNN integra um grafo de conhecimento com 17.080 entidades biomédicas, usando redes neurais de grafos para aprender relações complexas entre nós, podendo prever a eficácia potencial de medicamentos para doenças raras."
<cite>— Huang et al., Nature Medicine (2023)</cite>
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
<strong>Aviso Legal / 免責聲明</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. O uso de medicamentos deve seguir orientação médica. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示。
<br><br>
<small>Última revisão / 最後審核：2026-03 | Equipe BrTxGNN</small>
</div>
