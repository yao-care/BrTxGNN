---
layout: default
title: Benzila Benzoate
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 0
---

# Benzila Benzoate
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

# Benzoato de Benzila: Avaliação de Reposicionamento Inconclusiva por Dados Insuficientes

## Resumo em Uma Frase

O Benzoato de Benzila ("BENZILA BENZOATE") é um agente antiparasitário com uso histórico no tratamento de escabiose e pediculose.
O modelo TxGNN **não gerou nenhuma previsão de nova indicação** para este fármaco na presente análise, provavelmente em razão da ausência de DrugBank ID e de indicações originais registradas no Evidence Pack.
Sem previsões disponíveis, não há ensaios clínicos nem publicações vinculados a este processo de análise.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não identificada nos dados disponíveis |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Abaixo de L5 (ausência de previsões) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão Não Foi Gerada?

O Benzoato de Benzila é um éster aromático com propriedades antiparasitárias comprovadas, amplamente utilizado no tratamento tópico de escabiose e infestações por piolhos. Apesar de ser um fármaco bem estabelecido na prática clínica e presente na Lista de Medicamentos Essenciais da OMS, o Evidence Pack retornou sem mapeamento de DrugBank ID e sem indicações originais registradas.

Sem o DrugBank ID, o modelo TxGNN não consegue posicionar o fármaco no grafo de conhecimento (Knowledge Graph) e, consequentemente, não é capaz de calcular pontuações de similaridade com outras doenças nem gerar candidatos de reposicionamento. A ausência de indicações originais agrava essa limitação, pois o modelo perde os nós de ancoragem necessários para a inferência de novos usos.

A consulta ao DrugBank retornou 1 resultado (segundo o query\_log), mas as informações não foram integradas ao Evidence Pack. Isso sugere que o problema é de integração de dados no pipeline, e não de inexistência do fármaco nas bases de referência.

---

## Informações de Comercialização no Brasil

O fármaco **não possui registros ativos na ANVISA**. A consulta realizada em 26/03/2026 não encontrou nenhuma licença cadastrada para "BENZILA BENZOATE" no banco de dados regulatório brasileiro.

> **Nota:** É possível que registros existam sob a denominação alternativa "benzoato de benzila" ou "benzyl benzoate". Recomenda-se nova consulta com variações ortográficas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não gerou previsões de reposicionamento para este fármaco devido à ausência de DrugBank ID e de indicações originais no Evidence Pack. Sem esses dados de entrada, a análise de mecanismo de ação e de segurança também fica comprometida, tornando qualquer recomendação de reposicionamento prematuro.

**Para prosseguir, é necessário:**
- Identificar e registrar o DrugBank ID correto para o Benzoato de Benzila (buscar por "benzyl benzoate" — provável ID: DB00676)
- Registrar as indicações originais conhecidas (escabiose, pediculose) no Evidence Pack
- Obter dados de mecanismo de ação (MOA) via DrugBank API para preenchimento do campo `original_moa`
- Realizar nova consulta à ANVISA utilizando variações do nome ("benzoato de benzila", "benzyl benzoate") para verificar possíveis registros existentes
- Resolver a lacuna DG001 (advertências/contraindicações ANVISA) antes de qualquer avaliação de segurança
- Reexecutar o pipeline TxGNN com os dados corrigidos para gerar previsões de reposicionamento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

