---
layout: default
title: Teriflunomida
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 0
---

# Teriflunomida
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

# Teriflunomida: De Esclerose Múltipla — Avaliação de Reposicionamento Incompleta

## Resumo

Teriflunomida é um agente imunomodulador oral aprovado para o tratamento de formas recidivantes da esclerose múltipla (EM), atuando como inibidor da enzima dihidroorotato desidrogenase (DHODH). O presente Evidence Pack não contém predições TxGNN processadas para este fármaco, impossibilitando a análise de reposicionamento neste momento. Com 11 registros ativos no Brasil, há base regulatória estabelecida, mas os dados do pacote estão incompletos para suportar uma avaliação de nova indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Esclerose Múltipla recidivante (com base no INN e conhecimento farmacológico consolidado) |
| Nova Indicação Prevista | — Não disponível neste Evidence Pack |
| Pontuação de Previsão TxGNN | — Não disponível |
| Nível de Evidência | L5 (ausência de predição processada) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 11 |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

O Evidence Pack confirma **11 registros ativos** de Teriflunomida no Brasil e status de comercialização ativo. Entretanto, os campos de detalhamento dos registros (número, nome comercial, forma farmacêutica e texto de indicação aprovada) retornaram vazios na extração atual.

> Os dados de registro precisam ser complementados por consulta direta ao sistema DATAVISA/ANVISA para listar os produtos individualmente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém predições TxGNN processadas (`predicted_indications` vazio), o que impossibilita a identificação de candidatos de reposicionamento. Adicionalmente, os dados de registro no Brasil e as informações de segurança não foram carregados com sucesso, bloqueando a avaliação regulatória e de risco.

**Para prosseguir, é necessário:**
- **[Crítico]** Executar o pipeline TxGNN com o identificador DrugBank correto de Teriflunomida (DB08880) para gerar as predições de reposicionamento
- **[Crítico]** Reprocessar os dados ANVISA/TFDA para preencher os campos de registro (número, nome comercial, indicação aprovada)
- **[Alto]** Recuperar o MOA completo via DrugBank API (Teriflunomida: inibidor de DHODH) para permitir análise de relacionamento mecanístico
- **[Alto]** Baixar e analisar a bula aprovada pela ANVISA para extrair advertências, contraindicações e interações medicamentosas
- Após a obtenção das predições, reavaliar o Evidence Pack completo seguindo o fluxo padrão L1–L5
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

