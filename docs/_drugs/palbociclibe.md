---
layout: default
title: Palbociclibe
parent: Apenas Predição do Modelo (L5)
nav_order: 503
evidence_level: L5
indication_count: 4
drugbank_id: DB09073
monitor_inn: "Palbociclib"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
last_modified_at: 2026-11-20
description: "Palbociclibe: nova indicação prevista, Hipertireoidismo (hyperthyroidism) (nível de evidência L5). No Brasil, registros na ANVISA: 8 (ativos: 7)"
---

# Palbociclibe
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

## Palbociclibe: Hipertireoidismo (hyperthyroidism)
{: .text-alpha }

## Resumo em Uma Frase

Palbociclibe é um inibidor das quinases dependentes de ciclina 4 e 6 (CDK4/6), comercializado no Brasil por vários titulares de registro.
O modelo TxGNN prevê que pode ser eficaz para **Hipertireoidismo (hyperthyroidism)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Hipertireoidismo (hyperthyroidism) |
| Pontuação de Previsão TxGNN | 0.9944 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 8) |
| Número de Registros | 8 (ativos: 7) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Palbociclibe (tradução não oficial): “O palbociclibe é um inibidor das quinases dependentes de ciclina (CDK) 4 e 6. A ciclina D1 e as CDK4/6 estão a jusante de vias de sinalização que levam à proliferação celular. In vitro, o palbociclibe reduziu a proliferação celular de linhagens celulares de câncer de mama positivas para receptor de estrogênio (ER) ao bloquear a progressão da célula da fase G1 para a fase S do ciclo celular.” Texto original em inglês: "Palbociclib is an inhibitor of cyclin-dependent kinases (CDK) 4 and 6. Cyclin D1 and CDK4/6 are downstream of signaling pathways which lead to cellular proliferation. In vitro, palbociclib reduced cellular proliferation of estrogen receptor (ER)-positive breast cancer cell lines by blocking progression of the cell from G1 into S phase of the cell cycle." ([DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792), versão de 2026-07-06; acessado em 2026-11-19). Sabe-se que o palbociclibe pertence à classe dos inibidores de CDK4/6, que bloqueiam a progressão do ciclo celular da fase G1 para a fase S.

Não há um elo mecanístico evidente entre a inibição de CDK4/6 e o excesso de hormônio tireoidiano. Nenhum ensaio clínico ou publicação foi encontrado para hipertireoidismo, de modo que o sinal é exclusivamente computacional e a plausibilidade biológica não pôde ser avaliada.

Além disso, o palbociclibe causa mielossupressão (neutropenia), o que representa uma preocupação de segurança adicional em uma condição endócrina benigna, em que alternativas estabelecidas já estão disponíveis.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 115410021 | Palbociclibe | — | Não informada |
| 115410022 | Sedecib | — | Não informada |
| 121100467 | Ibrance | — | Não informada |
| 121100495 | Agatha | — | Não informada |
| 121100502 | Ibrance | — | Não informada |

Os dados compilados incluem 8 registros no total (7 válidos e 1 cancelado); a tabela acima mostra os 5 principais.

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de CDK4/6) |
| Risco de Mielossupressão | Alto (neutropenia é um efeito conhecido do fármaco) |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Hemograma completo (CBC) com diferencial, função hepática e renal |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Mielossupressão**: o palbociclibe é associado a neutropenia, o que exige cautela em uma população não oncológica.

Consulte a bula para as demais informações de segurança, incluindo advertências, contraindicações e interações medicamentosas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hipertireoidismo se baseia unicamente na pontuação do modelo (0,9944), sem ensaios clínicos, sem literatura e sem mecanismo plausível identificado. O nível de evidência é L5, e o perfil mielossupressor aumenta a preocupação de segurança.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação (MOA) e uma hipótese biológica que ligue a inibição de CDK4/6 ao hipertireoidismo
- Estudos pré-clínicos que demonstrem algum efeito na doença
- Bula da ANVISA com advertências e contraindicações para a triagem de segurança
- Avaliação da relação risco-benefício frente às terapias já estabelecidas para hipertireoidismo

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não foram recuperados na coleta a” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

