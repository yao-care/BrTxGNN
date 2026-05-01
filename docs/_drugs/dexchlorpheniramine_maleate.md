---
layout: default
title: Dexchlorpheniramine Maleate
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Dexchlorpheniramine Maleate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Usando o skill `txgnn-pipeline` para orientação de contexto. Agora vou analisar o Evidence Pack e gerar o relatório completo.

---

# Dexchlorpheniramine Maleate: Do Tratamento de Alergias à Porfiria Intermitente Aguda

## Resumo em Uma Frase

Dexchlorpheniramine maleate é o enantiômero dextrogiro da clorfeniramina, um anti-histamínico H1 de primeira geração amplamente utilizado no controle de reações alérgicas como rinite alérgica e urticária.
O modelo TxGNN prevê como principal nova indicação a **Porfiria Intermitente Aguda (Acute Intermittent Porphyria)**, com pontuação de 99,12%, porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Anti-histamínico H1 de primeira geração — sem registro ativo no Brasil |
| Nova Indicação Prevista | Porfiria Intermitente Aguda (Acute Intermittent Porphyria) |
| Pontuação de Previsão TxGNN | 99,12% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Dexchlorpheniramine maleate é o enantiômero farmacologicamente ativo da clorfeniramina. Como anti-histamínico H1 de primeira geração, atua como antagonista competitivo dos receptores H1 da histamina, bloqueando os efeitos mediados por histamina tanto no sistema imunológico quanto no sistema nervoso central. Por cruzar a barreira hematoencefálica, apresenta efeitos sedativos característicos dessa classe. Atualmente, não há dados detalhados de mecanismo de ação (MOA) disponíveis para este fármaco no DrugBank — este é um dado ausente de alta prioridade para a análise.

A porfiria intermitente aguda (PIA) é uma doença metabólica hereditária rara causada pela deficiência parcial da enzima porfobilinogênio deaminase (PBGD), levando ao acúmulo de precursores do heme com crises neurovasculares graves. A conexão mecanística direta entre o antagonismo H1 e a PIA é ausente na literatura. A hipótese mais plausível para a alta pontuação do TxGNN é a existência de ligações indiretas no grafo de conhecimento, possivelmente mediadas por enzimas do citocromo P450 ou por nós reguladores do heme. É importante notar que alguns anti-histamínicos de primeira geração figuram em listas de medicamentos "provavelmente seguros" em portadores de porfiria — porém esse status reflete apenas perfil de segurança (não precipitar crise), e **não** evidência de eficácia terapêutica.

Esta é uma previsão de nível **L5** (apenas modelo computacional, sem evidência translacional disponível). A alta pontuação provavelmente reflete a topologia do grafo de conhecimento e não uma relação farmacológica validada. Para contexto comparativo: entre as 10 indicações geradas nesta análise, a **urticária alérgica** (rank 6, pontuação 96,96%) apresenta mecanismo H1 diretamente pertinente e recomendação "Proceed with Guardrails" — sendo a candidatura biologicamente mais plausível, embora também sem evidência clínica registrada nesta rodada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Dexchlorpheniramine maleate em porfiria intermitente aguda.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Dexchlorpheniramine maleate em porfiria intermitente aguda.

---

## Informações de Comercialização no Brasil

Dexchlorpheniramine maleate não possui nenhum registro ativo na ANVISA. Nenhuma licença comercial foi localizada na base de dados regulatória consultada em 2026-03-24.

---

## Panorama das 10 Indicações Previstas (Visão Multi-Indicação)

> Este relatório cobre um candidato multi-indicação (ID: TW-DB09555-multi). A tabela abaixo resume todas as previsões geradas nesta rodada.

| Rank | Indicação Prevista | Pontuação TxGNN | Nível de Evidência | Decisão |
|------|--------------------|----------------|--------------------|---------|
| 1 | Porfiria Intermitente Aguda | 99,12% | L5 | Hold |
| 2 | Síndrome de Antidiurese Inapropriada Nefrogênica (NSIAD) | 98,36% | L5 | Hold |
| 3 | Porfiria (ampla) | 97,69% | L5 | Hold |
| 4 | Esquizofrenia | 97,17% | L4 | Hold |
| 5 | Polimicrogiria Perisilviana com Hipoplasia Cerebelar | 97,13% | L5 | Hold |
| **6** | **Urticária Alérgica** | **96,96%** | **L4** | **Proceed with Guardrails** |
| 7 | Miopia Sindrómica | 96,83% | L5 | Hold |
| 8 | Encefalopatia Glicínica Atípica | 96,75% | L5 | Hold |
| 9 | Miopia 26, Ligada ao X, Limitada ao Sexo Feminino | 96,71% | L5 | Hold |
| 10 | Miopia Ligada ao X | 96,61% | L5 | Hold |

**Nota:** A única candidatura com recomendação positiva é a urticária alérgica (rank 6), biologicamente consistente com o mecanismo H1. A repetição de três variantes de miopia ligada ao X (ranks 7, 9 e 10) com pontuações semelhantes sugere ruído do grafo de conhecimento, não sinal independente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A principal indicação prevista (porfiria intermitente aguda) apresenta nível de evidência L5 — sem ensaios clínicos, sem publicações e sem mecanismo de ação validado que sustente a hipótese. O fármaco também não está registrado na ANVISA, inviabilizando qualquer avanço clínico imediato no Brasil.

**Para prosseguir, é necessário:**
- Confirmar o mecanismo de ação (MOA) via DrugBank API — dado ausente de alta prioridade
- Obter bula/monografia oficial (ANVISA ou FDA/EMA) para avaliação completa de segurança e contraindicações
- Investigar evidências pré-clínicas sobre anti-histamínicos H1 em modelos de porfiria antes de escalar para L4
- **Priorizar a avaliação da urticária alérgica (rank 6)** como candidatura principal: mecanismo H1 diretamente aplicável e recomendação "Proceed with Guardrails" — requer coleta adicional de ensaios clínicos com clorfeniramina/dexchlorfeniramina em urticária
- Iniciar processo de registro na ANVISA caso alguma indicação avance para estudo clínico brasileiro

---

> ⚠️ **Aviso:** Este relatório é gerado por modelo computacional (TxGNN) e destina-se exclusivamente a fins de pesquisa. Não constitui recomendação médica. Qualquer candidatura de reposicionamento requer validação clínica rigorosa antes de aplicação terapêutica.
---

