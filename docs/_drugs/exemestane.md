---
layout: default
title: Exemestane
parent: Apenas Predição do Modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 7
monitor_inn: "Exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-11-20
description: "Exemestane: nova indicação prevista, Deficiência de antitrombina tipo 2 (antithrombin deficiency type 2) (nível de evidência L5). Indicação original: ANTINEOPLASICO"
---

# Exemestane
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Exemestano: inibidor de aromatase esteroidal irreversível → deficiência de antitrombina tipo 2 (antithrombin deficiency type 2)
{: .text-alpha }

## Resumo em Uma Frase

Exemestano é um inibidor esteroidal irreversível da aromatase, que reduz a produção de estrogênio.
O modelo TxGNN prevê que pode ser eficaz para **deficiência de antitrombina tipo 2 (antithrombin deficiency type 2)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção, ou seja, trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTINEOPLASICO; AGENTES ANTINEOPLÁSICOS |
| Nova Indicação Prevista | Deficiência de antitrombina tipo 2 (antithrombin deficiency type 2) |
| Pontuação de Previsão TxGNN | 0,9983 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 9) |
| Número de Registros | 9 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Exemestane (tradução não oficial): “O crescimento das células do câncer de mama pode ser dependente de estrogênio. A aromatase é a principal enzima que converte andrógenos em estrogênios, tanto em mulheres na pré-menopausa quanto na pós-menopausa. […] O exemestano é um inativador esteroidal irreversível da aromatase, estruturalmente relacionado ao substrato natural androstenediona.” Texto original em inglês: "Breast cancer cell growth may be estrogen-dependent. Aromatase is the principal enzyme that converts androgens to estrogens both in pre- and postmenopausal women. […] Exemestane is an irreversible, steroidal aromatase inactivator, structurally related to the natural substrate androstenedione." ([DailyMed: Aromasin (exemestane) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cf066b7a-032a-416c-8d40-15ba581423e3), versão de 2025-12-24; acessado em 2026-11-19). Pelo que se sabe, o exemestano é um inibidor esteroidal irreversível da aromatase, enzima que converte androgênios em estrogênios, resultando em redução dos níveis de estrogênio.

A deficiência de antitrombina tipo 2 é um defeito hereditário da função da antitrombina, ligado ao gene SERPINC1. A inibição da aromatase não corrige esse defeito, e não se conhece efeito de agentes redutores de estrogênio sobre a função da antitrombina. Não foi identificado um vínculo mecanístico plausível.

A pontuação elevada (0,9983) reflete apenas a previsão do modelo, sem respaldo de estudos clínicos ou da literatura. Por isso, a previsão deve ser vista com muita cautela.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431336 | PROEXTY | EUROFARMA LABORATORIOS S.A. | Ativo |
| 121100397 | AROMASIN | PFIZER BRASIL LTDA | Ativo |
| 146820066 | EXEMESTANO | SUN FARMACÊUTICA DO BRASIL LTDA | Ativo |
| 146820072 | EMAH | SUN FARMACÊUTICA DO BRASIL LTDA | Ativo |
| 155370048 | EXEMESTANO | ACCORD FARMACÊUTICA LTDA | Ativo |
| 102160141 | AROMASIN | LABORATÓRIOS PFIZER LTDA | Cancelado |
| 103840001 | AROMASIN | PHARMACIA BRASIL LTDA | Cancelado |
| 121100335 | EXEMESTANO | PFIZER BRASIL LTDA | Cancelado |
| 149320013 | EXEMESTANO | KEMMI PHARMA LTDA | Cancelado |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal (inibidor da aromatase), não é citotóxico convencional |
| Risco de Mielossupressão | Baixo |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 possíveis interações nos dados compilados. As de nível moderado incluem dexametasona e troglitazona. Outras, de gravidade não classificada, incluem pantoprazol, morfina, metformina, omeprazol, lansoprazol, sinvastatina, cloreto de potássio, ranitidina, ondansetrona e metronidazol.
- Do ponto de vista da nova indicação, os dados do modelo indicam que os inibidores da aromatase têm suas próprias considerações de segurança cardiovascular e tromboembólica, relevantes em um contexto de distúrbio da coagulação.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para esta indicação, e não há vínculo mecanístico plausível entre a inibição da aromatase e a função da antitrombina. A previsão é apenas do modelo (L5).

**Para prosseguir, é necessário:**
- Evidência mecanística ou pré-clínica que relacione a inibição da aromatase à função da antitrombina
- Dados de mecanismo de ação detalhados do fármaco
- Bula completa com advertências e contraindicações
- Avaliação de segurança tromboembólica em pacientes com trombofilia hereditária

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Aromasin (exemestane) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cf066b7a-032a-416c-8d40-15ba581423e3) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

