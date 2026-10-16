---
layout: default
title: Lemborexant
parent: Evidência Alta (L1-L2)
nav_order: 397
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-13
description: "Lemborexant: nova indicação prevista, Distúrbio do sono… (nível de evidência L1). Indicação original: Hipnóticos e sedativos"
---

# Lemborexant
{: .fs-9 }

Nível de evidência: **L1** | Indicações previstas: **1** 
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

# Lemborexante: De hipnótico e sedativo para distúrbio de início e manutenção do sono

## Resumo em Uma Frase

Lemborexante (DAYVIGO) é um hipnótico e sedativo, registrado originalmente na ANVISA na categoria "Hipnóticos e Sedativos".
O modelo TxGNN prevê que pode ser eficaz para **distúrbio do sono com dificuldade de iniciar e manter o sono (sleep disorder, initiating and maintaining sleep)**, mas essa previsão é praticamente a própria indicação já conhecida (insônia), e não um reposicionamento propriamente dito.
Atualmente há **0 ensaios clínicos registrados** nos dados compilados e **20 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipnóticos e sedativos |
| Nova Indicação Prevista | Distúrbio do sono, dificuldade de iniciar e manter o sono (sleep disorder, initiating and maintaining sleep) |
| Pontuação de Previsão TxGNN | 99,75% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Proceed with Guardrails |

> Observação sobre o nível de evidência: a classificação L1 foi atribuída com base no ensaio clínico de Fase 3 publicado (PMID 31880796) e em seus estudos de acompanhamento de longo prazo (SUNRISE 2), além de várias revisões sistemáticas e meta-análises em rede. Não há ensaios registrados nos dados compilados para este relatório.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação nos registros compilados. Pela literatura, porém, o lemborexante é um antagonista duplo dos receptores de orexina (DORA), que bloqueia reversivelmente os receptores OX1R e OX2R, com maior afinidade por OX2R. Ao inibir o sinal de orexina, que promove vigília e alerta, favorece o início e a manutenção do sono.

A indicação prevista (dificuldade de iniciar e manter o sono) corresponde ao uso já aprovado do fármaco para insônia em adultos, aprovado nos EUA (2019), no Japão e no Canadá. Portanto, não se trata de reposicionamento genuíno: o modelo recupera a indicação original, o que explica a pontuação muito alta.

O valor desta avaliação está, assim, em confirmar a coerência da previsão e em apontar a situação regulatória brasileira, já que o único registro encontrado está cancelado.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados nos dados compilados. Os ensaios de Fase 3 relevantes aparecem apenas por meio de suas publicações (tabela abaixo).

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Fase 3) | JAMA Netw Open | Lemborexante comparado com placebo e zolpidem de liberação prolongada em idosos com insônia |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Fase 3, SUNRISE 2) | Sleep | Eficácia e tolerabilidade de longo prazo versus placebo em adultos com insônia |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Fase 3, SUNRISE 2) | Sleep Med | Efetividade e segurança com até 12 meses de tratamento contínuo |
| [40244447](https://pubmed.ncbi.nlm.nih.gov/40244447/) | 2025 | Meta-análise | Naunyn-Schmiedeberg's Arch Pharmacol | Lemborexante versus placebo em 1.976 pacientes com insônia |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Revisão sistemática / meta-análise em rede | Transl Psychiatry | Comparação de eficácia e segurança de daridorexante, lemborexante e suvorexante |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Revisão sistemática / meta-análise em rede | Lancet | Efetividade comparada de tratamentos farmacológicos para insônia aguda e de longo prazo |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Revisão sistemática / meta-análise em rede | Drugs | Análise de 153 ensaios randomizados sobre eficácia e segurança de fármacos para insônia |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Meta-análise em rede | J Manag Care Spec Pharm | Eficácia comparada do lemborexante e de outros tratamentos para insônia |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Revisão (perfil de aprovação) | Drugs | Primeira aprovação do lemborexante (DAYVIGO) nos EUA em dezembro de 2019 para insônia em adultos |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Análise post-hoc | Sleep Med | Efeito do lemborexante na arquitetura do sono em insônia com apneia obstrutiva do sono leve |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 173100007 (cancelado) | DAYVIGO | Não informada | Hipnóticos e sedativos |

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento** (relações do grafo, não texto de bula): narcolepsia, síndrome de narcolepsia-cataplexia, doença do sistema nervoso central, esclerose concêntrica de Balo e adrenoleucodistrofia ligada ao X.
- **Interações medicamentosas**: foram identificadas 160 interações registradas. Entre as listadas, as de gravidade **maior** incluem ranitidina, aprepitanto, morfina (inclusive lipossomal), cimetidina, claritromicina e clotrimazol. As de gravidade **moderada** incluem pioglitazona, bupropiona, dexametasona, saxagliptina, difenoxina, difenoxilato, dronabinol, eliglustate, nabilona, naloxegol, fenilbutirato de glicerol, metoclopramida e metreleptina.
- **Cuidados gerais de classe**: efeito depressor do SNC (sonolência, comprometimento no dia seguinte), cautela com inibidores ou indutores fortes da CYP3A e com uso concomitante de outros depressores do SNC ou álcool.

Consulte a bula para as advertências e contraindicações oficiais, pois as informações da bula brasileira não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- A evidência clínica para insônia é sólida (ensaios de Fase 3 e meta-análises), mas a indicação prevista coincide com o uso já estabelecido, e o único registro no Brasil está cancelado, o que exige verificação regulatória antes de qualquer recomendação.

**Para prosseguir, é necessário:**
- Verificar a situação regulatória atual na ANVISA e o motivo do cancelamento do registro nº 173100007
- Obter e analisar a bula oficial (advertências e contraindicações)
- Confirmar os dados de mecanismo de ação em fonte primária (por exemplo, DrugBank)
- Definir plano de monitoramento: sonolência e comprometimento no dia seguinte, exclusão de pacientes com narcolepsia e revisão de interações com inibidores/indutores da CYP3A e depressores do SNC
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

