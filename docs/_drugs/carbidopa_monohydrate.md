---
noindex: true
sitemap: false
layout: default
title: Carbidopa Monohydrate
parent: Apenas Predição do Modelo (L5)
nav_order: 192
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Carbidopa Monohydrate
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

## CARBIDOPA MONOHYDRATE: Avaliação de Reposicionamento — Dados Insuficientes para Previsão
{: .text-alpha }

## Resumo em Uma Frase

CARBIDOPA MONOHYDRATE é um fármaco cujas indicações originais não foram identificadas no banco de dados regulatório consultado.
O modelo TxGNN **não gerou previsões de reposicionamento** para este composto na execução atual,
e **não há ensaios clínicos nem publicações** vinculados a candidatos de reposicionamento neste Evidence Pack.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não identificada nos dados disponíveis |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — apenas previsão do modelo, sem estudos reais |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 6) |
| Número de Registros | 6 (ativos: 6) |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. O campo `original_moa` está ausente, o DrugBank ID não foi confirmado, e nenhuma indicação original foi registrada.

Sem indicações de origem e sem previsões TxGNN geradas, não é possível estabelecer a relação farmacológica entre indicação original e nova indicação, nem conduzir análise mecanística de reposicionamento.

Para avançar na análise, é necessário primeiro preencher as lacunas de dados identificadas (ver Próximos Passos).

---

## Informações de Comercialização no Brasil

Nenhuma licença foi identificada no banco de dados regulatório consultado.

<!-- review:begin br-lic-20261106-carbidopa_monohydrate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “CARBIDOPA MONOHYDRATE não possui registros ativos no Brasil. Nenhuma licença foi identificada no banco de dados regulatório consultado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 6 registros para este medicamento, 6 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-carbidopa_monohydrate-1 -->

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não gerou previsões de reposicionamento para este fármaco, e os dados essenciais — indicações originais, mecanismo de ação, registro regulatório e perfil de segurança — estão todos ausentes. Não há base suficiente para emitir recomendação de reposicionamento.

**Para prosseguir, é necessário:**
- Confirmar o **DrugBank ID** para CARBIDOPA MONOHYDRATE e consultar a API do DrugBank para obter MOA, categorias e perfil de toxicidade
- Verificar a grafia exata do INN junto à ANVISA (o termo "MONOHYDRATE" pode ser um modificador salino — o princípio ativo canônico é **carbidopa**; buscar também sob esse nome)
- Baixar a **bula ANVISA** (quando registrado) ou referência internacional para extrair indicações originais, advertências e contraindicações
- Reexecutar o **pipeline TxGNN** com DrugBank ID e indicações confirmadas para gerar candidatos de reposicionamento
- Avaliar se o fármaco deve ser pesquisado em combinação (carbidopa é frequentemente coformulado com levodopa — verificar se a entrada correta no pipeline deve ser a combinação ou o monocomponente)

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “CARBIDOPA MONOHYDRATE não possui registros ativos no Brasil” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

