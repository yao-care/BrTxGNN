---
layout: default
title: Abacavir Sulfate
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Abacavir Sulfate: Sem Previsão de Reposicionamento Gerada pelo TxGNN

## Resumo

Abacavir Sulfate é um inibidor nucleosídico da transcriptase reversa (INTR), originalmente utilizado no tratamento da infecção por HIV-1 em adultos e crianças, sempre em combinação com outros antirretrovirais. O modelo TxGNN **não gerou nenhuma previsão de nova indicação** para este fármaco neste ciclo de análise. Adicionalmente, o fármaco **não possui registros ativos no Brasil**, e lacunas críticas nos dados de entrada — como ausência de DrugBank ID e de mecanismo de ação — comprometem a execução completa do pipeline de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecção por HIV-1 (antirretroviral INTR) |
| Nova Indicação Prevista | Nenhuma previsão gerada neste ciclo |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão do modelo) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Houve Previsão?

Abacavir Sulfate pertence à classe dos inibidores nucleosídicos da transcriptase reversa (INTR). Seu mecanismo envolve a incorporação ao DNA viral em formação, bloqueando a replicação do HIV-1. Clinicamente, é utilizado em esquemas combinados — como com lamivudina e dolutegravir — sendo a base de regimes antirretrovirais de primeira linha em diversas diretrizes internacionais.

A ausência de previsões pelo TxGNN neste ciclo pode ser atribuída a três fatores identificados no Evidence Pack:

1. **DrugBank ID não mapeado**: O campo `drugbank_id` está ausente (`null`), o que impede o modelo de ancorar o fármaco no grafo de conhecimento TxGNN — etapa essencial para o cálculo de score de reposicionamento.
2. **Mecanismo de ação não registrado**: O campo `original_moa` consta como lacuna de dados, limitando a análise de similaridade farmacológica entre indicações.
3. **Ausência de registros regulatórios locais**: Sem aprovação registrada no Brasil, o perfil do fármaco no sistema está estruturalmente incompleto para o pipeline atual.

Essas lacunas são classificadas como **Blocking (DG001)** e **High (DG002)** nos metadados do Evidence Pack, confirmando que os dados mínimos necessários para avaliação não foram atingidos.

---

## Informações de Comercialização no Brasil

Abacavir Sulfate **não possui registros ativos** no banco de dados consultado neste ciclo. Portanto, não há dados de comercialização disponíveis para listagem.

> **Nota de contexto**: Abacavir (Ziagen®) é um fármaco com amplo uso clínico documentado globalmente para o tratamento do HIV-1. Recomenda-se verificação direta na ANVISA para confirmar o status regulatório vigente no Brasil, pois o presente Evidence Pack pode não refletir registros mais recentes.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta farmacológico geral**: Abacavir é clinicamente associado a **reações de hipersensibilidade graves potencialmente fatais**, fortemente relacionadas ao alelo **HLA-B\*5701**. A triagem genética pré-tratamento é recomendada pelas principais diretrizes internacionais (OMS, DHHS). Esta informação deriva de conhecimento farmacológico geral e **não** do Evidence Pack fornecido — que não contém dados de segurança verificados para este fármaco.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não gerou previsões de reposicionamento para Abacavir Sulfate neste ciclo devido a lacunas de dados classificadas como **Blocking**, especialmente a ausência de DrugBank ID — sem o qual o fármaco não pode ser conectado ao grafo de conhecimento. Sem previsões geradas, não há base analítica para avançar na avaliação de reposicionamento.

**Para prosseguir, é necessário:**
- Mapear o **DrugBank ID** correto (provável: DB01048 para abacavir) e re-executar o pipeline TxGNN
- Preencher os dados de **MOA** no Evidence Pack a partir do DrugBank API (conforme remediação DG002)
- Baixar e analisar a bula (PDF) junto à ANVISA para verificar advertências e contraindicações (remediação DG001)
- Verificar e atualizar o **status regulatório atual** na ANVISA para confirmar ausência ou presença de registros ativos
- Com os dados completos, re-executar o ciclo de Evidence Pack para gerar um relatório de reposicionamento completo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

