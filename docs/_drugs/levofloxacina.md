---
layout: default
title: Levofloxacina
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 0
---

# Levofloxacina
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

# Levofloxacina: Dados Insuficientes para Análise de Reposicionamento

## Resumo em Uma Frase

Levofloxacina é um antibiótico da classe das fluoroquinolonas, amplamente utilizado no tratamento de infecções bacterianas do trato respiratório, urinário e de pele.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco na execução atual — os registros regulatórios foram localizados (4 no mercado brasileiro), mas as etapas de mapeamento DrugBank e predição precisam ser concluídas antes que qualquer análise de reposicionamento possa ser realizada.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (fluoroquinolona de amplo espectro) |
| Nova Indicação Prevista | Não disponível — predição TxGNN pendente |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Informações de Comercialização no Brasil

Foram identificados **4 registros** da Levofloxacina na base regulatória brasileira, confirmando que o fármaco está em situação de comercialização ativa. No entanto, os detalhes individuais de cada registro (número de registro ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada) não foram recuperados nesta execução do pipeline — os campos retornaram vazios.

É necessário complementar a consulta à base ANVISA para obter esses dados antes de qualquer análise regulatória comparativa.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline identificou 4 registros da Levofloxacina no mercado brasileiro, porém nenhuma predição TxGNN foi gerada e os dados regulatórios detalhados estão ausentes, tornando impossível conduzir uma avaliação de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- Resolver o mapeamento DrugBank (DrugBank ID ausente) para que o modelo TxGNN possa processar o fármaco corretamente — INN a usar na consulta: `levofloxacin`
- Executar a etapa de predição TxGNN após o mapeamento para gerar indicações candidatas
- Recuperar os detalhes dos 4 registros ANVISA: número de registro, nome comercial, forma farmacêutica e indicação aprovada
- Baixar e analisar a bula em PDF disponível no portal ANVISA para extrair advertências, contraindicações e instruções de segurança (atualmente classificadas como bloqueantes — DG001)
- Obter dados de interações medicamentosas (DDI) — a consulta atual retornou `not_found`, o que pode indicar divergência no nome utilizado na busca
---

