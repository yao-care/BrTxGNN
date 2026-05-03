---
layout: default
title: Bosutinibe Monohydrate
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 0
---

# Bosutinibe Monohydrate
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

# Bosutinibe: Avaliação Preliminar — Dados Insuficientes para Reposicionamento

## Resumo em Uma Frase

Bosutinibe (monoidrato) é um inibidor de tirosina quinase BCR-ABL, utilizado internacionalmente no tratamento da leucemia mieloide crônica (LMC) cromossomo Philadelphia positivo. Neste ciclo de avaliação, **não foram geradas previsões de novas indicações pelo modelo TxGNN**, e o fármaco **não possui registro vigente no mercado brasileiro**. A análise está limitada por lacunas críticas de dados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Leucemia mieloide crônica Ph+ (uso internacional conhecido; sem registro local) |
| Nova Indicação Prevista | **Nenhuma previsão gerada neste ciclo** |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | **L5** (sem previsão nem estudos vinculados) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Foi Possível Gerar Previsões?

Bosutinibe monoidrato não foi mapeado com sucesso no Knowledge Graph do TxGNN neste ciclo de avaliação. Isso pode decorrer de três fatores principais:

1. **Ausência de DrugBank ID no Evidence Pack**: O campo `drugbank_id` está nulo. Sem esse identificador, o pipeline de mapeamento DrugBank → Knowledge Graph não consegue vincular o fármaco aos nós do grafo. O DrugBank ID internacional conhecido para bosutinibe é DB06616, porém essa correspondência não foi confirmada automaticamente pelo sistema.

2. **Fármaco não registrado no mercado local**: Com zero registros na base regulatória consultada, não há dados de indicações aprovadas em português que alimentem o mapeamento de doenças (disease mapping), reduzindo a cobertura do modelo.

3. **Forma salina específica**: A busca foi realizada com "BOSUTINIBE MONOHYDRATE" (forma monoidrato). É possível que o Knowledge Graph contenha o INN base "bosutinib" sem a qualificação de sal, gerando falha de correspondência.

---

## Informações de Comercialização no Brasil

O fármaco **não possui registros vigentes** na base regulatória consultada.

> **Nota**: Internacionalmente, bosutinibe é comercializado como **Bosulif®** (Pfizer) e está aprovado pela FDA (EUA), EMA (Europa) e outras agências para o tratamento de LMC Ph+ em pacientes adultos.

---

## Citotoxicidade

Bosutinibe é um agente antineoplásico (inibidor de tirosina quinase), portanto esta seção é aplicável.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | **Terapia alvo** (inibidor de tirosina quinase BCR-ABL/SRC) |
| Risco de Mielossupressão | **Alto** — trombocitopenia, neutropenia e anemia são efeitos adversos frequentes relatados em bulas internacionais |
| Classificação de Emetogenicidade | Baixa a média |
| Itens de Monitoramento | CBC com diferencial, função hepática (ALT/AST — hepatotoxicidade é advertência em caixa preta), função renal, eletrólitos, lipase |
| Proteção no Manuseio | Seguir protocolos institucionais para manuseio de antineoplásicos orais |

> ⚠️ **Importante**: Dados de citotoxicidade acima são baseados em informações internacionais de referência. Consulte a bula oficial do produto quando disponível localmente.

---

## Considerações de Segurança

Os dados de segurança específicos não estão disponíveis no Evidence Pack atual:

- **Advertências Principais**: Não disponíveis na base consultada
- **Contraindicações**: Não disponíveis na base consultada
- **Interações Medicamentosas**: Nenhuma interação encontrada na base DDI consultada (0 resultados)

> **Referência internacional**: Bosutinibe apresenta advertências conhecidas para hepatotoxicidade (elevação de transaminases), diarreia, retenção hídrica e mielossupressão. É substrato do CYP3A4, com interações relevantes com inibidores e indutores desta enzima. Consulte a bula para informações completas de segurança.

---

## Evidências de Ensaios Clínicos

Não há ensaios clínicos vinculados a previsões de reposicionamento neste ciclo, pois nenhuma nova indicação foi gerada pelo modelo.

---

## Evidências da Literatura

Não há publicações vinculadas a previsões de reposicionamento neste ciclo, pois nenhuma nova indicação foi gerada pelo modelo.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline de avaliação não conseguiu gerar previsões de reposicionamento para bosutinibe monoidrato devido à ausência de mapeamento no Knowledge Graph (DrugBank ID nulo) e à inexistência de registros regulatórios locais. Sem previsões do TxGNN, não há base para avançar na avaliação.

**Para prosseguir, é necessário:**
- **Resolver o mapeamento DrugBank**: Confirmar e inserir o DrugBank ID (provável DB06616) no pipeline
- **Harmonizar a nomenclatura**: Verificar se a busca com o INN base "bosutinib" (sem "monohydrate") retorna resultados no Knowledge Graph
- **Obter dados regulatórios**: Caso o fármaco venha a ser registrado no Brasil ou se deseje avaliar com base em dados de outras jurisdições (FDA/EMA), atualizar o Evidence Pack
- **Coletar dados de segurança**: Extrair advertências, contraindicações e interações da bula internacional (Bosulif® Prescribing Information)
- **Re-executar o modelo TxGNN**: Após resolução das lacunas acima, submeter novamente ao pipeline de previsão
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

