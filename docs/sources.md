---
layout: default
title: Fontes de Dados
nav_order: 6
description: "Fontes de dados utilizadas pelo BrTxGNN para previsões de reposicionamento."
permalink: /sources/
---

# Fontes de Dados

<div class="key-takeaway">
O BrTxGNN integra múltiplas fontes de dados públicas para garantir a rastreabilidade e valor científico das previsões.
</div>

---

## Fontes Primárias

### TxGNN (Harvard)

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Modelo de previsão de IA |
| **Fonte** | Zitnik Lab, Harvard Medical School |
| **Dados** | Grafo de conhecimento biomédico |
| **Entidades** | 17.080 nós (medicamentos, doenças, genes) |
| **Relações** | ~80.000 arestas |
| **Link** | [zitniklab.hms.harvard.edu/projects/TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) |

### ANVISA

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Registro regulatório |
| **Fonte** | Agência Nacional de Vigilância Sanitária |
| **Dados** | Medicamentos registrados no Brasil |
| **Registros** | ~42.000 medicamentos |
| **Atualização** | Semanal |
| **Link** | [dados.anvisa.gov.br](https://dados.anvisa.gov.br/) |

---

## Fontes de Evidência

### ClinicalTrials.gov

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Registro de ensaios clínicos |
| **Fonte** | NIH (EUA) |
| **Dados** | Ensaios clínicos globais |
| **API** | REST API v2 |
| **Link** | [clinicaltrials.gov](https://clinicaltrials.gov/) |

**Uso**: Verificamos se existem ensaios clínicos para as combinações medicamento-doença previstas.

### PubMed

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Literatura científica |
| **Fonte** | NCBI (EUA) |
| **Dados** | Artigos biomédicos |
| **API** | Entrez E-utilities |
| **Link** | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/) |

**Uso**: Buscamos artigos relacionados ao reposicionamento de medicamentos.

### DrugBank

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Base de dados farmacológicos |
| **Fonte** | University of Alberta |
| **Dados** | Informações detalhadas de medicamentos |
| **Entidades** | ~8.000 medicamentos |
| **Link** | [go.drugbank.com](https://go.drugbank.com/) |

**Uso**: Mapeamento de nomes de medicamentos e informações farmacológicas.

---

## Fontes Regionais

### ICTRP (OMS)

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Portal de ensaios clínicos |
| **Fonte** | Organização Mundial da Saúde |
| **Dados** | Agregador global de registros |
| **Inclui** | ReBEC (Brasil) |
| **Link** | [trialsearch.who.int](https://trialsearch.who.int/) |

### ReBEC

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Registro brasileiro de ensaios |
| **Fonte** | Fiocruz |
| **Dados** | Ensaios clínicos no Brasil |
| **Link** | [ensaiosclinicos.gov.br](http://www.ensaiosclinicos.gov.br/) |

---

## Termos de Uso

Todas as fontes de dados são utilizadas em conformidade com seus respectivos termos de uso:

| Fonte | Licença/Termos |
|-------|----------------|
| TxGNN | CC BY 4.0 |
| ANVISA | Dados Abertos Brasil |
| ClinicalTrials.gov | Domínio Público |
| PubMed | Domínio Público |
| DrugBank | Academic License |

---

## Atualizações

| Fonte | Frequência |
|-------|------------|
| ANVISA | Semanal |
| ClinicalTrials.gov | Diária |
| PubMed | Contínua |
| DrugBank | Mensal |

---

## Citação

Se você utilizar os dados do BrTxGNN, por favor cite:

```bibtex
@misc{brtxgnn2026,
  title={BrTxGNN: Drug Repurposing Predictions for Brazil},
  author={Yao.Care},
  year={2026},
  url={https://brtxgnn.yao.care}
}
```

E a publicação original do TxGNN:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```
