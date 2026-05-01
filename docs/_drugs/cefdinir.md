---
layout: default
title: Cefdinir
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Cefdinir
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

# Cefdinir: De infecções bacterianas à pielonefrite

## Resumo em Uma Frase

Cefdinir é uma cefalosporina de terceira geração oral, utilizada no tratamento de infecções bacterianas como pneumonia comunitária, sinusite aguda, otite média e infecções de pele e tecidos moles.
O modelo TxGNN identifica **Pielonefrite (Pyelonephritis)** como a indicação com maior suporte de evidências (ranking 10 entre as previsões),
atualmente com **0 ensaios clínicos** registrados diretamente para esta combinação e **10 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (pneumonia, sinusite, otite média aguda, infecções de pele) |
| Nova Indicação Prevista | Pielonefrite (Pyelonephritis) |
| Pontuação de Previsão TxGNN | 94.64% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base em informações conhecidas, Cefdinir é uma cefalosporina de terceira geração oral que exerce seu efeito antimicrobiano inibindo a síntese da parede celular bacteriana — ligando-se às Proteínas de Ligação à Penicilina (PBPs) e bloqueando a etapa de transpeptidação, o que leva à lise bacteriana. Este mecanismo confere atividade de amplo espectro contra gram-positivos e, em especial, contra gram-negativos relevantes clinicamente.

A pielonefrite é causada predominantemente por *Escherichia coli*, *Klebsiella pneumoniae* e *Proteus mirabilis* — exatamente os gram-negativos para os quais cefalosporinas de terceira geração demonstram excelente cobertura antimicrobiana. Adicionalmente, Cefdinir alcança concentrações urinárias eficazes após administração oral, tornando-o farmacologicamente adequado para infecções do trato urinário superior.

Na prática clínica atual, Cefdinir já é empregado como terapia de transição oral (*step-down*) em pielonefrite e infecções urinárias complicadas, sobretudo diante da crescente resistência a fluoroquinolonas e cotrimoxazol — os agentes de primeira linha tradicionais. A previsão do TxGNN, portanto, reflete uma realidade clínica emergente amplamente documentada na literatura recente, conferindo alta plausibilidade farmacológica a esta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados especificamente para Cefdinir em pielonefrite.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41160587](https://pubmed.ncbi.nlm.nih.gov/41160587/) | 2025 | Estudo Comparativo Retrospectivo | Journal of Pharmacy Practice | Comparação direta de cefdinir vs. cefalexina como terapia step-down oral em pielonefrite e urossepse; avalia taxa de falha clínica entre as duas opções |
| [30662274](https://pubmed.ncbi.nlm.nih.gov/30662274/) | 2019 | RCT | Infection and Drug Resistance | Sitafloxacina oral vs. ceftriaxona IV seguida de cefdinir oral para pielonefrite aguda e ITU complicada; demonstra eficácia comparável entre os regimes |
| [37414282](https://pubmed.ncbi.nlm.nih.gov/37414282/) | 2023 | Revisão Sistemática | Journal of the American Pharmacists Association | Revisão sistemática do uso de cefalosporinas em pielonefrite não complicada; contextualiza cefdinir como alternativa às fluoroquinolonas e SMX-TMP |
| [38482607](https://pubmed.ncbi.nlm.nih.gov/38482607/) | 2024 | Estudo Observacional Multicêntrico | Journal of Antimicrobial Chemotherapy | Padrões de prescrição empírica para pielonefrite em 15 pronto-socorros dos EUA; identifica cefdinir como opção alternativa emergente |
| [36027632](https://pubmed.ncbi.nlm.nih.gov/36027632/) | 2022 | Estudo Transversal | American Journal of Emergency Medicine | Efetividade de antibióticos para ITU em pronto-socorros na fronteira EUA-México; analisa resistência e adequação de cefdinir como escolha empírica |
| [30119986](https://pubmed.ncbi.nlm.nih.gov/30119986/) | 2018 | Coorte Retrospectiva | American Journal of Emergency Medicine | Comparação de fluoroquinolonas/SMX-TMP vs. cefalosporinas (incluindo cefdinir) para pielonefrite em pacientes com alta hospitalar |
| [22010614](https://pubmed.ncbi.nlm.nih.gov/22010614/) | 2011 | Revisão/Diretriz | American Family Physician | Diretrizes para diagnóstico e tratamento de cistite não complicada; referência para comparação com espectro de indicação superior (pielonefrite) |
| [41769599](https://pubmed.ncbi.nlm.nih.gov/41769599/) | 2026 | Relato de Caso | Cureus | Pielonefrite recorrente em quadriplegia com nefrolitíase: reavaliação do uso de cefdinir oral nessa população de difícil manejo |
| [40708906](https://pubmed.ncbi.nlm.nih.gov/40708906/) | 2025 | Relato de Caso | Frontiers in Pediatrics | Pielonefrite xantogranulomatosa em lactente de 47 dias: relato de manejo e seleção de antibiótico empírico |
| [3209480](https://pubmed.ncbi.nlm.nih.gov/3209480/) | 1988 | Estudo Pré-Clínico In Vivo | Journal of Antibiotics | Atividade antibacteriana in vivo de FK482 (cefdinir) em modelos animais de infecções sistêmicas por *E. coli*, *Klebsiella* e *Proteus* — organismos-chave da pielonefrite |

---

## Informações de Comercialização no Brasil

Cefdinir está registrado com **3 licenças** ativas no mercado brasileiro (status: comercializado). Os dados detalhados dos registros individuais — número de registro ANVISA, nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack e devem ser consultados diretamente no portal da ANVISA (consulta de medicamentos registrados).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Cefdinir apresenta uso clínico documentado como terapia step-down oral em pielonefrite, sustentado por 1 RCT, 1 revisão sistemática e múltiplos estudos observacionais multicêntricos publicados entre 2018 e 2025. A indicação é mecanisticamente coerente com o espectro antibacteriano do fármaco contra os principais patógenos gram-negativos da pielonefrite, e sua disponibilidade oral representa vantagem prática relevante no cenário atual de resistência crescente às opções de primeira linha.

**Para prosseguir, é necessário:**
- Dados completos de advertências e contraindicações da bula ANVISA (atualmente ausentes no Evidence Pack)
- Mecanismo de ação detalhado via DrugBank (MOA não disponível)
- Dados dos registros ANVISA: número de registro, nome comercial, forma farmacêutica e indicação aprovada para os 3 produtos registrados
- Avaliação farmacocinética em insuficiência renal (particularmente relevante para infecções urinárias e pielonefrite)
- Dados de resistência local aos gram-negativos urinários no contexto brasileiro, para validar eficácia empírica no Brasil
---

