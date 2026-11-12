---
noindex: true
sitemap: false
layout: default
title: Atorvastatin Calcium
parent: Apenas Predição do Modelo (L5)
nav_order: 88
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Atorvastatin Calcium
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

## Atorvastatin Calcium: Avaliação de Reposicionamento — Dados Insuficientes para Conclusão
{: .text-alpha }

## Resumo

Atorvastatin Calcium é uma estatina (inibidor da HMG-CoA redutase) amplamente conhecida pelo tratamento de hipercolesterolemia e prevenção de eventos cardiovasculares. O Evidence Pack recebido não contém previsões de novas indicações pelo modelo TxGNN (`predicted_indications` vazio), e a consulta ao banco de dados regulatório não retornou nenhum registro. Sem indicações previstas e sem dados regulatórios, **não é possível gerar um relatório completo de reposicionamento neste momento**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Não aplicável |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 18) |
| Número de Registros | pelo menos 20 |
| Decisão Recomendada | **Hold** |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**

<!-- review:begin br-lic-20261106-atorvastatin_calcium-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**Justificativa:** / O Evidence Pack apresenta duas lacunas bloqueantes: ausência total de previsões TxGNN (`predicted_indications: []`) e ausência de registros regulatórios, o que impede qualquer análise de reposicionamento ou avaliação de segurança.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atorvastatin_calcium-1 -->

**Para prosseguir, é necessário:**

- **[Crítico]** Verificar o termo de busca no banco de dados regulatório — tentar variantes como `"atorvastatina"`, `"atorvastatin"` (sem "calcium") ou pelo nome comercial `"Lipitor"`, pois a consulta atual retornou 0 resultados para um fármaco amplamente comercializado
- **[Crítico]** Re-executar o modelo TxGNN com o DrugBank ID correto para gerar `predicted_indications` — sem esse campo o relatório de reposicionamento não pode ser produzido
- **[Alto]** Obter o DrugBank ID de Atorvastatin Calcium (referência: DB01076) via DrugBank API, conforme indicado no campo `DG002` do `data_gaps`
- **[Alto]** Coletar dados de mecanismo de ação (MOA) do DrugBank para subsidiar a análise de plausibilidade biológica
- **[Bloqueante]** Baixar e parsear a bula (PDF) do regulatório competente para preencher advertências e contraindicações (`DG001`), que atualmente estão em `[Data Gap]` com severidade **Blocking**

---

> É provável que a busca tenha falhado por incompatibilidade de nomenclatura. Recomenda-se revisão manual antes de qualquer conclusão sobre status de comercialização.

<!-- review:begin br-lic-20261106-atorvastatin_calcium-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “> ⚠️ **Nota sobre os dados recebidos:** A ausência de registros regulatórios para Atorvastatin Calcium é incomum, dado que este é um dos fármacos mais prescritos globalmente. É provável que a busca tenha falhado por incompatibilidade de nomenclatura.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atorvastatin_calcium-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O Evidence Pack apresenta duas lacunas bloqueantes: ausência total de previsões TxGNN (`predicted_indications: []`) e ausência de registros ” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “⚠️ **Nota sobre os dados recebidos:** A ausência de registros regulatórios para Atorvastatin Calcium é incomum, dado que este é um dos fárma” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

