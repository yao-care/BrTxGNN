---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: De Anti-inflamatório Articular para Espondilite Anquilosante

## Resumo

Flurbiprofen é um anti-inflamatório não esteroidal (AINE) da classe dos ácidos fenilalcanoicos, amplamente utilizado para controle de dor e inflamação em doenças reumáticas como artrite reumatoide e osteoartrite.
O modelo TxGNN prevê que pode ser eficaz para **Espondilite Anquilosante (Ankylosing Spondylitis)**, com **0 ensaios clínicos** registrados atualmente e **20 publicações** na literatura — incluindo múltiplos ensaios clínicos randomizados — apoiando esta direção.
Esta é a indicação com maior nível de evidência clínica entre as dez predições do modelo, classificada como L2 com recomendação **Proceed with Guardrails**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dor e inflamação em doenças reumáticas (artrite reumatoide, osteoartrite) |
| Nova Indicação Prevista | Espondilite Anquilosante (Ankylosing Spondylitis) |
| Pontuação de Previsão TxGNN | 99.97% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base nos estudos clínicos associados ao fármaco, Flurbiprofen é um AINE da classe dos ácidos fenilalcanoicos que atua como inibidor não seletivo de COX-1/COX-2, reduzindo a síntese de prostaglandinas (PGE2, PGI2) no tecido inflamado — mecanismo amplamente documentado na literatura reumatológica e referenciado em revisões abrangentes do fármaco.

A espondilite anquilosante (EA) é uma doença inflamatória crônica do esqueleto axial, impulsionada pelas vias de IL-17A e TNF-α. A prostaglandina E2 (PGE2) desempenha papel central na transmissão da dor e na erosão óssea nas articulações sacroilíacas, tornando a inibição de COX o alvo farmacológico direto para o controle sintomático. As diretrizes ASAS recomendam os NSAIDs como tratamento de primeira linha para EA axial ativa, conferindo ao mecanismo de flurbiprofen altíssima relevância fisiopatológica.

O que torna esta previsão particularmente significativa é que flurbiprofen já foi diretamente testado para EA em múltiplos ensaios clínicos randomizados entre 1974 e 1986, demonstrando eficácia equivalente à fenilbutazona, indometacina e naproxeno — os padrões terapêuticos da época. O modelo TxGNN está essencialmente redescobrindo evidências históricas sólidas, possivelmente não contempladas nos registros regulatórios brasileiros. A principal limitação é que esses ensaios utilizam design pré-moderno (sem grupo placebo puro, sem desfechos contemporâneos como ASDAS/BASDAI), o que exige atualização metodológica para fins regulatórios atuais. No cenário clínico vigente, os biológicos anti-TNF/IL-17 são a referência para EA refratária, posicionando flurbiprofen como alternativa para casos leves a moderados ou na fase inicial do tratamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para flurbiprofen em espondilite anquilosante nas bases consultadas (ClinicalTrials.gov e ICTRP).

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (duplo-cego cruzado) | British Medical Journal | 35 pacientes com EA; flurbiprofen 150 mg/dia mostrou eficácia terapêutica comparável à fenilbutazona, com boa tolerabilidade |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT (duplo-cego cruzado) | Annals of the Rheumatic Diseases | Comparação tripla duplo-cego cruzada — indometacina, flurbiprofen e placebo — em pacientes com EA |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (paralelo, duplo-cego) | Current Medical Research and Opinion | 26 pacientes com EA ativa por 6 semanas; flurbiprofen e indometacina igualmente eficazes no alívio da dor e sensibilidade articular |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (paralelo, duplo-cego) | European Journal of Clinical Pharmacology | 27 pacientes com EA ativa; flurbiprofen e fenilbutazona igualmente eficazes no alívio da dor e sensibilidade |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (duplo-cego cruzado) | New Zealand Medical Journal | 30 pacientes com EA; flurbiprofen 200 mg/dia vs. naproxeno 750 mg/dia — ambos muito eficazes sem diferença significativa de eficácia |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (comparativo, 26 sem.) | American Journal of Medicine | 57 pacientes com EA; flurbiprofen 200 mg/dia tão eficaz quanto indometacina no controle da dor após 26 semanas |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (comparativo, 26 sem.) | American Journal of Medicine | 90 pacientes com EA; flurbiprofen 200 mg/dia equivalente à fenilbutazona 300 mg/dia em 26 semanas; alguns casos controlados com 150 mg/dia |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Estudo de segurança | American Journal of Medicine | Análise de função hepática e renal em 1.677 pacientes com EA, OA ou AR em 9 ensaios de fase III; sem alterações clinicamente significativas |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Revisão | Drugs | Revisão abrangente da farmacologia e uso terapêutico de flurbiprofen em AR, OA, EA e condições relacionadas; 120–150 mg/dia comparável à aspirina em AR com menos efeitos adversos |
| [3963022](https://pubmed.ncbi.nlm.nih.gov/3963022/) | 1986 | Revisão | American Journal of Medicine | Experiência europeia com flurbiprofen em mais de 12 anos; segurança e eficácia documentadas em múltiplas condições reumáticas incluindo EA |

---

## Informações de Comercialização no Brasil

O Flurbiprofen possui **6 registros** ativos no Brasil com status comercializado. Os detalhes específicos de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack — recomenda-se consulta direta à base de dados da ANVISA para obter informações completas, especialmente para verificar se a espondilite anquilosante consta como indicação aprovada em algum desses registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há múltiplos ensaios clínicos randomizados (1974–1986) demonstrando eficácia de flurbiprofen equivalente aos tratamentos padrão da época para espondilite anquilosante, com mecanismo de ação (inibição COX-1/COX-2 → redução de PGE2) diretamente aplicável à patofisiologia da doença. O principal obstáculo é a ausência de ensaios com design moderno e a necessidade de confirmação do status regulatório nos registros brasileiros.

**Para prosseguir, é necessário:**
- Obter a bula completa registrada na ANVISA para verificar advertências, contraindicações e indicações aprovadas — dado crítico bloqueante (DG001)
- Confirmar mecanismo de ação detalhado via DrugBank API (DG002 — alta prioridade para análise de mecanismo)
- Consultar a ANVISA para verificar se algum dos 6 registros existentes já inclui espondilite anquilosante como indicação aprovada, evitando redundância regulatória
- Avaliar o design de um ensaio clínico moderno com desfechos contemporâneos (ASDAS, BASDAI) para posicionar flurbiprofen como alternativa custo-efetiva à EA leve a moderada, onde os biológicos podem ser inacessíveis
- Desenvolver plano de monitoramento de segurança gastrointestinal e renal para populações de risco (idosos, pacientes com comorbidades GI/renais)
---

