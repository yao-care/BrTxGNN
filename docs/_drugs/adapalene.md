---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Adapalene
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

# Adapalene: Da Acne Vulgar ao Zinco Plasmático Elevado

## Resumo em Uma Frase

Adapalene é um retinoide sintético agonista seletivo de RAR-β/γ, utilizado primariamente no tratamento tópico da acne vulgar por meio da regulação da diferenciação de queratinócitos e da inibição de mediadores pró-inflamatórios.
O modelo TxGNN prevê associação com **Zinco Plasmático Elevado (Zinc, Elevated Plasma)** com pontuação de **99,51%**,
porém esta previsão atualmente **não possui nenhum ensaio clínico nem publicação científica** de suporte — forte indicativo de falso positivo algorítmico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Acne vulgar (formulação tópica) |
| Nova Indicação Prevista | Zinco Plasmático Elevado (Zinc, Elevated Plasma) |
| Pontuação de Previsão TxGNN | 99,51% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Adapalene é um agonista seletivo dos receptores de ácido retinoico RAR-β e RAR-γ, proteínas pertencentes à superfamília dos fatores de transcrição com **domínio de dedo de zinco** (zinc finger proteins). Ao se ligar a esses receptores nucleares, o fármaco regula a diferenciação e proliferação dos queratinócitos no folículo pilossebáceo e exerce efeito anti-inflamatório pela inibição das vias AP-1 e NF-κB — base farmacológica do seu uso consolidado no tratamento da acne vulgar.

A conexão computacional entre adapalene e "zinco plasmático elevado" origina-se da **topologia do grafo de conhecimento**: o caminho adapalene → RAR (zinc finger protein) → metabolismo do zinco gerou uma ligação indireta que o algoritmo TxGNN pontuou com alta relevância topológica (score 0,9951). Contudo, essa associação reflete uma proximidade estrutural no grafo e não um mecanismo terapêutico clinicamente plausível — a ativação do RAR por adapalene não possui qualquer ação demonstrada sobre os níveis séricos de zinco.

É fundamental destacar que "zinco plasmático elevado" é um **marcador laboratorial metabólico**, e não uma entidade diagnóstica independente com protocolo de tratamento estabelecido. A ausência completa de ensaios clínicos e publicações científicas, combinada com a natureza puramente topológica do vínculo, classifica esta previsão como **provável falso positivo algorítmico** do modelo TxGNN, conforme indicado pela própria análise de racionalidade do Evidence Pack.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para "zinco plasmático elevado" apresenta nível de evidência L5 — baseada exclusivamente em predição computacional, sem qualquer ensaio clínico ou publicação de suporte. A análise mecanística revela que o vínculo RAR–zinco é uma associação topológica indireta no grafo de conhecimento, sem correspondência em mecanismo terapêutico validável; além disso, "zinco plasmático elevado" não constitui uma indicação clínica independente tratável com adapalene.

**Para prosseguir com as candidaturas mais promissoras deste Evidence Pack, é necessário:**

- Redirecionar a análise para as indicações com maior suporte evidencial identificadas no mesmo pack:
  - **Rank 9 — Anomalia de Glândula Sebácea** *(L3 / Proceed with Guardrails)*: 1 ensaio Phase 3 concluído ([NCT00446043](https://clinicaltrials.gov/study/NCT00446043), n=452, 12 meses) com mecanismo de ação diretamente relacionado à unidade pilossebácea
  - **Rank 8 — Dermatite Seborreica** *(L4 / Research Question)*: 3 ensaios clínicos e 3 publicações com vínculo mecanístico intermediário (normalização da diferenciação de queratinócitos e inibição de IL-1α/TNF-α)
- Complementar os dados de segurança (advertências e contraindicações via bula oficial — gap DG001, classificado como Blocking)
- Obter dados formais de mecanismo de ação via DrugBank API (gap DG002, severidade High)
- Confirmar situação regulatória junto à ANVISA, incluindo eventuais registros de produtos à base de adapalene comercializados no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

