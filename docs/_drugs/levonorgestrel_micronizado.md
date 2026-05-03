---
layout: default
title: Levonorgestrel Micronizado
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 0
---

# Levonorgestrel Micronizado
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

# Levonorgestrel Micronizado: Avaliação de Reposicionamento Pendente

## Resumo

Levonorgestrel micronizado é um progestágeno sintético de segunda geração, amplamente utilizado em contracepção hormonal — pílulas anticoncepcionais combinadas, dispositivos intrauterinos hormonais (DIU-LNG) e contracepção de emergência. Nesta rodada de análise, o modelo TxGNN **não gerou previsões de novas indicações** para este fármaco, provavelmente devido à ausência de mapeamento no grafo de conhecimento. A avaliação de reposicionamento fica pendente até que o DrugBank ID correto seja confirmado e a predição seja reexecutada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Contracepção hormonal (progestágeno) |
| Nova Indicação Prevista | Nenhuma previsão disponível nesta rodada |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Hold |

## Informações de Comercialização no Brasil

Foram identificados **8 registros ativos** no sistema regulatório brasileiro para Levonorgestrel Micronizado. Os detalhes individuais dos registros (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack — os campos retornaram vazios na consulta à base do TFDA/ANVISA.

> Para recuperar os detalhes, recomenda-se consultar diretamente o portal [Consulta de Produtos Registrados da ANVISA](https://consultas.anvisa.gov.br/) utilizando o INN "levonorgestrel".

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para este fármaco nesta rodada. A causa provável é que o sufixo de formulação **"MICRONIZADO"** incluído no INN impediu o mapeamento correto ao grafo de conhecimento — o identificador padrão no DrugBank é simplesmente **"Levonorgestrel"** (DB00367), sem descritor de forma farmacêutica. Sem o mapeamento confirmado, o modelo não consegue calcular pontuações de proximidade no grafo de doenças.

**Para prosseguir, é necessário:**
- Confirmar o DrugBank ID correto (esperado: **DB00367** — Levonorgestrel) e atualizar o campo `drugbank_id` no Evidence Pack
- Re-executar a predição TxGNN com o INN normalizado (`levonorgestrel`, sem "micronizado")
- Baixar e analisar a bula em PDF via ANVISA para preencher dados de segurança (advertências e contraindicações)
- Recuperar os detalhes dos 8 registros no portal ANVISA para completar a tabela de comercialização
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

