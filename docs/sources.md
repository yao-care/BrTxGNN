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
| **Doenças no grafo** | {{ site.data.source_stats.display.txgnn_diseases }} (nós de doença) |
| **Relações** | {{ site.data.source_stats.display.txgnn_drug_disease_edges }} arestas medicamento–doença (indicação e contraindicação) |
| **Link** | [zitniklab.hms.harvard.edu/projects/TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) |

### ANVISA

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Registro regulatório |
| **Fonte** | Agência Nacional de Vigilância Sanitária |
| **Dados** | Medicamentos registrados no Brasil |
| **Registros** | {{ site.data.source_stats.display.anvisa_records }} registros de medicamentos no arquivo ({{ site.data.source_stats.display.anvisa_active }} com situação Ativo) |
| **Atualização** | Semanal (download automático toda segunda-feira) |
| **Arquivo** | [DADOS_ABERTOS_MEDICAMENTOS.csv](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
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
| **Entidades** | {{ site.data.source_stats.display.txgnn_drugbank_drugs }} medicamentos com DrugBank ID no grafo de conhecimento do TxGNN |
| **Link** | [go.drugbank.com](https://go.drugbank.com/) |

**Uso**: Mapeamento de nomes de medicamentos e informações farmacológicas.

Os números das tabelas TxGNN, ANVISA e DrugBank acima são contados a partir dos arquivos de dados da Release deste repositório (`data/external/disease_vocab.csv`, `drug_disease_relations.csv`, `drugbank_vocab.csv` e `data/raw/br_fda_drugs.json`).

---

## Interações Medicamentosas

### DDInter

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Base de dados de interações medicamentosas (DDI) |
| **Arquivos** | 8 arquivos de download `ddinter_code_*.csv` (os mesmos nas páginas de download do DDInter 1.0 e 2.0; os arquivos não indicam versão) |
| **Dados** | {{ site.data.ddi_sources.display.ddinter_rows }} linhas, {{ site.data.ddi_sources.display.ddinter_unique_pairs }} pares únicos de medicamentos, {{ site.data.ddi_sources.display.ddinter_drug_names }} nomes de medicamentos |
| **Licença** | CC BY-NC-SA 4.0 |
| **Artigo** | [DDInter 2.0 (Nucleic Acids Research, 2024)](https://academic.oup.com/nar/article/53/D1/D1356/7740584) |
| **Link** | [ddinter2.scbdd.com](https://ddinter2.scbdd.com/) |

**Uso**: O coletor de evidências lê esses arquivos locais e inclui as interações encontradas no pacote de dados de cada medicamento; as seções de segurança dos relatórios citam essas interações.

### Guide to PHARMACOLOGY (GtoPdb)

| Aspecto | Detalhes |
|---------|----------|
| **Tipo** | Base de dados farmacológicos (alvos de medicamentos aprovados) |
| **Mantido por** | IUPHAR/BPS |
| **Arquivo** | `approved_drug_detailed_interactions.csv` (GtoPdb {{ site.data.ddi_sources.gtopdb_version }}) |
| **Dados** | {{ site.data.ddi_sources.display.gtopdb_drug_target_records }} registros fármaco–alvo de medicamentos aprovados (não são interações entre medicamentos) |
| **Link** | [guidetopharmacology.org](https://www.guidetopharmacology.org/) |

**Uso**: Informações de alvos farmacológicos no pacote de dados de cada medicamento.

Os números e a versão acima vêm de `.github/ddi-versions.json` (site_data, recalculado a partir dos arquivos de dados da Release deste repositório).

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
  author={yao.care},
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
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```
