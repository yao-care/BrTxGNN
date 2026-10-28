---
layout: default
title: Methionine
parent: Apenas Predição do Modelo (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
last_modified_at: 2026-10-28
description: "Methionine: nova indicação prevista, Acne (doença) (nível de evidência L5). Indicação original: Outros produtos para o aparelho digestivo e metabolismo"
---

# Methionine
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

## Metionina: De produtos para o aparelho digestivo e metabolismo e nutrição parenteral para acne (doença)
{: .text-alpha }

## Resumo em Uma Frase

A metionina é um aminoácido essencial, usado no Brasil em produtos para o aparelho digestivo e metabolismo, em soluções de nutrição parenteral e em associações vitamínicas.
O modelo TxGNN prevê relação com **acne (doença)**, mas sem nenhum ensaio clínico e com apenas **2 publicações** indiretas, que não mostram que a metionina trate acne.
O nível de evidência é **L5**: trata-se, na prática, apenas de uma previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho digestivo e metabolismo |
| Nova Indicação Prevista | Acne (doença) |
| Pontuação de Previsão TxGNN | 1,0000 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | Pelo menos 20 (a lista pode estar incompleta) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a metionina é um aminoácido sulfurado essencial, presente em soluções de nutrição parenteral e em produtos metabólicos, e participa do metabolismo de um carbono e da via da homocisteína.

A relação com a acne é fraca. A única publicação que toca o tema mostra níveis elevados de homocisteína (metabólito da metionina) em pacientes tratados com isotretinoína para acne cística, o que descreve um efeito colateral do tratamento, não um benefício da metionina. A outra publicação trata de um caso de mutação em *MTHFR* com encefalopatia neonatal, sem relação terapêutica com a acne.

Não há mecanismo terapêutico plausível estabelecido. A pontuação alta do TxGNN, isolada, não basta para sustentar a hipótese.

Entre as demais indicações previstas, a mais coerente do ponto de vista indireto é a **catarata diabética** (nível L4). Nesse caso, a metionina sulfóxido redutase B1 (MsrB1) protege células epiteliais do cristalino humano contra apoptose induzida por glicose alta e por peroxinitrito. Nenhum estudo, porém, testou a metionina como tratamento. Essa hipótese é tratada como pergunta de pesquisa, não como indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Coorte | Int J Dermatol | Homocisteína plasmática elevada em pacientes em uso de isotretinoína para acne cística |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Relato de caso | BMJ Case Reports | Mutação nova em *MTHFR* com encefalopatia neonatal, queda de cabelo e acne neonatal; sem relação terapêutica com a metionina |

---

## Informações de Comercialização no Brasil

Foram listados 20 registros válidos, todos de medicamentos de ingrediente único, e a lista pode estar incompleta. Abaixo, os 5 principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 196240004 | FIGZ | — | Outros produtos para o aparelho digestivo e metabolismo |
| Registro 178170079 | EPOCLER | — | Outros produtos para o aparelho digestivo e metabolismo |
| Registro 102980493 | REGENCEL | — | Outros medicamentos com ação no aparelho visual |
| Registro 100410131 | NEPHROTECT | — | Nutrientes parenterais |
| Registro 167730285 | NATUS GERIN | — | Vitaminas ou minerais associados a outros fármacos |

---

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não são texto de bula): hipertensão, doença renal (incluindo doença renal crônica e insuficiência renal terminal), diabetes mellitus e cetoacidose diabética, hipercalcemia, nefrocalcinose, nefrolitíase, doença cardíaca e cardiovascular, hiperlipidemia (incluindo a familiar), fenilcetonúria e distúrbios do metabolismo da fenilalanina, sarcoidose, intoxicação digitálica e fibrilação ventricular.
- **Interações medicamentosas** (5 registradas):
  - Moderada: carvão ativado.
  - Leves: efedrina, pseudoefedrina, mexiletina e flecainida.
- **Risco teórico:** a metionina em excesso pode elevar a homocisteína, o que é relevante para o risco vascular.

Consulte a bula para advertências e contraindicações oficiais, pois os dados de bula não estavam disponíveis.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos e as duas publicações sobre acne são indiretas, sem apoio a um efeito terapêutico da metionina; por isso o nível é L5. A acne não deve avançar como candidata de reposicionamento com os dados atuais.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), uma lacuna que impede a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank.
- Para acne: reunir evidência pré-clínica ou clínica que mostre algum efeito da metionina, o que hoje não existe.
- Para a linha alternativa da catarata diabética: realizar testes pré-clínicos (células epiteliais de cristalino em glicose alta ou modelo em roedor diabético), com monitoramento de homocisteína.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

