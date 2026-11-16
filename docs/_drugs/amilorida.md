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
description: "Amilorida: nova indicação prevista, Malignant hypertensive renal disease (nível de evidência L5). Indicação original: Não consta nos dados locais"
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

## Amilorida: Malignant hypertensive renal disease
{: .text-alpha }

## Resumo em Uma Frase

Amilorida é um diurético poupador de potássio, disponível no Brasil apenas em associações com hidroclorotiazida.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão renovascular maligna (malignant renovascular hypertension)**, mas, até o momento, há **0 ensaios clínicos** e **1 publicação** de caráter geral (uma revisão sobre hipertensão mineralocorticoide) associada a essa direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Malignant hypertensive renal disease |
| Pontuação de Previsão TxGNN | 0.9982 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 21) |
| Número de Registros | 21 (ativos: 3) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a amilorida bloqueia o canal epitelial de sódio (ENaC) no néfron distal, reduzindo a reabsorção de sódio e a perda de potássio. Isso é plausível para hipertensões dependentes de mineralocorticoides ou de volume.

A hipertensão renovascular maligna, porém, é impulsionada principalmente pela ativação do sistema renina-angiotensina. A ligação com o ENaC é, portanto, indireta. A única publicação recuperada é uma revisão geral sobre a investigação da hipertensão mineralocorticoide e não aborda a amilorida nessa condição.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Revisão | Journal of Hypertension. Supplement | Revisão geral sobre a investigação da hipertensão mineralocorticoide (aldosteronismo primário, hipocalemia, renina plasmática baixa); não avalia a amilorida na hipertensão renovascular maligna |

Não há ensaios clínicos relacionados registrados.

---

## Informações de Comercialização no Brasil

Todos os registros localizados são de associações (amilorida + hidroclorotiazida); nenhum é de amilorida isolada. Três registros estão válidos e 18 estão cancelados. Os textos de indicação aprovada não constam nos dados locais.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 100430981 | Diupress (associação) | Não informada | Não informada |
| 102350675 | Cloridrato de amilorida + hidroclorotiazida (associação) | Não informada | Não informada |
| 107150018 | Diurezin (associação) | Não informada | Não informada |

---

## Citotoxicidade

Não aplicável: a amilorida não é um antineoplásico.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

Observação: um relato de caso recuperado para outra condição prevista (cor pulmonale crônico) descreveu hiperpotassemia grave em paciente idosa em uso de outro medicamento. Isso reforça a cautela com fármacos poupadores de potássio, sobretudo na presença de insuficiência renal ou de outros agentes que elevam o potássio.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem estudos que avaliem a amilorida diretamente na hipertensão renovascular maligna. A previsão tem pontuação alta (0,9982), mas o mecanismo é indireto, já que a doença depende principalmente do sistema renina-angiotensina.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a falta desses dados impede a triagem de segurança.
- Complementar os dados de mecanismo de ação, por exemplo pela consulta ao DrugBank.
- Buscar estudos clínicos ou pré-clínicos que avaliem diretamente a amilorida na hipertensão renovascular maligna.
- Avaliar o risco de hiperpotassemia nessa população, incluindo função renal e uso concomitante de inibidores do sistema renina-angiotensina.

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

