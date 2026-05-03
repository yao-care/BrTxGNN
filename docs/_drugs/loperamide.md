---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Loperamide
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

A skill é sobre pipeline técnico — as instruções de relatório já estão no system prompt. Vou produzir o relatório agora.

---

# Loperamide: Da diarreia aguda à conjuntivite contagiosa aguda

## Resumo em Uma Frase

Loperamide é um antidiarreico clássico, amplamente utilizado no controle de diarreia aguda e crônica por sua ação agonista sobre os receptores μ-opioide do trato gastrointestinal. O modelo TxGNN prevê uma possível associação com **Conjuntivite Contagiosa Aguda (Acute Contagious Conjunctivitis)**, com pontuação de 99,97%; porém, **não há nenhum ensaio clínico nem publicação científica** apoiando esta direção, e a análise mecanística indica alta probabilidade de falso positivo por artefato do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro regulatório disponível no Brasil (uso estabelecido: controle de diarreia aguda e crônica) |
| Nova Indicação Prevista | Conjuntivite Contagiosa Aguda (Acute Contagious Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Por conhecimento farmacológico estabelecido, Loperamide (Imodium®) é um agonista seletivo dos receptores μ-opioide periféricos do trato gastrointestinal. Sua eficácia no controle da diarreia decorre da redução da motilidade intestinal, diminuição da secreção luminal de fluidos e eletrólitos, e aumento do tônus do esfíncter anal. Por não atravessar de forma significativa a barreira hematoencefálica em doses terapêuticas habituais, seus efeitos são essencialmente confinados ao intestino.

A relação entre este mecanismo intestinal e a conjuntivite contagiosa aguda é biologicamente implausível. Embora receptores opioides existam em tecidos oculares, não há evidência que suporte qualquer efeito terapêutico de um agonista μ-opioide administrado por via sistêmica ou oral sobre infecções conjuntivais de origem infecciosa. A própria análise de plausibilidade mecanística do Evidence Pack confirma a ausência de vínculo credível, atribuindo a alta pontuação TxGNN a um artefato de propagação por nós intermediários compartilhados no grafo.

Este padrão de pseudoassociação se repete de forma marcante no top 10 de previsões para este fármaco: **7 das 10 indicações previstas são variantes de conjuntivite** (conjuntivite folicular crônica, serosa, parasitária, pseudomembranosa, etc.), todas sem qualquer suporte mecanístico ou empírico. Trata-se de um cluster de predições espúrias gerado por conectividade indireta no grafo, e não de um sinal de reposicionamento legítimo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ **Alerta de segurança identificado na análise do top 10:** A previsão de Rank 2 (disenteria amebiana) apresenta sinal de segurança reverso. O artigo PMID [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) relata um caso de colite amebiana fulminante precipitada pelo uso de Loperamide — configurando contraindicação potencial, e não candidatura a reposicionamento. O uso de agentes antimotilidade em gastroenterites infecciosas graves já foi associado ao risco de megacólon tóxico.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão de Loperamide para conjuntivite contagiosa aguda não possui suporte mecanístico plausível nem qualquer evidência empírica (nível L5). A pontuação TxGNN elevada reflete artefato de conectividade no grafo de conhecimento, e não potencial terapêutico real. O padrão de cluster de conjuntivites no top 10 sugere necessidade de revisão do pipeline de mapeamento antes de qualquer análise aprofundada.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA do DrugBank (DG002 — severidade High)
- Obter advertências e contraindicações da bula ANVISA (DG001 — severidade Blocking)
- Investigar o sinal de segurança negativo identificado (PMID 17241255): risco de agravamento em infecções intestinais invasivas
- Revisar o pipeline TxGNN para identificar e corrigir o cluster de pseudoassociações com conjuntivite originado por nós intermediários compartilhados no grafo
- Avaliar separadamente a indicação de Rank 4 (gastroduodenite), a única com hipótese mecanística fraca e registro histórico na literatura (PMID 3520142, 1986), antes de qualquer decisão sobre avanço
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

