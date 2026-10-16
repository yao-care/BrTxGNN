---
layout: default
title: Praziquantel
parent: Apenas Predição do Modelo (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Praziquantel: nova indicação prevista, Leiomiossarcoma epitelioide do corpo uterino (uterine corpus epitheli… (nível de evidência L5). Indicação original: Opistorquíase, esquistossomose, enterobíase …"
monitor_inn: "Praziquantel"
predicted_indications: ["uterine corpus epithelioid leiomyosarcoma", "Plasmodium falciparum malaria", "retroperitoneal sarcoma", "uterine corpus myxoid leiomyosarcoma", "anus leiomyosarcoma", "small intestinal sarcoma", "gnathomiasis", "fascioliasis", "leiomyosarcoma", "dermatofibrosarcoma protuberans"]
---

# Praziquantel
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

# Praziquantel: Da esquistossomose à uterine corpus epithelioid leiomyosarcoma (leiomiossarcoma epitelioide do corpo uterino)

## Resumo em Uma Frase

Praziquantel é um anti-helmíntico originalmente usado no tratamento de opistorquíase, esquistossomose, enterobíase e triquinose.
O modelo TxGNN prevê que pode ser eficaz para **leiomiossarcoma epitelioide do corpo uterino (uterine corpus epithelioid leiomyosarcoma)**, mas **não há ensaios clínicos nem publicações** apoiando esta direção específica; trata-se de uma previsão puramente baseada em grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Opistorquíase, esquistossomose, enterobíase e triquinose (conforme o grafo de conhecimento do TxGNN; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Leiomiossarcoma epitelioide do corpo uterino (uterine corpus epithelioid leiomyosarcoma) |
| Pontuação de Previsão TxGNN | 97,28% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o praziquantel atua nos esquistossomos ativando o canal TRPM_PZQ, o que perturba a homeostase do cálcio do parasita e causa paralisia e lesão do tegumento. Esse é o mecanismo que sustenta seu uso contra trematódeos e cestódeos.

Não há relação mecanística reconhecida entre essa ação antiparasitária e a biologia do sarcoma de músculo liso. A pontuação alta (0,97) vem apenas da estrutura do grafo de conhecimento e não de evidência biológica ou clínica. Por isso, a previsão deve ser tratada como hipótese a explorar, não como indicação plausível.

Outras previsões do modelo para o mesmo fármaco incluem outros sarcomas (retroperitoneal, leiomiossarcoma, dermatofibrossarcoma protuberans, entre outros), todos igualmente sem evidências. Já a malária por *Plasmodium falciparum*, a gnatostomíase e a fasciolíase têm alguma literatura, porém também sem comprovação de eficácia.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (não extraídas da bula): epilepsia, doença hepática, doença da vesícula biliar, doença cardíaca e doença cardiovascular.
- **Interações Medicamentosas**: foram identificadas 83 interações no total. As de maior gravidade entre as listadas são de nível **Maior**:
  - Apalutamida
  - Fenobarbital
  - Carbamazepina

  Há também várias interações de nível Moderado (por exemplo, dexametasona, bosentana, armodafinila, bexaroteno, brigatinibe, deferasirox, butalbital, amobarbital) e de nível Menor (cimetidina, albendazol). Os indutores enzimáticos (fenobarbital, carbamazepina, apalutamida) tendem a reduzir a exposição ao praziquantel.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para leiomiossarcoma epitelioide uterino tem apenas pontuação do modelo (L5), sem ensaios, sem literatura e sem mecanismo plausível. Além disso, o fármaco não está registrado no Brasil e faltam dados de bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), hoje uma lacuna que impede a triagem de segurança
- Complementar os dados oficiais de mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos *in vitro* e *in vivo* em linhagens de leiomiossarcoma, para estabelecer ao menos uma plausibilidade biológica
- Avaliar a situação regulatória: o praziquantel não possui registro vigente no Brasil
- Priorizar, se houver interesse em reposicionamento, as previsões com alguma literatura (por exemplo, o estudo randomizado de 2026 sobre praziquantel na infecção por *P. falciparum*, PMID 41159886, que precisa de revisão do texto completo)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

