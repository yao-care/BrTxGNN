---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 0
---

# Carbidopa
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

# Carbidopa: Dados Insuficientes para Avaliação de Reposicionamento

## Resumo em Uma Frase

Carbidopa (DB00190) é um fármaco já comercializado no mercado brasileiro com 19 registros ativos junto à ANVISA.
O modelo TxGNN **não gerou previsões de reposicionamento** para este candidato no ciclo atual, impossibilitando a análise de novas indicações.
Para que a avaliação possa prosseguir, é necessário resolver as lacunas de dados identificadas — especialmente a extração das bulas registradas e o mecanismo de ação completo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste pacote de evidências |
| Nova Indicação Prevista | Nenhuma previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — (sem previsão gerada) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 19 |
| Decisão Recomendada | Hold |

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pacote de evidências não contém previsões de reposicionamento pelo TxGNN e os dados regulatórios detalhados — indicações aprovadas, advertências e contraindicações das bulas — ainda não foram extraídos dos 19 registros ANVISA. Sem esses insumos, não é possível realizar qualquer avaliação de reposicionamento ou segurança.

**Para prosseguir, é necessário:**
- **DG001 (Bloqueante):** Baixar e processar as bulas dos 19 registros ANVISA para extrair indicações aprovadas, advertências e contraindicações; sem isso, a avaliação de segurança não pode ser iniciada
- **DG002 (Alta prioridade):** Consultar a API do DrugBank (DB00190) para obter o mecanismo de ação completo, necessário para a análise de plausibilidade mecanística
- **Reexecutar o pipeline TxGNN** após resolução das lacunas acima para gerar candidatos de reposicionamento com pontuação e evidências associadas
- **Verificar mapeamento de doenças e integração com o knowledge graph** para garantir que o fármaco esteja corretamente representado no grafo de conhecimento antes de nova rodada de predição
---

