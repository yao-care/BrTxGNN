---
layout: default
title: Cefdinir
parent: Apenas Predição do Modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefdinir: nova indicação prevista, Hiperamilasemia (maior pontuação) (nível de evidência L5). Indicação original: Infecção estreptocócica, infecção por Staphylococcus aureus…"
monitor_inn: "Cefdinir"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "septicemic plague", "pyelonephritis"]
---

# Cefdinir
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

## Cefdinir: Da infecção estreptocócica à pielonefrite
{: .text-alpha }

## Resumo em Uma Frase

Cefdinir é uma cefalosporina de terceira geração, originalmente usada em infecções estreptocócicas e estafilocócicas (incluindo pneumonia estreptocócica).
O modelo TxGNN prevê que pode ser útil para **hiperamilasemia (hyperamylasemia)**, a previsão de maior pontuação, mas sem nenhuma evidência clínica que a sustente. A indicação com mais respaldo na literatura é a **pielonefrite (pyelonephritis)**, com **11 publicações** (nenhum ensaio clínico registrado), e é nela que este relatório se concentra.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção estreptocócica, infecção por *Staphylococcus aureus*, infecção estafilocócica e pneumonia estreptocócica (base de conhecimento TxGNN; não há texto de indicação aprovada no Brasil) |
| Nova Indicação Prevista | Hiperamilasemia (maior pontuação); pielonefrite (única com literatura relevante, analisada abaixo) |
| Pontuação de Previsão TxGNN | 98,27% (hiperamilasemia); 94,64% (pielonefrite) |
| Nível de Evidência | L5 (hiperamilasemia); L3 (pielonefrite) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold (hiperamilasemia); pielonefrite: questão de pesquisa, mantida em Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, cefdinir é uma cefalosporina de terceira geração que inibe a síntese da parede celular bacteriana, sua eficácia em infecções estreptocócicas e estafilocócicas é reconhecida, e mecanisticamente pode ser aplicável a outras infecções bacterianas.

**Hiperamilasemia (maior pontuação):** não há vínculo mecanístico identificável. Nenhuma via conecta um antibacteriano à regulação da amilase; a pontuação parece refletir a topologia do grafo de conhecimento, não a biologia. As demais previsões de topo (síndrome de hiperviscosidade policlonal, analbuminemia congênita, incompatibilidade de grupo sanguíneo, doenças hematológicas pré-malignas, gamopatia monoclonal etc.) apresentam o mesmo problema: sem mecanismo plausível, sem ensaios e sem literatura.

**Pielonefrite:** é biologicamente coerente, pois o cefdinir tem atividade contra uropatógenos comuns, como *E. coli* e *Klebsiella*. Porém, as evidências sobre cefalosporinas orais na pielonefrite indicam eficácia inferior ou incerta frente a fluoroquinolonas ou SMX-TMP, devido à menor exposição urinária e tecidual e à menor biodisponibilidade. O uso mais estudado é como terapia de transição (step-down) após tratamento intravenoso. A peste septicêmica (*Yersinia pestis*) também é plausível apenas em sentido geral, sem dados, e a via oral é inadequada para septicemia.

## Evidências de Ensaios Clínicos

Para a pielonefrite, atualmente não há ensaios clínicos relacionados registrados.

O único ensaio associado a outra previsão (doença hematológica congênita) é pouco relevante:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recrutando | 5000 | Estudo amplo de farmacocinética, farmacodinâmica e segurança de fármacos pouco estudados em crianças; não é específico para cefdinir nem fornece evidência de eficácia |

## Evidências da Literatura

Pielonefrite (10 publicações mais relevantes listadas):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30662274](https://pubmed.ncbi.nlm.nih.gov/30662274/) | 2019 | RCT | Infection and Drug Resistance | Sitafloxacino oral vs. ceftriaxona IV seguida de cefdinir oral em pielonefrite aguda e ITU complicada |
| [37414282](https://pubmed.ncbi.nlm.nih.gov/37414282/) | 2023 | Revisão sistemática | J Am Pharm Assoc | Cefalosporinas em pielonefrite não complicada; diretrizes recomendam ciprofloxacino ou SMX-TMP como primeira linha |
| [41160587](https://pubmed.ncbi.nlm.nih.gov/41160587/) | 2026 | Coorte | J Pharm Pract | Estudo retrospectivo em 3 hospitais comparando falha terapêutica de cefalexina e cefdinir como step-down em ITU grave |
| [42841836](https://pubmed.ncbi.nlm.nih.gov/42841836/) | 2026 | Coorte | Ann Emerg Med | Compara cefalosporinas orais de 1ª, 2ª e 3ª geração em pielonefrite de adultos liberados do pronto-socorro (DOGMA-ED) |
| [42565893](https://pubmed.ncbi.nlm.nih.gov/42565893/) | 2026 | Coorte retrospectiva nacional | Eur J Clin Microbiol Infect Dis | Cefalosporinas orais de 3ª geração, de menor e mais variável biodisponibilidade, vs. cefalexina/cefaclor em cistite não complicada |
| [38482607](https://pubmed.ncbi.nlm.nih.gov/38482607/) | 2024 | Coorte | J Antimicrob Chemother | Prescrição empírica para pielonefrite em 15 pronto-socorros dos EUA, com oportunidades de melhoria |
| [30119986](https://pubmed.ncbi.nlm.nih.gov/30119986/) | 2018 | Coorte | Am J Emerg Med | Cefalosporinas vs. fluoroquinolona ou SMX-TMP em pielonefrite em pronto-socorro comunitário |
| [36027632](https://pubmed.ncbi.nlm.nih.gov/36027632/) | 2022 | Coorte | Am J Emerg Med | Avaliação de antibióticos recomendados para ITU em pronto-socorros da fronteira EUA-México |
| [22010614](https://pubmed.ncbi.nlm.nih.gov/22010614/) | 2011 | Revisão | Am Fam Physician | Diagnóstico e tratamento da cistite aguda não complicada |
| [41769599](https://pubmed.ncbi.nlm.nih.gov/41769599/) | 2026 | Relato de caso | Cureus | Pielonefrite recorrente em quadriplegia e uso de cefdinir oral na presença de nefrolitíase |

## Considerações de Segurança

- **Contraindicações (base de conhecimento TxGNN, não texto de bula)**: colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações Medicamentosas**: foram identificadas 75 interações. As de nível moderado incluem antiácidos e sais minerais que contêm alumínio ou magnésio (hidróxido de alumínio, magaldrato, carbonato, hidróxido e óxido de magnésio), ferro e balsalazida. Há ainda interações de nível não classificado com, por exemplo, pantoprazol, omeprazol, lansoprazol, mesalazina, doxiciclina, vancomicina, metformina, morfina, prednisona e sinvastatina.
- **Observação adicional**: cefalosporinas podem causar, ocasionalmente, hemólise imune induzida por fármaco.

Para advertências e contraindicações da bula, consulte a bula; os dados da ANVISA ainda não estão disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão de maior pontuação (hiperamilasemia) e as demais de topo não têm mecanismo plausível, ensaios nem literatura, sendo L5. Para a pielonefrite, existe literatura observacional, uma revisão sistemática e um RCT em que o cefdinir aparece apenas como terapia de transição (L3), sem ensaio de fase 2/3 que teste o cefdinir para essa indicação. Além disso, o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), bloqueio atual para a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank.
- Para pielonefrite: estudos comparativos de cefdinir como step-down vs. alternativas, com desfechos de falha clínica e avaliação de exposição urinária.
- Avaliar a viabilidade regulatória, já que não há registro no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

