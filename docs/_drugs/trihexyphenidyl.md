---
layout: default
title: Trihexyphenidyl
parent: Apenas Predição do Modelo (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Trihexyphenidyl: nova indicação prevista, Transtorno de Déficit de Atenção e Hiperatividade (attention deficit-… (nível de evidência L4). Indicação original: Antiparkinsonianos"
monitor_inn: "Trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Trihexyphenidyl
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

## Triexifenidil: Do parkinsonismo ao transtorno de déficit de atenção e hiperatividade (TDAH)
{: .text-alpha }

## Resumo em Uma Frase

O triexifenidil (trihexyphenidyl) foi originalmente usado como antiparkinsoniano.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno de Déficit de Atenção e Hiperatividade (attention deficit-hyperactivity disorder)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** indireta (um estudo de coorte sobre tiques associados à distonia, condição diferente do TDAH) relacionada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiparkinsonianos |
| Nova Indicação Prevista | Transtorno de Déficit de Atenção e Hiperatividade (attention deficit-hyperactivity disorder) |
| Pontuação de Previsão TxGNN | 0,9992 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o triexifenidil é um antagonista muscarínico de ação central, seletivo para o receptor M1, e sua utilização em sintomas parkinsonianos está bem estabelecida.

A hipótese por trás da previsão é que o desequilíbrio colinérgico-dopaminérgico no estriado pode estar relacionado à hiperatividade, a tiques e à distonia, que frequentemente coexistem com o TDAH. Essa é, porém, uma ligação indireta: o único artigo recuperado trata do transtorno primário de tiques associado à distonia, que é uma condição distinta do TDAH.

Há ainda um argumento contrário importante: anticolinérgicos podem piorar a atenção e a cognição. Assim, o efeito líquido sobre os sintomas centrais do TDAH é incerto e possivelmente desfavorável. A pontuação muito alta do TxGNN é uma previsão computacional, sem respaldo em dados clínicos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Coorte | Movement Disorders | Série clínica de pacientes com tiques e distonia persistente, descrevendo a prevalência e as características clínicas dessa síndrome. Não testa o triexifenidil no TDAH. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101180604 (cancelado) | ARTANE | Não informada | Antiparkinsonianos |

## Considerações de Segurança

- **Contraindicações (com base no grafo de conhecimento do TxGNN, não em texto de bula)**: o grafo associa o fármaco a doenças como glaucoma de ângulo aberto e de ângulo fechado, hiperplasia prostática benigna, miastenia gravis, íleo paralítico, acalasia, megaesôfago, hérnia de hiato, colite ulcerativa, doença inflamatória intestinal, colite por *Clostridium difficile*, enterocolite necrosante perinatal, doença arterial coronariana, doenças da condução cardíaca, parada cardíaca súbita, hipertensão, hipotensão, doença pulmonar obstrutiva crônica, úlcera gástrica, doença renal, doença hepática e doença da vesícula biliar.
- **Interações Medicamentosas**: foram identificadas 100 interações no total. As de gravidade **maior** incluem **cloreto de potássio** e **citrato de potássio**. As de gravidade moderada incluem outros anticolinérgicos e antiespasmódicos (atropina, escopolamina, hioscina/hiosciamina, glicopirrônio, diciclomina, propantelina, trospio, metescopolamina, mepenzolato), opioides e antidiarreicos (morfina, loperamida, eluxadolina), canabinoides (dronabinol, nabilona) e procinéticos ou outros (metoclopramida, prucaloprida, pramlintida, hidróxido de magnésio). O risco principal é o efeito anticolinérgico aditivo.
- Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que testem o triexifenidil no TDAH; a pontuação alta do modelo é apenas computacional. Além disso, os efeitos adversos cognitivos dos anticolinérgicos podem agravar a desatenção, e o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação (MOA) detalhados, a partir do DrugBank.
- Bula do ANVISA com advertências e contraindicações, para a triagem de segurança.
- Revisão sistemática da literatura sobre anticolinérgicos em TDAH, tiques e hiperatividade, com atenção ao impacto cognitivo.
- Avaliação de estudos pré-clínicos ou de um ensaio exploratório antes de qualquer avanço.
- Avaliação da viabilidade regulatória, já que não há registro vigente no Brasil.

**Observação sobre outras previsões:** as demais indicações previstas (síndrome faciodigitogenital, TDAH tipo desatento, encefalite de Rasmussen, neurodegeneração associada ao PLA2G6, entre outras) também carecem de evidência clínica. A neurodegeneração associada ao PLA2G6 foi classificada como "questão de pesquisa", pelo possível benefício sintomático em distonia e tremor, com base em um único relato de caso.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

