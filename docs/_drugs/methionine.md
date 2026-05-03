---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Methionine
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

Usando o skill `txgnn-pipeline` como guia contextual. Agora vou analisar o Evidence Pack e gerar o relatório completo.

---

# Methionine: Do aminoácido essencial à acne

## Resumo em Uma Frase

Methionine (L-metionina, DB00134) é um aminoácido essencial com funções centrais no metabolismo celular, incluindo síntese proteica, metilação e produção de glutationa.
O modelo TxGNN prevê que pode ser eficaz para **Acne (Acne disease)**, porém esta direção conta apenas com **0 ensaios clínicos** e **4 publicações** de suporte — todas com conexão indireta ao mecanismo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Suplemento de aminoácido essencial (sem registro no Brasil) |
| Nova Indicação Prevista | Acne (Acne disease) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Segundo informações conhecidas, a Methionine é um aminoácido essencial que atua como ponto de partida do **ciclo da metionina**: é convertida em S-adenosilmetionina (SAM, o principal doador de grupos metil do organismo), e posteriormente em homocisteína, cisteína e glutationa (GSH). Esses metabólitos participam de processos críticos como metilação do DNA, síntese de proteínas e defesa antioxidante.

A conexão com a acne é **indireta**: a isotretinoína, retinóide de primeira linha para acne cística severa, demonstrou elevar significativamente os níveis plasmáticos de homocisteína em pacientes tratados (PMID 11277950). Esse fenômeno sugere que o tratamento da acne com isotretinoína pode perturbar o ciclo da metionina como efeito colateral — mas **não implica** que a suplementação de metionina tenha ação terapêutica direta sobre a acne.

Um relato de caso de 2024 (PMID 39357918) documenta um neonato com mutação no gene MTHFR (enzima essencial para o remetilação da homocisteína de volta à metionina) que apresentou, entre outras manifestações, acne neonatal — reforçando a plausibilidade de uma ligação entre disfunção do ciclo da metionina e alterações cutâneas, mas no contexto de doença genética rara, não de indicação terapêutica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case Report | BMJ Case Reports | Mutação MTHFR neonatal com encefalopatia severa; acne neonatal presente como manifestação cutânea associada à disfunção do ciclo da metionina |
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Observacional/Transversal | Int J Dermatology | Isotretinoína para acne cística eleva homocisteína plasmática, indicando perturbação do metabolismo da metionina como efeito adverso — não como mecanismo terapêutico da metionina em si |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Relato de Caso | J Am Acad Dermatology | Função neutrofílica em paciente com Síndrome de Sweet e acne cistonodular; isotretinoína reduziu quimiotaxia, sem relação direta com metionina |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Ciência Básica | J Invest Dermatology | Avaliação da função de neutrófilos (C5a) em 135 pacientes com doenças inflamatórias cutâneas incluindo acne conglobata; sem relação com metionina |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As quatro publicações identificadas apresentam conexão apenas indireta — a metionina aparece como metabólito perturbado por outros fármacos ou em condições genéticas raras, e não como agente terapêutico ativo contra acne. Não existem ensaios clínicos registrados, nenhuma plausibilidade mecanística direta foi demonstrada, e o produto não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA via DrugBank API (DG002 bloqueante)
- Investigar se a suplementação oral de metionina modula inflamação sebácea ou microbioma cutâneo em modelos pré-clínicos de acne
- Avaliar se a restauração do ciclo da metionina (via SAM ou GSH) tem relevância clínica na fisiopatologia da acne inflamatória
- Considerar indicações com evidência mais robusta neste mesmo pack (ex.: **Diabetic Cataract**, rank 10, nível L4 com múltiplos estudos em células humanas e suporte mecanístico via MsrB1/SAM sintase) como prioridade para desenvolvimento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

