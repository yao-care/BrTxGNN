---
layout: default
title: Oseltamivir
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: Da influenza à pielonefrite

## Resumo em Uma Frase

Oseltamivir (Tamiflu®) é um inibidor seletivo de neuraminidase viral, originalmente indicado para o tratamento e a profilaxia da influenza A e B em adultos e crianças.
O modelo TxGNN prevê que pode ser eficaz para **Pielonefrite (Pyelonephritis)**, com pontuação de previsão de **97,85%**.
Atualmente, há **0 ensaios clínicos** e apenas **1 publicação** associada a essa direção — sem relação direta com a indicação proposta —, configurando provável falso positivo computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Tratamento e profilaxia da influenza A e B |
| Nova Indicação Prevista | Pielonefrite (Pyelonephritis) |
| Pontuação de Previsão TxGNN | 97,85% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Segundo informações conhecidas, Oseltamivir é um pró-fármaco convertido in vivo em seu metabólito ativo (oseltamivir carboxilato), que inibe seletivamente a neuraminidase (NA) dos vírus influenza A e B. Ao bloquear a liberação de novos vírions da superfície das células infectadas, impede a disseminação viral nas vias aéreas superiores e inferiores. Sua eficácia comprovada no tratamento e na prevenção da gripe sazonal e pandêmica é o fundamento de sua indicação aprovada.

A pielonefrite, por sua vez, é uma infecção bacteriana ascendente do trato urinário superior — causada predominantemente por *Escherichia coli* e outros bacilos gram-negativos — cujos mecanismos patogênicos envolvem adesinas bacterianas, toxinas e evasão da imunidade inata no parênquima renal. Não existe intersecção mecanística conhecida entre a inibição de neuraminidase viral e as vias de patogênese bacteriana da pielonefrite.

A análise do conjunto de evidências indica que esta previsão é muito provavelmente um **falso positivo gerado por similaridade de vizinhança no grafo de conhecimento**. A alta pontuação TxGNN (97,85%) reflete a proximidade topológica dos nós no grafo, e não uma relação farmacológica real. A única publicação recuperada aborda o manejo da influenza na gestação — sem qualquer menção a pielonefrite —, reforçando o diagnóstico de erro de mapeamento bibliográfico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | *Presse Médicale* | Revisão sobre influenza na gestação: risco aumentado de pneumonia e hospitalização em grávidas durante surtos sazonais e pandêmicos. **Nenhum conteúdo relacionado a pielonefrite.** |

> ⚠️ **Nota de qualidade**: O único artigo recuperado trata exclusivamente de influenza na gestação. Sua associação à indicação "pielonefrite" representa muito provavelmente um erro de mapeamento bibliográfico no pipeline de busca, sem valor como evidência de suporte para este reposicionamento.

---

## Informações de Comercialização no Brasil

Oseltamivir está registrado no Brasil com **8 registros ativos** na ANVISA, confirmando sua comercialização regular no mercado nacional. Os detalhes individuais de cada registro (nome comercial, forma farmacêutica e texto completo da indicação aprovada) não estão disponíveis nesta versão do pacote de evidências.

Para consulta dos registros vigentes, acesse: [Consulta de Medicamentos — ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para pielonefrite enquadra-se no nível de evidência L5 (exclusivamente computacional), sem respaldo de ensaios clínicos e com única literatura inteiramente irrelevante à indicação proposta. A análise mecanística demonstra incompatibilidade fundamental entre a ação antiviral de Oseltamivir (inibição de NA viral) e a patogênese bacteriana da pielonefrite; o alto escore de previsão é atribuível a artefatos de vizinhança no grafo de conhecimento (falso positivo topológico).

**Para reconsiderar esta indicação em estudos futuros, seria necessário:**
- Identificar hipótese mecanística biologicamente plausível — por exemplo, investigar se neuraminidases bacterianas uropatogênicas (ex.: de *E. coli*) possuem sensibilidade a Oseltamivir in vitro
- Conduzir estudos pré-clínicos de atividade inibitória de Oseltamivir carboxilato contra neuraminidases de patógenos uropatogênicos
- Obter os dados de MOA completos via DrugBank para refinar a análise de intersecção mecanística
- Consultar especialistas em doenças infecciosas para avaliação independente da viabilidade biológica antes de qualquer investimento em pesquisa
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

