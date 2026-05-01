---
layout: default
title: Bictegravir Sodium
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 0
---

# Bictegravir Sodium
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

# Bictegravir Sódico: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo

Bictegravir sódico é um inibidor de integrase do HIV (classe INSTI), tipicamente utilizado no tratamento de infecção por HIV-1 em combinação com outros antirretrovirais. O Evidence Pack disponível encontra-se **incompleto**: nenhum registro foi localizado no banco de dados regulatório consultado e o modelo TxGNN **não gerou previsões de nova indicação** para este fármaco. Não é possível conduzir uma análise de reposicionamento fundamentada com os dados atuais.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | HIV-1 (inibidor de integrase — INSTI) |
| Nova Indicação Prevista | — (sem previsão TxGNN disponível) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem dados de previsão |
| Situação no Mercado Brasileiro | Não encontrado na base consultada |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que os Dados São Insuficientes?

O processo de avaliação foi interrompido antes de gerar previsões porque três lacunas críticas foram identificadas:

1. **DrugBank ID ausente** — Sem o identificador DrugBank, o modelo TxGNN não consegue localizar o fármaco no grafo de conhecimento e, portanto, não produz previsões de indicação. Isso é classificado como lacuna de alta prioridade no Evidence Pack (`DG002 — severity: High`).

2. **Mecanismo de ação (MOA) não disponível** — Sem dados de MOA, a etapa de análise de relevância mecanística não pode ser executada, o que impede a interpretação de qualquer previsão futura.

3. **Sem registro regulatório localizado** — A consulta ao banco de dados retornou 0 resultados. É possível que Bictegravir esteja registrado como parte de combinação fixa (ex.: Bictegravir + Emtricitabina + Tenofovir Alafenamida) e não como monocomponente — o que pode explicar a ausência no resultado da busca.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há previsões TxGNN geradas, os dados regulatórios brasileiros estão ausentes e as informações de segurança (advertências, contraindicações, interações) não foram recuperadas. A avaliação de reposicionamento não pode avançar sem que as lacunas abaixo sejam resolvidas.

**Para prosseguir, é necessário:**
- Identificar o DrugBank ID correto de Bictegravir sódico e re-executar o modelo TxGNN para gerar previsões de indicação
- Verificar o registro na ANVISA pela combinação fixa (Bictegravir/Emtricitabina/Tenofovir Alafenamida) e não apenas pelo monocomponente
- Obter dados de MOA, advertências e contraindicações a partir da bula ou do DrugBank API
- Após obter o DrugBank ID, coletar dados de interações medicamentosas (DDI) — a consulta atual retornou `not_found`

> ⚠️ *Este relatório é gerado para fins de pesquisa. Os resultados não constituem aconselhamento médico e qualquer candidato a reposicionamento requer validação clínica antes de qualquer aplicação.*
---

