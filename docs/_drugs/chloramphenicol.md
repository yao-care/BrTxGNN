---
layout: default
title: Chloramphenicol
parent: Apenas Predição do Modelo (L5)
nav_order: 219
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-03
monitor_inn: "chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
description: "Chloramphenicol: nova indicação prevista, Esclerodermia difusa (diffuse scleroderma) (nível de evidência L5). Indicação original: CLORANFENICOL E ANALOGOS"
---

# Chloramphenicol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Chloramphenicol: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumo em Uma Frase

Cloranfenicol é um antibiótico de amplo espectro que atua inibindo a síntese de proteínas bacterianas.
O modelo TxGNN prevê que pode ser eficaz para **esclerodermia difusa (diffuse scleroderma)**, mas **não há ensaios clínicos** e as **4 publicações** encontradas são estudos básicos in vitro sobre a regulação do gene do colágeno em fibroblastos, sem relação demonstrada com o fármaco.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | CLORANFENICOL E ANALOGOS; CICATRIZANTES; OUTROS MEDICAMENTOS COM ACAO NO APARELHO VISUAL |
| Nova Indicação Prevista | Esclerodermia difusa (diffuse scleroderma) |
| Pontuação de Previsão TxGNN | 0.9965 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 8) |
| Número de Registros | 8 (ativos: 7) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Pelo conhecimento geral, o cloranfenicol é um antibiótico que bloqueia a síntese proteica bacteriana, e não há mecanismo farmacológico estabelecido que o ligue à esclerodermia difusa.

As publicações recuperadas tratam da regulação do gene do pró-colágeno α1(I) em fibroblastos de esclerodermia (promotor, Smad3/Sp1/p300, sinalização do TGF-β). Os títulos não mencionam o cloranfenicol. A associação provavelmente é um artefato de ensaios com gene repórter (cloranfenicol acetiltransferase, CAT), e não um efeito farmacológico.

Portanto, a pontuação alta do modelo não é sustentada por evidência clínica ou mecanística. Além disso, o uso sistêmico do cloranfenicol traz risco de toxicidade medular, desfavorável para uma doença crônica autoimune e fibrosante.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | Ativação transcricional do gene COL1A1 em fibroblastos dérmicos de esclerose sistêmica difusa; papel de sequências intrônicas |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | Elementos do promotor de COL1A1 envolvidos na sua expressão aumentada na esclerose sistêmica |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | O bloqueio da sinalização do TGF-β previne a síntese aumentada de colágeno em fibroblastos de esclerodermia |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Pesquisa básica (in vitro) | Rheumatology (Oxford) | Smad3 fosforilado de forma constitutiva interage com Sp1 e p300 em fibroblastos de esclerodermia |

Nenhum desses estudos avalia o cloranfenicol como tratamento.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100410201 | Succinato sódico de cloranfenicol | Não informada | Cloranfenicol e análogos |
| Registro nº 116370118 | Arifenicol | Não informada | Cloranfenicol e análogos |
| Registro nº 156510092 | Kolpocervix | Não informada | Cicatrizantes |
| Registro nº 102980505 | Kollagenase com cloranfenicol | Não informada | Cicatrizantes |
| Registro nº 102980493 | Regencel | Não informada | Outros medicamentos com ação no aparelho visual |

A lista mostra os 5 principais registros; há 8 registros no total, dos quais 7 estão válidos.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 478 interações. Entre as listadas, as de nível maior são com **cisaprida** e **naloxegol**. Há interações moderadas com metronidazol, budesonida, aprepitanto, sulfonilureias (clorpropamida, glimepirida, glipizida, glibenclamida), repaglinida, rosuvastatina, sinvastatina, saxagliptina, ferro, entre outras.
- Para advertências e contraindicações de bula, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas no modelo (L5): não há ensaios clínicos e a literatura são estudos in vitro sem relação farmacológica com o cloranfenicol, provavelmente um artefato de ensaio com gene repórter CAT.
- O risco de toxicidade medular do uso sistêmico é desfavorável para uma doença crônica.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação do fármaco
- Evidência pré-clínica que demonstre efeito antifibrótico real do cloranfenicol, independente de ensaios com repórter CAT
- Advertências e contraindicações extraídas das bulas da ANVISA
- Avaliação de segurança hematológica caso se considere o uso sistêmico

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

