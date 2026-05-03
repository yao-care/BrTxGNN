---
layout: default
title: Paliperidona Palmitate
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 0
---

# Paliperidona Palmitate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# PALIPERIDONA PALMITATE: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

---

## Resumo em Uma Frase

Paliperidona Palmitato é a formulação injetável de longa duração (LAI) da paliperidona — metabólito ativo da risperidona —, originalmente utilizada no tratamento da esquizofrenia e do transtorno esquizoafetivo.
Neste ciclo de análise, o modelo TxGNN **não gerou nenhuma previsão de reposicionamento**, possivelmente em razão da ausência de DrugBank ID no Evidence Pack ou falha no mapeamento do composto.
Não há ensaios clínicos nem publicações vinculados a novas indicações neste relatório.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Esquizofrenia / Transtorno esquizoafetivo (conhecimento clínico geral; sem registro ANVISA confirmado) |
| Nova Indicação Prevista | Nenhuma previsão gerada neste ciclo |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D — sem previsão disponível |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há previsão a avaliar neste ciclo. O Evidence Pack não contém indicações previstas pelo TxGNN, o que impede qualquer análise de reposicionamento fundamentada em dados do modelo.

Com base no conhecimento clínico geral, a paliperidona palmitato é um éster de palmitato de paliperidona, administrado por via intramuscular em formulação de liberação prolongada (mensal ou trimestral). O mecanismo de ação da paliperidona envolve o antagonismo dos receptores dopaminérgicos D₂ e serotoninérgicos 5-HT₂A — perfil farmacológico compartilhado por outros antipsicóticos atípicos de segunda geração. Teoricamente, compostos com esse mecanismo têm sido investigados em condições como transtorno bipolar com características psicóticas, transtorno depressivo maior com características psicóticas e agitação relacionada à demência.

Contudo, sem DrugBank ID, sem MOA formalizado no Evidence Pack e sem previsões TxGNN, nenhuma análise de reposicionamento pode ser conduzida de forma confiável neste ciclo. As lacunas identificadas precisam ser resolvidas antes de avançar.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto — ausência de DrugBank ID, nenhuma previsão TxGNN gerada, dados de segurança indisponíveis e nenhum registro no mercado brasileiro. Não há base suficiente para avaliar o potencial de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**
- Identificar e inserir o DrugBank ID correto para PALIPERIDONA PALMITATE (paliperidona: provavelmente DB06016; verificar se a forma palmitato possui ID próprio)
- Re-executar o pipeline TxGNN com o DrugBank ID correto para gerar previsões de indicação
- Obter dados de segurança (advertências principais, contraindicações) da bula oficial (ANVISA, FDA ou EMA)
- Obter dados de MOA detalhados via DrugBank API
- Verificar registro junto à ANVISA — o medicamento é comercializado em outros países (ex: Invega Sustenna®, Invega Trinza®) e pode ter sido submetido para registro no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

