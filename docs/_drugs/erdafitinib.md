---
layout: default
title: Erdafitinib
parent: Apenas Predição do Modelo (L5)
nav_order: 294
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Erdafitinib: nova indicação prevista, Hipertensão Pulmonar (Pulmonary Hypertension) (nível de evidência L5). Indicação original: Outros agentes antineoplásicos"
monitor_inn: "erdafitinib"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome"]
---

# Erdafitinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Erdafitinibe: Do antineoplásico à hipertensão pulmonar
{: .text-alpha }

## Resumo em Uma Frase

Erdafitinibe é um inibidor de tirosina quinase dos receptores FGFR1-4, registrado no Brasil na categoria "outros agentes antineoplásicos".
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros agentes antineoplásicos |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 0,9938 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o erdafitinibe é um inibidor pan-FGFR (FGFR1-4) e pertence à classe dos inibidores de tirosina quinase, usada em oncologia.

A sinalização FGF/FGFR está associada ao remodelamento vascular pulmonar e à proliferação de células musculares lisas e endoteliais na hipertensão arterial pulmonar. Isso oferece uma justificativa biológica plausível para a previsão.

Há, porém, grande incerteza. A sinalização de FGF2 é descrita como patogênica e também como protetora em modelos de hipertensão pulmonar, de modo que a direção do efeito é incerta. A pontuação elevada do TxGNN é apenas uma previsão do modelo, sem validação clínica ou publicada.

**Outras indicações previstas (todas L5, Hold):**

| Indicação prevista | Pontuação TxGNN | Observação |
|------|------|------|
| Cardiopatia cifoescoliótica | 0,9927 | Sem vínculo mecanístico claro; o score vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, não evidência biológica |
| Amenorreia | 0,9926 | Direção terapêutica duvidosa; a inibição de FGFR tende a causar toxicidade reprodutiva |
| Artrite reumatoide | 0,9925 | Justificativa plausível, mas não validada; há apenas uma revisão geral |
| Esclerose lateral amiotrófica | 0,9906 | Direção do efeito incerta; sem dados de SNC |
| Síndrome de braquidactilia-sindactilia | 0,9903 | Malformação congênita; a inibição de FGFR é teratogênica |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para hipertensão pulmonar, atualmente não há literatura relacionada.

(Para a artrite reumatoide, a única publicação associada é uma revisão geral de inibidores de quinase aprovados pela FDA, [PMID 31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/), Roskoski, 2020, *Pharmacological Research*, que não estuda o erdafitinibe nessa doença.)

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 112363433 | ERFANDEL | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de tirosina quinase pan-FGFR) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Fosfato sérico, exame oftalmológico, função hepática e renal |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Toxicidades de classe dos inibidores de FGFR**: hiperfosfatemia, toxicidade ocular e mineralização de tecidos moles.
- **Interações medicamentosas**: foram identificadas 112 interações. Entre as de gravidade **maior** estão colecalciferol, dexametasona, fosfato de cálcio, calcifediol, calcitriol, acetato de cálcio, claritromicina, óxido de magnésio, sulfato de magnésio e cloreto de magnésio. Entre as de gravidade **moderada** estão metformina, loperamida, saxagliptina, eliglustat, empagliflozina, linagliptina, naldemedina, naloxegol, prucaloprida e rifaximina.
- Para advertências e contraindicações de bula, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as previsões estão no nível L5, sem ensaios clínicos nem literatura direta. Além disso, o registro no Brasil está cancelado e o perfil de segurança da classe (hiperfosfatemia, toxicidade ocular, 112 interações) exige cautela. A hipertensão pulmonar é a previsão com a justificativa biológica mais plausível, mas a direção do efeito é incerta.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem esses dados
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos de FGFR em modelos de hipertensão pulmonar, para esclarecer se a inibição é benéfica ou prejudicial
- Revisar a literatura sistematicamente para identificar evidências diretas
- Avaliar a viabilidade regulatória, já que o único registro está cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

