---
layout: default
title: Chlorthalidone
parent: Apenas Predição do Modelo (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Chlorthalidone: nova indicação prevista, Glaucoma hereditário primário (primary hereditary glaucoma) (nível de evidência L5). Indicação original: Diuréticos simples"
monitor_inn: "CHLORTHALIDONE"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Clortalidona: De anti-hipertensivo e diurético para glaucoma hereditário primário

## Resumo em Uma Frase

Clortalidona (clorotalidona) é um diurético tiazídico-símile, originalmente registrado no Brasil como diurético simples e anti-hipertensivo (isolado ou em associações, como com atenolol).
O modelo TxGNN prevê que pode ser eficaz para **glaucoma hereditário primário (primary hereditary glaucoma)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diuréticos simples |
| Nova Indicação Prevista | Glaucoma hereditário primário (primary hereditary glaucoma) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, a clortalidona é um diurético tiazídico-símile que inibe o cotransportador sódio-cloreto (Na-Cl) no túbulo contorcido distal do rim, aumentando a excreção de sódio e água e reduzindo a pressão arterial. Sua eficácia como diurético e anti-hipertensivo é bem estabelecida.

A relação entre a indicação original (controle de volume e pressão arterial) e o glaucoma é distante. Qualquer efeito sobre a pressão intraocular seria especulativo: diuréticos sistêmicos poderiam, em teoria, alterar a dinâmica do humor aquoso, mas isso não é sustentado por nenhum dado disponível. Sem o mecanismo de ação original verificado, não é possível construir uma ponte mecanística confiável.

A pontuação alta do TxGNN (99,92%) reflete padrões no grafo de conhecimento, e não evidência clínica. Por isso, a previsão deve ser tratada como hipótese a investigar, não como indicação pronta.

**Outras indicações previstas (todas sem ensaios clínicos registrados):**

| Posição | Indicação prevista | Pontuação TxGNN | Nível | Comentário |
|------|------|------|------|------|
| 2 | Glaucoma de ângulo aberto | 99,90% | L5 | Sem dados clínicos; efeito apenas teórico |
| 3 | Doença renal hipertensiva maligna | 99,89% | L5 | Plausível pelo efeito anti-hipertensivo, mas tiazídicos não são primeira linha e há sobreposição com a indicação atual |
| 4 | Hipertensão renovascular maligna | 99,89% | L5 | Diuréticos podem ativar o sistema renina-angiotensina; emergência hipertensiva |
| 5 | Hipertensão pulmonar de mecanismo multifatorial incerto | 99,88% | L5 | Alívio de sobrecarga de volume, sem efeito sobre a pressão vascular pulmonar |
| 6 | Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,88% | L5 | Única publicação recuperada é irrelevante |
| 7 | Síndrome de Braddock | 99,85% | L5 | Sem racional mecanístico identificável |
| 8 | Cor pulmonale crônico | 99,82% | L4 | Único candidato com indício indireto (relato de 1967) |
| 9 | Cor pulmonale agudo | 99,32% | L5 | Diuréticos não são terapia direcionada |
| 10 | Hipotricose congênita com milia | 99,19% | L5 | Sem conexão mecanística crível |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para glaucoma hereditário primário.

## Evidências da Literatura

Atualmente não há literatura relacionada para glaucoma hereditário primário.

Observação sobre as demais previsões: para o cor pulmonale crônico (posição 8), foram recuperadas duas publicações, sendo um relato clínico de 1967 sobre clortalidona em insuficiência cardíaca congestiva por cor pulmonale crônico (PMID 5597001, desenho provavelmente não controlado) e uma revisão de 2017 sobre a transição de hipertensão para insuficiência cardíaca (PMID 28711447), que serve apenas de contexto geral. Para a hipertensão pulmonar por doença pulmonar/hipóxia (posição 6), a única publicação recuperada (PMID 14288313, 1965) trata de transporte de íons no intestino médio de uma mariposa e não tem relevância clínica.

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados; não há produto atualmente comercializado. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 135690691 | Clortalil | — | Diuréticos simples |
| Registro 102350614 | Clorotalidona | — | Diuréticos simples |
| Registro 103920047 | Clordilon | — | Diuréticos simples |
| Registro 105831031 | Atenolol + Clortalidona | — | Anti-hipertensivos – associações medicamentosas |
| Registro 100430981 | Diupress | — | Associação de fármacos com ação diurética |

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento do TxGNN, não o texto da bula):** doença renal, anúria, insuficiência hepática, gota e hiperuricemia, diabetes mellitus tipo 2, deficiência de potássio, hipercalcemia e nefrocalcinose, distúrbios do metabolismo do fósforo, pancreatite, úlcera péptica, lúpus eritematoso sistêmico, asma, psoríase e parapsoríase, infarto do miocárdio e trombose coronariana, parada cardíaca súbita, hemoglobinopatia, epilepsia, transtornos de ansiedade, neuróticos e distímicos, e piureter.
- **Interações Medicamentosas:** foram identificadas 100 interações; entre as listadas, as de gravidade **maior** são com **cisaprida** e **dolasetrona** (risco associado a distúrbios eletrolíticos e prolongamento do intervalo QT). Há interações moderadas, por exemplo, com acarbose, metformina, alogliptina, albiglutida (efeito sobre a glicemia), hidrocortisona, dexametasona, triamcinolona e beclometasona (corticoides, risco de hipocalemia), anfotericina B, omeprazol, rabeprazol, bupropiona, morfina e colecalciferol. Interações menores incluem doxiciclina, atropina e hiosciamina.

Consulte a bula para advertências e contraindicações oficiais, pois o texto aprovado pela ANVISA não estava disponível para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para glaucoma hereditário primário baseia-se apenas na pontuação do modelo (nível L5), sem ensaios, sem literatura e sem mecanismo plausível verificado. Além disso, todos os registros brasileiros estão cancelados e a bula não foi analisada, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança.
- Obter o mecanismo de ação detalhado (por exemplo, via DrugBank) para analisar uma ligação mecanística com o glaucoma.
- Realizar revisão sistemática da literatura sobre diuréticos tiazídicos e pressão intraocular, além de estudos pré-clínicos.
- Avaliar a compatibilidade de via de administração (a via sistêmica atual versus a via tópica ocular típica do glaucoma).
- Entre as demais previsões, o cor pulmonale crônico é a única com indício indireto e poderia ser tratado como questão de pesquisa, exigindo validação moderna.
- Avaliar a viabilidade regulatória e comercial, dado que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

