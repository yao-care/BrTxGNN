---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Com base no Evidence Pack, vou gerar o relatório seguindo o formato especificado.

---

# Mirtazapina: Da depressão maior à síndrome de Ohdo

## Resumo em Uma Frase

Mirtazapina é um antidepressivo da classe NaSSA (Noradrenérgico e Serotonérgico Específico), amplamente utilizado no tratamento do transtorno depressivo maior em diversas jurisdições, porém sem registro vigente no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Ohdo e variantes (Ohdo syndrome and variants)**,
porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Transtorno depressivo maior (sem registro vigente no Brasil) |
| Nova Indicação Prevista | Síndrome de Ohdo e variantes (Ohdo syndrome and variants) |
| Pontuação de Previsão TxGNN | 99,42% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimento farmacológico público, a mirtazapina pertence à classe NaSSA — bloqueia receptores α₂-adrenérgicos pré-sinápticos, receptores 5-HT₂A, 5-HT₂C e 5-HT₃, resultando em aumento da liberação de noradrenalina e serotonina. É aprovada para o transtorno depressivo maior em múltiplos países, embora não esteja registrada no Brasil.

A Síndrome de Ohdo é uma doença genética rara do neurodesenvolvimento, causada principalmente por mutações nos genes KAT6A (MYST3) ou MED13L — fatores de transcrição cujas alterações resultam em deficiência intelectual, ptose palpebral e defeitos cardíacos congênitos. Sua patogênese opera fundamentalmente no nível da regulação transcricional, sem relação fisiopatológica conhecida com a via monoaminérgica modulada pela mirtazapina.

A pontuação TxGNN elevada (99,42%) provavelmente reflete conexões topológicas no grafo de conhecimento — como comorbidades neuropsiquiátricas compartilhadas ou associações indiretas via nós intermediários — e não uma relação farmacológica direta. Vale notar que as três indicações previstas (Síndrome de Ohdo e variantes, subtipo BIDS-Ohdo e torticolo paroxístico benigno da infância) compartilham este mesmo padrão: alto escore TxGNN combinado com ausência total de evidências clínicas, sugerindo que os resultados decorrem de artefatos de duplicação ontológica ou ligações indiretas no grafo, em vez de hipóteses terapêuticas sustentáveis.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As três indicações previstas pelo TxGNN apresentam nível de evidência L5 — exclusivamente previsão do modelo, sem suporte de ensaios clínicos ou publicações científicas. Adicionalmente, o mecanismo de ação monoaminérgico da mirtazapina não possui via farmacológica conhecida capaz de corrigir o defeito de transcrição gênica subjacente à Síndrome de Ohdo, tornando a plausibilidade mecanística muito baixa. A ausência de registro no Brasil e os dois gaps de dados bloqueantes (MOA e advertências da bula) impedem a progressão para qualquer estágio de avaliação formal.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA via DrugBank API (DG002) para análise de ligação mecanística
- Obter advertências e contraindicações da bula ANVISA/TFDA (DG001) para avaliação de segurança inicial
- Avaliar, com especialistas em genética médica e doenças raras, se há vias biológicas secundárias que conectem a mirtazapina à fisiopatologia da Síndrome de Ohdo
- Considerar que ensaios clínicos para doenças ultra-raras como a Síndrome de Ohdo requerem delineamento especial (ex.: n-of-1 trials, registros de pacientes internacionais)
- Investigar se o alto escore reflete artefato ontológico no grafo de conhecimento antes de qualquer investimento em pesquisa translacional
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

