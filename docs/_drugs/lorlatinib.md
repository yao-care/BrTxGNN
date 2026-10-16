---
layout: default
title: Lorlatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Lorlatinib: nova indicação prevista, Fibromatose gengival (fibromatosis, gingival) (nível de evidência L5). Indicação original: Agentes antineoplásicos"
monitor_inn: "lorlatinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Lorlatinib
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

# Lorlatinibe: De agente antineoplásico para fibromatose gengival (previsão do modelo, sem evidências de suporte)

## Resumo em Uma Frase

Lorlatinibe (marca LORBRENA) é um inibidor de tirosina quinase de ALK/ROS1, registrado na ANVISA na categoria de agentes antineoplásicos.
O modelo TxGNN prevê que pode ser eficaz para **fibromatose gengival (fibromatosis, gingival)**, mas **não há ensaios clínicos nem publicações** que apoiem esta previsão: trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Fibromatose gengival (fibromatosis, gingival) |
| Pontuação de Previsão TxGNN | 99,81% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas da literatura, o lorlatinibe é um inibidor de tirosina quinase de terceira geração, com penetração no sistema nervoso central, que atua sobre ALK e ROS1. Sua eficácia está bem estabelecida no câncer de pulmão de células não pequenas (CPNPC) ALK-positivo.

Não há ligação identificável entre a sinalização de ALK e a fibromatose gengival. A pontuação alta do TxGNN (99,81%) é uma previsão computacional, sem estudos que a sustentem. Portanto, **a plausibilidade mecanística desta previsão não pôde ser confirmada**.

As demais previsões de maior pontuação (fibroma de pulmão, hamartoma de pulmão, carcinoma do hilo pulmonar, entre outras) também carecem de apoio mecanístico, exceto onde há alteração de ALK. Isso exige cautela na interpretação do modelo. Algumas dessas previsões parecem refletir, na verdade, a indicação já estabelecida (CPNPC ALK-positivo) ou outro tumor com alteração de ALK (neuroblastoma), e não um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para fibromatose gengival.

## Evidências da Literatura

Atualmente não há literatura relacionada para fibromatose gengival.

### Observação sobre outras previsões de maior evidência

Entre as 10 previsões, algumas têm literatura, mas ela se refere sobretudo a usos já estabelecidos ou a mapeamentos de doença inadequados:

| Previsão | Evidência encontrada | Interpretação |
|------|------|------|
| Neoplasia benigna de pulmão (nº 5) | Estudos de fase 3 CROWN, como [33207094](https://pubmed.ncbi.nlm.nih.gov/33207094/) (NEJM, 2020) e [38819031](https://pubmed.ncbi.nlm.nih.gov/38819031/) (JCO, 2024) | Refere-se a CPNPC ALK-positivo (indicação já estabelecida), não a tumores benignos; provável erro de mapeamento |
| Tumor de células germinativas do pulmão (nº 7) | Fase 1 em neuroblastoma ALK-positivo, [37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/) (Nature Medicine, 2024) | Evidência de outro tumor (neuroblastoma); não apoia diretamente o rótulo |
| Carcinoma do hilo pulmonar (nº 4) | Relato de caso, [37934724](https://pubmed.ncbi.nlm.nih.gov/37934724/) (2023) | Evidência indireta, sobre CPNPC ALK-positivo |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 121100476 (cancelado) | LORBRENA | Não informada | Agentes antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de tirosina quinase ALK/ROS1) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Lipídios séricos (colesterol e triglicerídeos), função hepática, além de acompanhamento de efeitos no SNC e de sinais de toxicidade pulmonar, conforme a literatura compilada |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 461 interações, das quais as principais listadas são:
  - **Grave (Major)**: dexametasona, claritromicina.
  - **Moderada**: hidrocortisona, triamcinolona, betametasona, alosetrona, bupropiona, aprepitanto, morfina, clorpropamida, cimetidina, dapagliflozina, saxagliptina, linagliptina, empagliflozina, glimepirida, dronabinol, eliglustat, naldemedina, naloxegol.
- **Sinais de segurança na literatura compilada**: dislipidemia e efeitos metabólicos (hipercolesterolemia, hipertrigliceridemia, ganho de peso), síndrome do desconforto respiratório agudo, síndrome de Sweet e toxicidade pulmonar quando associado a anticorpo anti-GD2.

Os dados de advertências e contraindicações da bula não estavam disponíveis. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para fibromatose gengival é exclusivamente computacional (nível L5), sem ensaios clínicos, sem literatura e sem ligação mecanística com a inibição de ALK/ROS1.
- O único registro brasileiro está cancelado, e a bula não pôde ser analisada, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Obter os dados de mecanismo de ação (MOA) no DrugBank.
- Demonstrar uma hipótese biológica que ligue ALK/ROS1 à fibromatose gengival, ou revisar o modelo para as previsões com possível erro de mapeamento.
- Se houver interesse em outros tumores com alteração de ALK (por exemplo, neuroblastoma), tratá-los como candidatos separados, com avaliação própria.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

