---
layout: default
title: Piracetam
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Piracetam
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

Com base no `txgnn-pipeline` skill (que se aplica ao contexto BrTxGNN / geração de relatórios de reposicionamento), vou agora gerar o relatório conforme o Evidence Pack fornecido.

---

# Piracetam: Do Comprometimento Cognitivo à Osteoartrite

## Resumo em Uma Frase

Piracetam é um nootrópico da classe racetam, historicamente utilizado para comprometimento cognitivo, mioclonia e outras condições neurológicas do sistema nervoso central.
O modelo TxGNN prevê possível eficácia em **Osteoartrite (Osteoarthritis)**, porém atualmente **não há ensaios clínicos nem publicações** específicas de Piracetam para esta indicação — e a plausibilidade biológica é baixa, com a alta pontuação provavelmente refletindo ruído topológico no grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Comprometimento cognitivo, mioclonia (dados regulatórios detalhados não disponíveis neste pack) |
| Nova Indicação Prevista | Osteoartrite (Osteoarthritis) |
| Pontuação de Previsão TxGNN | 98,45% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros ANVISA | 15 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados formais de mecanismo de ação registrados no Evidence Pack. Com base nas informações disponíveis na literatura farmacológica, Piracetam pertence à classe dos racetams e atua principalmente no sistema nervoso central por meio de três mecanismos propostos: modulação positiva de receptores AMPA (que melhora a transmissão glutamatérgica), aumento da fluidez das membranas neuronais, e potencialização do sistema colinérgico. Possui também efeito antiagregante plaquetário com relevância clínica em condições trombóticas.

A osteoartrite é uma doença degenerativa articular cuja fisiopatologia envolve degradação da matriz de cartilagem mediada por metaloproteases (MMP-1, MMP-13), ativação inflamatória local por IL-1β e TNF-α, e sobrecarga biomecânica nas articulações. Não há qualquer intersecção conhecida entre os mecanismos SNC de Piracetam e essa cascata fisiopatológica periférica. O efeito antiagregante poderia, em teoria altamente especulativa, influenciar a microcirculação sinovial — mas trata-se de uma extrapolação sem qualquer suporte em dados pré-clínicos ou clínicos.

A pontuação TxGNN de 98,45% para osteoartrite quase certamente reflete um artefato de agrupamento topológico no grafo de conhecimento: doenças musculoesqueléticas (osteoartrite, artrite reumatoide, gota, pseudoacondroplasia, braquiolmia) formam um cluster denso no KG, e fármacos com conexões indiretas nessa região tendem a receber scores elevados sem respaldo biológico real. Das 10 indicações previstas para Piracetam (ranks 1–10), todas são classificadas como L5 e recebem recomendação Hold — padrão consistente com ruído sistêmico do modelo, e não com sinal biológico genuíno.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

> **⚠️ Nota sobre qualidade das buscas:** Nas buscas para indicações de rank 3 (artrite reumatoide) e rank 5 (porfiria hepática), foram recuperados artigos sobre **Levetiracetam** — um antiepiléptico estruturalmente distinto — e não sobre Piracetam. Esses resultados não constituem evidência para reposicionamento de Piracetam e não foram incluídos neste relatório. Recomenda-se revisão do pipeline de recuperação de literatura para evitar contaminação cruzada por similaridade de nome.

---

## Informações de Comercialização no Brasil

O Evidence Pack registra **15 registros** de Piracetam comercializados no Brasil (status: já comercializado). Os dados detalhados de cada registro — número ANVISA, nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis nesta versão do pack (campos em branco). Consulte o sistema **DATAVISA/ANVISA** para informações completas dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para osteoartrite carece de plausibilidade mecanística — os mecanismos conhecidos de Piracetam (SNC/colinérgico/AMPA) não se alinham com a fisiopatologia musculoesquelética da osteoartrite, e a ausência total de ensaios clínicos ou publicações relevantes confirma que esta linha de pesquisa ainda não foi investigada de forma alguma. O mesmo padrão se repete nas 10 indicações previstas: todas L5, todas Hold, sem exceção.

**Para prosseguir, é necessário:**
- Recuperar os dados regulatórios completos da ANVISA: indicações aprovadas e texto integral da bula (advertências, contraindicações)
- Verificar se existem estudos pré-clínicos (modelos animais de OA) com Piracetam ou análogos racetam não indexados no PubMed
- Corrigir o pipeline de busca de literatura para eliminar recuperação de artigos sobre Levetiracetam quando a query é Piracetam
- Reavaliar a qualidade das previsões TxGNN para Piracetam com filtro de plausibilidade mecanística, a fim de distinguir sinal biológico real de ruído topológico do KG
- Caso haja interesse em avançar para L4, considerar modelos pré-clínicos de osteoartrite em roedores como prova de conceito antes de qualquer investimento clínico
---

