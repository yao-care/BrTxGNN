---
layout: default
title: Bilastina
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 0
---

# Bilastina
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

# Bilastina: Da rinite alérgica — Análise de Reposicionamento Pendente

## Resumo

Bilastina é um anti-histamínico H1 de segunda geração, indicado para o tratamento da rinite alérgica (sazonal e perene) e urticária crônica espontânea. O modelo TxGNN **ainda não gerou previsões de reposicionamento** para este fármaco: os dados regulatórios brasileiros foram coletados com sucesso (19 registros identificados), porém a análise preditiva, os dados de segurança e os detalhes individuais dos registros permanecem pendentes de coleta.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Rinite alérgica (sazonal e perene); Urticária crônica espontânea |
| Nova Indicação Prevista | Análise TxGNN pendente |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 19 |
| Decisão Recomendada | Hold |

---

## Contexto Farmacológico

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base em conhecimento farmacológico geral, Bilastina é um antagonista seletivo e de alta afinidade pelos receptores H1 de histamina, pertencente à classe dos anti-histamínicos de segunda geração. Distingue-se dos agentes de primeira geração por apresentar perfil não sedativo e ausência de efeitos anticolinérgicos clinicamente relevantes, o que decorre da sua baixa penetração na barreira hematoencefálica.

Sua eficácia em rinite alérgica e urticária foi estabelecida em ensaios clínicos de fase 3, com aprovação em dezenas de países. O mecanismo de bloqueio do receptor H1 possui potencial de investigação em outras condições mediadas por histamina ou inflamação alérgica — mas essa análise só será possível após a geração das previsões TxGNN.

---

## Informações de Comercialização no Brasil

Os detalhes individuais dos registros (nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no Evidence Pack atual. Está confirmado que Bilastina possui **19 registros** na base regulatória brasileira com situação **comercializado**, porém a coleta dos campos individuais ainda não foi realizada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack de Bilastina encontra-se incompleto: não há previsões TxGNN, dados de segurança estruturados ou detalhes dos registros individuais. Sem a análise preditiva, não é possível identificar candidatos de reposicionamento nem avaliar a força das evidências para qualquer nova indicação.

**Para prosseguir, é necessário:**
- Executar a etapa de predição TxGNN para gerar `predicted_indications`
- Baixar e parsear os PDFs de bula da ANVISA para obter advertências e contraindicações *(Data Gap DG001 — Bloqueante)*
- Consultar o DrugBank API para obter o DrugBank ID e dados completos de MOA *(Data Gap DG002 — Alta prioridade)*
- Recuperar os detalhes individuais dos 19 registros (nome comercial, forma farmacêutica, indicação aprovada)
- Reexecutar a busca de interações medicamentosas (DDI) com o identificador correto do fármaco
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

