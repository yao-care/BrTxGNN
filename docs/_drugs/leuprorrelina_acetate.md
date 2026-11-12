---
noindex: true
sitemap: false
layout: default
title: Leuprorrelina Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 403
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Leuprorrelina Acetate
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

## LEUPRORRELINA ACETATE: Avaliação Inconclusiva — Dados Insuficientes para Análise de Reposicionamento
{: .text-alpha }

## Resumo em Uma Frase

Leuprorrelina (Leuprorelin) é um agonista do hormônio liberador de gonadotrofinas (GnRH), amplamente utilizado no tratamento de cânceres hormônio-sensíveis, endometriose e puberdade precoce.
O modelo TxGNN **não gerou indicações previstas** para este fármaco neste ciclo de avaliação, possivelmente devido ao nome incorreto na consulta ("LEUPRORRELINA" em vez do INN padronizado "LEUPRORELIN").
Sem previsão de nova indicação e sem registros no Brasil, não é possível avançar para análise de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma (modelo TxGNN retornou lista vazia) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | **L5** — Sem previsão de modelo, sem estudos reais |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão não foi Gerada?

Há dois prováveis motivos para o modelo TxGNN não ter retornado indicações previstas:

1. **Erro tipográfico no INN**: O nome consultado foi `LEUPRORRELINA ACETATE` (com duplo "R"), enquanto o INN padronizado é `LEUPRORELIN ACETATE`. Isso pode ter impedido o mapeamento correto ao DrugBank e, consequentemente, ao grafo de conhecimento.

2. **DrugBank ID ausente**: O campo `drugbank_id` está vazio, o que impede o pipeline de conhecimento de localizar as relações do fármaco no grafo. O log indica que a consulta ao DrugBank retornou 1 resultado (`result_count: 1`), mas o ID não foi transferido para o Evidence Pack — indicando falha na extração ou integração.

Esses dois fatores combinados impedem a execução do modelo de previsão, tornando o relatório de reposicionamento inaplicável neste ciclo.

---

## Informações de Comercialização no Brasil

Nenhuma licença foi identificada na consulta à ANVISA.

<!-- review:begin br-lic-20261106-leuprorrelina_acetate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco não possui registros ativos no Brasil. Nenhuma licença foi identificada na consulta à ANVISA.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 2 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-leuprorrelina_acetate-1 -->

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem indicações previstas pelo TxGNN e sem registros regulatórios no Brasil, não há base suficiente para iniciar a análise de reposicionamento. O problema é de ordem técnica e pode ser resolvido antes da próxima execução.

**Para prosseguir, é necessário:**

- [ ] **Corrigir o INN**: Usar o nome padronizado `LEUPRORELIN ACETATE` (remover o "R" duplicado) em todos os campos de consulta
- [ ] **Recuperar o DrugBank ID**: O log indica que o DrugBank retornou 1 resultado — extrair e registrar o `drugbank_id` correspondente (provavelmente `DB00007`)
- [ ] **Re-executar o pipeline TxGNN** com os dados corrigidos para obter `predicted_indications`
- [ ] **Coletar dados de segurança (DG001)**: Baixar a bula ANVISA/FDA para extrair advertências e contraindicações
- [ ] **Coletar MOA (DG002)**: Consultar DrugBank API com o ID correto para obter o mecanismo de ação formal

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco não possui registros ativos no Brasil” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

