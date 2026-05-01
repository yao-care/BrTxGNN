---
layout: default
title: Atazanavir Sulfate
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Atazanavir Sulfate
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

# Atazanavir Sulfato: Do Tratamento do HIV — Sem Previsão de Reposicionamento Disponível

## Resumo

Atazanavir Sulfato é um inibidor de protease do HIV-1, originalmente utilizado no tratamento da infecção por HIV em adultos e populações pediátricas.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados disponíveis atualmente.
Foram identificadas **lacunas críticas de dados** — incluindo ausência de registros regulatórios brasileiros e de mecanismo de ação documentado — que impedem a realização de uma avaliação completa neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecção por HIV-1 (antirretroviral, inibidor de protease) |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | Não registrado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não produziu candidatos de reposicionamento para Atazanavir Sulfato na execução atual, e o fármaco não possui registros ativos na base de dados regulatória consultada — impossibilitando qualquer análise de indicação original, mecanismo ou perfil de segurança a partir das fontes primárias.

**Para prosseguir, é necessário:**
- Consultar a ANVISA diretamente para verificar situação registratória (o fármaco é distribuído pelo Ministério da Saúde para o Programa Nacional de DST/AIDS e pode ter vias de registro distintas)
- Obter dados de mecanismo de ação (MOA) via DrugBank API (consulta retornou 1 resultado mas sem detalhes estruturados no pacote)
- Baixar e analisar bula(s) para extrair advertências, contraindicações e interações medicamentosas relevantes
- Reexecutar o pipeline TxGNN com os dados regulatórios completos para gerar previsões de reposicionamento
---

