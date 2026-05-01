---
layout: default
title: Benznidazol
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 0
---

# Benznidazol
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

# Benznidazol: Da Doença de Chagas — Previsão TxGNN Indisponível

## Resumo em Uma Frase

Benznidazol é um antiparasitário nitroimidazólico utilizado como tratamento de primeira linha para a Doença de Chagas (tripanossomíase americana), causada pelo *Trypanosoma cruzi*.
O modelo TxGNN **ainda não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise.
Devido à ausência de indicações previstas e a múltiplos dados faltantes críticos, este relatório não pode concluir a avaliação completa.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Chagas (*Trypanosoma cruzi*) |
| Nova Indicação Prevista | Não disponível (TxGNN sem previsões) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há previsões de reposicionamento geradas pelo modelo TxGNN para o Benznidazol neste ciclo de análise. Além disso, não há dados detalhados sobre o mecanismo de ação (MOA) disponíveis no Evidence Pack.

Com base em conhecimento farmacológico estabelecido, o Benznidazol é um derivado do grupo 2-nitroimidazol. Seu mecanismo de ação envolve a redução do grupo nitro por nitrorreductases parasitárias, gerando intermediários reativos que causam dano oxidativo ao DNA e às proteínas do *T. cruzi*. Este mecanismo seletivo para organismos com sistema nitrorreductase-dependente é distinto dos alvos mamíferos, o que historicamente limitou o interesse de reposicionamento para patologias humanas não-infecciosas.

Para que uma análise de reposicionamento seja possível, é necessário primeiro completar o mapeamento DrugBank (para obter o `drugbank_id`) e executar o pipeline completo do TxGNN com este fármaco incluído no conjunto de inferência.

---

## Informações de Comercialização no Brasil

O fármaco possui **2 registros ativos** no Brasil, porém os detalhes individuais (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não foram recuperados neste ciclo de coleta. Os dados de registro precisam ser complementados via consulta direta à base de dados da ANVISA.

> ℹ️ Nota: O Benznidazol é fabricado no Brasil pelo **LAFEPE** (Laboratório Farmacêutico do Estado de Pernambuco), sendo um medicamento estratégico para o Programa Nacional de Controle da Doença de Chagas do Ministério da Saúde.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em itens críticos — não há previsões TxGNN disponíveis, os dados de registro da ANVISA não foram recuperados, e tanto o MOA quanto as informações de segurança estão ausentes. Sem previsão de nova indicação, não é possível realizar a avaliação de reposicionamento.

**Para prosseguir, é necessário:**
- [ ] **[Bloqueante]** Baixar e parsear a bula (PDF ANVISA) para obter advertências, contraindicações e MOA detalhado
- [ ] **[Alta prioridade]** Obter o `drugbank_id` do Benznidazol via API do DrugBank (busca pelo INN `benznidazole`) para habilitar o pipeline TxGNN
- [ ] **[Alta prioridade]** Re-executar o pipeline `run_kg_prediction.py` após mapear o fármaco ao DrugBank ID
- [ ] Complementar os campos dos 2 registros ANVISA (número, nome comercial, forma farmacêutica, indicação aprovada)
- [ ] Verificar se há ensaios clínicos em andamento no ClinicalTrials.gov para Benznidazol em indicações não-Chagas (ex.: outras infecções parasitárias, uso profilático)
---

