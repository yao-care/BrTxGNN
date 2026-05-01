---
layout: default
title: Potassium Bicarbonate
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 1
---

# Potassium Bicarbonate
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

Using `txgnn-pipeline` skill noted. Now generating the report from the Evidence Pack.

---

# Bicarbonato de Potássio: De Suplemento Eletrolítico para Gastroduodenite

## Resumo em Uma Frase

Bicarbonato de Potássio (KHCO₃) é um composto inorgânico alcalino utilizado principalmente como suplemento de potássio e agente tamponante, sem indicações formalmente registradas no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Gastroduodenite (Gastroduodenitis)**,
porém, atualmente, **nenhum ensaio clínico** e **nenhuma publicação** apoiam diretamente esta direção — a evidência é inteiramente baseada na previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação aprovada registrada no Brasil |
| Nova Indicação Prevista | Gastroduodenite (Gastroduodenitis) |
| Pontuação de Previsão TxGNN | 99,72% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação formal do Bicarbonato de Potássio no DrugBank. Do ponto de vista químico, sabe-se que o KHCO₃ é um sal alcalino que, em contato com ácido clorídrico gástrico, realiza uma reação de neutralização: **KHCO₃ + HCl → KCl + H₂O + CO₂**. Essa propriedade tamponante poderia, em tese, reduzir a irritação ácida sobre a mucosa gastroduodenal, justificando a associação com gastroduodenite.

A relação com a indicação prevista é de ordem mecanística indireta: compostos alcalinos similares (como o bicarbonato de sódio) são usados empiricamente como antiácidos, e a gastroduodenite está frequentemente associada ao excesso de ácido ou à erosão da mucosa por agentes ácidos. A suplementação adequada de potássio também pode, de forma acessória, apoiar a função das células da mucosa gástrica.

Contudo, o próprio sistema classifica este raciocínio como **inferência química indireta**, sem nenhuma base em estudos clínicos ou pré-clínicos. O bicarbonato de potássio tem sido muito menos estudado que o bicarbonato de sódio para uso gastrointestinal, e o excesso de alcalinização pode interferir na fisiologia gastrointestinal normal. A previsão do TxGNN, embora matematicamente elevada (99,72%), reflete padrões de similaridade no grafo de conhecimento — não validação clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O nível de evidência é L5 — a indicação de gastroduodenite é suportada exclusivamente pela previsão do modelo TxGNN, sem nenhum ensaio clínico, estudo pré-clínico ou publicação científica identificados. Adicionalmente, o fármaco não está comercializado no Brasil e não possui indicação aprovada em nenhum registro nacional, o que eleva a barreira regulatória para qualquer iniciativa de desenvolvimento.

**Para prosseguir, é necessário:**
- Levantamento de estudos pré-clínicos (modelos animais de gastroduodenite com bicarbonato de potássio ou compostos alcalinos análogos) para elevar o nível de evidência para pelo menos L4
- Descrição formal do mecanismo de ação (MOA) via consulta ao DrugBank API ou literatura farmacológica
- Avaliação de segurança detalhada: advertências, contraindicações e interações medicamentosas a partir da bula ou fontes regulatórias
- Análise comparativa com bicarbonato de sódio (composto análogo mais estudado) para fundamentar translação mecanística
- Estudo de viabilidade regulatória no Brasil antes de qualquer investimento em desenvolvimento clínico
---

