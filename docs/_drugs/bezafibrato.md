---
layout: default
title: Bezafibrato
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 0
---

# Bezafibrato
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

# Bezafibrato: Avaliação de Reposicionamento — Previsões TxGNN Pendentes

## Resumo

Bezafibrato é um fármaco da classe dos fibratos, utilizado no tratamento de **dislipidemia** (hipertrigliceridemia e hiperlipidemia mista), com 18 registros ativos no Brasil.
O presente Evidence Pack não contém previsões TxGNN para novas indicações — o pipeline de predição ainda não foi executado ou não retornou candidatos para este fármaco.
São necessárias etapas adicionais de coleta de dados (MOA, indicações aprovadas detalhadas, dados de segurança) antes que uma avaliação completa de reposicionamento possa ser conduzida.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dislipidemia (hipertrigliceridemia, hiperlipidemia mista) |
| Nova Indicação Prevista | Não disponível neste Evidence Pack |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | Não disponível |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 18 |
| Decisão Recomendada | Hold |

---

## Sobre o Fármaco

Bezafibrato pertence à classe dos **fibratos**, fármacos agonistas dos receptores PPAR (Peroxisome Proliferator-Activated Receptors). Diferentemente de outros fibratos que ativam predominantemente o PPAR-α, o bezafibrato é considerado um **agonista pan-PPAR** (PPAR-α, PPAR-β/δ e PPAR-γ), o que lhe confere um perfil farmacológico mais amplo — e é exatamente esse espectro que justifica interesse em indicações além da dislipidemia.

No entanto, os dados de mecanismo de ação detalhados (MOA) não foram incorporados a este Evidence Pack. Consultas ao DrugBank foram realizadas com sucesso (1 resultado encontrado), mas os dados ainda não foram integrados ao relatório.

> **Nota:** Os dados regulatórios detalhados dos 18 registros no Brasil (nome comercial, forma farmacêutica, texto de indicação aprovada) também não estão disponíveis nesta versão do Evidence Pack. Os campos retornaram vazios na consulta à base TFDA/ANVISA.

---

## Informações de Comercialização no Brasil

O bezafibrato possui **18 registros ativos** no Brasil, confirmando que o fármaco está legalmente comercializado no país.

Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica, indicação aprovada) não constam neste Evidence Pack e precisam ser recuperados diretamente da base de dados da ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto — não há previsões TxGNN, dados de MOA, dados regulatórios detalhados nem informações de segurança disponíveis, o que impede qualquer avaliação fundamentada de potencial de reposicionamento.

**Para prosseguir, é necessário:**
- **[Bloqueante]** Obter advertências e contraindicações da bula registrada na ANVISA (DG001)
- **[Alta prioridade]** Integrar dados de MOA do DrugBank ao Evidence Pack (DG002)
- Recuperar os detalhes dos 18 registros (nome comercial, forma farmacêutica, indicação aprovada)
- Executar o pipeline de previsão TxGNN com os dados completos para gerar `predicted_indications`
- Após geração das previsões, coletar evidências de ensaios clínicos e literatura para as indicações candidatas
---

