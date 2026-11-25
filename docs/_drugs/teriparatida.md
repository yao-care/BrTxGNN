---
layout: default
title: Teriparatida
parent: Apenas Predição do Modelo (L5)
nav_order: 616
evidence_level: L5
indication_count: 9
drugbank_id: DB06285
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
last_modified_at: 2026-11-25
description: "Teriparatida: nova indicação prevista, Duodenal ulcer (disease) (nível de evidência L5). No Brasil, registros na ANVISA: 5 (ativos: 5)"
---

# Teriparatida
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Teriparatida: Duodenal ulcer (disease)
{: .text-alpha }

## Resumo em Uma Frase

Teriparatida é um fármaco osteoanabólico, análogo do hormônio paratireoidiano (PTH 1-34), comercializado no Brasil, com registros válidos (números atualizados no resumo rápido e na tabela de registros).
O modelo TxGNN prevê que pode ser eficaz para **úlcera duodenal (duodenal ulcer)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

<!-- review:begin br-lic-20261125-teriparatida-1 -->

> **Correção de verificação (2026-11-25)**: Texto original: “comercializado no Brasil em quatro registros válidos.” Corrigido conforme os dados abertos de medicamentos da ANVISA: o número ou a situação dos registros informado não correspondia aos dados; o texto não traz mais números fixos, e os números atualizados estão no resumo rápido e na tabela de registros desta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261125-teriparatida-1 -->

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Duodenal ulcer (disease) |
| Pontuação de Previsão TxGNN | 0.9986 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Teriparatida (tradução não oficial): “O paratormônio (PTH) endógeno de 84 aminoácidos é o principal regulador do metabolismo do cálcio e do fosfato no osso e no rim. As ações fisiológicas do PTH incluem a regulação do metabolismo ósseo, a reabsorção tubular renal de cálcio e fosfato e a absorção intestinal de cálcio. […] As ações biológicas do PTH e da teriparatida são mediadas pela ligação a receptores específicos de alta afinidade na superfície celular.” Texto original em inglês: "Endogenous 84-amino acid parathyroid hormone (PTH) is the primary regulator of calcium and phosphate metabolism in bone and kidney. Physiological actions of PTH include regulation of bone metabolism, renal tubular reabsorption of calcium and phosphate, and intestinal calcium absorption. […] The biological actions of PTH and teriparatide are mediated through binding to specific high-affinity cell-surface receptors." ([DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c), versão de 2026-08-31; acessado em 2026-11-19). Pelo conhecimento geral, a teriparatida atua como agonista do receptor PTH1R e estimula a formação óssea, o que explica seu uso como fármaco osteoanabólico.

Não há vínculo mecanístico crível entre essa ação e a úlcera duodenal. A teriparatida não tem papel estabelecido na supressão da acidez gástrica nem na cicatrização da mucosa duodenal. A pontuação alta do TxGNN é uma previsão computacional, sem respaldo de ensaios clínicos ou de literatura. Por isso, a previsão deve ser tratada como hipótese a ser examinada, e não como direção terapêutica com base sólida.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101180680 | FORZY | APSEN FARMACEUTICA S/A | Ativo |
| 112600079 | FORTEO | ELI LILLY DO BRASIL LTDA | Ativo |
| 115410026 | BONMIDE | CIPLA BRASIL IMPORTADORA E DISTRIBUIDORA DE MEDICA | Ativo |
| 155370135 | SONDELBAY | ACCORD FARMACÊUTICA LTDA | Ativo |
| 191290004 | TERROSA | GEDEON RICHTER DO BRASIL IMPORTADORA, EXPORTADORA  | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem publicações sobre teriparatida em úlcera duodenal, e o mecanismo de ação do fármaco não sustenta plausibilidade biológica para essa indicação. A previsão se baseia apenas na pontuação do modelo.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação (MOA) e de uma justificativa biológica para o trato gastrointestinal
- Estudos pré-clínicos que mostrem algum efeito sobre a mucosa duodenal
- Texto de bula da ANVISA com advertências e contraindicações para a triagem de segurança
- Revisão do texto de indicação aprovada nos registros locais

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c) |
| 2026-11-25 | “comercializado no Brasil em quatro registros válidos.” → “comercializado no Brasil, com registros válidos (números atualizados no resumo rápido e na tabela de registros).” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

