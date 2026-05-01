---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Clobazam
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

Com base no Evidence Pack fornecido, segue o relatório de avaliação de reposicionamento:

---

# Clobazam: Da Síndrome de Lennox-Gastaut à Epilepsia Relacionada a Infecção Febril

## Resumo em Uma Frase

Clobazam é uma benzodiazepina de classe 1,5 (1,5-BZD) utilizada como terapia adjuvante no controle de crises epilépticas, com indicação estabelecida para a Síndrome de Lennox-Gastaut (SLG).
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Epilepsia Relacionada a Infecção Febril (Febrile Infection-Related Epilepsy Syndrome — FIRES)**,
atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia — terapia adjuvante (Síndrome de Lennox-Gastaut) |
| Nova Indicação Prevista | Síndrome de Epilepsia Relacionada a Infecção Febril (FIRES) |
| Pontuação de Previsão TxGNN | 99.82% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações conhecidas, o clobazam é uma benzodiazepina de classe 1,5 que atua como modulador alostérico positivo do receptor GABA-A — diferindo estruturalmente das BZDs clássicas 1,4 (como diazepam e clonazepam), o que confere perfil farmacocinético distinto com menor sedação proporcional e meia-vida mais longa. Ao potencializar a transmissão inibitória GABAérgica, o fármaco reduz a excitabilidade neuronal e a propagação das descargas epilépticas.

FIRES é uma forma de estado de mal epiléptico super-refratário de início novo (NORSE), geralmente precipitada por infecção febril em crianças anteriormente saudáveis. Na fase aguda, as benzodiazepinas constituem medicamentos de primeira linha para sedação e controle de crises, sendo o lorazepam o agente mais documentado neste contexto clínico. Como clobazam pertence à mesma classe farmacológica, a previsão do TxGNN fundamenta-se na similaridade mecanicista intraclasse BZD — suportada pelo grafo de conhecimento (KG), que conecta clobazam a múltiplos subtipos de epilepsia refratária.

A vantagem teórica do clobazam sobre outras BZDs em FIRES reside especificamente na disponibilidade de formulação oral/enteral, que poderia facilitar estratégias de desmame de anestésicos gerais intravenosos (midazolam, propofol) — exatamente o cenário descrito na literatura identificada (PMID 35770765). Contudo, as publicações encontradas referem-se ao lorazepam e ao perampanel, não ao clobazam diretamente, limitando a evidência ao nível mecanicista e de analogia de classe.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | Epileptic Disorders | Lorazepam enteral demonstrou-se estratégia eficaz de desmame em pacientes com FIRES midazolam-dependentes — evidência indireta de viabilidade de BZD oral/enteral na fase de desmame do estado super-refratário |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | Perampanel reduziu dependência de barbituratos em criança de 13 anos com FIRES — contexto clínico de busca por agentes alternativos para desmame no estado epiléptico super-refratário |

---

## Informações de Comercialização no Brasil

Os detalhes individuais dos registros (número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis neste Evidence Pack. O fármaco possui **6 registros** ativos no mercado brasileiro com status **Comercializado**.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN apresenta fundamentação mecanicista razoável (classe BZD com atividade GABA-A positiva), mas as únicas publicações identificadas descrevem outros fármacos da mesma classe — lorazepam e perampanel — sem qualquer evidência clínica direta de clobazam em FIRES. Com nível de evidência L4 e ausência de ensaios clínicos, o conjunto de dados é insuficiente para recomendar avanço imediato.

**Para prosseguir, é necessário:**
- Levantamento específico de séries de casos ou estudos retrospectivos de clobazam em FIRES, NORSE ou estado de mal epiléptico super-refratário pediátrico
- Completar dados do mecanismo de ação (MOA) via consulta à API do DrugBank (DG002)
- Obter informações de segurança completas (advertências, contraindicações, interações medicamentosas) via download e análise da bula brasileira registrada na ANVISA (DG001)
- Recuperar detalhes dos 6 registros brasileiros (número de registro, nome comercial, forma farmacêutica, indicação aprovada) para confirmar a disponibilidade de formulação enteral/oral adequada à UTI pediátrica
- Avaliar a indicação de **Epilepsia Occipital Benigna** (rank 7, L3, 20 publicações com dados diretos de clobazam, recomendação *Proceed with Guardrails*) como alvo prioritário de reposicionamento em paralelo — apresenta base de evidências substancialmente mais robusta
---

