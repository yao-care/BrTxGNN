---
layout: default
title: Cemiplimab
parent: Apenas Predição do Modelo (L5)
nav_order: 213
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Cemiplimab: nova indicação prevista, Carcinoma adenoescamoso da vesícula biliar (gallbladder adenosquamous… (nível de evidência L5). Indicação original: Antineoplásico"
monitor_inn: "cemiplimab"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "external ear basal cell carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
---

# Cemiplimab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Cemiplimabe: Do tratamento antineoplásico ao carcinoma adenoescamoso da vesícula biliar
{: .text-alpha }

## Resumo em Uma Frase

Cemiplimabe (LIBTAYO) é um anticorpo monoclonal que bloqueia o PD-1, registrado na ANVISA com a indicação genérica de "antineoplásico".
O modelo TxGNN prevê que pode ser eficaz para o **carcinoma adenoescamoso da vesícula biliar (gallbladder adenosquamous carcinoma)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Carcinoma adenoescamoso da vesícula biliar (gallbladder adenosquamous carcinoma) |
| Pontuação de Previsão TxGNN | 0,9999 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo as informações farmacológicas disponíveis, o cemiplimabe é um anticorpo que se liga ao PD-1 (CD279, gene PDCD1) humano e bloqueia a interação PD-1/PD-L1, com IC50 inferior a 1 nM em ELISA. Ele recebeu autorização da FDA em 2018 para o carcinoma espinocelular cutâneo (CSCC) metastático ou localmente avançado, e depois para o câncer de pulmão de células não pequenas (CPNPC) com alta expressão de PD-L1. Em outubro de 2025, foi aprovado também como tratamento adjuvante do CSCC.

A lógica da previsão é que o carcinoma adenoescamoso da vesícula biliar tem um componente escamoso, semelhante ao CSCC, no qual o fármaco já tem eficácia comprovada. Em princípio, o bloqueio do PD-1 poderia restaurar a resposta imune contra células tumorais também nesse contexto.

Essa ligação, porém, é puramente computacional. Não foram fornecidos ensaios nem literatura para este tumor biliar raro, e a similaridade com a indicação original ainda não foi avaliada. A previsão deve ser tratada como hipótese, não como evidência.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 122140130 (cancelado) | LIBTAYO | Não informada | Antineoplásico |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Imunoterapia (anticorpo anti-PD-1) |
| Risco de Mielossupressão | Baixo (não é um citotóxico convencional; consulte a bula) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Consulte as advertências e precauções na bula. De modo geral, recomenda-se acompanhar hemograma, função hepática, renal e tireoidiana, dada a possibilidade de eventos imunomediados |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 9 interações de gravidade moderada com corticosteroides: hidrocortisona, triancinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona e deflazacorte. Os corticosteroides podem reduzir o efeito de um inibidor de checkpoint imune, e seu uso deve ser avaliado caso a caso.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão tem pontuação alta no modelo (0,9999), mas não conta com nenhum ensaio clínico nem publicação para o carcinoma adenoescamoso da vesícula biliar (nível L5). Além disso, o único registro na ANVISA está cancelado.

**Para prosseguir, é necessário:**
- Realizar busca dirigida de ensaios e literatura sobre cemiplimabe ou inibidores de PD-1 em tumores biliares e adenoescamosos
- Obter e analisar a bula da ANVISA (advertências e contraindicações)
- Obter dados detalhados do mecanismo de ação (MOA)
- Esclarecer a situação regulatória no Brasil, já que o registro está cancelado
- Avaliar a viabilidade da via de administração e a similaridade com a indicação original
- Avaliar o uso concomitante de corticosteroides

**Observação sobre outras previsões:** entre as 10 principais, o carcinoma basocelular da orelha externa é o único com algum respaldo (nível L4): um relato de caso (PMID [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/), 2021, *Clinical and Experimental Dermatology*) descreve resposta duradoura após a suspensão do cemiplimabe no carcinoma basocelular localmente avançado. É um dado anedótico e não específico da orelha externa, mas pode justificar uma questão de pesquisa. As demais previsões (carcinomas espinocelulares da glote, da supraglote e sinonasal, carcinoma cloacogênico retal, carcinoma adenoescamoso da próstata e do pâncreas, carcinoma verrucoso uretral e carcinoma espinocelular oculto do pulmão) permanecem apenas como previsões do modelo, sem evidência (L5, Hold).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

