---
layout: default
title: Acetazolamida
parent: Apenas Predição do Modelo (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
drugbank_id: DB00819
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-11-24
description: "Acetazolamida: nova indicação prevista, hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia) (nível de evidência L5). No Brasil, registros na ANVISA: 3 (ativos: 1)"
---

# Acetazolamida
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

## Acetazolamida: hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia)
{: .text-alpha }

## Resumo em Uma Frase

Acetazolamida é um inibidor da anidrase carbônica, com registros ativos e cancelados no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia)**, mas **não há ensaios clínicos nem publicações** que apoiem essa direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | hipertermia maligna induzida por exercício (exercise-induced malignant hyperthermia) |
| Pontuação de Previsão TxGNN | 0.9995 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Clinical Pharmacology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Acetazolamida (tradução não oficial): “A acetazolamida é um potente inibidor da anidrase carbônica, eficaz no controle da secreção de líquidos (p. ex., alguns tipos de glaucoma), no tratamento de certos distúrbios convulsivos (p. ex., epilepsia) e na promoção da diurese em casos de retenção anormal de líquidos (p. ex., edema cardíaco). A acetazolamida não é um diurético mercurial.” Texto original em inglês: "Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic." ([DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b), versão de 2026-11-10; acessado em 2026-11-19). Sabe-se, de forma geral, que a acetazolamida inibe a anidrase carbônica, o que altera o equilíbrio ácido-base e iônico dos tecidos.

Uma ligação plausível, porém não verificada, é que o fármaco module o equilíbrio iônico e ácido-base no músculo esquelético, como ocorre em paralisias periódicas. Já a hipertermia maligna é impulsionada pela liberação desregulada de cálcio pelo receptor RyR1, e nenhum dado sustenta um papel da acetazolamida nesse mecanismo.

Portanto, a previsão se apoia somente na pontuação do modelo. Sem estudos que abordem diretamente a doença, ela deve ser tratada como hipótese a ser testada, não como achado.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 104970289 | DIAMOX | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 107150117 | ZOLAMOX | CAZI QUIMICA FARMACEUTICA INDUSTRIA E COMERCIO LTD | Cancelado |
| 121100102 | DIAMOX | PFIZER BRASIL LTDA | Cancelado |

<!-- licenses:end -->

Dos registros listados, 1 está válido e 2 estão cancelados.

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão não tem nenhum ensaio clínico ou publicação que estude a doença, e não há base mecanística clara que ligue a inibição da anidrase carbônica à hipertermia maligna (nível L5).

**Para prosseguir, é necessário:**
- Revisão sistemática da literatura sobre acetazolamida e hipertermia maligna ou miopatias relacionadas ao RyR1
- Dados do mecanismo de ação e estudos pré-clínicos em modelos musculares
- Obtenção e análise da bula da ANVISA para avaliar advertências e contraindicações
- Avaliação da compatibilidade de vias de administração com o uso proposto

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Embora o sistema confirme **5 registros ativos** na ANVISA, todos os campos de detalhe (número de registro, nome comercial, forma farmacêuti” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

