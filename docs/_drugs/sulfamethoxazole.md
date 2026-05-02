---
layout: default
title: Sulfamethoxazole
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Sulfamethoxazole
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

O skill TxGNN Pipeline confirma o contexto do projeto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Sulfamethoxazole: De infecções bacterianas a conjuntivite contagiosa aguda

## Resumo em Uma Frase

Sulfamethoxazole é um antibiótico da classe sulfonamida, classicamente utilizado em combinação com trimetoprima (TMP-SMX / cotrimoxazol) para o tratamento de infecções bacterianas como infecções do trato urinário, pneumocistose e infecções respiratórias.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Contagiosa Aguda (Acute Contagious Conjunctivitis)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil (sulfonamida antibacteriana; combinação TMP-SMX para infecções bacterianas sistêmicas) |
| Nova Indicação Prevista | Conjuntivite Contagiosa Aguda (Acute Contagious Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,63% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados neste Evidence Pack. Com base no conhecimento farmacológico estabelecido, o sulfamethoxazole pertence à classe das sulfonamidas e inibe a enzima **diidropteroato sintase (DHPS)**, bloqueando a síntese de folato nos microrganismos bacterianos — etapa essencial para a replicação celular. Quando associado à trimetoprima (que bloqueia o passo subsequente da mesma via metabólica), forma o cotrimoxazol (TMP-SMX), amplamente utilizado na prática clínica global.

A conjuntivite contagiosa aguda é uma infecção bacteriana da conjuntiva, frequentemente causada por *Haemophilus influenzae*, *Streptococcus pneumoniae* e *Staphylococcus aureus*. Como sulfonamida de amplo espectro com atividade reconhecida contra muitos desses patógenos, o sulfamethoxazole apresenta base mecanística para uso nessa indicação. De forma particularmente relevante, o **sulfacetamida** — outro membro da classe sulfonamida — já é amplamente utilizado em colírios tópicos para conjuntivite bacteriana, o que reforça fortemente a plausibilidade desta previsão do TxGNN: a classe já possui eficácia ocular documentada, e o modelo provavelmente identificou essa conectividade no grafo de conhecimento.

A previsão é portanto mecanisticamente coerente, mas requer validação específica para sulfamethoxazole em formulação oftálmica, considerando que perfis de resistência bacteriana local podem influenciar significativamente a eficácia prática.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação específica.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Observacional (retrospectivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análise de bacteriologia e perfis de susceptibilidade a antibióticos em conjuntivite bacteriana aguda pediátrica no oeste da Grécia; avalia padrões de resistência relevantes para a escolha de antibióticos de amplo espectro, incluindo sulfonamidas |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora a previsão do TxGNN seja mecanisticamente razoável — e a classe sulfonamida possua uso oftálmico topicamente documentado via sulfacetamida —, há apenas 1 estudo observacional de suporte indireto, nenhum ensaio clínico específico para a indicação, ausência total de dados de segurança no pacote e o fármaco não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) formais via consulta ao DrugBank (DB01015)
- Levantar advertências, contraindicações e interações medicamentosas por meio da bula ou consulta direta à ANVISA/FDA
- Investigar se existe formulação tópica oftálmica de sulfamethoxazole ou avaliar o uso do análogo de classe **sulfacetamida** como proxy de evidência
- Buscar ensaios clínicos de fase 2/3 com sulfonamidas tópicas para conjuntivite bacteriana aguda como evidência de classe
- Avaliar perfis locais de resistência bacteriana antes de qualquer proposta terapêutica, dado o crescente problema de resistência a sulfonamidas
---

