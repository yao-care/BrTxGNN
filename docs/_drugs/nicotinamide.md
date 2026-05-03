---
layout: default
title: Nicotinamide
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Nicotinamide
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

A skill foi consultada — aplica-se ao contexto TxGNN, mas a geração de relatório de farmacologista é conduzida pelo prompt do sistema. Prossigo diretamente com a análise do Evidence Pack e geração do relatório.

**Decisão editorial antes de escrever:**
O Evidence Pack é multi-indicação (10 previsões). A previsão de rank 1 (zinc, elevated plasma, 97.83%) foi explicitamente avaliada como **falso positivo provável do grafo** — todos os 10 ensaios clínicos recuperados receberam grau C e as 2 publicações são indiretas. A indicação com maior suporte evidencial real é **Werner syndrome (rank 4, L3, Proceed with Guardrails)**, com 1 RCT duplo-cego publicado em 2025 e mecanismo NAD⁺/PARP/WRN bem estabelecido. O relatório focará em Werner syndrome como candidata principal, com nota explicativa sobre o rank 1.

---

# Nicotinamide: De Precursor de NAD⁺ à Síndrome de Werner

## Resumo em Uma Frase

Nicotinamide é a forma amida da vitamina B3, funcionando como principal precursor de NAD⁺ pela via de salvagem intracelular (NAMPT), sem registro aprovado no Brasil.
O modelo TxGNN identificou 10 potenciais novas indicações; a candidata com melhor suporte evidencial é a **Síndrome de Werner (Werner Syndrome)**, apoiada por **1 RCT duplo-cego** e **6 estudos celulares e de revisão** que sustentam a conexão via depleção de NAD⁺ e disfunção mitocondrial.
A previsão de maior pontuação bruta (zinc, elevated plasma, 97.83%) foi avaliada internamente como provável falso positivo do grafo de conhecimento e recebeu decisão **Hold**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil |
| Nova Indicação Prevista | Síndrome de Werner (Werner Syndrome) |
| Pontuação de Previsão TxGNN | 88.61% (Rank #4) |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

> **Nota sobre o Rank #1:** O TxGNN atribuiu pontuação de 97.83% para "zinc, elevated plasma". Esta previsão foi avaliada como **provável falso positivo do grafo**: embora zinco seja cofator metálico de enzimas NAD⁺-dependentes (PARP, SIRT), trata-se de relação indireta e inespecífica, insuficiente para sustentar "tratamento de hiperzincemia plasmática". Todos os 10 ensaios e 2 publicações recuperadas foram avaliados como grau C (sem relevância direta). **Decisão: Hold.**

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no banco de dados consultado. Com base no conhecimento estabelecido, Nicotinamide é a forma amida da niacina (vitamina B3) e o precursor de NAD⁺ pela **via de salvagem NAMPT** — enzima que converte Nicotinamide em NMN, que por sua vez gera NAD⁺. Este caminho é distinto do nicotinamide riboside (NR, que usa a quinase NRK) e do NMN (entrada direta), tornando os três compostos farmacologicamente relacionados mas metabolicamente não equivalentes. Esta distinção é fundamental para interpretar as evidências disponíveis.

A Síndrome de Werner (WS) é uma doença de envelhecimento prematuro causada por mutações no gene *WRN*, que codifica uma DNA helicase RecQ essencial para reparo de DNA e replicação. A perda funcional de WRN provoca: (1) ativação excessiva de PARP-1, que consome NAD⁺ como substrato para reparo de dano ao DNA; (2) depleção progressiva de NAD⁺ intracelular — confirmada diretamente em células WRN-deficientes em 2025 (PMID 40179319); (3) comprometimento de SIRT1/SIRT3 (sirtuínas dependentes de NAD⁺); (4) disfunção mitocondrial e mitofagia prejudicada; resultando no fenótipo de envelhecimento acelerado característico da doença.

Nicotinamide pode atuar em múltiplos pontos desta cascata: elevar NAD⁺ intracelular via NAMPT, restaurar a atividade de SIRT1/SIRT3, promover mitofagia funcional, e pela **inibição competitiva leve de PARP**, reduzir o consumo de NAD⁺. O elo mecanístico foi reforçado em 2025 por um RCT duplo-cego com nicotinamide riboside (NR) em pacientes WS (PMID 40459998), confirmando que a reposição de NAD⁺ é eficaz clinicamente. A diferença de via metabólica (NRK para NR vs. NAMPT para Nicotinamide) exige validação comparativa, mas não invalida a hipótese — ela define os guardrails necessários.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos registrados utilizando Nicotinamide especificamente para Síndrome de Werner.

O único RCT disponível utiliza **Nicotinamide Riboside (NR)** — molécula relacionada que compartilha o alvo terapêutico (reposição de NAD⁺) mas usa via metabólica distinta. Este estudo está sumarizado nas Evidências da Literatura abaixo.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/) | 2025 | RCT Duplo-cego | Aging Cell | NR em pacientes WS: ensaio crossover duplo-cego placebo-controlado demonstrou que suplementação de NAD⁺ melhora condição de pacientes com Síndrome de Werner |
| [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/) | 2019 | Pré-clínico | Nature Communications | Suplementação de NAD⁺ restaura mitofagia e limita envelhecimento acelerado em modelos in vitro e in vivo de WS; PARP-1 como principal consumidor de NAD⁺ |
| [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/) | 2025 | Celular | Aging | NAD⁺ mitocondrial reduzido em células WRN-deficientes ligado diretamente a proliferação disfuncional; confirma alvo terapêutico |
| [24757718](https://pubmed.ncbi.nlm.nih.gov/24757718/) | 2014 | Celular | Aging Cell | Depleção de WRN provoca desvio metabólico comprometendo homeostase redox e geração de equivalentes redutores; limita proliferação celular |
| [38184705](https://pubmed.ncbi.nlm.nih.gov/38184705/) | 2024 | Celular | Cell & Bioscience | Perda de WRN acelera adipogênese anormal in vitro (células-tronco) e in vivo (zebrafish); disfunção metabólica como fenótipo central de WS |
| [34201700](https://pubmed.ncbi.nlm.nih.gov/34201700/) | 2021 | Review | Int J Mol Sci | Revisão de dano ao DNA e neurodegeneração em síndromes de envelhecimento acelerado; WS contextualizado no espectro de doenças de reparo de DNA |
| [33353663](https://pubmed.ncbi.nlm.nih.gov/33353663/) | 2021 | Review | J Invest Dermatol | Anormalidades cutâneas em doenças com deficiência de reparo de DNA e disfunção mitocondrial; sobreposição fenotípica com WS discutida |

> ⚠️ **Nota de curadoria:** PMID 13469243 (1957) — recuperado pelo sistema por ser de autor "WERNER I" e mencionar "isonicotinamide" — é um estudo sobre arritmia cardíaca sem relação com Síndrome de Werner (WS é epônimo de Otto Werner). Excluído por ser falso positivo semântico.

---

## Resumo de Todas as Previsões TxGNN

| Rank | Indicação | Pontuação | Evidência | Decisão | Nota |
|------|-----------|-----------|-----------|---------|------|
| 1 | Zinc, elevated plasma | 97.83% | L5 | Hold | Falso positivo provável — relação indireta via cofator metálico de enzimas NAD⁺-dependentes |
| 2 | Isolated congenital adermatoglyphia | 94.85% | L5 | Hold | Doença genética (SMARCAD1/DNA helicase); sem cruzamento com via NAD⁺ |
| 3 | Beare-Stevenson cutis gyrata syndrome | 93.68% | L5 | Hold | Doença genética (FGFR2 ativado); sem intersecção conhecida com NAD⁺/PARP |
| **4** | **Werner syndrome** | **88.61%** | **L3** | **Proceed with Guardrails** | **Mecanismo NAD⁺/WRN/PARP bem fundamentado; RCT 2025 com NR confirma alvo** |
| 5 | PAPA syndrome | 87.28% | L5 | Hold | Autoinflamatório (PSTPIP1/NLRP3/IL-1β); sem antagonismo direto por Nicotinamide |
| 6 | Demodicidosis of sebaceous gland | 85.53% | L5 | Hold | Infestação parasitária por Demodex; Nicotinamide sem ação antiparasitária direta |
| 7 | Dyspepsia | 84.69% | L4 | Hold | Alta dose de Nicotinamide pode **causar** dispepsia — efeito adverso, não terapêutico |
| 8 | OXPHOS disorder (DNA nuclear) | 84.65% | L4 | Research Question | Mecanismo NAD⁺ plausível; sem evidência clínica direta — candidato para investigação básica |
| 9 | Inherited cutis laxa | 82.47% | L5 | Hold | Defeito em fibras elásticas (ELN/FBLN5); sem mecanismo de reparo por Nicotinamide |
| 10 | Syndromic oculocutaneous albinism | 81.74% | L5 | Hold | Defeito em melanossomo (HPS genes); Nicotinamide inibe transferência — direção oposta |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota prática para o contexto WS:** Nicotinamide em doses elevadas (>3 g/dia) pode causar hepatotoxicidade e comprometer tolerância à glicose. Pacientes com Síndrome de Werner já apresentam resistência à insulina e diabetes como comorbidades frequentes — o perfil de dose e monitoramento glicêmico é uma consideração crítica para qualquer protocolo de uso.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A Síndrome de Werner possui mecanismo de doença claramente centrado na depleção de NAD⁺ (PARP/WRN → disfunção mitocondrial → envelhecimento acelerado), confirmado por estudos celulares recentes e por um RCT duplo-cego de 2025 com molécula precursora de NAD⁺ relacionada (NR). A ausência de registro no Brasil e a diferença metabólica entre Nicotinamide e NR são os principais fatores de cautela, não bloqueadores de avanço.

**Para prosseguir, é necessário:**
- **Validação comparativa de NAD⁺:** Estudo in vitro comparando Nicotinamide vs NR vs NMN em células WRN-deficientes — medir elevação de NAD⁺ intracelular e mitocondrial por cada via
- **Dados de MOA:** Obter perfil farmacológico completo via DrugBank API (gap DG002 identificado no pack)
- **Registro ANVISA:** Pré-requisito obrigatório para qualquer ensaio clínico conduzido no Brasil
- **Protocolo de monitoramento:** Glicemia de jejum e função hepática (ALT/AST) para uso prolongado — especialmente crítico em pacientes WS com diabetes já estabelecido
- **Dose-finding:** Definir janela terapêutica entre dose eficaz para elevar NAD⁺ e dose que induz dispepsia/hepatotoxicidade
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

