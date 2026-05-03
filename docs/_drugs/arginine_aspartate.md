---
layout: default
title: Arginine Aspartate
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 0
---

# Arginine Aspartate
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

# ARGININE ASPARTATE: Avaliação Inconclusiva — Dados Insuficientes para Previsão de Reposicionamento

## Resumo em Uma Frase

ARGININE ASPARTATE é um sal de aminoácido formado pela combinação de L-arginina e ácido aspártico, sem indicações originais registradas no sistema atual.
O modelo TxGNN **não gerou nenhuma previsão** de reposicionamento para este fármaco com os dados disponíveis, provavelmente pela ausência de DrugBank ID mapeado e de registros regulatórios ativos no Brasil.
Não há ensaios clínicos nem publicações vinculados a esta entrada no sistema.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro no sistema |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 — sem previsão disponível |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão Disponível?

ARGININE ASPARTATE é uma combinação de dois aminoácidos — L-arginina e L-aspartato — utilizada clinicamente em outros países como hepatoprotetor, adjuvante em insuficiência hepática e suporte metabólico. No entanto, o sistema não localizou um **DrugBank ID** para este composto, o que impede o modelo TxGNN de posicioná-lo como nó na rede de conhecimento e, consequentemente, de calcular qualquer pontuação de reposicionamento.

Além da ausência de DrugBank ID, o fármaco **não possui registros ativos na ANVISA** (0 licenças encontradas), o que priva o pipeline de dados estruturados sobre indicações aprovadas, vias de administração e mecanismo de ação. Sem esses pontos de ancoragem, o grafo de conhecimento não consegue estabelecer as conexões fármaco–doença necessárias para a previsão.

Por fim, a consulta ao banco de dados de interações medicamentosas (DDI) também retornou sem resultados, e os dados de segurança (advertências e contraindicações) constam como indisponíveis. O único sinal positivo na coleta de dados foi uma consulta bem-sucedida ao DrugBank com 1 resultado, mas sem retorno de ID estruturado — o que sugere que o mapeamento pode estar ao alcance com uma busca manual direcionada.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem DrugBank ID mapeado e sem registros regulatórios no Brasil, o modelo TxGNN não pôde gerar previsões de reposicionamento. A ausência de dados de mecanismo de ação e segurança impede também qualquer avaliação preliminar de risco-benefício.

**Para prosseguir, é necessário:**
- **Mapear o DrugBank ID**: A busca manual no DrugBank por "arginine aspartate" ou "L-arginine L-aspartate" deve identificar o ID correto (ex.: DB09160 ou composto relacionado); registrar e atualizar o campo `drugbank_id`
- **Coletar dados regulatórios internacionais**: Verificar registros em países onde o fármaco está comercializado (ex.: França — Sargenor®, Espanha, Itália) para obter indicações aprovadas e bula estruturada
- **Obter MOA via DrugBank**: Com o ID correto, consultar mecanismo de ação, categorias farmacológicas e perfil de segurança
- **Re-executar o pipeline TxGNN**: Após resolução do DrugBank ID, repetir as etapas de KG prediction e DL prediction para geração de candidatos
- **Verificar dados de segurança**: Baixar bula disponível em outros países e extrair advertências, contraindicações e interações
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

