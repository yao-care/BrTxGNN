---
layout: default
title: Primidone
parent: Apenas Predição do Modelo (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidona: De anticonvulsivante a neoplasia do nervo trigêmeo (previsão do modelo, sem suporte biológico)

## Resumo em Uma Frase

Primidona é um anticonvulsivante, registrado na ANVISA com a indicação "anticonvulsivantes".
O modelo TxGNN prevê, em primeira posição, **neoplasia do nervo trigêmeo (trigeminal nerve neoplasm)**, mas **não há nenhum ensaio clínico nem publicação** que sustente essa direção, e a previsão provavelmente é um artefato de proximidade no grafo de conhecimento.
Entre as dez previsões, as mais plausíveis do ponto de vista biológico são as epilepsias reflexas (por exemplo, **convulsões audiogênicas**, com estudos em animais, e **convulsões induzidas por micção**, com literatura indireta).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Neoplasia do nervo trigêmeo (trigeminal nerve neoplasm) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 2 (ambos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a primidona é metabolizada em fenobarbital e feniletilmalonamida (PEMA), e atua sobre a excitabilidade neuronal (modulação de canais de sódio e potencialização do GABA-A via fenobarbital). Sua eficácia como anticonvulsivante está estabelecida.

Para **neoplasia do nervo trigêmeo**, não há vínculo mecanístico crível: a primidona não tem atividade antineoplásica conhecida. A pontuação muito alta (99,99%) provavelmente reflete proximidade no grafo com distúrbios do nervo trigêmeo, e não uma previsão biologicamente fundamentada. Esta previsão não deve ser considerada razoável.

As demais previsões de alta pontuação estão muito mais próximas da indicação original, pois são tipos de crises epilépticas (convulsões do pensamento, orgásmicas, de sobressalto, alimentares, por micção, audiogênicas e da leitura). O racional é a atividade antiepiléptica geral, mas nenhuma delas tem evidência direta de eficácia da primidona. A neuralgia do trigêmeo tem racional de classe (carbamazepina e oxcarbazepina são de primeira linha), porém sem dados específicos da primidona. A deficiência de beta-cetotiolase (erro inato do metabolismo) não tem vínculo plausível com o fármaco e provavelmente é um artefato do grafo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados, nem para a primeira previsão nem para as demais.

## Evidências da Literatura

Para a indicação principal (neoplasia do nervo trigêmeo), atualmente não há literatura relacionada. Abaixo, as publicações mais relevantes das previsões seguintes (todas indiretas, nenhuma demonstra eficácia da primidona na doença prevista):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41432787](https://pubmed.ncbi.nlm.nih.gov/41432787/) | 2025 | Revisão | Journal of Neurology | Efeitos adversos psiquiátricos e comportamentais dos anticonvulsivantes em adultos com epilepsia (convulsões por micção) |
| [35861924](https://pubmed.ncbi.nlm.nih.gov/35861924/) | 2022 | Revisão | CNS Drugs | Relação entre anticonvulsivantes e distúrbios do movimento (convulsões por micção) |
| [28729328](https://pubmed.ncbi.nlm.nih.gov/28729328/) | 2017 | Revisão sistemática / meta-análise em rede | BMJ Open | Segurança comparativa de anticonvulsivantes para o neurodesenvolvimento de crianças expostas na gestação e amamentação (convulsões por micção) |
| [10094253](https://pubmed.ncbi.nlm.nih.gov/10094253/) | 1999 | Estudo randomizado (retirada de fármacos) | Brain | Estudo do MRC sobre retirada de anticonvulsivantes, incluindo fenobarbital/primidona, e risco de recorrência (convulsões por micção) |
| [8891399](https://pubmed.ncbi.nlm.nih.gov/8891399/) | 1995 | Revisão | Clinical Neuroscience | Primidona (500–1.000 mg/dia) entre os fármacos mais úteis para mioclonia (convulsões da leitura) |
| [116632](https://pubmed.ncbi.nlm.nih.gov/116632/) | 1979 | Relato de caso | Archives of Neurology | Convulsões mioclônicas induzidas pelo ato de desenhar (epilepsia reflexa) |
| [8548670](https://pubmed.ncbi.nlm.nih.gov/8548670/) | 1995 | Relato de caso | Zhonghua Yi Xue Za Zhi | Epilepsia de sobressalto manifestada como queda atônica em menino de 3,5 anos |
| [184518](https://pubmed.ncbi.nlm.nih.gov/184518/) | 1976 | Estudo em animais | Neurologie et Psychiatrie | Efeito de fenobarbital, fenitoína e primidona sobre enzimas cerebrais em camundongos com epilepsia audiogênica |
| [14249886](https://pubmed.ncbi.nlm.nih.gov/14249886/) | 1964 | Estudo em animais | Biull Eksp Biol Med | Convulsões audiogênicas após administração prévia de primidona em animais |
| [4525036](https://pubmed.ncbi.nlm.nih.gov/4525036/) | 1974 | Relato de caso veterinário | J Am Vet Med Assoc | Efeitos da terapia prolongada com primidona em um cão (convulsões alimentares) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101180659 (cancelado) | PRIMID | Não informada | Anticonvulsivantes |
| Registro 101180131 (cancelado) | PRIMID | Não informada | Anticonvulsivantes |

## Citotoxicidade

Não se aplica: a primidona não é antineoplásica. (Seção omitida conforme as regras.)

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: transtorno de ansiedade, transtornos neuróticos e distímicos, porfirias (incluindo porfiria hereditária), doença renal, doença hepática, doença da vesícula biliar, abuso/dependência de substâncias, apneia do sono (obstrutiva e síndromes de hipoventilação central), e alterações hematológicas (trombocitopenia, neutropenia, agranulocitose, leucopenia, pancitopenia, anemia, incluindo anemia macrocítica e neutropenias congênitas).
- **Interações Medicamentosas**: 273 interações registradas. Entre as listadas, destacam-se as de gravidade **maior** com **morfina** e **eliglustate**. A maioria das demais é de gravidade moderada (por exemplo, doxiciclina, hidrocortisona, dexametasona, betametasona, triancinolona, colecalciferol, calcifediol, calcitriol, pioglitazona, bupropiona, aprepitanto, metronidazol, canagliflozina, saxagliptina, difenoxina, difenoxilato, dronabinol). Cimetidina é de gravidade leve.

Para advertências principais e demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (neoplasia do nervo trigêmeo) é L5, sem ensaios, sem literatura e sem vínculo mecanístico plausível; a pontuação alta parece artefato do grafo. Além disso, os dois registros da primidona no Brasil estão cancelados, o que dificulta qualquer desenvolvimento local.
- As previsões do espectro de epilepsias reflexas (por exemplo, audiogênicas e por micção) são biologicamente mais coerentes, mas têm evidência apenas indireta (L4) e são pouco relevantes, pois a primidona já é anticonvulsivante.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA (advertências e contraindicações), pois a lacuna atual impede a triagem de segurança.
- Obter dados de mecanismo de ação (por exemplo, via DrugBank).
- Esclarecer a situação regulatória (registros cancelados) e a viabilidade de comercialização no Brasil.
- Se houver interesse, priorizar uma revisão de literatura direcionada a epilepsias reflexas e à neuralgia do trigêmeo, em vez de neoplasia do trigêmeo.
- Avaliar o perfil de segurança diante das contraindicações do grafo (porfiria, doenças hepáticas e renais, discrasias sanguíneas) e das interações de gravidade maior (morfina, eliglustate).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

