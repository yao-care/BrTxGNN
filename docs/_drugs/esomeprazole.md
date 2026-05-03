---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Esomeprazole
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

# Esomeprazole: Do refluxo gastroesofágico ao refluxo duodenogástrico

## Resumo em Uma Frase

Esomeprazole é um inibidor da bomba de prótons (PPI) amplamente utilizado no tratamento da doença do refluxo gastroesofágico (DRGE), úlceras pépticas e erradicação de *Helicobacter pylori*.
O modelo TxGNN prevê que pode ser eficaz para **Refluxo Duodenogástrico (Duodenogastric Reflux)**, com pontuação de **99.53%**.
Atualmente, há **0 ensaios clínicos** e **1 publicação** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença do refluxo gastroesofágico, úlcera péptica, erradicação de *H. pylori* |
| Nova Indicação Prevista | Refluxo Duodenogástrico (Duodenogastric Reflux) |
| Pontuação de Previsão TxGNN | 99.53% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Esomeprazole é o S-isômero óptico do omeprazol e o primeiro PPI desenvolvido como isômero único. Seu mecanismo de ação consiste na inibição irreversível da H⁺/K⁺-ATPase (bomba de prótons) nas células parietais gástricas, resultando em supressão dose-dependente da secreção de ácido clorídrico. Por apresentar menor susceptibilidade ao metabolismo pela via CYP2C19 em comparação ao omeprazol racêmico, o Esomeprazole confere maior biodisponibilidade sistêmica e controle do pH intragástrico mais consistente e duradouro ao longo de 24 horas.

O refluxo duodenogástrico caracteriza-se pelo retorno de conteúdo duodenal — bile, enzimas pancreáticas e bicarbonato — ao estômago. Sua patogênese abrange dois subtipos distintos: o refluxo biliar **puro** (de natureza alcalina, no qual os PPIs têm eficácia muito limitada, pois não atuam sobre o componente biliar em si) e o refluxo **misto** ácido-bile (no qual a supressão ácida pelo PPI pode reduzir o dano à mucosa ao atenuar a sinergia lesiva entre ácido e bile). A ponte mecanicista entre a indicação original de Esomeprazole e o refluxo duodenogástrico existe, portanto, apenas no contexto do subtipo misto.

A pontuação TxGNN extremamente elevada (99.53%) provavelmente reflete a forte conexão no grafo de conhecimento entre DRGE e PPIs, estendida por adjacência ao nó de refluxo duodenogástrico — um efeito de vizinhança que não implica necessariamente eficácia terapêutica direta. A ausência completa de ensaios clínicos específicos e a escassez de literatura direcionada recomenda cautela antes de qualquer aplicação clínica nesta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para refluxo duodenogástrico com Esomeprazole.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Narrative Review | European Journal of Clinical Pharmacology | Revisão abrangente de uso clínico e farmacocinética dos PPIs; confirma PPIs como fármacos de primeira escolha para úlcera péptica, DRGE, infecção por *H. pylori*, lesões por AINEs e síndrome de Zollinger-Ellison — sem menção específica ao refluxo duodenogástrico |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação TxGNN elevada (99.53%), a evidência clínica direta para refluxo duodenogástrico é insuficiente — não há nenhum ensaio clínico registrado e apenas 1 publicação de revisão narrativa indiretamente relacionada. O mecanismo de ação do Esomeprazole (supressão ácida) tem relevância apenas parcial nesta indicação, sendo aplicável somente ao subtipo de refluxo misto ácido-bile, e não ao refluxo biliar puro, que é mecanisticamente distinto.

**Para prosseguir, é necessário:**
- Confirmar dados de registro na ANVISA e obter informações completas de segurança a partir da bula aprovada
- Realizar revisão sistemática dedicada ao papel dos PPIs no refluxo duodenogástrico misto, distinguindo-o do refluxo biliar puro
- Investigar se o alto escore TxGNN representa uma associação causal real ou um artefato de proximidade no grafo de conhecimento (análise de vizinhança)
- Avaliar a viabilidade de um estudo exploratório de Fase 2 com desfecho primário centrado no componente misto do refluxo duodenogástrico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

