---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Clotrimazole
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

Com base no Evidence Pack fornecido e seguindo o formato do sistema, aqui está o relatório completo:

---

# Clotrimazole: Das infecções fúngicas ao acne

## Resumo em Uma Frase

Clotrimazole é um antifúngico azólico sintético de amplo espectro, amplamente utilizado no tratamento de infecções fúngicas superficiais como tinea pedis, candidíase vulvovaginal e candidíase orofaríngea.
O modelo TxGNN prevê que pode ser eficaz para **Acne (acne (disease))**, com pontuação de previsão de **99,86%**.
Atualmente há apenas **1 ensaio clínico** (em estado suspenso, formulação combinada) e **nenhuma publicação científica** apoiando especificamente esta direção para uso isolado do fármaco.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antifúngico tópico (tinea, candidíase) — sem registro no Brasil |
| Nova Indicação Prevista | Acne (acne (disease)) |
| Pontuação de Previsão TxGNN | 99,86% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento farmacológico publicado, Clotrimazole é um imidazol sintético que inibe a enzima CYP51 (lanosterol 14α-desmetilase) dos fungos, bloqueando a biossíntese de ergosterol — componente essencial da membrana fúngica. Este mecanismo resulta em aumento da permeabilidade celular e morte do organismo fúngico (PMID 24863842).

A relação mecanística entre Clotrimazole e acne é indireta. O fármaco possui atividade comprovada contra *Malassezia* spp., responsável pela foliculite por *Malassezia* (pityrosporum folliculitis), uma condição frequentemente confundida clinicamente com acne vulgar. Contudo, o acne verdadeiro é uma doença inflamatória primariamente desencadeada por *Cutibacterium acnes* (bactéria Gram-positiva), que não possui parede celular com ergosterol — o alvo do Clotrimazole — e portanto não é susceptível ao seu mecanismo antifúngico.

O único ensaio clínico identificado (NCT01244256) avaliou uma combinação tripla de beclometasona + gentamicina + Clotrimazole, o que impossibilita isolar qualquer contribuição do Clotrimazole. O ensaio foi suspenso sem divulgação do motivo, levantando dúvidas adicionais de segurança ou viabilidade. A alta pontuação TxGNN provavelmente reflete sobreposição de categorias de doença inflamatória cutânea no grafo do conhecimento, e não uma relação mecanística direta com o acne vulgar.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspenso | 80 | Estudo comparativo da combinação Clotrimazole + Gentamicina + Beclometasona em pacientes com dermatose contaminada e lesões simétricas bilaterais. Ensaio suspenso; motivo não divulgado. Impossível isolar a contribuição individual do Clotrimazole. |

---

## Evidências da Literatura

Atualmente não há literatura científica relacionada ao uso de Clotrimazole especificamente para acne.

---

## Informações de Comercialização no Brasil

Clotrimazole não possui nenhum registro ativo na ANVISA. O medicamento não está comercializado no mercado brasileiro em nenhuma indicação.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora a pontuação do TxGNN para acne seja elevada (99,86%), a base mecanística é fundamentalmente fraca — Clotrimazole não possui atividade relevante contra *Cutibacterium acnes*, o principal agente causador do acne vulgar, pois este organismo não contém ergosterol. O único ensaio clínico disponível foi suspenso e avalia uma formulação combinada, não permitindo nenhuma conclusão sobre o Clotrimazole isolado, e não há qualquer literatura de suporte.

**Para prosseguir, é necessário:**
- Esclarecer previamente se o alvo terapêutico real é a foliculite por *Malassezia* (clinicamente confundida com acne), caso em que o mecanismo antifúngico poderia ser justificável
- Conduzir estudos pré-clínicos in vitro com Clotrimazole em modelos de foliculite fúngica
- Obter dados completos do mecanismo de ação via DrugBank API (remediação já identificada no Evidence Pack como DG002)
- Solicitar registro regulatório na ANVISA antes de qualquer desenvolvimento clínico no Brasil

---

> **📋 Contexto: Outras Indicações no Evidence Pack**
>
> Este Evidence Pack contém 10 indicações previstas com perfis de evidência muito distintos. As indicações de maior potencial de desenvolvimento imediato são:
>
> | Rank | Indicação | Nível de Evidência | Recomendação | Ensaios / Publicações |
> |------|-----------|-------------------|--------------|----------------------|
> | 2 | Vulvovaginite (vulvovaginitis) | **L1** | **Proceed with Guardrails** | 22 ensaios / 20 publicações |
> | 9 | Micose superficial (superficial mycosis) | **L2** | **Proceed with Guardrails** | 3 ensaios / 20 publicações |
> | 4 | Vulvovaginite tricomonial | L3 | Research Question | 4 ensaios / 20 publicações |
>
> A indicação de **vulvovaginite candidíasica (Rank 2)** possui o maior suporte clínico, incluindo Phase 3 RCT concluído com n=466 (NCT00755053) e múltiplos estudos de alta qualidade — representando a prioridade mais promissora no pipeline de reposicionamento deste fármaco no Brasil.
---

