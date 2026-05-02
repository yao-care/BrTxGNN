---
layout: default
title: Tafamidis
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

Usando o skill `txgnn-pipeline` como referência de contexto. Agora vou gerar o relatório com base no Evidence Pack fornecido.

---

# Tafamidis: Da Amiloidose por Transtirretina ao Transtorno Primário de Liberação de Plaquetas

## Resumo em Uma Frase

Tafamidis é um estabilizador cinético da proteína transtirretina (TTR), utilizado no tratamento da cardiomiopatia por amiloidose de transtirretina (ATTR-CM) e da polineuropatia amiloide hereditária por TTR (ATTR-PN).
O modelo TxGNN prevê que pode ser eficaz para o **Transtorno Primário de Liberação de Plaquetas (Primary Release Disorder of Platelets)**, porém atualmente **não há ensaios clínicos** nem **publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Amiloidose por Transtirretina (ATTR-CM / ATTR-PN) |
| Nova Indicação Prevista | Transtorno Primário de Liberação de Plaquetas (Primary Release Disorder of Platelets) |
| Pontuação de Previsão TxGNN | 89,27% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Tafamidis atua como estabilizador cinético do tetrâmero da transtirretina (TTR), ligando-se com alta afinidade aos dois sítios de ligação da tiroxina presentes na proteína. Essa ligação impede a dissociação do tetrâmero em monômeros, bloqueando a cascata que leva à formação e deposição de fibrilas amiloides no miocárdio e nos nervos periféricos — base do mecanismo de eficácia comprovado em ATTR-CM e ATTR-PN.

O transtorno primário de liberação de plaquetas é uma condição intrínseca à biologia plaquetária, envolvendo disfunção nos grânulos alfa e densos, sinalização de exocitose e eventos como a exposição da fosfatidilserina na superfície da membrana plaquetária. Todos esses processos pertencem a vias de ativação celular específicas das plaquetas e **não apresentam qualquer interseção conhecida** com o metabolismo, a estabilidade estrutural ou a homeostase da proteína TTR.

A análise de plausibilidade mecanística da própria plataforma TxGNN classifica esta previsão como **provável falso positivo**: a pontuação elevada (89,27%) provavelmente reflete proximidade topológica entre nós de doenças hematológicas e nós de doenças sistêmicas no grafo de conhecimento, e não uma associação biológica real. A ausência completa de literatura ou ensaios clínicos reforça esta conclusão.

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
A previsão de Tafamidis para o transtorno primário de liberação de plaquetas não possui qualquer sustentação mecanística — a estabilização do tetrâmero TTR não tem relação identificada com os mecanismos de liberação de grânulos plaquetários. Nenhum ensaio clínico ou publicação científica apoia esta indicação, e a análise de plausibilidade a classifica como falso positivo do modelo.

**Para prosseguir, seria necessário:**
- Identificar uma hipótese mecanística plausível que conecte a estabilização de TTR à função plaquetária
- Realizar busca sistematizada na literatura de estudos pré-clínicos sobre TTR e plaquetas
- Auditar o grafo de conhecimento do TxGNN para identificar a origem da associação entre estes dois nós de doença
---

