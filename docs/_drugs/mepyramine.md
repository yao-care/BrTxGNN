---
layout: default
title: Mepyramine
parent: Apenas Predição do Modelo (L5)
nav_order: 444
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "mepyramine"
predicted_indications: ["nasal cavity disease"]
description: "Mepyramine: nova indicação prevista, Nasal cavity disease (nível de evidência L5). Indicação original: DESCONGESTIONANTES NASAIS TOPICOS"
---

# Mepyramine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Mepyramine: Nasal cavity disease
{: .text-alpha }

## Resumo em Uma Frase

A mepiramina (mepyramine) é um anti-histamínico de primeira geração, registrado no Brasil como descongestionante nasal tópico, analgésico contra enxaqueca e produto para o aparelho digestivo e metabolismo.
O modelo TxGNN prevê que pode ser eficaz para **urticária alérgica (allergic urticaria)**,
mas atualmente há **0 ensaios clínicos** e apenas **4 publicações** indiretas (estudos pré-clínicos e um estudo veterinário) relacionadas a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | DESCONGESTIONANTES NASAIS TOPICOS; ANALGESICOS CONTRA ENXAQUECA; OUTROS PRODUTOS PARA O APARELHO DIGESTIVO E METABOLISMO |
| Nova Indicação Prevista | Nasal cavity disease |
| Pontuação de Previsão TxGNN | 0.9974 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 3) |
| Número de Registros | 3 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a mepiramina é um antagonista do receptor H1 da histamina (anti-histamínico de primeira geração). Seu uso em reações alérgicas e urticária é classicamente descrito, e mecanisticamente é aplicável à urticária alérgica.

A urticária alérgica depende fortemente da ativação de mastócitos e da liberação de histamina, e o bloqueio do receptor H1 é a base do tratamento. Por isso, a previsão é coerente com a farmacologia conhecida do fármaco. Ressalte-se, porém, que isso é essencialmente o uso anti-histamínico clássico, e não um reposicionamento verdadeiramente novo.

A literatura disponível é indireta: estudos de eletrofisiologia sobre canais iônicos (canal KCNQ/M e canais de sódio de nociceptores), cinética de ligação ao receptor H1 e um estudo veterinário em cães com angioedema.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [21033572](https://pubmed.ncbi.nlm.nih.gov/21033572/) | 2010 | Estudo clínico veterinário (cães, angioedema) | Polish Journal of Veterinary Sciences | Em 27 cães com angioedema, randomizados para tratamento (n=15) ou placebo (n=12), concluiu-se que o maleato de mepiramina pode ser útil. |
| [34758144](https://pubmed.ncbi.nlm.nih.gov/34758144/) | 2021 | Estudo mecanístico pré-clínico | FASEB Journal | A mepiramina inibe diretamente diversos canais de sódio dependentes de voltagem em nociceptores, o que explica o alívio da dor tópica. |
| [18222495](https://pubmed.ncbi.nlm.nih.gov/18222495/) | 2008 | Eletrofisiologia pré-clínica (neurônios de rato) | Neuropharmacology | Mepiramina e difenidramina inibem diretamente o canal KCNQ/M e despolarizam neurônios, o que pode explicar efeitos neurotóxicos em superdose (convulsões). |
| [29371669](https://pubmed.ncbi.nlm.nih.gov/29371669/) | 2018 | Farmacologia in vitro | Scientific Reports | Desenvolvimento de sondas fluorescentes para o receptor H1 para estudar a cinética de ligação em células vivas. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102350145 (cancelado) | NARIDRIN | Não informada | Descongestionantes nasais tópicos |
| Registro nº 117170079 (cancelado) | ENJOY | Não informada | Analgésicos contra enxaqueca |
| Registro nº 178170093 (cancelado) | ENGOV | Não informada | Outros produtos para o aparelho digestivo e metabolismo |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (PrimeKG, não texto de bula)**: o grafo associa o fármaco a diversas condições, entre elas hipertensão, insuficiência hepática, epilepsia, DPOC, doença renal, pancreatite, hipotireoidismo, úlcera péptica, doença inflamatória intestinal, diabetes mellitus, cetoacidose diabética, hiperplasia prostática benigna, hipotensão, abuso/dependência de substâncias, rabdomiólise, doença arterial coronariana, infarto do miocárdio, hemoglobinopatias, colite por *Clostridium difficile* e enterocolite necrosante perinatal. Trata-se de relações do grafo e devem ser confirmadas na bula.
- **Interações Medicamentosas**: foram identificadas 382 interações. As de gravidade **Maior** incluem **cloreto de potássio** e **citrato de potássio**. As de gravidade **Moderada** incluem outros fármacos anticolinérgicos (atropina, escopolamina, hioscina/hiosciamina, glicopirrônio, diciclomina, propantelina, tróspio), opioides (morfina, ópio, loperamida), metoclopramida e dronabinol, com possível somação de efeitos anticolinérgicos e depressores do sistema nervoso central.
- Superdose de anti-histamínicos de primeira geração está associada a sonolência, convulsões e coma, conforme descrito na literatura compilada.

As advertências e contraindicações da bula brasileira não estão disponíveis; consulte a bula para informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é mecanisticamente plausível, mas corresponde ao uso anti-histamínico clássico e não há ensaios clínicos em humanos; a literatura é indireta (pré-clínica e veterinária).

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (MOA) a partir do DrugBank
- Buscar evidências clínicas em humanos (ensaios ou estudos observacionais) para urticária alérgica
- Comparar com anti-histamínicos de segunda geração, preferidos pelas diretrizes atuais
- Avaliar a viabilidade regulatória, já que não há registro vigente, e a compatibilidade de vias de administração
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

