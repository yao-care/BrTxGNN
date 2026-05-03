---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Glicina: De suplemento aminoácido à doença da cavidade nasal

## Resumo em Uma Frase

Glicina (Glycine) é um aminoácido não essencial amplamente utilizado como suplemento nutricional e veículo farmacêutico em procedimentos cirúrgicos.
O modelo TxGNN prevê que pode ser eficaz para **Doença da Cavidade Nasal (Nasal Cavity Disease)**,
porém atualmente conta com apenas **1 ensaio clínico de relevância marginal** e **2 publicações científicas periféricas** apoiando esta direção, situando-se no nível de evidência mais baixo (L5).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação terapêutica registrada (uso como suplemento/veículo) |
| Nova Indicação Prevista | Doença da Cavidade Nasal (Nasal Cavity Disease) |
| Pontuação de Previsão TxGNN | 99,85% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimento farmacológico consolidado, a glicina é um aminoácido inibitório do sistema nervoso central e periférico, capaz de ativar canais de cloreto com portão de glicina (GlyR) em macrófagos e células imunes. Essa ativação promove hiperpolarização celular e reduz a liberação de citocinas pró-inflamatórias como IL-1β e TNF-α.

A hipótese mecanística para a doença da cavidade nasal baseia-se em três vias: (1) inibição da infiltração de neutrófilos e redução da liberação de espécies reativas de oxigênio (ROS) na mucosa nasal; (2) supressão da via NF-κB, reduzindo a inflamação crônica da mucosa; e (3) potencial antioxidante como precursor da glutationa. Adicionalmente, a glicina é o aminoácido mais abundante do colágeno, podendo contribuir para a reparação tecidual da mucosa.

Contudo, é importante ressaltar que todas essas vias mecanísticas permanecem no nível teórico ou pré-clínico. Não há estudos específicos em humanos com glicina para doença da cavidade nasal, e os dados de suporte disponíveis são indiretos e periféricos à hipótese central.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Concluído | 25 | Avaliação do radiofármaco 18F-FPPRGD2 (contendo sequência RGD com resíduo de glicina) para detecção de angiogênese tumoral em glioblastoma, cânceres ginecológicos e carcinoma renal. Relevância para glicina em doença nasal: mínima (Grau C) — o estudo testa um agente de imagem PET, não glicina como terapêutico. |

> **Nota**: O único ensaio recuperado avalia a glicina como componente estrutural de um agente de imagem (peptídeo RGD), não como fármaco isolado para doença da cavidade nasal. A doença nasal não é uma das indicações-alvo do ensaio.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Animal/Basic Science | Veterinary Pathology | Análise histoquímica de lectinas na mucosa nasal bovina normal e infectada por herpesvírus bovino-1 (BHV1), investigando a composição de glicoconjugados. Relevância indireta — estudo em bovinos sobre glicoconjugados da mucosa nasal, sem envolvimento direto da glicina como agente terapêutico. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | In Vitro / Formulation Science | Chemical & Pharmaceutical Bulletin | Estudo de oligoargininas conjugadas a polímeros biocompatíveis como adjuvante mucosal nasal para indução de IgA e IgG. Relevância indireta — foca em oligoargininas (não glicina) na via nasal; a conexão com glicina é estrutural/molecular, não farmacológica. |

---

## Informações de Comercialização no Brasil

Há **20 registros** de glicina na base regulatória brasileira com situação **comercializado**. No entanto, os dados detalhados de cada produto (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estavam disponíveis no Evidence Pack fornecido.

> Para consulta dos registros individuais, acesse o portal da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis são insuficientes para sustentar o reposicionamento da glicina para doença da cavidade nasal — o único ensaio clínico recuperado é irrelevante à hipótese (Grau C), e as duas publicações são estudos animais/in vitro sem conexão direta com a glicina como terapêutico nasal. A previsão do TxGNN, embora com pontuação alta (99,85%), não é corroborada por evidências clínicas ou pré-clínicas específicas, situando-se em nível L5.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) validados via DrugBank ou literatura primária
- Busca direcionada por estudos pré-clínicos de glicina em modelos de inflamação de mucosa nasal (rinite, sinusite, pólipos nasais)
- Identificação de ensaios clínicos que utilizem glicina como agente terapêutico ativo (não apenas como veículo ou componente estrutural)
- Download e análise das bulas registradas na ANVISA para avaliar advertências e contraindicações (Data Gap DG001 — bloqueante)
- Verificação de interações medicamentosas em bases especializadas (Drugs.com, DrugBank DDI module)
- Avaliação da plausibilidade da via de administração (oral vs. tópica nasal) para que a glicina atinja a mucosa nasal em concentrações terapêuticas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

