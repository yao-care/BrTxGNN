---
layout: default
title: Bempedoic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bempedoic Acid: nova indicação prevista, Hipertireoidismo (Hyperthyroidism) (nível de evidência L5). Indicação original: Antilipêmicos"
monitor_inn: "bempedoic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "homozygous familial hypercholesterolemia", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
---

# Bempedoic Acid
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

# Ácido bempedoico: De antilipêmico para hipertireoidismo (previsão do modelo)

## Resumo em Uma Frase

O ácido bempedoico (NUSTENDI) foi originalmente registrado na ANVISA como antilipêmico, ou seja, para redução de lipídios no sangue.
O modelo TxGNN prevê que pode ser eficaz para **Hipertireoidismo (Hyperthyroidism)**, mas esta é uma previsão puramente baseada em grafo, com **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Hipertireoidismo (Hyperthyroidism) |
| Pontuação de Previsão TxGNN | 99,61% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo conhecimento farmacológico geral, o ácido bempedoico inibe a enzima ATP-citrato liase (ACLY) no fígado, etapa anterior à HMG-CoA redutase, o que aumenta a expressão de receptores de LDL e reduz o LDL-colesterol.

Não há vínculo mecanístico claro entre essa via e a síntese ou secreção de hormônios tireoidianos. A pontuação alta (0,996) reflete apenas a proximidade no grafo de conhecimento, sem ensaios ou literatura que a sustentem. Portanto, a previsão deve ser tratada com cautela e, por ora, como hipótese sem respaldo.

**Outras previsões do modelo (todas com nível L5, salvo indicação):**

| Posição | Doença prevista | Pontuação | Comentário |
|------|------|------|------|
| 2 | Resistência ao hormônio tireoidiano (mutação no receptor beta) | 99,58% | Sobreposição conceitual frouxa com metabolismo lipídico hepático; especulativo |
| 3 | Febre catarral maligna | 99,58% | Doença veterinária de ruminantes; provável artefato do grafo |
| 4 | Rinotraqueíte infecciosa bovina | 99,58% | Doença veterinária; provável artefato do grafo |
| 5 | Infecção por citomegalovírus | 99,53% | Conceitualmente concebível via metabolismo lipídico do hospedeiro, sem dados |
| 6 | Hipercolesterolemia familiar homozigótica | 99,48% | Melhor ajuste mecanístico e única com literatura (nível L4) |
| 7 | Hipertiroxinemia | 99,34% | Sem vínculo conhecido |
| 8 | Osteoporose induzida por fármacos | 99,21% | Sem mecanismo conhecido |
| 9 | Neoplasia endócrina múltipla | 99,18% | Sem racional mecanístico |
| 10 | Osteoporose associada à gestação | 99,17% | Sem vínculo; preocupações de segurança na gravidez |

A previsão de **hipercolesterolemia familiar homozigótica (HoFH)** é a mais plausível: o fármaco atua sobre o metabolismo do colesterol. Contudo, na HoFH a função do receptor de LDL está gravemente comprometida ou ausente, de modo que a eficácia de um mecanismo dependente do aumento desses receptores tende a ser limitada, sobretudo em pacientes receptor-negativos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para hipertireoidismo.

## Evidências da Literatura

Atualmente não há literatura relacionada ao hipertireoidismo.

*Nota: a literatura disponível refere-se à HoFH (previsão de posição 6), não ao hipertireoidismo. Para referência, os estudos mais relevantes foram:*

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Coorte (mundo real) | Journal of Clinical Lipidology | Avaliação da eficácia e tolerabilidade do ácido bempedoico em pacientes com HoFH |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisão | J Am Coll Cardiol | Terapias novas e emergentes para redução de LDL-C, incluindo o ácido bempedoico |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Consenso de especialistas | Journal of Clinical Lipidology | Atualização da National Lipid Association sobre hipercolesterolemia familiar |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Revisão | J Atheroscler Thromb | Avanços no tratamento da HoFH |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Revisão | Experimental and Molecular Pathology | Terapias inovadoras para o manejo da HoFH |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 104540195 (cancelado) | NUSTENDI | Não informada | Antilipêmicos |

## Considerações de Segurança

**Interações Medicamentosas** (23 interações identificadas; as principais estão listadas abaixo):

- **Gravidade maior**: corticosteroides (hidrocortisona, triancinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort, fludrocortisona), levofloxacino e sinvastatina.
- **Gravidade moderada**: empagliflozina, glibenclamida, repaglinida, rifaximina, rosuvastatina, selexipague, fexofenadina e revefenacina.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para hipertireoidismo baseia-se apenas na pontuação do modelo (nível L5), sem ensaios, literatura ou vínculo mecanístico plausível. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação documentados e uma análise que relacione ACLY à fisiologia tireoidiana
- Obtenção e análise da bula na ANVISA (advertências e contraindicações), pendência bloqueante para a triagem de segurança
- Estudos pré-clínicos que sustentem qualquer efeito sobre a função tireoidiana
- Esclarecimento da situação regulatória no Brasil (registro cancelado)
- Considerar priorizar a avaliação da HoFH (posição 6), com evidências observacionais, mas atentando à limitação mecanística em pacientes com receptor de LDL ausente
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

