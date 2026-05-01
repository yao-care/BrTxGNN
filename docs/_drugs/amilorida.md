---
layout: default
title: Amilorida
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 0
---

# Amilorida
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

# Amilorida: Avaliação de Reposicionamento Pendente — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Amilorida (AMILORIDA) é um fármaco com **20 registros ativos** no mercado brasileiro, porém este pacote de evidências não contém dados de indicação original, mecanismo de ação nem previsões do modelo TxGNN. Sem previsões de nova indicação geradas, **não é possível realizar uma avaliação de reposicionamento neste momento**. A coleta de dados complementares é necessária antes de prosseguir.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível neste pacote de evidências |
| Nova Indicação Prevista | Nenhuma previsão TxGNN gerada |
| Pontuação de Previsão TxGNN | Não aplicável |
| Nível de Evidência | Não avaliável (sem predição de modelo) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para Amilorida neste pacote de evidências. Sem uma indicação candidata, não é possível avaliar a coerência mecanística entre indicação original e nova indicação.

Adicionalmente, não há dados sobre o mecanismo de ação (MOA) neste pacote. Segundo as lacunas identificadas (`DG002`), a consulta ao DrugBank é necessária para recuperar essas informações. Da mesma forma, as indicações originais aprovadas constam nos 20 registros regulatórios, mas os detalhes individuais de cada registro (nome comercial, forma farmacêutica, indicação aprovada) estão ausentes neste pacote — sendo necessário processar os registros via ANVISA/TFDA para completá-los.

---

## Informações de Comercialização no Brasil

O fármaco possui status **Comercializado** com **20 registros ativos**. Os detalhes individuais dos registros (nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste pacote de evidências — o preenchimento requer consulta direta às bulas registradas na ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para Amilorida, e os dados de mecanismo de ação, indicações originais aprovadas e perfil de segurança estão ausentes neste pacote, impossibilitando qualquer avaliação fundamentada de candidatura a reposicionamento.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN com Amilorida para obter previsões de novas indicações
- Consultar a API do DrugBank para recuperar o mecanismo de ação (MOA) e categorias farmacológicas
- Processar os 20 registros regulatórios via ANVISA para obter nome comercial, forma farmacêutica e indicação aprovada
- Baixar e analisar as bulas em PDF para extrair advertências principais, contraindicações e interações medicamentosas (`DG001`, severidade: Blocking)
---

