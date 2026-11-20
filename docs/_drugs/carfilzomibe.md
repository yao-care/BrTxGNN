---
layout: default
title: Carfilzomibe
parent: Apenas Predição do Modelo (L5)
nav_order: 195
evidence_level: L5
indication_count: 5
drugbank_id: DB08889
monitor_inn: "Carfilzomib"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
last_modified_at: 2026-11-20
description: "Carfilzomibe: nova indicação prevista, CMM7 (nível de evidência L5). No Brasil, registros na ANVISA: 7 (ativos: 7)"
---

# Carfilzomibe
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

## Carfilzomibe: CMM7
{: .text-alpha }

## Resumo em Uma Frase

Carfilzomibe é um inibidor irreversível do proteassoma 20S, comercializado no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **CMM7 (CMM7)**, aparentemente um subtipo familiar de melanoma maligno cutâneo.
Atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta previsão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | CMM7 |
| Pontuação de Previsão TxGNN | 0.9937 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 7) |
| Número de Registros | 7 (ativos: 7) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Carfilzomibe (tradução não oficial): “O carfilzomibe é um inibidor do proteassoma do tipo tetrapeptídeo epoxicetona que se liga irreversivelmente aos sítios ativos contendo treonina N-terminal do proteassoma 20S, a partícula central proteolítica dentro do proteassoma 26S. O carfilzomibe apresentou atividades antiproliferativas e pró-apoptóticas in vitro em células de tumores sólidos e hematológicos.” Texto original em inglês: "Carfilzomib is a tetrapeptide epoxyketone proteasome inhibitor that irreversibly binds to the N-terminal threonine-containing active sites of the 20S proteasome, the proteolytic core particle within the 26S proteasome. Carfilzomib had antiproliferative and proapoptotic activities in vitro in solid and hematologic tumor cells." ([DailyMed: Kyprolis (carfilzomib) prescribing information, Onyx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea66eb30-e665-4693-99a1-a9d3b4bbe2d6), versão de 2025-06-18; acessado em 2026-11-19). Pelo que se sabe da classe, o carfilzomibe inibe de forma irreversível a atividade tipo quimiotripsina do proteassoma 20S. Isso leva ao acúmulo de proteínas mal dobradas e reguladoras, estresse proteotóxico e apoptose.

CMM7 parece ser um subtipo de melanoma maligno cutâneo familiar. Em princípio, células de melanoma poderiam ser sensíveis ao estresse proteotóxico, o que daria uma base mecanística plausível. Porém, não há ensaios clínicos nem publicações sobre esta indicação específica.

A pontuação alta provavelmente reflete a proximidade da rede de relações com o nó geral de melanoma, e não evidência específica para esta doença. A previsão deve ser tratada como hipótese a ser investigada.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 102440010 | KYPROLIS | Não informada | Não informada |
| 151430106 | ZOFYSERVE | Não informada | Não informada |
| 155370131 | CARFILZOMIBE | Não informada | Não informada |
| 155370134 | KARFYLOR | Não informada | Não informada |
| 155840725 | CARFILZOMIBE | Não informada | Não informada |

Há mais registros válidos além dos cinco listados (7 no total, todos válidos e de produto isolado).

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de proteassoma) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula; seguir os regulamentos de manuseio de antineoplásicos |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para CMM7 baseia-se apenas no modelo, sem ensaios clínicos nem literatura sobre a doença (nível L5). A pontuação alta provavelmente decorre da proximidade com o melanoma em geral, não de evidência específica.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos específicos em modelos de melanoma cutâneo familiar, incluindo CMM7
- Dados detalhados do mecanismo de ação e sua ligação com a biologia da doença
- Informações de segurança da bula da ANVISA (advertências e contraindicações)
- Avaliação da vantagem de carfilzomibe como monoterapia, já que inibidores de proteassoma tiveram eficácia limitada em tumores sólidos

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Kyprolis (carfilzomib) prescribing information, Onyx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea66eb30-e665-4693-99a1-a9d3b4bbe2d6) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

