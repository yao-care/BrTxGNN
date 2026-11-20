---
layout: default
title: Tezacaftor
parent: Apenas Predição do Modelo (L5)
nav_order: 628
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Tezacaftor"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
description: "Tezacaftor: nova indicação prevista, Doença infecciosa por HIV (HIV infectious disease) (nível de evidência L5). No Brasil, registros na ANVISA: 3 (ativos: 3)"
---

# Tezacaftor
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

## Tezacaftor: Doença infecciosa por HIV (HIV infectious disease)
{: .text-alpha }

## Resumo em Uma Frase

Tezacaftor é um corretor da proteína CFTR, originalmente usado no tratamento da fibrose cística, em associação com outros moduladores de CFTR.
O modelo TxGNN prevê que pode ser eficaz para **Doença infecciosa por HIV (HIV infectious disease)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Doença infecciosa por HIV (HIV infectious disease) |
| Pontuação de Previsão TxGNN | 0.9924 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 3) |
| Número de Registros | 3 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para vanzacaftor, tezacaftor, and deutivacaftor (associação que contém Tezacaftor) (tradução não oficial): “O vanzacaftor e o tezacaftor ligam-se a sítios diferentes da proteína CFTR e têm um efeito aditivo na facilitação do processamento e do tráfego celular de determinadas formas mutantes da CFTR (incluindo a F508del- CFTR), aumentando a quantidade de proteína CFTR transportada para a superfície celular em comparação com cada molécula isoladamente. O efeito combinado de vanzacaftor, tezacaftor e deutivacaftor é o aumento da quantidade e da função da CFTR na superfície celular, resultando em aumento da atividade da CFTR, conforme medido tanto pelo transporte de cloreto mediado pela CFTR in vitro quanto pelo cloreto no suor em pacientes com FC.” Texto original em inglês: "Vanzacaftor and tezacaftor bind to different sites on the CFTR protein and have an additive effect in facilitating the cellular processing and trafficking of select mutant forms of CFTR (including F508del- CFTR) to increase the amount of CFTR protein delivered to the cell surface compared to either molecule alone. The combined effect of vanzacaftor, tezacaftor and deutivacaftor is increased quantity and function of CFTR at the cell surface, resulting in increased CFTR activity as measured both by CFTR-mediated chloride transport in vitro and by sweat chloride in patients with CF." ([DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20), versão de 2026-08-26; acessado em 2026-11-19). Segundo informações conhecidas, o tezacaftor é um corretor da CFTR: melhora o enovelamento e o transporte da proteína CFTR até a superfície celular. Foi aprovado pela primeira vez em 2018 em combinação de dose fixa com ivacaftor (Symdeko®) e também integra terapias triplas, como Trikafta® e Alyftrek®, para fibrose cística com mutações genéticas específicas. O alvo farmacológico registrado é o CFTR humano.

A previsão para HIV se apoia unicamente na pontuação elevada do modelo TxGNN (deep learning) (0,9924), que pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, e não evidência biológica. Com os dados compilados para este relatório, não se identifica um caminho mecanístico entre a correção da CFTR e atividade antiviral ou a patogênese do HIV. O candidato seguinte na lista (hanseníase) também parece refletir semelhanças aprendidas pelo modelo, e não uma justificativa biológica independente.

Portanto, a razoabilidade desta previsão é baixa e deve ser tratada como hipótese a ser testada, não como indicação de eficácia.

## Outras Indicações Previstas (para referência)

Todas com nível L5, sem ensaios clínicos nem literatura, e recomendação Hold:

| Posição | Indicação | Pontuação TxGNN |
|------|------|------|
| 2 | Hanseníase | 0,9914 |
| 3 | Neoplasia endócrina múltipla | 0,9906 |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Interações Medicamentosas

Foi identificada uma entrada de farmacologia: o tezacaftor tem como alvo a proteína humana **CFTR** (gene *CFTR*), o que corresponde ao seu mecanismo esperado como corretor. Não foram listadas interações com outros medicamentos nem níveis de gravidade.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é apenas computacional (L5), sem ensaios clínicos, sem literatura e sem vínculo mecanístico plausível entre a correção da CFTR e o HIV.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA ou fontes equivalentes, com advertências e contraindicações, para a triagem de segurança
- Complementar os dados de mecanismo de ação (MOA) a partir do DrugBank
- Realizar estudos pré-clínicos (por exemplo, atividade antiviral in vitro contra HIV) para avaliar se há algum fundamento biológico
- Revisar sistematicamente a literatura para confirmar a ausência de evidências
- Avaliar a compatibilidade de vias de administração e a viabilidade regulatória, já que não há registro no Brasil

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

