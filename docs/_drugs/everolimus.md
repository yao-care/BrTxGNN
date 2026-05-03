---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: Do carcinoma de células renais ao lipossarcoma

## Resumo em Uma Frase

Everolimus é um inibidor de mTOR (mammalian target of rapamycin), originalmente aprovado para o tratamento de carcinoma de células renais avançado, tumores neuroendócrinos pancreáticos e câncer de mama hormônio-receptor positivo/HER2-negativo.
O modelo TxGNN prevê que pode ser eficaz para **Lipossarcoma (Liposarcoma)**, atualmente com **1 ensaio clínico de Fase 2** e **4 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Carcinoma de células renais avançado; tumores neuroendócrinos pancreáticos; câncer de mama HR+/HER2− |
| Nova Indicação Prevista | Lipossarcoma (Liposarcoma) |
| Pontuação de Previsão TxGNN | 99.88% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não Comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimento publicado, Everolimus é um análogo da rapamicina e inibidor seletivo do complexo mTORC1 (mammalian target of rapamycin complex 1). Ao bloquear a sinalização mTOR, impede a tradução de proteínas que regulam o ciclo celular (como ciclina D1 e proteína ribossômica S6K1), reduz a proliferação tumoral e inibe a angiogênese.

A relevância para o lipossarcoma reside na ativação aberrante da via AKT-mTOR observada nessa neoplasia. Um estudo imuno-histoquímico conduzido em 99 espécimes de lipossarcoma desdiferenciado (DDLPS) demonstrou ativação significativa das vias Akt/mTOR e MAPK, com confirmação in vitro do efeito antitumoral de um inibidor de mTOR (PMID 26518767). Essa base molecular confere plausibilidade biológica direta à previsão do TxGNN.

A abordagem combinada de Everolimus (mTORi) com Ribociclib (CDK4/6i) explora a sinergia entre dois eixos oncogênicos críticos no DDLPS: a amplificação de CDK4 — presente em quase todos os casos — e a via mTOR. Essa combinação já demonstrou inibição sinérgica do crescimento tumoral em múltiplos modelos pré-clínicos e está sendo avaliada em um ensaio clínico de Fase 2 com resultados publicados em 2024 (PMID 37967116), conferindo ao reposicionamento suporte clínico substantivo.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Ativo (não recrutando) | 48 | Estudo de dois centros e 2 braços avaliando Ribociclib + Everolimus em lipossarcoma desdiferenciado avançado (Braço A) e leiomiossarcoma (Braço B), em pacientes com ≥1 terapia sistêmica prévia; Ribociclib 300 mg/dia (3 semanas ligado/1 semana desligado) + Everolimus 2,5 mg; resultados de 2024 publicados no Clinical Cancer Research (PMID 37967116) |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 RCT — resultado completo | Clinical Cancer Research | SAR-096: Ribociclib + Everolimus em DDL e LMS avançados; CDK4/6 em DDL e mTOR em LMS como alvos de interesse biológico; inibição sinérgica do crescimento validada em modelos tumorais múltiplos |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Estudo de mecanismo molecular | Tumour Biology | Ativação imuno-histoquímica das vias Akt-mTOR e MAPK em 99 espécimes de DDLS; estudo in vitro demonstrando efeito antitumoral de inibidor de mTOR na linhagem DDLS |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisão / estudo pré-clínico PDOX | Frontiers in Oncology | Modelos PDOX de sarcoma identificando combinações eficazes com inibidores de CDK (palbociclib); estratégia com implicações para aplicação clínica, incluindo associação com agentes mTOR |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Estudo pré-clínico de combinação | Anticancer Research | Eribulin em combinação com agentes de mecanismos diferentes (incluindo inibidores de mTOR) em modelos de xenoenxerto humano, incluindo lipossarcoma; confirma atividade pré-clínica de combinações no contexto de lipossarcoma |

---

## Informações de Comercialização no Brasil

Everolimus **não possui registros na ANVISA** e não está comercializado no mercado brasileiro. Não há dados de licença, nome comercial ou indicação aprovada localmente disponíveis.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (inibidor de mTOR — classe rapalogue/análogo da rapamicina) |
| Risco de Mielossupressão | Baixo a Médio — anemia, trombocitopenia e leucopenia podem ocorrer; menos frequente do que com quimioterapia citotóxica convencional |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo (com diferencial); glicemia em jejum; triglicerídeos e colesterol; função renal (creatinina, ureia); função hepática (ALT, AST, bilirrubinas); TC de tórax periódica para rastreamento de pneumonite não-infecciosa |
| Proteção no Manuseio | Seguir regulamentos institucionais para manuseio de antineoplásticos orais; precauções padrão com EPI conforme protocolo de citotóxicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Os dados de advertências principais, contraindicações e interações medicamentosas não estão disponíveis neste Evidence Pack — a obtenção da bula oficial (FDA, EMA ou ANVISA, se registrado) é etapa obrigatória antes de qualquer uso clínico ou avaliação de segurança formal.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A base molecular para o uso de everolimus em lipossarcoma desdiferenciado está estabelecida (ativação documentada da via AKT-mTOR em DDLPS) e um ensaio clínico de Fase 2 com everolimus em combinação está ativo, com dados publicados em 2024 em periódico de alto impacto. Entretanto, everolimus não é aprovado especificamente para lipossarcoma, os dados disponíveis são de combinação com ribociclib (não monoterapia), e o fármaco não possui registro no Brasil — o que exige guardrails regulatórios e de segurança antes de qualquer passo clínico.

**Para prosseguir, é necessário:**
- Obter e revisar a bula oficial (FDA/EMA) para extrair advertências completas, contraindicações e perfil de interações medicamentosas
- Confirmar o mecanismo de ação (MOA) detalhado via consulta ao DrugBank API (DG002)
- Acompanhar os resultados finais do NCT03114527 (SAR-096) quando publicação completa estiver disponível
- Avaliar viabilidade de registro na ANVISA ou acesso via uso compassivo/importação excepcional para o contexto brasileiro
- Definir estratégia posológica (monoterapia versus combinação com CDK4/6 inibidor) com base nos dados de eficácia e tolerabilidade disponíveis
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

