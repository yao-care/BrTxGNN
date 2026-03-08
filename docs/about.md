---
layout: default
title: Sobre o Projeto
nav_order: 2
description: "BrTxGNN é uma plataforma de predição de reposicionamento de medicamentos baseada no modelo TxGNN de Harvard, focada em medicamentos registrados na ANVISA do Brasil."
permalink: /about/
---

# Sobre o Projeto

<div class="key-takeaway">
Usando IA para acelerar a validação de evidências de reposicionamento de medicamentos.
</div>

---

## Contexto do Projeto

<p class="key-answer" data-question="O que é BrTxGNN?">
<strong>BrTxGNN</strong> é uma plataforma de pesquisa de reposicionamento de medicamentos (Drug Repurposing), baseada no modelo TxGNN publicado na <em>Nature Medicine</em> pelo Zitnik Lab de Harvard, focada em medicamentos aprovados pela ANVISA no Brasil.
</p>

---

## Equipe e Autores

| Item | Informação |
|------|-----------|
| Manutenção | Yao.Care |
| Base do Modelo | Harvard TxGNN (Zitnik Lab) |
| Última Atualização | Março 2026 |

### Base Acadêmica

Este projeto é baseado no seguinte artigo:

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## O que é Reposicionamento de Medicamentos?

<p class="key-answer" data-question="O que é reposicionamento de medicamentos?">
<strong>Reposicionamento de medicamentos (Drug Repurposing)</strong> refere-se à descoberta de novos usos terapêuticos para medicamentos existentes. Comparado ao desenvolvimento de novos medicamentos que requer 10-15 anos e US$ 1-2 bilhões, o reposicionamento requer apenas 3-5 anos e US$ 100-300 milhões, com dados de segurança humana já disponíveis e menor risco de falha.
</p>

<table class="comparison-table">
<thead>
<tr><th>Comparação</th><th>Novo Medicamento</th><th>Reposicionamento</th></tr>
</thead>
<tbody>
<tr><td>Tempo de desenvolvimento</td><td>10-15 anos</td><td>3-5 anos</td></tr>
<tr><td>Custo</td><td>US$ 1-2 bilhões</td><td>US$ 100-300 milhões</td></tr>
<tr><td>Dados de segurança</td><td>Necessário estabelecer</td><td>Já disponíveis</td></tr>
<tr><td>Risco de falha</td><td>Muito alto (>90%)</td><td>Menor</td></tr>
</tbody>
</table>

---

## O que é TxGNN?

<p class="key-answer" data-question="O que é TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> é um modelo de aprendizado profundo desenvolvido pela equipe do Zitnik Lab da Harvard Medical School, publicado na <em>Nature Medicine</em>, projetado especificamente para prever novas associações entre medicamentos e doenças.
</p>

<blockquote class="expert-quote">
"TxGNN integra um grafo de conhecimento com 17.080 entidades biomédicas, usando redes neurais de grafos para aprender relações complexas entre nós, podendo prever a eficácia potencial de medicamentos para doenças raras."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### Características Técnicas

<ol class="actionable-steps">
<li><strong>Grafo de Conhecimento</strong>: Integra 17.080 nós incluindo medicamentos, doenças, genes e proteínas</li>
<li><strong>Rede Neural de Grafos</strong>: Aprende relações complexas entre nós</li>
<li><strong>Capacidade de Previsão</strong>: Prevê para quais doenças um medicamento pode ser eficaz</li>
</ol>

---

## Fontes de Dados

<p class="key-answer" data-question="Quais são as fontes de dados do BrTxGNN?">
A plataforma integra múltiplas fontes de dados públicas, incluindo previsões de IA, ensaios clínicos, literatura acadêmica, informações de medicamentos e registro brasileiro ANVISA.
</p>

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fonte</th><th>Descrição</th></tr>
</thead>
<tbody>
<tr><td>Previsão IA</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Modelo de previsão de Harvard</td></tr>
<tr><td>Ensaios Clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Registro global de ensaios clínicos</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Base de literatura biomédica</td></tr>
<tr><td>Medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Base de dados de medicamentos</td></tr>
<tr><td>Registro Brasil</td><td><a href="https://dados.anvisa.gov.br/">ANVISA</a></td><td>Dados abertos da ANVISA</td></tr>
</tbody>
</table>

---

## Escala do Projeto

| Item | Quantidade |
|------|-----------|
| Medicamentos ANVISA | 42.819 |
| Medicamentos Ativos | 17.210 |
| Categorias Regulatórias | 9 |

---

## Contato e Feedback

Para perguntas ou sugestões, entre em contato através dos seguintes canais:

- **GitHub Issues**: [https://github.com/yao-care/BrTxGNN/issues](https://github.com/yao-care/BrTxGNN/issues)
- **Página do Projeto**: [https://brtxgnn.yao.care/](https://brtxgnn.yao.care/)

---

<div class="disclaimer">
<strong>Aviso Legal / 免責聲明</strong><br>
Este relatório é apenas para fins de pesquisa acadêmica e <strong>não constitui aconselhamento médico</strong>. O uso de medicamentos deve seguir orientação médica. Qualquer decisão de reposicionamento de medicamentos requer validação clínica completa e aprovação regulatória.
<br><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。
<br><br>
<small>Última revisão / 最後審核：2026-03 | Equipe BrTxGNN</small>
</div>
