---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Tramadol
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

A skill `txgnn-pipeline` foi verificada — não impõe restrições adicionais ao formato do relatório. Prosseguindo com a geração do relatório com base no Evidence Pack fornecido.

---

# Tramadol: Da analgesia à displasia acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Tramadol é um analgésico de ação central amplamente utilizado no controle de dor moderada a grave, atuando por duplo mecanismo: agonismo opioide μ e inibição da recaptação de norepinefrina e serotonina.
O modelo TxGNN prevê que pode ser eficaz para a **Displasia Acromesomélica tipo Hunter-Thompson (Acromesomelic Dysplasia, Hunter-Thompson Type)**, porém esta previsão conta com **0 ensaios clínicos** e **0 publicações** de suporte, constituindo exclusivamente uma predição algorítmica sem evidência clínica real.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgesia (dor moderada a grave) — detalhes de registro não disponíveis no pacote atual |
| Nova Indicação Prevista | Displasia Acromesomélica tipo Hunter-Thompson |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base em conhecimento farmacológico estabelecido, o Tramadol é um analgésico de ação central que atua por dois mecanismos simultâneos: agonismo nos receptores opioides μ (com potência inferior à morfina) e inibição da recaptação de norepinefrina e serotonina — efeito análogo ao de um inibidor de recaptação de serotonina e noradrenalina (IRSN). Esta combinação confere eficácia tanto em dores nociceptivas quanto neuropáticas.

A displasia acromesomélica tipo Hunter-Thompson é uma doença óssea rara de herança autossômica recessiva, causada por mutações no gene **CDMP1/GDF5**, que resultam em encurtamento desproporcional dos segmentos intermediários e distais dos membros. Não existe tratamento modificador de doença disponível; o manejo é essencialmente sintomático, e pacientes frequentemente desenvolvem dor crônica musculoesquelética associada às deformidades estruturais, podendo demandar suporte analgésico ao longo da vida.

A conexão prevista pelo TxGNN, contudo, reflete uma limitação estrutural conhecida dos modelos de grafo de conhecimento: o Tramadol apresenta ampla conectividade ao nó genérico de "dor" no grafo, o que gera associações com diversas condições dolorosas — incluindo displasias esqueléticas raras — sem sobreposição mecanística real com a fisiopatologia da doença subjacente. A previsão é biologicamente plausível apenas como manejo sintomático de dor, **não como reposicionamento terapêutico modificador de doença**. O alto score (99,99%) reflete a centralidade do nó de dor no grafo, e não evidência de eficácia específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Tramadol possui **20 registros ativos** no Brasil (ANVISA). Os dados detalhados de cada registro — nome comercial, forma farmacêutica e indicação aprovada — não constam do pacote de evidências atual e devem ser consultados diretamente no portal da ANVISA ([consulmed.anvisa.gov.br](https://consulmed.anvisa.gov.br/)).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ **Nota importante**: O FDA emite **advertência de caixa preta (black box warning)** para uso de Tramadol em pacientes com menos de 12 anos de idade, em razão de risco de depressão respiratória grave — informação relevante para as indicações pediátricas previstas pelo modelo (JIA, displasias congênitas). Recomenda-se obtenção e revisão das bulas da ANVISA antes de qualquer avaliação clínica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para a displasia acromesomélica tipo Hunter-Thompson apresenta nível de evidência **L5** — ausência total de ensaios clínicos e literatura de suporte específicos. A pontuação elevada (99,99%) decorre de associação genérica ao nó de "dor" no grafo de conhecimento, sem sobreposição com a fisiopatologia da doença (mutação CDMP1/GDF5 → defeito no desenvolvimento esquelético). O Tramadol pode ter papel sintomático em doenças raras com dor crônica, mas isso caracteriza uso off-label analgésico convencional, **não reposicionamento terapêutico**.

**Para prosseguir, é necessário:**
- Baixar e analisar as bulas registradas na ANVISA para extrair advertências, contraindicações e interações medicamentosas (DG001 — Blocking)
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API (DG002 — High)
- Verificar se há consenso clínico ou diretrizes de sociedades de doenças raras sobre uso de opioides fracos em displasias esqueléticas congênitas
- Reavaliar o pipeline de predição para distinguir reposicionamento mecanístico de uso sintomático analgésico, evitando falsos positivos estruturais no grafo de conhecimento

---

*Relatório gerado automaticamente com base em Evidence Pack v4 — Data de corte: 2026-05-02. Este relatório é exclusivamente para fins de pesquisa e não constitui recomendação clínica ou aconselhamento médico.*
---

