---
layout: default
title: Phenobarbital
parent: Apenas Predição do Modelo (L5)
nav_order: 520
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Phenobarbital: nova indicação prevista, Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) (nível de evidência L5). Indicação original: Anticonvulsivantes"
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Fenobarbital: Do uso anticonvulsivante à Neoplasia do Nervo Trigêmeo (previsão sem respaldo mecanístico)
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
| Pontuação de Previsão TxGNN | 0,9996 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 8 de 36) |
| Número de Registros | 36 (ativos: 8) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o fenobarbital é um modulador alostérico positivo do receptor GABA-A, com atividade antiepiléptica comprovada, e não tem efeito antineoplásico conhecido.

**Esta previsão, na prática, não é razoável.** A relação entre a indicação original (controle de crises convulsivas) e a nova (Neoplasia do Nervo Trigêmeo) é frágil. A única publicação recuperada é uma série de casos de 1997 sobre síndrome de Sturge-Weber, que trata do controle de crises em um distúrbio neurocutâneo e não de um tumor trigeminal. A pontuação alta do TxGNN (0.9996) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

### Outras previsões do modelo

As demais previsões de alto escore também carecem de respaldo robusto. Nenhuma tem ensaio clínico registrado:

| Posição | Indicação prevista | Escore TxGNN | Nível | Observação |
|---|---|---|---|---|
| 2 | Convulsões induzidas pela micção | 0,9996 | L4 | Evidência geral sobre convulsões (inclui 1 RCT neonatal comparando levetiracetam e fenobarbital); nada específico |
| 3 | Convulsões induzidas pelo orgasmo | 0,9996 | L5 | Apenas previsão; sem literatura |
| 4 | Convulsões alimentares | 0,9996 | L4 | Relatos de caso isolados |
| 5 | Convulsões audiogênicas | 0,9996 | L4 | Quase só estudos pré-clínicos; um estudo sugere possível sinal de segurança |
| 6 | Epilepsia do sobressalto | 0,9996 | L4 | Literatura sem evidência de eficácia |
| 7 | Convulsões do pensamento | 0,9996 | L4 | Literatura geral, sem especificidade |
| 8 | Convulsões da leitura | 0,9996 | L4 | Sem evidência direta |
| 9 | Neuralgia do trigêmeo | 0,9988 | L4 | Carbamazepina é a primeira linha; fenobarbital é indutor de CYP e complicaria o esquema |
| 10 | Deficiência de beta-cetotiolase | 0,9981 | L5 | Sem papel mecanístico conhecido; provável artefato |

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

Todos os 8 registros estão **válidos** (8 de 8); o medicamento é comercializado no Brasil.

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100630282 | FENOBARBITAL | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 102980016 | FENOCRIS | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 103700322 | CARBITAL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700640 | FENOBARBITAL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 104400238 | GARDENAL | CELLERA FARMACEUTICA S.A. | Ativo |
| 104970285 | FENOBARBITAL | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 104971330 | FENOBARBITAL | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 110390037 | FURP-FENOBARBITAL | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Ativo |
| 100820018 | EDHANOL | ABBOTT PRODUTOS PARA SAÚDE LTDA. | Cancelado |
| 101910155 | EUCALMINA | THERASKIN FARMACEUTICA LTDA. | Cancelado |
| 102350040 | FENOBARBITOL | EMS S/A | Cancelado |
| 102980332 | FENOCRIS | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Cancelado |
| 103700481 | FENOBARBITAL (PORT. 344/98 - LISTA B1) | LABORATÓRIO TEUTO BRASILEIRO S/A | Cancelado |
| 104440078 | VAGOSTESYL | LABORATÓRIO GROSS S. A. | Cancelado |
| 104440095 | GROSS | LABORATÓRIO GROSS S. A. | Cancelado |
| 104650177 | GARBITAL | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104650425 | FENOBARBITAL (PORT. 344/98 - LISTA B1) | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104970252 | UNIFENOBARB | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |
| 106460104 | FENOBARBITAL | LABORATORIO QUIMICO FARMACEUTICO BERGAMO LTDA | Cancelado |
| 107140105 | BARBITRON | SANVAL COMERCIO E INDUSTRIA LTDA | Cancelado |
| 107140242 | FENOBARBITAL | SANVAL COMERCIO E INDUSTRIA LTDA | Cancelado |
| 110630081 | FARMANGUINHOS - FENOBARBITAL | FUNDAÇÃO OSWALDO CRUZ | Cancelado |
| 112090014 | FUNED - FENOBARBITAL | FUNDAÇÃO EZEQUIEL DIAS - FUNED | Cancelado |
| 112090096 | FENOBARBITAL | FUNDAÇÃO EZEQUIEL DIAS - FUNED | Cancelado |
| 112100012 | LAFERGS - FENOBARBITAL | FUNDAÇÃO ESTADUAL DE PRODUÇÃO E PESQUISA EM SAÚDE  | Cancelado |
| 113000306 | GARDENAL | SANOFI-AVENTIS FARMACÊUTICA LTDA | Cancelado |
| 113001010 | FENOBARBITAL (PORT.344/98 LISTA - B1) | SANOFI-AVENTIS FARMACÊUTICA LTDA | Cancelado |
| 113430191 | FENOBARBITAL | HIPOLABOR FARMACEUTICA LTDA | Cancelado |
| 121550015 | SECUFENOTAL | ENGEFARMA PRODS. FARMACÊUTICOS LTDA. | Cancelado |
| 126250001 | LFM-FENOBARBITAL | LABORATÓRIO FARMACÊUTICO DA MARINHA | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

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
- Não há ensaios clínicos nem literatura relevante para Neoplasia do Nervo Trigêmeo, e o fenobarbital não tem efeito antineoplásico conhecido. A pontuação alta do TxGNN (0.9996) vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação consolidados (por exemplo, via DrugBank).
- Bula da ANVISA com advertências e contraindicações oficiais (lacuna bloqueante para a triagem de segurança).
- Se houver interesse em reposicionamento, priorizar as epilepsias reflexas (posições 2 a 8), com revisão sistemática e comparação com alternativas atuais.
- Verificar a situação regulatória atual do fenobarbital no Brasil, onde o medicamento é comercializado e os 8 registros listados estão válidos.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

