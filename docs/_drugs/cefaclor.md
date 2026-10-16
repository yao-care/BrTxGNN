---
layout: default
title: Cefaclor
parent: Apenas Predição do Modelo (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefaclor: nova indicação prevista, polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade poli… (nível de evidência L5). Indicação original: Infecção do trato urinário, amigdalite, faringit…"
monitor_inn: "Cefaclor"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "Ureaplasma urethritis", "gonococcal urethritis", "congenital analbuminemia", "blood group incompatibility", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "premalignant hematological system disease", "monoclonal gammopathy"]
---

# Cefaclor
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Cefaclor: Das infecções bacterianas ao tratamento da uretrite gonocócica

## Resumo em Uma Frase

Cefaclor é uma cefalosporina de segunda geração, originalmente usada em infecções do trato urinário, infecções respiratórias (faringite, amigdalite, pneumonia) e infecções estreptocócicas e estafilocócicas.
O modelo TxGNN prevê que pode ser eficaz para **polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade policlonal)**, a previsão de maior pontuação, mas sem nenhum respaldo clínico. A previsão com mais evidências é a **uretrite gonocócica (gonococcal urethritis)**, apoiada por **6 publicações** (1979–1997) e **nenhum ensaio clínico** registrado.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção do trato urinário, amigdalite, faringite, pneumonia e outras infecções respiratórias e estreptocócicas/estafilocócicas (conforme o grafo de conhecimento; não há texto de bula disponível) |
| Nova Indicação Prevista | polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade policlonal) |
| Pontuação de Previsão TxGNN | 97,70% |
| Nível de Evidência | L5 (para a indicação de maior pontuação) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

> **Observação:** a previsão de maior pontuação (hiperviscosidade policlonal) não tem plausibilidade mecanística. A candidata com respaldo na literatura é a uretrite gonocócica (pontuação de 97,48%, nível L3), detalhada abaixo.

## Por que Esta Previsão É Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o cefaclor é uma cefalosporina de segunda geração que inibe a síntese da parede celular bacteriana, e sua eficácia em infecções urinárias e respiratórias é reconhecida.

**Hiperviscosidade policlonal (maior pontuação):** a síndrome decorre do excesso de imunoglobulinas, e não de infecção bacteriana. Não há ligação mecanística plausível; a pontuação elevada (0,977) reflete proximidade no grafo, sem apoio clínico ou da literatura. O mesmo vale para hiperamilasemia, analbuminemia congênita, incompatibilidade de grupo sanguíneo, doenças hematológicas pré-malignas e gamopatia monoclonal.

**Uretrite gonocócica (candidata mais sustentada):** como beta-lactâmico, o cefaclor inibe as proteínas ligadoras de penicilina e tem atividade contra *Neisseria gonorrhoeae*, o que torna o mecanismo plausível e coerente com a indicação original em infecções do trato urinário. Já a **uretrite por Ureaplasma** é provavelmente um artefato do grafo: esses microrganismos não têm parede celular, então os beta-lactâmicos tendem a ser ineficazes. Outras previsões de natureza infecciosa (doença inflamatória uterina e pielonefrite xantogranulomatosa) têm apenas ligação indireta e sem evidências.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para **uretrite gonocócica** (a classificação dos desenhos de estudo foi inferida apenas pelos títulos, portanto é provisória):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Estudo clínico comparativo randomizado | Br J Vener Dis | 400 homens; taxas de cura de 98,9% (espectinomicina), 70,8% (cefamandol), 95,8% (cefaclor 3 g + probenecida) e 89,6% (cefaclor 3 g isolado) |
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Estudo randomizado / série de casos | Sex Transm Dis | Cefaclor 2, 3 e 4 g, com ou sem probenecida, por 3 dias, em uretrite gonocócica não complicada em homens; cura avaliada por cultura no dia 7 |
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Estudo clínico controlado | Postgrad Med J | 40 homens com uretrite gonocócica não complicada receberam cefaclor com dose de ataque de 1 g; boa atividade in vitro contra *N. gonorrhoeae* |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Estudo clínico | Genitourin Med | Reavaliação da eficácia in vivo e in vitro do cefaclor como alternativa às cefalosporinas de terceira geração em países em desenvolvimento |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Estudo clínico de dose única | Med J Malaysia | Cefaclor oral em dose única em homens com uretrite gonocócica não complicada (sem resumo disponível) |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Relato de experiência clínica (outro fármaco) | Curr Med Res Opin | Relevância indireta: estudo do cefetamet pivoxil, com o cefaclor como um dos comparadores |

As demais indicações previstas não têm literatura associada.

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não o texto da bula):** colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas:** foram identificadas 69 interações. As de gravidade **moderada** são: balsalazida, ácido picossulfúrico, hidróxido de magnésio e hidróxido de alumínio. Há outras de gravidade não classificada, como calcitriol, pantoprazol, mesalazina, doxiciclina, morfina, metformina, omeprazol, lansoprazol, cimetidina, triancinolona, prednisona, sinvastatina, nistatina, hidrocortisona, diciclomina e loperamida.

Consulte a bula para as advertências e contraindicações completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão de maior pontuação (hiperviscosidade policlonal) e as demais previsões não infecciosas não têm base mecanística nem evidências (L5). A uretrite gonocócica tem literatura (L3, provisório), mas os dados são antigos (1979–1997), a resistência gonocócica atual e as diretrizes baseadas em ceftriaxona limitam a aplicabilidade, e o fármaco não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada por essa lacuna
- Obter dados do mecanismo de ação no DrugBank
- Confirmar os desenhos dos estudos de uretrite gonocócica pela leitura dos textos completos
- Avaliar dados atuais de suscetibilidade de *N. gonorrhoeae* ao cefaclor e as diretrizes vigentes
- Avaliar a viabilidade regulatória, já que não há registro no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

