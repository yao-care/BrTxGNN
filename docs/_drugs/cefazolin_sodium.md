---
layout: default
title: Cefazolin Sodium
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 0
---

# Cefazolin Sodium
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

# Cefazolin Sódica: Avaliação de Reposicionamento — Dados Insuficientes para Análise

## Resumo

Cefazolin sódica é um antibiótico cefalosporínico de primeira geração, classicamente utilizado na profilaxia cirúrgica e no tratamento de infecções bacterianas por germes Gram-positivos e alguns Gram-negativos. O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco com os dados disponíveis neste Evidence Pack. Não há indicações previstas, ensaios clínicos vinculados nem literatura associada para avaliação — o que inviabiliza a análise de reposicionamento neste ciclo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível (nenhum registro encontrado na ANVISA) |
| Nova Indicação Prevista | Nenhuma previsão disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — sem previsão de modelo ou estudos vinculados |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão?

Cefazolin sódica é uma cefalosporina de primeira geração cujo mecanismo de ação envolve a inibição da síntese da parede celular bacteriana por ligação às proteínas de ligação à penicilina (PBPs). Apesar de ser um fármaco amplamente conhecido e utilizado em todo o mundo, o Evidence Pack retornou **zero registros regulatórios** e **zero indicações previstas pelo TxGNN**.

As causas mais prováveis para a ausência de previsões são:

1. **Falha no mapeamento DrugBank**: A consulta ao DrugBank retornou 1 resultado, mas o campo `drugbank_id` permaneceu nulo. Sem esse ID, o fármaco não consegue ser posicionado corretamente no grafo de conhecimento do TxGNN, inviabilizando o cálculo de score.
2. **Divergência de nomenclatura na busca regulatória**: A busca utilizou "CEFAZOLIN SODIUM" (inglês), mas a ANVISA registra o fármaco como **"cefazolina sódica"** (português). Essa discrepância provavelmente causou o retorno de 0 resultados.
3. **Dados de segurança ausentes**: Sem advertências e contraindicações da bula oficial, a etapa de triagem de segurança (S1) está bloqueada, conforme sinalizado pelo gap DG001 classificado como *Blocking*.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém dados suficientes para avaliar o potencial de reposicionamento da cefazolin sódica. A ausência de `drugbank_id`, de registros regulatórios válidos e de previsões TxGNN impede qualquer análise de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**
- Repetir a busca regulatória com nomenclatura em português: **"cefazolina sódica"** ou pelo código ATC **J01DB04**
- Resolver o mapeamento DrugBank (verificar se o ID correto é **DB01327**) e reexecutar o pipeline TxGNN com o ID confirmado
- Baixar a bula ANVISA/TFDA para extrair advertências, contraindicações e MOA oficial (gap DG001 — bloqueante)
- Após correção de nomenclatura e mapeamento, gerar novo Evidence Pack e reavaliar
---

