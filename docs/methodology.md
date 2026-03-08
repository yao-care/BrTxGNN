---
layout: default
title: Metodologia
nav_order: 5
description: "Metodologia técnica do BrTxGNN para previsão de reposicionamento de medicamentos."
permalink: /methodology/
---

# Metodologia

<div class="key-takeaway">
O BrTxGNN utiliza o modelo TxGNN de Harvard combinado com dados regulatórios brasileiros (ANVISA) para prever novas indicações terapêuticas.
</div>

---

## Visão Geral do Pipeline

```
ANVISA → DrugBank → TxGNN → Evidências → Relatórios
```

### 1. Coleta de Dados ANVISA

Coletamos dados de medicamentos registrados na ANVISA:

| Campo | Descrição |
|-------|-----------|
| NUMERO_REGISTRO_PRODUTO | Número de registro |
| NOME_PRODUTO | Nome comercial |
| PRINCIPIO_ATIVO | Ingrediente ativo |
| CLASSE_TERAPEUTICA | Classe terapêutica |
| SITUACAO_REGISTRO | Status (Ativo/Inativo) |

### 2. Mapeamento DrugBank

Mapeamos os princípios ativos da ANVISA para identificadores do DrugBank:

1. **Normalização** - Padronização de nomes de ingredientes
2. **Matching** - Correspondência com vocabulário DrugBank
3. **Validação** - Verificação de correspondências

### 3. Previsão TxGNN

O modelo TxGNN utiliza:

- **Grafo de Conhecimento**: 17.080 entidades biomédicas
- **Tipos de Nós**: Medicamentos, doenças, genes, proteínas
- **Tipos de Arestas**: Interações, indicações, efeitos adversos

<blockquote class="expert-quote">
"TxGNN é um modelo de rede neural de grafos que aprende representações de medicamentos e doenças a partir de um grafo de conhecimento biomédico, permitindo prever novas associações terapêuticas."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### 4. Coleta de Evidências

Para cada previsão, coletamos evidências de:

| Fonte | API/Método | Dados |
|-------|------------|-------|
| ClinicalTrials.gov | REST API v2 | Ensaios clínicos |
| PubMed | Entrez E-utilities | Literatura científica |
| ANVISA | Dados abertos | Status regulatório |
| DrugBank | Vocabulário | Informações farmacológicas |

### 5. Classificação de Evidências

Classificamos em 5 níveis:

| Nível | Critérios |
|-------|-----------|
| L1 | ≥2 ensaios Fase 3/4 |
| L2 | ≥1 ensaio Fase 3/4 ou ≥2 ensaios Fase 2 |
| L3 | ≥1 ensaio clínico |
| L4 | ≥1 artigo científico |
| L5 | Apenas previsão TxGNN |

---

## Modelo TxGNN

### Arquitetura

O TxGNN é composto por:

1. **Encoder de Grafo** - Aprende representações de nós
2. **Decoder de Links** - Prevê novas arestas
3. **Módulo de Confiança** - Estima incerteza

### Treinamento

- **Dados**: Grafo de conhecimento biomédico
- **Tarefa**: Predição de links
- **Validação**: Hold-out temporal

### Métricas de Desempenho

O modelo original reporta:

| Métrica | Valor |
|---------|-------|
| AUROC | 0.91 |
| AUPRC | 0.85 |

---

## Validação

### Validação Interna

1. **Cross-validation** - Divisão temporal dos dados
2. **Backtesting** - Previsão de indicações conhecidas

### Validação Externa

1. **ClinicalTrials.gov** - Verificação de ensaios em andamento
2. **PubMed** - Revisão de literatura
3. **Aprovações regulatórias** - Novas indicações aprovadas

---

## Limitações

<div class="disclaimer">
<strong>Limitações Importantes</strong>
<ul>
<li>O modelo foi treinado com dados internacionais, não específicos para o Brasil</li>
<li>Previsões não consideram aspectos farmacoeconômicos locais</li>
<li>Dados da ANVISA podem ter atrasos em relação a aprovações recentes</li>
<li>Não substitui validação clínica rigorosa</li>
</ul>
</div>

---

## Referências

1. Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*. [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

2. ANVISA. Dados Abertos de Medicamentos. [dados.anvisa.gov.br](https://dados.anvisa.gov.br/)

3. Wishart, D.S., et al. (2018). DrugBank 5.0. *Nucleic Acids Research*.
