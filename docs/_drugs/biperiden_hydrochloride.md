---
layout: default
title: Biperiden Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 0
---

# Biperiden Hydrochloride
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

# Biperideno (Cloridrato): Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Biperideno cloridrato é um anticolinérgico clássico (antagonista muscarínico M1), tradicionalmente utilizado no tratamento da doença de Parkinson e de reações extrapiramidais induzidas por antipsicóticos.
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco na rodada atual de análise, impossibilitando a avaliação de novas indicações terapêuticas.
A ausência de registros no mercado brasileiro e os dados de segurança incompletos reforçam a necessidade de complementação de informações antes de qualquer avanço.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson; reações extrapiramidais induzidas por medicamentos |
| Nova Indicação Prevista | — (sem previsão disponível) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem previsão gerada pelo modelo |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão Disponível?

O array `predicted_indications` retornou **vazio** neste Evidence Pack, indicando que o pipeline TxGNN não encontrou candidatos de reposicionamento com pontuação mínima para este composto na rodada atual de análise. Isso pode ocorrer por três razões principais:

**Lacuna de dados de identificação:** O campo `drugbank_id` está nulo, o que compromete a ancoragem do fármaco no grafo de conhecimento do TxGNN. Sem um identificador DrugBank válido, o modelo não consegue localizar o nó correspondente ao biperideno e, portanto, não calcula scores de reposicionamento.

**Lacuna de mecanismo de ação (MOA):** Os dados de MOA estão classificados como `[Data Gap]`. Com base no conhecimento farmacológico geral, biperideno é um antagonista muscarínico seletivo para receptores M1, reduzindo a hiperatividade colinérgica no corpo estriado — mecanismo relevante em condições que envolvam desequilíbrio dopaminérgico/colinérgico no sistema nervoso central. Contudo, sem esses dados estruturados no pipeline, a análise de reposicionamento baseada em similaridade de mecanismo fica prejudicada.

**Ausência de dados regulatórios locais:** A consulta à base regulatória brasileira retornou zero registros para "BIPERIDEN HYDROCHLORIDE", o que elimina a ancoragem por via de indicações aprovadas localmente. É recomendável repetir a busca pelo nome em português ("biperideno") para descartar falha de correspondência por grafia.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para biperideno cloridrato nesta rodada em razão de lacunas críticas de dados (DrugBank ID ausente, MOA não estruturado), e as informações de segurança estão indisponíveis. A ausência de registro no mercado brasileiro elimina o ponto de entrada regulatório imediato.

**Para prosseguir, é necessário:**
- Localizar e registrar o **DrugBank ID** correto para biperideno cloridrato (buscar por "biperiden" em [drugbank.com](https://go.drugbank.com/))
- Complementar os dados de **MOA** a partir do DrugBank API (DG002 — severidade High)
- Baixar e analisar a **bula aprovada** (ANVISA, EMA ou FDA) para preencher advertências e contraindicações (DG001 — severidade Blocking)
- **Re-executar o pipeline TxGNN** com os dados complementados para gerar previsões de reposicionamento
- Repetir a consulta regulatória com a grafia **"biperideno"** (sem especificação do sal) para verificar possíveis registros ANVISA não capturados
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

