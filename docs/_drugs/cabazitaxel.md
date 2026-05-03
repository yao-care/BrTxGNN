---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: Do câncer de próstata resistente à castração ao carcinoma de mama feminino

## Resumo em Uma Frase

Cabazitaxel é um agente quimioterápico da classe dos taxanos, originalmente aprovado pelo FDA para o tratamento do **câncer de próstata metastático resistente à castração (mCRPC)** em pacientes previamente tratados com docetaxel.
O modelo TxGNN prevê que pode ser eficaz para **Carcinoma de Mama Feminino (Female Breast Carcinoma)**,
atualmente com **0 ensaios clínicos registrados** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata metastático resistente à castração (mCRPC) |
| Nova Indicação Prevista | Carcinoma de Mama Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99.92% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Cabazitaxel é um taxano de segunda geração desenvolvido para superar a resistência a taxanos convencionais. Como estabilizador de microtúbulos, bloqueia a divisão celular ao impedir a desmontagem dos microtúbulos durante a mitose — o mesmo mecanismo que fundamenta o uso de paclitaxel e docetaxel como pilares do tratamento padrão do câncer de mama. A diferença estratégica é que Cabazitaxel possui baixa afinidade pela P-glicoproteína (P-gp), a proteína que bombeia fármacos para fora das células tumorais e é responsável por boa parte da resistência adquirida a taxanos. Isso significa que Cabazitaxel mantém atividade antitumoral em cenários onde paclitaxel e docetaxel já falharam.

Estudos in vitro demonstraram que a expressão elevada de βIII-tubulina — um marcador de agressividade tumoral e de resistência a taxanos — se correlaciona com maior eficácia de Cabazitaxel em comparação ao docetaxel, sugerindo uma janela terapêutica específica para tumores com esse perfil. Em câncer de mama, especialmente nos subtipos triplo-negativo (TNBC) e Luminal B/HER2-negativo, a resistência adquirida a taxanos convencionais representa um desafio clínico concreto para o qual Cabazitaxel oferece uma solução mecanisticamente embasada.

Além disso, Cabazitaxel apresenta maior penetração na barreira hematoencefálica em comparação a outros taxanos, o que abre potencial adicional para o tratamento de metástases cerebrais — complicação relevante no câncer de mama HER2+. Dados clínicos de Phase 1/II e Phase 2 já investigaram diretamente Cabazitaxel em câncer de mama metastático, confirmando que a predição do modelo TxGNN tem respaldo em investigação clínica real.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados nas bases ClinicalTrials.gov e ICTRP para a combinação Cabazitaxel + carcinoma de mama feminino.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase 2 RCT | European Journal of Cancer | Estudo GENEVIEVE: comparou Cabazitaxel vs. paclitaxel semanal como neoadjuvância em câncer de mama HER2-negativo (TNBC e Luminal B); avaliou taxa de resposta patológica completa (pCR) |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/II | European Journal of Cancer | Escalonamento de dose de Cabazitaxel + capecitabina em câncer de mama metastático pré-tratado com taxanos e antraciclinas; avaliou DLT, segurança, farmacocinética e atividade clínica |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase 2 | Clinical Breast Cancer | Cabazitaxel + lapatinib em câncer de mama HER2+ metastático com metástases intracranianas (NCT01934894); explorou a capacidade de Cabazitaxel de atravessar a barreira hematoencefálica |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | Mecanismos de resistência a Cabazitaxel usando células MCF-7 de câncer de mama; demonstrou 15 vezes menor resistência cruzada de Cabazitaxel vs. paclitaxel/docetaxel em variantes MDR |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | Revisão sobre ajuste de dose guiado por monitorização terapêutica (TDM) para taxanos incluindo Cabazitaxel; aborda relações PK-PD e personalização posológica clínica |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | In vitro | Cancer Chemotherapy and Pharmacology | Alta expressão de βIII-tubulina potencializa eficácia de Cabazitaxel vs. docetaxel; esclarece vantagem mecanística em tumores com marcador de resistência a taxanos |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | Journal for Immunotherapy of Cancer | Cabazitaxel melhora imunoterapia anti-CD47 em TNBC ao reprogramar macrófagos associados ao tumor (TAMs), estimulando a remoção programada de células cancerígenas (PrCR) |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | Nanopartículas PACA carregadas com Cabazitaxel em modelo PDX de TNBC; mostraram resultados promissores incluindo modulação de macrófagos M2 no microambiente tumoral |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | Nanopartículas PEBCA contendo Cabazitaxel obtiveram remissão completa em 6/8 tumores em modelo PDX de câncer de mama basal-like; eficácia superior ao fármaco livre |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chemistry and Physics of Lipids | Lipoesferas co-carregadas com Cabazitaxel + timoquinona mostraram atividade sinérgica contra tumores de mama, modulando p53, STAT3, Bax, BCL-2 e NF-κB |

---

## Informações de Comercialização no Brasil

Cabazitaxel possui **8 registros** ativos no Brasil. Os detalhes individuais dos registros (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis na base de dados consultada nesta versão do Evidence Pack. O fármaco é comercializado mundialmente sob o nome de marca **Jevtana®** (Sanofi), na forma de concentrado para solução injetável (60 mg/1,5 mL), com indicação aprovada internacionalmente para câncer de próstata metastático resistente à castração.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — classe Taxano (estabilizador de microtúbulos) |
| Risco de Mielossupressão | **Alto** — neutropenia febril é o efeito adverso mais frequente e limitante de dose; risco significativo de neutropenia grau 3/4 |
| Classificação de Emetogenicidade | Baixa a moderada |
| Itens de Monitoramento | Hemograma completo com diferencial (antes de cada ciclo), função hepática (AST, ALT, bilirrubina total), função renal (creatinina), monitoramento de neuropatia periférica e diarreia |
| Proteção no Manuseio | Obrigatório seguir normas de manuseio de citotóxicos: EPI completo, preparo em câmara de fluxo laminar, descarte em contentor específico para resíduos quimioterápicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um Phase 2 RCT randomizado e aberto (Estudo GENEVIEVE) e um estudo Phase 1/II investigando Cabazitaxel diretamente em câncer de mama, além de um Phase 2 em HER2+ com metástases cerebrais. A base biológica é robusta — mesmo mecanismo de ação dos taxanos padrão, com vantagem demonstrada sobre MDR mediada por P-gp. O conjunto de 20 publicações, incluindo estudos pré-clínicos em TNBC e pesquisas de entrega nanomédica de última geração, sustenta interesse científico crescente e aplicabilidade em subpopulações específicas.

**Para prosseguir, é necessário:**
- Obter dados completos de segurança (advertências, contraindicações, interações medicamentosas) via download e análise da bula registrada na ANVISA
- Confirmar mecanismo de ação detalhado via consulta à API do DrugBank (DG002)
- Identificar e delimitar as subpopulações-alvo com maior probabilidade de resposta: TNBC, Luminal B/HER2-negativo com resistência prévia a taxanos, tumores com expressão elevada de βIII-tubulina
- Realizar busca ampliada no ClinicalTrials.gov com termos alternativos ("breast neoplasm", "breast tumor", "mammary carcinoma") para mapear eventuais ensaios não capturados
- Comparar perfil de toxicidade de Cabazitaxel com taxanos já aprovados para mama (paclitaxel, docetaxel, nab-paclitaxel) para definir a relação risco-benefício no contexto clínico e regulatório brasileiro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

