---
layout: default
title: Lumacaftor
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Lumacaftor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Usando o sistema de prompt v5 como guia de formato para gerar o relatório de avaliação de reposicionamento.

---

# Lumacaftor: Da Fibrose Cística à Hanseníase

## Resumo em Uma Frase

Lumacaftor é um corretor de proteína CFTR, aprovado em combinação com ivacaftor (Orkambi) para o tratamento da fibrose cística com mutação F508del homozigótica.
O modelo TxGNN prevê possível eficácia para **Hanseníase (Leprosy)**, com pontuação de 99,44%.
Entretanto, **não há ensaios clínicos nem publicações científicas** sustentando esta direção — trata-se de previsão exclusivamente baseada no modelo de grafos de conhecimento, sem evidência independente.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrose cística (mutação F508del homozigótica) |
| Nova Indicação Prevista | Hanseníase (Leprosy) |
| Pontuação de Previsão TxGNN | 99,44% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base em informações conhecidas, Lumacaftor é um **corretor de dobramento da proteína CFTR** (*Cystic Fibrosis Transmembrane Conductance Regulator*): ele estabiliza a conformação da proteína mutante F508del, permitindo que ela seja transportada corretamente à superfície celular. Em combinação com ivacaftor — que potencializa a abertura do canal — demonstrou eficácia clínica comprovada na fibrose cística.

A hanseníase é causada por *Mycobacterium leprae*, um patógeno intracelular obrigatório que infecta principalmente macrófagos e células de Schwann. A única conexão indireta identificada envolve o papel do CFTR na função imunológica dos macrófagos: estudos em pacientes com fibrose cística documentam redução na capacidade de eliminação de micobactérias por macrófagos com CFTR disfuncional, sugerindo que a restauração do CFTR pode, em tese, melhorar a resposta imune a infecções por micobactérias.

No entanto, essa associação é observacional e restrita ao contexto da fibrose cística — não constitui fundamento mecanístico para reposicionamento. O mecanismo primário do Lumacaftor (resgate de dobramento proteico) não possui interseção conhecida com vias antimicrobianas, fagocitose aumentada ou imunomodulação de relevância para a hanseníase. A previsão do TxGNN provavelmente decorre de associações topológicas no grafo de conhecimento (CF → disfunção de macrófagos → micobactérias), não de uma relação causal direta.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Há **2 registros** do Lumacaftor junto à ANVISA com situação ativa, porém os detalhes individuais (número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada) não foram recuperados nesta consulta. O produto é comercializado no Brasil em combinação com ivacaftor, sob o nome comercial **Orkambi**, na forma de comprimido revestido.

> Para detalhes completos dos registros, consulte o portal ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existem ensaios clínicos nem publicações científicas vinculando Lumacaftor ao tratamento da hanseníase. A previsão do TxGNN baseia-se exclusivamente em inferências topológicas do grafo de conhecimento, e a ligação indireta via função de macrófagos em contexto de fibrose cística não constitui evidência translacional suficiente para avançar.

**Para prosseguir, é necessário:**
- Recuperar e analisar o mecanismo de ação completo do Lumacaftor (via DrugBank API ou literatura primária) para avaliar se há alvos relevantes para *M. leprae*
- Recuperar os detalhes completos dos registros ANVISA (número, nome comercial, indicação aprovada) via download do PDF da bula
- Conduzir estudos pré-clínicos *in vitro* avaliando o efeito do Lumacaftor em modelos de infecção de macrófagos por *M. leprae* ou espécies relacionadas (*M. tuberculosis*)
- Investigar se a expressão de CFTR em macrófagos de pacientes sem fibrose cística é biologicamente relevante para a resposta antimicobacteriana — pré-requisito para qualquer hipótese de reposicionamento
---

