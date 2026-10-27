---
layout: default
title: Phenobarbital
parent: Apenas Predição do Modelo (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phenobarbital: nova indicação prevista, Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) (nível de evidência L5). Indicação original: Anticonvulsivantes"
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
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

## Fenobarbital: Do uso anticonvulsivante ao tumor do nervo trigêmeo (previsão sem respaldo mecanístico)
{: .text-alpha }

## Resumo em Uma Frase

Fenobarbital (Phenobarbital) é um barbitúrico originalmente registrado na ANVISA como **anticonvulsivante**.
O modelo TxGNN prevê que poderia ser eficaz para **Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)**, mas essa previsão conta com **0 ensaios clínicos** e apenas **1 publicação** (uma série de casos sobre síndrome de Sturge-Weber, que não trata de tumor). A previsão parece ser um artefato do modelo, e não um sinal terapêutico real.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 8 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o fenobarbital é um modulador alostérico positivo do receptor GABA-A, com atividade antiepiléptica comprovada, e não tem efeito antineoplásico conhecido.

**Esta previsão, na prática, não é razoável.** A relação entre a indicação original (controle de crises convulsivas) e a nova (um tumor do nervo trigêmeo) é frágil. A única publicação recuperada é uma série de casos de 1997 sobre síndrome de Sturge-Weber, que trata do controle de crises em um distúrbio neurocutâneo e não de um tumor trigeminal. A pontuação alta do TxGNN provavelmente decorre de propagação no grafo de conhecimento (proximidade entre doenças neurológicas), e não de evidência biológica.

### Outras previsões do modelo

As demais previsões de alto escore também carecem de respaldo robusto. Nenhuma tem ensaio clínico registrado:

| Posição | Indicação prevista | Escore TxGNN | Nível | Observação |
|---|---|---|---|---|
| 2 | Convulsões induzidas pela micção | 99,96% | L4 | Evidência geral sobre convulsões (inclui 1 RCT neonatal comparando levetiracetam e fenobarbital); nada específico |
| 3 | Convulsões induzidas pelo orgasmo | 99,96% | L5 | Apenas previsão; sem literatura |
| 4 | Convulsões alimentares | 99,96% | L4 | Relatos de caso isolados |
| 5 | Convulsões audiogênicas | 99,96% | L4 | Quase só estudos pré-clínicos; um estudo sugere possível sinal de segurança |
| 6 | Epilepsia do sobressalto | 99,96% | L4 | Literatura sem evidência de eficácia |
| 7 | Convulsões do pensamento | 99,96% | L4 | Literatura geral, sem especificidade |
| 8 | Convulsões da leitura | 99,96% | L4 | Sem evidência direta |
| 9 | Neuralgia do trigêmeo | 99,88% | L4 | Carbamazepina é a primeira linha; fenobarbital é indutor de CYP e complicaria o esquema |
| 10 | Deficiência de beta-cetotiolase | 99,81% | L5 | Sem papel mecanístico conhecido; provável artefato |

As previsões de epilepsias reflexas (posições 2 a 8) são mecanisticamente coerentes com a ação anticonvulsivante, mas representam mais uma extensão da indicação original do que um reposicionamento genuíno.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Série de casos | Anales Españoles de Pediatría | Revisão de 14 casos de síndrome de Sturge-Weber acompanhados em 25 anos, avaliando características clínicas, evolução e resposta terapêutica. Não aborda tumor do nervo trigêmeo. |

---

## Informações de Comercialização no Brasil

Todos os 8 registros estão **cancelados**; não há registro vigente.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104970285 | Fenobarbital | Não informada | Anticonvulsivantes |
| Registro 141070658 | Gardenal | Não informada | Anticonvulsivantes |
| Registro 104971330 | Fenobarbital | Não informada | Anticonvulsivantes |
| Registro 103700322 | Carbital | Não informada | Anticonvulsivantes |
| Registro 110390037 | FURP-Fenobarbital | Não informada | Anticonvulsivantes |

(Exibidos os 5 principais de um total de 8 registros; os demais incluem Fenocris e outras apresentações de Fenobarbital.)

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas de bula)**: hipertensão, insuficiência e doença hepática, insônia, DPOC, úlcera gástrica e péptica, gastrite, transtornos de ansiedade, neuróticos e distímicos, porfiria (incluindo porfirias hereditárias), doença renal, doença da vesícula biliar, trombocitopenia, hiperglicemia, hipotireoidismo (incluindo mixedema e hipotireoidismo congênito), lúpus eritematoso sistêmico, transtornos psicóticos e esquizoafetivos.
- **Interações medicamentosas** (100 interações identificadas; exemplos de gravidade **maior**): morfina (inclusive lipossomal), eliglustate, naldemedina, naloxegol e rolapitant. Entre as de gravidade **moderada**: doxiciclina, corticosteroides (hidrocortisona, dexametasona, prednisona, prednisolona, betametasona, triancinolona), colecalciferol, pioglitazona, bupropiona, aprepitanto, dronabinol, metronidazol e piridoxina.
- **Sinais de segurança na literatura**: exposição precoce ao fenobarbital associada a prejuízo cognitivo tardio (PMID 10416094) e a alterações neurocomportamentais em modelos animais neonatais (PMID 25112558).

Consulte a bula para advertências e contraindicações oficiais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura relevante para tumor do nervo trigêmeo, e o fenobarbital não tem efeito antineoplásico conhecido. A pontuação alta do TxGNN provavelmente é artefato do grafo. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação consolidados (por exemplo, via DrugBank).
- Bula da ANVISA com advertências e contraindicações oficiais (lacuna bloqueante para a triagem de segurança).
- Se houver interesse em reposicionamento, priorizar as epilepsias reflexas (posições 2 a 8), com revisão sistemática e comparação com alternativas atuais.
- Verificar a situação regulatória atual do fenobarbital no Brasil, dado que todos os registros listados estão cancelados.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

