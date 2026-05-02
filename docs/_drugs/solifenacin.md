---
layout: default
title: Solifenacin
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Solifenacin
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

Analisando o Evidence Pack de Solifenacin (DB01591) e gerando o relatório conforme o formato especificado:

---

# Solifenacin: Da Bexiga Hiperativa à Doença Renal Policística 3

## Resumo em Uma Frase

Solifenacin é um antagonista seletivo do receptor muscarínico M3, originalmente aprovado para o tratamento da **bexiga hiperativa (Overactive Bladder – OAB)**, aliviando sintomas de urgência miccional, frequência urinária elevada e incontinência de urgência.
O modelo TxGNN prevê que pode ser eficaz para **Doença Renal Policística 3 com ou sem Doença Hepática Policística (polycystic kidney disease 3 with or without polycystic liver disease)**,
atualmente com **0 ensaios clínicos** e **20 publicações** relacionadas ao tema — embora a literatura encontrada aborde a doença em geral, sem referência direta ao uso de solifenacin.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Bexiga hiperativa (OAB) — urgência miccional, frequência urinária e incontinência de urgência |
| Nova Indicação Prevista | Doença Renal Policística 3 com ou sem Doença Hepática Policística |
| Pontuação de Previsão TxGNN | 97,13% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Segundo informações farmacológicas conhecidas, Solifenacin é um antagonista muscarínico seletivo para receptores M3. Seu mecanismo central consiste em bloquear esses receptores na musculatura detrusora da bexiga, inibindo contrações induzidas por acetilcolina e, consequentemente, reduzindo urgência e frequência miccionais. É a base de sua eficácia aprovada na bexiga hiperativa.

A Doença Renal Policística tipo 3 (PKD3) é causada por mutações nos genes **GANAB** e **SEC63**, que provocam cistogênese progressiva por meio de desregulação das vias de sinalização **mTOR/cAMP** e defeitos no dobramento de proteínas no retículo endoplasmático. Trata-se de uma condição de natureza estrutural e genética, com fisiopatologia completamente distinta da bexiga hiperativa.

**Não há plausibilidade mecanística estabelecida** entre o bloqueio de receptores M3 muscarínicos e a patogênese da PKD3. A análise de reposicionamento indica que a alta pontuação TxGNN provavelmente resulta de um efeito de agrupamento de nós de "doença renal" no grafo de conhecimento — fruto da proximidade topológica no KG —, e não de uma relação farmacológica direta. Todas as 20 publicações identificadas abordam a PKD/doença hepática policística em termos gerais (revisões, diretrizes clínicas, estudos genéticos), sem qualquer referência ao uso de solifenacin nessa indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Solifenacin em Doença Renal Policística 3.

---

## Evidências da Literatura

> ⚠️ As publicações abaixo abordam a doença-alvo (PKD3/Doença Hepática Policística) em termos gerais — diagnóstico, genética, fisiopatologia e manejo —, **sem nenhuma referência ao uso de solifenacin** nessa indicação. Servem apenas para contextualização da doença.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Diretriz Clínica | Am J Gastroenterology | Diretrizes ACG para lesões focais hepáticas; abrange diagnóstico e manejo da doença hepática policística |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Diretriz Clínica | J Hepatology | Diretrizes EASL para doenças císticas hepáticas, incluindo ADPKD e ADPLD — diagnóstico e tratamento |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Revisão | Lancet | ADPKD é a doença renal hereditária mais comum; revisão de manifestações clínicas sistêmicas e novas terapias |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Revisão | Clin Liver Dis | ADPKD como causa de insuficiência renal em estágio terminal; tolvaptana retarda deterioração renal e crescimento de cistos |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Revisão | JASN | Sobreposição fenotípica e genotípica entre ADPKD e ADPLD; oito genes causativos identificados, incluindo GANAB |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Revisão | Adv Kidney Dis Health | Espectro genético das doenças policísticas renais e hepáticas; PKD1 responde por ~80% dos casos |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Revisão | Annu Rev Pathol | Mecanismos primários, secundários e terciários da cistogênese hepática na DHP — potenciais alvos terapêuticos |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Ciência Básica | J Clin Invest | Sequenciamento de exoma em 102 pacientes: identifica GANAB (e outros) como genes causativos da PCLD isolada |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Revisão | Adv Kidney Dis Health | Fígado é o sítio extrarenal mais comum na ADPKD; minoria sintomática desenvolve complicações por hepatomegalia |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Estudo Clínico | Ann Transplant | Transplante combinado fígado-rim em DHP/DRP: análise retrospectiva de 9 pacientes (2015–2024) — desfechos cirúrgicos |

---

## Informações de Comercialização no Brasil

Solifenacin possui **20 registros** ativos na ANVISA e está comercializado no Brasil. Os dados detalhados de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no Evidence Pack atual e devem ser consultados diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para PKD3 apresenta apenas evidência de nível L5 — baseada exclusivamente no modelo, sem ensaios clínicos, sem literatura específica sobre solifenacin nessa indicação e sem plausibilidade mecanística estabelecida entre o antagonismo M3 muscarínico e a fisiopatologia da doença renal policística por mutação GANAB/SEC63.

> 💡 **Nota:** Entre as 10 indicações previstas pelo TxGNN para Solifenacin, a **Bexiga de Baixa Complacência (Low Compliance Bladder)** — ranking 7, pontuação 95,37% — apresenta evidência de nível **L3** com 2 ensaios clínicos e 11 publicações, incluindo RCTs. Essa indicação tem forte plausibilidade mecanística (o M3 é o receptor central na fisiopatologia do detrusor hiperativo) e recebeu recomendação **Proceed with Guardrails**, sendo a mais promissora do portfólio.

**Para prosseguir com PKD3, é necessário:**
- Identificar hipótese mecanística plausível que conecte o antagonismo M3 à cistogênese renal (ex.: papel da sinalização colinérgica em células do túbulo renal ou ductos biliares)
- Obter estudos pré-clínicos em modelos de cisto renal com solifenacin ou análogos antimuscarínicos
- Consultar especialistas em nefrologia para avaliar se há qualquer base racional para investigação
- Recuperar dados detalhados dos registros ANVISA e bula para avaliação completa de segurança (dados de advertências e contraindicações ausentes no Pack atual)
---

