---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

Usando o skill `txgnn-pipeline` para confirmar o contexto do projeto BrTxGNN antes de gerar o relatório.

---

# Prasugrel: Do Síndrome Coronário Agudo à Hipertensão Pulmonar

## Resumo em Uma Frase

Prasugrel é um agente antiplaquetário da classe das tienopiridinas e inibidor irreversível do receptor P2Y12, originalmente indicado para prevenção de eventos trombóticos cardiovasculares em pacientes com síndrome coronário agudo (SCA) submetidos à intervenção coronária percutânea (ICP).
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**, com pontuação de **99,88%**; entretanto, as **2 publicações** e os **2 ensaios clínicos** recuperados pela busca sistemática apresentam relevância grau C — isto é, não abordam diretamente prasugrel nesta indicação — e a previsão permanece sem suporte empírico direto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dados dos registros ANVISA não disponíveis no conjunto consultado |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos registros consultados (Data Gap DG002). Com base no conhecimento farmacológico estabelecido, prasugrel é um pró-fármaco convertido em metabólito ativo que bloqueia irreversivelmente o receptor P2Y12 nas plaquetas, inibindo a ativação e agregação plaquetárias mediadas por ADP. Sua potência antiplaquetária é superior à da clopidogrel, com início de ação mais rápido.

A conexão teórica com a hipertensão arterial pulmonar (HAP) parte da observação de que plaquetas ativadas liberam serotonina, tromboxano A2 (TXA2) e fator de crescimento derivado de plaquetas (PDGF), mediadores com papel documentado na remodelação vascular pulmonar. Em teoria, a inibição do receptor P2Y12 poderia atenuar essa cascata e reduzir a progressão da vasculopatia pulmonar.

Contudo, essa conexão permanece altamente especulativa e nunca foi avaliada diretamente com prasugrel em modelos animais ou humanos de HAP. A pontuação elevada do TxGNN provavelmente reflete padrões de proximidade no grafo de conhecimento entre o alvo P2Y12 e nós relacionados a mediadores vasoativos — não uma relação farmacológica validada. Nenhum dos ensaios clínicos ou publicações recuperados na busca sistemática fornece evidência direta para este reposicionamento.

---

## Evidências de Ensaios Clínicos

> ⚠️ Os ensaios abaixo foram recuperados pela busca sistemática, mas **não têm relação direta com prasugrel em hipertensão pulmonar** (relevância grau C). Não há ensaios clínicos registrados para este par fármaco-indicação.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Concluído | 500 | Estudo observacional sobre uso de NOACs em idosos com fibrilação atrial não valvar na Espanha; sem relação com prasugrel ou HAP |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Concluído | 300 | Retrospectiva sobre trombose associada a câncer e critérios de elegibilidade a DOACs; sem relação com prasugrel ou HAP |

---

## Evidências da Literatura

> ⚠️ As publicações abaixo foram recuperadas pela busca sistemática, mas **não abordam especificamente prasugrel em hipertensão pulmonar**.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Coorte retrospectiva | Current Medical Research and Opinion | Fatores associados ao uso e adesão de clopidogrel em SCA pós-ICP; prasugrel mencionado como alternativa terapêutica — sem dados de HAP |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Observacional | Kardiologiia | Análise do impacto de terapia cardiovascular prévia em desfechos de COVID-19 no registro ACTIVE; sem relação com HAP |

---

## Informações de Comercialização no Brasil

Prasugrel possui **2 registros ANVISA** com status **comercializado**. Os campos detalhados (número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão preenchidos no conjunto de dados consultado — é necessário recuperar os dados diretamente no portal ANVISA para complementar esta seção.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| — | — | — | Dados não disponíveis no conjunto consultado |
| — | — | — | Dados não disponíveis no conjunto consultado |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para prasugrel em hipertensão pulmonar encontra-se no nível L5 — exclusivamente baseada em padrões do grafo de conhecimento, sem qualquer estudo clínico ou pré-clínico direto. Os ensaios e publicações recuperados não são pertinentes ao par fármaco-indicação investigado, e a conexão mecanística proposta (inibição P2Y12 → redução de mediadores plaquetários → atenuação da remodelação vascular pulmonar) é altamente especulativa.

**Para prosseguir, é necessário:**
- Recuperar dados completos dos 2 registros ANVISA (nome comercial, forma farmacêutica, indicação aprovada) via portal ANVISA
- Obter mecanismo de ação completo (MOA) via DrugBank API (DG002)
- Obter advertências, contraindicações e interações medicamentosas da bula ANVISA (DG001)
- Conduzir busca direcionada de estudos pré-clínicos com inibidores P2Y12 em modelos de hipertensão pulmonar antes de considerar qualquer hipótese translacional
- **Considerar priorizar a indicação de rank 2 (Migraine Disorder, L4)** como candidato mais promissor: existem dados publicados de prasugrel e outras tienopiridinas reduzindo crises de enxaqueca em pacientes com forame oval patente (PFO), com maior plausibilidade mecanística e base de evidências inicial identificada
---

