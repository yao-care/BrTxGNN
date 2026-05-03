---
layout: default
title: Biperiden
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Biperiden
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Biperiden: Do Parkinsonismo à Encefalite Subaguda de Rasmussen

## Resumo em Uma Frase

Biperiden é um agente anticolinérgico utilizado no tratamento da doença de Parkinson e das síndromes extrapiramidais induzidas por medicamentos.
O modelo TxGNN prevê que pode ser eficaz para **Encefalite Subaguda de Rasmussen (Rasmussen Subacute Encephalitis)**, porém atualmente **sem ensaios clínicos registrados** e **sem publicações científicas** que apoiem diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson; síndrome extrapiramidal induzida por medicamentos |
| Nova Indicação Prevista | Encefalite Subaguda de Rasmussen (Rasmussen Subacute Encephalitis) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 13 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base no conhecimento farmacológico estabelecido, Biperiden é um antagonista seletivo dos receptores muscarínicos do subtipo M1, que atua bloqueando os efeitos da acetilcolina no sistema nervoso central e periférico. Na doença de Parkinson, seu benefício clínico deriva do reequilíbrio entre as vias dopaminérgica e colinérgica nos gânglios basais, aliviando a rigidez e o tremor de repouso.

A Encefalite de Rasmussen é uma doença autoimune progressiva mediada predominantemente por linfócitos T citotóxicos, tendo anticorpos anti-GluR3 e anti-NR2B como mediadores patogênicos. Clinicamente, manifesta-se por atrofia cortical unilateral progressiva e epilepsia focal contínua refratária. As terapias com comprovação de eficácia são exclusivamente imunomoduladoras — imunoglobulina intravenosa, plasmaférese, tacrolimus — ou cirúrgicas (hemisferiectomia funcional). O mecanismo anticolinérgico M1 do Biperiden não apresenta intersecção farmacológica conhecida com a cascata autoimune nem com os mecanismos epileptogênicos centrais desta condição.

A alta pontuação do TxGNN (0,9994) reflete, muito provavelmente, o efeito de proximidade no grafo de conhecimento (*graph proximity*): nós relacionados a "doenças inflamatórias do SNC" estão topologicamente próximos aos alvos conhecidos do Biperiden no grafo, gerando uma pontuação elevada sem que exista mecanismo biológico direto que sustente a previsão do ponto de vista terapêutico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Biperiden possui **13 registros ativos** no mercado brasileiro. Os detalhes individuais de cada registro — número de registro, nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste pacote de evidências e devem ser consultados diretamente na base de dados da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para a Encefalite de Rasmussen não possui suporte em ensaios clínicos nem na literatura científica publicada (nível de evidência L5), e o mecanismo anticolinérgico M1 do Biperiden não apresenta plausibilidade biológica para uma patologia essencialmente autoimune e epiléptica.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA junto ao DrugBank (DB00810) e verificar se existem vias secundárias com potencial de modulação imunológica ou antiepiléptica
- Consultar a bula completa na ANVISA para avaliação de advertências, contraindicações e interações medicamentosas relevantes
- Revisar os 13 registros brasileiros na base de dados da ANVISA para confirmar indicações aprovadas e formas farmacêuticas disponíveis
- Avaliar indicações de ranques mais baixos com maior plausibilidade mecanística, como a **PLAN (PLA2G6-associated neurodegeneration, rank 3)** e o **Hunt Juvenile Paralysis Agitans (rank 7)**, que apresentam racional de extensão da indicação antiparkinsoniana com potencial de "Research Question"
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

