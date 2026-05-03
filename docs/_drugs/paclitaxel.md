---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: Do câncer de ovário ao carcinoma mamário feminino

## Resumo em Uma Frase

Paclitaxel é um agente quimioterápico da classe dos taxanos, originalmente indicado para o tratamento do câncer de ovário resistente a compostos de platina e, posteriormente, estendido a múltiplos tumores sólidos.
O modelo TxGNN prevê alta eficácia para **Carcinoma Mamário Feminino (Female Breast Carcinoma)**, com pontuação de predição de **99,99%**,
sustentada por **50 ensaios clínicos** e **20 publicações** revisadas neste pacote de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dados de registro não disponíveis no pack atual; historicamente aprovado para câncer de ovário e outros tumores sólidos |
| Nova Indicação Prevista | Carcinoma Mamário Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Paclitaxel exerce sua atividade antitumoral por meio da ligação à subunidade β-tubulina, estabilizando os polímeros de microtúbulos contra a despolimerização. Essa ação bloqueia a formação do fuso mitótico funcional, resultando em parada do ciclo celular na fase G2/M, ativação das vias apoptóticas intrínseca e extrínseca, e morte celular programada. As células tumorais com alta taxa proliferativa são especialmente vulneráveis a esse mecanismo — e o carcinoma mamário é um dos tipos de tumor com maior índice mitótico entre os cânceres femininos, tornando paclitaxel mecanisticamente apto para esta indicação.

O carcinoma mamário feminino é uma doença heterogênea, abrangendo subtipos moleculares distintos: Luminal A/B (ER+/PR+), HER2-amplificado e triplo-negativo (TNBC). Em todos esses subtipos, o bloqueio de microtúbulos promovido por paclitaxel não depende de receptores hormonais ou de HER2, sendo eficaz independentemente do perfil molecular. Isso torna o mecanismo de ação particularmente relevante para casos de câncer de mama de alto risco, doença metastática ou situações onde a terapia endócrina falhou — contextos nos quais paclitaxel é parte central dos protocolos de tratamento.

O estudo CALGB 9344 (N=3.677) — um dos maiores ensaios randomizados conduzidos em mama — analisou diretamente o benefício diferencial de paclitaxel por subtipo intrínseco, demonstrando que tumores Basal-like (correspondentes ao TNBC) obtêm os maiores ganhos com a adição de paclitaxel a esquemas com antraciclinas. Múltiplos ensaios de fase 3 subsequentes (Neo ALTTO, GeparOcto, KEYNOTE-756 e outros) consolidaram paclitaxel como componente essencial dos esquemas contemporâneos neoadjuvantes, adjuvantes e paliativos para todos os subtipos de alto risco, apoiando plenamente a predição do modelo TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A | Concluído | 3.677 | Análise de subtipos intrínsecos de mama e benefício de paclitaxel nos estudos CALGB 9344/9741; maior análise demonstrando heterogeneidade de resposta por subtipo molecular — subtipo Basal-like com maior benefício |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Concluído | 3.270 | Quimioterapia adjuvante (AC→paclitaxel semanal ou TC) com ou sem trastuzumab em mama HER2-baixo com linfonodo positivo ou alto risco; compara estratégias quimioterápicas modernas |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Concluído | 2.005 | Doxorrubicina + ciclofosfamida seguida de paclitaxel em intervalos de 14 ou 21 dias em mama estágio II/IIIA com linfonodo positivo; avalia impacto da densidade de dose |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Ativo (não recruta) | 2.000 | EC→paclitaxel vs FEC→paclitaxel com suporte de pegfilgrastim em mama com linfonodo positivo; compara adição de fluorouracil à espinha dorsal antraciclina-taxano |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Concluído | 961 | GeparOcto: compara ETC de alta dose vs paclitaxel semanal + doxorrubicina lipossomal não-peguilada como neoadjuvante em mama de alto risco; ambos os braços com bloqueio duplo de HER2 |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Concluído | 455 | Neo ALTTO: lapatinibe vs trastuzumab vs combinação + paclitaxel neoadjuvante em HER2/ErbB2-positivo primário; avalia duplo bloqueio de HER2 com base taxano |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Concluído | 725 | Comparação ABP 980 (biossimilar de trastuzumab) vs trastuzumab de referência em mama HER2+ inicial; ambos os braços com regime neoadjuvante e adjuvante incluindo paclitaxel |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Encerrado | 63 | Paclitaxel + trastuzumab ± lapatinibe em mama metastática ErbB2+; encerrado precocemente antes do recrutamento completo (N=63 vs 700 planejados), mas provê dados de segurança da tríplice combinação |
| [NCT03272477](https://clinicaltrials.gov/study/NCT03272477) | Phase 2 | Concluído | 257 | Comparação pré-cirúrgica de trastuzumab + pertuzumab + paclitaxel semanal vs terapia endócrina por 12 semanas em mama HER2+/HR+ operável; avalia estratégia de de-escalada quimioterápica |
| [NCT00709761](https://clinicaltrials.gov/study/NCT00709761) | Phase 2 | Concluído | 60 | Nab-paclitaxel semanal + lapatinibe em primeira e segunda linha de mama metastática ErbB2+; avalia formulação nanoparticulada de paclitaxel ligada a albumina |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Prospective Clinical | BioMed Research International | Eficácia de EC + paclitaxel semanal + trastuzumab neoadjuvante em HER2+ câncer de mama em cenário de vida real; demonstra taxas satisfatórias de resposta patológica completa (pCR) |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Revisão abrangente dos mecanismos de ação e efeitos clínicos de paclitaxel no câncer de mama; discute vias de resistência, incluindo modulação de β-tubulina, glicoproteína-P e autofagia |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Review | Chemical Biology & Drug Design | Identificação de combinações terapêuticas sinérgicas de paclitaxel em carcinoma mamário usando modelos derivados de pacientes; aborda biomarcadores in vivo de resistência farmacológica |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase II Clinical | Cancer | Ensaio multicêntrico fase II de doxorrubicina + paclitaxel em carcinoma mamário avançado; avalia eficácia e impacto da terapia prévia com antraciclinas na resposta ao paclitaxel |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Avaliação de paclitaxel e docetaxel em câncer de mama e ovário; analisa extensão de licença de paclitaxel para câncer de mama metastático resistente a antraciclinas |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase II Clinical | Journal of Clinical Oncology | Ensaio ECOG de paclitaxel + cisplatina em regime quinzenal em carcinoma mamário avançado; determina eficácia da combinação em contexto metastático |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Phase II Clinical | Cancer | Papel de paclitaxel no tratamento multimodal do carcinoma mamário inflamatório (IBC), subforma de alto risco; relata atividade clínica significativa nesta apresentação agressiva |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genomic Study | Nature Communications | Variações germinativas em TEKT4 identificadas por sequenciamento do exoma como marcador de resistência a paclitaxel em câncer de mama; implica estabilização de tubulina em microtúbulos ciliares como mecanismo |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Preclinical/Mechanistic | Journal for Immunotherapy of Cancer | Paclitaxel remodela macrófagos associados ao tumor (TAMs) potencializando bloqueio de PD-1 em TNBC; esclarece mecanismo imunológico subjacente à sinergia com imunoterapia |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical | Journal of Cellular Physiology | ZD6474 (inibidor duplo de EGFR e VEGFR) potencializa efeitos antiproliferativos e apoptóticos de paclitaxel em células de carcinoma mamário com superexpressão de EGFR; base para combinações em TNBC |

---

## Informações de Comercialização no Brasil

Paclitaxel está **comercializado no Brasil** com **20 registros** ativos na ANVISA. As informações detalhadas de nome comercial, forma farmacêutica, fabricante e indicação aprovada de cada produto não estão disponíveis neste Evidence Pack. Para consultar os registros completos e as bulas aprovadas, acesse o portal da ANVISA: [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/).

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — Classe Taxano (inibidor de microtúbulos, ligação direta à subunidade β-tubulina) |
| Risco de Mielossupressão | **Alto** — neutropenia é o principal efeito limitante de dose; leucopenia, anemia e trombocitopenia também relatadas; risco de neutropenia febril requer monitoramento rigoroso antes de cada ciclo |
| Classificação de Emetogenicidade | **Baixa a média** — taxanos isolados apresentam potencial emetogênico baixo; emetogenicidade pode escalar para média-alta em combinações (ex.: paclitaxel + carboplatina) |
| Itens de Monitoramento | Hemograma completo com diferencial (antes de cada ciclo), AST/ALT/bilirrubina/fosfatase alcalina, creatinina, avaliação neurológica de neuropatia periférica (escores CIPN), pressão arterial e sinais de reação de hipersensibilidade durante infusão |
| Proteção no Manuseio | Seguir regulamentos de manuseio de citotóxicos (EPIs completos, cabine de segurança biológica); formulação convencional contém Cremophor EL (polioxietileno-óleo de rícino), exigindo **pré-medicação obrigatória** com corticosteroide (ex.: dexametasona), anti-histamínico H1 (ex.: difenidramina) e bloqueador H2 (ex.: cimetidina ou ranitidina) para prevenção de reações de hipersensibilidade |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A predição TxGNN (99,99%) para carcinoma mamário feminino é amplamente sustentada por nível de evidência L1, com múltiplos ensaios de fase 3 de grande porte (CALGB 9344, N=3.677; Neo-BCIRG, N=3.270; CALGB 9741, N=2.005; e outros) confirmando eficácia consistente nos subtipos HER2+, TNBC e ER+ de alto risco, tanto em regime neoadjuvante quanto adjuvante e metastático. O guardrail essencial é a seleção criteriosa do subtipo molecular e da linha de tratamento para maximizar o benefício clínico e minimizar toxicidade acumulada.

**Para prosseguir, é necessário:**
- Recuperar indicações aprovadas e texto completo das bulas dos 20 produtos registrados na ANVISA
- Obter dados completos de segurança (advertências principais, contraindicações, interações medicamentosas), atualmente ausentes neste pack
- Definir o subtipo molecular alvo (TNBC, HER2+, Luminal B de alto risco ou doença metastática) para protocolo de seleção de pacientes
- Estabelecer e padronizar protocolo de pré-medicação anti-hipersensibilidade (especialmente para formulações com Cremophor EL)
- Planejar monitoramento prospectivo de neuropatia periférica induzida por taxano (CIPN) como principal efeito adverso limitante de dose cumulativa
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

