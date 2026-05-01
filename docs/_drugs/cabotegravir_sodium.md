---
layout: default
title: Cabotegravir Sodium
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 0
---

# Cabotegravir Sodium
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

# Cabotegravir Sódico: Avaliação Preliminar — Dados Insuficientes para Análise de Reposicionamento

## Resumo em Uma Frase

Cabotegravir sódico é um inibidor de integrase do HIV (INSTI) de ação prolongada, utilizado no tratamento e na profilaxia pré-exposição (PrEP) do HIV-1.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco neste ciclo de análise,
pois os dados regulatórios e de segurança necessários para a avaliação ainda não foram integrados ao pipeline.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | HIV-1 (tratamento e PrEP) — classe INSTI (Integrase Strand Transfer Inhibitor) |
| Nova Indicação Prevista | — (nenhuma previsão TxGNN disponível neste ciclo) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão Não Foi Gerada?

O pipeline TxGNN exige, no mínimo, que o fármaco esteja mapeado no grafo de conhecimento (Knowledge Graph) com um `drugbank_id` válido e que haja dados regulatórios locais para ancoragem da análise. Para o cabotegravir sódico, foram identificadas duas lacunas bloqueantes:

1. **DrugBank ID ausente** — sem o identificador canônico, o modelo não consegue posicionar o nó do fármaco no KG e, portanto, não computa scores de reposicionamento para nenhuma doença.

2. **Dados regulatórios brasileiros ausentes** — o fármaco não possui registro na ANVISA, e a bula/monografia local (fonte primária de MOA, advertências e contraindicações) não foi carregada no Evidence Pack.

Enquanto essas lacunas não forem resolvidas, nenhuma previsão pode ser considerada confiável e nenhuma tabela de evidências pode ser gerada.

---

## Informações de Comercialização no Brasil

Cabotegravir sódico **não possui registro ativo na ANVISA** até a data de corte deste relatório (2026-04-19).

> O fármaco é comercializado em outros países sob os nomes Vocabria® (oral) e Apretude® (injetável de longa ação) e, em combinação com rilpivirina, como Cabenuva®. Uma solicitação de registro junto à ANVISA pode estar em andamento; recomenda-se verificar o portal DATAVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> Dados de advertências, contraindicações e interações medicamentosas não foram carregados neste Evidence Pack. A obtenção da monografia ANVISA (ou equivalente FDA/EMA) é etapa bloqueante antes de qualquer análise clínica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há previsões TxGNN para este fármaco neste ciclo, e os dados mínimos exigidos para a análise de reposicionamento (DrugBank ID, MOA, dados regulatórios brasileiros) estão ausentes. Sem essas informações, qualquer recomendação clínica seria especulativa.

**Para prosseguir, é necessário:**

- [ ] **Resolver DG001 (Bloqueante):** Localizar e parsear a bula/monografia no portal ANVISA ou na FDA/EMA, extraindo advertências, contraindicações e indicações aprovadas
- [ ] **Resolver DG002 (Alta prioridade):** Consultar a API do DrugBank para obter o `drugbank_id` de Cabotegravir (forma base: DB11753) e confirmar se o sal sódico está mapeado separadamente ou como sinônimo
- [ ] **Reprocessar o pipeline TxGNN** após inserção do DrugBank ID para que o modelo gere scores de reposicionamento
- [ ] **Avaliar viabilidade regulatória:** Verificar se há registro em andamento na ANVISA (DATAVISA) ou se será necessário protocolar pedido de importação/registro antes de qualquer estudo clínico brasileiro
---

