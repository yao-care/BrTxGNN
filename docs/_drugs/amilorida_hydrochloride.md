---
layout: default
title: Amilorida Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 0
---

# Amilorida Hydrochloride
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

# Amilorida Cloridrato: Avaliação de Reposicionamento — Sem Previsões Disponíveis

## Resumo em Uma Frase

Amilorida Cloridrato (AMILORIDA HYDROCHLORIDE) é um fármaco consultado na base do TFDA/ANVISA, porém **sem registros comerciais ativos no Brasil**.
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** nesta execução, possivelmente em razão da ausência de DrugBank ID mapeado ou de dados insuficientes de indicações originais.
A avaliação está incompleta e requer complementação de dados antes de qualquer análise de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (sem registros no TFDA) |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos — sem previsão de modelo) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Lacunas de Dados Identificadas

A execução do pipeline identificou **2 lacunas críticas** que inviabilizaram a geração de previsões:

| ID | Item | Severidade | Impacto |
|----|------|------------|---------|
| DG001 | Advertências/contraindicações do TFDA (bula) | Bloqueante | Impossibilita avaliação inicial de segurança (S1) |
| DG002 | Mecanismo de ação (MOA) | Alta | Impede análise de relevância mecanística |

> **Observação sobre o DrugBank:** O log de consulta indica que a busca ao DrugBank retornou **1 resultado** para "AMILORIDA HYDROCHLORIDE", mas os dados não foram populados no Evidence Pack. É provável que o mapeamento DrugBank ID esteja pendente de resolução manual.

---

## Informações de Comercialização no Brasil

Nenhum registro encontrado. O fármaco **AMILORIDA HYDROCHLORIDE não possui registros ativos** na base consultada do TFDA/ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não gerou previsões de reposicionamento para este fármaco na execução atual, e os dados mínimos necessários (DrugBank ID, MOA, indicações originais e perfil de segurança) estão ausentes do Evidence Pack, impossibilitando qualquer análise de viabilidade.

**Para prosseguir, é necessário:**
- **[DG002 — Alta prioridade]** Consultar o DrugBank API para recuperar o DrugBank ID e o MOA do fármaco (a query já retornou 1 resultado: verificar por que os dados não foram populados)
- **[DG001 — Bloqueante]** Baixar e analisar o PDF da bula no TFDA para extrair advertências e contraindicações
- Verificar se o nome "AMILORIDA HYDROCHLORIDE" está indexado corretamente no DrugBank — possível variação de grafia em relação ao INN padrão em inglês ("Amiloride hydrochloride")
- Reexecutar o pipeline TxGNN após resolução do mapeamento DrugBank para obter previsões de reposicionamento
- Avaliar se o fármaco possui registro em outros mercados relevantes (EUA, Europa) que possam fornecer dados de indicações originais como referência
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

