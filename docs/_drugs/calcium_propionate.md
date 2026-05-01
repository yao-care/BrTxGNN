---
layout: default
title: Calcium Propionate
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 0
---

# Calcium Propionate
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

# Propionato de Cálcio: Conservante Alimentar — Sem Previsão de Reposicionamento Disponível

## Resumo em Uma Frase

Propionato de Cálcio (Calcium Propionate) é um conservante alimentar amplamente utilizado em produtos de panificação para inibir o crescimento de bolores e bactérias, reconhecido como seguro para uso em alimentos (status GRAS nos EUA).
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este composto, provavelmente por ausência de mapeamento farmacológico completo no DrugBank ou por o composto não possuir indicação farmacêutica registrada como ponto de partida.
A avaliação atual é **inconclusiva** por insuficiência de dados estruturados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Conservante alimentar (aditivo E282) — sem indicação farmacêutica registrada |
| Nova Indicação Prevista | Nenhuma (sem previsão TxGNN disponível) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos de reposicionamento identificados) |
| Situação no Mercado Brasileiro | Não comercializado como medicamento |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não gerou nenhuma indicação prevista para o Propionato de Cálcio, e o composto não possui qualquer registro regulatório como medicamento no Brasil, inviabilizando a análise de reposicionamento no estágio atual.

**Para prosseguir, é necessário:**
- Confirmar o mapeamento do Propionato de Cálcio no DrugBank — o log de consulta indica 1 resultado encontrado, mas nenhum `drugbank_id` foi importado para o Evidence Pack; requer revisão manual
- Verificar se o composto possui indicações farmacêuticas reconhecidas em outros mercados (ex.: uso veterinário para hipocalcemia bovina no pós-parto, pesquisas sobre efeitos neurológicos)
- Re-executar o pipeline TxGNN com o DrugBank ID confirmado para gerar previsões de reposicionamento
- Levantar dados de MOA junto ao DrugBank para viabilizar a análise de mecanismo
- Avaliar se o objeto correto da pesquisa é o sal (Propionato de **Cálcio**) ou o ácido livre (ácido propiônico), pois podem ter entradas distintas no grafo de conhecimento do TxGNN
---

