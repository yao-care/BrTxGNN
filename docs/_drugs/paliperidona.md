---
layout: default
title: Paliperidona
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 0
---

# Paliperidona
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

# Paliperidona: Avaliação Incompleta — Dados Insuficientes para Gerar Previsão de Reposicionamento

## Resumo em Uma Frase

Paliperidona (PALIPERIDONA) é um antipsicótico atípico registrado no Brasil com 4 licenças ativas na ANVISA.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de dados, impedindo a análise de novas indicações.
Os dados de suporte — mecanismo de ação, detalhes dos registros e informações de segurança — estão todos ausentes neste pacote de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos registros do pacote atual |
| Nova Indicação Prevista | Nenhuma previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão de modelo nem estudos associados) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Informações de Comercialização no Brasil

Os registros ANVISA foram identificados (4 licenças ativas), porém os campos de detalhe — número de registro, nome comercial, forma farmacêutica e indicação aprovada — estão todos em branco no pacote de evidências recebido.

| Situação | Detalhe |
|------|------|
| Total de Registros ANVISA | 4 |
| Detalhes dos Produtos | Não disponíveis — requer complementação |

> Para completar esta seção, é necessário re-executar a consulta TFDA/ANVISA com retorno dos campos de produto.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O TxGNN não produziu previsões válidas para Paliperidona neste ciclo (campo `predicted_indications` vazio), e os dados regulatórios e de segurança estão incompletos, tornando inviável qualquer análise de reposicionamento no momento.

**Para prosseguir, é necessário:**
- **Verificar o mapeamento DrugBank**: o log indica que a consulta ao DrugBank retornou 1 resultado — confirmar se o `drugbank_id` foi corretamente capturado e alimentado ao TxGNN para gerar previsões
- **Completar os detalhes dos 4 registros ANVISA**: nome comercial, forma farmacêutica e indicação aprovada de cada licença
- **Obter o MOA via DrugBank API**: o `drugbank_id` recuperado deve permitir extrair mecanismo de ação e categorias farmacológicas
- **Baixar e analisar a bula ANVISA**: necessário para preencher advertências principais e contraindicações (bloqueador DG001)
- **Re-executar o pipeline TxGNN** após correção do mapeamento para obter previsões de indicações candidatas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

