---
noindex: true
sitemap: false
layout: default
title: Betamethasone Valerate
parent: Apenas Predição do Modelo (L5)
nav_order: 130
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Betamethasone Valerate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Betamethasone Valerate: Sem Previsão de Reposicionamento Disponível
{: .text-alpha }

## Resumo

Betamethasone Valerate é um corticosteroide tópico de potência média a alta, classicamente utilizado no tratamento de condições inflamatórias da pele, como eczema, psoríase e dermatites.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo de análise atual, possivelmente por ausência do identificador DrugBank ID no grafo de conhecimento.
Os dados de segurança apresentam lacunas críticas.

<!-- review:begin br-lic-20261106-betamethasone_valerate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O medicamento **não possui registros ativos** no mercado brasileiro, e os dados de segurança apresentam lacunas críticas.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-betamethasone_valerate-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não registrada no Evidence Pack |
| Nova Indicação Prevista | Nenhuma — sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | pelo menos 20 |
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

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “medicamento **não possui registros ativos** no mercado brasileiro, e o” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

