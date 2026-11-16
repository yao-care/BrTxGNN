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
last_modified_at: 2026-11-16
description: "Adenosina: nova indicação prevista, bloqueio de ramo obsoleto (obsolete bundle branch block) (nível de evidência L5). Indicação original: Não consta nos dados locais"
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

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Sabe-se, pela farmacologia geral, que a adenosina retarda a condução no nó atrioventricular e pode causar bloqueio AV transitório.

Isso torna a previsão pouco plausível do ponto de vista terapêutico: um fármaco que reduz a condução não tem fundamento claro para tratar um bloqueio de ramo. A associação provavelmente reflete o uso diagnóstico da adenosina para desmascarar doenças de condução, e não um benefício terapêutico.

Além disso, o termo da doença está marcado como obsoleto na ontologia, ou seja, é provavelmente um rótulo descontinuado ou fundido com outro conceito. Sem remapeamento para um conceito clínico atual, a previsão não é interpretável. Trata-se de um sinal apenas computacional, sem respaldo clínico.

## Informações de Comercialização no Brasil

Há 23 registros no total, dos quais 5 válidos (4 de produto isolado e 1 em associação) e 18 cancelados. Os registros válidos de produto isolado estão listados abaixo; os dados locais não trazem forma farmacêutica nem texto de indicação aprovada.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 103110176 | Adenosina | Não informada | Não informada |
| Registro 103110180 | Lowe | Não informada | Não informada |
| Registro 110110054 | Adenosina | Não informada | Não informada |
| Registro 113430182 | Adenosina | Não informada | Não informada |

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

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Adenosina é um nucleosídeo endógeno com presença consolidada no mercado brasileiro, contando com **20 registros ativos**” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco possui **20 registros ativos** no mercado brasileiro, confirmando disponibilidade comercial ampla. Contudo, os detalhes individuai” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

