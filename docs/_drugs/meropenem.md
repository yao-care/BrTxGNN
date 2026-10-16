---
layout: default
title: Meropenem
parent: Evidência Moderada (L3-L4)
nav_order: 445
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Meropenem: nova indicação prevista, Artrite bacteriana (bacterial arthritis) (nível de evidência L4). Indicação original: Antibióticos sistêmicos simples"
monitor_inn: "meropenem"
predicted_indications: ["bacterial arthritis", "epiglottitis", "staphylococcus aureus infection", "laryngitis", "paratyphoid fever", "urinary tract infection (disease)", "Lyme disease", "Peptostreptococcus infectious disease", "Ureaplasma urethritis", "gonococcal urethritis"]
---

# Meropenem
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
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

# Meropenem: De antibiótico sistêmico à infecção do trato urinário

## Resumo em Uma Frase

Meropenem é um antibiótico carbapenêmico de amplo espectro, registrado na ANVISA na categoria "antibióticos sistêmicos simples".
O modelo TxGNN prevê que pode ser eficaz para **artrite bacteriana (bacterial arthritis)**, a previsão de maior pontuação, mas sem ensaios clínicos e com literatura apenas indireta (relatos de caso, coortes retrospectivas, revisões e estudos farmacocinéticos). A indicação com maior suporte de evidências entre as previstas é a **infecção do trato urinário (urinary tract infection)**, com **9 ensaios clínicos** e **20 publicações**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples |
| Nova Indicação Prevista | Artrite bacteriana (bacterial arthritis) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 10 (todos cancelados) |
| Decisão Recomendada | Hold |

> **Observação:** a indicação de maior pontuação (artrite bacteriana) tem evidências fracas (L4). Entre as 10 indicações previstas, a infecção do trato urinário (pontuação 99,52%) é a única com evidências robustas (L1, recomendação "Proceed with Guardrails"), e é detalhada nas seções de evidências abaixo, por ser a única com ensaios clínicos registrados. As demais indicações estão resumidas na seção de conclusão.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no conjunto de dados compilado. Segundo informações conhecidas, meropenem é um carbapenêmico de amplo espectro que inibe a síntese da parede celular bacteriana por meio da ligação às proteínas ligadoras de penicilina (PBP). É estável frente a muitas beta-lactamases, incluindo as de espectro estendido (ESBL).

Para **artrite bacteriana**, a atividade contra bacilos Gram-negativos e contra *Burkholderia pseudomallei* (melioidose), patógenos que causam infecções osteoarticulares, é plausível. Contudo, a penetração em osso e articulação é sustentada apenas por dados farmacocinéticos indiretos, e não há ensaios registrados.

Para **infecção do trato urinário (ITU)**, a atividade contra Enterobacterales, inclusive produtores de ESBL, está bem estabelecida. Vários ensaios de Fase 3 usam meropenem como comparador. Como a ITU complicada provavelmente se sobrepõe ao uso já aprovado do fármaco, o reposicionamento neste caso é, na prática, uma confirmação de uso existente.

## Evidências de Ensaios Clínicos

Os ensaios abaixo referem-se à indicação **infecção do trato urinário**, a única das 10 previstas com ensaios registrados. Para artrite bacteriana, atualmente não há ensaios clínicos relacionados registrados.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03840148](https://clinicaltrials.gov/study/NCT03840148) | Phase 3 | Concluído | 661 | Cefepima/VNRX-5133 vs meropenem em ITU complicada, incluindo pielonefrite aguda (não inferioridade) |
| [NCT03477422](https://clinicaltrials.gov/study/NCT03477422) | Phase 3 | Concluído | 230 | CSE-1034 (ceftriaxona + sulbactam + EDTA) vs meropenem em ITU complicada por bactérias produtoras de beta-lactamase |
| [NCT02142751](https://clinicaltrials.gov/study/NCT02142751) | Phase 3 | Concluído | 161 | Fosfomicina vs meropenem ou ceftriaxona em ITU bacterêmica por *E. coli* multirresistente |
| [NCT01970371](https://clinicaltrials.gov/study/NCT01970371) | Phase 3 | Concluído | 69 | Plazomicina vs colistina (associadas a meropenem ou tigeciclina) em infecções por Enterobacteriaceae resistentes a carbapenêmicos |
| [NCT03543436](https://clinicaltrials.gov/study/NCT03543436) | Phase 3 | Concluído | 29 | Temocilina vs carbapenêmico em ITU por Enterobacterales produtores de ESBL (amostra pequena) |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | Concluído | 134 | Ceftolozana/tazobactam vs meropenem em ITU complicada pediátrica |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | Suspenso | 198 | Piperacilina/tazobactam vs carbapenêmicos em ITU por ESBL; dados incompletos |
| [NCT03174795](https://clinicaltrials.gov/study/NCT03174795) | Phase 1 | Concluído | 20 | Farmacocinética de RO7079901 coadministrado com meropenem em ITU complicada |
| [NCT00771316](https://clinicaltrials.gov/study/NCT00771316) | Phase 3 | Encerrado | 6 | MK0826 vs meropenem em ITU complicada; encerrado com 6 participantes, sem valor informativo |

Observação: na maioria desses ensaios, o meropenem é o comparador, e não o fármaco em estudo. Ainda foi identificado o estudo observacional NCT04278404 (farmacocinética de fármacos pouco estudados em crianças, n=5.000), que não constitui evidência de eficácia em ITU.

## Evidências da Literatura

Publicações referentes à **infecção do trato urinário**:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I: meropenem-vaborbactam vs piperacilina-tazobactam em ITU complicada (cura clínica e erradicação microbiana) |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | RCT | Infect Dis Ther | TANGO II: meropenem-vaborbactam vs melhor terapia disponível em infecções por Enterobacteriaceae resistentes a carbapenêmicos |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Revisão sistemática / meta-análise em rede | J Comp Eff Res | Eficácia das opções de tratamento em ITU complicada e pielonefrite aguda; carbapenêmicos como terapia de última linha |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Coorte retrospectiva | Antimicrob Agents Chemother | Meropenem-vaborbactam vs ceftazidima-avibactam em infecções por CRE (classificado na base como RCT, mas descrito como coorte retrospectiva multicêntrica) |
| [33058798](https://pubmed.ncbi.nlm.nih.gov/33058798/) | 2021 | RCT | Lancet Infect Dis | APEKS-NP: cefiderocol vs meropenem em dose alta e infusão estendida em pneumonia nosocomial (indireta para ITU) |
| [18416587](https://pubmed.ncbi.nlm.nih.gov/18416587/) | 2008 | Revisão | Drugs | Revisão do uso de meropenem em infecções bacterianas graves |
| [36726388](https://pubmed.ncbi.nlm.nih.gov/36726388/) | 2023 | Revisão | Infect Drug Resist | Avaliação clínica de meropenem-vaborbactam em ITU |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Revisão | Int J Antimicrob Agents | Diretrizes práticas SIMIT/SPILF para infecções por bacilos Gram-negativos multirresistentes |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Revisão | Int J Antimicrob Agents | Dados clínicos de novos antibióticos contra Gram-negativos multirresistentes |
| [14508383](https://pubmed.ncbi.nlm.nih.gov/14508383/) | 2003 | Revisão | Ther Drug Monit | Carbapenêmicos em pediatria; estabilidade frente a ESBL e AmpC |

Para a indicação de maior pontuação, **artrite bacteriana**, a literatura é indireta: revisões sobre melioidose osteoarticular, uma coorte retrospectiva (PMID 35146367) e relatos de caso, como o de artrite séptica por *Klebsiella pneumoniae* produtora de ESBL tratada com meropenem e amicacina (PMID 17433752), além de estudos farmacocinéticos.

## Informações de Comercialização no Brasil

Todos os 10 registros encontrados estão **cancelados**; atualmente não há registro válido de meropenem monofármaco nos dados compilados.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100430034 | Meropeném | Não informada | Antibióticos sistêmicos simples |
| Registro nº 100630190 | Mepenox | Não informada | Antibióticos sistêmicos simples |
| Registro nº 100410207 | Meropenem | Não informada | Antibióticos sistêmicos simples |
| Registro nº 100630229 | Meropeném | Não informada | Antibióticos sistêmicos simples |
| Registro nº 116370187 | Meropeném | Não informada | Antibióticos sistêmicos simples |

Há ainda outros cinco registros cancelados (incluindo Meronem e Meromax), totalizando 10.

## Considerações de Segurança

- **Contraindicações associadas (grafo de conhecimento, não texto de bula):** epilepsia, doença renal, piureter, trombocitopenia, colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas (14 identificadas):**
  - **Maiores:** bupropiona (risco aumentado de convulsões), iohexol e iopamidol.
  - **Moderadas:** ácido picossulfúrico, polietilenoglicol 3350 com eletrólitos, sulfato de sódio, nitisinona, lindano, etinilestradiol, alpelisibe, encorafenibe, ácido micofenólico, pemetrexede e teriflunomida.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, artrite bacteriana)

**Justificativa:**
- A indicação de maior pontuação (artrite bacteriana, 99,92%) tem apenas evidência indireta (L4), sem ensaios registrados.
- A infecção do trato urinário (L1) permitiria "Proceed with Guardrails", mas provavelmente se sobrepõe ao uso já estabelecido do meropenem, e os registros brasileiros estão todos cancelados.

**Situação das demais indicações previstas:**

| Indicação | Pontuação | Nível | Recomendação | Comentário |
|------|------|------|------|------|
| Epiglotite | 99,91% | L4 | Hold | Sem evidência clínica; agentes de espectro mais estreito são o padrão |
| Infecção por *Staphylococcus aureus* | 99,85% | L4 | Hold | Ativo contra MSSA, mas não preferencial; MRSA é resistente |
| Laringite | 99,59% | L5 | Hold | Predominantemente viral; sem racional |
| Febre paratifoide | 99,57% | L4 | Hold | Opção de resgate em febre entérica XDR; sem dados diretos |
| Infecção do trato urinário | 99,52% | L1 | Proceed with Guardrails | Ver seções de evidências |
| Doença de Lyme | 99,46% | L5 | Hold | Apenas dados in vitro; existem terapias padrão |
| Infecção por *Peptostreptococcus* | 99,37% | L5 | Hold | Plausível, mas sem estudos |
| Uretrite por *Ureaplasma* | 99,33% | L5 | Hold | Mecanisticamente implausível (ausência de parede celular) |
| Uretrite gonocócica | 99,33% | L5 | Hold | Ceftriaxona é a primeira linha; conflita com o uso racional de antimicrobianos |

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança.
- Complementar os dados de mecanismo de ação (MOA) e esclarecer a situação regulatória, já que todos os registros estão cancelados.
- Para artrite bacteriana: dados de penetração óssea e articular e estudos clínicos comparativos.
- Para ITU, se for priorizada: reservar para patógenos produtores de ESBL ou multirresistentes, seguir o programa de uso racional de antimicrobianos e a suscetibilidade local, ajustar a dose à função renal, considerar alternativas poupadoras de carbapenêmicos e reconciliar a sobreposição com o uso original.
- Plano de monitoramento para populações de risco (epilepsia, doença renal, trombocitopenia, uso de bupropiona).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

