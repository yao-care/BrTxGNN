---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 500
evidence_level: L5
indication_count: 7
---

# Valsartan
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

A seguir está o relatório completo em Markdown para o Evidence Pack de Valsartan:

---

# Valsartan: Da Hipertensão Arterial à Hipertensão Renovascular Maligna

## Resumo em Uma Frase

Valsartan é um bloqueador do receptor de angiotensina II (BRA/ARB), originalmente utilizado no tratamento da hipertensão arterial, insuficiência cardíaca e proteção cardiovascular pós-infarto do miocárdio.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial, insuficiência cardíaca, proteção pós-infarto do miocárdio |
| Nova Indicação Prevista | Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Valsartan é um antagonista seletivo e competitivo do receptor de angiotensina II do tipo 1 (AT1R), pertencente à classe dos bloqueadores do receptor de angiotensina (BRA). Ao ocupar o AT1R sem ativá-lo, impede os efeitos vasoconstritores, pró-fibróticos, pró-inflamatórios e estimuladores da aldosterona mediados pela angiotensina II. O resultado é redução sustentada da pressão arterial com marcante proteção de órgãos-alvo — em particular rins e coração — sem o efeito colateral da tosse seca associado aos inibidores da ECA.

A hipertensão renovascular maligna tem como mecanismo central a hiperativação em cascata do sistema renina-angiotensina-aldosterona (SRAA): a estenose da artéria renal reduz a perfusão renal → o rim libera grandes quantidades de renina → a angiotensina II sobe acentuadamente → o AT1R é estimulado de forma excessiva → vasoconstricção sistêmica grave, dano endotelial progressivo e lesão renal acelerada. O bloqueio direto do AT1R pelo Valsartan interrompe exatamente esse ciclo patológico, e ainda reduz a pressão intraglomerular e inibe a fibrose renal mediada por TGF-β — o que é especialmente relevante porque a lesão renal nesses pacientes costuma progredir mesmo após o controle pressórico.

A conexão mecanística entre Valsartan e hipertensão renovascular maligna é biologicamente muito robusta. Os BRAs são farmacologicamente ideais em situações de SRAA hiperativado, e há ao menos um estudo experimental (Circulation, 2001) demonstrando que o bloqueio do AT1R preveniu hipertensão maligna letal em modelo animal mesmo sem redução significativa da pressão arterial, atribuindo o efeito à contenção da inflamação renal. A principal barreira à progressão clínica é a ausência total de ensaios controlados nessa entidade específica — e a preocupação real de que, em casos de estenose bilateral das artérias renais, o bloqueio do SRAA pode precipitar insuficiência renal aguda.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Estudo experimental (modelo animal) | *Circulation* | O bloqueio do receptor AT1 com antagonista ARB preveniu o desenvolvimento de hipertensão maligna letal em ratos, mesmo sem efeito redutor relevante na pressão arterial; o mecanismo proposto foi a supressão da inflamação renal induzida pela angiotensina II |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A conexão mecanística entre o Valsartan e a hipertensão renovascular maligna é biologicamente muito forte — ambos compartilham o SRAA hiperativado como eixo central —, mas a evidência disponível resume-se a um único estudo experimental em animais (L4), sem nenhum ensaio clínico registrado. Adicionalmente, existe risco clínico real de hipoperfusão renal aguda em pacientes com estenose bilateral das artérias renais, o que exige avaliação cautelosa antes de qualquer progressão.

**Para prosseguir, é necessário:**
- Realizar estudos de segurança dedicados em pacientes com hipertensão renovascular maligna confirmada (especialmente exclusão de estenose bilateral)
- Avaliar a viabilidade de ensaios clínicos controlados, considerando o caráter raro e frequentemente emergencial desta entidade
- Obter os dados completos da bula dos 20 registros ANVISA do Valsartan no Brasil (indicações aprovadas, advertências, contraindicações)
- Levantar dados de MOA detalhados via DrugBank API (DG002 pendente) para embasar análise de mecanismo completa
- Conduzir revisão sistemática de literatura específica sobre uso de ARBs em crises hipertensivas renovasculares malignas
---

