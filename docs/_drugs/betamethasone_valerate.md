---
layout: default
title: Betamethasone Valerate
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 0
---

# Betamethasone Valerate
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

# Betamethasone Valerate: Sem Previsão de Reposicionamento Disponível

## Resumo

Betamethasone Valerate é um corticosteroide tópico de potência média a alta, classicamente utilizado no tratamento de condições inflamatórias da pele, como eczema, psoríase e dermatites.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo de análise atual, possivelmente por ausência do identificador DrugBank ID no grafo de conhecimento.
O medicamento **não possui registros ativos** no mercado brasileiro, e os dados de segurança apresentam lacunas críticas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não registrada no Evidence Pack |
| Nova Indicação Prevista | Nenhuma — sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Os dados de advertências e contraindicações não estão disponíveis neste Evidence Pack. Consulte a bula ou referência farmacológica oficial para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não produziu previsões de reposicionamento para este fármaco — o que, aliado à ausência de DrugBank ID e à falta de registro ANVISA, torna inviável qualquer análise de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**
- **Resolver o DrugBank ID ausente**: o log de consulta registrou 1 resultado no DrugBank, mas o identificador não foi capturado no objeto `drug` — verificar e corrigir o pipeline de extração
- **Re-executar a predição TxGNN** com o DrugBank ID correto para gerar candidatos de reposicionamento
- **Verificar o status ANVISA**: confirmar se há registros com denominação alternativa (ex.: Betametasona Valerato, Betamethasone 17-valerate)
- **Coletar dados de MOA**: utilizar o DrugBank ID recuperado para consultar mecanismo de ação via API
- **Obter advertências e contraindicações**: baixar bula de referência (ANVISA, EMA ou FDA) para completar o perfil de segurança
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

