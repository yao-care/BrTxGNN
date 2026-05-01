---
layout: default
title: Avibactam Sodium
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Avibactam Sodium
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

# Avibactam Sódico: Avaliação de Reposicionamento — Predições Indisponíveis

## Resumo em Uma Frase

Avibactam sódico é um inibidor de beta-lactamase não-beta-lactâmico, utilizado em combinação com ceftazidima para tratar infecções bacterianas por gram-negativos multirresistentes.
O modelo TxGNN **não gerou predições de reposicionamento** para este fármaco nesta rodada de análise, impossibilitando a identificação de novas indicações candidatas.
O fármaco **não possui registros** no Brasil, e os dados essenciais de segurança e mecanismo de ação precisam ser complementados antes de qualquer avaliação adicional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas por gram-negativos multirresistentes (em combinação com ceftazidima) |
| Nova Indicação Prevista | Nenhuma predição disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — sem predições geradas pelo modelo |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Predições Disponíveis?

Avibactam sódico é um inibidor de beta-lactamase de nova geração, ativo contra enzimas das classes A, C e parte da classe D (incluindo KPC e OXA-48). É utilizado exclusivamente em combinação com ceftazidima — o produto combinado (ceftazidima/avibactam) restaura a atividade antibacteriana frente a organismos como *Klebsiella pneumoniae* produtora de carbapenemase e *Pseudomonas aeruginosa* resistente. Avibactam sódico, por si só, não possui atividade antibacteriana intrínseca.

Nesta rodada de análise, o pipeline TxGNN não produziu candidatos de reposicionamento para este fármaco. As causas mais prováveis são: (1) ausência de DrugBank ID confirmado para o composto — impede o mapeamento correto no grafo de conhecimento; (2) presença no Knowledge Graph como componente de combinação, e não como entidade independente; ou (3) relações insuficientes no KG para gerar escores com significância estatística.

A consulta ao DrugBank retornou 1 resultado no log de rastreamento, indicando que o composto existe na base, mas o ID não foi capturado no Evidence Pack. Confirmar esse ID e re-executar o mapeamento é o passo mais crítico para desbloquear as predições.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma predição de reposicionamento para avibactam sódico, e os dados regulatórios, de segurança e mecanismo de ação estão ausentes ou incompletos. Sem esses elementos, não há base técnica suficiente para avançar na avaliação.

**Para prosseguir, é necessário:**
- **[Bloqueante]** Confirmar o DrugBank ID de avibactam sódico a partir do resultado já retornado pela consulta ao DrugBank, e re-executar o mapeamento no pipeline TxGNN
- **[Alta prioridade]** Obter a bula/monografia do produto (ex.: Avycaz, registrado na FDA e EMA) para preencher MOA, advertências e contraindicações
- Re-executar o pipeline TxGNN completo após correção do mapeamento de identidade do fármaco
- Avaliar se o reposicionamento deve ser analisado para avibactam sódico como entidade isolada ou para a combinação ceftazidima/avibactam como um único agente terapêutico
---

