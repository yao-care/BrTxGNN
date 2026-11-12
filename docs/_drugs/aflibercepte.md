---
noindex: true
sitemap: false
layout: default
title: Aflibercepte
parent: Apenas Predição do Modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Aflibercepte
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

## Aflibercepte: Avaliação de Reposicionamento — Dados Insuficientes para Previsão TxGNN
{: .text-alpha }

## Resumo

O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco nesta versão do Evidence Pack,
e há lacunas de dados críticas — incluindo ausência de MOA e dados de segurança — que impedem a avaliação completa de reposicionamento.

<!-- review:begin br-lic-20261106-aflibercepte-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Aflibercepte (AFLIBERCEPTE) é um fármaco atualmente comercializado no Brasil com 4 registros ativos na ANVISA. / O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco nesta versão do Evidence Pack,” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 6 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-aflibercepte-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível (detalhes das licenças ausentes) |
| Nova Indicação Prevista | Sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | Não aplicável |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 6) |
| Número de Registros | 6 (ativos: 5) |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação de aflibercepte neste Evidence Pack. A consulta ao DrugBank retornou 1 resultado com sucesso, mas os dados não foram integrados ao relatório — é necessário verificar o pipeline de ingestão para recuperar o MOA.

Sem previsões TxGNN disponíveis e sem indicação original mapeada, não é possível estabelecer a relação mecanística entre indicação de origem e nova indicação candidata. Esta seção será atualizada assim que os dados de MOA e as previsões do modelo forem incorporados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack atual carece dos três pilares mínimos para avaliação de reposicionamento: previsão TxGNN, mecanismo de ação e dados de segurança. A tomada de decisão sem esses elementos seria tecnicamente infundada.

**Para prosseguir, é necessário:**

- **[Bloqueante — DG001]** Baixar e analisar as bulas da ANVISA para as 4 licenças registradas, a fim de extrair advertências principais e contraindicações
- **[Alta Prioridade — DG002]** Consultar DrugBank API para recuperar MOA — a query já retornou 1 resultado com sucesso, verificar integração dos dados no pipeline
- **[Essencial]** Executar o modelo TxGNN para gerar previsões de novas indicações para aflibercepte
- **[Complementar]** Recuperar os detalhes completos das 4 licenças brasileiras: número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Aflibercepte (AFLIBERCEPTE) é um fármaco atualmente comercializado no Brasil com 4 registros ativos na ANVISA” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

