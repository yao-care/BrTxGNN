---
layout: default
title: Amorolfina Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Amorolfina Hydrochloride
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

# Amorolfina Cloridrato: Avaliação de Potencial de Reposicionamento — Dados Insuficientes para Previsão

## Resumo

Amorolfina Cloridrato é um antifúngico da classe das morfolinas, utilizado no tratamento de onicomicoses (infecções fúngicas das unhas), geralmente em formulação de esmalte medicamentoso de uso tópico.

O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco na execução atual. Não foram encontrados registros regulatórios brasileiros, ensaios clínicos, publicações ou dados de segurança no pacote de evidências disponível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Onicomicose (infecção fúngica das unhas) — classe antifúngica das morfolinas |
| Nova Indicação Prevista | Não disponível — nenhuma previsão TxGNN gerada |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Abaixo de L5 — ausência total de previsão e estudos |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Foi Possível Analisar Esta Previsão?

A execução do modelo TxGNN para Amorolfina Cloridrato não produziu candidatos de reposicionamento (`predicted_indications` vazio). Isso pode ocorrer por três razões principais:

Primeiro, o fármaco pode não ter sido mapeado ao DrugBank Knowledge Graph — o campo `drugbank_id` está ausente no pacote de evidências, o que impede o modelo de localizar o nó correspondente na rede de conhecimento. A consulta ao DrugBank retornou um resultado (`result_count: 1`), mas o ID não foi incorporado ao registro.

Segundo, a ausência de dados de mecanismo de ação (`original_moa: [Data Gap]`) limita a capacidade do modelo de identificar conexões mecanísticas com novas indicações. Amorolfina inibe a biossíntese do ergosterol (enzimas Δ14-redutase e Δ7,8-isomerase), mas essa informação não foi integrada ao pipeline de previsão.

Terceiro, como formulação tipicamente tópica (esmalte ungueal), o fármaco apresenta baixa biodisponibilidade sistêmica, o que pode justificar a ausência de previsões para indicações sistêmicas — o modelo pode reconhecer essa limitação farmacocinética.

---

## Considerações de Segurança

Consulte a bula para informações de segurança completas. Nenhum dado de advertências, contraindicações ou interações medicamentosas foi encontrado neste pacote de evidências.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não produziu previsões de reposicionamento para este fármaco, e os dados regulatórios brasileiros indicam ausência de registros na ANVISA. Sem um `drugbank_id` válido integrado ao pipeline, não é possível gerar ou validar candidatos de reposicionamento.

**Para prosseguir, é necessário:**

- **Resolver DG002 (Crítico):** Obter e integrar o `drugbank_id` correto para Amorolfina — a consulta ao DrugBank encontrou 1 resultado (`result_count: 1`), mas o ID não foi inserido no registro; revisar o pipeline de mapeamento
- **Resolver DG001 (Bloqueante):** Baixar e analisar a bula ANVISA/TFDA para extrair advertências e contraindicações
- **Reexecutar o modelo TxGNN** após integração do DrugBank ID para gerar previsões válidas
- **Verificar o status regulatório brasileiro** diretamente na base da ANVISA usando o nome AMOROLFINA, CLORIDRATO DE AMOROLFINA e o nome comercial Loceryl® (comercializado em outros mercados)
- **Avaliar barreira farmacocinética:** dado que a formulação padrão é tópica (esmalte ungueal), documentar se há formulações sistêmicas disponíveis que tornariam o reposicionamento clinicamente viável
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

