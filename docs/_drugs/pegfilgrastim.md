---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Pegfilgrastim
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

Using **txgnn-pipeline** to guide report generation for this BrTxGNN evidence pack.

---

# Pegfilgrastim: De neutropenia febril à retinopatia diabética grave não proliferativa

## Resumo em Uma Frase

Pegfilgrastim é uma forma pegilada do filgrastim (G-CSF), originalmente utilizado para reduzir a incidência de neutropenia febril em pacientes com neoplasias não mieloides submetidos à quimioterapia mielossupressora.
O modelo TxGNN prevê que pode ser eficaz para **Retinopatia Diabética Grave Não Proliferativa (Severe Nonproliferative Diabetic Retinopathy)**, com pontuação de previsão de **99,89%**.
Atualmente, **nenhum ensaio clínico** e **nenhuma publicação científica** apoiam diretamente essa direção, e a decisão recomendada é **Hold**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Redução de neutropenia febril em pacientes em quimioterapia mielossupressora |
| Nova Indicação Prevista | Retinopatia Diabética Grave Não Proliferativa (Severe Nonproliferative Diabetic Retinopathy) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 11 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações conhecidas, Pegfilgrastim é um análogo pegilado do G-CSF (fator de crescimento de colônias de granulócitos), cuja eficácia na prevenção de neutropenia febril foi amplamente comprovada em pacientes oncológicos. A pegilação prolonga sua meia-vida, permitindo administração única por ciclo de quimioterapia.

O fundamento mecanístico proposto para esta previsão é a expressão de receptores de G-CSF em células ganglionares da retina. Estudos pré-clínicos sugerem que o G-CSF possui potencial neuroprotetor retiniano — com efeitos antiapoptóticos e de promoção de reparo celular — o que poderia ser relevante na retinopatia diabética grave não proliferativa, condição caracterizada por dano isquêmico progressivo às células nervosas da retina.

Contudo, há uma contradição mecanística importante: o G-CSF também mobiliza células progenitoras endoteliais CD34+ e pode potencializar a angiogênese patológica mediada por VEGF. Em pacientes com retinopatia diabética em fase pré-proliferativa, esse efeito poderia teoricamente acelerar a progressão para a forma proliferativa, agravando o quadro em vez de tratá-lo. A direção clínica permanece incerta e bidirecional, o que limita fortemente o suporte a essa indicação no estágio atual.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Pegfilgrastim possui **11 registros** ativos no Brasil. Os detalhes individuais dos registros — número de registro, nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack e devem ser consultados diretamente no portal da ANVISA (https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN é baseada exclusivamente em inferência de grafo de conhecimento (nível L5), sem nenhum ensaio clínico ou publicação científica de suporte direto. Mais criticamente, o mecanismo proposto é contraditório — o G-CSF pode tanto exercer neuroproteção retiniana quanto estimular neovascularização patológica — tornando o risco-benefício desta indicação imprevisível sem estudos dedicados.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API ou literatura especializada
- Realizar estudos pré-clínicos em modelos animais de retinopatia diabética para avaliar o balanço neuroprotecção vs. angiogênese
- Avaliar o risco de progressão para retinopatia proliferativa antes de qualquer estudo em humanos
- Recuperar advertências, contraindicações e perfil de segurança completo a partir da bula registrada na ANVISA (DG001)
- Detalhar os 11 registros individuais da ANVISA para avaliação regulatória (nomes comerciais, formas farmacêuticas, indicações aprovadas)
---

