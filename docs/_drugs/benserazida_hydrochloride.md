---
layout: default
title: Benserazida Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 0
---

# Benserazida Hydrochloride
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

# Benserazida Cloridrato: Inibidor da DOPA Descarboxilase – Sem Previsões de Reposicionamento Disponíveis

## Resumo em Uma Frase

Benserazida cloridrato é um inibidor periférico da DOPA descarboxilase, utilizado classicamente em combinação fixa com levodopa para o tratamento da doença de Parkinson.
O modelo TxGNN **não gerou previsões de reposicionamento** para este composto no ciclo atual de análise, provavelmente por ausência do DrugBank ID no Evidence Pack.
O fármaco **não possui registro ativo no mercado brasileiro**, o que limita ainda mais as perspectivas imediatas de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson (em combinação com levodopa) |
| Nova Indicação Prevista | Nenhuma previsão disponível |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 – Sem estudos de reposicionamento identificados |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Foram Geradas Previsões?

Benserazida cloridrato é um inibidor periférico da DOPA descarboxilase (DDC), enzima responsável por converter levodopa em dopamina fora do sistema nervoso central. Ao bloquear essa conversão na periferia, o fármaco potencializa o efeito antiparkinsônico da levodopa, permitindo que maior quantidade dela atravesse a barreira hematoencefálica. Na prática clínica, benserazida é utilizada exclusivamente em associação fixa com levodopa (ex.: Madopar®, levodopa + benserazida).

O campo `drugbank_id` do Evidence Pack está como `null`, o que indica que o mapeamento do composto na rede de conhecimento do TxGNN não foi concluído. Sem esse identificador, o modelo não consegue posicionar a benserazida no grafo de interações fármaco-doença, inviabilizando a geração de qualquer previsão de reposicionamento neste ciclo.

Para viabilizar análise futura, recomenda-se confirmar o DrugBank ID da benserazida (provavelmente **DB13528**) e reprocessar o Evidence Pack com esse dado corrigido.

---

## Situação no Mercado Brasileiro

O fármaco **não possui nenhum registro ativo na ANVISA** conforme os dados deste Evidence Pack (`total_licenses: 0`, `market_status: não comercializado`). Não há, portanto, nenhum produto contendo Benserazida Cloridrato legalmente comercializado no Brasil neste momento.

> **Nota:** A benserazida é comumente disponibilizada no mercado internacional como formulação combinada com levodopa (Madopar®). Caso haja interesse em reposicionamento no Brasil, o ponto de entrada regulatório mais natural seria via registro do produto combinado, e não do princípio ativo isolado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não gerou previsões de reposicionamento para este composto devido à ausência do DrugBank ID, e o fármaco não possui registro ativo no Brasil — dois bloqueadores estruturais que impedem avançar para avaliação clínica ou regulatória neste momento.

**Para prosseguir, é necessário:**
- Confirmar e preencher o DrugBank ID correto (provável: **DB13528**) e reprocessar o Evidence Pack
- Obter a bula completa para extração de advertências, contraindicações e interações medicamentosas
- Verificar se há registros ANVISA sob o nome do produto combinado (levodopa + benserazida, ex.: Madopar®)
- Após reprocessamento com DrugBank ID, reavaliar as previsões TxGNN geradas antes de decidir sobre avançar
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

