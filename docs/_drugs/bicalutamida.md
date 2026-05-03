---
layout: default
title: Bicalutamida
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 0
---

# Bicalutamida
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

# Bicalutamida: Do Câncer de Próstata — Avaliação de Reposicionamento Pendente

## Resumo

Bicalutamida é um antiandrogênio não esteroidal utilizado no tratamento do câncer de próstata, atuando como antagonista competitivo do receptor androgênico. O Evidence Pack fornecido **não contém previsões do modelo TxGNN** para novas indicações terapêuticas, pois o campo `predicted_indications` está vazio — o que impossibilita a geração de candidatos de reposicionamento nesta versão. Duas lacunas de dados críticas bloqueiam a continuidade da avaliação: ausência de informações de segurança da ANVISA (gravidade **Blocking**) e ausência do mecanismo de ação detalhado (gravidade **High**).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata (antiandrogênio não esteroidal) |
| Nova Indicação Prevista | — (sem previsão TxGNN neste pacote) |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 10 |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

Bicalutamida é empregada em oncologia (câncer de próstata), configurando o critério de exibição desta seção.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal antineoplásica (antiandrogênio não esteroidal) — **não** é citotóxico convencional |
| Risco de Mielossupressão | Baixo (mecanismo hormonal; sem ação citotóxica direta sobre medula óssea) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Função hepática (ALT/AST), PSA sérico, hemograma periódico |
| Proteção no Manuseio | Precauções padrão para fármacos com risco reprodutivo (classificado como *hazardous drug* pela NIOSH — categoria reprodutiva) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está estruturalmente incompleto — `predicted_indications` retornou lista vazia e os dados de registro ANVISA não foram populados, tornando inviável qualquer análise de reposicionamento ou avaliação de segurança nesta versão.

**Para prosseguir, é necessário:**
- **[Blocking]** Obter informações de segurança da bula ANVISA (advertências e contraindicações) — fazer download do PDF da bula no portal da ANVISA e extrair os dados relevantes
- **[High]** Mapear o DrugBank ID de bicalutamida e consultar o MOA via DrugBank API (campo `drugbank_id` atualmente nulo)
- Re-executar o pipeline TxGNN com o DrugBank ID correto para gerar as previsões de reposicionamento (`predicted_indications`)
- Re-popular os campos detalhados das 10 licenças ANVISA (número de registro, nome comercial, forma farmacêutica e indicação aprovada estão todos ausentes no pacote atual)
- Após resolução das lacunas acima, reprocessar o Evidence Pack em nova versão para obter relatório completo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

