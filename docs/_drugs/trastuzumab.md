---
layout: default
title: Trastuzumab
parent: Apenas Predição do Modelo (L5)
nav_order: 651
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
monitor_inn: "Trastuzumab"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: nova indicação prevista, Malignant cutaneous granular cell skin tumor (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Trastuzumab
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

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## Resumo em Uma Frase

Trastuzumabe é um anticorpo monoclonal anti-HER2, originalmente usado no tratamento do carcinoma de mama HER2-positivo.
O modelo TxGNN prevê que pode ser eficaz para **câncer de mama com receptor de progesterona positivo (progesterone-receptor positive breast cancer)**,
atualmente com **13 ensaios clínicos** e **20 publicações** apoiando esta direção. Na prática, trata-se de um subgrupo da indicação original (tumores HR+/HER2+), e não de um reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Malignant cutaneous granular cell skin tumor |
| Pontuação de Previsão TxGNN | 0.9948 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 14 de 14) |
| Número de Registros | 14 (ativos: 14) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base de dados consultada. Segundo informações conhecidas, o trastuzumabe liga-se ao domínio extracelular do HER2, inibe a sinalização mediada por esse receptor e induz citotoxicidade celular dependente de anticorpo (ADCC).

Uma fração substancial dos cânceres de mama HER2-positivos também expressa receptor de progesterona (perfil HR+/HER2+, ou "triplo-positivo"). Assim, a nova indicação prevista é, na prática, um subgrupo da indicação original, e não uma indicação totalmente nova. A evidência para pacientes HER2-positivos é sólida. Já o benefício em doença PR-positiva HER2-negativa não é sustentado; as exceções são cenários HER2-low, que usam trastuzumabe deruxtecana, um produto diferente.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Concluído | 3270 | Ensaio adjuvante randomizado: quimioterapia isolada vs. quimioterapia + trastuzumabe em câncer de mama inicial; inclui pacientes HR+ |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Concluído | 517 | Biossimilar de pertuzumabe (QL1209) + trastuzumabe + docetaxel em HER2+ e ER/PR-negativo; foco em equivalência, não em PR+ |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Retirado | 0 | Trastuzumabe com ou sem tamoxifeno em doença estágio IV ER/PR+ e HER2+; diretamente pertinente, mas sem participantes, portanto sem evidência |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Concluído | 92 | Quimioterapia neoadjuvante com e sem trastuzumabe |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | Concluído | 36 | Cabozantinibe isolado ou com trastuzumabe em metástases cerebrais; estudo pequeno e exploratório |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Concluído | 33 | Letrozol + trastuzumabe em doença metastática ErbB2+ e ER e/ou PR+ |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | Concluído | 50 | Quimioterapia neoadjuvante seguida de trastuzumabe em HER2+; estudo pequeno |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recrutando | 30 | Neratinibe + terapia endócrina + trastuzumabe pré-operatório em ER+/HER2+ |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Desconhecido | 34 | Palbociclibe, trastuzumabe, pirotinibe e fulvestranto em metástases cerebrais ER/PR+ e HER2+ |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Concluído | 37 | Everolimo, letrozol e trastuzumabe em tumores HR+/HER2+; estudo de dose e segurança |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | Análise de 5 anos do NeoSphere: pertuzumabe + trastuzumabe neoadjuvante em câncer de mama HER2+ (sobrevida livre de progressão e de doença, segurança) |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciclibe + trastuzumabe ± fulvestranto vs. quimioterapia + trastuzumabe em HR+/HER2+ avançado |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT HER2+/HR-: bloqueio duplo neoadjuvante com ou sem paclitaxel |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | ExteNET: neratinibe após terapia adjuvante com trastuzumabe em HER2+ inicial |
| [41780642](https://pubmed.ncbi.nlm.nih.gov/41780642/) | 2026 | RCT | Ann Oncol | DESTINY-Breast06: trastuzumabe deruxtecana em HR+/HER2-low/ultralow (produto diferente) |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Meta-análise | N Engl J Med | Risco de recorrência em 20 anos após suspender terapia endócrina aos 5 anos em câncer ER+ |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-análise | Lancet | Efeitos de quimioterapia e terapia hormonal na recorrência e sobrevida em 15 anos |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Estudo molecular | Theranostics | Perfil molecular e resposta ao trastuzumabe em tumores ER+/PR+/HER2+ |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Revisão | Nat Rev Clin Oncol | Bloqueio do alvo correto em câncer HER2+ e receptor hormonal positivo |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Diretriz | J Clin Oncol | Atualização da diretriz ASCO sobre terapia sistêmica em câncer de mama HER2+ avançado |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 94 interações. Entre as de gravidade **maior**: deferiprona, samário (153Sm) lexidronam, adalimumabe e baricitinibe. Entre as de gravidade **moderada**: paclitaxel, varfarina, dicumarol, zidovudina, cloranfenicol, alentuzumabe, azatioprina, anakinra, canaquinumabe, roflumilaste, palifermina, cloreto de estrôncio Sr-89 e algumas vacinas (toxoide tetânico, antraz).
- Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há um ensaio Phase 3 randomizado concluído (n=3270) e várias publicações de RCT apoiando o uso de trastuzumabe em câncer de mama HER2-positivo, que inclui o subgrupo PR-positivo. A indicação prevista sobrepõe-se à indicação original; por isso, o uso deve se restringir a tumores com HER2 confirmado.

**Para prosseguir, é necessário:**
- Confirmar o status de HER2 (superexpressão/amplificação) antes de qualquer uso; não há suporte para doença HER2-negativa.
- Obter as advertências e contraindicações da bula na ANVISA (dados ausentes), incluindo monitoramento cardíaco, dado o risco de cardiotoxicidade descrito na literatura.
- Esclarecer a situação regulatória no Brasil: os dados compilados indicam 0 registros, o que deve ser verificado.
- Obter dados detalhados do mecanismo de ação (MOA) na base DrugBank.
- Avaliar o plano de manejo das interações de gravidade maior.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

