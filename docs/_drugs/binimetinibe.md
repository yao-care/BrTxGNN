---
layout: default
title: Binimetinibe
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 0
---

# Binimetinibe
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

# Binimetinibe: Avaliação de Reposicionamento – Previsões TxGNN Pendentes

## Resumo

Binimetinibe é um inibidor de MEK1/MEK2 (terapia-alvo) utilizado no tratamento do melanoma com mutação BRAF V600E/K, em combinação com encorafenibe.
O Evidence Pack atual **não contém previsões de novas indicações** geradas pelo modelo TxGNN, impossibilitando a análise completa de reposicionamento neste ciclo.
O fármaco está comercializado no Brasil com 2 registros, mas os detalhes dos registros e dados de segurança não foram populados nesta versão do pack.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Melanoma com mutação BRAF V600E/K (inibidor de MEK) |
| Nova Indicação Prevista | Pendente – sem previsões TxGNN disponíveis |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

Binimetinibe pertence à classe dos inibidores de MEK, categorizada como terapia-alvo antineoplásica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (Inibidor de MEK1/MEK2 – classe MAPK pathway) |
| Risco de Mielossupressão | Baixo a médio (menos pronunciado que quimioterapia citotóxica convencional) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Fração de ejeção ventricular esquerda (FEVE), acuidade visual, função hepática, CBC com diferencial, pressão arterial |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões de novas indicações (`predicted_indications: []`), e os campos de registro regulatório e segurança estão sem dados, o que impede qualquer avaliação de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN para gerar previsões de novas indicações para Binimetinibe
- Preencher os detalhes dos 2 registros da ANVISA (número de registro, nome comercial, forma farmacêutica, indicação aprovada) — a consulta TFDA retornou 2 resultados mas os campos foram devolvidos vazios
- Recuperar dados de MOA do DrugBank — a consulta retornou 1 resultado (`result_status: success`) mas o campo `drugbank_id` e `original_moa` não foram populados; verificar a extração
- Baixar e analisar a bula da ANVISA/TFDA para preencher advertências principais e contraindicações (DG001 – severidade Blocking)
- Consultar banco de dados de interações medicamentosas (DDI) com nome alternativo ou sinônimos, pois a consulta atual retornou `not_found`
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

