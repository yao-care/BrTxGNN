---
layout: default
title: Iopamidol
parent: Apenas Predição do Modelo (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Iopamidol: nova indicação prevista, Angina de Prinzmetal (Prinzmetal angina) (nível de evidência L5). Indicação original: Não informada nos dados compilados"
monitor_inn: "Iopamidol"
predicted_indications: ["Prinzmetal angina", "female breast carcinoma", "migraine with brainstem aura", "migraine disorder", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "hemoglobinopathy", "pulmonary hypertension", "fibromyalgia"]
---

# Iopamidol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Iopamidol: De agente de contraste radiológico à angina de Prinzmetal

## Resumo em Uma Frase

Iopamidol é um meio de contraste radiográfico iodado não iônico, usado em exames de imagem diagnóstica. Não há indicação terapêutica original registrada nos dados compilados para o Brasil.
O modelo TxGNN prevê que pode ser eficaz para **angina de Prinzmetal (Prinzmetal angina)**, mas essa previsão se baseia apenas em grafo de conhecimento: há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não informada nos dados compilados |
| Nova Indicação Prevista | Angina de Prinzmetal (Prinzmetal angina) |
| Pontuação de Previsão TxGNN | 98,57% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Iopamidol é conhecido como um contraste iodado não iônico de baixa osmolaridade, usado para visualizar estruturas em exames radiológicos, e não como fármaco com ação terapêutica direta.

Não foi estabelecida relação mecanística com a angina de Prinzmetal, que é causada por vasoespasmo coronariano. Iopamidol não tem farmacologia vasodilatadora ou antiespástica conhecida. Ele é usado de forma diagnóstica em angiografia coronariana, o que não é um efeito terapêutico sobre o vasoespasmo.

A pontuação alta (0,986) reflete provavelmente similaridade de rede no grafo de conhecimento, e não um efeito farmacológico real. Por isso, a previsão deve ser tratada com cautela.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a angina de Prinzmetal.

### Outras indicações previstas com literatura (contexto)

Para outras previsões do modelo, a literatura existente trata sobretudo de usos diagnósticos ou de segurança, e não de efeito terapêutico:

| Indicação prevista | Evidência disponível | Interpretação |
|------|------|------|
| Carcinoma de mama feminino (98th percentil de score: 97,91%) | Linfografia por TC para mapeamento de linfonodo-sentinela (ex.: [14699178](https://pubmed.ncbi.nlm.nih.gov/14699178/), [14976475](https://pubmed.ncbi.nlm.nih.gov/14976475/), [15905719](https://pubmed.ncbi.nlm.nih.gov/15905719/)); imagem acidoCEST por RM para pH tumoral ([26108564](https://pubmed.ncbi.nlm.nih.gov/26108564/), [27572810](https://pubmed.ncbi.nlm.nih.gov/27572810/)) | Uso diagnóstico, sem atividade antitumoral (L4) |
| Hipertensão pulmonar (96,16%) | Angiografia pulmonar com iopamidol: hemodinâmica e segurança ([3659354](https://pubmed.ncbi.nlm.nih.gov/3659354/), [8539407](https://pubmed.ncbi.nlm.nih.gov/8539407/)) | Segurança diagnóstica, sem benefício terapêutico (L4) |
| Hemoglobinopatia (96,43%) | Estudo in vitro sobre falcização ([7089282](https://pubmed.ncbi.nlm.nih.gov/7089282/)) | Compatibilidade do contraste, sem benefício terapêutico (L4) |
| Tendinite (96,70%) | Visualização radiográfica de enxertos tendinosos ([9442336](https://pubmed.ncbi.nlm.nih.gov/9442336/)) | Técnica de imagem (L4) |
| Enxaqueca com aura do tronco encefálico, enxaqueca, miosite fibrosa, miosite granulomatosa idiopática, fibromialgia | Nenhuma | Apenas previsão do modelo (L5) |

## Informações de Comercialização no Brasil

Não há registros de iopamidol nos dados compilados para o Brasil.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações, sendo as listadas de gravidade **Maior**, entre elas: hidrocortisona, metformina, anfotericina B (incluindo formulações lipídica, lipossomal e sulfato de colesterila), bupropiona, mesalazina, balsalazida, triancinolona, dexametasona, betametasona, morfina, vancomicina, dietilpropiona, fenfluramina, dexfenfluramina, femtermina, efedrina e dronabinol.
- Em pacientes com hemoglobinopatia falciforme, um estudo in vitro sugere que contrastes não iônicos como o iopamidol causam menos falcização do que os iônicos.
- Os dados de advertências e contraindicações da bula brasileira não estavam disponíveis. Consulte a bula para informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para angina de Prinzmetal tem apenas suporte computacional (L5): sem ensaios, sem literatura e sem mecanismo plausível. As demais indicações com literatura referem-se a usos diagnósticos ou de segurança, não a reposicionamento terapêutico.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação a partir do DrugBank.
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Confirmar a situação regulatória no Brasil (nenhum registro foi identificado).
- Gerar evidência pré-clínica de efeito vasodilatador/antiespástico antes de qualquer avanço.
- Avaliar, separadamente, as aplicações diagnósticas (linfografia por TC e imagem acidoCEST) como possíveis novas indicações de imagem, e não como reposicionamento terapêutico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

