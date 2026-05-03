---
layout: default
title: Teriparatida
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 0
---

# Teriparatida
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

# Teriparatida: Relatório de Avaliação Preliminar — Previsões TxGNN Indisponíveis

---

## Resumo

Teriparatida é um análogo sintético do hormônio paratireoidiano humano (PTH 1-34), originalmente indicado para o tratamento da osteoporose grave com alto risco de fratura em mulheres na pós-menopausa e em homens. O presente Evidence Pack não contém previsões de novas indicações pelo modelo TxGNN (`predicted_indications: []`), o que impede a geração de um relatório completo de reposicionamento. A avaliação está bloqueada por duas lacunas críticas de dados: ausência de informações sobre o mecanismo de ação (MOA) e ausência de advertências/contraindicações da bula registrada.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|---------|
| Indicação Original | Osteoporose grave (dado de conhecimento público — detalhes do registro ANVISA não preenchidos no pack) |
| Nova Indicação Prevista | **Não disponível** — `predicted_indications` está vazio |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | **Não avaliável** — sem previsões |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | **Hold** |

---

## Por que Este Relatório Está Incompleto?

O Evidence Pack retornou **3 registros na ANVISA** e **1 resultado no DrugBank**, confirmando que o fármaco existe e está em circulação. Contudo, dois bloqueadores críticos impedem o prosseguimento da análise:

1. **Previsões TxGNN ausentes**: O array `predicted_indications` está vazio. Sem uma indicação candidata prevista pelo modelo, não há hipótese de reposicionamento a avaliar.

2. **Dados da bula não recuperados**: Apesar do sucesso na consulta à ANVISA (3 registros encontrados), todos os campos dos registros (`license_number`, `product_name_zh`, `approved_indication_text`, etc.) estão em branco no JSON. Isso indica uma falha no passo de extração/preenchimento do pipeline, não na busca em si.

Teriparatida é um fármaco **não antineoplásico** (análogo de PTH, agente anabólico ósseo), portanto a seção de Citotoxicidade não se aplica.

---

## Informações de Comercialização no Brasil

Os dados de registro foram consultados com sucesso (3 licenças encontradas), mas os campos de detalhe retornaram vazios no Evidence Pack atual. Não é possível gerar a tabela de registros.

> Os registros precisam ser reprocessados a partir do pipeline ANVISA para recuperar nome comercial, forma farmacêutica e texto de indicação aprovada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança (dados de advertências e contraindicações não disponíveis neste pack).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está estruturalmente incompleto — sem previsões TxGNN e sem dados de bula extraídos, não há base para conduzir uma análise de reposicionamento. O fármaco está confirmado no mercado brasileiro, mas a análise não pode avançar até que as lacunas abaixo sejam resolvidas.

**Para prosseguir, é necessário:**

- [ ] **[Bloqueador]** Executar o modelo TxGNN para Teriparatida e popular `predicted_indications` com pelo menos uma indicação candidata
- [ ] **[Bloqueador]** Reprocessar os 3 registros ANVISA para extrair `license_number`, `product_name_zh`, `dosage_form` e `approved_indication_text`
- [ ] **[Alta prioridade]** Consultar DrugBank API para recuperar MOA completo (o query log indica sucesso com 1 resultado, mas o campo `drugbank_id` está nulo e `original_moa` está como `[Data Gap]`)
- [ ] **[Alta prioridade]** Baixar e parsear PDFs das bulas ANVISA para extrair advertências e contraindicações (DG001)
- [ ] Verificar se o `candidate_id` "TW-UNKNOWN-multi" indica ausência de mapeamento DrugBank — pode ser necessário mapear manualmente o INN "TERIPARATIDA" para `DB06285` (DrugBank ID padrão para teriparatide)

---

> ⚠️ **Nota**: Este relatório é gerado a partir de um Evidence Pack incompleto. Os dados de natureza clínica e regulatória precisam ser validados antes de qualquer uso. Este documento é estritamente para fins de pesquisa e não constitui aconselhamento médico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

