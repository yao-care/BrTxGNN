---
layout: default
title: Atomoxetina Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 0
---

# Atomoxetina Hydrochloride
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

# Cloridrato de Atomoxetina: Avaliação de Reposicionamento Pendente

## Resumo em Uma Frase

Cloridrato de Atomoxetina é um inibidor seletivo da recaptação de norepinefrina, amplamente conhecido no tratamento do Transtorno de Déficit de Atenção e Hiperatividade (TDAH) em diversas jurisdições internacionais.
Nesta avaliação, **o modelo TxGNN não gerou previsões de novas indicações**, pois o fármaco não foi localizado nos registros regulatórios brasileiros e o DrugBank ID não pôde ser mapeado automaticamente.
A ausência desses dados estruturais impede a continuidade da análise de reposicionamento neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrada no Brasil |
| Nova Indicação Prevista | Sem previsão disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — sem previsões ou estudos disponíveis no contexto local |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão Disponível?

O modelo TxGNN opera mapeando o identificador **DrugBank ID** do fármaco para os nós do grafo de conhecimento biomédico. Neste caso, o DrugBank ID de "Atomoxetina Cloridrato" **não foi recuperado automaticamente**, o que bloqueou a etapa de geração de candidatos de reposicionamento. Sem esse vínculo, o grafo não consegue propagar predições de novas indicações.

Paralelamente, a consulta à base regulatória brasileira retornou **zero registros**, indicando que o fármaco não possui registro ativo junto à ANVISA sob o nome consultado. Isso restringe a análise de indicações aprovadas localmente e limita a validação cruzada com dados regulatórios.

Vale ressaltar que a atomoxetina é aprovada em diversas jurisdições internacionais (EUA, Europa, outros) para o TDAH. A ausência de registro no Brasil pode refletir uma lacuna regulatória local — e não uma limitação intrínseca do composto — o que torna este caso candidato a uma reavaliação após complementação dos dados.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A falha no mapeamento automático do DrugBank ID e a ausência de registros regulatórios brasileiros impediram a geração de previsões pelo TxGNN. Sem previsões de reposicionamento, não há base estruturada para avançar na avaliação de novas indicações.

**Para prosseguir, é necessário:**
- Localizar manualmente o DrugBank ID correto para Atomoxetina Cloridrato em [drugbank.com](https://www.drugbank.ca/) e reprocessar o Evidence Pack
- Verificar se o fármaco possui registro na ANVISA sob nome alternativo (ex.: "Atomoxetina", "Atomoxetine" ou nome comercial como "Strattera")
- Baixar a bula ANVISA ou, na ausência, a bula FDA/EMA para extrair MOA, advertências e contraindicações
- Após correção do mapeamento, reexecutar o pipeline TxGNN para gerar candidatos de reposicionamento e nova análise de evidências
---

