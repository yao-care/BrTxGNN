---
layout: default
title: Ampicillin Anhydrous
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 0
---

# Ampicillin Anhydrous
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

# Ampicillin Anhydrous: Sem Previsão de Reposicionamento Disponível

## Resumo em Uma Frase

Ampicillin Anhydrous é a forma anidra da ampicilina, antibiótico de amplo espectro da classe das aminopenicilinas (β-lactâmicos), classicamente utilizado no tratamento de infecções bacterianas.
O modelo TxGNN **não gerou previsões de reposicionamento** para este composto no ciclo de dados atual,
pois o DrugBank ID não foi mapeado, impedindo a execução do algoritmo de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (aminopenicilina, classe β-lactâmica) |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 – Sem previsão disponível |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Houve Previsão?

Ampicillin Anhydrous é a forma anidra da ampicilina, antibiótico de amplo espectro da família das aminopenicilinas. Atua inibindo as PBPs (Proteínas Ligantes de Penicilina), enzimas essenciais à síntese da parede celular bacteriana, levando à lise e morte do microrganismo. Essa classe é ativa contra uma ampla gama de bactérias Gram-positivas e Gram-negativas.

A ausência de previsões TxGNN não indica que o composto seja inadequado para reposicionamento, mas sim que o pipeline não dispôs de informações mínimas para processá-lo. Dois problemas foram identificados:

1. **DrugBank ID não mapeado**: Sem a vinculação a um nó da rede de conhecimento do TxGNN, o algoritmo de reposicionamento não é executado. O DrugBank ID provável para ampicilina base é **DB00415**; é necessário validar esse mapeamento e reprocessar o pipeline.
2. **Sem registros ANVISA para esta denominação**: Nenhuma licença ativa foi encontrada para "AMPICILLIN ANHYDROUS" no Brasil. A ampicilina pode estar registrada sob denominação distinta (e.g., ampicilina tri-hidratada), o que demanda verificação cruzada antes de concluir ausência de mercado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem previsão gerada pelo TxGNN e sem registros ANVISA confirmados para esta denominação específica, não existem evidências suficientes para conduzir uma avaliação de reposicionamento no ciclo atual. Trata-se de uma lacuna de dados no pipeline, não de uma contraindicação ao composto.

**Para prosseguir, é necessário:**
- Validar e mapear o DrugBank ID correto (candidato: **DB00415** – ampicillin) e reprocessar o pipeline TxGNN
- Verificar se ampicilina em outras formas farmacêuticas ou denominações possui registros ANVISA ativos que abranjam esta forma anidra
- Obter dados completos de MOA via DrugBank API (lacuna DG002 — prioridade Alta)
- Baixar e analisar a bula na ANVISA para advertências e contraindicações (lacuna DG001 — prioridade Bloqueante)
- Após resolução das lacunas, reexecutar o Evidence Pack e gerar novo relatório de avaliação
---

