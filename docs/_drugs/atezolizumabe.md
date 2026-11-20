---
layout: default
title: Atezolizumabe
parent: Apenas Predição do Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 6
drugbank_id: DB11595
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-16
description: "Atezolizumabe: nova indicação prevista, Adenocarcinoma do ligamento uterino (uterine ligament adenocarcinoma) (nível de evidência L5). No Brasil, registros na ANVISA: 1 (ativos: 1)"
---

# Atezolizumabe
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

## Atezolizumabe: Adenocarcinoma do ligamento uterino (uterine ligament adenocarcinoma)
{: .text-alpha }

## Resumo em Uma Frase

Atezolizumabe é um anticorpo monoclonal inibidor de PD-L1, comercializado no Brasil sob o nome Tecentriq.
O modelo TxGNN prevê que pode ser eficaz para **adenocarcinoma do ligamento uterino (uterine ligament adenocarcinoma)**, mas **não há ensaios clínicos nem publicações** nos dados compilados para este relatório que apoiem diretamente essa previsão. Trata-se, portanto, de uma previsão exclusivamente do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Adenocarcinoma do ligamento uterino (uterine ligament adenocarcinoma) |
| Pontuação de Previsão TxGNN | 0.9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Atezolizumabe (tradução não oficial): “O PD L1 pode ser expresso em células tumorais e/ou em células imunes infiltrantes do tumor e pode contribuir para a inibição da resposta imune antitumoral no microambiente tumoral. A ligação do PD L1 aos receptores PD 1 e B7.1 encontrados nas células T e nas células apresentadoras de antígenos suprime a atividade das células T citotóxicas, a proliferação das células T e a produção de citocinas. […] Atezolizumabe é um anticorpo monoclonal que se liga ao PD L1 e bloqueia suas interações com os receptores PD 1 e B7.1.” Texto original em inglês: "PD L1 may be expressed on tumor cells and/or tumor infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD L1 to the PD 1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation and cytokine production. […] Atezolizumab is a monoclonal antibody that binds to PD L1 and blocks its interactions with both PD 1 and B7.1 receptors." ([DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee), versão de 2026-10-13; acessado em 2026-11-19). Sabe-se que o atezolizumabe bloqueia o PD-L1, restaurando a atividade das células T contra o tumor. Em princípio, esse mecanismo poderia ser aplicável a adenocarcinomas do trato genital feminino.

No entanto, a pontuação muito alta do modelo (0,9993) não é sustentada por nenhuma evidência clínica nos dados disponíveis. A relação com a indicação original ainda não foi analisada, e a expressão de PD-L1 nesse tipo de tumor, que é raro, não está estabelecida. Qualquer vínculo seria uma extrapolação a partir de tumores ginecológicos em geral, e não evidência direta.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101000665 | TECENTRIQ | Não informada | Não registrada nos dados locais |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura sobre esta doença específica; a previsão se apoia somente na pontuação do modelo, o que corresponde ao nível L5.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada pela ANVISA (advertências e contraindicações), hoje ausente dos dados.
- Complementar os dados de mecanismo de ação a partir de fonte especializada, como o DrugBank.
- Realizar busca dirigida de estudos clínicos e literatura sobre este tipo tumoral, incluindo séries de casos e dados de expressão de PD-L1.
- Avaliar a viabilidade de estudos exploratórios (por exemplo, biomarcadores de PD-L1) antes de qualquer decisão de desenvolvimento.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “No entanto, os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não estão disponíveis** no Evidence ” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “os detalhes do registro regulatório estão vazios” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(ANVISA/TFDA)” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

