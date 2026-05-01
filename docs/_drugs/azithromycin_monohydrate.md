---
layout: default
title: Azithromycin Monohydrate
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 0
---

# Azithromycin Monohydrate
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

# Azithromycin Monohydrate: Avaliação Incompleta — Sem Previsão TxGNN Disponível

---

## Resumo

Azithromycin Monohydrate é a forma mono-hidratada da azitromicina, um antibiótico macrolídeo amplamente utilizado no tratamento de infecções bacterianas. Nesta execução do pipeline TxGNN, **nenhuma previsão de reposicionamento foi gerada**, provavelmente porque a busca utilizou o nome na forma salina completa ("AZITHROMYCIN MONOHYDRATE") em vez do nome comum ("AZITHROMYCIN"), causando falha de correspondência nos bancos de dados regulatório e de conhecimento. Dados de segurança, mecanismo de ação e indicações originais também não foram recuperados, tornando impossível uma avaliação de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nesta execução |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (ausência de previsões e estudos disponíveis) |
| Situação no Mercado Brasileiro | Não registrado (0 licenças encontradas) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsões Disponíveis?

O pipeline TxGNN necessita de um **DrugBank ID** válido para gerar candidatos de reposicionamento. Nesta execução, o campo `drugbank_id` está nulo, o que interrompeu o fluxo de predição antes de qualquer resultado ser produzido.

A causa provável é que a busca regulatória foi realizada com o nome de forma salina completa ("AZITHROMYCIN MONOHYDRATE"), enquanto as bases de dados regulatórias geralmente indexam o fármaco pelo nome comum ("AZITHROMYCIN"). A consulta ao DrugBank retornou 1 resultado com sucesso, confirmando que o fármaco existe na base — mas esse resultado não foi corretamente propagado para o restante do pipeline.

Adicionalmente, duas lacunas de dados bloqueadores foram identificadas:

| Código | Item em Falta | Impacto |
|--------|--------------|---------|
| DG001 | Advertências e contraindicações regulatórias | Bloqueador — impede avaliação inicial de segurança |
| DG002 | Mecanismo de Ação (MOA) | Alto — impede análise de relevância mecanística |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento nesta execução por falha de correspondência do nome do fármaco. Sem indicações previstas, pontuação de predição ou dados de segurança, não é possível conduzir uma avaliação de reposicionamento fundamentada.

**Para prosseguir, é necessário:**
1. **Corrigir a entrada do fármaco**: reexecutar todas as buscas com "AZITHROMYCIN" (sem o sufixo "MONOHYDRATE") para obter correspondência nos bancos regulatórios
2. **Recuperar o DrugBank ID**: o DrugBank retornou 1 resultado — extrair e registrar o ID correspondente (provavelmente DB00207) para habilitar as predições TxGNN
3. **Obter dados de segurança**: baixar e parsear a bula PDF do site regulatório para extrair advertências e contraindicações (DG001)
4. **Obter MOA via DrugBank API**: com o DrugBank ID em mãos, recuperar mecanismo de ação, categorias e dados de toxicidade (DG002)
5. **Reexecutar o pipeline completo**: após as correções acima, reger a predição TxGNN para gerar candidatos de reposicionamento e produzir o relatório completo
---

