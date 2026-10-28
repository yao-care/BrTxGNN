---
layout: default
title: Ritonavir
parent: Apenas Predição do Modelo (L5)
nav_order: 570
evidence_level: L5
indication_count: 3
monitor_inn: "RITONAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Ritonavir: nova indicação prevista, Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection) (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Ritonavir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Ritonavir: Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection)
{: .text-alpha }

## Resumo em Uma Frase

Ritonavir é um inibidor da protease do HIV, originalmente usado no tratamento da infecção por HIV/AIDS e da infecção pelo vírus da hepatite C (relações registradas no grafo de conhecimento do modelo).
O modelo TxGNN prevê que pode ser eficaz para **infecção pelo vírus da imunodeficiência símia (SIV)**, atualmente com **nenhum ensaio clínico** e **10 publicações** (todas pré-clínicas, in vitro ou de comentário) associadas a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection) |
| Pontuação de Previsão TxGNN | 0.9992 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 20) |
| Número de Registros | 20 (ativos: 5) |
| Decisão Recomendada | Hold |

Observação sobre o nível de evidência: as publicações disponíveis estudam o SIV em macacos e em cultura de células, ou sobre outros temas. Como não há ensaio clínico nem estudo que avalie diretamente o ritonavir como tratamento desta doença em contexto de indicação, o nível é limitado a L5, conforme a regra de teto de evidência.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o ritonavir é um inibidor da protease do HIV (e também um potente inibidor da enzima CYP3A4, usado para "reforçar" outros antirretrovirais). Sua eficácia em HIV está registrada no grafo de conhecimento, e mecanisticamente pode ser aplicável a lentivírus aparentados.

O SIV é um lentivírus muito próximo do HIV, com protease semelhante. Um estudo in vitro (PMID 12709355) mostrou que o SIVmac239 foi inibido pelo ritonavir com concentração efetiva de 50% de cerca de 13 nM, comparável à observada para o HIV-1 (cerca de 25 nM). Isso sustenta a plausibilidade biológica.

Porém, a pontuação alta do modelo provavelmente reflete a semelhança entre HIV e SIV, e não um novo sinal de reposicionamento. Trata-se essencialmente de um modelo animal da doença humana já tratada, com pouco valor clínico novo para humanos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Nenhuma das publicações é ensaio clínico randomizado; a maioria é pré-clínica em macacos ou in vitro.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 foi inibido por indinavir, saquinavir e ritonavir (ritonavir ≈ 13 nM vs. ≈ 25 nM para HIV-1) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | Avaliação da atividade de 16 antirretrovirais aprovados contra HIV-2, SIV e SHIV, com implicações para tratamento e profilaxia pós-exposição |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Pré-clínico (modelo animal) | mBio | Infecções por lentivírus persistem no cérebro apesar de terapia antirretroviral eficaz |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Pré-clínico (modelo animal) | PLoS Pathogens | Regime antirretroviral muito intensificado induziu supressão viral prolongada e restrição do reservatório em macacos com AIDS símia |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Pré-clínico (modelo animal) | PLoS One | Terapia antirretroviral supressiva combinada com SAHA em macacos rhesus chineses infectados por SIV |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Pré-clínico (modelo animal) | Journal of Virology | Queda viral rápida em macacos infectados por SIV com terapia antirretroviral quádrupla |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Pré-clínico (modelo animal) | J Virol Methods | Efeito da terapia oral (AZT, 3TC e lopinavir/ritonavir) sobre o subconjunto CD8 em macacos com SHIV |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Não classificado | Microbes and Infection | SHIV com protease derivada do HIV-1 como ferramenta para testar inibidores de protease em macacos |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro | Antivir Chem Chemother | Derivado de fluoroquinolona K-12 com atividade de amplo espectro, inclusive contra cepas de HIV-1 resistentes ao ritonavir |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro | J Virol | Processamento da proteína Vif do HIV-1 pela protease viral |

## Informações de Comercialização no Brasil

Há 20 registros no total, dos quais 5 válidos e 15 cancelados. Os registros não trazem texto de indicação aprovada nem forma farmacêutica nos dados compilados. Abaixo, os registros válidos de ritonavir isolado; o registro de Kaletra e o de lopinavir + ritonavir são produtos de associação, e o de Paxlovid é uma associação com nirmatrelvir, portanto não descrevem a aprovação do ritonavir isolado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102980437 | Ritonavir (Cristália) | Não informada | Não informada nos dados compilados |
| Registro 101830153 | Ritonavir (LAFEPE) | Não informada | Não informada nos dados compilados |

Registros válidos de produtos em associação (apenas para referência): Kaletra (198600010), Lopinavir + Ritonavir (102980436) e Paxlovid (121100496).

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (relações do grafo, não texto de bula): síndrome do QT longo (inclusive familiar), torsades de pointes, parada cardíaca súbita, doenças de condução cardíaca e bloqueio atrioventricular, cardiomiopatias, isquemia miocárdica e doença arterial coronariana, pancreatite, doença hepática e cirrose, doença da vesícula biliar, hiperglicemia, diabetes mellitus e cetoacidose diabética, deficiência de potássio, hepatite B crônica, hiperuricemia e gota, hipertrigliceridemia e hiperlipidemias familiares, hiperbilirrubinemia (inclusive síndrome de Gilbert) e hemofilia.
- **Interações medicamentosas**: foram identificadas 100 interações; entre as principais listadas estão as de nível **maior** com loperamida, triancinolona e budesonida. Há interações de nível moderado com, por exemplo, metformina, acarbose, alogliptina, dexametasona, hidrocortisona, betametasona, claritromicina, metronidazol, bupropiona, aprepitanto, canagliflozina e clorpropamida. O ritonavir é um forte inibidor da CYP3A4, o que explica boa parte dessas interações.

As advertências e contraindicações da bula brasileira não estavam disponíveis nos dados compilados; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se refere a uma infecção de primatas não humanos, essencialmente um modelo animal do HIV, que o ritonavir já trata no contexto humano. Não há ensaios clínicos, e as evidências são pré-clínicas, o que resulta em nível L5 e oferece pouco valor novo de reposicionamento para humanos.

**Para prosseguir, é necessário:**
- Definir se há interesse real (por exemplo, uso do SIV como modelo de pesquisa) que justifique avançar
- Dados do mecanismo de ação do fármaco
- Texto de bula da ANVISA com advertências e contraindicações
- Estudos que avaliem diretamente o ritonavir na doença prevista
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

