---
layout: default
title: Albuterol Sulfate
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
---

# Albuterol Sulfate
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

# Albuterol Sulfato: Avaliação de Reposicionamento — Dados Insuficientes para Conclusão

## Resumo em Uma Frase

Albuterol Sulfato (Salbutamol) é um agonista beta-2 adrenérgico clássico, amplamente utilizado no tratamento de broncoespasmo, asma e DPOC em todo o mundo.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco nesta execução — provavelmente por divergência de nomenclatura entre "Albuterol Sulfate" (nome utilizado nos EUA) e "Salbutamol" (nome DCI adotado no Brasil e na maioria dos países).
**Nenhum ensaio clínico ou publicação** foi vinculado a novas indicações neste pacote de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no pacote (divergência de nomenclatura ANVISA) |
| Nova Indicação Prevista | Não disponível — sem previsão TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos vinculados) |
| Situação no Mercado Brasileiro | Não encontrado (0 registros com este nome) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pacote de evidências não contém previsões TxGNN nem dados regulatórios brasileiros para este fármaco. A busca na ANVISA com o termo "ALBUTEROL SULFATE" retornou **0 registros**, o que indica uma provável divergência de nomenclatura: no Brasil e nos demais países que adotam o sistema DCI/INN da OMS, este fármaco é registrado como **Salbutamol** — enquanto "Albuterol" é o nome utilizado principalmente nos Estados Unidos.

**Para prosseguir, é necessário:**
- Repetir a busca regulatória na ANVISA utilizando o nome DCI correto: **"Salbutamol"** ou **"Salbutamol Sulfato"**
- Identificar o DrugBank ID correspondente (DB01001 — Salbutamol) e reexecutar o pipeline TxGNN com o identificador correto
- Recuperar o MOA detalhado via DrugBank API (bloqueador DG002)
- Obter advertências e contraindicações da bula ANVISA (bloqueador DG001)
- Após correção da nomenclatura, reavaliar as previsões TxGNN antes de qualquer decisão de reposicionamento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

