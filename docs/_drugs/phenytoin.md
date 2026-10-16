---
layout: default
title: Phenytoin
parent: Apenas Predição do Modelo (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phenytoin: nova indicação prevista, Neoplasia do nervo trigêmeo (trigeminal nerve neoplasm) (nível de evidência L5). Indicação original: Anticonvulsivantes"
---

# Phenytoin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Fenitoína: Do anticonvulsivante à neoplasia do nervo trigêmeo (previsão do modelo)

## Resumo em Uma Frase

A fenitoína (phenytoin) é um anticonvulsivante, registrado no Brasil na classe dos "anticonvulsivantes".
O modelo TxGNN prevê, com maior pontuação, que ela poderia ser eficaz para **neoplasia do nervo trigêmeo (trigeminal nerve neoplasm)**, mas **não há ensaios clínicos** e as 2 publicações recuperadas tratam de neuralgia do trigêmeo e síndrome de Sturge-Weber, não de tumores. A previsão é considerada um provável artefato do grafo de conhecimento. Entre as demais previsões, a **neuralgia do trigêmeo** é a mais bem sustentada (literatura clínica, sem ensaios registrados).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Neoplasia do nervo trigêmeo (trigeminal nerve neoplasm) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 12 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a fenitoína bloqueia canais de sódio dependentes de voltagem, o que explica sua ação anticonvulsivante e seu uso em dor neuropática.

Para a indicação de maior pontuação, **neoplasia do nervo trigêmeo**, não há vínculo mecanístico crível. A fenitoína não tem atividade antineoplásica conhecida contra tumores nervosos. A pontuação alta parece decorrer da proximidade no grafo com o nó vizinho "neuralgia do trigêmeo". Por isso, a previsão não é considerada razoável como reposicionamento oncológico.

As previsões seguintes são, na prática, extensões dentro da classe antiepiléptica (crises reflexas: miccionais, audiogênicas, por alimentação, por sobressalto, por leitura etc.), com evidência majoritariamente pré-clínica ou de relatos de caso. A **neuralgia do trigêmeo** (pontuação 99,97%, nível L3) é a mais plausível: o bloqueio de sódio reduz a descarga ectópica de alta frequência nas aferências trigeminais, mesmo mecanismo da carbamazepina. A fenitoína seria opção de segunda linha ou de resgate intravenoso agudo; carbamazepina e oxcarbazepina continuam como primeira linha.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisão | Expert Rev Neurother | Panorama dos tratamentos clínicos e cirúrgicos da neuralgia do trigêmeo; não trata de neoplasia |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Série de casos | An Esp Pediatr | Experiência com 14 casos de síndrome de Sturge-Weber; não trata de neoplasia do trigêmeo |

Para a neuralgia do trigêmeo (indicação alternativa, não a de maior pontuação), a literatura recuperada inclui a diretriz da Academia Europeia de Neurologia (2019), uma análise retrospectiva de 144 casos de lacosamida e fenitoína intravenosas em exacerbações agudas (2022), uma coorte retrospectiva de fenitoína IV como resgate (2020) e uma revisão crítica (2017) que sugere evidência fraca para a fenitoína em comparação com a carbamazepina.

## Informações de Comercialização no Brasil

Todos os 12 registros estão cancelados; não há registro válido. Principais registros (máximo de 5):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 110390036 | FURP - Fenitoína | Não informada | Anticonvulsivantes (cancelado) |
| Registro 103700473 | Fenitoína | Não informada | Anticonvulsivantes (cancelado) |
| Registro 107150171 | Fenitoína | Não informada | Anticonvulsivantes (cancelado) |
| Registro 112090023 | FUNED - Fenitoína | Não informada | Anticonvulsivantes (cancelado) |
| Registro 107150095 | Dantalin | Não informada | Anticonvulsivantes (cancelado) |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: o grafo associa a fenitoína a contraindicações em síndrome do QT longo e torsades de pointes, insuficiência e doença hepática, encefalopatia hepática, porfiria, doença renal, doença da vesícula biliar, trombocitopenia, neutropenia e agranulocitose, hiperglicemia, diabetes e cetoacidose diabética, lúpus eritematoso sistêmico, hipotensão, apneia do sono, transtornos de ansiedade e dependência de substâncias.
- **Interações Medicamentosas**: 100 interações listadas; as principais retornadas são de nível moderado, com acarbose, famotidina, ranitidina, doxiciclina, hidrocortisona, dexametasona, betametasona, triamcinolona, metformina, pioglitazona, alogliptina, albiglutida, bupropiona, aprepitanto, morfina, omeprazol, metronidazol, colecalciferol e calcifediol. Interação com ácido acetilsalicílico é de nível leve.
- **Pontos da literatura**: casos de trombocitopenia, hiperglicemia/cetoacidose, crises de porfiria, reações cutâneas graves associadas à radioterapia craniana (síndrome EMPACT), hiperplasia gengival e neuropatia periférica. A fenitoína tem índice terapêutico estreito e farmacocinética não linear.

Para as demais advertências, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A indicação de maior pontuação (neoplasia do nervo trigêmeo) tem apenas previsão do modelo (L5), sem ensaios, sem literatura pertinente e sem vínculo mecanístico. Além disso, todos os registros brasileiros estão cancelados. A neuralgia do trigêmeo (L3, "Proceed with Guardrails" na avaliação individual) é a direção mais viável, mas como terapia de segunda linha ou resgate.

**Para prosseguir, é necessário:**
- Obter da bula da ANVISA as advertências e contraindicações oficiais (lacuna de dados bloqueante para a triagem de segurança).
- Complementar os dados de mecanismo de ação.
- Se houver interesse, redirecionar a avaliação para neuralgia do trigêmeo, com revisão sistemática da evidência de fenitoína versus carbamazepina/oxcarbazepina e eventual ensaio de resgate IV.
- Verificar a situação regulatória atual no Brasil, já que não há registro válido, e planejar monitoramento de níveis séricos e de interações medicamentosas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

