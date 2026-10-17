---
layout: default
title: Ivacaftor
parent: Apenas Predição do Modelo (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ivacaftor: nova indicação prevista, Artrite Reumatoide (Rheumatoid Arthritis) (nível de evidência L5). Indicação original: Fibrose cística"
monitor_inn: "Ivacaftor"
predicted_indications: ["rheumatoid arthritis", "HIV infectious disease", "leprosy", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "multiple endocrine neoplasia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "cytomegalovirus infection"]
---

# Ivacaftor
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Ivacaftor: Da fibrose cística à artrite reumatoide

## Resumo em Uma Frase

Ivacaftor é um potenciador da proteína CFTR, originalmente usado no tratamento da fibrose cística.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrose cística |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 96,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o ivacaftor é um potenciador da CFTR, canal iônico de cloreto presente em células epiteliais, e sua eficácia na fibrose cística foi estabelecida.

A relação com a artrite reumatoide é fraca. A CFTR é expressa em algumas células imunes e epiteliais, mas não há dados que conectem a potenciação da CFTR às vias inflamatórias que causam a artrite reumatoide. A pontuação elevada (96,97%) reflete apenas uma previsão baseada em grafo de conhecimento, sem respaldo de ensaios ou publicações.

Portanto, a razoabilidade mecanística é **não estabelecida**. A previsão deve ser tratada como hipótese a ser investigada, não como indicação com fundamento clínico.

Outras previsões do modelo (HIV, hanseníase, citomegalovírus, síndromes genéticas raras, entre outras) também carecem de evidências e vínculo mecanístico. Duas delas (infecção por vírus da imunodeficiência símia e síndrome da imunodeficiência adquirida felina) são doenças animais com pontuação idêntica, sugerindo um sinal compartilhado do grafo e não evidências independentes.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; as principais amostras dos dados compilados incluem:
  - **Maior gravidade (Major)**: aprepitanto e claritromicina.
  - **Moderada**: corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), loperamida, cimetidina, cisaprida, clotrimazol, eliglustate, eluxadolina e sulfonilureias (clorpropamida, acetoexamida, glimepirida, glipizida, glibenclamida).
  - **Leve (Minor)**: fidaxomicina.

  Chama atenção a interação com corticosteroides, frequentemente usados na artrite reumatoide.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem publicações, o mecanismo é desconhecido e o fármaco não está registrado no Brasil. A previsão é apenas computacional (nível L5).

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (consulta à API do DrugBank)
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem isso
- Realizar revisão da literatura e estudos pré-clínicos que testem a hipótese CFTR–inflamação na artrite reumatoide
- Avaliar a situação regulatória no Brasil, já que não há registro vigente
- Avaliar o manejo das interações medicamentosas, em especial com corticosteroides e inibidores/indutores do CYP3A
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

