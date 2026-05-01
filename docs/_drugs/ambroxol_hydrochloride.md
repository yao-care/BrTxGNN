---
layout: default
title: Ambroxol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 0
---

# Ambroxol Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ambroxol Hydrochloride: Avaliação de Reposicionamento — Dados Insuficientes para Análise Completa

## Resumo em Uma Frase

Ambroxol Hydrochloride é um agente mucolítico e secretolítico amplamente utilizado no tratamento de doenças respiratórias em todo o mundo.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise — possivelmente devido a falha na normalização do nome ou ausência de mapeamento no grafo de conhecimento.
Sem previsões disponíveis, não é possível realizar a análise de evidências padrão.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (sem registro no Brasil) |
| Nova Indicação Prevista | Nenhuma previsão gerada neste ciclo |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem resultados de predição |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão Disponível?

O Evidence Pack retornou `predicted_indications: []` — ou seja, o pipeline TxGNN não produziu nenhuma candidatura de reposicionamento para este fármaco neste ciclo. Há duas causas prováveis:

**1. Falha de mapeamento no grafo de conhecimento:** O campo `drugbank_id` está ausente (`null`). O pipeline depende do DrugBank ID para localizar o nó do fármaco no grafo. Embora a consulta ao DrugBank tenha retornado 1 resultado (`result_status: success`), o ID não foi propagado para os campos do Evidence Pack — bloqueando as etapas de predição KG e DL.

**2. Variação de nome:** A nomenclatura "AMBROXOL HYDROCHLORIDE" (sal cloridrato) pode não corresponder exatamente à entrada "Ambroxol" no grafo TxGNN. A normalização do nome precisa mapear a forma de sal para o INN base antes da predição.

> Ambroxol é o metabólito ativo da bromexina. Fora deste Evidence Pack, a literatura científica reporta potencial terapêutico em condições como Doença de Gaucher (variante GBA), síndromes de dor neuropática e distúrbios lisossomais — mas essas observações **não integram o Evidence Pack atual** e não devem fundamentar decisões formais de reposicionamento sem dados estruturados.

---

## Informações de Comercialização no Brasil

Nenhum registro encontrado na base de dados regulatória consultada (0 licenças).

> **Nota importante:** Ambroxol Hydrochloride é amplamente comercializado em países da América Latina sob marcas como Mucosolvan, Ambroxil e outras. A ausência de registros pode refletir uma falha na consulta ou uma incompatibilidade de nomenclatura com a base ANVISA. Recomenda-se verificação direta em [consulta.anvisa.gov.br](https://consulta.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de reposicionamento, dados de segurança estruturados ou registros regulatórios verificáveis, tornando inviável qualquer avaliação de viabilidade clínica neste momento.

**Para prosseguir, é necessário:**
- 🔴 **[DG001 — Bloqueante]** Obter advertências e contraindicações via bula ANVISA: baixar PDF do produto e extrair seções de segurança
- 🟠 **[DG002 — Alta]** Resolver DrugBank ID via API DrugBank (a consulta já retornou 1 resultado — propagar o ID para o campo `drug.drugbank_id`)
- 🔧 **Normalização de nome:** Confirmar que "AMBROXOL HYDROCHLORIDE" é mapeado para o nó "Ambroxol" (DB06742) no grafo TxGNN antes de reexecutar
- 🔄 **Reexecutar o pipeline** de predição KG + DL após resolução das lacunas acima
- ✅ **Verificar status ANVISA** diretamente para confirmar se o fármaco está comercializado no Brasil com outra denominação ou como componente de associação
---

