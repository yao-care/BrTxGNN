---
layout: default
title: Oxybutynin Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 0
---

# Oxybutynin Hydrochloride
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

# Oxibutinina Cloridrato: Da Bexiga Hiperativa a Nova Indicação – Previsões TxGNN Indisponíveis

## Resumo em Uma Frase

Oxibutinina (Oxybutynin Hydrochloride) é um fármaco anticolinérgico/antimuscarínico amplamente utilizado no tratamento da bexiga hiperativa, incontinência urinária de urgência e espasmos vesicais. O Evidence Pack atual **não contém previsões de reposicionamento pelo modelo TxGNN**, impossibilitando a identificação de novas indicações candidatas. Adicionalmente, o fármaco **não possui registro comercial no Brasil** e dados críticos de mecanismo de ação e segurança estão ausentes no pacote recebido.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Bexiga hiperativa / Incontinência urinária *(dado externo – não constante no pacote)* |
| Nova Indicação Prevista | Não disponível (ausência de previsões TxGNN) |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 – Sem previsões de modelo disponíveis |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Conforme registros da literatura médica geral, a oxibutinina é um antagonista não seletivo dos receptores muscarínicos (subtipos M1, M2 e M3), com ação direta no músculo liso detrusor da bexiga urinária. Ao bloquear esses receptores, o fármaco reduz as contrações involuntárias do detrusor, aliviando urgência, frequência e incontinência urinárias. A molécula também apresenta efeito espasmolítico direto e fraca ação anestésica local.

A previsão de reposicionamento pelo TxGNN ainda não foi gerada para este fármaco. O log de consultas indica que o DrugBank retornou **1 resultado** para este fármaco (consulta em 2026-03-26), mas os dados de MOA estruturado não foram incorporados ao pacote. Sem as previsões TxGNN, não é possível avaliar a relação mecanística com potenciais novas indicações.

> **Atenção:** Para avançar para a análise de reposicionamento, é necessário primeiro executar o pipeline TxGNN com o DrugBank ID correto e reprocessar este Evidence Pack.

---

## Informações de Comercialização no Brasil

O fármaco **não possui nenhum registro ativo junto à ANVISA** conforme os dados consultados em 2026-03-26. Nenhuma licença comercial foi identificada para Oxybutynin Hydrochloride no mercado brasileiro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN, indicações originais estruturadas nem informações de segurança verificáveis, tornando inviável qualquer avaliação de reposicionamento neste momento. A ausência de registro no Brasil também representa uma barreira regulatória adicional caso uma indicação candidata venha a ser identificada.

**Para prosseguir, é necessário:**
- **[Prioritário]** Identificar o DrugBank ID correto para Oxybutynin Hydrochloride e reexecutar o pipeline TxGNN para gerar previsões de reposicionamento
- **[Prioritário]** Completar a extração de dados do DrugBank (1 resultado identificado no log, porém MOA ausente no pacote)
- Obter bula e informações de segurança completas (advertências, contraindicações) via ANVISA ou FDA/EMA
- Confirmar as indicações originais aprovadas internacionalmente e registrá-las no campo `original_indications`
- Avaliar viabilidade de registro no Brasil caso uma candidatura de reposicionamento seja identificada
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

