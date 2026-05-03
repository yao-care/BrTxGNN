---
layout: default
title: Azithromycin Dihydrate
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 0
---

# Azithromycin Dihydrate
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

# Azithromycin Dihydrate: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Azithromycin Dihydrate é a forma di-hidratada da azitromicina, um antibiótico macrolídeo de amplo espectro amplamente utilizado no tratamento de infecções bacterianas do trato respiratório, pele e tecidos moles.
O modelo TxGNN **não gerou previsões de reposicionamento** para este composto nesta execução do pipeline, possivelmente por ausência de DrugBank ID e falha na correspondência dos registros regulatórios.
Sem candidatos de reposicionamento disponíveis, esta avaliação não pode ser concluída com os dados atuais.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (antibiótico macrolídeo) |
| Nova Indicação Prevista | Não disponível nesta consulta |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão do modelo) |
| Situação no Mercado Brasileiro | Não encontrado com este nome exato (0 registros) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão Não Pôde Ser Gerada?

A azitromicina é um antibiótico da classe dos macrolídeos que atua inibindo a síntese proteica bacteriana ao se ligar reversivamente à subunidade ribossômica 50S, bloqueando a translocação peptídica. Possui amplo espectro de ação contra patógenos gram-positivos, gram-negativos atípicos e alguns anaeróbios, com meia-vida tecidual longa que permite esquemas de dose única ou curta duração.

A consulta ao banco de dados regulatório brasileiro foi realizada com o nome exato **"AZITHROMYCIN DIHYDRATE"** e retornou **0 registros**, o que não reflete a realidade do mercado. Medicamentos com azitromicina são amplamente comercializados no Brasil, porém tipicamente registrados sob as grafias **"AZITROMICINA"** (português) ou **"AZITROMICINA DI-HIDRATADA"** — variações que não foram contempladas nesta consulta. Esta é uma limitação de normalização de nomes, não ausência real do produto no mercado.

O segundo problema crítico é a ausência de **DrugBank ID**, que é o identificador central para execução do modelo TxGNN. Sem esse vínculo, o pipeline não consegue localizar o nó correspondente no grafo de conhecimento e, portanto, não é capaz de calcular scores de reposicionamento. O DrugBank ID correto para azitromicina é **DB00207**.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há previsões de reposicionamento disponíveis para este composto nesta execução. As duas lacunas de dados identificadas — DrugBank ID ausente e falha na correspondência do nome no banco regulatório — bloqueiam todas as etapas subsequentes da análise.

**Para prosseguir, é necessário:**
- Vincular o DrugBank ID correto: **DB00207** (azitromicina)
- Re-executar a consulta ANVISA com o nome normalizado **"AZITROMICINA"** (em português, sem especificação do sal)
- Após identificação dos registros ANVISA, extrair dados de MOA e advertências da bula para preencher as lacunas de segurança
- Re-executar o modelo TxGNN com o DrugBank ID correto para gerar candidatos de reposicionamento e seus scores
- Repetir coleta de evidências (ensaios clínicos, literatura) após definição da nova indicação prevista
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

