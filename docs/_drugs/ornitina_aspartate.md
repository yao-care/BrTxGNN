---
layout: default
title: Ornitina Aspartate
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 0
---

# Ornitina Aspartate
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

# Ornitina Aspartato: Avaliação Incompleta — Dados Insuficientes para Previsão de Reposicionamento

## Resumo em Uma Frase

Ornitina Aspartato (L-ornitina L-aspartato) é um fármaco cujos dados regulatórios e de indicação original não constam no sistema brasileiro.
O modelo TxGNN **não gerou previsões de reposicionamento** para este composto neste ciclo de análise,
pois a ausência de registro nacional e as lacunas críticas de dados (MOA, advertências, indicação original) impediram a execução completa do pipeline.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no sistema |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão ou estudos associados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão Disponível?

A ausência de previsões do TxGNN resulta diretamente de duas lacunas bloqueantes identificadas no pipeline de coleta de dados:

1. **Sem registro brasileiro (ANVISA)**: A consulta ao banco regulatório retornou zero resultados para "ORNITINA ASPARTATE". Sem ao menos uma indicação aprovada registrada localmente, o modelo não possui âncora para calcular similaridade farmacológica.

2. **DrugBank ID ausente**: Embora a consulta ao DrugBank tenha retornado 1 resultado, o `drugbank_id` não foi preenchido no Evidence Pack. Isso impede o mapeamento do composto ao grafo de conhecimento (KG) do TxGNN, que utiliza o DrugBank ID como chave de entrada para previsão de novas indicações.

3. **Mecanismo de ação não disponível**: Sem dados de MOA, a análise de plausibilidade mecanística não pode ser realizada.

---

## Considerações de Segurança

Não há dados de advertências, contraindicações ou interações medicamentosas disponíveis neste Evidence Pack.

> Consulte a bula e fontes primárias (DrugBank, literatura científica) para informações de segurança antes de qualquer uso ou análise aprofundada.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A ausência total de dados regulatórios brasileiros, de DrugBank ID vinculado e de mecanismo de ação torna inviável qualquer avaliação de reposicionamento neste ciclo. Não há base de evidências para recomendar avanço.

**Para prosseguir, é necessário:**

- [ ] **Vincular DrugBank ID**: O DrugBank retornou 1 resultado — recuperar e confirmar o ID correto (provavelmente `DB09341` para L-ornitina L-aspartato) e atualizar o Evidence Pack
- [ ] **Mapear indicação original**: Identificar a(s) indicação(ões) aprovadas internacionalmente (ex.: encefalopatia hepática, hiperamonemia) como âncora para o modelo TxGNN
- [ ] **Resolver status regulatório**: Verificar se o composto está disponível no Brasil sob outro nome (ex.: "L-ORNITINA L-ASPARTATO", "LOLA") ou como suplemento/hospitalar
- [ ] **Coletar MOA**: Consultar DrugBank API ou literatura para descrever o mecanismo (ciclo da ureia, síntese de glutamina)
- [ ] **Re-executar pipeline**: Após resolução das lacunas acima, re-executar a predição TxGNN com o DrugBank ID correto
---

