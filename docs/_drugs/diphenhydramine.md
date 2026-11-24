---
layout: default
title: Diphenhydramine
parent: Apenas Predição do Modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 1
monitor_inn: "Diphenhydramine"
predicted_indications: ["rosacea conjunctivitis"]
last_modified_at: 2026-11-24
description: "Diphenhydramine: nova indicação prevista, conjuntivite rosácea (rosacea conjunctivitis) (nível de evidência L5). Indicação original: ANTI-HISTAMINICOS SISTEMICOS"
---

# Diphenhydramine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Difenidramina: anti-histamínico H1 → Conjuntivite rosácea (rosacea conjunctivitis)
{: .text-alpha }

## Resumo em Uma Frase

A difenidramina é um anti-histamínico de uso sistêmico e tópico, também presente em produtos antieméticos, antitussígenos e para orofaringe.
O modelo TxGNN prevê que pode ser eficaz para **conjuntivite rosácea (rosacea conjunctivitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTI-HISTAMINICOS SISTEMICOS; ANTIEMETICOS E ANTINAUSEANTES; ANTITUSSIGENOS; ANTITUSSIGENOS-ASSOCIACOES MEDICAMENTOSAS; ANTIALERGICOS TOPICOS; PRODUTOS PARA OROFARINGE |
| Nova Indicação Prevista | conjuntivite rosácea (rosacea conjunctivitis) |
| Pontuação de Previsão TxGNN | 0,9920 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 6) |
| Número de Registros | 6 (ativos: 6) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Clinical Pharmacology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Diphenhydramine (tradução não oficial): “O cloridrato de difenidramina é um anti-histamínico com efeitos colaterais anticolinérgicos (de ressecamento) e sedativos. Os anti-histamínicos parecem competir com a histamina pelos sítios receptores celulares nas células efetoras. O cloridrato de difenidramina na forma injetável tem início de ação rápido.” Texto original em inglês: "Diphenhydramine hydrochloride is an antihistamine with anticholinergic (drying) and sedative side effects. Antihistamines appear to compete with histamine for cell receptor sites on effector cells. Diphenhydramine hydrochloride in the injectable form has a rapid onset of action." ([DailyMed: diphenhydramine hydrochloride prescribing information, Henry Schein, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af972e71-62ab-40c6-925a-cbcb4d6720a4), versão de 2026-10-28; acessado em 2026-11-19). Sabe-se que a difenidramina é um antagonista do receptor H1 da histamina, e, em tese, poderia reduzir a inflamação da superfície ocular mediada por histamina.

Por outro lado, a conjuntivite rosácea é impulsionada principalmente por disfunção das glândulas meibomianas, ativação da imunidade inata e fatores microbianos ou relacionados ao *Demodex*. O bloqueio de histamina, portanto, tende a atacar apenas uma parte do problema. A ligação mecanística é plausível, mas especulativa.

A previsão baseia-se somente na pontuação do modelo. Nenhum ensaio clínico ou publicação sustenta a relação entre a difenidramina e esta doença.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 101180653 | LENIX | Ativo |
| 102350421 | ENDCOFF | Ativo |
| 102980170 | DIFENIDRIN | Ativo |
| 115600099 | BENATUX | Ativo |
| 155840134 | CALAMYN | Ativo |
| 157211204 | BENALET | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

**Interações Medicamentosas** (100 interações registradas; exemplos):
- **Gravidade maior**: citrato de potássio, eliglustat.
- **Gravidade moderada**: hiosciamina, loperamida, bupropiona, morfina, atropina, lorcasserina, glicopirrônio, diciclomina, clidínio, dronabinol, eluxadolina, metoclopramida, nabilona, entre outros. Muitos são anticolinérgicos ou depressores do sistema nervoso central, com risco de efeitos aditivos.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (0,9920), mas não há nenhum ensaio clínico ou publicação sobre conjuntivite rosácea; o nível de evidência é L5. O mecanismo da doença vai além da via da histamina.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Completar os dados de mecanismo de ação no DrugBank.
- Realizar revisão da literatura e estudos pré-clínicos ou piloto sobre anti-histamínicos oculares na conjuntivite rosácea.
- Avaliar a compatibilidade da via de administração (por exemplo, formulação oftálmica), ainda pendente.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: diphenhydramine hydrochloride prescribing information, Henry Schein, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af972e71-62ab-40c6-925a-cbcb4d6720a4) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

