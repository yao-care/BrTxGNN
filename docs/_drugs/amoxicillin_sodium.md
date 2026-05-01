---
layout: default
title: Amoxicillin Sodium
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Amoxicillin Sodium
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

# AMOXICILLIN SODIUM: Avaliação de Reposicionamento — Dados Insuficientes para Análise

## Resumo

AMOXICILLIN SODIUM é a forma sódica (geralmente injetável) da amoxicilina, um antibiótico beta-lactâmico amplamente utilizado no tratamento de infecções bacterianas.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual, possivelmente por ausência de mapeamento DrugBank ou cobertura insuficiente no grafo de conhecimento.
Sem previsões disponíveis, não é possível conduzir análise de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no registro brasileiro (0 registros ANVISA para este INN) |
| Nova Indicação Prevista | Nenhuma previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão do modelo) |
| Situação no Mercado Brasileiro | Não comercializado sob este INN |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações pelo TxGNN, e o fármaco não possui registros ANVISA sob o INN "AMOXICILLIN SODIUM", impossibilitando tanto a análise de reposicionamento quanto a avaliação regulatória no Brasil.

**Para prosseguir, é necessário:**

- **Resolver DG001 (Bloqueante):** Localizar e analisar a bula ANVISA/TFDA para obter advertências e contraindicações
- **Resolver DG002 (Alto):** Consultar DrugBank API para obter o mecanismo de ação (MOA) e o DrugBank ID, permitindo que o TxGNN processe corretamente o fármaco
- **Verificar cobertura no KG:** Confirmar se "AMOXICILLIN SODIUM" está mapeado no grafo de conhecimento — possivelmente o fármaco está indexado apenas como "AMOXICILLIN" (forma livre), sem o sufixo do sal
- **Reprocessar previsão TxGNN:** Após normalização do nome INN e mapeamento DrugBank, reexecutar o pipeline de previsão
- **Investigar registros ANVISA alternativos:** Buscar sob variantes do nome, como "AMOXICILINA", "AMOXICILLIN TRIHYDRATE" ou o nome comercial correspondente
---

