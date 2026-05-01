---
layout: default
title: Axitinibe
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
---

# Axitinibe
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

# Axitinibe: Avaliação de Reposicionamento — Dados Insuficientes para Previsão Completa

## Resumo em Uma Frase

Axitinibe é um fármaco registrado no Brasil com 2 licenças ativas na ANVISA, porém os dados de indicação original e mecanismo de ação não estão disponíveis neste Evidence Pack.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados atuais, tornando inviável a análise de novas indicações.
Para avançar na avaliação, é necessário complementar os dados faltantes identificados em dois gaps críticos.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Sem previsões disponíveis |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão do modelo com dados atuais) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

Foram identificados **2 registros ativos** de Axitinibe na ANVISA. No entanto, os detalhes individuais de cada registro (número oficial, nome comercial, forma farmacêutica e texto da indicação aprovada) não constam nos dados recebidos neste Evidence Pack.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Não disponível | Não disponível | Não disponível | Não disponível |
| Não disponível | Não disponível | Não disponível | Não disponível |

> Os registros existem conforme confirmado pelo query TFDA (resultado: 2 licenças), mas os campos de detalhamento não foram retornados. Recomenda-se consulta direta à base ANVISA para recuperar esses dados.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack apresenta lacunas de dados em nível **Blocking** e **High** que impedem a execução completa do pipeline de avaliação: estão ausentes as advertências e contraindicações da bula ANVISA, o mecanismo de ação (MOA) e, sobretudo, qualquer previsão de reposicionamento gerada pelo TxGNN — tornando inviável a análise de novas indicações neste momento.

**Para prosseguir, é necessário:**
- **[DG001 — Blocking]** Baixar e analisar as bulas ANVISA dos 2 registros, extraindo indicações aprovadas, advertências principais e contraindicações (fonte: TFDA/ANVISA, método: download e parse do PDF da bula)
- **[DG002 — High]** Consultar a DrugBank API para recuperar o mecanismo de ação (MOA) do Axitinibe e categorias farmacológicas — nota: o query DrugBank retornou 1 resultado, mas os dados não foram incluídos no Evidence Pack atual
- Complementar os campos vazios dos 2 registros ANVISA (número de registro, nome comercial, forma farmacêutica, texto completo da indicação)
- Reexecutar o pipeline TxGNN com os dados de MOA e indicação preenchidos para gerar previsões de reposicionamento válidas
---

