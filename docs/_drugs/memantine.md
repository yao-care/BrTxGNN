---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Memantine
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

# Memantine: Da Demência de Alzheimer à Hipertensão Arterial Pulmonar

## Resumo em Uma Frase

Memantine é um antagonista não competitivo do receptor NMDA (N-metil-D-aspartato), amplamente reconhecido pelo tratamento da demência moderada a grave associada à doença de Alzheimer.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**, com pontuação de previsão de **99,54%**.
Atualmente, esta direção é apoiada por **0 ensaios clínicos** e **2 publicações**, configurando evidência em estágio ainda exploratório.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Demência moderada a grave (Doença de Alzheimer) |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 99,54% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Memantine atua bloqueando os canais iônicos dos receptores NMDA de forma não competitiva e dependente de voltagem, reduzindo a excitotoxicidade mediada pelo glutamato. Esse mecanismo está clinicamente estabelecido no contexto da doença de Alzheimer, onde a superativação do NMDAR leva à morte neuronal progressiva. A ação seletiva sobre receptores tonicamente ativados — poupando a transmissão sináptica fisiológica — é considerada a base da sua tolerabilidade clínica.

A conexão mecanicista com a hipertensão pulmonar ainda é especulativa. Evidências pré-clínicas emergentes sugerem que receptores NMDA funcionais estão expressos em células do músculo liso arterial pulmonar e podem participar da regulação da remodelação vascular e da proliferação celular. O eixo glutamato/NMDAR foi associado à hipertensão arterial pulmonar (HAP) em modelos animais e celulares, incluindo vias de estresse oxidativo e angiogênese patológica. Contudo, não há demonstração direta desse mecanismo em pacientes humanos com HAP.

Um dado que merece atenção é o desenvolvimento clínico do MN-08 — um derivado nitrato da memantina criado especificamente para hipertensão arterial pulmonar —, atualmente em Fase 1. Isso indica que a comunidade científica reconhece potencial terapêutico no scaffold molecular da memantina para esta indicação, ainda que a memantina em si não tenha sido testada diretamente em ensaios clínicos para HAP. A alta pontuação TxGNN provavelmente reflete conexões no grafo de conhecimento via nós patobiológicos compartilhados (proliferação vascular, estresse oxidativo), em vez de uma relação farmacológica diretamente comprovada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Ciência Básica | *Theranostics* | O eixo glutamato/NMDAR está implicado em lesão pulmonar aguda e hipertensão arterial pulmonar; estudo em modelos animal e celular demonstra papel do NMDAR na regulação metabólica lipídica e na resistência à insulina com relevância para a fisiopatologia pulmonar |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Estudo de Fase 1 (PK) | *Clinical Drug Investigation* | MN-08, derivado nitrato da memantina desenvolvido para HAP, avaliado em voluntários chineses saudáveis; dados de segurança, tolerabilidade e farmacocinética após dose única e múltipla ascendente — sugere viabilidade do scaffold da memantina para esta indicação |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para hipertensão pulmonar apresenta nível de evidência L5 — apenas dois estudos de ciência básica/fase 1, sem ensaios clínicos randomizados ou estudos observacionais robustos em humanos para a memantina nesta indicação. O mecanismo proposto é biologicamente plausível, mas não está diretamente comprovado; a ausência de registro no Brasil adiciona uma barreira regulatória adicional.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos direcionados avaliando o efeito da memantina em modelos estabelecidos de hipertensão pulmonar (ex.: MCT-rat, SuHx)
- Monitoramento dos resultados dos estudos de Fase 1/2 com MN-08 (derivado direto da memantina para HAP)
- Caracterização da densidade e função dos receptores NMDA em células do músculo liso vascular pulmonar humano
- Levantamento de dados completos de MOA e segurança via DrugBank para análise de interações com vasodilatadores usados em HAP (ex.: sildenafila, bosentana)
- Avaliação de viabilidade regulatória no Brasil (ANVISA), considerando que o medicamento não possui nenhum registro ativo no país
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

