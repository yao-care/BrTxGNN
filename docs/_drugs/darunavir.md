---
layout: default
title: Darunavir
parent: Apenas Predição do Modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 4
monitor_inn: "DARUNAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Darunavir: nova indicação prevista, Infecção pelo vírus da imunodeficiência símia (nível de evidência L5). Indicação original: Infecção por HIV e AIDS"
---

# Darunavir
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

## Darunavir: Da infecção por HIV à infecção pelo vírus da imunodeficiência símia
{: .text-alpha }

## Resumo em Uma Frase

Darunavir é um inibidor da protease do HIV-1, originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que pode ser eficaz para **infecção pelo vírus da imunodeficiência símia (SIV)**, atualmente com **0 ensaios clínicos** e **4 publicações** (todas em modelos pré-clínicos com primatas não humanos) apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV e AIDS (relação registrada no grafo de conhecimento; os textos de indicação dos registros na ANVISA não estavam preenchidos) |
| Nova Indicação Prevista | Infecção pelo vírus da imunodeficiência símia |
| Pontuação de Previsão TxGNN | 0,9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 6) |
| Número de Registros | 6 (ativos: 6) |
| Decisão Recomendada | Hold |

O nível L5 se justifica porque nenhum estudo citado examina o darunavir isoladamente contra essa doença: os estudos em macacos usam regimes combinados de antirretrovirais, e não há ensaios clínicos registrados.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o darunavir é um inibidor da protease do HIV-1, e sua relação com o HIV/AIDS está registrada no grafo de conhecimento. Mecanisticamente, a previsão pode ser aplicável ao SIV.

O SIV é um lentivírus intimamente relacionado ao HIV, com protease estruturalmente semelhante. Isso torna plausível a lógica do mecanismo e explica a pontuação alta do modelo.

Há uma ressalva importante: o SIV é usado principalmente como **modelo animal** do HIV. Os estudos recuperados são com macacos rhesus, nos quais o darunavir foi um componente de regimes combinados de terapia antirretroviral (cART), voltados a investigar reservatórios virais e sua persistência, junto a agentes adjuntos como auranofina e um inibidor de histona desacetilase. Não se trata, portanto, de uma nova indicação humana, e a evidência é indireta.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Pré-clínico (primata não humano) | PloS one | Macacos rhesus chineses infectados por SIV tratados com cART intensiva e 3 semanas do inibidor de histona desacetilase SAHA, para estudar reservatórios virais |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Pré-clínico (primata não humano) | AIDS Res Hum Retroviruses | Comparação de dois regimes injetáveis coformulados de cART em macacos rhesus infectados por SIVmac239 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Pré-clínico (primata não humano) | AIDS | A auranofina restringiu o reservatório viral no modelo de AIDS em macacos e favoreceu o controle da carga viral após a suspensão da terapia |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Pré-clínico (primata não humano) | PLoS Pathogens | Regime antirretroviral altamente intensificado induziu supressão viral de longo prazo e restrição do reservatório em modelo de AIDS símia |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 188300114 | Darunavir (Viatris) | Não informada | Texto de indicação não disponível |
| Registro 112330056 | Darunavir (Laboratório Químico Farmacêutico da Aeronáutica) | Não informada | Texto de indicação não disponível |
| Registro 112363387 | Prezista | Não informada | Texto de indicação não disponível |
| Registro 112363434 | Symtuza® | Não informada | Texto de indicação não disponível |
| Registro 101830156 | Darunavir (LAFEPE) | Não informada | Texto de indicação não disponível |

Há ainda o registro 102980571 (Darvyr, Cristália), totalizando 6 registros válidos. Todos constam como produtos de princípio ativo único.

---

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não provêm do texto da bula): insuficiência hepática, doença hepática, cirrose, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, infecção crônica por hepatite C e B, hipertrigliceridemia e hemofilia.
- **Interações medicamentosas** (100 interações identificadas; principais exemplos):
  - **Grave**: cisaprida.
  - **Moderadas**: antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, canagliflozina, dapagliflozina, saxagliptina, clorpropamida, albiglutida), corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), aprepitanto e claritromicina.

Para advertências e contraindicações formais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia em similaridade biológica entre HIV e SIV, mas as evidências vêm de modelos animais em que o darunavir fazia parte de regimes combinados, sem estudo que o isole. O SIV não é uma indicação humana, e o uso já coberto no HIV não representa um novo reposicionamento clínico.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação do darunavir (DrugBank).
- Definir se há uma questão de pesquisa relevante (por exemplo, uso em modelos animais de pesquisa) que justifique avançar, já que não há aplicação clínica humana.
- Estudos específicos de atividade do darunavir isolado contra a protease do SIV.
- Bula da ANVISA com advertências e contraindicações formais, ainda não analisada.

**Observação sobre as demais previsões:** infecção por imunodeficiência felina (veterinária, sem estudos), um transtorno do neurodesenvolvimento raro (sem vínculo mecanístico plausível) e hiperlipidemia combinada familiar obsoleta (o darunavir tende a elevar lipídios, e não a reduzi-los) também ficaram em L5 e Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

