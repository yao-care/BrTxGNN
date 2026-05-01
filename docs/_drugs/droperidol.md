---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Droperidol
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

# Droperidol: Da sedação peri-operatória à Síndrome de Tourette

## Resumo em Uma Frase

Droperidol é um antipsicótico da classe butyrophenone, utilizado principalmente para sedação, prevenção de náuseas e vômitos pós-operatórios e contenção farmacológica de agitação aguda em ambiente hospitalar.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Tourette (Tourette syndrome)**, com base em sua afinidade ao receptor dopaminérgico D2 — o mesmo alvo terapêutico do haloperidol, tratamento de primeira linha para esta condição.
Atualmente, há **0 ensaios clínicos** e **1 publicação indireta** (relativa ao haloperidol, da mesma classe farmacológica) apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sedação peri-operatória, prevenção de náuseas/vômitos pós-operatórios e controle de agitação aguda |
| Nova Indicação Prevista | Síndrome de Tourette (Tourette syndrome) |
| Pontuação de Previsão TxGNN | 99.89% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados nesta análise. Com base nas informações disponíveis no Evidence Pack, droperidol pertence à classe butyrophenone — a mesma classe do haloperidol — e seu efeito clínico é mediado pelo antagonismo dos receptores dopaminérgicos D2 no sistema nervoso central. Essa propriedade farmacológica é amplamente reconhecida na literatura e sustenta a hipótese de reposicionamento.

A Síndrome de Tourette tem como principal substrato patológico a hiperativação dos receptores D2 no estriado, o que desencadeia os tiques motores e vocais característicos da condição. O haloperidol — butyrophenone farmacologicamente análogo ao droperidol — é reconhecido como tratamento de primeira linha para Tourette exatamente por bloquear esses receptores. A lógica de classe farmacológica é, portanto, cientificamente coerente: se o bloqueio D2 é o mecanismo terapêutico efetivo para Tourette e droperidol possui o mesmo mecanismo, a previsão do modelo TxGNN tem fundamento mecanístico defensável.

No entanto, há uma diferença operacional importante: o droperidol é formulado para uso parenteral de curta duração (sedação aguda, procedimentos), enquanto o tratamento da Síndrome de Tourette exige administração crônica. Não existem dados clínicos diretos sobre o uso de droperidol para Tourette, e a única publicação identificada trata do haloperidol, não do droperidol. A previsão do TxGNN representa uma analogia de classe, não uma evidência clínica direta.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Droperidol na indicação de Síndrome de Tourette.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Observacional | Current Psychiatric Therapies | Uso de **haloperidol** (butyrophenone da mesma classe farmacológica do droperidol) no tratamento de transtornos graves de comportamento — evidência indireta de classe, não específica para droperidol ou Tourette |

---

## Informações de Comercialização no Brasil

Droperidol possui **4 registros** com situação de comercialização ativa no Brasil. Os dados detalhados de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estavam disponíveis nesta análise. Para consulta completa, acesse o banco de dados de registros da ANVISA diretamente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN tem embasamento mecanístico coerente — droperidol e haloperidol compartilham o antagonismo D2, mecanismo validado para Tourette —, porém a ausência de qualquer ensaio clínico direto, a dependência de uma única publicação indireta de 1976 sobre um fármaco análogo, e a incompatibilidade de via de administração para uso crônico impedem a progressão imediata.

**Para prosseguir, é necessário:**
- Obter e analisar a bula ANVISA completa (advertências, contraindicações, posologia)
- Documentar o mecanismo de ação (MOA) detalhado via DrugBank
- Avaliar a viabilidade de formulação oral ou transdérmica para uso crônico, dado que a via parenteral atual é incompatível com tratamento prolongado de Tourette
- Realizar pelo menos um estudo pré-clínico ou série de casos prospectiva específica para Tourette antes de considerar ensaio clínico
- Revisar o perfil de segurança em uso prolongado — especialmente risco de discinesia tardia e prolongamento de QTc, reconhecidos na classe butyrophenone
---

