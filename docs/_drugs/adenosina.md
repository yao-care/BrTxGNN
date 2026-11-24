---
layout: default
title: Adenosina
parent: Apenas Predição do Modelo (L5)
nav_order: 30
evidence_level: L5
indication_count: 1
drugbank_id: DB00640
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-11-24
description: "Adenosina: nova indicação prevista, bloqueio de ramo obsoleto (obsolete bundle branch block) (nível de evidência L5). No Brasil, registros na ANVISA: 23 (ativos: 5)"
---

# Adenosina
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

## Adenosina: bloqueio de ramo obsoleto (obsolete bundle branch block)
{: .text-alpha }

## Resumo em Uma Frase

Adenosina é um fármaco com registros ativos no Brasil, mas o texto de indicação aprovada não consta nos dados locais.
O modelo TxGNN prevê, como principal nova indicação, **bloqueio de ramo obsoleto (obsolete bundle branch block)**, um termo marcado como obsoleto na ontologia de doenças, sem nenhum ensaio clínico e sem nenhuma publicação que apoie esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | bloqueio de ramo obsoleto (obsolete bundle branch block) |
| Pontuação de Previsão TxGNN | 0.9994 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 23) |
| Número de Registros | 23 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Adenosina (tradução não oficial): “A Adenosina Injetável retarda o tempo de condução através do nó A-V, pode interromper as vias de reentrada através do nó A-V e pode restaurar o ritmo sinusal normal em pacientes com taquicardia supraventricular paroxística (TSVP), incluindo a TSVP associada à síndrome de Wolff-Parkinson-White. A Adenosina Injetável é antagonizada competitivamente por metilxantinas, como a cafeína e a teofilina, e potencializada por bloqueadores do transporte de nucleosídeos, como o dipiridamol.” Texto original em inglês: "Adenosine Injection slows conduction time through the A-V node, can interrupt the reentry pathways through the A-V node, and can restore normal sinus rhythm in patients with paroxysmal supraventricular tachycardia (PSVT), including PSVT associated with Wolff-Parkinson-White Syndrome. Adenosine Injection is antagonized competitively by methylxanthines such as caffeine and theophylline, and potentiated by blockers of nucleoside transport such as dipyridamole." ([DailyMed: adenosine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9508caf5-0e3a-4d32-909d-bff7ea40ec30), versão de 2026-08-31; acessado em 2026-11-19). Sabe-se, pela farmacologia geral, que a adenosina retarda a condução no nó atrioventricular e pode causar bloqueio AV transitório.

Isso torna a previsão pouco plausível do ponto de vista terapêutico: um fármaco que reduz a condução não tem fundamento claro para tratar um bloqueio de ramo. A associação provavelmente reflete o uso diagnóstico da adenosina para desmascarar doenças de condução, e não um benefício terapêutico.

Além disso, o termo da doença está marcado como obsoleto na ontologia, ou seja, é provavelmente um rótulo descontinuado ou fundido com outro conceito. Sem remapeamento para um conceito clínico atual, a previsão não é interpretável. Trata-se de um sinal apenas computacional, sem respaldo clínico.

## Informações de Comercialização no Brasil

Há 23 registros no total, dos quais 5 válidos (4 de produto isolado e 1 em associação) e 18 cancelados. Os registros estão listados abaixo; os dados locais não trazem forma farmacêutica nem texto de indicação aprovada.

<!-- review:begin br-lic-20261124b-adenosina-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “Os registros válidos de produto isolado estão listados abaixo” Corrigido conforme os dados abertos de medicamentos da ANVISA: a tabela desta seção inclui todos os registros do medicamento (de princípio ativo único e em associação, válidos e cancelados), e não só os descritos na frase. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124b-adenosina-1 -->

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 103110176 | ADENOSINA | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Ativo |
| 103110180 | LOWE | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Ativo |
| 110110054 | ADENOSINA | NEWCOM FARMACEUTICA LTDA. | Ativo |
| 113430182 | ADENOSINA | HIPOLABOR FARMACEUTICA LTDA | Ativo |
| 167730285 | NATUS GERIN | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100020089 | TIAMINA + ASSOCIAÇÕES | LABORATORIO SEDABEL LTDA | Cancelado |
| 100330038 | ADENOCARD | LIBBS FARMACÊUTICA LTDA | Cancelado |
| 100410233 | ADENOSINA | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100470115 | FÓRMULA 28 | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 102350011 | ANEKRON | EMS S/A | Cancelado |
| 102940104 | BIOHEPAX | NEOLATINA COMÉRCIO E INDÚSTRIA FARMACEUTICA S.A | Cancelado |
| 104650405 | GERIVIX | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 105730072 | GERIATON | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Cancelado |
| 105770019 | NECRO B 6 | LABORATIL FARMACEUTICA LTDA | Cancelado |
| 105830085 | NATUS GERIN | GERMED FARMACEUTICA LTDA | Cancelado |
| 105830176 | FOSFOCAPS | GERMED FARMACEUTICA LTDA | Cancelado |
| 113050021 | MULTIVIMS PLUS | LUMA INDUSTRIA FARMACEUTICA LTDA | Cancelado |
| 115600051 | HEPATOX | CIFARMA CIENTÍFICA FARMACÊUTICA LTDA | Cancelado |
| 116950033 | VITFORTE | LABORATÓRIO FARMACÊUTICO VITAMED LTDA | Cancelado |
| 121100120 | EPOCLER | PFIZER BRASIL LTDA | Cancelado |
| 133460008 | CHOFRAFIG | BIO MACRO LABORATÓRIO FARMACÊUTICO LTDA | Cancelado |
| 142570060 | EPATOZIN | LUCIOMED FARMACÊUTICA DO BRASIL LTDA | Cancelado |
| 172870347 | GERIVIX | HYPERA S.A. | Cancelado |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem pontuação alta (0,9994), mas não conta com ensaios clínicos nem literatura, o termo da doença é obsoleto e o mecanismo conhecido da adenosina (retardo da condução AV) vai contra um benefício terapêutico.

**Para prosseguir, é necessário:**
- Remapear o termo obsoleto para um conceito de doença atual e reavaliar a previsão.
- Obter o mecanismo de ação detalhado do fármaco.
- Baixar e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem esses dados.
- Só então buscar estudos clínicos ou publicações que abordem diretamente a condição.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Adenosina é um nucleosídeo endógeno com presença consolidada no mercado brasileiro, contando com **20 registros ativos**” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco possui **20 registros ativos** no mercado brasileiro, confirmando disponibilidade comercial ampla. Contudo, os detalhes individuai” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: adenosine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9508caf5-0e3a-4d32-909d-bff7ea40ec30) |
| 2026-11-24 | “Os registros válidos de produto isolado estão listados abaixo” → “Os registros estão listados abaixo” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

