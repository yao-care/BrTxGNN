---
layout: default
title: Belimumabe
parent: Apenas Predição do Modelo (L5)
nav_order: 111
evidence_level: L5
indication_count: 6
drugbank_id: DB08879
monitor_inn: "Belimumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-11-24
description: "Belimumabe: nova indicação prevista, Distúrbio primário de liberação plaquetária (primary release disorder of platelets) (nível de evidência L5). No Brasil, registros na ANVISA: 1 (ativos: 1)"
---

# Belimumabe
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Belimumabe: Distúrbio primário de liberação plaquetária (primary release disorder of platelets)
{: .text-alpha }

## Resumo em Uma Frase

Belimumabe é um anticorpo monoclonal que inibe o estimulador de linfócitos B (BLyS/BAFF), comercializado no Brasil com o nome Benlysta.
O modelo TxGNN prevê que pode ser eficaz para **Distúrbio primário de liberação plaquetária (primary release disorder of platelets)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Distúrbio primário de liberação plaquetária (primary release disorder of platelets) |
| Pontuação de Previsão TxGNN | 0.9996 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Belimumabe (tradução não oficial): “BENLYSTA é um inibidor específico do BLyS que bloqueia a ligação do BLyS solúvel, um fator de sobrevivência das células B, aos seus receptores nas células B. BENLYSTA não se liga diretamente às células B, mas, ao se ligar ao BLyS, BENLYSTA inibe a sobrevivência das células B, incluindo as células B autorreativas, e reduz a diferenciação das células B em plasmócitos produtores de imunoglobulinas.” Texto original em inglês: "BENLYSTA is a BLyS-specific inhibitor that blocks the binding of soluble BLyS, a B-cell survival factor, to its receptors on B cells. BENLYSTA does not bind B cells directly, but by binding BLyS, BENLYSTA inhibits the survival of B cells, including autoreactive B cells, and reduces the differentiation of B cells into immunoglobulin-producing plasma cells." ([DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3), versão de 2026-10-30; acessado em 2026-11-19). Pelo conhecimento geral da classe, o belimumabe inibe o BLyS solúvel (BAFF), reduzindo a sobrevivência de linfócitos B e a produção de autoanticorpos.

Os distúrbios primários de liberação plaquetária costumam ser defeitos hereditários ou adquiridos da secreção de grânulos e da sinalização plaquetária, e não são impulsionados principalmente por autoimunidade mediada por linfócitos B. Por isso, não se identifica uma ligação mecanística plausível entre a inibição de BLyS e esta condição.

A pontuação elevada (0,9996) reflete apenas uma previsão computacional, sem respaldo de ensaios clínicos ou literatura. A previsão deve ser tratada como hipótese a ser examinada com cautela, não como indício de benefício terapêutico.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101070295 | BENLYSTA | GLAXOSMITHKLINE BRASIL LTDA | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações sobre esta indicação, não há racional mecanístico plausível e o nível de evidência é L5 (apenas previsão do modelo).

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), hoje ausente dos dados.
- Obter dados do mecanismo de ação em fonte de referência (por exemplo, DrugBank).
- Realizar busca sistemática de literatura e estudos pré-clínicos que justifiquem uma ligação entre a inibição de BLyS e os defeitos de liberação plaquetária.
- Reavaliar a decisão somente se surgirem evidências diretas para a doença prevista.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Os detalhes individuais do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não foram populados** no Evidence Pa” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

