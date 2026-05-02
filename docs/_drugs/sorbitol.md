---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

O skill `txgnn-pipeline` confirma que este é um projeto TxGNN standard. Agora vou gerar o relatório completo seguindo o prompt v5.

---

# Sorbitol: De laxativo osmótico à hipertermia maligna induzida por exercício

## Resumo em Uma Frase

Sorbitol é um álcool de açúcar (poliol) amplamente utilizado como laxativo osmótico, excipiente farmacêutico e adoçante em formulações medicamentosas. O modelo TxGNN prevê que pode ser eficaz para **Hipertermia Maligna Induzida por Exercício (Exercise-induced Malignant Hyperthermia)**, com pontuação de previsão de **99.40%**; porém, atualmente esta indicação conta com **zero ensaios clínicos** e **zero publicações** de suporte direto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Laxativo osmótico / excipiente farmacêutico (dados de registro não disponíveis no Evidence Pack) |
| Nova Indicação Prevista | Hipertermia Maligna Induzida por Exercício (Exercise-induced Malignant Hyperthermia) |
| Pontuação de Previsão TxGNN | 99.40% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) disponíveis no Evidence Pack. Com base em conhecimento farmacológico geral, o sorbitol é um álcool de açúcar de seis carbonos que atua primariamente como agente osmótico: retém água no lúmen intestinal produzindo efeito laxativo; e, quando administrado por via intravenosa, pode exercer diurese osmótica de modo similar ao manitol. No metabolismo endógeno, o sorbitol é gerado pela via do poliol (aldose redutase converte glicose em sorbitol), uma via particularmente relevante em estados de hiperglicemia.

A hipertermia maligna induzida por exercício é causada por mutações nos genes *RYR1* e *CACNA1S*, que comprometem os canais de liberação de cálcio do retículo sarcoplasmático. Durante exercício intenso ou exposição a agentes desencadeantes, ocorre liberação descontrolada de cálcio intracelular nas células musculares esqueléticas, resultando em rigidez muscular grave, hipertermia extrema e colapso metabólico. Não há mecanismo farmacológico estabelecido que conecte o efeito osmótico do sorbitol ou a via do poliol à fisiopatologia de canais RYR1/CACNA1S.

A alta pontuação computacional do TxGNN (99.40%) provavelmente reflete associações indiretas no grafo de conhecimento — possivelmente por caminhos distantes envolvendo metabolismo energético muscular — sem suporte de plausibilidade biológica direta. A própria análise de repurposing rationale do Evidence Pack classifica esta previsão como possível **erro do modelo ou falsa associação por grafo**. A ausência completa de evidências clínicas e pré-clínicas confirma o nível L5.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O sorbitol possui **20 registros** na ANVISA e está atualmente comercializado no Brasil. Os dados detalhados de cada registro (número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis no Evidence Pack atual — os campos retornaram vazios. Para consulta completa, acesse o sistema de consulta de medicamentos da ANVISA diretamente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para hipertermia maligna induzida por exercício não possui plausibilidade biológica — não há mecanismo farmacológico conhecido que conecte o sorbitol à fisiopatologia de canais RYR1/CACNA1S — e está completamente desprovida de evidências clínicas ou pré-clínicas (L5). A alta pontuação computacional, neste caso, reflete provavelmente uma associação espúria no grafo de conhecimento.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) via DrugBank API (DG002, severidade: High) para avaliar qualquer ligação com metabolismo muscular ou homeostase do cálcio
- Descarregar e analisar as bulas registradas na ANVISA para preencher dados de segurança, advertências e contraindicações (DG001, severidade: Blocking)
- Considerar redirecionar esforços analíticos para indicações de menor rank mas maior plausibilidade: **Otite Média Infecciosa (rank 4, L4)** — onde xylitol (estrutura análoga) tem RCT com grau B de relevância, sugerindo que o sorbitol pode partilhar mecanismo de interferência na adesão bacteriana — é o candidato com melhor fundamento biológico neste Evidence Pack
- Preencher os dados de registro da ANVISA para completar a seção de comercialização
---

