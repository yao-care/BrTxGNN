---
layout: default
title: Sacituzumab Govitecan
parent: Apenas Predição do Modelo (L5)
nav_order: 576
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Sacituzumab Govitecan: nova indicação prevista, Osteoporose induzida por fármacos (drug-induced osteoporosis) (nível de evidência L5). Indicação original: Não disponível nos dados compilados"
monitor_inn: "sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Sacituzumabe govitecana: Da indicação original não registrada à osteoporose induzida por fármacos
{: .text-alpha }

## Resumo em Uma Frase

Sacituzumabe govitecana (TRODELVY) é um conjugado anticorpo-fármaco dirigido ao Trop-2, que carrega o SN-38 (inibidor da topoisomerase I) e é um agente citotóxico usado em oncologia. Nos dados compilados para este relatório, o texto da indicação original não consta no registro brasileiro.
O modelo TxGNN prevê que pode ser eficaz para **osteoporose induzida por fármacos (drug-induced osteoporosis)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados compilados (o registro não traz texto de indicação) |
| Nova Indicação Prevista | Osteoporose induzida por fármacos (drug-induced osteoporosis) |
| Pontuação de Previsão TxGNN | 99,78% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o sacituzumabe govitecana é um anticorpo dirigido ao Trop-2 ligado ao SN-38, metabólito ativo do irinotecano, que inibe a topoisomerase I e causa dano ao DNA em células tumorais.

**Não se estabelece um vínculo mecanístico plausível** com a osteoporose induzida por fármacos. A quimioterapia citotóxica está, em geral, mais associada à perda óssea do que à proteção óssea. A pontuação elevada do TxGNN (0,998) provavelmente reflete artefatos do grafo de conhecimento, e não um mecanismo terapêutico real.

Outras indicações previstas pelo modelo também carecem de respaldo. Para retinopatia diabética grave não proliferativa (99,69%), retinopatia diabética (99,60%) e catarata diabética (99,12%), não há ensaios nem literatura, e o risco do uso sistêmico de um citotóxico (mielossupressão, infecções) em população crônica não oncológica é desfavorável.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 109290012 (cancelado) | TRODELVY | Não informada | Não informada |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Conjugado anticorpo-fármaco com carga citotóxica (inibidor da topoisomerase I, SN-38) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte a bula; em geral, hemograma completo com diferencial e função hepática e renal |
| Proteção no Manuseio | Seguir os regulamentos de manuseio de citotóxicos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 40 interações no total. Entre as principais:
  - **Gravidade maior**: deferiprona, fostamatinibe, adalimumabe, apalutamida, certolizumabe pegol, cladribina, dacomitinibe, irinotecano, leflunomida, natalizumabe, nilotinibe e ozanimode.
  - **Gravidade moderada**: alefacepte, alentuzumabe, anaquinra, canaquinumabe, fumarato de dimetila, lorlatinibe, ocrelizumabe e omacetaxina mepesuccinato.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é apenas computacional (L5), sem ensaios clínicos nem literatura, sem vínculo mecanístico plausível e com perfil de toxicidade desfavorável para uso sistêmico em condições não oncológicas. Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada
- Complementar os dados do mecanismo de ação via DrugBank
- Realizar validação pré-clínica de um mecanismo plausível antes de qualquer estudo clínico
- Confirmar a indicação original e a situação regulatória do produto no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

