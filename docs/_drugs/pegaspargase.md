---
layout: default
title: Pegaspargase
parent: Apenas Predição do Modelo (L5)
nav_order: 511
evidence_level: L5
indication_count: 7
monitor_inn: "PEGASPARGASE"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
last_modified_at: 2026-10-31
description: "Pegaspargase: nova indicação prevista, Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Pegaspargase
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Pegaspargase: Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma
{: .text-alpha }

## Resumo em Uma Frase

Pegaspargase é uma forma pegilada da enzima asparaginase, usada originalmente no tratamento da leucemia linfoblástica aguda (LLA).
O modelo TxGNN prevê que ele pode ser eficaz para **leucemia linfocítica crônica/linfoma linfocítico de pequenas células pré-germinal (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)**, mas **não há ensaios clínicos nem publicações** que estudem diretamente essa doença: trata-se de uma previsão exclusivamente do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| Pontuação de Previsão TxGNN | 0.9995 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, a asparaginase degrada a asparagina circulante, e células linfoides imaturas com baixa expressão de asparagina sintetase dependem desse aminoácido para sobreviver. Esse racional é bem estabelecido na LLA.

A relação com a nova indicação é fraca. A LLC/LLP é composta por células B maduras, de proliferação lenta, e nada indica a mesma dependência de asparagina. A pontuação alta provavelmente reflete a proximidade na ontologia com as indicações de leucemia linfoide, e não um sinal biológico independente. Isso vale também para o subtipo com hipermutação somática dos genes da região variável da cadeia pesada de imunoglobulina (pontuação idêntica, 0,9995).


---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação principal (LLC/LLP pré-germinal).

Para contexto, o modelo também associou o pegaspargase a "neoplasia linfoide" (rank 5), com ensaios majoritariamente em LLA, que é a indicação original e, portanto, não constituem evidência direta da nova indicação principal. Exemplos:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Concluído | 470 | Estudo internacional em LLA recidivante/refratária; indicação original |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Concluído | 37 | Regime MOAD com pegaspargase em resgate de LLA |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Ativo, sem recrutamento | 440 | Levocarnitina para prevenir hepatotoxicidade associada à asparaginase |
| [NCT06376721](https://clinicaltrials.gov/study/NCT06376721) | Phase 1/2 | Recrutando | 43 | Linperlisib + camrelizumabe + pegaspargase em linfoma NK/T recidivante/refratário |
| [NCT02396043](https://clinicaltrials.gov/study/NCT02396043) | Phase 2 | Desconhecido | 50 | Regime BFM-95 modificado em linfoma linfoblástico T do adulto |

---

## Evidências da Literatura

Atualmente não há literatura relacionada à indicação principal (LLC/LLP pré-germinal).

Literatura de contexto, em doenças linfoides diferentes:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27723108](https://pubmed.ncbi.nlm.nih.gov/27723108/) | 2017 | Ensaio Phase 2 | Hematol Oncol | Regime MESA (com pegaspargase) em linfoma NK/T: resposta completa de 43,5% e resposta global de 87% em 46 pacientes |
| [34449095](https://pubmed.ncbi.nlm.nih.gov/34449095/) | 2021 | Estudo multicêntrico | Am J Hematol | P-GEMOX seguido de radioterapia em linfoma NK/T em estágio inicial |
| [36781296](https://pubmed.ncbi.nlm.nih.gov/36781296/) | 2023 | Revisão | Leuk Lymphoma | Opinião de especialistas sobre uso e manejo de toxicidade da asparaginase na LLA |
| [30626253](https://pubmed.ncbi.nlm.nih.gov/30626253/) | 2019 | Coorte | Leuk Lymphoma | Atividade plasmática da asparaginase e depleção de asparagina com pegaspargase em LLA |

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 112780076 | ONCASPAR | LABORATÓRIOS SERVIER DO BRASIL LTDA | Ativo |
| 156280010 | ONCASPAR | BAXALTA BRASIL BIOCIÊNCIA LTDA | Cancelado |
| 169790012 | ONCASPAR | SHIRE FARMACÊUTICA BRASIL LTDA. | Cancelado |

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Enzima antineoplásica (depletora de asparagina), não é um citotóxico convencional clássico |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Função hepática, amilase/lipase, coagulação e fibrinogênio, glicemia, atividade da asparaginase |
| Proteção no Manuseio | Seguir os regulamentos institucionais de manuseio de antineoplásicos |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações, todas de gravidade moderada nos dados exibidos. Exemplos: corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (metformina, acarbose, alogliptina, canagliflozina, dapagliflozina, dulaglutida, clorpropamida), antibióticos (doxiciclina, tetraciclina, claritromicina), ácido acetilsalicílico e bupropiona.
- **Pontos de atenção da literatura**: hepatotoxicidade, pancreatite, trombose, hipersensibilidade e toxicidade maior em adultos e adolescentes/jovens adultos.

Consulte a bula para advertências e contraindicações.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (LLC/LLP pré-germinal) baseia-se apenas na pontuação do modelo, sem ensaios ou publicações sobre a própria doença. Não há racional biológico para dependência de asparagina, e a pontuação parece refletir proximidade de ontologia.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos que mostrem sensibilidade de células de LLC/LLP à depleção de asparagina (expressão de asparagina sintetase).
- Dados do mecanismo de ação e da bula da ANVISA (advertências e contraindicações; o texto de indicação dos registros está vazio).
- Se houver interesse em reposicionamento, avaliar separadamente o linfoma NK/T extranodal, onde a literatura é mais consistente, como indicação própria (não é a previsão principal deste relatório).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

