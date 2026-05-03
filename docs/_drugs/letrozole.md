---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: Da Terapia Endócrina ao Carcinoma Mamário Feminino (Female Breast Carcinoma)

## Resumo em Uma Frase

Letrozole é um inibidor não esteroidal de aromatase de terceira geração, amplamente aprovado no mundo para o tratamento do câncer de mama com receptor hormonal positivo em mulheres pós-menopausa, porém sem registro ativo na ANVISA no Brasil até esta data.
O modelo TxGNN prevê com 99,98% de confiança que pode ser eficaz para o **Carcinoma Mamário Feminino (Female Breast Carcinoma)**,
atualmente com **mais de 40 ensaios clínicos registrados** — incluindo múltiplos estudos Phase 3 concluídos — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro na ANVISA |
| Nova Indicação Prevista | Carcinoma Mamário Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) registrados de forma estruturada neste sistema. Com base nas informações amplamente disponíveis, Letrozole pertence à classe dos **inibidores não esteroidais de aromatase**. A enzima aromatase (CYP19A1) catalisa a conversão de andrógenos em estrógenos nos tecidos periféricos — especialmente o tecido adiposo — de mulheres na pós-menopausa. Ao inibir esta via de forma competitiva e reversível, Letrozole reduz os níveis séricos de estradiol em até 98%, privando células tumorais que expressam o receptor estrogênico (ERα/ESR1) de seu principal sinal proliferativo.

O carcinoma mamário feminino representa a indicação central de Letrozole na oncologia global, aprovada pela FDA (EUA), EMA (Europa), PMDA (Japão) e outras agências regulatórias para os contextos neoadjuvante, adjuvante e de doença avançada/metastática. A relação entre supressão estrogênica e inibição do crescimento de tumores ER+ é uma das associações farmacológicas mais bem validadas em toda a oncologia, sustentada por décadas de pesquisa clínica de alto nível, incluindo os estudos BIG 1-98, PALOMA-2, MONALEESA-2 e NATALEE.

A pontuação TxGNN de 99,98% confirma, pelo modelo de grafo de conhecimento, a correspondência direta entre o mecanismo de Letrozole e a biologia do carcinoma mamário feminino — uma validação cruzada entre o modelo computacional e a evidência clínica já consolidada. A ausência de registro na ANVISA não reflete limitação de eficácia, mas uma lacuna de acesso ao mercado brasileiro que pode ser explorada.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00003140](https://clinicaltrials.gov/study/NCT00003140) | Phase 3 | Concluído | 5.187 | Estudo MA.17 (NCIC CTG): Letrozole versus placebo após ≥5 anos de tamoxifeno adjuvante em mulheres com câncer de mama primário; estudo fundamental que estabeleceu o benefício da terapia adjuvante estendida |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Concluído | 4.172 | Comparação head-to-head de Letrozole (2,5 mg/dia × 5 anos) versus anastrozole (1 mg/dia × 5 anos) como adjuvância em mulheres pós-menopausa com câncer de mama HR+ com linfonodos positivos |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Ativo, não recrutando | 4.486 | Estudo POETIC: terapia endócrina perioperatória com inibidor de aromatase — determina se Ki67 medido pós-início de AI prediz tempo de recorrência de forma individual, orientando intensidade do tratamento adjuvante |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Concluído | 1.918 | Randomização duplo-cega de Letrozole versus placebo em mulheres que completaram 5 anos de inibidor de aromatase como adjuvância; avalia benefício de extensão adicional da terapia endócrina |
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | Concluído | 300 | Duração ótima de Letrozole neoadjuvante para regressão tumoral em mulheres pós-menopausa com câncer de mama primário HR+, visando viabilizar cirurgia conservadora da mama |
| [NCT00673335](https://clinicaltrials.gov/study/NCT00673335) | Phase 3 | Concluído | 170 | Estudo LIBER: Letrozole versus placebo para prevenção de câncer de mama em mulheres pós-menopausa portadoras de mutação germinativa BRCA1/2; duração de acompanhamento de 15 anos |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3B | Concluído | 301 | Estudo 4EVER: eficácia e segurança de everolimus + exemestane em câncer de mama ER+ localmente avançado ou metastático após progressão em inibidor de aromatase não esteroidal (como Letrozole) |
| [NCT06311383](https://clinicaltrials.gov/study/NCT06311383) | N/A | Concluído | 2.610 | Grande estudo observacional real-world (Alemanha): avaliação de efetividade de ribociclib + AI/fulvestrant versus monoterapia endócrina ou quimioterapia como tratamento de primeira linha em câncer de mama HR+/HER2- metastático |
| [NCT07340658](https://clinicaltrials.gov/study/NCT07340658) | Phase 3 | Não iniciado | 300 | Estudo SIE-3: Letrozole em formulação injetável subcutânea versus Femara® oral, ambos combinados com palbociclib, como primeira linha em câncer de mama HR+/HER2- avançado ou metastático — valida novas formulações do fármaco |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Concluído | 263 | Avaliação dos efeitos de Letrozole versus tamoxifeno sobre metabolismo ósseo (densidade mineral, marcadores de remodelação) e metabolismo lipídico em mulheres pós-menopausa com câncer de mama precoce HR+ ressecado |

---

## Evidências da Literatura

Atualmente não há literatura relacionada indexada para esta combinação específica de busca (female breast carcinoma + Letrozole).

> **Nota clínica:** Existe extenso corpo de evidências publicado em periódicos de alto impacto (NEJM, JCO, Lancet Oncology, Annals of Oncology) para indicações correlatas — como câncer de mama ER+ e HR+ — abrangendo os estudos PALOMA-2/3, MONALEESA-2, NATALEE, BIG 1-98 e PADA-1. A ausência de resultado nesta query específica reflete limitação do termo de busca, não falta de evidência bibliográfica.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia endócrina-alvo (Inibidor não esteroidal de Aromatase — classe das triazolas; não é citotóxico convencional) |
| Risco de Mielossupressão | Baixo — inibidores de aromatase não causam toxicidade hematológica direta; não há risco relevante de neutropenia ou trombocitopenia |
| Classificação de Emetogenicidade | Mínima (administração oral diária; náuseas leves relatadas em <10% dos pacientes) |
| Itens de Monitoramento | Densidade mineral óssea (DXA anual), perfil lipídico, enzimas hepáticas (ALT/AST), sintomas musculoesqueléticos (artralgia, artrite de AI) |
| Proteção no Manuseio | Precauções padrão para medicamentos orais; não requer infraestrutura especial de manuseio de citotóxicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Letrozole apresenta nível de evidência L1 para carcinoma mamário feminino, com múltiplos ensaios Phase 3 concluídos e score TxGNN de 99,98%. O fármaco é considerado padrão-ouro global para câncer de mama HR+ em pós-menopausa; a ausência de registro na ANVISA constitui a principal barreira de acesso no Brasil, não uma limitação de eficácia ou segurança.

**Para prosseguir, é necessário:**
- Completar o registro formal do mecanismo de ação (MOA) via DrugBank API — Data Gap DG002, prioridade alta
- Obter advertências e contraindicações da bula registrada internacionalmente (FDA/EMA) — Data Gap DG001, prioridade bloqueante para avaliação de segurança estruturada
- Avaliar estratégia regulatória para submissão de registro à ANVISA ou identificar parceiros com autorização vigente de importação
- Definir populações-alvo no contexto brasileiro: mulheres pós-menopausa com câncer de mama HR+/HER2- nos cenários neoadjuvante, adjuvante ou doença avançada/metastática
- Mapear interações medicamentosas relevantes no contexto brasileiro (anticoagulantes orais, fármacos cardiovasculares, antidiabéticos) via base de DDI
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

