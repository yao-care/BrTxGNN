---
layout: default
title: Ciprofloxacin
parent: Evidência Moderada (L3-L4)
nav_order: 223
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Ciprofloxacin: nova indicação prevista, Esclerodermia Difusa (Diffuse Scleroderma) (nível de evidência L4). Indicação original: Infecções bacterianas (febre tifoide, salmonelose, febre paratifoide…"
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
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

# Ciprofloxacino: De infecções bacterianas à esclerodermia difusa

## Resumo em Uma Frase

O ciprofloxacino é um antibiótico da classe das fluoroquinolonas, originalmente usado em infecções bacterianas como febre tifoide, salmonelose, shigelose, pneumonia bacteriana e infecções por *Pseudomonas aeruginosa*.
O modelo TxGNN prevê que pode ser eficaz para **Esclerodermia Difusa (Diffuse Scleroderma)**, mas **não há ensaios clínicos registrados** e apenas **2 publicações** apoiam esta direção, ambas de baixa solidez.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (febre tifoide, salmonelose, febre paratifoide, pneumonia bacteriana, infecção por *Pseudomonas aeruginosa*, antraz, shigelose, entre outras) |
| Nova Indicação Prevista | Esclerodermia Difusa (Diffuse Scleroderma) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

> Observação: as indicações originais vêm das relações do grafo de conhecimento do TxGNN, e não de texto de bula, pois não há registros da ANVISA nos dados compilados.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o ciprofloxacino é uma fluoroquinolona que inibe a DNA girase e a topoisomerase IV bacterianas, e sua eficácia em infecções por bactérias Gram-negativas e Gram-positivas está bem estabelecida.

A relação com a esclerodermia é indireta e se apoia em duas linhas. A primeira é a hipótese de um efeito antifibrótico na pele, possivelmente por modulação da síntese de colágeno ou da atividade de fibroblastos (PMID 20507401). A segunda é o tratamento do supercrescimento bacteriano do intestino delgado, comum na esclerose sistêmica e causa de diarreia crônica e má absorção (PMID 7728404). Essa segunda linha atua sobre uma complicação, não sobre a doença em si.

Nenhuma das duas linhas traz evidência controlada de modificação da doença. A pontuação muito alta do TxGNN é apenas uma previsão computacional e não substitui dados clínicos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Exploratório/pré-clínico (segundo a classificação dos dados) | The Journal of Dermatology | Avalia o ciprofloxacino oral como antifibrótico na pele de pacientes com esclerodermia; o resumo disponível descreve um ensaio clínico randomizado, duplo-cego e controlado, mas está truncado e não mostra os resultados |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Coorte/diagnóstico | British Journal of Rheumatology | 24 pacientes com esclerose sistêmica e sintomas de má absorção investigados para supercrescimento bacteriano do intestino delgado e resultado do tratamento |

## Citotoxicidade

Não se aplica: o ciprofloxacino não é um antineoplásico.

## Considerações de Segurança

- **Contraindicações (segundo relações do grafo de conhecimento, não texto de bula)**: síndrome do QT longo (inclusive familiar), *torsades de pointes*, epilepsia, doença renal, deficiência de potássio, tendinite e outras doenças de tendão e articulação (periartrite, esporão do calcâneo, bursite do calcâneo), doenças do sistema nervoso periférico e neuropatia periférica, colite por *Clostridium difficile*, miastenia gravis (inclusive de início na idade adulta) e doenças da junção neuromuscular, enterocolite necrosante perinatal.
- **Interações Medicamentosas** (100 interações identificadas; as de gravidade **Maior** incluem):
  - Corticosteroides: hidrocortisona, triancinolona, dexametasona e betametasona (risco aumentado de lesão de tendão)
  - Bupropiona
- **Interações de gravidade Moderada** (exemplos): antidiabéticos (metformina, pioglitazona, acarbose, alogliptina, albiglutida), famotidina, loperamida, alosetrona, aprepitanto, ácido acetilsalicílico, budesonida, bisacodil e fosfato de cálcio.

Para a esclerodermia, vale atenção especial: pacientes frequentemente usam corticosteroides, e as contraindicações de tendinite e neuropatia periférica podem ser relevantes. Consulte a bula para as advertências completas, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos registrados, e a literatura é limitada e de baixa solidez, sem resultados controlados de modificação da doença. A pontuação do TxGNN é apenas uma previsão computacional, e há sinais de segurança relevantes no perfil do fármaco (tendões, neuropatia).

**Para prosseguir, é necessário:**
- Obter o texto completo e os resultados do estudo de 2010 (PMID 20507401) e avaliar sua qualidade metodológica
- Realizar ou localizar ensaios clínicos controlados de ciprofloxacino na esclerodermia difusa
- Obter dados de mecanismo de ação (MOA) para sustentar a hipótese antifibrótica
- Obter advertências e contraindicações da bula aprovada pela ANVISA
- Esclarecer a situação regulatória no Brasil: os dados compilados indicam "não comercializado" e zero registros, o que parece inconsistente com um antibiótico amplamente utilizado

---

### Nota sobre as demais previsões

Entre as outras indicações previstas, a **peste septicêmica** (pontuação TxGNN de 99,64%) tem o respaldo mais forte nos dados compilados, com nível de evidência L1 e estágio S2, e trata-se de um uso antibacteriano direto, coerente com a atividade do fármaco contra *Yersinia pestis*. Há ensaio randomizado (NEJM 2025, PMID 40768716; protocolo IMASOY, PMID 32807214 e 38970065) e dados em primatas não humanos (PMID 32435805). Contudo, o ensaio randomizado se refere à peste bubônica, não à septicêmica, e o status de Fase 3 precisa ser verificado. Como essa indicação é uma extensão da atividade antibacteriana já conhecida, e não um reposicionamento propriamente dito, ela não foi adotada como indicação principal deste relatório, que segue a primeira previsão do modelo. As demais (hiperamilasemia, síndrome de hiperviscosidade policlonal, analbuminemia congênita, incompatibilidade de grupo sanguíneo, doenças hematológicas pré-malignas, ceratoconjuntivite epitelial punctata, gamopatia monoclonal e doença hematológica associada a neuropatia periférica) não têm sustentação mecanística ou apresentam apenas evidência indireta, com recomendação de *Hold*.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

