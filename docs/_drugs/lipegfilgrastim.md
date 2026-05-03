---
layout: default
title: Lipegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Usando o skill `txgnn-pipeline` como referência de contexto do projeto. Agora gero o relatório com base no Evidence Pack fornecido.

---

# Lipegfilgrastim: Da neutropenia por quimioterapia ao distúrbio primário de liberação plaquetária

## Resumo em Uma Frase

Lipegfilgrastim é um G-CSF (fator estimulante de colônias de granulócitos) de longa ação, indicado para reduzir a duração da neutropenia grave em pacientes oncológicos submetidos à quimioterapia citotóxica.
O modelo TxGNN prevê que pode ser eficaz para **Distúrbio Primário de Liberação Plaquetária (Primary Release Disorder of Platelets)**, com pontuação de **99,93%** — porém atualmente **não há ensaios clínicos nem publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Neutropenia grave em pacientes com tumores não mieloides submetidos à quimioterapia citotóxica |
| Nova Indicação Prevista | Distúrbio Primário de Liberação Plaquetária (Primary Release Disorder of Platelets) |
| Pontuação de Previsão TxGNN | 99,93% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento consolidado, lipegfilgrastim é um G-CSF glicosilado e pegilado (derivado de filgrastim), cujo mecanismo primário consiste na ligação ao receptor de G-CSF (G-CSFR) em precursores hematopoéticos da medula óssea. Esse estímulo acelera a produção, maturação e liberação de neutrófilos para a corrente sanguínea, sendo por isso o padrão de cuidado na prevenção de neutropenia febril induzida por quimioterapia.

A previsão do TxGNN baseia-se na observação de que receptores de G-CSF também estão presentes em megacariócitos (precursores das plaquetas), e que o estímulo por G-CSF pode, de forma indireta, promover a trombocitopoese — gerando, em teoria, alguma plausibilidade biológica superficial. É esse elo que provavelmente levou o modelo a atribuir alta pontuação a doenças plaquetárias como grupo.

Contudo, a relação mecanística é fraca e indireta. O distúrbio primário de liberação plaquetária é caracterizado por defeitos na secreção de grânulos plaquetários (grânulos δ ou α), ou seja, é uma disfunção **qualitativa** — e não um problema de quantidade insuficiente de plaquetas. Elevar o número de plaquetas via G-CSF não corrige um defeito funcional de secreção. A alta pontuação do TxGNN é melhor explicada pela proximidade topológica entre os nós de neutrófilos e plaquetas na via hematopoética compartilhada do grafo de conhecimento, e não por uma relação biológica real com esta indicação específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Há **1 registro** de lipegfilgrastim no Brasil (situação: comercializado), porém os detalhes do registro — número, nome comercial, forma farmacêutica e texto de indicação aprovada — não constam nos dados fornecidos neste Evidence Pack. Para informações completas, consulte diretamente o portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão situa-se em nível L5 (apenas saída do modelo, sem qualquer estudo humano de suporte), e a análise mecanística indica que G-CSF não atua sobre o defeito de secreção de grânulos que define o distúrbio primário de liberação plaquetária — tornando a relevância biológica desta indicação improvável no estado atual do conhecimento.

**Para prosseguir, é necessário:**
- Obter a bula completa (ANVISA) e preencher as lacunas de segurança: advertências, contraindicações e dados de farmacovigilância
- Confirmar o mecanismo de ação detalhado (MOA) via DrugBank API (DG002)
- Conduzir revisão sistemática da literatura sobre G-CSF/filgrastim e disfunções qualitativas de plaquetas (grânulos δ/α)
- Avaliar se estudos pré-clínicos com modelos de disfunção de grânulos plaquetários são viáveis antes de qualquer avanço clínico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

