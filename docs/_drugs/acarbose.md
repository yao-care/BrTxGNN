---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acarbose: Do Diabetes Tipo 2 à Síndrome de Stiff-Limb Focal

## Resumo em Uma Frase

Acarbose é um inibidor das α-glucosidases intestinais, originalmente aprovado para o tratamento do **diabetes mellitus tipo 2** mediante a redução da absorção pós-prandial de glicose.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Stiff-Limb Focal (focal stiff limb syndrome)** como indicação de maior prioridade (score 99,65%), em uma avaliação multi-alvo que engloba **9 novas indicações previstas** — todas sem ensaios clínicos ou literatura de suporte registrados até a data de corte.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Diabetes mellitus tipo 2 |
| Nova Indicação Prevista (Rank 1) | Síndrome de Stiff-Limb Focal (focal stiff limb syndrome) |
| Pontuação de Previsão TxGNN | 99,65% |
| Nível de Evidência | L5 |
| Situação no Mercado de Taiwan | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados de mecanismo de ação (MOA) disponíveis neste pacote de evidências. Com base em conhecimento farmacológico consolidado, Acarbose é um pseudo-tetrassacarídeo que inibe competitivamente e de forma reversível as α-glucosidases intestinais (maltase, glucoamilase, sacarase) presentes na borda em escova do intestino delgado. Esse mecanismo retarda a digestão e absorção de carboidratos complexos, reduzindo o pico glicêmico pós-prandial sem estimular diretamente a secreção de insulina — tornando-o útil no manejo glicêmico do diabetes tipo 2 com perfil de segurança bem estabelecido.

A Síndrome de Stiff-Limb Focal é uma variante da Síndrome da Pessoa Rígida (SPS), mediada por autoanticorpos anti-GAD65 que comprometem neurônios GABAérgicos, provocando espasmos musculares focais. A SPS e o diabetes mellitus tipo 1 compartilham o antígeno GAD65 como alvo autoimune, criando uma associação epidemiológica bem documentada entre as duas condições no grafo de conhecimento biomédico. O TxGNN provavelmente identificou essa conexão através do caminho **"diabetes ← anticorpos anti-GAD65 ← SPS"**, atribuindo alta pontuação por co-ocorrência de comorbidade.

Contudo, essa associação é fundamentalmente epidemiológica, não terapêutica. Acarbose atua exclusivamente sobre enzimas digestivas luminais e não possui mecanismos de modulação imunológica, supressão de autoanticorpos ou ação GABAérgica conhecidos. A previsão reflete uma sobreposição de nó no grafo de conhecimento, não um fundamento mecanístico para o tratamento da SPS ou suas variantes.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Acarbose em Síndrome de Stiff-Limb Focal.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Acarbose em Síndrome de Stiff-Limb Focal.

---

## Análise Multi-Alvo — 9 Indicações Previstas

Este pacote de evidências cobre 9 indicações previstas simultaneamente pelo TxGNN. A tabela abaixo apresenta uma visão comparativa, incluindo a avaliação mecanística de cada candidato:

| Rank | Indicação | Pontuação TxGNN | Evidência | Decisão | Avaliação Mecanística |
|------|-----------|:--------------:|:---------:|:-------:|----------------------|
| 1 | Síndrome de Stiff-Limb Focal | 99,65% | L5 | Hold | Co-ocorrência anti-GAD65; sem mecanismo terapêutico direto |
| 2 | Síndrome da Pessoa Rígida Clássica | 99,65% | L5 | Hold | Mesma via anti-GAD65; tratamento atual (diazepam, baclofen, IVIG) sem relação com α-glucosidases |
| 3 | ⚠️ Síndrome de Disfunção Responsiva à Tiamina (TRMA) | 99,62% | L5 | **Hold** | **Sinal de segurança adverso** — Acarbose pode interferir na absorção intestinal de tiamina; avaliar como contraindicação |
| 4 | Opsismodisplasia | 99,62% | L5 | Hold | Sem relação com vias SHIP2/PI3K de sinalização óssea; provável viés de dados esparsos |
| 5 | Lipodistrofia Localizada por Fármacos | 99,24% | L5 | Hold | Inferência de segunda ordem via redução de insulina injetável; sem evidência direta |
| 6 | Lipodistrofia Centrífuga | 99,22% | L5 | Hold | Possível via resistência à insulina no KG; evidência extremamente fraca |
| 7 | Lipoatrofia Localizada por Pressão | 99,20% | L5 | Hold | Lesão puramente mecânica/isquêmica; nenhum mecanismo farmacológico identificado |
| 8 | Lipodistrofia Localizada Idiopática | 99,17% | L5 | Hold | Efeito de agrupamento de nós no KG; possível melhora de comorbidades metabólicas associadas |
| 9 | Agenesia Pancreática | 99,16% | L5 | Research Question | **Candidato mecanisticamente mais plausível** — Acarbose age na mucosa intestinal independentemente da função pancreática |

### ⚠️ Alerta de Segurança — Rank 3 (TRMA)

A indicação de Rank 3 não deve ser considerada candidata terapêutica. A Síndrome de Disfunção Responsiva à Tiamina (TRMA) é causada por mutação no gene *SLC19A2* (transportador de tiamina), exigindo suplementação contínua de vitamina B1. Evidências farmacológicas sugerem que Acarbose pode competir pelos transportadores intestinais de tiamina, agravando potencialmente a deficiência em portadores de TRMA. **Esta indicação deve ser incluída na revisão de contraindicações do fármaco.**

### Candidato com Maior Plausibilidade Mecanística — Rank 9 (Agenesia Pancreática)

A Agenesia Pancreática apresenta a justificativa mais coerente do conjunto:
- Pacientes carecem de função pancreática exócrina e endócrina (insulino-dependentes absolutos)
- Acarbose age diretamente nas α-glucosidases da mucosa intestinal, sendo **independente da presença do pâncreas**
- Poderia reduzir o pico glicêmico pós-prandial e, consequentemente, otimizar a dose de insulina exógena
- Ressalva: a ausência de enzimas pancreáticas exócrinas pode alterar a digestão de carboidratos de forma imprevisível, criando interação farmacodinâmica complexa com o mecanismo do Acarbose — avaliação clínica necessária

---

## Informações de Comercialização em Taiwan

O sistema TFDA confirma **4 registros ativos** para Acarbose em Taiwan com status **Comercializado**. Os detalhes individuais (números de registro, nomes comerciais, formas farmacêuticas e textos de indicação) não foram recuperados neste ciclo de coleta de dados.

> Para consultar os registros completos, acesse diretamente o [Sistema de Consulta de Medicamentos da TFDA](https://www.fda.gov.tw/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança completas, incluindo advertências, contraindicações e interações medicamentosas.

> **Nota sobre lacuna de dados**: A consulta de interações medicamentosas (DDI) retornou status "not_found" com 0 interações — isso pode refletir limitação da fonte consultada, não ausência real de interações. Acarbose possui interações conhecidas com digestivos enzimáticos e adsorventes intestinais que devem ser verificadas em fontes especializadas (DrugBank, Micromedex).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as 9 indicações previstas pelo TxGNN apresentam exclusivamente nível de evidência L5 (previsão computacional sem suporte clínico ou bibliográfico), e a maioria das conexões identificadas reflete associações epidemiológicas no grafo de conhecimento sem mecanismo terapêutico verificável para Acarbose. O único candidato com plausibilidade mecanística mínima (Agenesia Pancreática, Rank 9) ainda é classificado como "Research Question", exigindo investigação prospectiva antes de qualquer progressão.

**Para prosseguir, é necessário:**
- Recuperar os dados completos dos 4 registros TFDA (números de registro, indicações aprovadas, textos completos das bulas)
- Obter dados de MOA detalhados via API do DrugBank para confirmar interações enzimáticas e de transportadores relevantes
- **Investigar e formalizar o sinal de segurança em TRMA (Rank 3)** — avaliar interferência de Acarbose no transporte intestinal de tiamina e incluir na revisão de contraindicações
- Para a Agenesia Pancreática: elaborar protocolo de série de casos avaliando segurança, eficácia e interação com a ausência de amilase pancreática
- Realizar consulta de DDI em fontes secundárias especializadas (Micromedex, Lexicomp) para suprir a lacuna da consulta automatizada
- Completar dados de segurança (advertências, contraindicações) antes de qualquer avaliação de progressão para S1
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

