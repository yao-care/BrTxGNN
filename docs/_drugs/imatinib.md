---
layout: default
title: Imatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
last_modified_at: 2026-11-20
description: "Imatinib: nova indicação prevista, fibrossarcoma cardíaco (heart fibrosarcoma) (nível de evidência L5). No Brasil, registros na ANVISA: 29 (ativos: 17)"
---

# Imatinib
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

## Imatinibe: inibidor de tirosina quinase (BCR-ABL, KIT, PDGFR) → fibrossarcoma cardíaco (heart fibrosarcoma)
{: .text-alpha }

## Resumo em Uma Frase

Imatinibe é um inibidor de tirosina quinase que atua sobre as quinases ABL, KIT e PDGFR.
O modelo TxGNN prevê que pode ser eficaz para **fibrossarcoma cardíaco (heart fibrosarcoma)**, mas, nos dados compilados para este relatório, há **0 ensaios clínicos** e apenas **1 publicação** (um comentário geral sobre novas indicações do imatinibe), sem estudo que investigue diretamente essa doença.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | fibrossarcoma cardíaco (heart fibrosarcoma) |
| Pontuação de Previsão TxGNN | 0,9994 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 17 de 29) |
| Número de Registros | 29 (ativos: 17) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Imatinib (tradução não oficial): “O mesilato de imatinibe é um inibidor da proteína tirosina quinase que inibe a tirosina quinase BCR-ABL, a tirosina quinase anormal constitutiva criada pela anomalia do cromossomo Filadélfia na LMC. O imatinibe inibe a proliferação e induz a apoptose em linhagens celulares BCR-ABL positivas, bem como em células leucêmicas frescas de leucemia mieloide crônica com cromossomo Filadélfia positivo.” Texto original em inglês: "Imatinib mesylate is a protein-tyrosine kinase inhibitor that inhibits the BCR-ABL tyrosine kinase, the constitutive abnormal tyrosine kinase created by the Philadelphia chromosome abnormality in CML. Imatinib inhibits proliferation and induces apoptosis in BCR-ABL positive cell lines as well as fresh leukemic cells from Philadelphia chromosome positive chronic myeloid leukemia." ([DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b), versão de 2026-07-13; acessado em 2026-11-19). Segundo informações conhecidas e a literatura citada, o imatinibe inibe as quinases PDGFR, KIT e ABL.

Alguns tumores do tipo fibrossarcoma podem ser dependentes de PDGFB, como ocorre na fusão COL1A1-PDGFB do dermatofibrossarcoma protuberans. Isso fornece uma ponte mecanística plausível, pois a inibição de PDGFR poderia, em teoria, atingir tumores com esse tipo de sinalização.

No entanto, não existem dados específicos para tumores cardíacos. A única publicação disponível é uma revisão geral sobre novas indicações do imatinibe, com a observação de que as evidências não são robustas. A previsão, portanto, é sustentada essencialmente pelo modelo e por um raciocínio mecanístico indireto.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Revisão | Prescrire International | Comentário sobre as novas indicações do imatinibe, concluindo que, apesar da expansão progressiva, as evidências não são robustas. Não aborda fibrossarcoma cardíaco. |

## Considerações de Segurança

- **Interações Medicamentosas** (100 interações registradas; exemplos):
  - Gravidade maior: eliglustate, naloxegol.
  - Gravidade moderada: hidrocortisona, dexametasona, betametasona, budesonida, triancinolona, pioglitazona, glimepirida, claritromicina, cimetidina, aprepitanto, morfina, lansoprazol, entre outras.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo (0,9994), mas não há ensaios clínicos nem estudos que avaliem diretamente o imatinibe em fibrossarcoma cardíaco (nível L5). O raciocínio mecanístico é plausível, porém indireto.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação detalhados e verificação da dependência de PDGFR/KIT em tumores cardíacos.
- Relatos de casos, séries ou estudos pré-clínicos específicos de fibrossarcoma cardíaco.
- Obtenção e análise da bula registrada na ANVISA (advertências e contraindicações).
- Plano de monitoramento de segurança, considerando as interações de gravidade maior e a cardiotoxicidade em população com tumor cardíaco.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

