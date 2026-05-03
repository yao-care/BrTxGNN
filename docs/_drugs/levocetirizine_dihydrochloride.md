---
layout: default
title: Levocetirizine Dihydrochloride
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 0
---

# Levocetirizine Dihydrochloride
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

# Levocetirizine Dihydrochloride: Avaliação Incompleta — Sem Previsão de Reposicionamento Disponível

## Resumo em Uma Frase

Levocetirizine dihydrochloride é o enantiômero R da cetirizina, pertencente à classe dos anti-histamínicos H1 de segunda geração, utilizado no tratamento de rinite alérgica e urticária crônica idiopática.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise, o que pode refletir ausência de mapeamento DrugBank ou lacunas nos dados de entrada.
Não há evidências de ensaios clínicos ou publicações vinculadas a novas indicações neste pacote.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrada no pacote (rinite alérgica / urticária — conhecimento geral) |
| Nova Indicação Prevista | Nenhuma — TxGNN não gerou previsões |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 (sem estudos reais vinculados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pacote de evidências está incompleto em múltiplas dimensões críticas — sem DrugBank ID mapeado, sem previsões TxGNN geradas, sem registros regulatórios no Brasil e sem dados de segurança disponíveis. Não é possível conduzir uma avaliação de reposicionamento válida neste estágio.

**Para prosseguir, é necessário:**
- **DG001 (Bloqueante):** Obter jula e advertências/contraindicações na ANVISA — sem isso, a triagem de segurança S1 não pode ser iniciada
- **DG002 (Alta prioridade):** Recuperar o DrugBank ID e o mecanismo de ação (MOA) via DrugBank API — o ID nulo provavelmente impede o mapeamento no grafo TxGNN
- Re-executar o pipeline TxGNN após corrigir o mapeamento de DrugBank ID para obter previsões de indicações
- Verificar se `LEVOCETIRIZINE DIHYDROCHLORIDE` está indexado no grafo de conhecimento como nó de fármaco (pode exigir normalização para `levocetirizine`)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

