---
layout: default
title: Betahistine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Betahistine Hydrochloride
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

# Betahistina Cloridrato: Análise de Reposicionamento — Previsões Pendentes por Lacunas de Dados

## Resumo em Uma Frase

Betahistina cloridrato é um análogo da histamina reconhecido internacionalmente, classicamente empregado no tratamento da Doença de Ménière e vertigens vestibulares.
O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco na rodada atual de análise, possivelmente em razão da ausência de DrugBank ID e de indicações originais cadastradas no Evidence Pack.
Sem previsões disponíveis, não é possível avançar para a etapa de avaliação de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (nenhum registro ANVISA encontrado) |
| Nova Indicação Prevista | Nenhuma gerada nesta rodada |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 — Apenas previsão do modelo, sem estudos reais |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsões?

Betahistina cloridrato é amplamente conhecida na literatura internacional como agonista fraco do receptor H1 e antagonista potente do receptor H3 da histamina, com aprovação em mais de 100 países para o tratamento de síndromes vestibulares. Apesar disso, o Evidence Pack atual não contém DrugBank ID, indicações originais estruturadas nem dados de mecanismo de ação (MOA), que são insumos essenciais para que o grafo de conhecimento TxGNN realize o mapeamento de nós e gere candidatos de reposicionamento.

A ausência de registros ativos na ANVISA agrava o problema: sem histórico regulatório brasileiro, o pipeline não consegue ancorar o composto a um perfil farmacológico local verificado. Isso implica que a etapa de mapeamento DrugBank → nó do grafo não pôde ser completada, resultando em lista de previsões vazia.

Para desbloquear a análise, as lacunas DG001 (advertências/contraindicações da bula) e DG002 (MOA e DrugBank ID) precisam ser resolvidas antes de uma nova execução do pipeline.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não produziu previsões de reposicionamento nesta rodada devido a lacunas críticas de dados (DrugBank ID ausente, MOA não disponível, zero registros ANVISA), tornando inviável qualquer avaliação de evidências clínicas ou regulatórias neste momento.

**Para prosseguir, é necessário:**
- Localizar e vincular o DrugBank ID oficial para betahistina (remediar **DG002**) via DrugBank API
- Obter dados de mecanismo de ação (MOA) a partir do DrugBank ou literatura científica (**DG002**)
- Verificar possibilidade de registro ANVISA vigente ou histórico de comercialização no Brasil, incluindo possíveis nomes comerciais alternativos
- Baixar e analisar bula de referência internacional (ex.: EMA, Health Canada) para preencher advertências e contraindicações (**DG001**)
- Re-executar o pipeline TxGNN após a resolução das lacunas acima
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

