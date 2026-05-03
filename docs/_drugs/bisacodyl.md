---
layout: default
title: Bisacodyl
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 0
---

# Bisacodyl
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

# Bisacodyl: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo

Bisacodyl (DB09020) é um fármaco identificado na base DrugBank, porém o Evidence Pack gerado em 05/04/2026 **não contém previsões de reposicionamento pelo modelo TxGNN**, tampouco dados de indicações originais ou mecanismo de ação. O fármaco não possui registros ativos na base regulatória consultada (equivalente à ANVISA), e todos os dados de segurança apresentam lacunas críticas. Nessas condições, não é possível avançar para análise de reposicionamento sem complementar as informações faltantes.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 (apenas identificação no DrugBank, sem previsões) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Informações de Comercialização no Brasil

Não há registros de Bisacodyl na base regulatória consultada. A consulta realizada em 26/03/2026 retornou zero resultados, confirmando que o fármaco **não está comercializado no Brasil** segundo os dados disponíveis.

> Se houver suspeita de registro sob nome comercial diferente ou como associação, recomenda-se consulta direta à base de dados da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não gerou previsões de reposicionamento para Bisacodyl — o que pode decorrer da ausência de registro regulatório nacional (pré-requisito para execução do fluxo completo) e de lacunas de dados críticas identificadas no Evidence Pack. Sem indicação original, mecanismo de ação e perfil de segurança, não é possível realizar avaliação de reposicionamento.

**Para prosseguir, é necessário:**

- **\[DG001 — Bloqueante\]** Obter advertências principais e contraindicações da bula oficial via ANVISA/TFDA (download do PDF da monografia e extração dos campos de segurança)
- **\[DG002 — Alta prioridade\]** Complementar dados de mecanismo de ação (MOA) via consulta à DrugBank API (o DrugBank foi consultado com sucesso e retornou 1 resultado — os dados precisam ser integrados ao Evidence Pack)
- Verificar se Bisacodyl está registrado na ANVISA sob outro nome comercial ou como componente de associação
- Após sanear DG001 e DG002, re-executar o pipeline TxGNN para geração de previsões de reposicionamento
- Confirmar interações medicamentosas relevantes (consulta DDI retornou `not_found`)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

