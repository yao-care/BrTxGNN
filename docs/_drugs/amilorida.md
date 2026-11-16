---
layout: default
title: Amilorida
parent: Apenas Predição do Modelo (L5)
nav_order: 52
evidence_level: L5
indication_count: 5
drugbank_id: DB00594
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-16
description: "Amilorida: nova indicação prevista, doença renal hipertensiva maligna (malignant hypertensive renal disease) (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Amilorida
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

## Amilorida: doença renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumo em Uma Frase

Amilorida é um diurético poupador de potássio, usado como adjuvante no tratamento da hipertensão e do edema.
O modelo TxGNN prevê que pode ser eficaz para **doença renal hipertensiva maligna (malignant hypertensive renal disease)**, mas essa previsão se apoia apenas na pontuação do modelo: há **0 ensaios clínicos** e **0 publicações** sobre essa doença nos dados compilados para este relatório.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | doença renal hipertensiva maligna (malignant hypertensive renal disease) |
| Pontuação de Previsão TxGNN | 0.9982 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 21) |
| Número de Registros | 21 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Pelo conhecimento farmacológico geral, a amilorida bloqueia o canal epitelial de sódio (ENaC) nos túbulos renais distais, promovendo a excreção de sódio e a retenção de potássio. É usada como adjuvante anti-hipertensivo, o que sugere uma ligação plausível com o controle da pressão arterial.

A doença renal hipertensiva maligna é uma condição grave, em que a pressão muito elevada lesa rapidamente os rins. Seu manejo costuma exigir agentes parenterais de ação rápida. Um diurético poupador de potássio oral dificilmente seria uma terapia principal, e o papel potencial seria, no máximo, de apoio no controle de volume e pressão.

A pontuação alta do modelo (0,9982) é o único suporte da previsão. Não há ensaios nem publicações sobre esta doença. Há ainda uma preocupação importante de segurança: o risco de hiperpotassemia em pacientes com função renal comprometida, exatamente o cenário desta doença.

## Informações de Comercialização no Brasil

A amilorida está comercializada no Brasil, mas, entre os registros compilados, os três válidos são de produtos em associação (com hidroclorotiazida). Esses registros descrevem os produtos combinados e não a amilorida como único princípio ativo.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 100430981 | DIUPRESS | Não informada | Texto de indicação não registrado |
| 102350675 | CLORIDRATO DE AMILORIDA + HIDROCLOROTIAZIDA | Não informada | Texto de indicação não registrado |
| 107150018 | DIUREZIN | Não informada | Texto de indicação não registrado |

Dos 21 registros localizados, 3 estão válidos e 18 estão cancelados.

## Considerações de Segurança

Consulte a bula para informações de segurança.

Ponto de atenção derivado da avaliação da previsão: o risco de hiperpotassemia em pacientes com insuficiência renal é uma preocupação importante para qualquer uso da amilorida em doença renal.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas na pontuação do modelo (nível de evidência L5), sem ensaios clínicos ou literatura sobre a doença renal hipertensiva maligna.
- Trata-se de uma condição grave, manejada com agentes de ação rápida, e o risco de hiperpotassemia na disfunção renal pesa contra o uso.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação e segurança da bula aprovada pela ANVISA (advertências e contraindicações).
- Revisão da literatura ou estudos pré-clínicos específicos sobre amilorida em nefropatia hipertensiva maligna.
- Avaliação do risco de hiperpotassemia em pacientes com função renal reduzida, antes de qualquer estudo clínico.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Amilorida (AMILORIDA) é um fármaco com **20 registros ativos** no mercado brasileiro, porém este pacote de evidências não contém dados de in” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “mas os detalhes individuais de cada registro (nome comercial, forma farmacêutica, indicação aprovada) estão ausentes neste pacote — sendo ne” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco possui status **Comercializado** com **20 registros ativos**. Os detalhes individuais dos registros (nome comercial, forma farmacê” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

