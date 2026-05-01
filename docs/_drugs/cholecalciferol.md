---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

O skill confirma que estou no contexto correto do pipeline TxGNN. Agora vou gerar o relatório seguindo o formato especificado no sistema.

---

# Colecalciferol: Da Deficiência de Vitamina D ao Hipoparatireoidismo Familiar Isolado por Secreção Deficiente de PTH

## Resumo em Uma Frase

Colecalciferol (Vitamina D3) é um pró-hormônio essencial amplamente utilizado na prevenção e tratamento da deficiência de vitamina D, raquitismo nutricional e osteomalácia — atualmente sem registro ANVISA identificado na base consultada.
O modelo TxGNN prevê que pode ser eficaz para o **Hipoparatireoidismo Familiar Isolado por Secreção Deficiente de PTH (familial isolated hypoparathyroidism due to impaired PTH secretion)**, com pontuação de **99,79%**, porém atualmente sem **nenhum ensaio clínico** nem **publicação** específica apoiando esta direção nesta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Deficiência de Vitamina D / Raquitismo nutricional (nenhum registro ANVISA identificado na base consultada) |
| Nova Indicação Prevista | Hipoparatireoidismo Familiar Isolado por Secreção Deficiente de PTH |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (nenhum registro identificado) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados na fonte consultada. Com base no conhecimento farmacológico estabelecido, o Colecalciferol (Vitamina D3) é o precursor da vitamina D, convertido no fígado em 25-hidroxivitamina D₃ e, posteriormente, nos rins pela enzima 1α-hidroxilase em calcitriol [1,25(OH)₂D₃] — a forma biologicamente ativa. O calcitriol atua como hormônio esteroidal, ligando-se ao receptor VDR para promover a absorção intestinal de cálcio, a reabsorção tubular renal de cálcio e a mobilização óssea de cálcio, processos centrais para a homeostase calcêmica.

No hipoparatireoidismo familiar isolado por secreção deficiente de PTH, um defeito genético impede a produção adequada de PTH pelas paratireoides, resultando em hipocalcemia crônica. Como o calcitriol — forma ativa derivada do colecalciferol — pode contornar a ausência de PTH ao agir diretamente nos tecidos-alvo (intestino e rim), existe uma conexão teórica pela via Colecalciferol → Calcitriol. De fato, o calcitriol é parte do tratamento padrão do hipoparatireoidismo.

Contudo, há uma limitação mecanística importante: o passo de ativação renal do colecalciferol (25-OH-D → calcitriol) é catalisado pela 1α-hidroxilase, cuja atividade é estimulada justamente pelo PTH. Na ausência de PTH, essa conversão fica gravemente prejudicada, tornando o colecalciferol um substrato menos eficiente do que a administração direta de calcitriol. Por isso, as diretrizes clínicas de hipoparatireoidismo preferem o calcitriol ou alfacalcidol ao colecalciferol. A pontuação elevada do TxGNN provavelmente reflete a proximidade de nós no grafo de conhecimento ("doenças do metabolismo do cálcio"), e não uma evidência clínica real para esta indicação ultrarara.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para o uso de colecalciferol no hipoparatireoidismo familiar isolado por secreção deficiente de PTH.

---

## Evidências da Literatura

Atualmente não há literatura relacionada especificamente ao uso de colecalciferol nesta indicação.

---

## Informações de Comercialização no Brasil

Nenhum registro ANVISA foi identificado para colecalciferol na base de dados consultada (total de registros: 0).

> **Observação:** O colecalciferol é um princípio ativo amplamente disponível no Brasil, frequentemente comercializado como suplemento alimentar ou medicamento de venda livre. A ausência de registros na consulta pode refletir limitações na cobertura da base ANVISA consultada ou classificação do produto como suplemento nutricional (fora do escopo da busca por medicamentos). Recomenda-se verificação direta no portal ANVISA (consulta.anvisa.gov.br).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão possui base mecanística teórica — o calcitriol (forma ativa do colecalciferol) é de fato utilizado no manejo do hipoparatireoidismo — mas a indicação específica de "hipoparatireoidismo familiar isolado por secreção deficiente de PTH" é ultrarara, não possui nenhum ensaio clínico nem publicação direcionada a colecalciferol, e na prática clínica o substrato ativo (calcitriol) é claramente preferido ao precursor (colecalciferol) neste contexto. O nível de evidência L5 não sustenta progressão clínica.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) completos via DrugBank API (DG002)
- Realizar busca sistemática de relatos de caso e séries de casos sobre colecalciferol no hipoparatireoidismo familiar isolado
- Comparar eficácia relativa colecalciferol vs. calcitriol/alfacalcidol neste contexto genético específico
- Revisar diretrizes clínicas de hipoparatireoidismo (Endocrine Society, ETA) quanto ao papel do colecalciferol como suplementação adjuvante
- Consultar diretamente o portal ANVISA para regularização regulatória no Brasil (DG001)
- Avaliar indicações com evidência superior identificadas no mesmo Evidence Pack: **佝僂病低磷血症 (L3, Rank 5)** e **osteodistrofia renal (L3, Rank 6)** apresentam suporte de ensaios clínicos e podem ser priorizadas
---

