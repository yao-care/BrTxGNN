---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: Da leucemia linfoblástica aguda ao linfoma/leucemia linfoblástica de precursores

## Resumo em Uma Frase

Pegaspargase (Oncaspar®) é uma L-asparaginase peguilada derivada de *Escherichia coli*, utilizada como componente essencial de regimes de quimioterapia combinada para tratamento da leucemia linfoblástica aguda (LLA) em pacientes pediátricos e adultos.
O modelo TxGNN prevê que pode ser eficaz para **Linfoma/Leucemia Linfoblástica de Precursores (Precursor Lymphoblastic Lymphoma/Leukemia)**,
atualmente com **mais de 10 ensaios clínicos de Fase 3** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Leucemia linfoblástica aguda (LLA) |
| Nova Indicação Prevista | Linfoma/Leucemia Linfoblástica de Precursores (Precursor Lymphoblastic Lymphoma/Leukemia) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Pegaspargase é uma enzima antineoplásica cujo mecanismo de ação se baseia na depleção do aminoácido asparagina no plasma sanguíneo. Células tumorais de linhagem linfoblástica — tanto B quanto T — apresentam expressão drasticamente reduzida ou ausente de asparagine synthetase (ASNS), a enzima necessária para sintetizar asparagina intracelularmente a partir de glutamina. Diferentemente das células normais, essas células neoplásicas são incapazes de compensar a queda plasmática de asparagina, resultando em colapso da síntese proteica e subsequente apoptose. A conjugação com polietilenoglicol (PEG) prolonga a meia-vida plasmática para aproximadamente 5,7 dias — versus ~1,2 dias da L-asparaginase nativa — reduzindo a frequência de administração e a imunogenicidade.

A indicação original (LLA) e a nova indicação prevista (linfoma/leucemia linfoblástica de precursores, ALL/LBL pela classificação da OMS) representam dois polos de um mesmo espectro biológico: ambas resultam da expansão clonal de linfoblastos precursores B ou T com baixa expressão de ASNS. A distinção clínica reside principalmente no grau de envolvimento medular (predomínio leucêmico versus apresentação linfonodal/extranodal), e não em diferenças moleculares que alterariam a sensibilidade ao fármaco.

A previsão do TxGNN é, portanto, plenamente consistente com a biologia tumoral e com a prática clínica internacional. Protocolos pediátricos e adultos de referência global — BFM, COG, NOPHO, GIMEMA, FRALLE — já incorporam pegaspargase como agente obrigatório tanto no tratamento da LLA quanto do linfoma linfoblástico (LBL) de linhagem B e T, validando a aplicabilidade mecanística desta previsão de forma inequívoca.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Ativo (não recrutando) | 9.350 | LLA-B de risco padrão recém-diagnosticada e LBL-B localizado; avaliação de regimes de quimioterapia adaptados ao risco; maior RCT ativo nesta indicação |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Concluído | 6.136 | Protocolo ALL-BFM colaborativo internacional para crianças e adolescentes; pegaspargase como droga-backbone; alta qualidade metodológica e evidência direta |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Ativo (não recrutando) | 6.720 | Blinatumomabe + quimioterapia (incluindo pegaspargase) em LLA-B de risco padrão e síndrome de Down; avalia adição de imunoterapia ao backbone padrão |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | Recrutando | 5.951 | Inotuzumabe ozogamicina em LLA-B de alto risco; terapia pós-indução adaptada ao risco com pegaspargase como base quimioterápica |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Ativo (não recrutando) | 2.044 | Protocolo FRALLE 2016 francês: otimização do uso de L-asparaginase em crianças e adolescentes com LLA; compara diferentes regimes de asparaginase |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | Concluído | 650 | NOPHO: PEG-asparaginase intermitente vs contínua em LLA não-AR; define esquema ótimo de depleção de asparagina com menor toxicidade |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | Concluído | 600 | Total Therapy XVI: dose alta vs convencional de PEG-asparaginase na continuação; avalia farmacocinética, farmacodinâmica e sobrevida livre de eventos |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Concluído | 166 | Calaspargase pegol vs Oncaspar® (pegaspargase) em LLA de alto risco; comparação direta de formulações PEG-asparaginase confirma eficácia do produto original |
| [NCT00866307](https://clinicaltrials.gov/study/NCT00866307) | Phase 1 | Concluído | 104 | PEG-asparaginase intensificada em LLA de alto risco: estudo piloto de segurança e tolerabilidade; base para intensificação de dose nos protocolos atuais |
| [NCT00186875](https://clinicaltrials.gov/study/NCT00186875) | Phase 2 | Concluído | 47 | LLA pediátrica recidivada ou refratária: avalia taxa de resposta e sobrevida; fornece dados de eficácia em população de difícil tratamento |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase III RCT | J Clin Oncol | COG AALL1231: bortezomibe em T-ALL/T-LL recém-diagnosticados com pegaspargase como backbone obrigatório; avalia redução de irradiação craniana profilática |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | Phase III RCT | J Clin Oncol | COG AALL0232: dexametasona e metotrexate em alta dose melhoram sobrevida em LLA-B de alto risco pediátrica; pegaspargase é componente central do regime |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | Phase III RCT | J Clin Oncol | COG AALL0434: nelarabina em T-ALL recém-diagnosticada; pegaspargase como backbone; maior RCT em T-ALL pediátrica |
| [32552472](https://pubmed.ncbi.nlm.nih.gov/32552472/) | 2020 | Phase III RCT | J Clin Oncol | COG AALL0434: resultados favoráveis em T-LBL pediátrico com C-MTX/pegaspargase; valida eficácia de pegaspargase especificamente no componente linfoma linfoblástico |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Estudo comparativo | J Clin Oncol | DFCI 11-001: eficácia e toxicidade comparadas de pegaspargase vs calaspargase pegol em LLA pediátrica; confirma pegaspargase como padrão de referência |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Phase II | Blood Advances | GIMEMA LAL1913: pegaspargase 2000 UI/m² em 8 blocos para Ph− ALL/LL em adultos de 18–65 anos; demonstra viabilidade com estratificação por risco para TMO |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase II longitudinal | Leukemia | HyperCVAD + nelarabina + pegaspargase ± venetoclax em T-ALL/LBL adultos; acompanhamento prolongado confirma eficácia de pegaspargase em LBL de adultos |
| [21454191](https://pubmed.ncbi.nlm.nih.gov/21454191/) | 2011 | Estudo prospectivo | Clin Lymphoma Myeloma Leuk | Hyper-CVAD aumentado com intensificação de pegaspargase em LLA adulta em recaída; demonstra atividade clínica significativa no resgate |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Revisão consenso | Haematologica | Painel de especialistas sobre reconhecimento, prevenção e manejo de eventos adversos de pegaspargase em adultos com LLA; estratégias práticas de mitigação |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Revisão de especialista | Blood | Manejo de toxicidades de pegaspargase em adultos com LLA; revisão abrangente do perfil único de toxicidade, monitoramento e ajuste de dose |

---

## Informações de Comercialização no Brasil

O medicamento conta com **3 registros ativos** na ANVISA e está classificado como **Comercializado** no mercado brasileiro. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e texto de indicação aprovada) não estavam disponíveis nos dados desta análise.

Para consulta dos registros, acesse: [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/) e pesquise por "pegaspargase".

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Enzima antineoplásica (L-asparaginase PEGuilada) — mecanismo de depleção de asparagina, distinto das citotóxicas convencionais com dano ao DNA |
| Risco de Mielossupressão | Baixo (pegaspargase não causa mielossupressão direta; o efeito citotóxico é específico para células com baixa expressão de ASNS, poupando as células hematopoiéticas normais) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Função hepática (ALT, AST, bilirrubinas), enzimas pancreáticas (amilase, lipase), hemostasia (fibrinogênio, TP, TTPa, antitrombina III), glicemia, triglicerídeos, hemograma completo com diferencial, e atividade sérica de asparaginase |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de medicamentos citotóxicos; preparação em cabine de segurança biológica (BSC classe II) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A previsão do TxGNN é respaldada por nível de evidência L1, com múltiplos ensaios clínicos de Fase 3 concluídos — incluindo estudos com mais de 6.000 participantes — e literatura de alta qualidade em periódicos de primeira linha (*J Clin Oncol*, *Blood*, *Leukemia*). O mecanismo de ação é biologicamente validado e o fármaco já integra protocolos padrão internacionais para a indicação prevista, tanto para LLA quanto para LBL de precursores B e T.

**Para prosseguir, é necessário:**
- Verificar e consolidar os detalhes dos 3 registros ANVISA (números, nomes comerciais, formas farmacêuticas e indicações aprovadas no Brasil)
- Obter a bula brasileira para levantamento formal de advertências, contraindicações e indicações oficialmente aprovadas
- Confirmar se o registro brasileiro cobre explicitamente o linfoma linfoblástico (LBL), além da LLA
- Estabelecer protocolo de monitoramento de segurança adaptado para populações adultas (especialmente >55 anos), dado o perfil de toxicidade diferenciado em relação à população pediátrica
---

