---
layout: default
title: Guia de Uso
nav_order: 3
description: "Como usar e interpretar os relatórios de reposicionamento de medicamentos do BrTxGNN."
permalink: /guide/
---

# Guia de Uso

<div class="key-takeaway">
Este guia explica como interpretar os relatórios de previsão e os níveis de evidência.
</div>

---

## Níveis de Evidência

O BrTxGNN classifica as previsões de reposicionamento em 5 níveis de evidência:

| Nível | Descrição | Critérios |
|-------|-----------|-----------|
| **L1** | Evidência Forte | ≥2 ensaios clínicos Fase 3/4 |
| **L2** | Evidência Moderada | ≥1 ensaio Fase 3/4 ou ≥2 ensaios Fase 2 |
| **L3** | Evidência Inicial | ≥1 ensaio clínico (qualquer fase) |
| **L4** | Evidência Pré-clínica | ≥1 artigo científico relevante |
| **L5** | Apenas Previsão | Previsão do modelo TxGNN, sem evidência externa |

---

## Como Interpretar os Relatórios

### Score TxGNN

O score TxGNN indica a confiança do modelo na previsão:

- **90-100**: Muito alta confiança
- **70-89**: Alta confiança
- **50-69**: Confiança moderada
- **<50**: Baixa confiança

<blockquote class="expert-quote">
O score TxGNN é baseado em relações no grafo de conhecimento biomédico. Scores mais altos indicam relações mais fortes entre o medicamento e a doença no grafo.
</blockquote>

### Evidências Coletadas

Para cada previsão, coletamos evidências de múltiplas fontes:

1. **ClinicalTrials.gov** - Ensaios clínicos registrados
2. **PubMed** - Literatura científica
3. **ANVISA** - Status regulatório no Brasil
4. **DrugBank** - Informações farmacológicas

---

## Exemplo de Análise

Suponha que encontramos uma previsão de **Metformina** para **Doença de Alzheimer**:

| Aspecto | Valor |
|---------|-------|
| Score TxGNN | 85.3 |
| Nível de Evidência | L3 |
| Ensaios Clínicos | 3 (Fase 1/2) |
| Artigos PubMed | 47 |

**Interpretação**: Esta é uma previsão promissora com score alto. O nível L3 indica que já existem ensaios clínicos em andamento, mas ainda não atingiu Fase 3. Os 47 artigos sugerem interesse significativo da comunidade científica.

---

## Limitações

<div class="disclaimer">
<strong>Aviso Importante</strong><br>
<ul>
<li>As previsões são geradas por IA e <strong>não substituem validação clínica</strong></li>
<li>Não constitui recomendação médica ou de tratamento</li>
<li>Uso off-label requer supervisão médica especializada</li>
<li>Dados podem estar desatualizados</li>
</ul>
</div>

---

## Próximos Passos

Se você identificou uma previsão interessante:

1. **Pesquise mais** - Consulte as fontes originais (ClinicalTrials.gov, PubMed)
2. **Avalie criticamente** - Considere o desenho dos estudos e tamanho das amostras
3. **Consulte especialistas** - Discuta com profissionais de saúde e pesquisadores
4. **Monitore atualizações** - Novas evidências podem surgir

---

## Contato

Para dúvidas ou sugestões sobre o BrTxGNN:

- **GitHub Issues**: [github.com/yao-care/BrTxGNN/issues](https://github.com/yao-care/BrTxGNN/issues)
- **Página do Projeto**: [brtxgnn.yao.care](https://brtxgnn.yao.care)
