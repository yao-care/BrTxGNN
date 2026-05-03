---
layout: default
title: Abiraterona Acetate
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Abiraterona Acetate
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

# Abiraterona Acetato: Do Câncer de Próstata a Indicações Não Preditas — Dados Insuficientes para Ciclo Atual

## Resumo

Abiraterona Acetato é um inibidor da enzima CYP17A1, aprovado internacionalmente para o tratamento do câncer de próstata resistente à castração (CRPC), atuando ao bloquear a biossíntese de andrógenos em tecidos tumorais, adrenais e testiculares.
O modelo TxGNN **não identificou novas indicações de reposicionamento** para este fármaco no ciclo atual, pois há **duas lacunas críticas de dados** — ausência de informações regulatórias e de mecanismo de ação — que interromperam o pipeline de análise.
O fármaco **não possui registros vigentes no Brasil**, e a avaliação completa está bloqueada até que as lacunas sejam sanadas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata resistente à castração *(baseado em conhecimento geral; não registrado no Evidence Pack)* |
| Nova Indicação Prevista | Nenhuma previsão disponível no ciclo atual |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | **Hold** |

---

## Citotoxicidade

Abiraterona Acetato é classificado como antineoplásico por sua indicação primária no tratamento do câncer de próstata, ainda que atue como terapia hormonal-alvo (inibição enzimática), e não como quimioterapia citotóxica convencional.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo hormonal — Inibidor de biossíntese androgênica (CYP17A1); não é citotóxico convencional |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Baixa (baseado na classe farmacológica — inibidor hormonal de uso oral) |
| Itens de Monitoramento | Função hepática (ALT/AST), potássio sérico, pressão arterial, hemograma completo (CBC), testosterona e PSA |
| Proteção no Manuseio | Seguir regulamentos padrão de manuseio de antineoplásicos; evitar contato com gestantes ou pessoas que tentam conceber |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou candidatos de reposicionamento para Abiraterona Acetato neste ciclo, e a análise de segurança está bloqueada pela ausência de bula ANVISA. O fármaco também não possui registro ativo no Brasil, o que impõe barreiras regulatórias adicionais a qualquer desenvolvimento clínico local.

**Para prosseguir, é necessário:**
- **[DG001 — Bloqueante]** Baixar e extrair informações da bula da ANVISA (advertências, contraindicações, populações especiais)
- **[DG002 — Alta prioridade]** Consultar a API do DrugBank para obter dados de mecanismo de ação (MOA), categorias farmacológicas e interações medicamentosas
- Re-executar o pipeline TxGNN com o Evidence Pack completo após resolução das lacunas
- Avaliar viabilidade regulatória: caso surjam candidatos de reposicionamento, será necessário verificar o caminho de registro na ANVISA (importação, registro novo ou uso compassivo)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

