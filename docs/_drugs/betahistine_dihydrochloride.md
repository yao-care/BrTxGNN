---
noindex: true
sitemap: false
layout: default
title: Betahistine Dihydrochloride
parent: Apenas Predição do Modelo (L5)
nav_order: 125
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Betahistine Dihydrochloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Betahistina Dicloridrato: Avaliação de Reposicionamento — Sem Previsões TxGNN Disponíveis
{: .text-alpha }

## Resumo

Betahistina Dicloridrato é um análogo da histamina amplamente utilizado no tratamento da Doença de Ménière e síndromes vertiginosas periféricas, com mecanismo de ação relacionado aos receptores histaminérgicos H1 e H3.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise (lista `predicted_indications` vazia).

<!-- review:begin br-lic-20261106-betahistine_dihydrochloride-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise (lista `predicted_indications` vazia). / O fármaco também **não possui registros** no mercado regulatório consultado, o que limita significativamente a avaliação.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betahistine_dihydrochloride-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados regulatórios consultados (0 registros) |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/A (ausência de previsão impede classificação) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | pelo menos 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão?

O Evidence Pack indica que a consulta ao DrugBank retornou 1 resultado (`result_count: 1`), mas o `drugbank_id` permanece nulo no registro do fármaco. Isso sugere que o mapeamento entre o nome **"BETAHISTINE DIHYDROCHLORIDE"** e o identificador DrugBank não foi concluído, o que impede o modelo TxGNN de posicionar o fármaco no grafo de conhecimento e gerar candidatos de reposicionamento.

Uma possível causa é a variação de nomenclatura: o fármaco pode estar registrado no DrugBank como **Betahistine** (base livre, DB00772) em vez de **Betahistine Dihydrochloride** (forma de sal). A resolução deste mapeamento é o pré-requisito para executar qualquer previsão.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Betahistina Dicloridrato, os dados regulatórios locais estão ausentes, e as lacunas de dados críticas (MOA e advertências) ainda precisam ser resolvidas antes de qualquer avaliação de segurança ou eficácia.

<!-- review:begin br-lic-20261106-betahistine_dihydrochloride-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Betahistina Dicloridrato, os dados regulatórios locais estão ausentes (0 registros), e as lacunas de dados críticas (MOA e advertências) ainda precisam ser resolvidas antes de qualquer avaliação de segurança ou eficácia.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betahistine_dihydrochloride-2 -->

**Para prosseguir, é necessário:**
- **[DG002 — Alta prioridade]** Resolver o mapeamento `drugbank_id`: verificar se `DB00772` (Betahistine) corresponde a este sal e atualizar o registro para reprocessar as previsões TxGNN
- **[DG001 — Bloqueante]** Obter a bula oficial para extrair advertências e contraindicações
- Confirmar se o fármaco está registrado sob nome alternativo (ex.: "Betahistina", "Betaserc", "Merislon") no mercado consultado
- Após resolução do DrugBank ID, reexecutar o pipeline TxGNN para gerar `predicted_indications`
- Avaliar a necessidade de inclusão de fontes regulatórias adicionais para mercados onde o fármaco está efetivamente comercializado (ex.: UE, Japão)

<!-- review:begin br-lic-20261106-betahistine_dihydrochloride-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**[DG001 — Bloqueante]** Obter a bula oficial via TFDA ou equivalente regulatório para extrair advertências e contraindicações” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betahistine_dihydrochloride-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco também **não possui registros** no mercado regulatório consultado, o que limita significativamente a avaliação” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(0 registros)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “via TFDA ou equivalente regulatório” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

