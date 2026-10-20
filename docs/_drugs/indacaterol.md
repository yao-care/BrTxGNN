---
layout: default
title: Indacaterol
parent: Evidência Alta (L1-L2)
nav_order: 366
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Indacaterol: nova indicação prevista, Doença Brônquica (Bronchial Disease) (nível de evidência L1). Indicação original: Não disponível nos dados de registro compilados"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
{: .fs-9 }

Nível de evidência: **L1** | Indicações previstas: **10** 
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

# Indacaterol: Da indicação original não registrada à doença brônquica

## Resumo em Uma Frase

Indacaterol é um agonista beta-2 adrenérgico inalatório de ultra-longa duração, utilizado em doenças obstrutivas das vias aéreas. Os dados compilados para este relatório não trazem indicação original registrada na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **Doença Brônquica (Bronchial Disease)**, atualmente com **22 ensaios clínicos** e **20 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro compilados |
| Nova Indicação Prevista | Doença Brônquica (Bronchial Disease) |
| Pontuação de Previsão TxGNN | 99,18% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

**Observação sobre a seleção da indicação:** a primeira previsão do modelo (síndrome nefrogênica de antidiurese inapropriada, 99,54%) e as demais com pontuação superior não têm nenhum ensaio ou publicação, e foram classificadas como L5 / Hold. Este relatório foca na previsão de Doença Brônquica (7ª na classificação), a única com evidências reais. Para as previsões sem evidência, não há racional mecanístico plausível nos dados compilados (por exemplo, cefaleia pode ser inclusive um efeito adverso de agonistas beta).

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o indacaterol é um agonista beta-2 adrenérgico de ultra-longa duração (ultra-LABA), que relaxa a musculatura lisa brônquica pela via do AMPc, permitindo administração uma vez ao dia.

A relação com a nova indicação é direta: a broncodilatação é o efeito farmacológico central do fármaco, e a literatura o descreve para doenças obstrutivas das vias aéreas, principalmente asma e DPOC. A maior parte dos ensaios avalia o indacaterol em asma, isolado ou em combinações de dose fixa (indacaterol/mometasona e indacaterol/glicopirrônio/mometasona).

Ressalvas: "doença brônquica" é uma categoria ampla, e as evidências se concentram em asma e DPOC. Além disso, os dados indicam "não comercializado" e ausência de indicação original, o que conflita com a literatura publicada (inclusive com a aprovação de combinações na União Europeia) e deve ser verificado nas bases regulatórias da ANVISA.

## Evidências de Ensaios Clínicos

Foram identificados 22 ensaios; abaixo, os 10 mais relevantes.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Concluído | 2216 | QMF149 (indacaterol/mometasona) vs. mometasona em 52 semanas em asma mal controlada: eficácia e segurança |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Concluído | 511 | Eficácia broncodilatadora de 14 dias do indacaterol vs. placebo e salmeterol em asma persistente |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Concluído | 805 | Segurança de indacaterol (300 e 600 µg) vs. salmeterol por 26 semanas em asma moderada a grave |
| [NCT04259164](https://clinicaltrials.gov/study/NCT04259164) | Phase 3 | Concluído | 28 | Efeito anti-inflamatório do glicopirrônio adicionado a indacaterol/mometasona na resposta asmática tardia induzida por alérgeno |
| [NCT00403637](https://clinicaltrials.gov/study/NCT00403637) | Phase 2/3 | Concluído | 45 | Indacaterol (150, 300, 600 µg) vs. placebo e formoterol: eficácia broncodilatadora em dose única |
| [NCT00545272](https://clinicaltrials.gov/study/NCT00545272) | Phase 2 | Concluído | 392 | Estudo de dose-resposta de 14 dias com 4 doses de indacaterol vs. placebo e formoterol |
| [NCT01156844](https://clinicaltrials.gov/study/NCT01156844) | Phase 2 | Concluído | 191 | Três regimes de indacaterol inalado vs. placebo em asma persistente: eficácia broncodilatadora |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Concluído | 335 | Indacaterol acetato (75 e 150 µg) por 12 semanas em asma persistente, para apoiar a seleção de dose da combinação QMF149 |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Concluído | 79 | Indacaterol acetato (75 e 150 µg) em crianças de 6 a 11 anos com asma, por 2 semanas |
| [NCT01959412](https://clinicaltrials.gov/study/NCT01959412) | Phase 2 | Concluído | 91 | Cinco doses de indacaterol inalado em asma persistente, em estudo cruzado controlado por placebo |

O ensaio NCT04206761 (Phase 3, QVM149) foi retirado, com 0 participantes, e não fornece evidência utilizável.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT (Phase 3, IRIDIUM) | Lancet Respir Med | Combinação uma vez ao dia de mometasona-indacaterol-glicopirrônio vs. ICS-LABA em asma inadequadamente controlada |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | RCT / revisão | Expert Rev Respir Med | Combinação de dose fixa indacaterol/glicopirrônio/mometasona em asma moderada a grave |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Revisão | Drugs | Revisão da combinação tripla (Enerzair Breezhaler), aprovada na UE para manutenção em asma não controlada |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Revisão | Respir Med | Ultra-LABAs (incluindo indacaterol) em asma; uso apenas associado a corticosteroide inalatório |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revisão | Am J Respir Crit Care Med | Terapia com agonistas beta-2 em doenças pulmonares |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Revisão | Pharmacol Rev | Farmacologia e terapêutica de broncodilatadores, pilares do tratamento de DPOC e asma |
| [22499359](https://pubmed.ncbi.nlm.nih.gov/22499359/) | 2012 | Revisão | Pharmacotherapy | Indacaterol como beta-2 agonista de ultra-longa duração para DPOC |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Revisão | Adv Ther | Broncodilatação rápida e sustentada em DPOC e asma de diferentes gravidades |
| [40887869](https://pubmed.ncbi.nlm.nih.gov/40887869/) | 2025 | Pré-clínico / farmacologia molecular | Pharmacol Res Perspect | Comparação das propriedades farmacológicas de agonistas beta-2 curtos, longos e ultra-longos |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Estudo de ponte de dose | Pulm Pharmacol Ther | Ponte de doses de mometasona nas combinações de dose fixa com indacaterol em asma |

## Considerações de Segurança

- **Contraindicações baseadas no grafo de conhecimento (não oriundas de bula):** hipertensão, síndrome do QT longo (inclusive familiar), epilepsia, hiperglicemia, deficiência de potássio, diabetes mellitus, cetoacidose diabética, parada cardíaca súbita, doenças de condução cardíaca, tireotoxicose/hipertireoidismo/doença de Graves e doença arterial coronariana.
- **Interações medicamentosas:** foram identificadas 100 interações; as listadas incluem principalmente nível moderado, como antidiabéticos (acarbose, metformina, pioglitazona, canagliflozina, dapagliflozina, alogliptina, saxagliptina, albiglutida, clorpropamida), epinefrina, isometepteno, famotidina e claritromicina. Corticosteroides (hidrocortisona, triancinolona, dexametasona, beclometasona, betametasona, budesonida) e aprepitanto têm nível leve.
- Como classe, os agonistas beta exigem atenção a efeitos cardiovasculares, hipocalemia e hiperglicemia, além do uso de LABA em asma sempre associado a corticosteroide inalatório.

Consulte a bula para as advertências e contraindicações formais, pois essas informações não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há múltiplos ensaios de Phase 3 concluídos e um RCT de Phase 3 publicado (IRIDIUM) apoiando o uso do indacaterol, principalmente em combinação, em asma, com mecanismo diretamente plausível (nível L1). A ausência de registro na ANVISA e a amplitude da categoria "doença brônquica" justificam cautela.

**Para prosseguir, é necessário:**
- Verificar a situação regulatória real na ANVISA, pois o "não comercializado" conflita com a literatura.
- Definir a indicação específica (asma e/ou DPOC), a formulação (monoterapia ou combinação) e a via de administração.
- Obter as advertências e contraindicações da bula da ANVISA, e os dados de mecanismo de ação no DrugBank.
- Elaborar um plano de monitoramento cardiovascular e metabólico, considerando as contraindicações do grafo de conhecimento.
- Manter as demais previsões (nível L5) em Hold, até que surja evidência clínica ou mecanística.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

