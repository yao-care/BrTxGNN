---
layout: default
title: Alcaftadina
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 0
---

# Alcaftadina
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

# Alcaftadina: Avaliação Preliminar — Previsão TxGNN Indisponível

## Resumo em Uma Frase

Alcaftadina é um anti-histamínico oftálmico antagonista H1, indicado para a prevenção do prurido ocular associado à conjuntivite alérgica. O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual, em razão de lacunas críticas nos dados de entrada — principalmente a ausência de DrugBank ID e de mecanismo de ação (MOA). Com **1 registro ativo** na ANVISA e zero candidatos computacionais, a avaliação de novas indicações não pode ser conduzida neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Conjuntivite alérgica (uso oftálmico tópico) |
| Nova Indicação Prevista | — Sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | — |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão Disponível?

O modelo TxGNN não produziu candidatos de reposicionamento para alcaftadina neste ciclo. As causas identificadas são:

**1. DrugBank ID ausente**
O grafo de conhecimento do TxGNN utiliza o DrugBank ID como chave primária para localizar o fármaco na rede de interações. Sem esse identificador, o fármaco não pôde ser mapeado e o pipeline de predição não foi executado.

**2. Mecanismo de ação indisponível (Data Gap DG002 — Severidade Alta)**
A ausência do MOA impede a inferência por similaridade mecanística entre indicações, que é um dos principais sinais utilizados pelo modelo para sugerir reposicionamentos biologicamente plausíveis.

**3. Detalhes do registro ANVISA não recuperados**
Embora haja confirmação de 1 registro ativo, os campos de número de registro, nome comercial, forma farmacêutica e indicação aprovada retornaram vazios. Isso impossibilita a validação da indicação original e a análise de sobreposição com novas indicações candidatas.

Do ponto de vista farmacológico geral, alcaftadina é um antagonista seletivo do receptor H1 de histamina, formulado exclusivamente como colírio de uso tópico ocular. Fármacos com absorção sistêmica mínima possuem escopo de reposicionamento naturalmente restrito, o que torna ainda mais importante a obtenção de dados farmacocinéticos e do MOA completo antes de avançar na análise.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As lacunas críticas nos dados de entrada impediram a execução do pipeline TxGNN. Sem previsões computacionais e sem os dados regulatórios completos, não há base suficiente para conduzir uma avaliação de reposicionamento neste ciclo.

**Para prosseguir, é necessário:**
- Identificar e confirmar o **DrugBank ID** de alcaftadina (busca manual ou via API DrugBank) para habilitar o mapeamento no grafo de conhecimento
- Baixar e processar a **bula ANVISA** para extrair indicação aprovada, advertências e contraindicações (**Data Gap DG001 — Bloqueante**)
- Complementar os campos do registro ANVISA: número de registro, nome comercial, forma farmacêutica e fabricante
- Re-executar o **pipeline TxGNN** com o DrugBank ID correto para gerar candidatos de reposicionamento
- Verificar se existem dados de **biodisponibilidade sistêmica** — fundamentais dado o perfil de uso tópico do fármaco
---

