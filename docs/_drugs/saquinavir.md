---
layout: default
title: Saquinavir
parent: Apenas Predição do Modelo (L5)
nav_order: 579
evidence_level: L5
indication_count: 4
monitor_inn: "SAQUINAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Saquinavir: nova indicação prevista, Síndrome da imunodeficiência adquirida felina (nível de evidência L5). Indicação original: Infecção por HIV e AIDS"
---

# Saquinavir
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

## Saquinavir: Da infecção por HIV/AIDS à síndrome da imunodeficiência adquirida felina
{: .text-alpha }

## Resumo em Uma Frase

Saquinavir é um inibidor da protease do HIV-1, usado originalmente no tratamento da infecção por HIV e da AIDS (relação registrada no grafo de conhecimento do TxGNN).
O modelo TxGNN prevê que pode ser eficaz para a **síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)**, mas, para essa doença, há **0 ensaios clínicos** e **0 publicações** apoiando a previsão.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV e AIDS (relação registrada no grafo de conhecimento; os registros da ANVISA compilados não trazem texto de indicação aprovada) |
| Nova Indicação Prevista | Síndrome da imunodeficiência adquirida felina |
| Pontuação de Previsão TxGNN | 0,9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 14) |
| Número de Registros | 14 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o saquinavir é um inibidor da protease do HIV-1. O vírus da imunodeficiência felina (FIV) é um lentivírus relacionado ao HIV, de modo que um mecanismo baseado na inibição de protease é plausível em princípio.

Contudo, a protease do FIV difere da protease do HIV-1 na especificidade de substrato e na sensibilidade a inibidores. A pontuação elevada do TxGNN provavelmente reflete a proximidade na rede de conhecimento com a indicação de HIV/AIDS, e não uma evidência independente. Não há ensaios nem literatura para esta doença, portanto trata-se apenas de uma previsão do modelo.

### Outras previsões do modelo

- **Infecção pelo vírus da imunodeficiência símia (SIV)** (pontuação 0,9997): há 4 publicações, mas são estudos in vitro, estruturais e em animais, sem ensaios clínicos. Elas sustentam apenas a plausibilidade biológica. O SIV é principalmente um modelo de pesquisa para o HIV, não uma indicação clínica humana. Esta previsão não foi escolhida como principal e permanece em Hold.
- **Transtorno do neurodesenvolvimento com marcha atáxica, ausência de fala e redução da substância branca cortical** (pontuação 0,9997): não há vínculo mecanístico plausível, e a baixa penetração do saquinavir no sistema nervoso central limita qualquer racional especulativo.
- **Hiperlipidemia familiar combinada (termo obsoleto)** (pontuação 0,9959): inibidores da protease do HIV estão associados a dislipidemia, o que argumenta contra benefício terapêutico. O termo obsoleto sugere um artefato da ontologia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada à síndrome da imunodeficiência adquirida felina.

---

## Informações de Comercialização no Brasil

Foram compilados 14 registros de produtos de ingrediente único, dos quais 1 está válido e 13 foram cancelados. Os registros não trazem texto de indicação aprovada nem forma farmacêutica. Os principais são:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102980309 (válido) | SVIR | Não informada | Não informada |
| Registro nº 101000538 (cancelado) | INVIRASE | Não informada | Não informada |
| Registro nº 101000553 (cancelado) | FORTOVASE | Não informada | Não informada |
| Registro nº 104971157 (cancelado) | SAQUIVIRAL | Não informada | Não informada |
| Registro nº 102980211 (cancelado) | VIRNAN | Não informada | Não informada |

---

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não correspondem a texto de bula): síndrome do QT longo (inclusive familiar), torsades de pointes, bloqueio atrioventricular, insuficiência e doença hepática, cirrose, hepatites B e C crônicas, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, deficiência de potássio, hipertrigliceridemia, abuso/dependência de substâncias e hemofilia.
- **Interações medicamentosas**: foram identificadas 100 interações; as primeiras 20 incluem 3 de nível maior: **claritromicina**, **budesonida** e **triamcinolona**. Entre as de nível moderado estão acarbose, metformina, omeprazol, rabeprazol, famotidina, dexametasona, hidrocortisona, betametasona, loperamida e aprepitanto, entre outros.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para as informações de segurança oficiais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações sobre o saquinavir na síndrome da imunodeficiência adquirida felina (nível L5). A pontuação alta do modelo, isolada, não é suficiente. Além disso, o saquinavir tem diversas interações importantes e um perfil de segurança que exige cautela.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação do saquinavir e comparação da sensibilidade da protease do FIV a ele.
- Estudos in vitro e em animais de atividade antiviral contra o FIV.
- Obtenção e análise da bula da ANVISA (advertências e contraindicações).
- Avaliação de que há interesse de uso veterinário, já que a doença prevista é felina e não uma indicação humana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

