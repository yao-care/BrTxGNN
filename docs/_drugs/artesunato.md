---
layout: default
title: Artesunato
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 0
---

# Artesunato
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Artesunato: Do tratamento da malária — Previsão TxGNN Não Disponível

## Resumo em Uma Frase

Artesunato é um antimalárico semissintético derivado da artemisinina, indicado como tratamento de primeira linha para malária grave, especialmente por *Plasmodium falciparum*. Neste ciclo de análise, **não foram geradas previsões TxGNN** para novas indicações terapêuticas, pois o identificador DrugBank está ausente e os dados regulatórios detalhados não foram carregados no Evidence Pack. O medicamento possui **5 registros ativos no Brasil**, mas a avaliação de reposicionamento completa requer dados adicionais antes de prosseguir.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Malária grave (*Plasmodium falciparum*) |
| Nova Indicação Prevista | Não disponível — previsão TxGNN não gerada |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 5 |
| Decisão Recomendada | Hold |

---

## Por que a Previsão Não Foi Gerada?

Artesunato é um antimalárico amplamente utilizado no tratamento de malária grave. Em seu mecanismo de ação estabelecido, o fármaco é ativado pelo ferro heme liberado durante a digestão de hemoglobina pelo parasita, gerando radicais livres de carbono que danificam proteínas e membranas celulares do *Plasmodium*. Este mecanismo dependente de ferro tem levado pesquisadores a investigar seu potencial antineoplásico, uma vez que células tumorais frequentemente apresentam demanda elevada de ferro — porém esta aplicação permanece em fase de pesquisa e não está contemplada nas indicações registradas no Brasil.

Neste Evidence Pack, o campo `drugbank_id` está ausente e o campo `original_moa` consta como lacuna de dados. Sem o identificador DrugBank, o pipeline TxGNN não consegue localizar o nó correspondente no grafo de conhecimento para calcular pontuações de reposicionamento. Por isso, o campo `predicted_indications` retornou vazio e nenhuma nova indicação pôde ser avaliada neste ciclo.

Para habilitar as previsões, recomenda-se obter o DrugBank ID do artesunato — provável **DB09068** — e reprocessar o candidato no pipeline com os dados regulatórios corretamente populados.

---

## Informações de Comercialização no Brasil

O artesunato possui **5 registros ativos** confirmados pela consulta à ANVISA. Os detalhes individuais de cada registro não foram incluídos neste Evidence Pack: os campos de `licenses` (número de registro, nome comercial, forma farmacêutica, indicação aprovada) estão em branco. Recomenda-se consultar diretamente a base de dados da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/) para obter as informações completas de cada registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN nem dados regulatórios detalhados, impossibilitando uma avaliação de reposicionamento completa. Embora a disponibilidade comercial do medicamento no Brasil esteja confirmada (5 registros ativos), os dados necessários para a análise de reposicionamento estão ausentes de forma crítica.

**Para prosseguir, é necessário:**
- Obter o `drugbank_id` do artesunato (provável: **DB09068**) e reprocessar no pipeline TxGNN para gerar `predicted_indications`
- Baixar e analisar as bulas dos 5 registros ANVISA para extrair indicações aprovadas, advertências e contraindicações (remediação do DG001 — severidade Blocking)
- Consultar o DrugBank API para preencher os dados de mecanismo de ação (remediação do DG002 — severidade High)
- Reexecutar o Evidence Pack Builder com os campos `licenses` corretamente populados
---

