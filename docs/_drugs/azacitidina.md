---
layout: default
title: Azacitidina
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 0
---

# Azacitidina
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

# Azacitidina: Avaliação de Reposicionamento — Previsão TxGNN Pendente

## Resumo em Uma Frase

Azacitidina (AZACITIDINA) é um agente antineoplásico da classe dos análogos de nucleosídeo de pirimidina, com amplo uso clínico estabelecido em síndromes mielodisplásicas e leucemias mieloides. O Evidence Pack recebido **não contém previsões de novas indicações pelo modelo TxGNN**, e dados críticos como indicação original aprovada, mecanismo de ação e segurança estão pendentes de coleta — impedindo a condução de uma avaliação completa de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Aguardando coleta (ANVISA / bula) |
| Nova Indicação Prevista | Previsão TxGNN ainda não gerada |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (nenhum dado de estudos disponível no pacote) |
| Situação no Mercado Brasileiro | Comercializado |
| Número de Registros | 11 |
| Decisão Recomendada | **Hold** |

---

## Citotoxicidade

> Azacitidina é um fármaco antineoplásico citotóxico — esta seção é obrigatória.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — análogo de nucleosídeo de pirimidina com ação hipometilante (inibidor de DNA metiltransferase) |
| Risco de Mielossupressão | **Alto** — neutropenia, trombocitopenia e anemia são os efeitos adversos hematológicos mais frequentes e clinicamente relevantes |
| Classificação de Emetogenicidade | **Médio a alto** — varia conforme a via de administração (subcutânea apresenta menor emetogenicidade que a intravenosa) |
| Itens de Monitoramento | Hemograma completo com diferencial antes de cada ciclo; função hepática (TGO, TGP, bilirrubinas); função renal (creatinina, ureia); eletrólitos séricos |
| Proteção no Manuseio | Obrigatório seguir protocolos de manuseio de citotóxicos; uso de EPI (luvas duplas, avental impermeável, máscara) na preparação e administração |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em itens bloqueantes: o pipeline TxGNN não gerou previsões de novas indicações para Azacitidina, os 11 registros ANVISA não possuem detalhes de indicações aprovadas, e os dados de advertências e contraindicações ainda não foram coletados — tornando inviável qualquer análise de reposicionamento neste momento.

**Para prosseguir, é necessário:**

- **[Crítico]** Re-executar o pipeline TxGNN para Azacitidina: verificar se o mapeamento DrugBank foi concluído e se o arquivo `repurposing_candidates.csv` contém entradas para este fármaco
- **[Crítico]** Confirmar o DrugBank ID de Azacitidina via API (consulta registrada como `success` mas `drugbank_id` retornou `null`) e recuperar o mecanismo de ação detalhado
- **[Bloqueante]** Coletar os detalhes dos 11 registros ANVISA: números de registro, nomes comerciais, formas farmacêuticas e textos das indicações aprovadas
- **[Bloqueante]** Baixar e parsear a(s) bula(s) ANVISA para extrair advertências principais, contraindicações e posologia
- **[Recomendado]** Investigar por que a consulta de DDI retornou `not_found` — tentar com variações do nome INN ("azacitidine", "5-azacytidine") e reprocessar
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

