---
layout: default
title: Isotretinoin
parent: Apenas Predição do Modelo (L5)
nav_order: 377
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Isotretinoin: nova indicação prevista, Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension) (nível de evidência L5). Indicação original: Hipertensão / transtorno hipertensivo (confo…"
monitor_inn: "ISOTRETINOIN"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Isotretinoin
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

# Isotretinoína: Da hipertensão à hipertensão renovascular maligna

## Resumo em Uma Frase

Isotretinoína é um retinoide sistêmico; no grafo de conhecimento usado pelo modelo, seu uso original aparece registrado como transtorno hipertensivo/hipertensão, o que deve ser verificado (veja abaixo).
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão / transtorno hipertensivo (conforme o grafo de conhecimento; sem texto de indicação aprovada no Brasil) |
| Nova Indicação Prevista | Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension) |
| Pontuação de Previsão TxGNN | 99,01% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. A isotretinoína é um retinoide sistêmico, cujo perfil clínico conhecido é dermatológico (acne grave). Não é um anti-hipertensivo estabelecido.

Uma ligação plausível, porém não comprovada, é que a sinalização por retinoides influencia a remodelação vascular e a regulação do sistema renina-angiotensina, o que poderia ter relação com a patologia renovascular. Isso é especulativo e não foi verificado por nenhum estudo nos dados compilados.

As "indicações originais" registradas (hipertensão) conflitam com a farmacologia conhecida da isotretinoína e podem refletir um erro de mapeamento de dados. Isso deve ser conferido antes de qualquer avanço. A segunda previsão do modelo, **doença renal hipertensiva maligna**, tem exatamente a mesma pontuação (99,01%), sugerindo que ambas partem do mesmo sinal do grafo e não de evidências independentes. Estudos pré-clínicos com retinoides em modelos de lesão e fibrose renal existem, mas são indiretos e não constam nos dados compilados.

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (não é texto de bula): transtornos de ansiedade, neuróticos e distímicos; transtornos psicóticos e mentais (esquizofreniforme, esquizoafetivo); doença renal; doença hepática; doença da vesícula biliar; pancreatite; doença inflamatória intestinal; osteoporose (inclusive pós-menopausa); lúpus eritematoso sistêmico (inclusive pediátrico); angioedema (adquirido, hereditário, não histamínico e induzido por bloqueadores do SRAA); diabetes mellitus e cetoacidose diabética; deficiência de potássio; neutropenia e agranulocitose; piureter; hipotensão.
- **Interações Medicamentosas**: 98 interações registradas. Entre as de gravidade **Maior**: doxiciclina, minociclina, tetraciclina e vitamina A. Entre as de gravidade **Moderada**: corticosteroides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triancinolona), varfarina, dicumarol, naltrexona, nitisinona, etanol, fostamatinibe, ivacaftor, lumacaftor e abametapir (tópico).
- **Preocupações gerais do perfil conhecido**: teratogenicidade, dislipidemia e hepatotoxicidade, relevantes para pacientes com doença vascular e renal grave, que costumam usar vários anti-hipertensivos.
- As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se apoia apenas na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura. O mecanismo é desconhecido, a indicação original parece conflitar com a farmacologia conhecida do fármaco e o perfil de segurança é preocupante para essa população. O fármaco também não tem registro no Brasil.

**Para prosseguir, é necessário:**
- Verificar o possível erro de mapeamento das indicações originais (hipertensão) no grafo de conhecimento.
- Obter os dados de mecanismo de ação (MOA) no DrugBank.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), necessária para a triagem de segurança.
- Fazer uma busca sistemática de literatura e ensaios clínicos, incluindo estudos pré-clínicos de retinoides em modelos renais e vasculares.
- Avaliar a viabilidade regulatória, dado que não há registro vigente no Brasil e que a teratogenicidade exige programa de gerenciamento de risco.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

