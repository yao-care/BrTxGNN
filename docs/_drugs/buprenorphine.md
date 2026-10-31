---
layout: default
title: Buprenorphine
parent: Apenas Predição do Modelo (L5)
nav_order: 165
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
description: "Buprenorphine: nova indicação prevista, Porfiria Aguda Intermitente (Acute Intermittent Porphyria) (nível de evidência L5). Indicação original: Analgésicos narcóticos"
monitor_inn: "BUPRENORPHINE"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
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

## Buprenorfina: De analgésico narcótico para porfiria aguda intermitente
{: .text-alpha }

## Resumo em Uma Frase

Buprenorfina é um analgésico opioide, originalmente registrado na ANVISA como analgésico narcótico.
O modelo TxGNN prevê que possa ser eficaz para **Porfiria Aguda Intermitente (Acute Intermittent Porphyria)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (um relato de caso de manejo anestésico de 1993), que não demonstra eficácia no tratamento da doença.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgésicos narcóticos |
| Nova Indicação Prevista | Porfiria Aguda Intermitente (Acute Intermittent Porphyria) |
| Pontuação de Previsão TxGNN | 0,9941 |
| Nível de Evidência | L5 (apenas previsão do modelo; a literatura disponível é um relato de caso sem evidência de eficácia) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a buprenorfina é um agonista parcial do receptor opioide mu e antagonista do receptor kappa, usada para analgesia, e mecanisticamente não há uma ligação clara com a nova indicação.

A porfiria aguda intermitente é causada por um defeito na biossíntese do heme. Não se identificou relação mecanística entre a ação opioide da buprenorfina e esse defeito. O único trabalho encontrado descreve o manejo anestésico de uma paciente com porfiria, refletindo considerações de segurança perioperatória e analgesia opioide durante crises, e não modificação da doença.

Portanto, a pontuação elevada do TxGNN (0,9941) deve ser entendida como uma previsão computacional sem respaldo clínico. A plausibilidade mais realista seria o uso da buprenorfina como analgésico sintomático nas crises dolorosas, o que é diferente de tratar a doença.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Relato de caso | Masui (Jpn J Anesthesiol) | Manejo anestésico de uma paciente de 40 anos com suspeita de porfiria aguda intermitente submetida a cirurgia por tumor ovariano maligno; foca em segurança perioperatória, sem avaliar eficácia da buprenorfina na doença |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 122140137 (cancelado) | LUSANDA | Não informada | Analgésicos narcóticos |
| Registro 191980002 (cancelado) | RESTIVA | Não informada | Analgésicos narcóticos |
| Registro 186100012 (cancelado) | TRANSTEC | Não informada | Analgésicos |
| Registro 122140134 (cancelado) | BUPRENORFINA | Não informada | Analgésicos narcóticos |
| Registro 191980011 (cancelado) | NORPATCH | Não informada | Analgésicos narcóticos |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (TxGNN/PrimeKG, não texto de bula)**: síndrome de taquicardia postural ortostática, hipotensão ortostática, atrofia de múltiplos sistemas, síndrome do QT longo (incluindo familiar) e torsades de pointes, doença pulmonar obstrutiva crônica, insuficiência respiratória, doença hepática (incluindo hepatite B e C crônicas), doença da vesícula biliar, insuficiência adrenocortical/doença de Addison, hipotireoidismo/mixedema, hiperplasia prostática benigna, íleo paralítico e obstrução intestinal, estenose uretral, hipertensão intracraniana/pseudotumor cerebral, dependência e abuso de substâncias.
- **Interações Medicamentosas** (100 interações registradas; exemplos de gravidade maior): alvimopano, bupropiona, morfina, cisaprida e dolasetrona. Entre as de gravidade moderada: famotidina, hiosciamina, loperamida, aprepitanto, atropina, dexametasona, claritromicina, cimetidina, entre outras.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem evidência de eficácia; a única publicação é um relato de caso anestésico, e não há ligação mecanística plausível entre a buprenorfina e a porfiria aguda intermitente. Além disso, o medicamento é comercializado no Brasil, com 5 registros válidos de 5.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação e análise da ligação mecanística com a via de biossíntese do heme
- Bula da ANVISA com advertências e contraindicações, para triagem de segurança
- Evidências pré-clínicas ou clínicas específicas para porfiria aguda intermitente
- Avaliação da situação regulatória e da via de administração compatível
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

