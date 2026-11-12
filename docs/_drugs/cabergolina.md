---
noindex: true
sitemap: false
layout: default
title: Cabergolina
parent: Apenas Predição do Modelo (L5)
nav_order: 169
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Cabergolina
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

## Cabergolina: Avaliação de Reposicionamento — Dados Insuficientes para Previsão
{: .text-alpha }

## Resumo em Uma Frase

Cabergolina é um agonista dopaminérgico utilizado principalmente no tratamento da hiperprolactinemia e da doença de Parkinson.
O presente Evidence Pack **não contém previsões TxGNN** para novas indicações — o campo `predicted_indications` está vazio — portanto não é possível avaliar candidatos de reposicionamento neste ciclo.

<!-- review:begin br-lic-20261106-cabergolina-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O presente Evidence Pack **não contém previsões TxGNN** para novas indicações — o campo `predicted_indications` está vazio — portanto não é possível avaliar candidatos de reposicionamento neste ciclo. / Existem **20 registros** da substância no mercado brasileiro, porém os detalhes dos registros não foram recuperados nesta execução.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 25 registros para este medicamento, 15 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-cabergolina-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste pack (registros sem detalhes) |
| Nova Indicação Prevista | — (sem previsão TxGNN) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 25) |
| Número de Registros | 25 (ativos: 15) |
| Decisão Recomendada | **Hold** |

---

## Por que Este Relatório Está Incompleto?

Há dois bloqueios críticos identificados no `meta.data_gaps`:

<!-- review:begin br-lic-20261106-cabergolina-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Este Evidence Pack foi gerado com **dados parciais**: apenas a consulta ao banco regulatório brasileiro (TFDA/ANVISA) e ao DrugBank foram executadas, mas os campos de retorno dos registros estão em branco (campos `license_number`, `product_name_zh`, `approved_indication_text` todos vazios).” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-cabergolina-2 -->

| ID | Item Faltante | Severidade | Impacto |
|----|--------------|-----------|---------|
| DG001 | ANVISA — advertências e contraindicações da bula | **Bloqueante** | Impede avaliação inicial de segurança |
| DG002 | Mecanismo de ação (MOA) | Alta | Impede análise de relevância mecanística |

Adicionalmente, o campo `predicted_indications` retornou **lista vazia**, o que significa que o pipeline TxGNN não gerou candidatos de reposicionamento para CABERGOLINA neste ciclo. Sem candidatos, não há base para avaliação de nova indicação.

---

## Informações de Comercialização no Brasil

Os 20 registros existem no sistema regulatório, mas os detalhes não foram recuperados nesta execução do pipeline. A tabela abaixo não pode ser preenchida:

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431274 | CABERGOLINA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100630307 | CABERGOLINA | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 102351161 | CABERGOLINA | EMS S/A | Ativo |
| 102980410 | CABEREDUX | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 102980442 | CABERGOLINA | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 105830808 | CABERGOLINA | GERMED FARMACEUTICA LTDA | Ativo |
| 110390214 | CABERGOLINA | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Ativo |
| 110630134 | CABERGOLINA | FUNDAÇÃO OSWALDO CRUZ | Ativo |
| 118190331 | CABERGOLINA | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 121100412 | DOSTINEX | PFIZER BRASIL LTDA | Ativo |
| 122140091 | CABERTRIX | ADIUM S.A. | Ativo |
| 123520266 | CABERGOLINA | RANBAXY FARMACÊUTICA LTDA | Ativo |
| 125680257 | CABERGOLINA | PRATI DONADUZZI & CIA LTDA | Ativo |
| 146820083 | CABERGOLINA | SUN FARMACÊUTICA DO BRASIL LTDA | Ativo |
| 198830001 | CABERGOLINA | FUNDAÇÃO BAIANA DE PESQ. CIENTIFICA E DESENV.  TEC | Ativo |
| 102160140 | DOSTINEX | LABORATÓRIOS PFIZER LTDA | Cancelado |
| 102980409 | CABERGOLINA | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Cancelado |
| 104920229 | CABERGOLINA | BIOLAB FARMA GENERICOS LTDA | Cancelado |
| 109220064 | ADEGRIP | H B FARMA LABORATÓRIOS LTDA | Cancelado |
| 122140090 | CABERGOLINA | ADIUM S.A. | Cancelado |
| 123890061 | DOSTINEX | PHARMACIA BRASIL LTDA | Cancelado |
| 126750197 | CABERGOLINA | NOVA QUIMICA FARMACÊUTICA S/A | Cancelado |
| 135690677 | CABERGOLINA | EMS SIGMA PHARMA LTDA | Cancelado |
| 167730428 | CABERGOLINA | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 167730433 | BERGOX | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |

> **Ação necessária:** Executar novamente a consulta ao portal ANVISA com extração completa dos campos de cada registro.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações e os dados regulatórios de detalhe não foram recuperados, tornando impossível qualquer análise de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**

1. **Reexecutar a consulta regulatória** — recuperar os campos `license_number`, `product_name_zh`, `dosage_form` e `approved_indication_text` dos 20 registros ANVISA de Cabergolina
2. **Corrigir o pipeline TxGNN** — investigar por que `predicted_indications` retornou vazio; verificar se o mapeamento DrugBank foi bem-sucedido (query_log id=3 indica `success` com 1 resultado, mas o `drugbank_id` ficou `null`)
3. **Preencher o MOA (DG002)** — consultar DrugBank API com o ID recuperado para obter o mecanismo de ação e categorias do fármaco
4. **Baixar e parsear a bula (DG001)** — obter advertências e contraindicações do PDF da bula ANVISA para liberar a avaliação de segurança
5. **Reprocessar o pack** — após as correções acima, gerar novo Evidence Pack versão v5 com dados completos

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Existem **20 registros** da substância no mercado brasileiro, porém os detalhes dos registros não foram recuperados nesta execução” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Este Evidence Pack foi gerado com **dados parciais**: apenas a consulta ao banco regulatório brasileiro (TFDA/ANVISA) e ao DrugBank foram ex” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

