---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: Do câncer HER2-positivo ao câncer de mama com receptor de progesterona positivo

## Resumo em Uma Frase

Trastuzumab (Herceptin®) é um anticorpo monoclonal humanizado anti-HER2, amplamente utilizado no tratamento do câncer de mama e gástrico HER2-positivo em estágio inicial e metastático.
O modelo TxGNN prevê que pode ser eficaz para o **Câncer de Mama com Receptor de Progesterona Positivo (progesterone-receptor positive breast cancer)**,
atualmente com **36 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de mama HER2-positivo (precoce e metastático); câncer gástrico HER2-positivo |
| Nova Indicação Prevista | Câncer de Mama com Receptor de Progesterona Positivo (PR+) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 14 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base no conhecimento clínico e científico estabelecido, trastuzumab é um anticorpo monoclonal IgG1 humanizado que se liga ao domínio extracelular IV do receptor HER2/ErbB2. Essa ligação bloqueia a dimerização mediada por HER2, suprime a via de sinalização PI3K/AKT→mTOR e ativa a citotoxicidade celular dependente de anticorpo (ADCC), resultando em inibição do crescimento e indução de apoptose nas células que superexpressam HER2.

A conexão com o câncer de mama PR+ baseia-se no fenômeno de co-expressão HER2/HR: aproximadamente 15–20% dos tumores de mama PR+ também apresentam superexpressão de HER2, formando o subgrupo HR+/HER2+ (também denominado "triplo-positivo"). Nesse contexto, a via HER2→PI3K/AKT→mTOR estabelece um *crosstalk* com o receptor de progesterona (PR): a sinalização HER2 fosforila e ativa o PR de forma independente do ligante hormonal, gerando resistência à terapia endócrina. Trastuzumab, ao bloquear HER2, interrompe esse mecanismo de escape e restaura a sensibilidade ao tratamento hormonal.

Essa plausibilidade mecanística é diretamente corroborada por ensaios clínicos voltados ao subtipo HR+/HER2+: o estudo MonarcHER (Phase 2 RCT) demonstrou que abemaciclibe + trastuzumab supera quimioterapia + trastuzumab em sobrevida livre de progressão; o WSG-ADAPT HER2+/HR+ testou a de-escalada de quimioterapia neste subtipo; e o WSG-TP-II (*JAMA Oncology*, 2023) realizou a primeira comparação prospectiva entre ET + duplo bloqueio HER2 *versus* quimioterapia. A **guardrail** essencial: trastuzumab somente é eficaz nesta indicação quando há **superexpressão confirmada de HER2 (IHC 3+ ou FISH amplificado)** — PR+ isolado sem HER2+ não constitui indicação.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Concluído | 3.270 | Quimioterapia adjuvante com ou sem trastuzumab em câncer de mama HER2+ com linfonodos positivos ou alto risco; maior ensaio adjuvante HER2+ com análise de subgrupo HR+ cobrindo diretamente a população PR+/HER2+ |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Concluído | 652 | Taxane + lapatinibe *vs.* trastuzumab em primeira linha para câncer de mama metastático HER2+; comparação direta de estratégias anti-HER2, com PR+ como subgrupo primário de análise |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Concluído | 454 | IMpassion050: atezolizumabe *vs.* placebo combinado a ddAC→paclitaxel+trastuzumab+pertuzumabe neoadjuvante em HER2+ precoce (T2-4, N1-3); inclui análise de subgrupo PR+ |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Concluído | 517 | QL1209 (biossimilar pertuzumabe) + trastuzumab + docetaxel em HER2+/ER-PR−; ensaio randomizado multicêntrico duplo-cego que estabelece o padrão de eficácia do trastuzumab na neoadjuvância |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Concluído | 417 | NeoSphere: 4 braços neoadjuvantes com trastuzumab ± pertuzumabe ± docetaxel em HER2+ localmente avançado/inflamatório/precoce; avalia taxas de resposta patológica completa em subgrupos incluindo HR+ |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Ativo (não recrutando) | 128 | TBCRC 023: lapatinibe + trastuzumab com ou sem terapia endócrina neoadjuvante por 12 *vs.* 24 semanas em HER2+; análise específica de subgrupo HR+ com duplo bloqueio HER2 sem quimioterapia |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Concluído | 37 | Everolimo + letrozol + trastuzumab em HR+/HER2+ avançado; exploração da terapia tripla mTOR inibidor + inibidor de aromatase + anti-HER2, com suporte indireto para a indicação PR+/HER2+ |
| [NCT02654119](https://clinicaltrials.gov/study/NCT02654119) | Phase 2 | Concluído | 20 | Ciclofosfamida + paclitaxel + trastuzumab adjuvante em câncer de mama HER2+ Estágio I-II; avalia regime de menor toxicidade combinado com trastuzumab no contexto pós-operatório |
| [NCT04152057](https://clinicaltrials.gov/study/NCT04152057) | Phase 1/2 | Desconhecido | 20 | Pyrotinibe + nab-paclitaxel + trastuzumab neoadjuvante em HER2+ precoce/localmente avançado; explora eficácia e marcadores moleculares (RCB, TILs) preditivos de resposta |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Concluído | 33 | Letrozol 2,5 mg/dia + trastuzumab semanal em câncer de mama metastático ErbB2+/ER+ ou PR+; avalia diretamente a combinação anti-HER2 + inibidor de aromatase no subtipo PR+/HER2+ |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncology | MonarcHER: abemaciclibe + trastuzumab ± fulvestranto *vs.* quimioterapia + trastuzumab em HR+/HER2+ avançado; melhora significativa de PFS com regime livre de quimioterapia no subgrupo PR+/HER2+ |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: primeira comparação prospectiva de terapia endócrina + trastuzumab + pertuzumabe *vs.* quimioterapia de-escalada em HR+/HER2+ precoce; demonstra viabilidade da estratégia sem quimioterapia |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5 anos) | Lancet Oncology | NeoSphere 5 anos: seguimento de longo prazo da resposta neoadjuvante a pertuzumabe + trastuzumab ± docetaxel; análise de sobrevida livre de progressão e doença em subgrupos incluindo HR+ |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT Phase 3 | Lancet Oncology | ExteNET: neratinibe após adjuvância baseada em trastuzumab em HER2+ precoce; benefício ampliado no subgrupo HR+, evidenciando importância do bloqueio HER2 prolongado em PR+/HER2+ |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Annals of Oncology | WSG-ADAPT HER2+/HR+: bloqueio dual trastuzumab + pertuzumabe ± paclitaxel semanal neoadjuvante no subtipo HR+/HER2+; avalia pCR como substituto de eficácia na estratégia de de-escalada |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Translacional | Theranostics | Perfis moleculares e responsividade ao trastuzumab no câncer de mama ER+/PR+/HER2+ (triplo-positivo); análise multiômica de 32.056 casos no SEER confirma a sensibilidade ao trastuzumab especificamente no subgrupo PR+/HER2+ |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Observacional | BMC Cancer | Trastuzumab + fulvestranto em câncer de mama HR+/HER2+ avançado metastático; dados retrospectivos de centro único com resposta objetiva documentada no subgrupo PR+/HER2+ |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncology | ASCO 2022: atualização das recomendações de terapia sistêmica para HER2+ avançado; inclui estratégias específicas para o subtipo HR+/HER2+, evidenciando o papel central do trastuzumab combinado com endocrinoterapia |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-análise | Lancet | EBCTCG: quimioterapia e terapia hormonal em câncer de mama precoce com seguimento de 15 anos; base evidencial para a eficácia das combinações em HR+ que sustenta os regimes contemporâneos de trastuzumab + endocrinoterapia |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Coorte (grande) | NEJM | Risco de recorrência em 20 anos após 5 anos de terapia endócrina em câncer de mama ER+; demonstra a persistência do risco em PR+ que motiva o uso de estratégias combinadas, incluindo bloqueio anti-HER2 neste subgrupo |

---

## Informações de Comercialização no Brasil

O trastuzumab está **comercializado no Brasil** com **14 registros ativos** na ANVISA. Os dados individuais de cada registro (número de registro ANVISA, nome comercial e texto de indicação aprovada) não constam no Evidence Pack fornecido.

> Trastuzumab está disponível no Brasil sob diversas apresentações, incluindo o produto referência Herceptin® (Roche) e biossimilares aprovados pela ANVISA. A indicação registrada abrange câncer de mama HER2-positivo (estágio precoce e metastático) e câncer gástrico HER2-positivo.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — anticorpo monoclonal anti-HER2 (IgG1 humanizado); não é quimioterapia citotóxica convencional |
| Risco de Mielossupressão | Baixo em monoterapia; médio a alto quando combinado com quimioterapia (neutropenia é evento frequente nos regimes de combinação com taxanes ou antraciclinas) |
| Classificação de Emetogenicidade | Baixa (trastuzumab isolado); a emetogenicidade do regime é determinada pelos quimioterápicos associados |
| Itens de Monitoramento | Fração de ejeção ventricular esquerda (FEVE) antes do início e periodicamente durante o tratamento; hemograma completo; função hepática e renal; avaliação cardiológica em pacientes com fatores de risco |
| Proteção no Manuseio | Manuseio como anticorpo monoclonal antineoplásico; preparação em ambiente de assepsia com cabine de fluxo laminar; não exige EPI de quimioterapia citotóxica convencional, mas deve seguir os protocolos institucionais de segurança para medicamentos antineoplásicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O subgrupo HR+/HER2+ (que engloba os tumores PR+/HER2+) conta com pelo menos dois Phase 3 RCTs concluídos com trastuzumab (NCT01275677, N=3.270; NCT00667251, N=652) e com ensaios de combinação específica endocrinoterapia + anti-HER2 (MonarcHER, WSG-ADAPT HER2+/HR+, WSG-TP-II) que sustentam o nível L1 de evidência, justificando a progressão condicionada às guardrails.

**Para prosseguir, é necessário:**
- **Confirmar superexpressão de HER2** (IHC 3+ ou FISH amplificado) como pré-requisito obrigatório — PR+ isolado sem HER2+ não constitui indicação para trastuzumab
- **Completar dados de MOA** via consulta à API DrugBank (DB00072) para documentação formal do mecanismo de ação
- **Acessar bula completa (ANVISA)** para avaliação estruturada de advertências e contraindicações, incluindo risco de cardiotoxicidade
- **Definir plano de monitoramento cardíaco** (FEVE basal e a cada 3 meses) para uso combinado com antraciclinas ou em pacientes com risco cardiovascular preexistente
- **Definir estratégia de regime combinado** com base no estadiamento e histórico terapêutico: (1) trastuzumab + pertuzumabe + quimioterapia neoadjuvante/adjuvante; (2) trastuzumab + CDK4/6 inibidor + terapia endócrina (ex.: esquema MonarcHER); ou (3) T-DM1/T-DXd para doença residual ou progressão
---

