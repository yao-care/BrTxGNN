---
layout: default
title: Tegaserod
parent: Apenas Predição do Modelo (L5)
nav_order: 608
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Tegaserod: nova indicação prevista, Enxaqueca (Migraine Disorder) (nível de evidência L4). Indicação original: Outros produtos para o aparelho digestivo e metabolismo"
monitor_inn: "tegaserod"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Tegaserod
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

## Tegaserod: De outros produtos para o aparelho digestivo e metabolismo para enxaqueca
{: .text-alpha }

## Resumo em Uma Frase

Tegaserod foi originalmente registrado na ANVISA na categoria "outros produtos para o aparelho digestivo e metabolismo", sendo um agonista parcial do receptor 5-HT4 com ação procinética.
O modelo TxGNN prevê que pode ser eficaz para **enxaqueca (Migraine Disorder)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão) relacionada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho digestivo e metabolismo |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 0,9947 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, tegaserod é um agonista parcial do receptor 5-HT4 com atividade procinética (estimula a motilidade gastrointestinal). Essa informação baseia-se em conhecimento geral de farmacologia e não foi verificada contra os dados fornecidos.

A relação com a enxaqueca é indireta. A enxaqueca envolve sinalização serotoninérgica (receptores 5-HT1B/1D/1F, entre outros). Além disso, a estase gástrica e as náuseas durante as crises podem prejudicar a absorção de medicamentos orais para enxaqueca, e por isso os procinéticos já foram estudados como adjuvantes. Tegaserod não possui um mecanismo antienxaqueca direto estabelecido.

A pontuação TxGNN muito alta (0,9947) é uma previsão do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica nem clínica. A segunda previsão, **enxaqueca com aura do tronco encefálico** (pontuação 0,9929, nível L5, sem ensaios nem literatura), provavelmente reflete apenas semelhanças aprendidas pelo modelo com a enxaqueca e não um sinal independente.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Revisão | Journal of Gastroenterology and Hepatology | Revisa a eficácia de agentes procinéticos em doenças externas ao trato gastrointestinal, incluindo sistema nervoso central, respiratório, urológico e metabólico |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 109740242 (cancelado) | ZELMAC | Não informada | Outros produtos para o aparelho digestivo e metabolismo |

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento (não extraídas de bula):** doença hepática, doença da vesícula biliar e das vias biliares, icterícia obstrutiva, acidente vascular cerebral e doenças cerebrovasculares (incluindo infarto cerebral), infarto do miocárdio e trombose coronariana, hemoglobinopatia, íleo paralítico e obstrução intestinal, doença diarreica e colite isquêmica.
- **Interações medicamentosas:** foram identificadas 238 interações no total. Entre as listadas, digoxina e etinilestradiol têm gravidade menor; as demais (por exemplo, ciclosporina, eritromicina, azitromicina, fluconazol, tramadol, lorazepam, valsartana, ramipril, pravastatina e pantoprazol) têm gravidade não classificada.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica; não há ensaios clínicos e há uma única revisão geral. O medicamento está comercializado no Brasil, com 1 registro válido de 1, e o perfil de segurança sugerido (eventos cardiovasculares e cerebrovasculares) é particularmente preocupante em uma população com enxaqueca.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança
- Obter dados do mecanismo de ação (MOA) no DrugBank
- Buscar evidências diretas de tegaserod na enxaqueca (estudos pré-clínicos ou clínicos)
- Avaliar o risco cardiovascular e cerebrovascular em pacientes com enxaqueca, e a viabilidade regulatória diante do registro cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

