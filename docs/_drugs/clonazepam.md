---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 3
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using `txgnn-pipeline` para produção do relatório de reposicionamento (BrTxGNN — Brasil).

---

# Clonazepam: Da Epilepsia à Síndrome das Pernas Inquietas

## Resumo em Uma Frase

Clonazepam é um benzodiazepínico anticonvulsivante utilizado no tratamento de epilepsia, transtornos de pânico e outras condições neuropsiquiátricas.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome das Pernas Inquietas (Restless Legs Syndrome)**,
com **0 ensaios clínicos registrados** e **20 publicações** apoiando esta direção, incluindo uma revisão Cochrane e o guia clínico AASM 2025.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia e transtornos convulsivos |
| Nova Indicação Prevista | Síndrome das Pernas Inquietas (Restless Legs Syndrome) |
| Pontuação de Previsão TxGNN | 99,65% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Clonazepam é um modulador alostérico positivo dos receptores GABA-A. Ao se ligar às subunidades α do receptor, potencializa o influxo de Cl⁻ mediado por GABA, amplificando a inibição sináptica em todo o sistema nervoso central. Este mecanismo suprime diretamente a hiperexcitabilidade dos circuitos motores espinais e subcorticais, reduzindo a frequência dos Movimentos Periódicos dos Membros (PLM) e o número de despertares noturnos associados — ambos marcadores centrais da Síndrome das Pernas Inquietas.

A SPI é uma doença sensoriomotora caracterizada por desconforto irresistível nos membros inferiores em repouso, com piora noturna e alívio pelo movimento, frequentemente acompanhada de PLMS (movimentos periódicos dos membros durante o sono). Sua fisiopatologia central envolve disfunção dopaminérgica (vias D2/D3) e déficit de ferro cerebral. A ação GABAérgica do clonazepam complementa indiretamente o sistema dopaminérgico, tornando-o uma opção de tratamento adjuvante que atua em via paralela — e não antagônica — à farmacologia dopaminérgica de primeira linha.

O guia clínico da AASM (2025) reconhece formalmente o clonazepam como tratamento de segunda linha para SPI, com evidências documentadas desde 1984, quando um ensaio cruzado randomizado duplo-cego demonstrou melhora significativa da qualidade do sono e da disestesia nos membros. Uma pesquisa com 16.694 pacientes em tratamento para SPI revelou que aproximadamente 25% utilizam benzodiazepínicos — isoladamente ou em combinação — consolidando a relevância clínica real desta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos registrados no ClinicalTrials.gov para a combinação Clonazepam + Síndrome das Pernas Inquietas.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Revisão Sistemática (Cochrane) | Cochrane Database Syst Rev | Única revisão sistemática de benzodiazepínicos para SPI; clonazepam é o mais utilizado, com documentação histórica de benefício no sono; evidência ainda insuficiente para recomendação formal por ausência de RCTs modernos |
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Guia Clínico (AASM) | J Clin Sleep Med | Diretriz de prática clínica da AASM para tratamento de SPI e PLMD em adultos e pacientes pediátricos; inclui recomendações sobre benzodiazepínicos |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Ensaio Clínico Prospectivo Randomizado | J Mid-Life Health | Comparação direta de clonazepam vs. nortriptilina em mulheres acima de 40 anos com SPI; avalia taxa, frequência e gravidade dos sintomas |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | Ensaio Cruzado Randomizado Duplo-Cego | Acta Neurol Scand | 6 pacientes com SPI; clonazepam mostrou eficácia significativa vs. placebo na melhora subjetiva do sono e da disestesia; considerado seguro e eficaz |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Estudo Controlado por Placebo | Eur Neuropsychopharmacol | Estudo em laboratório do sono: 1 mg de clonazepam melhora variáveis objetivas e subjetivas do sono em pacientes com SPI/PLMD |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Revisão Sistemática / Meta-análise | J Clin Sleep Med | Responsividade farmacológica dos PLM na SPI; analisa sistematicamente quais classes de fármacos são eficazes na supressão dos PLM |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Revisão Narrativa | Tremor Other Hyperkinetic Mov | Panorama histórico do papel dos benzodiazepínicos na SPI; identifica 17 artigos sobre clonazepam em SPI/PLMS; ~25% dos pacientes em tratamento para SPI utilizam benzodiazepínicos |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Revisão Baseada em Evidências (MDS) | Movement Disorders | Força-tarefa da Movement Disorder Society: revisão abrangente das modalidades de tratamento para SPI com classificação formal de eficácia por fármaco |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Consenso de Especialistas | Arq Neuropsiquiatr | Grupo Brasileiro de Estudo da SPI (GBE-SPI): consenso sobre diagnóstico e manejo da SPI no contexto brasileiro; agentes dopaminérgicos como primeira linha, com referência a benzodiazepínicos |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Revisão | Neurotherapeutics | Evolução do tratamento da SPI; diversas classes de medicamentos com eficácia demonstrada, incluindo benzodiazepínicos como opção estabelecida |

---

## Informações de Comercialização no Brasil

O clonazepam possui **20 registros ativos** no Brasil e está amplamente comercializado. Os dados individuais de cada registro (nome comercial, forma farmacêutica e texto da indicação aprovada) não foram recuperados nesta consulta.

> ℹ️ Para detalhes dos registros individuais, consulte o portal da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há sólida base literária para o uso do clonazepam em SPI, incluindo revisão Cochrane, diretriz oficial da AASM 2025 e ensaios controlados com placebo. O fármaco é reconhecido formalmente como segunda linha para SPI, porém com restrições relevantes de dependência, tolerância e sedação diurna que exigem monitoramento ativo.

**Para prosseguir, é necessário:**
- Recuperar os dados completos dos 20 registros ANVISA (nome comercial, forma farmacêutica, indicação aprovada por produto)
- Obter e analisar a bula vigente para advertências, contraindicações e interações medicamentosas
- Confirmar disponibilidade de formulações orais em dosagens adequadas para uso crônico em SPI (tipicamente 0,5–2 mg/noite)
- Avaliar perfil de risco em populações especiais — idosos (risco aumentado de quedas e comprometimento cognitivo), gestantes e pacientes com apneia obstrutiva do sono
- Estabelecer protocolo de monitoramento para dependência física e tolerância farmacodinâmica em uso prolongado
---

