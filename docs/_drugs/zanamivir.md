---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

O skill TxGNN Pipeline confirma o contexto de trabalho. A tarefa é geração de relatório de reposicionamento — área coberta pelo sistema prompt. Prosseguindo com o relatório.

---

# Zanamivir: Da influenza à pielonefrite

## Resumo

Zanamivir é um inibidor de neuraminidase viral (NAI), originalmente utilizado no tratamento e prevenção da gripe (influenza A e B).
O modelo TxGNN prevê que pode ser eficaz para **Pielonefrite (Pyelonephritis)** como nova indicação,
porém atualmente **não há ensaios clínicos** nem **publicações** apoiando diretamente esta direção — a previsão baseia-se exclusivamente no modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Gripe (influenza A e B) |
| Nova Indicação Prevista | Pielonefrite (Pyelonephritis) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base nas informações presentes na literatura incluída no próprio pack, Zanamivir é um **inibidor de neuraminidase (NAI)** — atua pela inibição competitiva da neuraminidase de superfície do vírus influenza (uma glicoproteína essencial para a liberação de novos vírions das células infectadas), bloqueando assim a disseminação viral. Juntamente com o oseltamivir, é considerado o tratamento de escolha para influenza A e B.

A pielonefrite é uma infecção bacteriana do trato urinário superior, causada predominantemente por *Escherichia coli*. Embora algumas bactérias gram-negativas expressem sialidases bacterianas (enzimas estruturalmente relacionadas à neuraminidase viral, com papel na adesão às células hospedeiras), a atividade de Zanamivir sobre estas enzimas bacterianas **não possui validação clínica ou pré-clínica robusta**. O espectro de ação do fármaco é restrito à neuraminidase viral do influenza.

A pontuação elevada do TxGNN (99,84%) para esta associação muito provavelmente reflete **associações topológicas no grafo de conhecimento** entre nós de doenças infecciosas — e não um sinal biológico real. A hipótese de reposicionamento para pielonefrite não é convincente no estado atual das evidências, e a recomendação é aguardar antes de qualquer investigação adicional.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O fármaco possui **2 registros ativos** na ANVISA com situação **comercializado**. Os detalhes individuais dos registros (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no Evidence Pack atual e precisam ser obtidos diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para pielonefrite carece de fundamentação mecanística convincente e não conta com nenhum ensaio clínico ou publicação de suporte direto — trata-se de uma previsão exclusivamente baseada no modelo (L5), provavelmente gerada por artefato de topologia do grafo de conhecimento entre nós de doenças infecciosas.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação completo via DrugBank API (DG002 — severidade High)
- Levantar advertências e contraindicações da bula no portal ANVISA (DG001 — severidade Blocking)
- Verificar os detalhes dos 2 registros ANVISA (número, nome comercial, indicações aprovadas)
- Realizar busca exploratória de estudos pré-clínicos sobre atividade de Zanamivir contra sialidases bacterianas antes de qualquer decisão de Go
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

