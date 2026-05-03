---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

Usando o skill **txgnn-pipeline** para verificar o contexto do projeto, e agora gerando o relatório a partir do Evidence Pack fornecido.

---

# Rasburicase: Da Hiperuricemia à Hipouricemia Renal

## Resumo em Uma Frase

Rasburicase é uma urato oxidase recombinante aprovada para redução rápida do ácido úrico elevado em pacientes oncológicos sob risco de síndrome de lise tumoral (SLT). O modelo TxGNN prevê que pode ser eficaz para **Hipouricemia Renal (hypouricemia, renal)** — contudo, esta previsão apresenta uma **contradição de direção farmacológica crítica**: a hipouricemia renal caracteriza-se por ácido úrico já anormalmente baixo, e rasburicase reduziria ainda mais esse nível, agravando a condição. Atualmente, há **0 ensaios clínicos** e **0 publicações** apoiando esta direção, e a previsão é classificada como **potencial falso positivo do modelo**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hiperuricemia associada à síndrome de lise tumoral em pacientes oncológicos |
| Nova Indicação Prevista | Hipouricemia Renal (hypouricemia, renal) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Rasburicase (DB00049) é uma urato oxidase recombinante que catalisa a conversão do ácido úrico em alantoína — um metabólito mais solúvel e prontamente excretado pelos rins. Esta via enzimática está naturalmente ausente em humanos (o gene UOX é um pseudogene silenciado), razão pela qual rasburicase oferece uma redução de ácido úrico extraordinariamente rápida e potente, sendo especialmente útil no contexto de síndrome de lise tumoral em leucemias, linfomas e tumores sólidos sob quimioterapia intensa.

A hipouricemia renal (hypouricemia, renal), por outro lado, é causada por defeito nos transportadores tubulares renais de urato — principalmente URAT1 (*SLC22A12*) e GLUT9 (*SLC2A9*) — resultando em reabsorção insuficiente de urato e excreção excessiva. O quadro clínico é de ácido úrico sérico cronicamente baixo (geralmente < 2 mg/dL), com risco de nefropatia por exercício e urolitíase de urato de amônio.

A conexão mecanística é **inversa e clinicamente prejudicial**: aplicar um fármaco que reduz ativamente o urato sérico em uma condição cujo problema central é justamente o urato sérico já insuficiente representa uma contradição terapêutica fundamental. O alto score TxGNN (99,99%) provavelmente reflete a proximidade topológica entre os nós "metabolismo de purinas" e "transportadores renais de urato" no grafo de conhecimento, sem que o modelo avalie a **direção do desequilíbrio** ou o sentido do efeito farmacológico. Esta previsão deve ser tratada como falso positivo de modelo (model artifact por inversão de direção).

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Rasburicase está registrado no Brasil com **3 licenças ativas** confirmadas na base ANVISA. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e texto de indicação aprovada) não constam nos dados estruturados disponíveis neste Evidence Pack. Recomenda-se consultar diretamente o sistema de Consulta de Medicamentos da ANVISA para obter as informações completas dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão de rank 1 (hipouricemia renal) é um **falso positivo do modelo TxGNN por inversão de direção terapêutica** — rasburicase reduz ácido úrico, e a hipouricemia renal já apresenta ácido úrico insuficiente; não existe qualquer evidência clínica ou pré-clínica que suporte esta direção, e o uso do fármaco seria clinicamente contraindicado nesta indicação.

> **Nota sobre a indicação de rank 2:** A segunda previsão — **Deficiência Parcial de HGPRT** (síndrome de Kelley-Seegmiller, score 99,97%) — apresenta lógica mecanística válida e oposta: pacientes com deficiência parcial de hipoxantina-guanina fosforribosiltransferase produzem ácido úrico em excesso, e rasburicase poderia oferecer redução aguda de urato neste contexto. Esta indicação foi classificada como "Research Question" e merece avaliação separada antes de ser descartada.

**Para prosseguir com qualquer nova indicação de rasburicase, é necessário:**
- Obter texto completo das advertências e contraindicações da bula ANVISA (dado bloqueante — DG001)
- Obter dados de mecanismo de ação detalhados do DrugBank (DG002)
- Realizar revisão bibliográfica manual para indicações com lógica mecanística positiva, especialmente **deficiência parcial de HGPRT** (rank 2)
- Recuperar os detalhes estruturados dos 3 registros ANVISA ativos (número, nome comercial, indicações aprovadas)
- Avaliar se o perfil de segurança (incluindo risco de hemólise em deficiência de G6PD — contraindicação clássica de rasburicase) é compatível com as populações-alvo das novas indicações
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

