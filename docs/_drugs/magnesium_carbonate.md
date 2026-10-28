---
layout: default
title: Magnesium Carbonate
parent: Apenas Predição do Modelo (L5)
nav_order: 431
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
monitor_inn: "MAGNESIUM CARBONATE"
predicted_indications: ["gastroduodenitis", "gastroparesis (disease)", "stomach disease", "duodenal obstruction"]
description: "Magnesium Carbonate: nova indicação prevista, Gastroduodenitis (nível de evidência L5). Indicação original: ANALGESICOS NAO NARCOTICOS"
---

# Magnesium Carbonate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Magnesium Carbonate: Gastroduodenitis
{: .text-alpha }

## Resumo em Uma Frase

Carbonato de magnésio é um sal de magnésio usado como antiácido e em associações analgésicas não narcóticas, com registros hoje todos cancelados no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **doença ulcerosa péptica ativa (active peptic ulcer disease)**,
mas há **0 ensaios clínicos** e apenas **1 publicação** (um estudo in vitro) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANALGESICOS NAO NARCOTICOS; ANTIACIDO |
| Nova Indicação Prevista | Gastroduodenitis |
| Pontuação de Previsão TxGNN | 0.9994 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o carbonato de magnésio é um antiácido: neutraliza o ácido clorídrico gástrico, elevando o pH do estômago. Sua indicação como antiácido consta em um dos registros da ANVISA.

A úlcera péptica é uma doença relacionada à acidez gástrica, e o alívio dos sintomas por neutralização ácida é mecanisticamente coerente. Na prática, a previsão é mais uma **extensão da indicação antiácida existente** do que um reposicionamento verdadeiramente novo.

A única publicação recuperada é uma avaliação in vitro da capacidade de neutralização ácida de antiácidos comercializados no Marrocos. Trata-se de evidência indireta, sem desfechos clínicos, como cicatrização da úlcera.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro / avaliação de qualidade de produto | Medicine and Pharmacy Reports | Avaliou a capacidade de neutralização ácida e outras propriedades de antiácidos comercializados no Marrocos; não mede resultados clínicos |

### Outras indicações previstas (resumo)

Outras previsões do modelo têm evidências igualmente fracas:

| Indicação prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Gastroduodenite | 0,9994 | L4 | Apenas modelo in vitro de estômago-duodeno artificial |
| Gastroparesia | 0,9969 | L5 | Distúrbio de motilidade; neutralização ácida não se aplica |
| Doença gástrica | 0,9959 | L4 | Categoria ampla, sobreposta à indicação antiácida atual |
| Obstrução duodenal | 0,9935 | L5 | Condição mecânica; sem papel terapêutico plausível |

## Informações de Comercialização no Brasil

Os 2 registros estão válidos.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 135690647 | SOMALGIN CARDIO | Não informada | Analgésicos não narcóticos |
| Registro nº 137640180 | MAGNESIA BISURADA | Não informada | Antiácido |

## Considerações de Segurança

- **Contraindicações (base de conhecimento TxGNN/PrimeKG, não texto de bula)**: o grafo associa o fármaco a contraindicações em doenças como insuficiência hepática, doença hepática, encefalopatia hepática, doença renal, nefrocalcinose, hipercalcemia, hiperparatireoidismo, porfirias, sarcoidose, doença da vesícula biliar, trombocitopenia, neutropenia, agranulocitose, anemias, diarreia, transtornos de ansiedade, apneia do sono e dependência de substâncias. Esses itens devem ser confirmados em fontes oficiais, pois não provêm de bula.
- **Interações Medicamentosas** (100 interações identificadas; exemplos):
  - **Maior**: dolutegravir.
  - **Moderada**: doxiciclina, alendronato, risedronato, colecalciferol, atazanavir, azitromicina, ácido acetilsalicílico, atropina, acalabrutinibe, anfetamina, baloxavir marboxil, benzfetamina.
  - **Menor**: famotidina, ranitidina, alprazolam, atenolol, acebutolol, axitinibe, benazepril.

Para advertências e contraindicações em bula, consulte a bula do medicamento.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (0,9994), mas as evidências se limitam a um estudo in vitro (L4), sem nenhum ensaio clínico. A indicação é essencialmente uma extensão do uso antiácido já conhecido, e os 2 registros no Brasil estão válidos. O tratamento atual da úlcera péptica se baseia em inibidores da bomba de prótons e erradicação do *H. pylori*.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) a partir do DrugBank
- Bulas da ANVISA (advertências e contraindicações), ainda não analisadas
- Estudos clínicos que avaliem desfechos de cicatrização ou sintomas de úlcera com carbonato de magnésio
- Avaliação do interesse comercial e regulatório, dado o cancelamento dos registros
- Revisão das interações medicamentosas (especialmente com dolutegravir, tetraciclinas e bifosfonatos) e das contraindicações em insuficiência renal e hepática
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

