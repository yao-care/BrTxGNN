---
layout: default
title: Carbinoxamina Maleate
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 0
---

# Carbinoxamina Maleate
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

# Carbinoxamina Maleato: Avaliação Preliminar — Dados Insuficientes para Previsão TxGNN

## Resumo

Carbinoxamina Maleato é um anti-histamínico de primeira geração (antagonista H1), historicamente utilizado no tratamento de rinite alérgica, urticária e sintomas de resfriado comum.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no presente ciclo de dados, possivelmente devido à ausência de mapeamento DrugBank.
Sem indicações previstas, ensaios clínicos associados ou literatura de suporte recuperada, **não é possível avançar para análise de reposicionamento** neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Condições alérgicas (rinite, urticária) — conhecimento geral; ausente no Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem estudos reais recuperados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão Não Está Disponível?

O pipeline TxGNN depende de dois insumos críticos para gerar previsões: o identificador DrugBank (`drugbank_id`) e o mecanismo de ação (MOA) do fármaco. Para a Carbinoxamina Maleato, ambos estão ausentes no Evidence Pack atual.

A consulta ao DrugBank retornou 1 resultado (`result_status: success`, `result_count: 1`), mas o `drugbank_id` não foi populado no registro, indicando uma falha na etapa de extração ou mapeamento pós-consulta. Sem esse identificador, o modelo de grafo de conhecimento (KG) não consegue posicionar o fármaco na rede de relações droga–doença.

Do ponto de vista farmacológico, a Carbinoxamina é um anti-histamínico clássico de primeira geração. Mecanisticamente, antagonistas H1 têm sido investigados em contextos além das alergias — como náuseas, tontura e distúrbios do sono — o que poderia gerar candidatos de reposicionamento relevantes caso o pipeline seja corretamente alimentado.

---

## Informações de Comercialização no Brasil

Nenhum registro ativo localizado na ANVISA. O fármaco **não está comercializado no Brasil**.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack carece do `drugbank_id` e do MOA necessários para execução do modelo TxGNN, e nenhuma previsão de reposicionamento foi gerada. Sem esse insumo, não há candidato a avaliar.

**Para prosseguir, é necessário:**

1. **Corrigir o mapeamento DrugBank** — A consulta retornou 1 resultado mas não populou o `drugbank_id`. Verificar manualmente o resultado e associar o ID correto (provavelmente `DB01114` — Carbinoxamine no DrugBank).
2. **Recuperar o MOA via DrugBank API** — Extrair `pharmacology.mechanism_of_action` do registro identificado.
3. **Reexecutar o pipeline TxGNN** — Com `drugbank_id` e MOA preenchidos, regenerar `predicted_indications`.
4. **Verificar status regulatório** — Confirmar se há solicitações de registro pendentes ou histórico de comercialização anterior no Brasil.
5. **Coletar informações de segurança** — Baixar bula de referência (FDA ou EMA) para preencher `key_warnings` e `contraindications`.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

