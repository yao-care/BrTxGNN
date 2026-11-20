---
layout: default
title: Pegvaliase
parent: Apenas Predição do Modelo (L5)
nav_order: 513
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Pegvaliase"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract"]
description: "Pegvaliase: nova indicação prevista, Retinopatia diabética (diabetic retinopathy) (nível de evidência L5). No Brasil, registros na ANVISA: 1 (ativos: 1)"
---

# Pegvaliase
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

## Pegvaliase: Retinopatia diabética (diabetic retinopathy)
{: .text-alpha }

## Resumo em Uma Frase

Pegvaliase é uma enzima fenilalanina amônia-liase peguilada, que degrada a fenilalanina e cujo uso aprovado em outros países é a fenilcetonúria. Não há indicação original registrada no Brasil nos dados compiládos para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **retinopatia diabética (diabetic retinopathy)**, porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Retinopatia diabética (diabetic retinopathy) |
| Pontuação de Previsão TxGNN | 0.9917 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Pegvaliase (tradução não oficial): “A pegvaliase-pqpz é uma enzima fenilalanina amônia-liase (PAL) PEGuilada que converte a fenilalanina em amônia e ácido trans -cinâmico. Ela substitui a atividade deficiente da enzima fenilalanina hidroxilase (PAH) em pacientes com PKU e reduz as concentrações sanguíneas de fenilalanina.” Texto original em inglês: "Pegvaliase-pqpz is a PEGylated phenylalanine ammonia lyase (PAL) enzyme that converts phenylalanine to ammonia and trans -cinnamic acid. It substitutes for the deficient phenylalanine hydroxylase (PAH) enzyme activity in patients with PKU and reduces blood phenylalanine concentrations." ([DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c), versão de 2026-03-02; acessado em 2026-11-19). Segundo informações conhecidas, pegvaliase é uma fenilalanina amônia-liase peguilada que degrada a fenilalanina, e seu uso aprovado é a fenilcetonúria.

Não foi estabelecida nenhuma relação mecanística entre a depleção de fenilalanina e a patologia microvascular da retina diabética. A pontuação elevada do TxGNN (0,9917) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica; por si só, não constitui prova de plausibilidade biológica.

As demais previsões do modelo seguem o mesmo padrão: Retinopatia diabética não proliferativa grave (0,9916) e catarata diabética (0,9911). Ambas sem ensaios ou literatura. Essas pontuações vêm do modelo TxGNN (deep learning) e podem refletir semelhanças aprendidas entre doenças relacionadas, não biologia específica de cada doença.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 16 interações de nível moderado (fonte: DDInter), principalmente com outros fármacos peguilados ou biológicos:
  - Fatores de coagulação: fator anti-hemofílico recombinante humano e fator IX de coagulação humano
  - Fármacos peguilados: certolizumabe pegol, pegaptanibe (oftálmico), pegloticase, pegademase, pegaspargase, pegfilgrastim, peginesatida, peginterferona alfa-2a, alfa-2b e beta-1a, pegvisomanto
  - Outros: doxorrubicina lipossomal, acetato de medroxiprogesterona e naloxegol

Não há dados disponíveis sobre advertências principais e contraindicações da bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é baseada apenas no modelo (L5), sem ensaios clínicos, sem literatura e sem mecanismo plausível.

**Para prosseguir, é necessário:**
- Obter e analisar a bula e os dados de segurança (advertências e contraindicações), etapa bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação (MOA) via DrugBank
- Propor e testar uma hipótese biológica que ligue a degradação de fenilalanina à retinopatia diabética, com estudos pré-clínicos
- Avaliar a viabilidade da via de administração (a via sistêmica peguilada versus a necessidade de acesso ocular) e a situação regulatória no Brasil
- Buscar sinais clínicos ou de literatura antes de qualquer reavaliação

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

