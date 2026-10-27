---
layout: default
title: Letermovir
parent: Apenas Predição do Modelo (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Letermovir: nova indicação prevista, Candidíase Vulvovaginal (vulvovaginal candidiasis) (nível de evidência L5). Indicação original: Infecção por citomegalovírus"
monitor_inn: "Letermovir"
predicted_indications: ["vulvovaginal candidiasis", "fungal infectious disease", "tinea nigra", "malignant catarrh", "infectious bovine rhinotracheitis", "anogenital human papillomavirus infection", "AIDS", "dermatophytosis", "piedra", "varicella zoster infection"]
---

# Letermovir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Letermovir: Da infecção por citomegalovírus à candidíase vulvovaginal
{: .text-alpha }

## Resumo em Uma Frase

Letermovir foi originalmente usado no tratamento/prevenção da infecção por citomegalovírus (CMV).
O modelo TxGNN prevê que pode ser eficaz para **Candidíase Vulvovaginal (vulvovaginal candidiasis)**, mas **não há ensaios clínicos nem publicações** apoiando esta direção; trata-se apenas de uma previsão computacional, sem plausibilidade mecanística identificada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por citomegalovírus |
| Nova Indicação Prevista | Candidíase Vulvovaginal (vulvovaginal candidiasis) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o letermovir inibe o complexo terminase do CMV (pUL56/UL89/UL51), responsável pela clivagem e empacotamento do DNA viral. Sua eficácia na infecção por CMV está estabelecida.

A candidíase vulvovaginal é causada por fungos do gênero *Candida*, que não possuem um equivalente conhecido desse alvo viral. Por isso, **a previsão não é sustentada por um mecanismo plausível**: a pontuação elevada do TxGNN provavelmente reflete associações no grafo de conhecimento (por exemplo, o contexto de infecções oportunistas), e não um efeito terapêutico real.

Vale destacar que outras previsões do mesmo fármaco têm base um pouco mais consistente. A mais relevante é a **AIDS/HIV** (posição 7), com 3 ensaios clínicos e literatura associada, embora o objetivo seja reduzir a inflamação crônica causada pelo CMV, e não tratar o HIV. A indicação principal (candidíase vulvovaginal) é apresentada aqui conforme o ranking do modelo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para candidíase vulvovaginal.

## Evidências da Literatura

Atualmente não há literatura relacionada para candidíase vulvovaginal.

## Informações de Comercialização no Brasil

O letermovir não possui registro ativo no Brasil nos dados compilados para este relatório (0 registros).

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as exibidas, destacam-se as de gravidade **maior**:
  - Eliglustat
  - Naloxegol
  - Cisaprida

  Há ainda diversas interações de gravidade **moderada**, entre elas corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), inibidores da bomba de prótons (omeprazol, lansoprazol), antidiabéticos (pioglitazona, glimepirida, saxagliptina, clorpropamida, acetoexamida), aprepitanto, claritromicina, naldemedina e nitisinona.
- Os triazólicos (por exemplo, voriconazol) merecem atenção especial caso se cogite uso em contexto antifúngico, pois a literatura aponta preocupações de segurança na coadministração com letermovir.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para candidíase vulvovaginal, e o alvo do letermovir (terminase viral) não existe em fungos. A previsão é considerada um artefato do modelo.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação consolidados (por exemplo, via DrugBank).
- Bula da ANVISA (advertências e contraindicações), atualmente indisponível; o fármaco não tem registro no Brasil.
- Estudos *in vitro* de atividade contra *Candida*, antes de qualquer investimento clínico.
- Priorizar a avaliação de outras indicações previstas com maior respaldo, em especial a inflamação associada ao CMV em pessoas vivendo com HIV (nível de evidência L2, ensaios NCT04840199, NCT05362916 e NCT06626555).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

