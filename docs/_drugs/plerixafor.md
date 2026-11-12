---
layout: default
title: Plerixafor
parent: Apenas Predição do Modelo (L5)
nav_order: 531
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
description: "Plerixafor: nova indicação prevista, CMM7 (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Plerixafor
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Plerixafor: CMM7
{: .text-alpha }

## Resumo em Uma Frase

Plerixafor é um antagonista do receptor CXCR4, usado como mobilizador de células-tronco hematopoéticas em pacientes com mieloma múltiplo (mieloma de plasmócitos) e linfoma não Hodgkin que farão transplante autólogo.
O modelo TxGNN prevê que ele pode ser eficaz para **mieloma de plasmócitos indolente (indolent plasma cell myeloma)**.
Até o momento, **nenhum ensaio clínico** e **nenhuma publicação** apoiam esta previsão específica, que se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | CMM7 |
| Pontuação de Previsão TxGNN | 0.9934 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações farmacológicas conhecidas, o plerixafor bloqueia o receptor CXCR4 (e também interage com o ACKR3). Com isso, interrompe o eixo CXCR4/CXCL12, que mantém as células na medula óssea.

Esse eixo ancora as células de mieloma de plasmócitos no nicho da medula óssea. A hipótese é que bloqueá-lo possa afetar a permanência e a sobrevivência dessas células. Isso torna a previsão plausível do ponto de vista biológico, mas é apenas uma hipótese.

É preciso cautela. No mieloma, o plerixafor é usado principalmente para mobilizar células-tronco antes do transplante, e não como tratamento dirigido à doença. Não há dados, nem de estudos nem de literatura, para a forma indolente. A pontuação alta do TxGNN é uma previsão computacional, não uma demonstração de eficácia.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

- **Contraindicações indicadas pelo grafo de conhecimento do TxGNN** (não provêm do texto da bula): trombocitopenia, insuficiência renal e leucemia. Esses itens servem apenas como sinal de alerta e precisam ser confirmados na bula oficial.
- Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para o mieloma indolente é apenas computacional (L5), sem ensaios clínicos nem literatura. O plerixafor atua hoje no mieloma como mobilizador de células-tronco, não como terapia contra a doença.
- As advertências e contraindicações da bula da ANVISA não estão disponíveis.

<!-- review:begin br-lic-20261106-plerixafor-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O medicamento não tem registro no Brasil, e as advertências e contraindicações da bula da ANVISA não estão disponíveis.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 3 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-plerixafor-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações), pois isso bloqueia a triagem de segurança.
- Obter dados detalhados do mecanismo de ação (MOA) em fonte curada.
- Realizar estudos pré-clínicos ou clínicos que testem o bloqueio de CXCR4 no mieloma indolente.
- Avaliar o cenário regulatório no Brasil.
- Considerar outra indicação prevista para o mesmo fármaco com evidências muito mais robustas: a **leucemia mieloide**, com 24 ensaios clínicos de fase 1 e 2 (por exemplo NCT00512252 e NCT00906945). Ela atingiu nível L2, mas sem ensaios de fase 3, e merece avaliação em separado.

<!-- review:begin br-lic-20261106-plerixafor-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Avaliar o cenário regulatório no Brasil, já que não há registro vigente.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 3 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-plerixafor-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O medicamento não tem registro no Brasil, e a” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que não há registro vigente” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

