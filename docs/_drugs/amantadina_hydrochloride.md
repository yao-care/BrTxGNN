---
layout: default
title: Amantadina Hydrochloride
parent: Apenas Predição do Modelo (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
drugbank_id: DB00915
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
last_modified_at: 2026-11-24
description: "Amantadina Hydrochloride: nova indicação prevista, Encefalite subaguda de Rasmussen (Rasmussen subacute encephalitis) (nível de evidência L5). Indicação original: ANTIPARKINSONIANOS"
---

# Amantadina Hydrochloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Amantadina Hydrochloride: Encefalite subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumo em Uma Frase

A amantadina (cloridrato de amantadina) é um medicamento classificado como antiparkinsoniano no registro local.
O modelo TxGNN prevê que pode ser eficaz para **Encefalite subaguda de Rasmussen (Rasmussen subacute encephalitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTIPARKINSONIANOS |
| Nova Indicação Prevista | Encefalite subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Pontuação de Previsão TxGNN | 0.9948 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Amantadina Hydrochloride (tradução não oficial): “O mecanismo pelo qual a amantadina exerce eficácia no tratamento da discinesia em pacientes com doença de Parkinson ou como tratamento adjuvante à levodopa/carbidopa em pacientes com doença de Parkinson que apresentam episódios 'off' é desconhecido. A amantadina é um antagonista incompetitivo fraco do receptor NMDA.” Texto original em inglês: "The mechanism by which amantadine exerts efficacy in the treatment of dyskinesia in patients with Parkinson's disease or as adjunctive treatment to levodopa/carbidopa in patients with Parkinson's disease experiencing 'off' episodes is unknown. Amantadine is a weak uncompetitive antagonist of the NMDA receptor." ([DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28), versão de 2026-10-05; acessado em 2026-11-19). Sabe-se, de forma geral, que a amantadina atua como antagonista do receptor NMDA e modula a transmissão dopaminérgica.

A encefalite de Rasmussen é uma doença neuroinflamatória de origem imunomediada, que costuma cursar com crises epilépticas e atrofia progressiva de um hemisfério cerebral. Hipóteses sobre excitotoxicidade mediada por glutamato (por exemplo, envolvendo anticorpos anti-GluR3) sugerem um racional teórico para a modulação de receptores NMDA.

Esse racional é apenas teórico. Não há ensaios clínicos nem literatura nos dados compilados que sustentem o uso da amantadina nessa doença, e a pontuação do modelo, por si só, não substitui evidência clínica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 100431410 | MANTIDAN | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (0,9948), mas não há nenhum estudo clínico ou publicação sobre a encefalite de Rasmussen; o nível de evidência é L5, baseado apenas no modelo.

**Para prosseguir, é necessário:**
- Levantamento da literatura e de ensaios específicos sobre amantadina em encefalite de Rasmussen, incluindo relatos de caso.
- Dados detalhados do mecanismo de ação (MOA) e sua relação com a fisiopatologia da doença.
- Informações de segurança da bula da ANVISA (advertências e contraindicações), ainda não disponíveis.
- Avaliação de viabilidade da via de administração e da população-alvo (doença rara, em geral pediátrica).

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A ausência de registros no mercado brasileiro e a falta do DrugBank ID impedem o mapeamento do fármaco na rede de conhecimento TxGNN, inviab” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “A consulta ao banco de dados regulatório brasileiro retornou **0 registros** para o nome "AMANTADINA HYDROCHLORIDE"” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco não possui registros no mercado brasileiro e não gerou previsões TxGNN” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Gocovri (amantadine) prescribing information, Adamas Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82ff865f-78f3-4c94-b6a9-727a54944b28) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

