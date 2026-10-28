---
layout: default
title: Fluocinolone Acetonide
parent: Apenas Predição do Modelo (L5)
nav_order: 322
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Fluocinolone Acetonide: nova indicação prevista, Líquen plano atrófico anular (annular atrophic lichen planus) (nível de evidência L5). Indicação original: Desmelanizantes"
monitor_inn: "fluocinolone acetonide"
predicted_indications: ["annular atrophic lichen planus", "hypertrophic lichen planus", "lichen planus pigmentosus", "lichen planus pemphigoides"]
---

# Fluocinolone Acetonide
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

## Fluocinolona acetonida: De desmelanizante e corticoide tópico associado para líquen plano atrófico anular
{: .text-alpha }

## Resumo em Uma Frase

Fluocinolona acetonida é um corticoide tópico sintético, registrado no Brasil como desmelanizante, como medicamento de ação no aparelho auditivo e como glicocorticoide tópico em associação medicamentosa.
O modelo TxGNN prevê que pode ser eficaz para **líquen plano atrófico anular (annular atrophic lichen planus)**.
Atualmente há **0 ensaios clínicos** e **0 publicações** nos dados compilados para esta direção, de modo que a previsão se apoia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Desmelanizantes |
| Nova Indicação Prevista | Líquen plano atrófico anular (annular atrophic lichen planus) |
| Pontuação de Previsão TxGNN | 0,9942 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 9) |
| Número de Registros | 9 (ativos: 9) |
| Decisão Recomendada | Hold |

Outras previsões do modelo, com o mesmo nível de evidência (L5) e igualmente sem estudos associados: líquen plano hipertrófico (99,42%), líquen plano pigmentoso (99,42%) e líquen plano penfigoide (99,34%).

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação deste fármaco nos dados compilados. Segundo informações farmacológicas conhecidas, a fluocinolona acetonida é um corticoide que atua sobre o receptor de glicocorticoide (NR3C1), com efeito anti-inflamatório e imunossupressor. É usada em cremes para condições cutâneas inflamatórias e pruriginosas, e em implantes intravítreos (por exemplo, para edema macular diabético e uveíte posterior não infecciosa, aprovados pelo FDA).

O líquen plano é uma dermatose inflamatória mediada por linfócitos T, e os corticoides tópicos são abordagem padrão de primeira linha no líquen plano em geral. A plausibilidade mecanística é, portanto, razoável: supressão da inflamação dirigida por células T.

Ressalvas: trata-se de uma previsão para um subtipo específico, sem estudos com este fármaco nos dados disponíveis. A relação com a indicação original (desmelanizante, em associações com hidroquinona e tretinoína) é apenas contextual. No líquen plano pigmentoso, o benefício sobre a pigmentação já estabelecida é incerto. No líquen plano penfigoide, a gravidade pode exigir terapia sistêmica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Os 9 registros são válidos (9 de 9); o medicamento está comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 167730078 | SUAVICID | Não informada | Desmelanizantes |
| Registro 105830630 | HORMOSKIN | Não informada | Desmelanizantes |
| Registro 101910295 | VITACID PLUS | Não informada | Desmelanizantes |
| Registro 102350930 | Hidroquinona + Tretinoína + Fluocinolona acetonida | Não informada | Desmelanizantes |
| Registro 154230164 | Fluocinolona acetonida + sulfato de polimixina B + sulfato de neomicina | Não informada | Glicocorticoides tópicos - associação medicamentosa |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: o grafo de conhecimento do TxGNN (PrimeKG) associa o fármaco a contraindicações em: queimadura solar, ceratite por herpes simples, infecção por herpes simples, herpes-zóster geniculado, insuficiência adrenocortical, doença de Addison, glaucoma, atrofia da pele, telangiectasia (incluindo telangiectasia hemorrágica hereditária), doença capilar, doença vascular periférica (incluindo claudicação intermitente e doença arterial periférica), eczema atópico, dermatite, infecção fúngica ocular, tuberculose ocular e úlcera de córnea micótica. Atenção especial à **atrofia da pele**, relevante porque a indicação prevista é uma forma atrófica de líquen plano.
- **Interações Medicamentosas**: foram identificadas 9 interações na base DDInter, todas com nível de gravidade não classificado: dexametasona, cetirizina, citalopram, ácido valproico, paracetamol, digoxina, levotiroxina, ácido alendrônico e clonazepam. Além disso, o fármaco atua sobre o receptor de glicocorticoide.

Consulte a bula para advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (0,9942), mas está no nível L5: não há ensaios clínicos nem literatura. O medicamento está comercializado, com 9 registros válidos de 9.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), pois a triagem de segurança não pôde ser concluída.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar revisão sistemática da literatura sobre corticoides tópicos no líquen plano e seus subtipos.
- Avaliar a compatibilidade de via de administração e forma farmacêutica, e a disponibilidade de produto com registro ativo no Brasil.
- Avaliar o risco de atrofia cutânea com corticoide potente na forma atrófica anular.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

