---
layout: default
title: Caffeine
parent: Apenas Predição do Modelo (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Caffeine: nova indicação prevista, Doença da cavidade nasal (nasal cavity disease) (nível de evidência L5). Indicação original: Estimulantes respiratórios"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
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

## Cafeína: De analgésico e estimulante respiratório para doença da cavidade nasal
{: .text-alpha }

## Resumo em Uma Frase

A cafeína foi usada no Brasil principalmente como adjuvante em analgésicos não narcóticos, relaxantes musculares, estimulantes respiratórios e produtos para o alívio sintomático da gripe.
O modelo TxGNN prevê que ela pode ser eficaz para **doença da cavidade nasal (nasal cavity disease)**, mas até o momento há **0 ensaios clínicos** e apenas **3 publicações** indiretas (uma revisão, um estudo de formulação pré-clínico e um estudo em animais) ligadas a essa direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Estimulantes respiratórios |
| Nova Indicação Prevista | Doença da cavidade nasal (nasal cavity disease) |
| Pontuação de Previsão TxGNN | 99,91% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a cafeína é um antagonista dos receptores de adenosina e inibidor de fosfodiesterases (PDE). Esse perfil explica seu uso como estimulante respiratório e como adjuvante analgésico em associações com dipirona, ácido acetilsalicílico e relaxantes musculares.

A relação com a doença nasal é plausível, mas não comprovada. Receptores de sabor amargo (TAS2R) presentes nas vias aéreas são ativados pela cafeína e podem regular o batimento ciliar e a defesa inata. A única literatura específica para o nariz é um estudo de formulação de gel intranasal de cafeína para cognição após privação de sono, que visa a entrega do nariz ao cérebro e não o tratamento de doença nasal.

A pontuação alta do TxGNN (99,91%) não é sustentada por dados clínicos. A previsão deve ser tratada como hipótese a explorar, não como evidência de eficácia.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Revisão | Pharmacology & Therapeutics | Os receptores de sabor amargo (T2R) estão presentes em diversos tecidos, incluindo cavidade nasal e pulmões, e podem ter papel nas vias aéreas humanas |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Estudo pré-clínico de formulação | Current Drug Delivery | Gel intranasal termossensível de cafeína para melhorar a cognição após privação de sono (entrega nariz-cérebro) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Estudo em animais | Cancer Research | Chá preto e cafeína inibiram a carcinogênese pulmonar induzida por NNK em ratos F344 |

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados. Os cinco principais são:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100580115 | Peyona | Não informada | Estimulantes respiratórios |
| Registro nº 154230047 | Tylalgin Caf | Não informada | Analgésicos não narcóticos |
| Registro nº 101180611 | Miosan Caf | Não informada | Relaxantes musculares |
| Registro nº 109170076 | Gripinew | Não informada | Produtos para terapia sintomática da gripe |
| Registro nº 178170004 | Melhoral | Não informada | Analgésicos não narcóticos |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: o grafo de conhecimento do TxGNN associa a cafeína a contraindicações em diversas condições, entre elas: hipertensão, síndrome do QT longo, hipotensão ortostática, síndrome de taquicardia postural ortostática, epilepsia, insônia, transtornos de ansiedade, DPOC, úlcera gástrica e péptica, doença inflamatória intestinal, porfiria, doença hepática e insuficiência hepática, doença renal, pancreatite, doença da vesícula biliar, trombocitopenia e hipotireoidismo.
- **Interações Medicamentosas**: foram identificadas 75 interações. As de maior gravidade entre as listadas são com **cocaína (nasal e tópica)**, classificadas como **Maior**. Interações de nível **Moderado** incluem alosetrona, obeticólico, adenosina, anagrelida, bendamustina, capmatinibe, ciprofloxacino, cicloserina, dipiridamol e duloxetina. Interações de nível **Menor** incluem ácido acetilsalicílico, cimetidina, atazanavir e dissulfiram.

Consulte a bula para advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se apoia apenas no modelo e em literatura indireta, sem ensaios clínicos (nível L5). Além disso, todos os 20 registros brasileiros estão cancelados, e há um amplo conjunto de contraindicações potenciais no grafo de conhecimento.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), lacuna de dados que bloqueia a triagem de segurança
- Obter dados de mecanismo de ação a partir do DrugBank
- Realizar estudos pré-clínicos e clínicos específicos de doença nasal (por exemplo, papel dos receptores TAS2R no epitélio nasal)
- Avaliar a viabilidade de via de administração (intranasal ou outra) e a situação regulatória, dado que não há registros vigentes no Brasil
- Considerar alternativas com evidência mais forte entre as demais previsões (por exemplo, cefaleia hípnica, cuja literatura relata o uso de cafeína como terapia de primeira linha em séries pequenas e relatos de casos)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

