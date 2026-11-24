---
layout: default
title: Benznidazol
parent: Apenas Predição do Modelo (L5)
nav_order: 120
evidence_level: L5
indication_count: 3
drugbank_id: DB11989
monitor_inn: "Benznidazole"
predicted_indications: ["congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-11-24
description: "Benznidazol: nova indicação prevista, Analbuminemia congênita (congenital analbuminemia) (nível de evidência L5). No Brasil, registros na ANVISA: 2 (ativos: 1)"
---

# Benznidazol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Benznidazol: Analbuminemia congênita (congenital analbuminemia)
{: .text-alpha }

## Resumo em Uma Frase

Benznidazol é um antiparasitário da classe dos nitroimidazóis, comercializado no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Analbuminemia congênita (congenital analbuminemia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Analbuminemia congênita (congenital analbuminemia) |
| Pontuação de Previsão TxGNN | 0.9951 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Benznidazol (tradução não oficial): “O benznidazol é um medicamento antimicrobiano nitroimidazólico. […] O benznidazol inibe a síntese de DNA, RNA e proteínas no parasita T. cruzi. Estudos sugerem que o benznidazol é reduzido por uma enzima nitrorredutase (NTR) do tipo I do T. cruzi, produzindo uma série de intermediários de curta duração que podem promover danos a diversas macromoléculas, incluindo o DNA.” Texto original em inglês: "Benznidazole is a nitroimidazole antimicrobial drug. […] Benznidazole inhibits the synthesis of DNA, RNA, and proteins within the T. cruzi parasite. Studies suggest that benznidazole is reduced by a Type I nitroreductase (NTR) enzyme of T. cruzi producing a series of short-lived intermediates that may promote damage to several macromolecules including DNA." ([DailyMed: benznidazole prescribing information, Exeltis USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8983d6a0-f63f-4f8e-bba4-38223f39e29b), versão de 2026-08-27; acessado em 2026-11-19). Segundo informações conhecidas, o benznidazol é um nitroimidazólico antiparasitário cuja atividade depende de ativação por nitrorredutases, gerando metabólitos reativos e radicais livres contra o *Trypanosoma cruzi*.

A analbuminemia congênita é uma doença genética rara, causada por mutações de perda de função no gene da albumina (ALB). Não é uma condição infecciosa nem parasitária. Não há via farmacológica plausível que ligue a ação antiparasitária do benznidazol à restauração da síntese de albumina.

A pontuação elevada (0,9951) é apenas uma previsão computacional, provavelmente influenciada pela estrutura dos dados do modelo e não por uma justificativa biológica. Por isso, a previsão deve ser tratada com muita cautela.

---

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101830145 | LAFEPE BENZNIDAZOL | LABORATORIO FARMACEUTICO DO ESTADO DE PERNAMBUCO G | Ativo |
| 101000074 | ROCHAGAN | PRODUTOS ROCHE QUÍMICOS E FARMACÊUTICOS S.A. | Cancelado |

<!-- licenses:end -->

Dos registros, um é válido e um está cancelado (ROCHAGAN).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem publicações que estudem a analbuminemia congênita, e não existe vínculo mecanístico plausível com o benznidazol. A previsão é apenas computacional (nível L5).

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações)
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Identificar qualquer evidência pré-clínica ou clínica que relacione o benznidazol à síntese ou ao metabolismo da albumina
- Reavaliar a previsão somente se surgir um racional biológico concreto

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco possui **2 registros ativos** no Brasil, porém os detalhes individuais (número de registro, nome comercial, forma farmacêutica e i” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: benznidazole prescribing information, Exeltis USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8983d6a0-f63f-4f8e-bba4-38223f39e29b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

