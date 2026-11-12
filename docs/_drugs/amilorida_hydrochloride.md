---
noindex: true
sitemap: false
layout: default
title: Amilorida Hydrochloride
parent: Apenas Predição do Modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amilorida Hydrochloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Amilorida Cloridrato: Avaliação de Reposicionamento — Sem Previsões Disponíveis
{: .text-alpha }

## Resumo em Uma Frase

O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** nesta execução, possivelmente em razão da ausência de DrugBank ID mapeado ou de dados insuficientes de indicações originais.
A avaliação está incompleta e requer complementação de dados antes de qualquer análise de reposicionamento.

<!-- review:begin br-lic-20261106-amilorida_hydrochloride-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Amilorida Cloridrato (AMILORIDA HYDROCHLORIDE) é um fármaco consultado na base do TFDA/ANVISA, porém **sem registros comerciais ativos no Brasil**. / O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** nesta execução, possivelmente em razão da ausência de DrugBank ID mapeado ou de dados insuficientes de indicações originais.” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amilorida_hydrochloride-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos — sem previsão de modelo) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 5) |
| Número de Registros | 5 (ativos: 3) |
| Decisão Recomendada | Hold |

---

## Lacunas de Dados Identificadas

A execução do pipeline identificou **2 lacunas críticas** que inviabilizaram a geração de previsões:

| ID | Item | Severidade | Impacto |
|----|------|------------|---------|
| DG001 | Advertências/contraindicações (bula) | Bloqueante | Impossibilita avaliação inicial de segurança (S1) |
| DG002 | Mecanismo de ação (MOA) | Alta | Impede análise de relevância mecanística |

> **Observação sobre o DrugBank:** O log de consulta indica que a busca ao DrugBank retornou **1 resultado** para "AMILORIDA HYDROCHLORIDE", mas os dados não foram populados no Evidence Pack. É provável que o mapeamento DrugBank ID esteja pendente de resolução manual.

<!-- review:begin br-lic-20261106-amilorida_hydrochloride-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Nenhum registro encontrado. O fármaco **AMILORIDA HYDROCHLORIDE não possui registros ativos** na base consultada do TFDA/ANVISA.” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amilorida_hydrochloride-2 -->

---

## Informações de Comercialização no Brasil

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
- **[DG001 — Bloqueante]** Baixar e analisar o PDF da bula para extrair advertências e contraindicações
- Verificar se o nome "AMILORIDA HYDROCHLORIDE" está indexado corretamente no DrugBank — possível variação de grafia em relação ao INN padrão em inglês ("Amiloride hydrochloride")
- Reexecutar o pipeline TxGNN após resolução do mapeamento DrugBank para obter previsões de reposicionamento
- Avaliar se o fármaco possui registro em outros mercados relevantes (EUA, Europa) que possam fornecer dados de indicações originais como referência

<!-- review:begin br-lic-20261106-amilorida_hydrochloride-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**[DG001 — Bloqueante]** Baixar e analisar o PDF da bula no TFDA para extrair advertências e contraindicações” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amilorida_hydrochloride-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Amilorida Cloridrato (AMILORIDA HYDROCHLORIDE) é um fármaco consultado na base do TFDA/ANVISA, porém **sem registros comerciais ativos no Br” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Nenhum registro encontrado. O fármaco **AMILORIDA HYDROCHLORIDE não possui registros ativos** na base consultada do TFDA/ANVISA” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “no TFDA” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

