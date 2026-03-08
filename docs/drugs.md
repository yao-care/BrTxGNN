---
layout: default
title: Medicamentos
nav_order: 4
description: "Lista de medicamentos analisados pelo BrTxGNN para reposicionamento."
permalink: /drugs/
---

# Medicamentos Analisados

<p class="key-answer" data-question="Quais medicamentos são analisados?">
O BrTxGNN analisa medicamentos registrados na ANVISA que possuem mapeamento para o DrugBank, permitindo previsões de reposicionamento baseadas no modelo TxGNN.
</p>

---

## Estatísticas

| Métrica | Valor |
|---------|-------|
| Total de medicamentos ANVISA | 42.819 |
| Medicamentos ativos | ~17.210 |
| Com mapeamento DrugBank | A calcular |
| Com previsões TxGNN | A calcular |

---

## Como Pesquisar

Você pode pesquisar medicamentos de várias formas:

1. **Por nome** - Nome comercial ou princípio ativo
2. **Por classe terapêutica** - Ex: ANTICOAGULANTES, ANTI-HIPERTENSIVOS
3. **Por indicação** - Doença ou condição prevista

---

## Categorias por Nível de Evidência

### L1 - Evidência Forte
Medicamentos com ≥2 ensaios clínicos Fase 3/4 para indicações previstas.

### L2 - Evidência Moderada
Medicamentos com ensaios Fase 3/4 ou múltiplos ensaios Fase 2.

### L3 - Evidência Inicial
Medicamentos com pelo menos um ensaio clínico registrado.

### L4 - Evidência Pré-clínica
Medicamentos com literatura científica relevante.

### L5 - Apenas Previsão
Previsões do modelo sem evidência externa ainda.

---

## Lista de Medicamentos

<div class="disclaimer">
A lista completa de medicamentos estará disponível após a execução das previsões do modelo TxGNN. Por enquanto, você pode consultar os dados brutos da ANVISA.
</div>

### Classes Terapêuticas Principais

Com base nos dados da ANVISA, as principais classes terapêuticas incluem:

- ANTI-HIPERTENSIVOS
- ANTIDIABÉTICOS
- ANTI-INFLAMATÓRIOS
- ANTIBIÓTICOS
- ANTICOAGULANTES
- ANTIDEPRESSIVOS
- ANALGÉSICOS
- ANTINEOPLÁSICOS

---

## Fontes de Dados

| Fonte | Descrição | Link |
|-------|-----------|------|
| ANVISA | Registro de medicamentos Brasil | [dados.anvisa.gov.br](https://dados.anvisa.gov.br/) |
| DrugBank | Base de dados farmacológicos | [drugbank.com](https://go.drugbank.com/) |
| TxGNN | Modelo de previsão | [Harvard TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) |

---

## Download de Dados

Os dados processados estão disponíveis para download na página [Downloads](/downloads/).
