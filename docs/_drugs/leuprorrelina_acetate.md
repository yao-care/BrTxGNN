---
layout: default
title: Leuprorrelina Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 402
evidence_level: L5
indication_count: 2
drugbank_id: DB00007
monitor_inn: "Leuprolide"
predicted_indications: ["osteoarthritis", "pseudoachondroplasia"]
last_modified_at: 2026-11-24
description: "Leuprorrelina Acetate: nova indicação prevista, Osteoartrite (osteoarthritis) (nível de evidência L5). Indicação original: OUTROS HORMONIOS MEDIADORES E PRODUTOS EQUIVALENTES"
---

# Leuprorrelina Acetate
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

## Leuprorrelina Acetate: Osteoartrite (osteoarthritis)
{: .text-alpha }

## Resumo em Uma Frase

Leuprorrelina acetato é um fármaco com registro vigente no Brasil, com formulações comercializadas sob os nomes LECTRUM e ELIGARD.
O modelo TxGNN prevê que pode ser eficaz para **Osteoartrite (osteoarthritis)**, mas, até o momento, há **0 ensaios clínicos** e **nenhuma publicação** que estude diretamente essa doença; a previsão se apoia apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | OUTROS HORMONIOS MEDIADORES E PRODUTOS EQUIVALENTES; ANTINEOPLASICO |
| Nova Indicação Prevista | Osteoartrite (osteoarthritis) |
| Pontuação de Previsão TxGNN | 0.9970 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Leuprorrelina Acetate (tradução não oficial): “O acetato de leuprorrelina, um agonista do hormônio liberador de gonadotrofina (GnRH), atua como inibidor da secreção de gonadotrofinas quando administrado continuamente em doses terapêuticas. Estudos em animais e em humanos indicam que, após uma estimulação inicial, a administração crônica de acetato de leuprorrelina resulta na supressão da esteroidogênese testicular e ovariana.” Texto original em inglês: "Leuprolide acetate, a gonadotropin releasing hormone (GnRH) agonist, acts as an inhibitor of gonadotropin secretion when given continuously in therapeutic doses. Animal and human studies indicate that after an initial stimulation, chronic administration of leuprolide acetate results in suppression of testicular and ovarian steroidogenesis." ([DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f), versão de 2026-04-30; acessado em 2026-11-19). Pelo conhecimento farmacológico geral, a leuprorrelina é um agonista do hormônio liberador de gonadotrofinas (GnRH): suprime o eixo hipófise-gônadas e reduz os esteroides sexuais (estrogênio e testosterona).

Não foi identificado um vínculo mecanístico crível com a osteoartrite. A deficiência de estrogênio está, se algo, associada a maior risco de osteoartrite e perda óssea, de modo que a previsão não é sustentada pela farmacologia conhecida. A pontuação elevada provavelmente reflete proximidade estatística no modelo, e não um mecanismo terapêutico real.

Por isso, a previsão deve ser tratada com cautela, como uma hipótese computacional sem respaldo biológico até que surjam dados reais.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Foi recuperada apenas uma publicação, que não estuda a osteoartrite e, portanto, não sustenta a previsão:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Relato de caso | Clinical Breast Cancer | Adenocarcinoma de próstata metastático simulando carcinoma inflamatório de mama em homem de 78 anos; sem relação com osteoartrite |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 100470410 | LECTRUM | Ativo |
| 122140074 | ELIGARD | Ativo |

<!-- licenses:end -->

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Não é citotóxico convencional; terapia hormonal (agonista do GnRH) |
| Risco de Mielossupressão | Baixo |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que estudem a osteoartrite com este fármaco, e o mecanismo conhecido (supressão de estrogênio) não sustenta a previsão. O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação e das advertências e contraindicações da bula na ANVISA
- Estudos pré-clínicos que apontem um vínculo biológico plausível com a osteoartrite
- Reavaliação somente se surgirem evidências diretas sobre a doença

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco não possui registros ativos no Brasil” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Vabrinty (leuprolide acetate) prescribing information, URONOVA PHARMACEUTICALS, INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=008776cc-83f1-4f8c-819b-6471425da15f) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

