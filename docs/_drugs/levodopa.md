---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Levodopa: Da doença de Parkinson à encefalite subaguda de Rasmussen

## Resumo em Uma Frase

Levodopa é um precursor da dopamina, amplamente utilizado no tratamento da doença de Parkinson para repor a deficiência dopaminérgica no sistema nigroestriatal.
O modelo TxGNN prevê que pode ser eficaz para **Encefalite Subaguda de Rasmussen (Rasmussen Subacute Encephalitis)**,
porém **sem ensaios clínicos** e **sem publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson |
| Nova Indicação Prevista | Encefalite Subaguda de Rasmussen |
| Pontuação de Previsão TxGNN | 99.06% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Levodopa é um precursor da dopamina que atravessa a barreira hematoencefálica e é convertido em dopamina pela enzima DOPA descarboxilase. Seu uso principal é repor a deficiência dopaminérgica na via nigroestriatal, sendo o tratamento de referência para a doença de Parkinson. Não há dados detalhados de MOA disponíveis neste pacote de evidências — a análise abaixo baseia-se no conhecimento farmacológico estabelecido.

A encefalite de Rasmussen (RSE) é uma doença neuroinflamatória crônica rara, de caráter unilateral, cujo mecanismo patológico central envolve ataque autoimune mediado por linfócitos T CD8+ citotóxicos e microglia, resultando em epilepsia focal refratária e déficits neurológicos progressivos. Existe uma ligação mecanística teoricamente possível, porém muito fraca: os receptores dopaminérgicos D1 e D2 são expressos em linfócitos T, células dendríticas e macrófagos, o que poderia modular a neuroinflamação. Entretanto, o processo central da RSE é um ataque autoimune mediado por linfócitos T, sem relação farmacológica direta com o sistema dopaminérgico.

O efeito da dopamina sobre o limiar epiléptico varia conforme o subtipo de receptor (D1 pró-convulsivante, D2 anticonvulsivante), impossibilitando prever o efeito líquido em pacientes com RSE. A pontuação elevada do TxGNN (0.9906) provavelmente reflete a **proximidade topológica dos nós de doenças do SNC** no grafo de conhecimento — ambas são doenças neurológicas — e não uma relevância farmacológica genuína.

---

## Informações de Comercialização no Brasil

Levodopa possui **20 registros ativos** no Brasil com situação **Comercializado**. Os detalhes individuais dos registros (número de registro, nome comercial, forma farmacêutica, indicação aprovada) não estão disponíveis no conjunto de dados atual e precisam ser obtidos via ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para Levodopa na encefalite de Rasmussen está classificada como nível **L5** — apenas previsão do modelo, sem nenhum ensaio clínico ou publicação de suporte. A ligação mecanística é extremamente fraca: o alto score provavelmente reflete proximidade topológica no grafo de conhecimento de doenças do SNC, e não relevância farmacológica genuína. A relação risco-benefício é incerta e não justifica avanço sem evidências adicionais.

**Para prosseguir, é necessário:**
- Obter dados detalhados de MOA via DrugBank API (DG002)
- Download e análise da bula ANVISA em PDF para advertências e contraindicações (DG001)
- Busca bibliográfica expandida sobre dopamina e neuroinflamação em encefalites autoimunes
- Identificação de estudos pré-clínicos que sustentem a hipótese mecanística antes de qualquer reavaliação do nível de evidência
- Levantamento dos 20 registros ANVISA com detalhes de forma farmacêutica e indicação aprovada
---

