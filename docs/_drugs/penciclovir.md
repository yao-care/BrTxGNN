---
layout: default
title: Penciclovir
parent: Apenas Predição do Modelo (L5)
nav_order: 516
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Penciclovir"
predicted_indications: ["fascioliasis"]
description: "Penciclovir: nova indicação prevista, fascioliase (fascioliasis) (nível de evidência L5). No Brasil, registros na ANVISA: 4 (ativos: 1)"
---

# Penciclovir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Penciclovir: fascioliase (fascioliasis)
{: .text-alpha }

## Resumo em Uma Frase

Penciclovir é um antiviral análogo de guanosina, usado originalmente contra infecções por herpes-vírus.
O modelo TxGNN prevê que pode ser eficaz para **fascioliase (fascioliasis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | fascioliase (fascioliasis) |
| Pontuação de Previsão TxGNN | 0.9906 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 4) |
| Número de Registros | 4 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Penciclovir (tradução não oficial): “O penciclovir é um agente antiviral ativo contra os alfa-herpesvírus. […] O penciclovir tem atividade inibitória contra os vírus herpes simples tipos 1 (HSV-1) e 2 (HSV-2). Em células infectadas pelo HSV-1 ou HSV-2, a timidina quinase viral fosforila o penciclovir em uma forma monofosfato que, por sua vez, é convertida por quinases celulares na forma ativa trifosfato de penciclovir.” Texto original em inglês: "Penciclovir is an antiviral agent active against alpha herpes viruses. […] Penciclovir has inhibitory activity against herpes simplex virus types 1 (HSV-1) and 2 (HSV-2). In cells infected with HSV-1 or HSV-2, the viral thymidine kinase phosphorylates penciclovir to a monophosphate form that, in turn, is converted by cellular kinases to the active form penciclovir triphosphate." ([DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5), versão de 2018-11-26; acessado em 2026-11-19). Pelo que se sabe, o penciclovir é um análogo de guanosina: após ser fosforilado pela timidina-quinase viral, sua forma trifosfato inibe a DNA polimerase de herpes-vírus.

A fascioliase é causada por *Fasciola hepatica*, um trematódeo (parasita), e não por um vírus. Esse organismo não possui uma via conhecida de ativação dependente de timidina-quinase viral, que é a base da ação do penciclovir. Por isso, não se identifica um vínculo mecanístico plausível com a ação antiviral original.

A pontuação alta (0,9906) é apenas uma previsão computacional. Não há ensaios clínicos nem literatura que a sustentem, e a previsão deve ser tratada com cautela.

## Informações de Comercialização no Brasil

Segundo os dados compilados para este relatório, o penciclovir consta como **comercializado** no Brasil, com registros válidos e cancelados (números atualizados no resumo rápido).

<!-- review:begin br-lic-20261106-penciclovir-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “Segundo os dados compilados para este relatório, o penciclovir consta como **comercializado** no Brasil, com 4 registros no total: 1 válido e 3 cancelados. Os detalhes individuais dos registros (número, nome comercial e forma farmacêutica) não estão disponíveis nos dados compilados.” Corrigido conforme os dados abertos de medicamentos da ANVISA: o número ou a situação dos registros informado não correspondia aos dados; o texto não traz mais números fixos, e os números atualizados estão no resumo rápido e na tabela de registros desta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-penciclovir-1 -->

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia exclusivamente no modelo, sem ensaios clínicos nem publicações, e não há vínculo mecanístico plausível entre a ação antiviral do penciclovir e um parasita trematódeo.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos (in vitro ou em modelos animais) que mostrem atividade contra *Fasciola hepatica*
- Dados de mecanismo de ação que justifiquem a aplicabilidade em parasitoses
- Bula do ANVISA com advertências e contraindicações, para a triagem de segurança
- Avaliação da compatibilidade de vias de administração com o uso proposto

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-24 | “Segundo os dados compilados para este relatório, o penciclovir consta como **comercializado** no Brasil, com…” → “Segundo os dados compilados para este relatório, o penciclovir consta como **comercializado** no Brasil, com…” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

