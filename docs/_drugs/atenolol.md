---
layout: default
title: Atenolol
parent: Apenas Predição do Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-29
description: "Atenolol: nova indicação prevista, Doença renal hipertensiva maligna (malignant hypertensive renal disease) (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Atenolol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

## Atenolol: Doença renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumo em Uma Frase

Atenolol é um betabloqueador cardiosseletivo (beta-1), registrado no grafo de conhecimento do TxGNN para hipertensão, infarto do miocárdio e outras condições cardiovasculares.
O modelo TxGNN prevê que pode ser eficaz para **doença renal hipertensiva maligna (malignant hypertensive renal disease)**,
mas, nos dados compiladas para este relatório, há **0 ensaios clínicos** e **0 publicações** que estudem diretamente essa doença. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Doença renal hipertensiva maligna (malignant hypertensive renal disease) |
| Pontuação de Previsão TxGNN | 0.9985 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 4) |
| Número de Registros | Pelo menos 20 registros (lista possivelmente parcial): 5 válidos e 15 cancelados |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, atenolol é um betabloqueador beta-1 seletivo, que reduz a frequência cardíaca, o débito cardíaco e a liberação de renina, e é um anti-hipertensivo consolidado.

A doença renal hipertensiva maligna é uma complicação grave de órgão-alvo da hipertensão. A pontuação alta do modelo TxGNN (deep learning) pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica nem clínica própria.

Há ressalvas: na hipertensão maligna, geralmente se preferem agentes parenterais de rápida titulação, de modo que um betabloqueador oral não é um encaixe óbvio. Esta é apenas uma previsão, sem evidência de reposicionamento.

## Considerações sobre Outras Previsões

Outras indicações previstas também carecem de apoio clínico direto:

- **Hipertensão pulmonar de mecanismo multifatorial incerto** (0.9984): L5. O único vínculo é o rótulo "hipertensão"; o bloqueio beta-1 sistêmico não atua na remodelação vascular pulmonar e pode piorar a função do ventrículo direito.
- **Hipertensão pulmonar por doença pulmonar e/ou hipóxia** (0.9984): a literatura é pré-clínica ou indireta, com resultados inconsistentes em ratos sobre hipertrofia cardíaca direita induzida por hipóxia. Não há estudos em humanos.
- **Síndrome de Braddock** (0.9980): L5, sem ensaios, literatura ou vínculo mecanístico identificável.
- **Cor pulmonale crônico** (0.9904): a literatura é indireta (betabloqueadores na hipertensão e em pacientes com doença das vias aéreas). Uma questão de pesquisa razoável é a segurança dos betabloqueadores cardiosseletivos em pacientes com DPOC e doença cardiovascular, e não se o atenolol trata o cor pulmonale.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Nenhuma publicação estuda diretamente a doença renal hipertensiva maligna. Para a indicação prevista principal, atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Foram listados 20 registros, mas o total é de pelo menos 20 e a lista pode ser parcial. Abaixo estão os registros válidos de medicamentos de componente único (os registros não trazem forma farmacêutica nem texto de indicação aprovada).

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 154230268 | Atenolol (Geolab) | — | — |
| Registro nº 102351170 | Himaagin (EMS) | — | — |
| Registro nº 109740272 | Atenolol (Biolab Sanus) | — | — |
| Registro nº 125680146 | Atenolol (Prati Donaduzzi) | — | — |
| Registro nº 109740100 | Ablok (Biolab Sanus) | — | — |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (não provêm da bula): insuficiência hepática, asma (incluindo intrínseca e alérgica), diabetes mellitus (tipos 1 e 2) e cetoacidose diabética, bloqueio atrioventricular, doença de Raynaud, anafilaxia, psoríase, lúpus eritematoso sistêmico, gota, pancreatite, anúria, transtornos de ansiedade e distímico, além de distúrbios de potássio, cálcio e fósforo.
- **Interações medicamentosas** (100 registradas; principais exemplos): epinefrina, hidrocortisona, hiosciamina, bupropiona, triamcinolona, morfina, acetoexamida, atropina, betametasona, budesonida e sais de cálcio têm interação de nível moderado; ácido acetilsalicílico, hidróxido de alumínio e attapulgita, nível leve.
- Para advertências e contraindicações da bula, consulte a bula; elas ainda não foram obtidas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica; não há ensaios ou literatura (nível L5). Clinicamente, um betabloqueador oral não é a escolha habitual na hipertensão maligna.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas da ANVISA (advertências, contraindicações e indicações aprovadas).
- Complementar os dados de mecanismo de ação.
- Realizar revisão sistemática da literatura sobre betabloqueadores em doença renal hipertensiva maligna.
- Definir a justificativa clínica e o plano de segurança, considerando as contraindicações do grafo de conhecimento e as interações medicamentosas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

