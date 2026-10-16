---
layout: default
title: Saquinavir
parent: Apenas Predição do Modelo (L5)
nav_order: 579
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Saquinavir: nova indicação prevista, Infecção pelo vírus da imunodeficiência símia (simian immunodeficienc… (nível de evidência L5). Indicação original: HIV (infecção pelo HIV) e AIDS"
monitor_inn: "SAQUINAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "AIDS related complex", "congenital human immunodeficiency virus"]
---

# Saquinavir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

# Saquinavir: Da infecção por HIV/AIDS à infecção pelo vírus da imunodeficiência símia

## Resumo em Uma Frase

Saquinavir é um inibidor da protease do HIV-1, originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que pode ser eficaz para **infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection)**, mas essa previsão tem apoio apenas de **4 publicações pré-clínicas** e **nenhum ensaio clínico**. A previsão reflete sobretudo a proximidade biológica com a indicação original, e não um novo uso terapêutico em humanos.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | HIV (infecção pelo HIV) e AIDS (indicação obtida do grafo de conhecimento, pois não há registros no Brasil) |
| Nova Indicação Prevista | Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L4 (apenas estudos pré-clínicos e de mecanismo) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o saquinavir é um inibidor da protease do HIV-1: ele bloqueia a maturação de partículas virais infecciosas. Sua eficácia na infecção por HIV e na AIDS está comprovada, e mecanisticamente pode ser aplicável a outros lentivírus com protease semelhante.

A protease do vírus da imunodeficiência símia (SIV) é estruturalmente relacionada às proteases do HIV-1 e do HIV-2. Um estudo in vitro mostrou que o SIVmac239 é inibido pelo saquinavir com concentração efetiva de 50% de cerca de 55 nM, valor próximo ao observado para o HIV-1 (cerca de 47 nM). Isso torna a atividade plausível.

É importante ressaltar que o SIV é um vírus de modelo animal. Não existe indicação clínica humana nem ensaios em humanos. A pontuação alta do TxGNN reflete principalmente a semelhança com a indicação original (HIV), e não um uso terapêutico novo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | Estudo de suscetibilidade in vitro | Antimicrob Agents Chemother | SIVmac239 foi inibido por indinavir, saquinavir e ritonavir, com potência semelhante à observada para o HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Estudo de suscetibilidade in vitro | Antivir Ther | Avaliação da atividade de 16 fármacos aprovados contra HIV-2, SIV e SHIV, com implicações para tratamento e profilaxia pós-exposição |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Pré-clínico (primata não humano) | J Infect Dis | Macacos infectados com SIV tratados com terapia antirretroviral altamente ativa (HAART) tiveram menor replicação viral e inflamação no sistema nervoso central, mas o DNA viral persistiu |
| [16809296](https://pubmed.ncbi.nlm.nih.gov/16809296/) | 2006 | Pré-clínico (estrutura/função da protease) | J Virol | Papel do resíduo invariante Thr80 na estrutura, função e infectividade da protease do HIV-1 |

## Citotoxicidade

Esta seção não se aplica: o saquinavir é um antirretroviral, não um antineoplásico.

## Considerações de Segurança

Os dados de advertências e contraindicações da bula não estavam disponíveis. Consulte a bula para essas informações.

- **Contraindicações (segundo o grafo de conhecimento, não texto de bula)**: síndrome do QT longo (incluindo a forma familiar), torsades de pointes, bloqueio atrioventricular, insuficiência hepática, doença hepática, cirrose, hepatite B e C crônicas, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, deficiência de potássio, hipertrigliceridemia, hemofilia (incluindo a forma sintomática em portadoras) e abuso/dependência de substâncias.
- **Interações Medicamentosas**: 100 interações foram identificadas. Entre as listadas, as de gravidade **maior** são com **triancinolona**, **budesonida** e **claritromicina**. Há ainda várias de gravidade **moderada**, incluindo antidiabéticos (acarbose, metformina, alogliptina, canagliflozina, clorpropamida, albiglutida), inibidores da bomba de prótons e antiácidos (omeprazol, rabeprazol, famotidina), corticosteroides (hidrocortisona, dexametasona, betametasona), aprepitanto, loperamida e bisacodil.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A indicação prevista (SIV) é uma condição de modelo animal, sem uso clínico humano e sem ensaios, e apoiada apenas por estudos pré-clínicos (L4). O fármaco não é comercializado no Brasil.

**Outras indicações previstas avaliadas:**
- **AIDS related complex (L1, Hold)** e **HIV congênito (L3, Hold)** são extensões da indicação original, não reposicionamento real. Há ensaios de Fase 2 e um de Fase 3 (NCT00002334, 3.000 participantes), mas são da década de 1990, em regimes combinados. A contribuição isolada do saquinavir não é separável nos dados. Antirretrovirais mais novos o substituíram.
- **AIDS felina**, **transtorno do neurodesenvolvimento raro** e **hiperlipidemia combinada familiar (obsoleta)** são previsões sem evidências. As duas primeiras não têm vínculo mecanístico plausível com um inibidor da protease do HIV. A última tem direção de efeito desfavorável, pois inibidores de protease causam dislipidemia.

**Para prosseguir, é necessário:**
- Obter o texto da bula da ANVISA (advertências e contraindicações), lacuna bloqueante para a triagem de segurança.
- Complementar os dados do mecanismo de ação (por exemplo, via DrugBank).
- Reavaliar se há relevância humana ou veterinária para a indicação prevista; sem ela, não há valor de reposicionamento a perseguir.
- Considerar o risco cardiovascular (prolongamento do QT) e as muitas interações medicamentosas em qualquer plano futuro.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

