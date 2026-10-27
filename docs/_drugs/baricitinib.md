---
layout: default
title: Baricitinib
parent: Apenas Predição do Modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Baricitinib: nova indicação prevista, Síndrome de microftalmia colobomatosa com displasia rizomélica (colob… (nível de evidência L5). Indicação original: Artrite reumatoide"
monitor_inn: "baricitinib"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Baricitinibe: Da artrite reumatoide à síndrome de displasia rizomélica com microftalmia colobomatosa
{: .text-alpha }

## Resumo em Uma Frase

Baricitinibe (OLUMIANT) foi originalmente usado no tratamento da artrite reumatoide.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Artrite reumatoide (conforme as indicações originais do grafo de conhecimento; o texto de indicação aprovado no registro da ANVISA está vazio) |
| Nova Indicação Prevista | Síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, o baricitinibe é um inibidor de JAK1/JAK2, e sua eficácia na artrite reumatoide é estabelecida. A modulação da via JAK-STAT reduz a sinalização inflamatória, o que explica o efeito nessa doença autoimune.

Para a nova indicação, porém, **os dados compilados não sustentam um vínculo mecanístico**. Trata-se de uma síndrome do desenvolvimento muito rara, com provável base genética, e não há via estabelecida que conecte a inibição de JAK-STAT à sua fisiopatologia. A pontuação alta (99,94%) é uma previsão baseada em grafo e pode refletir artefatos da rede, como a baixa conectividade do nó da doença, e não plausibilidade biológica.

A segunda previsão do modelo, a **síndrome de braquidactilia-sindactilia** (pontuação de 99,94%, também nível L5), apresenta o mesmo problema: são malformações congênitas de membros, de origem tipicamente genética, sem relação evidente com a inibição de JAK1/JAK2. Qualquer vínculo seria especulativo e exigiria validação independente, por exemplo, análise de vias ou das variantes causais.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 112600198 (cancelado) | OLUMIANT | Não informada | Não informada |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 321 interações no total. Entre as principais:
  - **Gravidade maior**: corticosteroides (hidrocortisona, triancinolona, betametasona, budesonida, dexametasona, prednisolona, prednisona), deferiprona e radiofármacos/radioimunoconjugados (ibritumomabe tiuxetana, iobenguano [I-131], tositumomabe [I-131]).
  - **Gravidade moderada**: morfina (incluindo lipossomal), ácido acetilsalicílico, nitisinona e ópio.
  - **Gravidade menor**: sais de zinco (acetato, gliconato e sulfato).

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a indicação prevista, e o nível de evidência é L5 (apenas previsão do modelo). Os dados compilados não sustentam nenhum vínculo mecanístico com a doença, e o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação detalhados (por exemplo, via consulta ao DrugBank)
- Análise independente de vias ou genética que relacione a via JAK-STAT à fisiopatologia da síndrome
- Advertências e contraindicações da bula da ANVISA, para a triagem de segurança
- Esclarecer a situação regulatória do registro cancelado e a viabilidade de via de administração/forma farmacêutica
- Revisão sistemática da literatura e busca de ensaios clínicos ou relatos de caso sobre a doença
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

