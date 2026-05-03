---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Clarithromycin
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

Com base no Evidence Pack fornecido, aqui está o relatório de avaliação de reposicionamento de fármacos:

---

# Clarithromycin: De Antibiótico Macrólido à Gamopatia Monoclonal

## Resumo em Uma Frase

Clarithromycin é um antibiótico macrolídeo de 14 membros, amplamente utilizado no tratamento de infecções bacterianas como pneumonia comunitária, erradicação de *Helicobacter pylori* e profilaxia do complexo *Mycobacterium avium* (MAC).
O modelo TxGNN prevê que pode ser eficaz para **Gamopatia Monoclonal (Monoclonal Gammopathy)**, incluindo mieloma múltiplo, atualmente com **1 ensaio clínico concluído** e **20 publicações** apoiando esta direção — tornando-a a indicação com evidência clínica mais robusta entre as 10 candidatas previstas.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (antibiótico macrólido) |
| Nova Indicação Prevista | Gamopatia Monoclonal (Monoclonal Gammopathy) |
| Pontuação de Previsão TxGNN | 98.81% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado (conforme dados ANVISA disponíveis) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

> **Nota sobre seleção da indicação-alvo:** O TxGNN atribuiu escore mais alto à síndrome de hiperviscosidade policlonal (99.35%), porém esta indicação não possui qualquer evidência clínica (L5 / Hold). A gamopatia monoclonal, com escore de 98.81%, concentra toda a evidência clínica disponível e recebeu classificação L2 com recomendação "Proceed with Guardrails", sendo portanto selecionada como foco deste relatório.

---

## Por que Esta Previsão é Razoável?

Embora os dados de mecanismo de ação não estejam disponíveis neste Evidence Pack, o conhecimento consolidado indica que Clarithromycin inibe a síntese proteica bacteriana ao se ligar à subunidade 50S ribossomal. Além dessa ação antimicrobiana, o fármaco exerce efeitos anti-inflamatórios sistêmicos documentados — inibição de IL-1β e TNF-α e modulação da via NF-κB — que são a base para sua atividade antitumoral.

A razoabilidade clínica reside nos efeitos sobre células plasmáticas neoplásicas. Propõe-se que Clarithromycin amplifique a atividade de agentes imunomoduladores (IMiDs) como lenalidomida e talidomida por meio de: (1) modulação da sinalização de IL-6, citocina central para a sobrevivência de células de mieloma; (2) regulação autofágica nas células neoplásicas; e (3) possível aumento da biodisponibilidade dos IMiDs. O esquema **BiRD** (Biaxin/Clarithromycin + Revlimid/Lenalidomida + Dexametasona) emergiu dessas hipóteses e acumula extensa documentação clínica.

A conexão com gamopatia monoclonal (MGUS) é especialmente relevante: trata-se de um estado pré-maligno com risco de progressão para mieloma múltiplo. Um ensaio fase 2 randomizado concluído (NCT00006219) avaliou diretamente Clarithromycin nessa população de alto risco, consolidando a plausibilidade clínica da previsão do TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00006219](https://clinicaltrials.gov/study/NCT00006219) | Phase 2 | Concluído | N/A | Ensaio randomizado comparando DHEA (dehidroepiandrosterona) versus Clarithromycin em pacientes com MGUS de significado indeterminado ou borderline com alto risco de progressão para mieloma múltiplo; avaliou potencial de quimioprevenção, com Clarithromycin como um dos dois braços ativos |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36394758](https://pubmed.ncbi.nlm.nih.gov/36394758/) | 2022 | Meta-análise/Revisão sistemática | European Review for Medical and Pharmacological Sciences | Comparação sistemática de regimes triplos baseados em pomalidomida + dexametasona (incluindo ClaPd com Clarithromycin) em MM recidivante/refratário; analisa melhor opção terapêutica |
| [34021118](https://pubmed.ncbi.nlm.nih.gov/34021118/) | 2021 | Estudo randomizado (Fase 3) | Blood Cancer Journal | 286 pacientes com MM inelegíveis para transplante; Rd com ou sem Clarithromycin não mostrou diferença significativa em sobrevida livre de progressão (SLP) — sugere que benefício é restrito a subgrupos específicos |
| [30792190](https://pubmed.ncbi.nlm.nih.gov/30792190/) | 2019 | Fase 2 | Blood Advances | 120 pacientes com RRMM com exposição prévia a lenalidomida receberam ClaPd (Clarithromycin + pomalidomida + dexametasona); documentou resposta objetiva e perfil de segurança aceitável |
| [24576165](https://pubmed.ncbi.nlm.nih.gov/24576165/) | 2014 | Fase 2 | Leukemia & Lymphoma | T-BiRD (talidomida + Clarithromycin + lenalidomida + dexametasona) em 26 pacientes com MM recém-diagnosticado; alta taxa de resposta global observada |
| [17989313](https://pubmed.ncbi.nlm.nih.gov/17989313/) | 2008 | Ensaio clínico | Blood | BiRD como terapia de primeira linha em MM sintomático; definiu o esquema e demonstrou altas taxas de resposta completa e global em ciclos de 28 dias |
| [34424561](https://pubmed.ncbi.nlm.nih.gov/34424561/) | 2021 | Fase 2 | American Journal of Hematology | Car-BiRd: indução com carfilzomib + dexametasona seguida de consolidação com lenalidomida + Clarithromycin + dexametasona; avalia se sequenciamento PI→IMiD reduz toxicidade sem comprometer eficácia |
| [24723438](https://pubmed.ncbi.nlm.nih.gov/24723438/) | 2014 | Estudo clínico | American Journal of Hematology | Análise retrospectiva de 24 pacientes com MM em progressão sob Rd; adição de Clarithromycin reverteu resistência em proporção significativa; mediana de terapias prévias: 3 |
| [12685831](https://pubmed.ncbi.nlm.nih.gov/12685831/) | 2002 | Fase 2 | Leukemia & Lymphoma | Estudo fundador de BLT-D (Clarithromycin + talidomida baixa dose + dexametasona) em MM não tratado e tratado previamente e em macroglobulinemia de Waldenström; primeiro a sistematizar atividade antimieloma oral não-mielossupressiva |
| [11778973](https://pubmed.ncbi.nlm.nih.gov/11778973/) | 2001 | Fase 2 | Medical Oncology | 20 pacientes com MM (recidivante, refratário, não tratados) receberam Clarithromycin 500 mg 2x/dia + pamidronato mensal sem citotóxicos/esteroides; avaliou atividade antimieloma como agente único |
| [33138750](https://pubmed.ncbi.nlm.nih.gov/33138750/) | 2021 | Revisão | Current Medicinal Chemistry | Revisão abrangente de reposicionamento de fármacos em doenças hematológicas; descreve vias de sinalização e mecanismos pelos quais Clarithromycin e outros agentes exercem efeitos anticancerígenos em MM |

---

## Informações de Comercialização no Brasil

Nenhum registro ativo foi encontrado para Clarithromycin junto à ANVISA conforme os dados disponíveis neste Evidence Pack (data de corte: 2026-04-25). Este resultado pode representar uma lacuna de dados, uma vez que Clarithromycin é um antibiótico de uso difundido globalmente — recomenda-se verificação direta no portal ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Múltiplos ensaios clínicos Fase 2 documentam o uso de Clarithromycin como adjuvante em mieloma múltiplo e gamopatia monoclonal, e um ensaio Fase 2 específico para MGUS foi concluído. Contudo, o único ensaio Fase 3 disponível (PMID 34021118) não confirmou benefício em SLP na população geral de MM — indicando que o benefício pode ser subgrupo-dependente — o que exige critérios de seleção rigorosos antes de qualquer avanço clínico.

**Para prosseguir, é necessário:**
- Verificar o status atual de registro ANVISA para Clarithromycin no Brasil (possível lacuna de dados)
- Obter dados completos de mecanismo de ação (MOA), advertências e contraindicações da bula
- Mapear perfil de interações medicamentosas, especialmente com IMiDs (lenalidomida, pomalidomida) e inibidores de proteassoma (bortezomibe, carfilzomibe)
- Identificar e definir subpopulações com maior probabilidade de benefício (ex.: MM refratário a lenalidomida, MGUS de alto risco, amiloidose AL)
- Avaliar viabilidade de ensaio clínico local ou acesso via uso compassivo/protocolo de uso expandido no contexto regulatório brasileiro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

