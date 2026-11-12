---
noindex: true
sitemap: false
layout: default
title: Binimetinibe
parent: Apenas Predição do Modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Binimetinibe
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

## Binimetinibe: Avaliação de Reposicionamento – Previsões TxGNN Pendentes
{: .text-alpha }

## Resumo

Binimetinibe é um inibidor de MEK1/MEK2 (terapia-alvo) utilizado no tratamento do melanoma com mutação BRAF V600E/K, em combinação com encorafenibe.
O Evidence Pack atual **não contém previsões de novas indicações** geradas pelo modelo TxGNN, impossibilitando a análise completa de reposicionamento neste ciclo.
O fármaco está comercializado no Brasil com 2 registros.

<!-- review:begin br-lic-20261106-binimetinibe-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco está comercializado no Brasil com 2 registros, mas os detalhes dos registros e dados de segurança não foram populados nesta versão do pack.” Removido: a afirmação contradizia os dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-binimetinibe-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Melanoma com mutação BRAF V600E/K (inibidor de MEK) |
| Nova Indicação Prevista | Pendente – sem previsões TxGNN disponíveis |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

Binimetinibe pertence à classe dos inibidores de MEK, categorizada como terapia-alvo antineoplásica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (Inibidor de MEK1/MEK2 – classe MAPK pathway) |
| Risco de Mielossupressão | Baixo a médio (menos pronunciado que quimioterapia citotóxica convencional) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Fração de ejeção ventricular esquerda (FEVE), acuidade visual, função hepática, CBC com diferencial, pressão arterial |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações (`predicted_indications: []`), e os campos de registro regulatório e segurança estão sem dados, o que impede qualquer avaliação de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN para gerar previsões de novas indicações para Binimetinibe
- Recuperar dados de MOA do DrugBank — a consulta retornou 1 resultado (`result_status: success`) mas o campo `drugbank_id` e `original_moa` não foram populados; verificar a extração
- Baixar e analisar a bula da ANVISA para preencher advertências principais e contraindicações (DG001 – severidade Blocking)
- Consultar banco de dados de interações medicamentosas (DDI) com nome alternativo ou sinônimos, pois a consulta atual retornou `not_found`

<!-- review:begin br-lic-20261106-binimetinibe-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Executar o pipeline TxGNN para gerar previsões de novas indicações para Binimetinibe / Preencher os detalhes dos 2 registros da ANVISA (número de registro, nome comercial, forma farmacêutica, indicação aprovada) — a consulta TFDA retornou 2 resultados mas os campos foram devolvidos vazios” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-binimetinibe-2 -->

<!-- review:begin br-lic-20261106-binimetinibe-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Baixar e analisar a bula da ANVISA/TFDA para preencher advertências principais e contraindicações (DG001 – severidade Blocking)” Removido: a afirmação contradizia os dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-binimetinibe-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “mas os detalhes dos registros e dados de segurança não foram populados nesta versão do pack” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Preencher os detalhes dos 2 registros da ANVISA (número de registro, nome comercial, forma farmacêutica, indicação aprovada) — a consulta TF” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “A/TFD” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

