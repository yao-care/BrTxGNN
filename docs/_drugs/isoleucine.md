---
layout: default
title: Isoleucine
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 1
---

# Isoleucine
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

---

# Isoleucina: De aminoácido essencial à gastroparesia

## Resumo em Uma Frase

Isoleucina (Isoleucine) é um aminoácido essencial de cadeia ramificada (BCAA), conhecido principalmente por seu papel na nutrição e no metabolismo proteico, sem indicações terapêuticas formalmente aprovadas no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **gastroparesia (Gastroparesis)**,
porém atualmente **não há ensaios clínicos nem publicações científicas** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Suplemento de aminoácido essencial (uso nutricional) |
| Nova Indicação Prevista | Gastroparesia (Gastroparesis) |
| Pontuação de Previsão TxGNN | 99.32% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Isoleucina é um aminoácido essencial de cadeia ramificada (BCAA) sem indicações farmacoterapêuticas formalmente aprovadas. Atualmente, não há dados detalhados sobre seu mecanismo de ação específico para condições gastrointestinais — seu papel primário é nutricional, participando da síntese proteica e do metabolismo energético muscular.

A conexão teórica entre isoleucina e a gastroparesia pode ser explicada por três vias indiretas: (1) células L intestinais detectam aminoácidos luminais e secretam GLP-1/GLP-2, hormônios que modulam o esvaziamento gástrico; (2) a sinalização BCAA → mTOR pode influenciar a função do sistema nervoso entérico; (3) a isoleucina estimula a secreção de insulina, e a gastroparesia de origem diabética está associada a deficiências na sinalização insulínica.

Contudo, todos esses mecanismos são especulativos e indiretos — não há experimento ou estudo clínico demonstrando que isoleucina, isoladamente, melhora o esvaziamento gástrico. A alta pontuação do TxGNN (99.32%) provavelmente reflete raciocínio de múltiplos saltos no grafo de conhecimento (*metabolismo de aminoácidos → complicações diabéticas → gastroparesia*), e não evidências clínicas diretas. Esta previsão deve ser interpretada com cautela considerável.

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
Não há nenhuma evidência clínica ou pré-clínica direta apoiando o uso de isoleucina para gastroparesia; a previsão do TxGNN é classificada como L5 — exclusivamente baseada em inferências computacionais do grafo de conhecimento, sem qualquer respaldo experimental ou regulatório.

**Para prosseguir, é necessário:**
- Levantamento bibliográfico ampliado sobre o papel de BCAAs (e isoleucina especificamente) na motilidade gastrointestinal
- Estudos pré-clínicos em modelos animais de gastroparesia com isoleucina ou misturas BCAA
- Dados de mecanismo de ação (MOA) obtidos via DrugBank API ou revisão de literatura
- Verificação de segurança: advertências, contraindicações e interações medicamentosas por meio de bula ou bases de dados regulatórias (ANVISA, DrugBank)
- Avaliação de viabilidade da via de administração e forma farmacêutica adequada para a indicação proposta
---

