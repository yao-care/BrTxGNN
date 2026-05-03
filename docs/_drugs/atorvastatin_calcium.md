---
layout: default
title: Atorvastatin Calcium
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium
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

# Atorvastatin Calcium: Avaliação de Reposicionamento — Dados Insuficientes para Conclusão

## Resumo

Atorvastatin Calcium é uma estatina (inibidor da HMG-CoA redutase) amplamente conhecida pelo tratamento de hipercolesterolemia e prevenção de eventos cardiovasculares. O Evidence Pack recebido não contém previsões de novas indicações pelo modelo TxGNN (`predicted_indications` vazio), e a consulta ao banco de dados regulatório não retornou nenhum registro. Sem indicações previstas e sem dados regulatórios, **não é possível gerar um relatório completo de reposicionamento neste momento**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Não aplicável |
| Situação no Mercado Brasileiro | Não comercializado (0 registros encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack apresenta duas lacunas bloqueantes: ausência total de previsões TxGNN (`predicted_indications: []`) e ausência de registros regulatórios, o que impede qualquer análise de reposicionamento ou avaliação de segurança.

**Para prosseguir, é necessário:**

- **[Crítico]** Verificar o termo de busca no banco de dados regulatório — tentar variantes como `"atorvastatina"`, `"atorvastatin"` (sem "calcium") ou pelo nome comercial `"Lipitor"`, pois a consulta atual retornou 0 resultados para um fármaco amplamente comercializado
- **[Crítico]** Re-executar o modelo TxGNN com o DrugBank ID correto para gerar `predicted_indications` — sem esse campo o relatório de reposicionamento não pode ser produzido
- **[Alto]** Obter o DrugBank ID de Atorvastatin Calcium (referência: DB01076) via DrugBank API, conforme indicado no campo `DG002` do `data_gaps`
- **[Alto]** Coletar dados de mecanismo de ação (MOA) do DrugBank para subsidiar a análise de plausibilidade biológica
- **[Bloqueante]** Baixar e parsear a bula (PDF) do regulatório competente para preencher advertências e contraindicações (`DG001`), que atualmente estão em `[Data Gap]` com severidade **Blocking**

---

> ⚠️ **Nota sobre os dados recebidos:** A ausência de registros regulatórios para Atorvastatin Calcium é incomum, dado que este é um dos fármacos mais prescritos globalmente. É provável que a busca tenha falhado por incompatibilidade de nomenclatura. Recomenda-se revisão manual antes de qualquer conclusão sobre status de comercialização.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

