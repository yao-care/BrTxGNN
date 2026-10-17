---
layout: default
title: Tizanidine
parent: Apenas Predição do Modelo (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tizanidine: nova indicação prevista, Transtorno de enxaqueca (Migraine disorder) (nível de evidência L5). Indicação original: Relaxantes musculares centrais simples"
monitor_inn: "Tizanidine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "Tourette syndrome", "ulerythema ophryogenesis", "trichotillomania", "headache disorder", "dysthymic disorder", "fibromyalgia"]
---

# Tizanidine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Tizanidina: De relaxante muscular central a transtorno de enxaqueca

## Resumo em Uma Frase

A tizanidina foi originalmente registrada no Brasil como relaxante muscular de ação central.
O modelo TxGNN prevê que pode ser eficaz para **transtorno de enxaqueca (migraine disorder)**,
atualmente com **2 ensaios clínicos registrados** (1 deles diretamente relevante) e **16 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Relaxantes musculares centrais simples |
| Nova Indicação Prevista | Transtorno de enxaqueca (Migraine disorder) |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L1 (conforme classificação do conjunto de dados; ver ressalva na conclusão) |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 3 (todos cancelados) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a tizanidina é um agonista alfa-2 adrenérgico de ação central, usado como relaxante muscular, e mecanisticamente pode ser aplicável à enxaqueca.

A relação entre a indicação original e a nova é plausível: o agonismo alfa-2 pode reduzir a transmissão nociceptiva trigeminovascular e a tensão da musculatura pericraniana, que contribui para as cefaleias. Ou seja, o efeito sobre o tônus muscular e o efeito sobre a dor central podem convergir na profilaxia da enxaqueca.

Há apoio clínico direto: um estudo duplo-cego controlado por placebo em cefaleia crônica diária (Saper et al., 2002) e um ensaio de Fase 3 em prevenção de enxaqueca. Também foram previstas, em ordem decrescente de pontuação, outras indicações (cefaleia em geral, fibromialgia, síndrome de Tourette etc.), mas apenas a cefaleia e, de forma preliminar, a fibromialgia contam com algum respaldo.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Desconhecido | 189 | Estudo multicêntrico, randomizado, duplo-cego e controlado por placebo de tizanidina oral na prevenção de crises de enxaqueca episódica em adultos de 18 a 65 anos. Sem resultados disponíveis; conclusão prevista para dez/2025. |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Concluído | 300 | Estudo observacional (PACE) de 24 semanas sobre AINEs tópicos para alívio da dor. Relevância baixa; sem vínculo claro com a tizanidina. |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Tizanidina versus placebo como profilaxia adjuvante de cefaleia crônica diária (enxaqueca crônica, cefaleia migranosa ou tensional), estudo multicêntrico duplo-cego |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Revisão | CNS Drugs | Fármacos que atuam em espasmo e tônus muscular (baclofeno, tizanidina, toxina botulínica) como prevenção de enxaqueca e cefaleia tensional; faltam estudos controlados |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Consenso | Arquivos de Neuro-Psiquiatria | Consenso da Sociedade Brasileira de Cefaleia sobre o tratamento da enxaqueca crônica |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Estudo aberto | Headache | Titulação de dose, aberta, de tizanidina na profilaxia da cefaleia crônica diária (eficácia e tolerabilidade) |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Revisão | Current Pain and Headache Reports | Novas opções de prevenção da enxaqueca, incluindo a tizanidina entre outros agentes |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | Revisão | Neurological Sciences | Revisão dos estudos duplo-cegos controlados por placebo na profilaxia da enxaqueca crônica |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Revisão | Headache | Tratamento profilático da cefaleia crônica diária; a tizanidina está entre os poucos fármacos com evidência |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | Relato/regime clínico | Headache | Tizanidina em baixa dose com AINEs na desintoxicação da cefaleia por abuso de analgésicos |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | Pré-clínico/formulação | J Control Release | Automontagem supramolecular de tizanidina com meloxicam, com efeito antienxaqueca sinérgico |
| [21770931](https://pubmed.ncbi.nlm.nih.gov/21770931/) | 2011 | Revisão | Headache | Ensaios clínicos em abuso de medicação e profilaxia da enxaqueca crônica; tizanidina citada entre os agentes avaliados |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 123520196 (cancelado) | Cloridrato de Tizanidina | Não informada | Relaxantes musculares centrais simples |
| Registro 156490008 (cancelado) | Cloridrato de Tizanidina | Não informada | Relaxantes musculares centrais simples |
| Registro 100470659 (cancelado) | Sirdalud | Não informada | Relaxantes musculares centrais simples |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: insuficiência hepática, doença renal, transtornos psicóticos (incluindo esquizofreniforme e esquizoafetivo), transtornos mentais em geral e transtornos hipotensivos.
- **Interações Medicamentosas**: foram identificadas 100 interações; entre as principais, de gravidade **maior**: famotidina, cimetidina, morfina, dolasetrona e ácido obeticólico. De gravidade moderada: claritromicina, levofloxacino, metoclopramida, naltrexona, atropina, hiosciamina, dicicloverina, loperamida, dronabinol, nabilona, palonosetrona, entre outras. Inibidores da CYP1A2 (p. ex., fluvoxamina, ciprofloxacino) exigem atenção especial.
- **Pontos de atenção do perfil do fármaco**: sedação, hipotensão e risco de hepatotoxicidade, com necessidade de monitoramento hepático.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há um ensaio de Fase 3 diretamente testando a tizanidina na prevenção da enxaqueca e um RCT controlado por placebo em cefaleia crônica diária, além de numerosas revisões. Porém, o ensaio de Fase 3 tem status desconhecido e sem resultados publicados; por isso, o nível L1 deve ser tratado com cautela, pois a condição de "≥2 RCTs de Fase 3 concluídos" não é claramente atendida pelos dados disponíveis.
- Todos os registros brasileiros estão cancelados, o que limita a via regulatória imediata.

**Para prosseguir, é necessário:**
- Obter os resultados do NCT05484349 (confirmar status e conclusão).
- Obter dados do mecanismo de ação (DrugBank) e da bula da ANVISA (advertências e contraindicações), atualmente ausentes.
- Definir plano de monitoramento de função hepática, pressão arterial e sedação, e regras para uso concomitante de inibidores da CYP1A2.
- Avaliar a situação regulatória: novo registro ou reativação, já que não há registro vigente no Brasil.
- As demais indicações previstas (fibromialgia, síndrome de Tourette, tricotilomania etc.) permanecem em *Hold* ou em fase de pergunta de pesquisa, sem evidência suficiente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

