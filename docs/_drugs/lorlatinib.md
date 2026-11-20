---
layout: default
title: Lorlatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Lorlatinib: nova indicação prevista, Fibromatose gengival (fibromatosis, gingival) (nível de evidência L5). Indicação original: Agentes antineoplásicos"
monitor_inn: "lorlatinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Lorlatinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Lorlatinibe: De agente antineoplásico para fibromatose gengival (previsão do modelo, sem evidências de suporte)
{: .text-alpha }

## Resumo em Uma Frase

Lorlatinibe (marca LORBRENA) é um inibidor de tirosina quinase de ALK/ROS1, registrado na ANVISA na categoria de agentes antineoplásicos.
O modelo TxGNN prevê que pode ser eficaz para **fibromatose gengival (fibromatosis, gingival)**, mas **não há ensaios clínicos nem publicações** que apoiem esta previsão: trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Fibromatose gengival (fibromatosis, gingival) |
| Pontuação de Previsão TxGNN | 0,9981 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Lorlatinib (tradução não oficial): “O lorlatinibe é um inibidor de quinase com atividade in vitro contra ALK e ROS1, bem como TYK1, FER, FPS, TRKA, TRKB, TRKC, FAK, FAK2 e ACK. O lorlatinibe demonstrou atividade in vitro contra múltiplas formas mutantes da enzima ALK, incluindo algumas mutações detectadas em tumores no momento da progressão da doença durante o uso de crizotinibe e outros inibidores de ALK.” Texto original em inglês: "Lorlatinib is a kinase inhibitor with in vitro activity against ALK and ROS1 as well as TYK1, FER, FPS, TRKA, TRKB, TRKC, FAK, FAK2, and ACK. Lorlatinib demonstrated in vitro activity against multiple mutant forms of the ALK enzyme, including some mutations detected in tumors at the time of disease progression on crizotinib and other ALK inhibitors." ([DailyMed: Lorbrena (lorlatinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2b34d62d-e02a-4af3-bc0d-1571dd4ee76d), versão de 2026-06-26; acessado em 2026-11-19). Segundo informações conhecidas da literatura, o lorlatinibe é um inibidor de tirosina quinase de terceira geração, com penetração no sistema nervoso central, que atua sobre ALK e ROS1. Sua eficácia está bem estabelecida no câncer de pulmão de células não pequenas (CPNPC) ALK-positivo.

Não há ligação identificável entre a sinalização de ALK e a fibromatose gengival. A pontuação alta do TxGNN (0,9981) é uma previsão computacional, sem estudos que a sustentem. Portanto, **a plausibilidade mecanística desta previsão não pôde ser confirmada**.

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

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 121100476 | LORBRENA | PFIZER BRASIL LTDA | Ativo |

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

<!-- review:begin br-lic-20261106-lorlatinib-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão para fibromatose gengival é exclusivamente computacional (nível L5), sem ensaios clínicos, sem literatura e sem ligação mecanística com a inibição de ALK/ROS1. / O único registro brasileiro está cancelado, e a bula não pôde ser analisada, o que impede a triagem de segurança.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-lorlatinib-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Obter os dados de mecanismo de ação (MOA) no DrugBank.
- Demonstrar uma hipótese biológica que ligue ALK/ROS1 à fibromatose gengival, ou revisar o modelo para as previsões com possível erro de mapeamento.
- Se houver interesse em outros tumores com alteração de ALK (por exemplo, neuroblastoma), tratá-los como candidatos separados, com avaliação própria.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O único registro brasileiro está cancelado, e a bula não pôde ser analisada, o que impede a triagem de segurança” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Lorbrena (lorlatinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2b34d62d-e02a-4af3-bc0d-1571dd4ee76d) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

