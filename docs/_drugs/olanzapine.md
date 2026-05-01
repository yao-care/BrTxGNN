---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

O skill `txgnn-pipeline` é sobre gestão de pipeline/infraestrutura e não se sobrepõe ao formato de relatório já definido no sistema. Procedendo diretamente à geração do relatório com base no Evidence Pack fornecido.

---

# Olanzapine: Da Esquizofrenia à Torticolose Paroxística Benigna da Infância

## Resumo em Uma Frase

Olanzapine é um antipsicótico atípico da classe tienobenzodiazepínica, originalmente utilizado no tratamento de esquizofrenia e transtorno bipolar, por meio do bloqueio simultâneo de receptores D2 e 5-HT2A.
O modelo TxGNN prevê que pode ser eficaz para **Torticolose Paroxística Benigna da Infância (Benign Paroxysmal Torticollis of Infancy)**, porém esta indicação conta atualmente com **0 ensaios clínicos** e **nenhuma publicação** diretamente disponível — a previsão baseia-se exclusivamente em inferência topológica do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Esquizofrenia e transtorno bipolar (baseado em conhecimento geral; dados ANVISA não disponíveis na base atual) |
| Nova Indicação Prevista | Torticolose Paroxística Benigna da Infância (Benign Paroxysmal Torticollis of Infancy) |
| Pontuação de Previsão TxGNN | 99,54% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não Comercializado (0 registros encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis na base consultada. Com base no conhecimento estabelecido, olanzapine é um antipsicótico atípico cujo mecanismo primário envolve o antagonismo dos receptores dopaminérgicos D2 e serotoninérgicos 5-HT2A. Também bloqueia receptores histaminérgicos H1, muscarínicos M1–M5 e adrenérgicos alfa-1, conferindo-lhe um perfil farmacológico amplo relevante para diversas condições neuropsiquiátricas.

A Torticolose Paroxística Benigna da Infância (BPT) é considerada um equivalente migrânoso na infância, associada ao sistema vestibular e à via trigeminovascular. Em tese, o antagonismo D2/5-HT2A do olanzapine poderia modular a transmissão de sinais vestibulares relacionados à enxaqueca. No entanto, esta cadeia de raciocínio exige pelo menos três saltos de inferência indireta: (1) BPT como equivalente migrânoso → (2) envolvimento da via 5-HT2A → (3) efeito terapêutico do olanzapine na condição específica.

Mais criticamente, o uso de olanzapine em lactentes e crianças pequenas — a população-alvo desta indicação — representa uma preocupação de segurança de primeira ordem, incluindo risco de síndrome metabólica, prolongamento do intervalo QTc, sedação excessiva e possíveis impactos sobre o neurodesenvolvimento. A alta pontuação TxGNN (0,9954) reflete exclusivamente a posição topológica do fármaco no grafo de conhecimento, sem qualquer respaldo clínico direto nesta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Não foram encontrados registros de comercialização no Brasil na base de dados consultada (0 registros ANVISA).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para Torticolose Paroxística Benigna da Infância é de nível L5 — ausência total de ensaios clínicos e publicações identificadas. A fundamentação mecanística envolve múltiplas inferências indiretas não validadas, e o perfil de risco do olanzapine em lactentes representa um obstáculo crítico de segurança que inviabiliza qualquer avanço sem investigação prévia aprofundada.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) via DrugBank API (DG002)
- Obter advertências e contraindicações da bula (DG001) — item bloqueante para avaliação de segurança
- Ampliar busca sistemática na literatura de neurologia pediátrica e distúrbios vestibulares
- Consultar especialistas em neurologia pediátrica e cefaleia para avaliar a plausibilidade biológica
- Verificar status de comercialização real no Brasil junto à ANVISA diretamente
- Avaliar se indicações de nível L3–L4 presentes no mesmo Evidence Pack (Transtorno Distímico, Agorafobia) justificam priorização antes desta
---

