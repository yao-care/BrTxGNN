---
layout: default
title: Triptorelin
parent: Apenas Predição do Modelo (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Triptorelin: nova indicação prevista, Hipertricose (hypertrichosis) (nível de evidência L5). Indicação original: Outros produtos para o aparelho digestivo e metabolismo"
monitor_inn: "triptorelin"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "allergic urticaria", "familial male-limited precocious puberty", "precocious puberty", "familial isolated trichomegaly", "aromatase excess syndrome"]
---

# Triptorelin
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

# Triptorelina: De "outros produtos para o aparelho digestivo e metabolismo" para hipertricose

## Resumo em Uma Frase

A triptorelina é um agonista do hormônio liberador de gonadotrofinas (GnRH). No Brasil, seus registros constam apenas em categorias terapêuticas genéricas, como "outros produtos para o aparelho digestivo e metabolismo".
O modelo TxGNN prevê que ela possa ser eficaz para **Hipertricose (hypertrichosis)**, mas essa previsão tem **0 ensaios clínicos** e **1 publicação** que não apoia a direção: é um relato de caso sobre hipertricose induzida por ciclosporina, sem tratamento com triptorelina.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho digestivo e metabolismo (classe terapêutica constante no registro, não uma indicação clínica específica) |
| Nova Indicação Prevista | Hipertricose (hypertrichosis) |
| Pontuação de Previsão TxGNN | 99,997% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 3 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, a triptorelina é um agonista do GnRH. A estimulação contínua dessensibiliza os receptores de GnRH da hipófise, reduz o LH e o FSH e, com isso, os esteroides sexuais produzidos pelas gônadas.

**Esta previsão não tem respaldo mecanístico crível.** A supressão de esteroides sexuais não deveria tratar a hipertricose e pode até agir no sentido oposto sobre o crescimento de pelos. A pontuação alta do modelo (99,997%) provavelmente reflete proximidade na rede de conhecimento biomédico, e não uma relação terapêutica real. Outras doenças previstas com pontuações igualmente altas (por exemplo, hipertricose congênita de Ambras e anormalidades genéticas da haste capilar) também não têm lógica farmacológica plausível.

Observação: entre as demais previsões do modelo, a **puberdade precoce** (posição 8 da lista) tem evidência robusta, com vários ensaios de Fase 3 concluídos. É, porém, um uso já consolidado em diversas regiões, e portanto não é reposicionamento genuíno. Ela confirma que o modelo reconhece a farmacologia conhecida do fármaco, mas não altera a avaliação da hipertricose.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Relato de caso | Cureus | Mulher trans de 25 anos, com psoríase em placas grave, desenvolveu hipertricose generalizada após iniciar ciclosporina, apesar de usar estradiol e triptorelina como bloqueio de testosterona. O quadro foi atribuído à ciclosporina, **não** a um benefício da triptorelina. |

---

## Informações de Comercialização no Brasil

Todos os registros estão cancelados; atualmente não há produto com registro válido.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 128760009 | Gonapeptyl Depot | Não informada | Outros produtos para o aparelho digestivo e metabolismo |
| Registro nº 128760014 | Gonapeptyl Daily | Não informada | Outros produtos para o aparelho digestivo e metabolismo |
| Registro nº 105730120 | Neo Decapeptyl | Não informada | Outros prods. não enquadrados em classe terapêutica específica |

---

## Considerações de Segurança

Os dados de advertências e contraindicações da bula da ANVISA não estavam disponíveis nos dados compilados. Consulte a bula para essas informações.

- **Contraindicações ou condições de atenção sugeridas pelo grafo de conhecimento do TxGNN** (associações do grafo, não texto de bula): hipertensão, doença renal, piureter, doença hepática, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, obesidade (incluindo obesidade monogênica), obstrução do trato urinário e doença da medula espinhal.
- **Interações medicamentosas:** foram identificadas 262 interações. Entre as listadas:
  - **Grave:** dolasetrona.
  - **Moderada:** antidiabéticos (acarbose, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, saxagliptina, dulaglutida, empagliflozina, glimepirida), famotidina, loperamida, bisacodil, claritromicina, ácido picossulfúrico, polietilenoglicol 3350 com eletrólitos e palonosetrona.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que apoiem a triptorelina na hipertricose. O único artigo encontrado descreve um efeito adverso da ciclosporina, e não há mecanismo plausível que sustente a previsão (nível de evidência L5).
- Além disso, todos os registros brasileiros do fármaco estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Obter os dados de mecanismo de ação a partir do DrugBank.
- Apresentar uma hipótese mecanística plausível e dados pré-clínicos ou clínicos que ligue a supressão do eixo GnRH à hipertricose, o que hoje não existe.
- Esclarecer a situação regulatória atual da triptorelina no Brasil, já que todos os registros listados estão cancelados.
- Se o objetivo for aproveitar o potencial do fármaco, avaliar separadamente indicações com evidência real, como a puberdade precoce central.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

