---
layout: default
title: Downloads
nav_order: 7
description: "Downloads de dados do BrTxGNN para pesquisa."
permalink: /downloads/
---

# Downloads

<div class="key-takeaway">
Dados processados do BrTxGNN disponíveis para download em formatos abertos.
</div>

---

## Dados Disponíveis

### Dados ANVISA Processados

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `br_fda_drugs.json` | JSON | Medicamentos ANVISA processados |

**Campos incluídos**:
- NUMERO_REGISTRO_PRODUTO
- NOME_PRODUTO
- PRINCIPIO_ATIVO
- CLASSE_TERAPEUTICA
- SITUACAO_REGISTRO
- CATEGORIA_REGULATORIA

### Vocabulários TxGNN

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `drugbank_vocab.csv` | CSV | Vocabulário de medicamentos DrugBank |
| `disease_vocab.csv` | CSV | Vocabulário de doenças |
| `drug_disease_relations.csv` | CSV | Relações conhecidas medicamento-doença |

---

## Recursos FHIR

Os dados também estão disponíveis no formato FHIR R4:

| Recurso | Endpoint |
|---------|----------|
| CapabilityStatement | `/fhir/metadata` |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}.json` |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}.json` |
| Bundle (todos) | `/fhir/Bundle/all-predictions.json` |

---

## Formato dos Dados

### JSON - Medicamentos

```json
{
  "TIPO_PRODUTO": "MEDICAMENTO",
  "NOME_PRODUTO": "ASPIRINA",
  "NUMERO_REGISTRO_PRODUTO": "100000001",
  "PRINCIPIO_ATIVO": "ÁCIDO ACETILSALICÍLICO",
  "CLASSE_TERAPEUTICA": "ANALGÉSICOS",
  "SITUACAO_REGISTRO": "Ativo",
  "CATEGORIA_REGULATORIA": "Genérico"
}
```

### CSV - Vocabulário DrugBank

```csv
drugbank_id,drug_name
DB00945,Acetylsalicylic acid
DB00316,Acetaminophen
...
```

---

## Termos de Uso

<div class="disclaimer">
<strong>Termos de Uso dos Dados</strong>
<ul>
<li>Dados fornecidos apenas para fins de pesquisa</li>
<li>Não constitui aconselhamento médico</li>
<li>Cite a fonte ao utilizar os dados</li>
<li>Verifique atualizações nas fontes originais</li>
</ul>
</div>

---

## API de Acesso

Os dados também podem ser acessados via API estática:

```bash
# Obter metadados FHIR
curl https://brtxgnn.yao.care/fhir/metadata

# Obter índice de pesquisa
curl https://brtxgnn.yao.care/data/search-index.json
```

---

## Citação

Se você utilizar estes dados em sua pesquisa, por favor cite:

> BrTxGNN: Drug Repurposing Predictions for Brazil. Yao.Care, 2026. https://brtxgnn.yao.care

---

## Contato

Para solicitações de dados personalizados ou dúvidas:

- **GitHub**: [github.com/yao-care/BrTxGNN](https://github.com/yao-care/BrTxGNN)
- **Issues**: [github.com/yao-care/BrTxGNN/issues](https://github.com/yao-care/BrTxGNN/issues)
