---
layout: default
title: Inositol
parent: Apenas Predição do Modelo (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Inositol: nova indicação prevista, Trombose da veia porta primitiva (primitive portal vein thrombosis) (nível de evidência L5). Indicação original: Pelagra, beribéri, hipertrigliceridemia…"
monitor_inn: "INOSITOL"
predicted_indications: ["primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatoportal sclerosis", "hepatic porphyria", "congestive heart failure", "hyperlipoproteinemia", "acute pulmonary heart disease", "glycogen storage disease due to hepatic glycogen synthase deficiency"]
---

# Inositol
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

## Inositol: Das indicações lipídicas e nutricionais à trombose portal primitiva (previsão computacional)
{: .text-alpha }

## Resumo em Uma Frase

Inositol foi originalmente associado ao tratamento de condições como pelagra, beribéri, hipertrigliceridemia, hiperlipidemia familiar combinada e hipoalfalipoproteinemia.
O modelo TxGNN prevê que pode ser eficaz para **Trombose da Veia Porta Primitiva (primitive portal vein thrombosis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção, ou seja, é apenas uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Pelagra, beribéri, hipertrigliceridemia, hiperlipidemia familiar combinada, hipoalfalipoproteinemia (conforme o grafo de conhecimento; não há texto de indicação aprovada no Brasil) |
| Nova Indicação Prevista | Trombose da veia porta primitiva (primitive portal vein thrombosis) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o inositol é um composto envolvido no metabolismo lipídico e na sinalização celular (via fosfoinositídeos e IP3), e as indicações originais registradas no grafo de conhecimento são lipídicas e nutricionais.

Os dados compilados para este relatório **não sustentam um vínculo mecanístico** entre o inositol e a trombose da veia porta. A pontuação do modelo é muito alta (99,98%), mas é idêntica à de várias outras doenças hepáticas e portais (cirrose associada ao cobre, hipertensão portal familiar não cirrótica, síndrome hepatopulmonar, esclerose hepatoportal), o que sugere um artefato computacional e não um sinal biológico específico. Não há ensaios clínicos nem literatura para essa indicação.

Outras previsões do mesmo fármaco apresentam algum respaldo indireto:
- **Hiperlipoproteinemia** (pontuação 99,40%, nível L3): é a mais próxima das indicações originais. Há estudos clínicos antigos (1976–1983) com a combinação de clofibrato e nicotinato de inositol, que reduziram colesterol e triglicerídeos. Contudo, o efeito é confundido pelo clofibrato e pelo éster de ácido nicotínico, e a indicação se sobrepõe às já existentes, portanto não é um reposicionamento realmente novo.
- **Insuficiência cardíaca congestiva** (pontuação 99,44%, nível L4): a literatura é majoritariamente pré-clínica ou mecanística. Um estudo de coorte de 2024 relata mio-inositol plasmático elevado em pacientes com insuficiência cardíaca, o que é uma associação de biomarcador e pode até indicar direção oposta à benéfica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (trombose da veia porta primitiva).

## Informações de Comercialização no Brasil

O inositol não possui registros ativos na ANVISA nos dados compilados (0 registros; situação: não comercializado).

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento TxGNN** (não provêm de bula): doença hepática, doença da vesícula biliar, trombocitopenia, hiperglicemia, úlcera péptica, diabetes mellitus, cetoacidose diabética, distúrbios hipotensivos, gota, abuso/dependência de substâncias, distúrbios da coagulação sanguínea, síndrome coronariana aguda, doença arterial coronariana, AVC e doenças cerebrovasculares (incluindo infarto cerebral e oclusão de artéria cerebral), infarto do miocárdio, trombose coronariana, hemoglobinopatias e hipofosfatemia.
- **Relevância para a indicação prevista:** as contraindicações de doença hepática e de distúrbios da coagulação merecem atenção especial em um cenário de trombose portal.
- Não foram encontradas interações medicamentosas nos dados consultados.

Consulte a bula para advertências e contraindicações formais, pois o texto aprovado pela ANVISA não estava disponível.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (trombose da veia porta primitiva) baseia-se apenas em pontuação do modelo, sem ensaios, sem literatura e sem vínculo mecanístico documentado; a pontuação é idêntica à de várias outras condições hepáticas, o que enfraquece sua especificidade.
- O fármaco não está comercializado no Brasil e as contraindicações do grafo incluem doença hepática e distúrbios da coagulação.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (por exemplo, consulta à API do DrugBank)
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança
- Revisão sistemática da literatura sobre inositol e trombose/hipertensão portal
- Avaliação de candidatas alternativas com mais respaldo (hiperlipoproteinemia, com estudos isolados de inositol sem clofibrato; insuficiência cardíaca, apenas como questão de pesquisa)
- Avaliação de compatibilidade de vias de administração e de situação regulatória no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

