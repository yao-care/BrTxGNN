---
layout: default
title: Buclizina Dihydrochloride
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 0
---

# Buclizina Dihydrochloride
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

# Buclizina (Dicloridrato): Avaliação Preliminar — Sem Indicação Prevista pelo TxGNN

## Resumo em Uma Frase

Buclizina (dicloridrato) é um anti-histamínico da classe piperazina, tradicionalmente utilizado como antiemético e estimulante do apetite. O modelo TxGNN **não gerou nenhuma previsão de nova indicação** para este fármaco, e ele **não possui registro ativo** na base regulatória consultada. A avaliação atual está bloqueada por lacunas críticas de dados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Sem dados disponíveis no Evidence Pack |
| Nova Indicação Prevista | — (Nenhuma previsão gerada pelo TxGNN) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (Sem evidências disponíveis) |
| Situação no Mercado | ✗ Não registrado na base consultada |
| Número de Registros | 0 |
| DrugBank ID | Não mapeado |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão?

A ausência de previsões do TxGNN para buclizina dicloridrato pode ser atribuída a um ou mais dos seguintes fatores:

1. **Falta de mapeamento DrugBank**: O fármaco não possui `drugbank_id` associado no Evidence Pack. O modelo TxGNN depende do grafo de conhecimento DrugBank para estabelecer relações fármaco–doença. Sem esse identificador, o fármaco não pode ser inserido no grafo de conhecimento e, portanto, não participa do processo de inferência.

2. **Ausência no grafo de conhecimento (KG)**: Mesmo que buclizina exista no DrugBank sob outra denominação ou forma salina (por exemplo, "buclizine" sem o sufixo "dihydrochloride"), a normalização de nomes pode não ter identificado a correspondência. Variações de nomenclatura de sais são uma causa comum de falha no mapeamento.

3. **Dados regulatórios insuficientes**: Com zero registros na base regulatória e nenhuma indicação original catalogada, o pipeline não dispõe de ponto de partida para buscar indicações alternativas.

---

## Informações de Comercialização

Nenhum registro encontrado na base regulatória consultada.

> **Nota:** Buclizina é comercializada em diversos países da América Latina (incluindo o Brasil, sob o nome comercial Buclina®) como estimulante do apetite e antiemético. A ausência de registros pode refletir uma limitação da base de dados consultada (TFDA — Taiwan) e não necessariamente a indisponibilidade global do fármaco.

---

## Considerações de Segurança

Não foram obtidos dados de segurança no Evidence Pack. Todas as categorias — advertências principais, contraindicações e interações medicamentosas — constam como lacunas de dados.

> Consulte a bula do fabricante para informações completas de segurança.

---

## Lacunas de Dados Identificadas

| ID | Categoria | Item Faltante | Severidade | Impacto | Remediação Sugerida |
|----|-----------|---------------|------------|---------|---------------------|
| DG001 | Drug_Level | Advertências e contraindicações da bula | **Bloqueante** | Impede a avaliação inicial de segurança (S1) | Baixar e analisar a bula oficial (PDF) |
| DG002 | Drug_Level | Mecanismo de ação (MOA) | Alta | Compromete a análise de plausibilidade mecanística | Consultar DrugBank API ou literatura farmacológica |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não é possível avançar na avaliação de reposicionamento sem (1) previsões do modelo TxGNN e (2) dados mínimos de segurança e mecanismo de ação. A ausência de mapeamento DrugBank é a causa raiz provável da falta de previsões.

**Para prosseguir, é necessário:**
- **Resolver o mapeamento DrugBank**: Buscar "buclizine" (INN sem sal) no DrugBank para obter o `drugbank_id` correto (provável: [DB09005](https://go.drugbank.com/drugs/DB09005)) e re-executar o pipeline
- **Obter dados de MOA**: Buclizina é um antagonista do receptor H1 da histamina (classe piperazina) — confirmar via DrugBank e incorporar ao Evidence Pack
- **Alimentar indicações originais**: Registrar as indicações aprovadas (antiemético, cinetose, estimulante do apetite) para permitir a análise de plausibilidade
- **Consultar base regulatória brasileira (ANVISA)**: Verificar registros ativos de buclizina no Brasil para complementar os dados regulatórios
- **Re-executar pipeline TxGNN** após resolução das lacunas acima
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

