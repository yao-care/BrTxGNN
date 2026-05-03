---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Ibuprofen
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

Usando a skill **txgnn-pipeline** para orientar a geração deste relatório de reposicionamento.

---

# Ibuprofen: Do tratamento da dor e inflamação à Displasia Acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Ibuprofen é um anti-inflamatório não esteroidal (AINE) amplamente utilizado no alívio de dor, febre e inflamação, com 20 registros ativos no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Displasia Acromesomélica tipo Hunter-Thompson (Acromesomelic Dysplasia, Hunter-Thompson Type)**, uma doença genética rara do desenvolvimento esquelético.
Entretanto, esta previsão **não conta com nenhum ensaio clínico nem publicação científica** de suporte, situando-se no nível de evidência mais baixo (L5).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dor, febre e inflamação (AINE clássico) |
| Nova Indicação Prevista | Displasia Acromesomélica tipo Hunter-Thompson |
| Pontuação de Previsão TxGNN | 99.74% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento farmacológico bem estabelecido, Ibuprofen é um inibidor das enzimas ciclo-oxigenase (COX-1 e COX-2), reduzindo a síntese de prostaglandinas e, consequentemente, dor, inflamação e febre. Este mecanismo é amplamente documentado na literatura e constitui a base do seu uso como AINE de referência.

A Displasia Acromesomélica tipo Hunter-Thompson é causada por mutações no gene GDF5 (também denominado CDMP1), resultando em defeito na formação de cartilagem e encurtamento característico dos segmentos médios dos membros. Trata-se de uma condição estrutural e genética, sem componente inflamatório primário conhecido. A ligação entre a inibição de COX pelo Ibuprofen e a via de sinalização GDF5 não possui suporte mecanístico direto na literatura atual.

A hipótese mais plausível seria uma influência indireta: inibição de COX-2 → redução de PGE2 → possível modulação do microambiente da placa epifisária. Contudo, esta cadeia de raciocínio permanece estritamente teórica. A elevada pontuação do TxGNN (99.74%) provavelmente reflete padrões estruturais no grafo de conhecimento — como conectividade entre AINEs e doenças esqueléticas via nós intermediários — e não necessariamente uma relação farmacológica direta. Esta previsão é classificada como **L5: apenas sinal do modelo, sem suporte empírico**.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Ibuprofen possui **20 registros ativos** no Brasil. Os detalhes individuais dos registros (número ANVISA, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no conjunto de dados atual — os campos retornaram vazios na consulta. Para consulta completa, acesse diretamente o **[portal ANVISA — Consulta de Produtos Registrados](https://consultas.anvisa.gov.br/#/medicamentos/)**.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN baseia-se exclusivamente em padrão do grafo de conhecimento (L5), sem nenhum ensaio clínico, estudo pré-clínico ou publicação científica que relacione Ibuprofen à Displasia Acromesomélica tipo Hunter-Thompson. A doença é de origem genética estrutural (mutação GDF5), sem componente inflamatório primário que justifique o uso de um AINE como abordagem terapêutica de modificação de doença.

**Para prosseguir, é necessário:**
- Obter advertências e contraindicações via bula ANVISA (resolve DG001 — bloqueante para avaliação de segurança)
- Confirmar mecanismo de ação completo via DrugBank API (resolve DG002)
- Realizar busca manual em PubMed com termos combinados: `ibuprofen AND (GDF5 OR "skeletal dysplasia" OR chondrocyte OR "bone morphogenetic protein")` para verificar se há literatura relevante não capturada pelo coletor automático
- Consultar especialista em doenças raras ou genética médica para avaliar plausibilidade biológica antes de qualquer etapa de desenvolvimento clínico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

