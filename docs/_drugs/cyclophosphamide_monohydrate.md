---
layout: default
title: Cyclophosphamide Monohydrate
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 0
---

# Cyclophosphamide Monohydrate
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

# Ciclofosfamida Mono-hidratada: De [Indicação Original Não Registrada] para [Sem Previsão Disponível] — Análise Incompleta

## Resumo em Uma Frase

Ciclofosfamida mono-hidratada é a forma mono-hidratada da ciclofosfamida, um agente alquilante citotóxico amplamente reconhecido no tratamento de neoplasias e doenças autoimunes.
O modelo TxGNN **não gerou previsões de reposicionamento** para este registro — provavelmente por falha no mapeamento do INN para o DrugBank ID correspondente (DB00531).
A análise está **incompleta**: nenhuma indicação prevista, nenhum ensaio clínico vinculado e nenhum dado regulatório brasileiro disponível neste Evidence Pack.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Evidence Pack |
| Nova Indicação Prevista | Sem previsões disponíveis |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (apenas inferência nominal; sem estudos reais vinculados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros ANVISA encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão Disponível?

O pipeline TxGNN depende de um mapeamento bem-sucedido do nome do fármaco para um nó do conhecimento (DrugBank ID). Neste caso, a consulta ao DrugBank retornou **1 resultado** (log de consulta ID 3), mas o campo `drugbank_id` permaneceu nulo no Evidence Pack — indicando que o resultado foi encontrado, porém não vinculado corretamente ao registro.

A ciclofosfamida mono-hidratada é a forma farmacêutica mono-hidratada da ciclofosfamida (DrugBank: **DB00531**), um agente alquilante clássico da classe das oxazafosforinas. Mecanisticamente, forma ligações cruzadas no DNA mediante bioativação hepática (via CYP2B6/CYP3A4), inibindo a replicação celular tanto em células neoplásicas quanto em linfócitos — base do seu uso oncológico e imunossupressor.

Sem o mapeamento correto ao nó do grafo de conhecimento, o modelo não pôde calcular pontuações de reposicionamento. O fármaco em si possui vasta literatura de reposicionamento (doenças autoimunes, transplante de medula, neoplasias hematológicas e sólidas), que ficará acessível após correção do pipeline.

---

## Informações de Comercialização no Brasil

Nenhum registro foi localizado para o INN exato "CYCLOPHOSPHAMIDE MONOHYDRATE" na base consultada.

> **Atenção:** A forma-base "ciclofosfamida" (sem especificação de hidratação) pode estar registrada separadamente na ANVISA. Recomenda-se busca complementar com o INN simplificado para identificar registros equivalentes.

---

## Citotoxicidade

> A ciclofosfamida é um agente alquilante citotóxico clássico. Esta seção é exibida com base no perfil farmacológico reconhecido do fármaco.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (agente alquilante — classe oxazafosforina) |
| Risco de Mielossupressão | **Alto** — neutropenia, trombocitopenia e anemia são efeitos dose-dependentes; nadir típico entre 8–14 dias |
| Classificação de Emetogenicidade | **Médio a alto** — dependente da dose e via de administração (oral vs. IV) |
| Itens de Monitoramento | Hemograma completo (CBC com diferencial), função renal (creatinina, ureia), função hepática (TGO/TGP), uroanálise seriada (risco de cistite hemorrágica por acroleína) |
| Proteção no Manuseio | **Obrigatório** seguir regulamentos de citotóxicos — NIOSH classifica ciclofosfamida como agente antineoplásico de grupo 1; manipulação exclusiva em cabine de segurança biológica com EPI completo |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O sistema TxGNN não produziu nenhuma previsão de reposicionamento para este registro devido a falha de mapeamento do INN para o DrugBank ID, e não há dados regulatórios brasileiros disponíveis, inviabilizando qualquer avaliação substantiva neste momento.

**Para prosseguir, é necessário:**

- **[Crítico]** Corrigir o mapeamento: associar o INN "CYCLOPHOSPHAMIDE MONOHYDRATE" ao DrugBank ID **DB00531** e reprocessar o candidato pelo pipeline TxGNN completo
- **[Crítico]** Buscar registros ANVISA para "ciclofosfamida" (INN sem especificação de hidratação) para identificar licenças equivalentes e obter indicações aprovadas e advertências
- **[Alto]** Coletar dados de segurança (advertências, contraindicações, interações medicamentosas) a partir da bula do fabricante ou banco de dados de segurança DrugBank
- **[Médio]** Após reprocessamento, verificar quais indicações o TxGNN prevê e iniciar coleta de evidências (ensaios clínicos, literatura) para as indicações de maior pontuação
---

