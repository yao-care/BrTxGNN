---
layout: default
title: Clobutinol
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Clobutinol
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

Usando o skill `txgnn-pipeline` para orientação sobre relatórios TxGNN. Agora vou gerar o relatório com base no Evidence Pack.

---

# Clobutinol: De antitussivo à febre tifoide

## Resumo em Uma Frase

Clobutinol é um agente antitussivo de ação central, utilizado historicamente no controle da tosse seca. O modelo TxGNN prevê que pode ser eficaz para **Febre Tifoide (Typhoid Fever)**, com pontuação de **99,98%** — porém, atualmente **sem nenhum ensaio clínico** e **sem publicações científicas** apoiando esta direção, e com importantes ressalvas de segurança que limitam qualquer avanço.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|---------|
| Indicação Original | Antitussivo (controle da tosse seca) |
| Nova Indicação Prevista | Febre Tifoide (Typhoid Fever) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações farmacológicas conhecidas, Clobutinol é um antitussivo de ação central que suprime o reflexo da tosse por atuação sobre centros no sistema nervoso central — sem atividade antibacteriana, antiparasitária ou imunomoduladora documentada.

A previsão de febre tifoide pelo TxGNN recebeu pontuação elevada (0,9998), mas a justificativa mecanística é **extremamente fraca**: a febre tifoide é causada pela bactéria *Salmonella typhi*, uma infecção sistêmica grave que exige tratamento com antibióticos específicos. Clobutinol não possui nenhuma atividade antibacteriana conhecida. A alta pontuação do modelo provavelmente decorre de conexões compartilhadas no grafo de conhecimento (por exemplo, vias imunológicas gerais), e não de uma relação farmacológica direta.

Vale destacar que este padrão se repete em todas as 10 indicações previstas: nenhuma possui ensaios clínicos, literatura de suporte ou conexão mecanística biologicamente plausível com Clobutinol. Todas receberam recomendação **Hold** e nível **L5**, apontando para um cenário de previsão puramente computacional sem base empírica estabelecida.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para nenhuma das indicações previstas pelo TxGNN para Clobutinol.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para nenhuma das indicações previstas pelo TxGNN para Clobutinol.

---

## Informações de Comercialização no Brasil

O fármaco possui **20 registros ativos** no mercado (status: comercializado). Os detalhes individuais de cada registro — nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack e deverão ser obtidos diretamente junto à ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as 10 indicações previstas pelo TxGNN apresentam nível de evidência L5 (apenas previsão do modelo, sem estudos reais), ausência total de ensaios clínicos e literatura de suporte, e mecanismos de ação biologicamente implausíveis para Clobutinol — um antitussivo sem atividade antibacteriana, antiparasitária, imunológica ou antifibrótica documentada.

**Para prosseguir, é necessário:**
- Obter dados de MOA via DrugBank API (DG002 — severity: High)
- Baixar e analisar a bula para advertências e contraindicações (DG001 — severity: Blocking)
- Verificar o histórico regulatório de segurança cardíaca (risco de prolongamento do intervalo QT, que motivou retiradas de mercado em outros países)
- Realizar busca de estudos pré-clínicos (*in vitro*/*in vivo*) para qualquer das indicações antes de considerar avanço
- Revisar se indicações com conexão indireta ao sistema respiratório (pneumonia, bronquiolite obliterante) têm suporte em literatura especializada, considerando o perfil de risco do fármaco
---

