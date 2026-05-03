---
layout: default
title: Oxymetazoline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 0
---

# Oxymetazoline Hydrochloride
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

# Oxymetazoline Hidrocloreto: Sem Previsão de Reposicionamento — Dados Insuficientes

## Resumo em Uma Frase

Oxymetazoline hidrocloreto é um agonista alfa-adrenérgico amplamente utilizado como descongestionante nasal e vasoconstritor ocular em formulações tópicas.
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco na análise atual, pois não foram encontrados registros na ANVISA e os dados de mecanismo de ação permanecem pendentes.
Com isso, **não há ensaios clínicos nem publicações** vinculados a novas indicações previstas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Descongestionante nasal / vasoconstritor ocular (uso tópico) |
| Nova Indicação Prevista | Não disponível — nenhuma previsão TxGNN gerada |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Houve Previsão?

O modelo TxGNN opera sobre um grafo de conhecimento que conecta fármacos, genes e doenças. Para que um candidato gere previsões, é necessário que o fármaco esteja mapeado no grafo — o que requer, minimamente, um identificador DrugBank e indicações originais cadastradas. Neste caso, ambos estão ausentes no Evidence Pack.

Segundo informações de domínio público, oxymetazoline é um agonista seletivo dos receptores alfa-1 e alfa-2 adrenérgicos com pronunciada ação vasoconstritora. É empregado principalmente em sprays nasais (alívio de congestão) e colírios (hiperemia ocular). Em outros países, versões de baixa concentração (1%) foram aprovadas para o tratamento da eritema facial persistente associada à rosácea, o que indica potencial terapêutico além das indicações clássicas. Contudo, esses dados não estão refletidos no Evidence Pack atual e, portanto, não alimentaram o pipeline preditivo.

A ausência de registro na ANVISA (zero resultados na consulta de 26/03/2026) impede o mapeamento das indicações locais aprovadas e reduz a conectividade do fármaco no grafo de conhecimento. A consulta ao DrugBank retornou 1 resultado, indicando que os dados existem mas ainda não foram extraídos e integrados ao Evidence Pack — o que explica, em grande parte, a lacuna de previsão.

---

## Informações de Comercialização no Brasil

Oxymetazoline Hidrocloreto **não possui registros ativos na ANVISA**. A consulta realizada em 26/03/2026 retornou zero resultados. O fármaco é amplamente utilizado em outros países sob nomes comerciais como Afrin® (spray nasal), Visine® L.R. (colírio) e Rhofade® (creme para rosácea), o que sugere que o registro local pode simplesmente não estar indexado na fonte consultada, ou que o produto é comercializado sob composição combinada não identificada pela busca por INN.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento por ausência de dados regulatórios na ANVISA e lacunas críticas no mecanismo de ação e nas indicações originais — impedimentos que bloqueiam o funcionamento do pipeline preditivo antes mesmo da etapa de avaliação de evidências.

**Para prosseguir, é necessário:**
- Extrair e integrar os dados do DrugBank (consulta já realizada com 1 resultado): DrugBank ID, categorias terapêuticas, MOA e toxicidade
- Verificar registros do fármaco em outras jurisdições (FDA NDC, EMA, PMDA) para identificar indicações aprovadas que possam alimentar o grafo de conhecimento
- Investigar se o produto é comercializado no Brasil sob denominação combinada ou nome comercial diferente do INN
- Baixar e analisar a bula disponível em outras agências regulatórias para preencher advertências e contraindicações (campo de severidade "Blocking" no DG001)
- Reprocessar o candidato no pipeline TxGNN após completar os dados acima
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

