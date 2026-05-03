---
layout: default
title: Promethazine
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Promethazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using `txgnn-pipeline` para orientar a geração do relatório de reposicionamento farmacêutico.

Analisando o Evidence Pack de Promethazine (DB01069) e gerando o relatório conforme o formato v5:

---

# Promethazine: De anti-histamínico clássico a conjuntivite rosácea

## Resumo em Uma Frase

Promethazine é um anti-histamínico de primeira geração da classe fenotiazina, com uso histórico no tratamento de reações alérgicas, náuseas/vômitos e sedação pré-operatória.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Rosácea (Rosacea Conjunctivitis)**,
atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Reações alérgicas, náuseas/vômitos, sedação (uso histórico; sem registro no Brasil) |
| Nova Indicação Prevista | Conjuntivite Rosácea (Rosacea Conjunctivitis) |
| Pontuação de Previsão TxGNN | 98.94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Promethazine é um anti-histamínico de primeira geração pertencente à classe das fenotiazinas. Atua como antagonista competitivo dos receptores H1 de histamina, bloqueando o aumento da permeabilidade vascular e a contração da musculatura lisa induzidos pela histamina. Adicionalmente, possui propriedades anticolinérgicas, antidopaminérgicas e sedativas centrais — o que explica seu amplo histórico de uso em alergias, cinetose, náuseas e como pré-medicação anestésica.

A conjuntivite rosácea é uma manifestação ocular da rosácea, condição cuja fisiopatologia central envolve disfunção neurovascular e comprometimento da barreira cutânea/ocular. Embora haja um componente inflamatório secundário, a histamina não é o mediador principal desta patologia — diferindo substancialmente das conjuntivites alérgicas onde o bloqueio H1 tem eficácia comprovada. A sobreposição mecanística entre Promethazine e conjuntivite rosácea é, portanto, considerada fraca.

Segundo a análise de mecanismo do Evidence Pack, a previsão do TxGNN provavelmente reflete proximidade topológica entre nós de doenças oculares e alérgicas no grafo de conhecimento (co-ocorrência de features), e não uma ligação farmacológica direta. A ausência total de ensaios clínicos e publicações sobre este par fármaco-doença reforça a necessidade de cautela antes de qualquer investimento de desenvolvimento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Promethazine não possui registro ativo na ANVISA. A consulta à base regulatória brasileira não retornou nenhum produto contendo esta substância ativa. O fármaco não está oficialmente comercializado no mercado nacional.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe nenhum ensaio clínico nem publicação que apoie o uso de Promethazine em conjuntivite rosácea. A previsão do TxGNN (98,94%) parece derivar de similaridade topológica no grafo de conhecimento entre doenças oculares/alérgicas, sem respaldo farmacológico direto — a histamina não é o mediador central da rosácea.

**Para prosseguir, é necessário:**
- Levantamento bibliográfico especializado sobre o papel de anti-histamínicos H1 na rosácea ocular
- Obtenção dos dados de mecanismo de ação (MOA) completos via DrugBank API (DG002)
- Extração das advertências e contraindicações da bula oficial via ANVISA (DG001) antes de qualquer avaliação de segurança
- Regularização do status regulatório: registro na ANVISA seria pré-requisito para qualquer estudo clínico conduzido no Brasil
- Considerar redirecionar esforços para as indicações de rank 2 (Urticária Alérgica, L3) e rank 4 (Rinite, L3), que apresentam evidências reais e recomendação "Proceed with Guardrails"
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

