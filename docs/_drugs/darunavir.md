---
layout: default
title: Darunavir
parent: Apenas Predição do Modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 4
monitor_inn: "DARUNAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-24
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

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Darunavir (tradução não oficial): “O darunavir é um medicamento antiviral contra o HIV-1. […] O darunavir é um inibidor da protease do HIV-1. Ele inibe seletivamente a clivagem das poliproteínas Gag-Pol codificadas pelo HIV-1 em células infectadas, impedindo assim a formação de partículas virais maduras.” Texto original em inglês: "Darunavir is an HIV-1 antiviral drug. […] Darunavir is an inhibitor of the HIV-1 protease. It selectively inhibits the cleavage of HIV-1 encoded Gag-Pol polyproteins in infected cells, thereby preventing the formation of mature virus particles." ([DailyMed: Prezista (darunavir) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814301f9-c990-46a5-b481-2879a521a16f), versão de 2025-08-29; acessado em 2026-11-19). Segundo informações conhecidas, o darunavir é um inibidor da protease do HIV-1, e sua relação com o HIV/AIDS está registrada no grafo de conhecimento. Mecanisticamente, a previsão pode ser aplicável ao SIV.

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

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101830156 | DARUNAVIR | LABORATORIO FARMACEUTICO DO ESTADO DE PERNAMBUCO G | Ativo |
| 102980571 | DARVYR | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 112330056 | DARUNAVIR | LABORATORIO QUIMICO FARMACEUTICO DA AERONAUTICA | Ativo |
| 112363387 | PREZISTA | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 112363434 | SYMTUZA® | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 188300114 | DARUNAVIR | VIATRIS FARMACEUTICA DO BRASIL LTDA | Ativo |

<!-- licenses:end -->

<!-- review:begin br-lic-20261124b-darunavir-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “Há ainda o registro 102980571 (Darvyr, Cristália), totalizando 6 registros válidos.” Removido: a frase descrevia quantos registros a tabela antiga mostrava; a tabela de registros desta seção agora é gerada por programa a partir dos dados abertos de medicamentos da ANVISA (os ativos primeiro), e os números atualizados estão no resumo rápido. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124b-darunavir-1 -->

 Todos constam como produtos de princípio ativo único.

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

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Prezista (darunavir) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814301f9-c990-46a5-b481-2879a521a16f) |
| 2026-11-24 | Removido: “Há ainda o registro 102980571 (Darvyr, Cristália), totalizando 6 registros válidos.” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

