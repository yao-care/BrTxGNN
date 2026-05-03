---
layout: default
title: Palbociclibe
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 0
---

# Palbociclibe
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

# Palbociclib: Avaliação de Reposicionamento — Dados Insuficientes para Análise Completa

## Resumo

Palbociclib (registrado no sistema como "PALBOCICLIBE") é um inibidor de CDK4/6 da classe das terapias-alvo, indicado para o tratamento de câncer de mama hormônio-receptor positivo e HER2-negativo (HR+/HER2−).
O Evidence Pack atual **não contém indicações previstas pelo TxGNN**, o que impossibilita a análise de reposicionamento neste momento.
Para avançar, é necessário resolver os dois gaps de dados críticos identificados (DG001 e DG002) e executar o pipeline de predição.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Câncer de mama HR+/HER2− (dados detalhados pendentes — ver DG001) |
| Nova Indicação Prevista | Nenhuma indicação prevista disponível no Evidence Pack |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 — sem predições nem estudos no Evidence Pack atual |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 7 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Esta seção não pode ser preenchida no ciclo atual.

O campo `predicted_indications` está vazio, o que significa que o modelo TxGNN ainda não gerou candidatos de reposicionamento para este fármaco. Sem uma indicação-alvo definida, não é possível avaliar a coerência mecanística de nenhuma hipótese de reposicionamento.

Adicionalmente, o dado de mecanismo de ação (MOA) está ausente (DG002), o que limitaria a análise mesmo que houvesse uma indicação prevista. Recomenda-se consultar o DrugBank (DB01229 — palbociclib) para obter os alvos moleculares antes de prosseguir.

---

## Informações de Comercialização no Brasil

O fármaco está registrado no Brasil com **7 registros ativos** confirmados pela ANVISA. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não foram recuperados na coleta atual.

> Para visualizar os registros completos, consulte diretamente o portal da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/) pesquisando por "palbociclibe".

---

## Citotoxicidade

Palbociclib é classificado como antineoplásico (inibidor de CDK4/6 — terapia-alvo molecular), portanto esta seção se aplica.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | Terapia-alvo — Inibidor de CDK4/6 (não citotóxico convencional) |
| Risco de Mielossupressão | Alto — neutropenia é o efeito adverso dose-limitante mais comum da classe; monitoramento obrigatório |
| Classificação de Emetogenicidade | Baixa a mínima (conforme diretrizes ASCO/MASCC para inibidores orais de CDK4/6) |
| Itens de Monitoramento | Hemograma completo (CBC) antes de cada ciclo; função hepática; função renal em populações de risco |
| Proteção no Manuseio | Seguir protocolos institucionais de manuseio de antineoplásicos orais (capsula intacta — não triturar) |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em dois itens críticos: ausência de indicações previstas pelo TxGNN e ausência de dados de segurança (advertências, contraindicações e bula). Sem esses dados, não é possível conduzir nem a análise de eficácia nem a avaliação de segurança para qualquer indicação de reposicionamento.

**Para prosseguir, é necessário:**

- **\[DG001 — Bloqueante\]** Baixar e processar a bula da ANVISA para extrair advertências e contraindicações aprovadas no Brasil
- **\[DG002 — Alta Prioridade\]** Consultar a DrugBank API (buscar por "palbociclib") para obter MOA, alvos moleculares e categorias farmacológicas
- **Executar o pipeline TxGNN** para gerar `predicted_indications` e habilitar a análise de reposicionamento
- **Recuperar detalhes dos 7 registros** ANVISA (número, nome comercial, forma farmacêutica, indicação aprovada)
- **Verificar a grafia do INN** no sistema: padronizar de `"PALBOCICLIBE"` para `"palbociclibe"` (conforme INN em português brasileiro)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

