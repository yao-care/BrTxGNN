---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

O skill `txgnn-pipeline` é focado em operações de pipeline técnico (treino, deploy, debugging) e não se aplica à escrita de relatórios de avaliação. Prossigo diretamente com a geração do relatório.

---

# Itraconazol: De infecções fúngicas à pneumocistose

## Resumo em Uma Frase

Itraconazol é um antifúngico triazólico de amplo espectro, historicamente utilizado no tratamento de infecções fúngicas sistêmicas e superficiais como aspergilose, candidíase e onicomicose.
O modelo TxGNN prevê que pode ser eficaz para **Pneumocistose (Pneumocystosis)**, porém **não há ensaios clínicos** nem **publicações científicas** apoiando esta direção — trata-se exclusivamente de uma previsão algorítmica, com evidências mecanísticas apontando para **falso positivo**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções fúngicas sistêmicas e superficiais (aspergilose, candidíase, onicomicose, histoplasmose) |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 99,34% |
| Nível de Evidência | L5 — apenas previsão do modelo, sem estudos reais |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Itraconazol atua inibindo a **lanosterol 14α-desmetilase**, uma enzima dependente do citocromo P450 fúngico. Ao bloquear essa via, o fármaco impede a síntese de **ergosterol** — o esterol essencial para a integridade da membrana celular da maioria dos fungos patogênicos. Sem ergosterol funcional, a membrana perde estabilidade e o fungo morre. Este mecanismo explica o amplo espectro de ação do itraconazol em aspergilose, candidíase e outras micoses.

No entanto, a pneumocistose é causada por *Pneumocystis jirovecii*, um fungo fenotipicamente atípico que **não sintetiza ergosterol**. A membrana de *P. jirovecii* é composta predominantemente por **colesterol derivado do hospedeiro humano**, tornando o alvo farmacológico do itraconazol inexistente neste patógeno. Trata-se de uma **incompatibilidade mecanística fundamental (mechanistic mismatch)**: o fármaco não tem onde agir.

A elevada pontuação do TxGNN (99,34%) reflete, na prática, uma **generalização categórica** do grafo de conhecimento, que associou itraconazol a "infecções fúngicas" de forma ampla, sem distinção entre fungos ergosterol-dependentes e não-dependentes. Clinicamente, nenhum azólico é empregado no tratamento da pneumocistose: a primeira linha é **TMP-SMX** (trimetoprima-sulfametoxazol), com **pentamidina** e **atovaquona** como alternativas. Esta previsão deve ser interpretada como um artefato do modelo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
*Pneumocystis jirovecii* não contém ergosterol — o único alvo farmacológico confirmado do itraconazol — tornando esta indicação **mecanisticamente inviável**. A ausência total de ensaios clínicos e literatura de apoio, combinada com a análise de incompatibilidade de alvo, confirma que a previsão do TxGNN é um **falso positivo** por generalização categórica, não um candidato real a reposicionamento.

**Para reconsiderar esta decisão, seria necessário:**
- Identificação de um mecanismo de ação alternativo do itraconazol sobre *P. jirovecii* (ex.: inibição de vias de colesterol, efeito imunomodulador no hospedeiro ou outra hipótese mecanisticamente sustentável)
- Dados de estudos pré-clínicos demonstrando atividade *in vitro* ou *in vivo* contra *P. jirovecii*
- Revisão do pipeline TxGNN para incorporar a distinção ergosterol vs. colesterol como critério de filtragem de falsos positivos em previsões de antifúngicos
---

