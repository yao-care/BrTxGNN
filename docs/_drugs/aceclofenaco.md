---
layout: default
title: Aceclofenaco
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# Aceclofenaco
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

# Aceclofenaco: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Aceclofenaco é um anti-inflamatório não esteroidal (AINE) amplamente registrado no mercado brasileiro, com 20 licenças ativas na ANVISA.
O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco nesta rodada de análise — provavelmente por ausência de mapeamento no DrugBank ou de correspondência na base de conhecimento do modelo.
Por este motivo, **não há candidatos de reposicionamento a avaliar** neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados recebidos |
| Nova Indicação Prevista | Sem previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão?

Aceclofenaco é um AINE da classe dos arilacéticos, com registro consolidado no Brasil. Contudo, **dois bloqueios técnicos impediram a geração de previsões** pelo modelo TxGNN nesta execução:

1. **DrugBank ID ausente**: O pipeline TxGNN utiliza o identificador DrugBank como chave de entrada para o grafo de conhecimento. Sem este ID, o fármaco não é localizado no grafo e nenhuma predição é computada. O log de consulta registra que a busca no DrugBank retornou 1 resultado (`result_status: success`), mas o ID não foi persistido no Evidence Pack — sendo necessário verificar e incluir o valor retornado.

2. **MOA não catalogado** (gap de alta severidade): A ausência do mecanismo de ação impede a análise de relevância mecanística entre indicação original e candidatos previstos, comprometendo a etapa de ranqueamento de plausibilidade.

Até que estes dois bloqueios sejam resolvidos, qualquer resultado de previsão seria não confiável.

---

## Informações de Comercialização no Brasil

Existem **20 registros ativos** para Aceclofenaco junto à ANVISA. Os dados detalhados dos registros (número, nome comercial, forma farmacêutica, indicação aprovada) **não constam no Evidence Pack atual** — os campos foram recebidos em branco.

> Para consultar os registros individuais, acesse o [Consulta de Produtos Registrados da ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para Aceclofenaco devido à ausência de DrugBank ID e de mapeamento completo no grafo de conhecimento. Sem previsões, não há candidato de nova indicação a avaliar — e prosseguir sem essa base invalidaria qualquer análise subsequente.

**Para prosseguir, é necessário:**
- Recuperar e persistir o **DrugBank ID** de Aceclofenaco a partir do resultado já obtido na consulta DrugBank (query log ID 3)
- Baixar e analisar as **bulas em PDF** disponíveis na ANVISA para preencher MOA, advertências e contraindicações (gap DG001 bloqueante e DG002 de alta severidade)
- Completar os **dados dos registros ANVISA** (número de registro, nome comercial, forma farmacêutica, indicação aprovada) para os 20 licenças registradas
- **Reexecutar o pipeline TxGNN** após corrigir o mapeamento do DrugBank ID, para que o modelo gere as previsões de reposicionamento
- Após obter previsões, realizar nova rodada de coleta de evidências (ensaios clínicos e literatura) antes de emitir relatório definitivo
---

