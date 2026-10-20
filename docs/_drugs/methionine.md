---
layout: default
title: Methionine
parent: Apenas Predição do Modelo (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Methionine: nova indicação prevista, Acne (acne disease) (nível de evidência L5). Indicação original: Outros produtos para o aparelho digestivo e metabolismo"
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "nuclear senile cataract", "cortical cataract", "craniostenosis cataract", "tetanic cataract", "immature cataract", "mature cataract", "diabetic cataract"]
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

# Metionina: Do suporte nutricional à acne

## Resumo em Uma Frase

A metionina é um aminoácido essencial, usado no Brasil principalmente em soluções de nutrição parenteral e em produtos metabólicos e vitamínicos.
O modelo TxGNN prevê que pode ser eficaz para **acne (acne disease)**, mas até o momento há **0 ensaios clínicos** e apenas **2 publicações** de relevância muito limitada, nenhuma delas testando a metionina como tratamento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho digestivo e metabolismo |
| Nova Indicação Prevista | Acne (acne disease) |
| Pontuação de Previsão TxGNN | 99,9996% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a metionina é um aminoácido essencial que participa do metabolismo da homocisteína e de um carbono (via de metilação). No Brasil, ela aparece como componente de soluções de nutrição parenteral e de produtos metabólicos e vitamínicos.

A relação entre a indicação original (suporte nutricional e metabólico) e a acne é fraca. A pontuação do modelo é muito alta, mas não há respaldo mecanístico direto. A única literatura ligeiramente relacionada mostra **aumento da homocisteína em pacientes tratados com isotretinoína** para acne cística, ou seja, um efeito metabólico adverso do tratamento, e não evidência de que a metionina trate a acne. O outro artigo trata de uma mutação do gene MTHFR em um recém-nascido com encefalopatia, sem relação com o tratamento da acne.

Assim, a previsão deve ser vista como uma hipótese gerada por computador, ainda sem validação biológica ou clínica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Coorte | Int J Dermatol | Níveis elevados de homocisteína plasmática em pacientes em uso de isotretinoína para acne cística; não avalia a metionina como tratamento |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Relato de caso | BMJ Case Reports | Mutação nova do MTHFR em recém-nascido com encefalopatia, queda de cabelo e acne neonatal; sem relação terapêutica com a acne |

## Informações de Comercialização no Brasil

Todos os 20 registros encontrados estão **cancelados**. Principais exemplos:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 196240004 | FIGZ | — | Outros produtos para o aparelho digestivo e metabolismo |
| Registro nº 178170079 | EPOCLER | — | Outros produtos para o aparelho digestivo e metabolismo |
| Registro nº 102980493 | REGENCEL | — | Outros medicamentos com ação no aparelho visual |
| Registro nº 100410131 | NEPHROTECT | — | Nutrientes parenterais |
| Registro nº 106830181 | OLIMEL | — | Reposição hidroeletrolítica e alimentação parenteral |

## Considerações de Segurança

- **Contraindicações (base de conhecimento TxGNN/PrimeKG, não extraídas de bula):** hipertensão, doença renal (incluindo doença renal crônica e insuficiência renal terminal), nefrolitíase, nefrocalcinose, hipercalcemia, sarcoidose, diabetes mellitus e cetoacidose diabética, doença cardíaca e cardiovascular, hiperlipidemia (incluindo familiar), nefropatia aguda por urato, intoxicação digitálica, fibrilação ventricular, fenilcetonúria e outros distúrbios do metabolismo da fenilalanina, entre outras.
- **Interações Medicamentosas (5 identificadas):**
  - **Moderada:** carvão ativado.
  - **Menores:** efedrina, pseudoefedrina, mexiletina e flecainida.
- **Observação:** a suplementação de metionina pode elevar a homocisteína, o que é preocupante em pacientes cardiovasculares e é um risco teórico no contexto da acne.

Consulte a bula para as advertências oficiais, pois os dados de advertências e contraindicações da ANVISA não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem evidência mecanística direta de que a metionina trate a acne; a previsão é apenas computacional (L5). Além disso, todos os registros brasileiros estão cancelados e há uma lista extensa de contraindicações potenciais.

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação (por exemplo, via DrugBank) e avaliar a plausibilidade biológica na acne.
- Obter e analisar as bulas na ANVISA (advertências e contraindicações).
- Realizar estudos pré-clínicos que testem diretamente a metionina na acne e avaliem o efeito sobre a homocisteína.
- Avaliar a situação regulatória, já que não há registro vigente no Brasil.

---

**Observação sobre outras indicações previstas:** as demais indicações do modelo (retinopatia diabética não proliferativa grave e vários tipos de catarata) também estão em nível L5, com decisão *Hold*. A **catarata diabética** é a que tem evidência indireta mais relevante (nível L4, "pergunta de pesquisa"), envolvendo a metionina sulfóxido redutase B1 e a proteção contra o estresse oxidativo no cristalino. Mesmo assim, esses dados mostram o envolvimento da via e não o benefício da administração de metionina, que poderia até elevar a homocisteína. Esse é um possível caminho para investigação futura.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

