---
layout: default
title: Docetaxel
parent: Apenas Predição do Modelo (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Docetaxel: nova indicação prevista, Carcinoma de mama feminino (Female Breast Carcinoma) (nível de evidência L5). Indicação original: Câncer de pulmão de células não pequenas, câncer de pulmão…"
monitor_inn: "Docetaxel"
predicted_indications: ["Ewing sarcoma", "primary pulmonary lymphoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "pulmonary blastoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Docetaxel
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

# Docetaxel: Do câncer de pulmão, próstata, mama, estômago e cabeça e pescoço ao carcinoma de mama feminino

## Resumo em Uma Frase

Docetaxel é um taxano (agente quimioterápico) originalmente usado no tratamento de câncer de pulmão de células não pequenas, próstata, cabeça e pescoço, estômago e mama.
O modelo TxGNN prevê que pode ser eficaz para **carcinoma de mama feminino (Female Breast Carcinoma)**, com **44 ensaios clínicos** e **20 publicações** nos dados compilados para este relatório.
Atenção: o câncer de mama já consta entre as indicações originais do fármaco, de modo que esta previsão é, na prática, uma confirmação de uso existente, e não um reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de pulmão de células não pequenas, câncer de pulmão, câncer de próstata, câncer de cabeça e pescoço, câncer gástrico, carcinoma de mama (conforme o grafo de conhecimento do TxGNN; não há texto de indicação aprovada na ANVISA) |
| Nova Indicação Prevista | Carcinoma de mama feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L1 (vários Phase 3 concluídos nos dados compilados; ver observação abaixo) |
| Situação no Mercado Brasileiro | Não comercializado (nenhum registro localizado nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

**Observação sobre o nível de evidência:** a classificação automática dos dados atribuiu L2. Porém, os dados contêm ao menos dois Phase 3 concluídos com docetaxel no braço de tratamento em câncer de mama (por exemplo, NCT00003519, NCT00021255, NCT00003782, NCT00333775, NCT00887536, NCT00431080, NCT00002707), o que atende, em tese, ao critério L1. Mantém-se aqui L1 como leitura conservadora dos ensaios listados, ficando a confirmação da classificação final a cargo da equipe.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas e a literatura retornada, docetaxel é um taxano que estabiliza os microtúbulos, bloqueando a divisão celular na fase M do ciclo celular e levando à morte de células tumorais em proliferação rápida.

A previsão é coerente porque o carcinoma de mama já está entre as indicações originais do fármaco. A literatura recuperada descreve docetaxel como agente de atividade substancial em câncer de mama avançado, usado isoladamente ou em associação com antraciclinas, ciclofosfamida, capecitabina, gencitabina e terapias anti-HER2.

Em resumo, o modelo está reconhecendo uma indicação já estabelecida. Isso reforça a confiabilidade da previsão, mas ela não representa uma nova oportunidade de reposicionamento.

## Evidências de Ensaios Clínicos

Foram listados os ensaios mais relevantes (máximo de 10), priorizando os de fase mais avançada e com docetaxel como componente central.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Concluído | 3222 | Adjuvante em câncer de mama HER2-positivo: AC seguido de docetaxel, com ou sem trastuzumabe, versus docetaxel + carboplatina + trastuzumabe |
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | Concluído | 5351 | Adjuvante com linfonodos positivos: comparação de AC-T, AT e ATC |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Concluído | 2778 | Adjuvante: doxorrubicina/docetaxel versus doxorrubicina/ciclofosfamida |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Concluído | 2411 | Pré-operatório: AC com ou sem docetaxel antes ou depois da cirurgia |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Phase 3 | Concluído | 1613 | Docetaxel + ciclofosfamida (TC) com bevacizumabe versus TC isolado e versus TAC em HER2-negativo |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Concluído | 736 | Bevacizumabe + docetaxel versus docetaxel + placebo em primeira linha, HER2-negativo metastático |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Concluído | 652 | Quimioterapia com taxano + lapatinibe versus + trastuzumabe, HER2-positivo metastático |
| [NCT03588091](https://clinicaltrials.gov/study/NCT03588091) | Phase 3 | Concluído | 355 | Neoadjuvante: piротinibe + trastuzumabe + docetaxel versus placebo + trastuzumabe + docetaxel |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Concluído | 148 | Carboplatina versus docetaxel em câncer de mama metastático com perfil genético (BRCA) |
| [NCT00003352](https://clinicaltrials.gov/study/NCT00003352) | Phase 2 | Concluído | 89 | Combinação doxorrubicina, docetaxel e ciclofosfamida em câncer de mama metastático ou localmente avançado |

Os dados compilados incluem outros ensaios adicionais (por exemplo, o estudo de dosagem guiada por farmacocinética em idosas, NCT02502864, Phase 4, n=9).

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | Estudos ABC: docetaxel + ciclofosfamida (TC) comparado a regimes com taxano e antraciclina no câncer de mama inicial |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revisão | Lancet | Taxanos: docetaxel e paclitaxel como componentes baseados em evidências no câncer de mama, pulmão e ovário |
| [9775340](https://pubmed.ncbi.nlm.nih.gov/9775340/) | 1998 | Revisão | Am J Health Syst Pharm | Farmacologia, farmacocinética, ensaios e efeitos adversos do docetaxel no câncer de mama metastático |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Revisão | Breast Cancer Res Treat | Combinações de docetaxel com antraciclinas no câncer de mama metastático |
| [12868802](https://pubmed.ncbi.nlm.nih.gov/12868802/) | 2003 | Revisão | Breast Cancer Res Treat | Docetaxel neoadjuvante no câncer de mama localmente avançado |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Revisão | Expert Opin Drug Metab Toxicol | Lições do desenvolvimento do docetaxel (farmacologia e farmacocinética) |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Docetaxel semanal + gencitabina em primeira linha no câncer de mama metastático |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabina + docetaxel + epirrubicina em câncer de mama avançado não tratado |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospectivo | Anti-Cancer Drugs | Associação entre quimioterapia adjuvante com docetaxel e linfedema relacionado ao câncer de mama |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Revisão | Oncology (Williston Park) | Docetaxel/vinorelbina no câncer de mama metastático e no câncer de pulmão de células não pequenas |

## Informações de Comercialização no Brasil

Nos dados compilados para este relatório, não há registros de docetaxel na ANVISA (0 registros; situação: não comercializado). Recomenda-se verificar diretamente o banco de registros da ANVISA, pois a ausência pode refletir lacuna na coleta e não necessariamente a inexistência de produtos.

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (classe dos taxanos; estabilizador de microtúbulos) |
| Risco de Mielossupressão | Alto (o grafo de conhecimento associa o fármaco a neutropenia, trombocitopenia, agranulocitose e anemia como condições de cautela) |
| Classificação de Emetogenicidade | Baixa a média (classificação geral da classe; não há dado específico nos dados compilados) |
| Itens de Monitoramento | Hemograma completo com diferencial, função hepática (incluindo bilirrubina), função renal, sinais de neuropatia periférica, retenção de líquidos e função pulmonar |
| Proteção no Manuseio | Necessário seguir os regulamentos de manuseio de citotóxicos |

## Considerações de Segurança

- **Condições associadas a contraindicação ou cautela (grafo de conhecimento, não texto de bula)**: doença hepática, doença da vesícula biliar, trombocitopenia, neutropenia, agranulocitose, anemia, hiperbilirrubinemia (incluindo síndrome de Gilbert), neuropatia periférica e neurite, doença diarreica, edema pulmonar, estomatite e tamponamento cardíaco.
- **Interações Medicamentosas** (100 interações identificadas; principais listadas):
  - **Maior gravidade**: claritromicina.
  - **Moderada**: aprepitanto, metronidazol, cimetidina, eliglustate, miconazol, rolapitanto, rosuvastatina, sinvastatina, tinidazol, troglitazona.
  - **Menor**: dexametasona, levofloxacino, prednisolona, prednisona.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- O carcinoma de mama já é indicação original do docetaxel, com extensa base de ensaios de Phase 2 e Phase 3 e literatura consistente; a previsão é plausível, mas não constitui reposicionamento novo.
- A segurança exige cautela: há risco hematológico relevante, interação de gravidade maior (claritromicina) e lacunas de dados de bula e de mecanismo de ação.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada na ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança.
- Confirmar a situação de registro no Brasil, já que os dados compilados não mostram nenhum.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Definir plano de monitoramento hematológico, hepático e neurológico, além de revisão de interações medicamentosas.
- Se houver interesse em reposicionamento genuíno, priorizar outras previsões: sarcoma de Ewing e rabdomiossarcoma têm dados de Phase 2 (principalmente em combinação com gencitabina), mas com respostas modestas. As demais previsões (por exemplo, câncer de pulmão de pequenas células, linfoma pulmonar primário e blastoma pulmonar) têm evidência fraca ou inespecífica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

