---
noindex: true
sitemap: false
layout: default
title: Albuterol
parent: Apenas Predição do Modelo (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Albuterol
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

## Albuterol: Avaliação de Reposicionamento — Dados Insuficientes para Geração de Previsão
{: .text-alpha }

## Resumo

Albuterol (denominação internacional alternativa: salbutamol) é um broncodilatador beta-2 adrenérgico de curta ação, classicamente utilizado no alívio do broncoespasmo em asma e DPOC. O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco na rodada atual de análise, provavelmente devido à ausência do identificador DrugBank no Evidence Pack. A avaliação completa está bloqueada até a complementação dos dados de entrada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Broncoespasmo (asma, DPOC) — inferido externamente; não constou no Evidence Pack |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 — sem previsão do modelo gerada |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 14 de 15) |
| Número de Registros | 15 (ativos: 14) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão Não Foi Gerada?

Albuterol (salbutamol) é um agonista seletivo dos receptores adrenérgicos beta-2, com mecanismo de ação bem estabelecido: ao ativar esses receptores na musculatura lisa brônquica, estimula a adenilil ciclase, eleva o AMPc intracelular e promove broncodilatação rápida. Trata-se de um dos fármacos mais utilizados no mundo para o manejo do broncoespasmo agudo.

O Evidence Pack recebido apresenta `drugbank_id: null`, o que provavelmente impediu o mapeamento correto do fármaco na base de conhecimento do TxGNN. Sem o identificador DrugBank, o modelo de grafo de conhecimento não consegue localizar o nó correspondente ao fármaco e, portanto, não produz previsões de reposicionamento. O DrugBank ID esperado para Albuterol é **DB01001**, e sua ausência representa a causa mais provável da lista de `predicted_indications` vazia.

No Brasil, este fármaco é registrado sob o nome INN adotado pela OMS — **salbutamol** — utilizado amplamente em produtos como Aerolin®, Salbutamol Sandoz® e similares. A divergência de nomenclatura explica o resultado negativo da consulta regulatória.

<!-- review:begin br-lic-20261106-albuterol-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Adicionalmente, a busca realizada na base da ANVISA com o termo "ALBUTEROL" retornou 0 registros. No Brasil, este fármaco é registrado sob o nome INN adotado pela OMS — **salbutamol** — utilizado amplamente em produtos como Aerolin®, Salbutamol Sandoz® e similares.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 15 registros para este medicamento, 14 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-albuterol-1 -->

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A ausência do `drugbank_id` bloqueou a geração de previsões pelo TxGNN, e a busca regulatória utilizou INN incorreto para o contexto brasileiro, resultando em um Evidence Pack sem dados suficientes para avaliação de reposicionamento.

**Para prosseguir, é necessário:**
- Inserir o `drugbank_id` correto (**DB01001**) e reprocessar o pipeline de previsão TxGNN
- Repetir a busca na ANVISA utilizando o nome INN alternativo **salbutamol**
- Baixar as bulas dos produtos registrados na ANVISA para extrair advertências, contraindicações e interações medicamentosas
- Após reprocessamento, verificar se o mecanismo beta-2 agonista apresenta relevância para alguma indicação alvo identificada pelo modelo

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Adicionalmente, a busca realizada na base da ANVISA com o termo "ALBUTEROL" retornou 0 registros” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

