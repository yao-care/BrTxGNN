---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

O skill `txgnn-pipeline` confirma que o fluxo de escrita de relatórios TxGNN está no escopo. Procedendo agora com a geração do relatório.

---

> **Nota metodológica:** A previsão de maior pontuação TxGNN corresponde à *ceratoconjuntivite epitelial punctata* (rank 1, 99.57%), porém sem qualquer evidência clínica de suporte (L5 — Hold). A **conjuntivite bacteriana** (rank 2, 99.17%) apresenta o maior nível de evidência (L1) com ensaios clínicos diretos e é o foco deste relatório.

---

# Trimethoprim: De antibiótico bacteriano para conjuntivite bacteriana

## Resumo em Uma Frase

Trimethoprim é um antibiótico clássico amplamente utilizado no tratamento de infecções bacterianas, especialmente infecções do trato urinário (ITU) e respiratórias, habitualmente combinado com sulfametoxazol (cotrimoxazol/TMP-SMX).
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Bacteriana (Conjunctivitis)**, com a combinação tópica Polytrim (TMP/Polymyxin B) já aprovada pela FDA para uso oftálmico — atualmente com **3 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (ITU, infecções respiratórias) |
| Nova Indicação Prevista | Conjuntivite bacteriana (Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99.17% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação documentados neste pacote de evidências. Segundo informações farmacológicas amplamente estabelecidas, Trimethoprim pertence à classe dos inibidores de dihidrofolato redutase (DHFR) bacteriana, frequentemente utilizado em combinação com sulfametoxazol (cotrimoxazol/TMP-SMX). Sua eficácia em infecções bacterianas sistêmicas foi amplamente comprovada, e mecanisticamente é aplicável à conjuntivite bacteriana por atuar contra os mesmos patógenos oculares — *Haemophilus influenzae*, *Staphylococcus aureus* e *Streptococcus pneumoniae* — por meio de formulação tópica oftálmica.

A relação entre a indicação original (infecções bacterianas sistêmicas) e a nova indicação prevista (conjuntivite bacteriana) é direta: o mecanismo antibacteriano é o mesmo, mas a via de administração migra para uso tópico ocular. A combinação Polytrim (Trimethoprim 1 mg/mL + Polymyxin B 10.000 UI/mL) foi aprovada pela FDA para tratamento de conjuntivite bacteriana, criando sinergia contra Gram-negativos (Polymyxin B) e Gram-positivos (Trimethoprim), cobrindo o espectro completo dos principais causadores.

A vantagem estratégica da formulação tópica é significativa: as concentrações locais no tecido conjuntival superam amplamente a concentração inibitória mínima (CIM), enquanto a absorção sistêmica é mínima — contornando os riscos de toxicidade sistêmica (discrasias sanguíneas, reações cutâneas graves) associados ao TMP-SMX oral. Esse perfil farmacológico diferenciado, aliado à aprovação regulatória já existente nos EUA, fortalece e fundamenta a previsão do modelo TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Concluído | 124 | RCT único-cego comparando diretamente Polytrim (TMP/Polymyxin B) vs Moxifloxacino 0,5% no tratamento de conjuntivite em crianças; ambos aprovados pela FDA para esta indicação — evidência direta de nível A |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Phase 3 | Concluído | 218 | RCT duplo-cego com antibióticos profiláticos (incluindo TMP-SMX) em infecção por sarampo na Guiné-Bissau; avaliou redução de pneumonia pós-sarampo e complicações oculares bacterianas secundárias |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Phase 4 | Concluído | 252 | Estudo observacional sobre resistência antimicrobiana e microbioma intestinal/nasofaríngeo após curso curto de antibióticos em crianças de 6–59 meses em Burkina Faso; fornece contexto epidemiológico do uso de TMP em pediatria |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT multicêntrico | J Pediatric Ophthalmol Strabismus | Comparação multicêntrica da velocidade de eficácia clínica entre TMP-Polymyxin B (Polytrim) e Moxifloxacino 0,5% no tratamento de conjuntivite bacteriana em crianças |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Revisão sistemática & Meta-análise | J Pediatric Infect Dis Soc | Revisão e meta-análise de tratamentos antibióticos para conjuntivite neonatal por Chlamydia, incluindo eritromicina, azitromicina e trimethoprim; avaliação da eficácia e segurança |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Ensaio clínico | Am J Ophthalmology | Avaliação clínica de soluções oftálmicas de TMP combinado com sulfacetamida e Polymyxin B em pacientes com conjuntivite bacteriana e blefarite; documentação de eficácia e segurança oculares |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Observação clínica | Clin Ther | Levantamento pediátrico amplo de conjuntivite bacteriana aguda tratada com solução oftálmica TMP-Polymyxin B; eficácia demonstrada contra *H. influenzae* e *S. pneumoniae* — os patógenos mais frequentes |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Revisão | J Pediatric Ophthalmol Strabismus | Importância do uso de agentes antimicrobianos no controle de surtos epidêmicos de conjuntivite bacteriana contagiosa por *S. pneumoniae*; recomendações clínicas práticas |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Revisão | Paediatr Child Health | Revisão da etiologia, características clínicas e manejo da conjuntivite infecciosa aguda em crianças após o período neonatal; papel dos antibióticos tópicos incluindo TMP |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Relato de caso | Ophthalmic Plast Reconstr Surg | Conjuntivite crônica por *Nocardia nova* em paciente com stent de silicone; sensibilidade ao TMP/sulfametoxazol documentada em cultura, sugerindo espectro de cobertura mais amplo do que esperado |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Estudo retrospectivo | Antibiotics (Basel) | Infecções oculares por MSSA em Taiwan (2010–2017): características clínicas moleculares e perfil de sensibilidade antimicrobiana incluindo TMP, com comparação CA vs HA |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Série de casos | Curr Opin Ophthalmology | Síndrome oculoglandular de Parinaud por *Bartonella henselae* (doença da arranhadura do gato) como causa de conjuntivite granulomatosa; antimicrobianos e manejo clínico |
| [3262623](https://pubmed.ncbi.nlm.nih.gov/3262623/) | 1988 | Estudo microbiológico | J Clin Microbiol | Caracterização bioquímica e epidemiológica de *H. influenzae* biótipo aegyptius associado à Febre Purpúrica Brasileira (FPB), precedida por conjuntivite purulenta — patógeno-alvo clássico do TMP |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A combinação Polytrim (Trimethoprim/Polymyxin B) em colírio já é aprovada pela FDA para conjuntivite bacteriana, com ensaio clínico direto (Phase 4, n=124) confirmando eficácia comparável ao moxifloxacino. A formulação tópica elimina os principais riscos sistêmicos do TMP-SMX oral. O principal obstáculo é a ausência total de registro no Brasil, que exige avaliação regulatória completa junto à ANVISA antes de qualquer aplicação clínica local.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API — lacuna de evidência de alta prioridade (DG002)
- Levantar advertências, contraindicações e interações da bula oficial — lacuna bloqueante (DG001) que impede avaliação de segurança inicial
- Avaliar a viabilidade de registro do produto oftálmico (Polytrim ou equivalente genérico) junto à ANVISA, incluindo requisitos de estabilidade e esterilidade para uso oftálmico
- Verificar o perfil de resistência local de *Pseudomonas aeruginosa* (resistência natural ao Trimethoprim), relevante para casos refratários de conjuntivite no contexto brasileiro
- Validar a aplicabilidade das evidências norte-americanas para o perfil epidemiológico de patógenos causadores de conjuntivite no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

