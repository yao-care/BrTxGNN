---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using `txgnn-pipeline` to orient context, then generating the repurposing report per the v5 prompt spec.

---

# Digoxin: Da insuficiência cardíaca à angina de Prinzmetal

## Resumo

Digoxin é um glicosídeo cardíaco com longa história de uso clínico no tratamento da insuficiência cardíaca congestiva e no controle da frequência ventricular em fibrilação atrial.
O modelo TxGNN prevê que pode ser eficaz para **Angina de Prinzmetal (Prinzmetal angina)**, com pontuação de **99,81%** — contudo, não há ensaios clínicos registrados e apenas **2 publicações** perifericamente relacionadas apoiam esta direção, resultando em evidência de nível L5.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Insuficiência cardíaca congestiva / Fibrilação atrial (detalhes regulatórios não disponíveis neste pack) |
| Nova Indicação Prevista | Angina de Prinzmetal (Prinzmetal angina) |
| Pontuação de Previsão TxGNN | 99,81% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base no conhecimento farmacológico estabelecido, Digoxin é um inibidor da Na⁺/K⁺-ATPase que eleva o cálcio intracelular nos cardiomiócitos (efeito inotrópico positivo) e potencializa o tono vagal (parassimpático), reduzindo a frequência cardíaca. Suas indicações consolidadas incluem insuficiência cardíaca sistólica com fração de ejeção reduzida e controle da resposta ventricular na fibrilação atrial.

A angina de Prinzmetal é causada por espasmo transitório das artérias coronárias, mediado principalmente por hiperreatividade adrenérgica α e serotoninérgica da musculatura lisa vascular — não por obstrução aterosclerótica fixa. O tratamento padrão consiste em antagonistas dos canais de cálcio (ex.: verapamil, diltiazem) e nitratos de ação prolongada, que relaxam diretamente a musculatura lisa coronariana.

A ligação mecanística entre Digoxin e a angina de Prinzmetal é **biologicamente implausível**: o efeito vagotônico do fármaco não antagoniza o espasmo coronariano α-adrenérgico/serotoninérgico e, mais preocupante, há relatos na literatura de que a estimulação vagal pode **precipitar** espasmo coronariano em pacientes susceptíveis. A alta pontuação TxGNN (99,81%) reflete, muito provavelmente, proximidade topológica no grafo de conhecimento cardiovascular — Digoxin e angina de Prinzmetal compartilham muitos nós intermediários (frequência cardíaca, isquemia, sistema nervoso autônomo) —, e não uma associação farmacológica real com potencial terapêutico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Narrative Review | Chinese Medical Sciences Journal | Reavaliação de 30 pacientes com angina decubitus: a condição foi associada a lesões coronárias obstrutivas graves e aumento do consumo miocárdico de oxigênio — não ao espasmo coronariano isolado característico da angina de Prinzmetal |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | Revisão sobre cronofarmacogia e tratamento anti-hipertensivo; discute ritmos circadianos em doenças cardiovasculares — sem menção a Digoxin ou angina vasospástica |

> ⚠️ **Nota**: Nenhuma das publicações investiga diretamente o uso de Digoxin no tratamento da angina de Prinzmetal. A relevância é periférica e o nível de evidência permanece L5.

---

## Informações de Comercialização no Brasil

Digoxin possui **20 registros** ativos junto à ANVISA e encontra-se comercializado no Brasil. Os dados detalhados dos registros individuais (nome comercial, forma farmacêutica, indicação aprovada) não foram coletados nesta versão do Evidence Pack. Para consulta completa, acesse o portal ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe suporte mecanístico para o uso de Digoxin na angina de Prinzmetal — o perfil farmacológico do fármaco (vagotônico, inotrópico positivo) é incompatível com o mecanismo de espasmo coronariano, e a estimulação vagal pode inclusive agravar o quadro vasospástico. A ausência total de ensaios clínicos e de literatura primária relevante, combinada com uma análise mecanística contraindicatória, torna esta previsão um artefato topológico do modelo TxGNN, sem valor clínico imediato.

**Para prosseguir, é necessário:**
- Completar os dados regulatórios da ANVISA: nomes comerciais, formas farmacêuticas e indicações aprovadas por registro
- Obter dados de mecanismo de ação (MOA) via DrugBank API (DB00390)
- Baixar e parsear a bula ANVISA para advertências, contraindicações e interações medicamentosas
- Realizar revisão farmacológica especializada sobre efeito de Digoxin em musculatura lisa vascular coronariana antes de qualquer decisão de desenvolvimento
- Avaliar as demais indicações previstas (postos 2–6) sob perspectiva de maior plausibilidade mecanística, especialmente à luz dos dados de segurança disponíveis
---

