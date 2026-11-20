---
layout: default
title: Aflibercepte
parent: Apenas Predição do Modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 1
drugbank_id: DB08885
monitor_inn: "Aflibercept"
predicted_indications: ["esotropia"]
last_modified_at: 2026-11-20
description: "Aflibercepte: nova indicação prevista, Esotropia (nível de evidência L5). No Brasil, registros na ANVISA: 6 (ativos: 5)"
---

# Aflibercepte
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Aflibercepte: Esotropia
{: .text-alpha }

## Resumo em Uma Frase

Aflibercepte é uma proteína de fusão recombinante que age como "armadilha" de fatores de crescimento vasculares (VEGF-A, VEGF-B e PlGF).
O modelo TxGNN prevê que pode ser eficaz para **Esotropia (esotropia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Esotropia |
| Pontuação de Previsão TxGNN | 0.9938 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 6) |
| Número de Registros | 6 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Aflibercepte (tradução não oficial): “O fator de crescimento endotelial vascular A (VEGF-A) e o fator de crescimento placentário (PlGF) são membros da família VEGF de fatores angiogênicos que podem atuar como fatores mitogênicos, quimiotáticos e de permeabilidade vascular para as células endoteliais. O VEGF atua por meio de dois receptores tirosina-quinase, VEGFR-1 e VEGFR-2, presentes na superfície das células endoteliais. […] Os produtos à base de aflibercepte atuam como um receptor solúvel chamariz que se liga ao VEGF-A e ao PlGF e, desse modo, pode inibir a ligação e a ativação desses receptores cognatos de VEGF.” Texto original em inglês: "Vascular endothelial growth factor-A (VEGF-A) and placental growth factor (PlGF) are members of the VEGF family of angiogenic factors that can act as mitogenic, chemotactic, and vascular permeability factors for endothelial cells. VEGF acts via two receptor tyrosine kinases, VEGFR-1 and VEGFR-2, present on the surface of endothelial cells. […] Aflibercept products act as a soluble decoy receptor that binds VEGF - A and PlGF, and thereby can inhibit the binding and activation of these cognate VEGF receptors." ([DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06), versão de 2026-10-29; acessado em 2026-11-19). Segundo informações conhecidas, o aflibercepte se liga ao VEGF-A, ao VEGF-B e ao fator de crescimento placentário (PlGF), impedindo que estimulem a formação e a permeabilidade de vasos sanguíneos. É usado em doenças vasculares da retina.

A esotropia é um desvio do alinhamento ocular, causado sobretudo por fatores neuromusculares, refrativos ou de desenvolvimento sensorial. Não há, nos dados compilados, uma via mecanística que ligue a inibição do VEGF à esotropia. Uma ligação plausível, mas não verificada, seria indireta: doenças vasculares da retina (como a retinopatia da prematuridade) e déficits sensoriais podem se associar a estrabismo. Assim, o sinal do modelo pode refletir comorbidade ou proximidade nos dados de treinamento, e não um efeito terapêutico.

Apesar da pontuação alta, a injeção intraocular de anti-VEGF não é um tratamento estabelecido para esotropia. A previsão deve ser tratada como hipótese, sem suporte clínico até o momento.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102440027 | PAVBLU | Não informada | Não registrada |
| Registro 116640011 | YESAFILI | Não informada | Não registrada |
| Registro 170560097 | EYLIA | Não informada | Não registrada |
| Registro 183260338 | ZALTRAP | Não informada | Não registrada |
| Registro 192160007 | EYDENZELT | Não informada | Não registrada |

Há 6 registros no total, dos quais 5 estão válidos e 1 cancelado (um registro antigo do ZALTRAP, omitido da tabela acima).

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações sobre aflibercepte em esotropia, e não há mecanismo plausível que sustente a previsão. O nível de evidência é L5, apesar da pontuação alta do modelo.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), hoje ausentes.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Revisão de literatura e de registros de ensaios para verificar se há qualquer relato de anti-VEGF em estrabismo/esotropia.
- Avaliar a via de administração (intravítrea) e sua compatibilidade com a nova indicação, ainda pendente.
- Estudos pré-clínicos ou mecanísticos que justifiquem uma hipótese biológica antes de qualquer investimento clínico.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Aflibercepte (AFLIBERCEPTE) é um fármaco atualmente comercializado no Brasil com 4 registros ativos na ANVISA” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

