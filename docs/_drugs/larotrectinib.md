---
layout: default
title: Larotrectinib
parent: Apenas Predição do Modelo (L5)
nav_order: 392
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Larotrectinib: nova indicação prevista, Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia) (nível de evidência L3). Indicação original: Agentes antineoplásicos"
monitor_inn: "larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
---

# Larotrectinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Larotrectinibe: De antineoplásico (agente antineoplásico) para Neoplasia Endócrina Múltipla
{: .text-alpha }

## Resumo em Uma Frase

Larotrectinibe (VITRAKVI) é um agente antineoplásico, inibidor seletivo de TRK (NTRK1/2/3), registrado na ANVISA na classe de "agentes antineoplásicos".
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia)**,
porém há apenas **1 ensaio clínico** (basket trial tumor-agnóstico, relevância indireta) e **2 publicações** (uma revisão e um estudo mecanístico) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia) |
| Pontuação de Previsão TxGNN | 0,9924 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o larotrectinibe é um inibidor altamente seletivo de TRK (NTRK1/2/3), usado em tumores com fusão de NTRK.

A Neoplasia Endócrina Múltipla tipo 2 (MEN2) é causada principalmente por mutações germinativas ativadoras do gene RET, e não por alterações em NTRK. Portanto, **não há sobreposição direta de alvo**. A ligação é indireta: a literatura aborda terapias com inibidores de quinase no câncer de tireoide avançado (incluindo o carcinoma medular de tireoide, tumor característico da MEN2), e tumores dependentes de RET podem apresentar resistência por vias paralelas de quinases.

Os inibidores seletivos de RET (selpercatinibe e pralsetinibe) são a opção direcionada estabelecida. O larotrectinibe seria relevante apenas em tumores raros com fusão de NTRK. A pontuação alta do TxGNN (0,9924) é uma previsão computacional do modelo de aprendizado profundo, que pode refletir semelhanças aprendidas entre doenças relacionadas, e não evidência biológica. Por si só, não demonstra benefício clínico.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Ativo, sem recrutamento | 6452 | NCI-MATCH: ensaio basket que direciona o tratamento conforme alterações moleculares do tumor, com braço para fusão de NTRK. Sinal tumor-agnóstico; sem evidência direta para esta indicação (relevância B). |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Terapia direcionada com inibidores de quinase no câncer de tireoide avançado, incluindo aprovações específicas por mutação. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Estudo pré-clínico/mecanístico | NPJ Precision Oncology | Mecanismos de resistência off-target à inibição seletiva de RET (selpercatinibe) em carcinoma medular de tireoide com mutação de RET. |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 170560116 | VITRAKVI | BAYER S.A. | Ativo |
| 170560117 | VITRAKVI | BAYER S.A. | Ativo |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de quinase TRK) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 427 interações no total. Entre as principais listadas:
  - **Grave (Major)**: claritromicina.
  - **Moderada**: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, pioglitazona, aprepitanto, omeprazol, cimetidina, saxagliptina, dolasetrona, dronabinol, eliglustate, naldemedina, naltrexona, cisaprida, clotrimazol.
  - **Leve (Minor)**: naloxegol.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há alvo em comum entre o larotrectinibe (TRK) e o principal motor da MEN2 (RET), e as evidências são apenas indiretas (um ensaio basket tumor-agnóstico e literatura sobre outros inibidores). Além disso, os registros do produto no Brasil estão cancelados e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Identificar evidências específicas de tumores relacionados à MEN com fusão de NTRK, ou dados pré-clínicos diretos
- Esclarecer a situação regulatória e a disponibilidade do produto no Brasil, dado o cancelamento dos registros
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

