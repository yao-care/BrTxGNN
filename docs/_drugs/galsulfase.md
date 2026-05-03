---
layout: default
title: Galsulfase
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Galsulfase
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

# Galsulfase: Da Mucopolissacaridose Tipo VI à Síndrome de Ptose-Estrabismo-Pupilas Ectópicas

## Resumo em Uma Frase

Galsulfase (Naglazyme®) é uma terapia de reposição enzimática (TRE) aprovada para o tratamento da Mucopolissacaridose Tipo VI (MPS VI, síndrome de Maroteaux-Lamy), condição em que a deficiência da enzima arilsulfatase B (ARSB) causa acúmulo progressivo de dermatan sulfato nos tecidos.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Ptose-Estrabismo-Pupilas Ectópicas (Ptosis-Strabismus-Ectopic Pupils Syndrome)**, porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mucopolissacaridose Tipo VI (MPS VI / Síndrome de Maroteaux-Lamy) |
| Nova Indicação Prevista | Síndrome de Ptose-Estrabismo-Pupilas Ectópicas |
| Pontuação de Previsão TxGNN | 97,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base em informações conhecidas, Galsulfase é uma forma recombinante da enzima arilsulfatase B (ARSB), que catalisa a degradação do dermatan sulfato dentro dos lisossomos. Na MPS VI, a deficiência hereditária de ARSB leva ao acúmulo deste glicosaminoglicano (GAG) em múltiplos tecidos, causando manifestações progressivas nos ossos, coração, pulmões e **olhos** — incluindo opacidade de córnea, glaucoma e retinopatia.

A síndrome de ptose-estrabismo-pupilas ectópicas é uma anomalia congênita neuromuscular e estrutural dos olhos, sem qualquer patologia documentada de acúmulo de GAG. Não existe relação enzima-substrato entre a ARSB e os mecanismos que causam esta síndrome congênita. A pontuação elevada do modelo (97,89%) reflete provavelmente a **proximidade topológica dos nós de doenças oculares raras no grafo de conhecimento** utilizado pelo TxGNN — pacientes com MPS VI têm manifestações oftalmológicas, o que cria vizinhança no grafo —, e não uma conexão mecanicista real.

Em resumo: a previsão é um artefato de topologia de grafo. A síndrome alvo é de origem congênita e estrutural, não relacionada à deficiência de ARSB, tornando a aplicação de Galsulfase mecanisticamente não fundamentada para esta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Galsulfase possui **1 registro ativo** no Brasil. Os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis nos dados atuais do Evidence Pack.

> Para consulta completa ao registro ANVISA, acesse: [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para esta indicação é classificada como L5 (apenas predição do modelo, sem estudos reais), e a análise mecanicista indica que a síndrome alvo é uma anomalia congênita estrutural sem relação etiológica com o acúmulo de dermatan sulfato que Galsulfase trata. Não há base clínica nem biológica para prosseguir com esta indicação.

**Para prosseguir com avaliações futuras, é necessário:**
- Obter informações completas de segurança (advertências, contraindicações, reações adversas) via download e análise da bula ANVISA
- Detalhar o mecanismo de ação (MOA) via consulta à API do DrugBank (DB01279)
- Completar os detalhes do registro ANVISA (número de registro, nome comercial, forma farmacêutica, indicação aprovada)
- Priorizar a reavaliação da indicação de **Rank 10 — Síndrome de Scheie (MPS I-S)**, que apresenta conexão biológica mais plausível (ambas as condições envolvem acúmulo de dermatan sulfate) e conta com 4 publicações de suporte; embora a distinção enzimática entre IDUA (MPS I) e ARSB (MPS VI) impeça substituição direta, o tema merece análise aprofundada
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

