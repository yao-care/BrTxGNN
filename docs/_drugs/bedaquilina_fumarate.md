---
layout: default
title: Bedaquilina Fumarate
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 0
---

# Bedaquilina Fumarate
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

# Bedaquilina Fumarato: Avaliação de Candidato — Previsão de Reposicionamento Indisponível

## Resumo

Bedaquilina fumarato é um antibiótico diarylquinoline utilizado no tratamento da tuberculose resistente a múltiplos fármacos (MDR-TB). O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco nesta execução — provavelmente devido à ausência de mapeamento ao DrugBank ID e à falta de registros na base regulatória consultada. Esta avaliação é, portanto, **inconclusiva** e requer coleta de dados complementares antes de qualquer análise de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Tuberculose resistente a múltiplos fármacos (MDR-TB) |
| Nova Indicação Prevista | Não disponível — sem previsões geradas nesta execução |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 (ausência de dados de previsão) |
| Situação no Mercado Brasileiro | Não comercializado (ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que as Previsões Não Foram Geradas?

A ausência de previsões de reposicionamento nesta execução tem três causas prováveis, identificadas no log de consultas:

**1. Falha no mapeamento ao DrugBank**
A busca pelo nome "BEDAQUILINA FUMARATE" (grafia em português/espanhol) pode não ter encontrado correspondência ao identificador canônico no DrugBank. Sem um `drugbank_id` válido, o modelo TxGNN não consegue posicionar o fármaco no grafo de conhecimento para gerar predições.

**2. Ausência de registro regulatório**
O fármaco não possui registros ativos na base regulatória consultada (total de registros: 0). Isso reduz a cobertura de dados de indicações aprovadas, que alimenta parte do pipeline de predição.

**3. Lacunas críticas de dados**
O mecanismo de ação (MOA) não foi recuperado nesta execução. Embora o log indique que a consulta ao DrugBank retornou 1 resultado, os dados não foram populados no Evidence Pack, configurando uma lacuna de dados de severidade "High" que afeta diretamente a análise de relacionamento mecanístico.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não produziu previsões de reposicionamento por falhas de mapeamento e lacunas de dados que precisam ser resolvidas antes de qualquer análise ser possível. Não há base de evidências suficiente para avaliar nenhuma nova indicação neste momento.

**Para prosseguir, é necessário:**
- Remapear o fármaco usando o nome INN canônico em inglês (`bedaquiline`) e verificar o DrugBank ID correspondente
- Recuperar o mecanismo de ação (MOA) via DrugBank API com o ID correto
- Verificar o status de disponibilização no Brasil via canais de saúde pública (SUS/RENAME), que pode diferir do registro comercial ANVISA
- Obter as advertências, contraindicações e interações medicamentosas da bula oficial (TFDA/ANVISA/EMA)
- Re-executar o pipeline TxGNN com o mapeamento corrigido para gerar predições válidas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

