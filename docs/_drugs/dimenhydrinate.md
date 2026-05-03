---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando o skill `txgnn-pipeline` para orientar a geração do relatório de reposicionamento. Agora, gerando o relatório a partir do Evidence Pack fornecido.

---

# Dimenhydrinate: Da cinetose à urticária alérgica

## Resumo em Uma Frase

Dimenhydrinate é um anti-histamínico de primeira geração — sal composto por difenidramina e 8-cloroteofilina —, classicamente utilizado na prevenção e no tratamento de náusea, vômito e tontura causados por cinetose (enjoo de viagem).
O modelo TxGNN prevê que pode ser eficaz para **Urticária Alérgica (Allergic Urticaria)**, atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Cinetose (náusea e vômito por movimento) |
| Nova Indicação Prevista | Urticária Alérgica (Allergic Urticaria) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base nas informações conhecidas: Dimenhydrinate é um sal de difenidramina (diphenhydramine) e 8-cloroteofilina. A difenidramina é um antagonista competitivo do receptor H1 de histamina de primeira geração — mecanismo pelo qual o fármaco atua nas indicações tradicionais de cinetose.

A urticária alérgica tem como núcleo patológico a ativação de mastócitos com desgranulação e liberação de histamina, que estimula os receptores H1 cutâneos e produz as características pápulas eritematosas e prurido intenso. Antagonistas H1, incluindo a difenidramina, são reconhecidos nas diretrizes EAACI/WAO como tratamento de primeira linha para urticária — o que torna a previsão do TxGNN mecanisticamente plausível.

No entanto, existem ressalvas relevantes: as diretrizes modernas recomendam anti-histamínicos de segunda geração (cetirizina, loratadina) em substituição aos de primeira geração, para minimizar os efeitos sedativos e anticolinérgicos. Adicionalmente, o papel do componente 8-cloroteofilina (antagonista da adenosina) no tratamento da urticária permanece indefinido, introduzindo incerteza mecanística adicional que diferencia o dimenhydrinate da difenidramina isolada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Estudo de Farmacocinética | Veterinary Dermatology | Avaliação da farmacocinética de difenidramina oral e IV em cães saudáveis; dimenhydrinate produziu absorção oral superior de difenidramina; o efeito farmacodinâmico foi mensurado pela supressão de pápulas induzidas por histamina — modelo que apoia indiretamente a relevância anti-histamínica do fármaco |

> ⚠️ **Nota:** O único estudo disponível foi conduzido em modelo animal (cão), não em humanos, e tem foco farmacocinético — não é um ensaio clínico de eficácia para urticária.

---

## Informações de Comercialização no Brasil

Dimenhydrinate **não possui registro ativo na ANVISA**. Não há produtos com este ativo comercializados no mercado brasileiro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN (99,74%) é mecanisticamente coerente — a difenidramina é um H1 antagonista com indicação reconhecida para urticária —, mas o nível de evidência atual é L4: há apenas um estudo farmacocinético em modelo animal, sem ensaios clínicos em humanos para esta indicação específica. A ausência de registro no Brasil e a preferência clínica atual por anti-histamínicos de segunda geração reforçam a recomendação de aguardar evidências mais robustas antes de avançar.

**Para prosseguir, é necessário:**
- Dados completos de segurança (advertências e contraindicações) via bula oficial do fabricante
- Dados de MOA detalhados via DrugBank API (DG002)
- Ensaios clínicos em humanos com dimenhydrinate ou difenidramina oral especificamente para urticária alérgica
- Análise comparativa de eficácia e segurança frente a cetirizina e loratadina (padrão-ouro atual nas diretrizes)
- Avaliação regulatória para eventual pedido de registro na ANVISA, caso as evidências se fortaleçam
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

