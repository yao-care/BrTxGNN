---
layout: default
title: Tocopherol
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
---

# Tocopherol
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

Com base no Evidence Pack fornecido, aqui está o relatório de avaliação:

---

# Tocopherol: De Antioxidante Vitamínico (Vitamina E) à Colangite Esclerosante

## Resumo em Uma Frase

Tocopherol é a forma ativa da Vitamina E, amplamente reconhecido como antioxidante lipossolúvel com papel essencial na proteção de membranas celulares contra peroxidação lipídica — sem indicação farmacêutica formalmente registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Colangite Esclerosante (Sclerosing Cholangitis)**,
atualmente com **1 ensaio clínico** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação farmacêutica aprovada no Brasil |
| Nova Indicação Prevista | Colangite Esclerosante (Sclerosing Cholangitis) |
| Pontuação de Previsão TxGNN | 98,84% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no banco de dados consultado. Segundo informações amplamente estabelecidas na literatura científica, Tocopherol (Vitamina E) é o principal antioxidante lipossolúvel do organismo: interrompe reações em cadeia de peroxidação lipídica, neutraliza radicais livres derivados do oxigênio (ROS) e preserva a integridade de membranas celulares em tecidos sob alta carga oxidativa. Sua eficácia como agente antioxidante está bem documentada, e mecanisticamente pode ser aplicável à colangite esclerosante.

A colangite esclerosante — especialmente a forma primária (PSC) — é caracterizada por inflamação progressiva, fibrose e destruição dos ductos biliares. A colestase resultante compromete gravemente a absorção de vitaminas lipossolúveis (A, D, E e K), levando à depleção sistêmica de Tocopherol e à redução da capacidade antioxidante plasmática. Dados observacionais confirmam que pacientes com hepatopatias colestáticas crônicas apresentam níveis significativamente reduzidos de antioxidantes circulantes (PMID 10735930). Paralelamente, evidências crescentes apontam que o estresse oxidativo participa ativamente do mecanismo de dano ao epitélio dos ductos biliares na PSC.

Teoricamente, a suplementação com Tocopherol poderia atuar em dois níveis: (1) corrigir a deficiência vitamínica induzida pela má absorção colestática, restaurando os estoques antioxidantes; e (2) atenuar o estresse oxidativo local nos ductos biliares, potencialmente reduzindo a progressão do dano epitelial. Contudo, esta ligação é essencialmente indireta e baseada em inferência mecanicista — não existem ensaios clínicos controlados testando diretamente Tocopherol como tratamento específico da colangite esclerosante.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05582447](https://clinicaltrials.gov/study/NCT05582447) | N/A | Ativo (não recrutando) | 40 | Estudo piloto observacional que avalia fragilidade osmótica e deformabilidade eritrocitária em pacientes pediátricos com doenças hepáticas colestáticas (incluindo PSC). Tocopherol não é a intervenção principal; a relevância para o uso terapêutico direto é indireta. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10735930](https://pubmed.ncbi.nlm.nih.gov/10735930/) | 2000 | Estudo transversal observacional | Alimentary Pharmacology & Therapeutics | Pacientes com hepatopatias colestáticas crônicas apresentam níveis plasmáticos reduzidos de vitaminas lipossolúveis (incluindo vitamina E/Tocopherol) e outros antioxidantes, sugerindo que radicais livres derivados do oxigênio participam da patogênese do dano hepático crônico. |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para Tocopherol na colangite esclerosante resumem-se a um único estudo observacional pediátrico de relevância indireta (grau C) e uma publicação transversal de nível 3, configurando nível de evidência L4 — insuficiente para justificar avanço clínico sem investigação adicional. Adicionalmente, o fármaco não possui qualquer registro na ANVISA, o que representa barreira regulatória relevante.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) via DrugBank API (DG002 pendente)
- Obter advertências e contraindicações da bula oficial (DG001 pendente — classificado como *Blocking*)
- Conduzir estudos pré-clínicos controlados testando Tocopherol em modelos de colangite esclerosante
- Avaliar o perfil de biodisponibilidade oral em pacientes com colestase grave (a própria doença compromete a absorção do fármaco)
- Investigar se formas de Tocopherol com maior absorção (ex.: tocoferil polietilenoglicol succinato, TPGS) seriam mais adequadas para esta indicação
- Planejar registro na ANVISA caso os dados pré-clínicos justifiquem progressão para ensaio clínico
---

