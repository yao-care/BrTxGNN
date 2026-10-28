---
layout: default
title: Methadone
parent: Evidência Moderada (L3-L4)
nav_order: 448
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-28
description: "Methadone: nova indicação prevista, Síndrome de Tourette (Tourette syndrome) (nível de evidência L4). Indicação original: Analgésicos narcóticos"
monitor_inn: "Methadone"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold"]
---

# Methadone
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **7** 
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

## Metadona: De analgésico narcótico para síndrome de Tourette
{: .text-alpha }

## Resumo em Uma Frase

A metadona é um analgésico opioide, registrado no Brasil na categoria de "analgésicos narcóticos".
O modelo TxGNN prevê que ela possa ser eficaz para a **Síndrome de Tourette (Tourette syndrome)**,
mas atualmente há **0 ensaios clínicos** e apenas **4 publicações** associadas a essa direção, sendo apenas uma delas diretamente sobre o tema (um relato de 1992).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgésicos narcóticos |
| Nova Indicação Prevista | Síndrome de Tourette (Tourette syndrome) |
| Pontuação de Previsão TxGNN | 0,9976 |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a metadona é um agonista de receptores opioides mu com atividade antagonista sobre receptores NMDA. Sua eficácia como analgésico está estabelecida, e mecanisticamente pode ser aplicável a transtornos de tiques.

A hipótese é que a modulação opioide de circuitos dopaminérgicos e estriatais possa influenciar a expressão dos tiques. A literatura recuperada menciona que opioides têm sido relatados como eficazes em casos refratários de TOC e de síndrome de Tourette, e que o comportamento relacionado ao receptor 5-HT2A (associado a tiques e compulsões) é modulado por opioides em modelos experimentais.

Ainda assim, o respaldo é frágil. O único item clínico direto é um relato de 1992 sobre tratamento de Tourette com metadona, que parece ser pequeno e não controlado. Os demais artigos (coreia, TOC, dor neuropática) são indiretos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Relato de caso / estudo aberto pequeno (não verificado) | Am J Psychiatry | Tratamento do transtorno de Tourette com metadona; sem resumo disponível |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Pré-clínico / Revisão | Psychopharmacology | Opioides atípicos em TOC; opioides são eficazes em TOC refratário e na síndrome de Tourette, com base em comportamento mediado por 5-HT2A |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Revisão | Curr Opin Neurol | Causas não genéticas de coreia; relevância indireta |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Revisão | Palliat Care Soc Pract | Novos fármacos para dor neuropática em câncer avançado; relevância indireta |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102980138 (cancelado) | MYTEDOM | Não informada | Analgésicos narcóticos |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: o grafo de conhecimento do TxGNN aponta contraindicação com síndrome do QT longo (inclusive familiar), torsades de pointes, parada cardíaca súbita, doença do sistema de condução cardíaca, insuficiência respiratória, asma, epilepsia, doença renal, doença hepática, doença da vesícula biliar, hipotireoidismo/mixedema, doença inflamatória intestinal, íleo paralítico, obstrução intestinal, hipertensão intracraniana, hipertrofia prostática benigna, hipotensão, estenose uretral e transtornos por uso de substâncias/dependência.
- **Interações Medicamentosas**: foram identificadas 100 interações no total (20 listadas nos dados). Entre as de nível **grave (Major)**: alvimopan, bupropiona, morfina, dexametasona, claritromicina, ácido picossulfúrico, polietilenoglicol (3350 com eletrólitos) e cisaprida. Há também diversas interações de nível moderado (por exemplo, famotidina, cimetidina, aprepitanto, atropina, loperamida, hiosciamina, glicopirrônio, diciclomina, bisacodil, óleo de rícino, attapulgita e clidínio).
- **Sinais de risco específicos para a previsão**: a literatura recuperada e o racional do modelo destacam risco de dependência opioide e prolongamento do intervalo QT, relevantes para uma condição crônica e frequentemente pediátrica como a síndrome de Tourette.

Consulte a bula para advertências e contraindicações oficiais, pois os dados de bula da ANVISA não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia em um único relato clínico antigo (1992), sem ensaios registrados, e o perfil de risco da metadona (dependência, QT longo, depressão respiratória) pesa fortemente contra o uso em uma condição crônica, frequentemente pediátrica. Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), atualmente indisponível
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank)
- Revisar o relato de 1992 (PMID 1728167) em texto completo para avaliar desenho, tamanho amostral e resultados
- Comparar com tratamentos já estabelecidos para tiques, que não envolvem risco de dependência
- Se houver interesse, planejar estudo pré-clínico ou ensaio controlado pequeno, com monitoramento de ECG (QT) e risco de dependência

---

**Observação sobre outras indicações previstas:** as demais previsões do modelo (síndrome nefrogênica de antidiurese inapropriada, tricotilomania, cefaleia, transtorno bipolar maníaco, cefaleia autonômica trigeminal, resfriado comum, enxaqueca, fibromialgia e miosite fibrosa) também receberam recomendação *Hold*. Para várias delas a literatura não sustenta eficácia: na cefaleia autonômica trigeminal há sinal de que a metadona pode induzir ou piorar a cefaleia em salvas, e no resfriado comum os artigos recuperados tratam de sensibilidade à dor pelo frio, sem relação com a doença.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

