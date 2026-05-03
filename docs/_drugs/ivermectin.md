---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

Usando o skill `txgnn-pipeline` para orientar a geração do relatório de reposicionamento. Agora vou analisar o Evidence Pack e produzir o relatório.

---

# Ivermectin: De antiparasitário à Candidíase Vulvovaginal

## Resumo em Uma Frase

Ivermectin é um agente antiparasitário amplamente utilizado no tratamento de infecções por helmintos e ectoparasitas, como escabiose, estrongiloidíase e oncocercose. O modelo TxGNN prevê que pode ser eficaz para **Candidíase Vulvovaginal (vulvovaginal candidiasis)**, porém atualmente não há **ensaios clínicos** nem **publicações** apoiando esta direção. A pontuação de previsão elevada (99,95%) contrasta diretamente com a ausência completa de base mecanística e de evidências clínicas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções parasitárias (escabiose, estrongiloidíase, oncocercose) |
| Nova Indicação Prevista | Candidíase Vulvovaginal (vulvovaginal candidiasis) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimentos consolidados, Ivermectin é um antiparasitário macrolídeo que atua seletivamente sobre os **canais iônicos glutamato-dependentes (GluCl)** em invertebrados — aumentando a permeabilidade da membrana ao cloreto e causando paralisia neuromuscular e morte dos parasitas. Este mecanismo é altamente específico para helmintos e artrópodes, como *Sarcoptes scabiei* (causador da escabiose) e *Strongyloides stercoralis*.

A candidíase vulvovaginal é causada por fungos do gênero *Candida*, predominantemente *Candida albicans*. **Fungos não possuem receptores GluCl** — o alvo farmacológico central do Ivermectin — o que elimina a base biológica para qualquer ação antifúngica direta. Embora estudos in vitro de largo espectro tenham sugerido que Ivermectin possa inibir o transporte nuclear via importina α/β (mecanismo explorado em pesquisas antivirais), não há dados pré-clínicos ou clínicos que demonstrem atividade relevante contra *Candida* spp.

A pontuação elevada gerada pelo TxGNN provavelmente reflete **padrões de co-ocorrência no grafo de conhecimento** — por exemplo, Ivermectin e *Candida* aparecem juntos em registros de pacientes imunossuprimidos com infecções simultâneas (conforme evidenciado pelos case reports encontrados, onde o Ivermectin foi usado para tratar escabiose em pacientes com candidíase de base) — e não uma relação farmacológica real. Esta previsão é considerada um **artefato do modelo**, sem plausibilidade mecanística.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Ivermectin em candidíase vulvovaginal.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Ivermectin em candidíase vulvovaginal.

---

## Informações de Comercialização no Brasil

Ivermectin possui **20 registros ativos** no mercado brasileiro (status: Comercializado). Os detalhes individuais de cada registro — nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack e devem ser consultados diretamente na base de dados da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação TxGNN elevada (99,95%), a previsão não possui suporte mecanístico — Ivermectin atua em canais GluCl exclusivos de invertebrados, estrutura inexistente em fungos. Não há nenhum ensaio clínico nem publicação científica específica que apoie o uso de Ivermectin em candidíase vulvovaginal, configurando evidência nível L5 (previsão de modelo sem suporte empírico real). A previsão deve ser interpretada como artefato de co-ocorrência no grafo de conhecimento, não como sinal de reposicionamento.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação completo (MOA) via DrugBank API — remediação do gap DG002
- Baixar e analisar bulas ANVISA para levantar advertências e contraindicações — remediação do gap DG001
- Realizar estudos in vitro para verificar se há qualquer atividade de Ivermectin contra *Candida* spp. antes de considerar avanço
- Investigar a origem da previsão no grafo TxGNN (auditoria de nós adjacentes) para confirmar se se trata de viés de co-ocorrência e documentar como falso positivo do modelo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

