---
noindex: true
sitemap: false
layout: default
title: Atropine Sulfate
parent: Apenas Predição do Modelo (L5)
nav_order: 92
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Atropine Sulfate
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

## Atropine Sulfate: Avaliação de Reposicionamento — Dados Insuficientes para Análise Completa
{: .text-alpha }

---

## Resumo em Uma Frase

Sulfato de Atropina é um agente anticolinérgico clássico com décadas de uso em indicações como bradicardia, midríase e tratamento de intoxicação por organofosforados.
O modelo TxGNN **não retornou indicações previstas** nesta consulta (26/03/2026), provavelmente porque o fármaco não foi localizado na base regulatória brasileira consultada.
Com os dados disponíveis, **não é possível conduzir uma análise de reposicionamento**, e a avaliação deve ser suspensa até a resolução das lacunas identificadas.

<!-- review:begin br-lic-20261106-atropine_sulfate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN **não retornou indicações previstas** nesta consulta (26/03/2026), provavelmente porque o fármaco não foi localizado na base regulatória brasileira consultada (0 registros encontrados).” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 5 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atropine_sulfate-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos registros consultados |
| Nova Indicação Prevista | Sem previsão disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — apenas predição de modelo, sem dados reais acessíveis |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

A consulta à base regulatória não retornou nenhum registro para **ATROPINE SULFATE**.

> Atropina é um medicamento de uso amplamente estabelecido; recomenda-se verificar o cadastro sob termos alternativos (ex.: "ATROPINA", "ATROPINA SULFATO") antes de concluir pela ausência de comercialização.

<!-- review:begin br-lic-20261106-atropine_sulfate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “> **Atenção:** A ausência de registros pode refletir uma divergência de grafia ou identificador, e **não necessariamente** indica que o fármaco não está disponível no Brasil. Atropina é um medicamento de uso amplamente estabelecido; recomenda-se verificar o cadastro sob termos alternativos (ex.: "ATROPINA", "ATROPINA SULFATO") antes de concluir pela ausência de comercialização.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 5 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atropine_sulfate-2 -->

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém indicações previstas pelo TxGNN, dados regulatórios, mecanismo de ação (MOA) nem informações de segurança — o que torna inviável qualquer análise de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**

- **[DG001 — Bloqueante]** Localizar e baixar a bula ANVISA (fonte: ANVISA) para extrair advertências, contraindicações e precauções
- **[DG002 — Alta prioridade]** Obter o DrugBank ID e informações de MOA via DrugBank API, necessários para a análise de plausibilidade mecanística
- **Verificação de cadastro:** Re-consultar a base ANVISA com grafias alternativas ("ATROPINA", "ATROPINA SULFATO", "ATROPINE") para confirmar se há registro ativo
- **Re-execução do pipeline:** Após obter o DrugBank ID correto, re-executar o TxGNN para gerar indicações previstas com pontuação e evidências associadas

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “(0 registros encontrados)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “**Atenção:** A ausência de registros pode refletir uma divergência de grafia ou identificador, e **não necessariamente** indica que o fármac” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

