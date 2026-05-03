---
layout: default
title: Brigatinibe
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 0
---

# Brigatinibe
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

# BRIGATINIBE: Avaliação Preliminar — Dados Insuficientes para Reposicionamento

## Resumo em Uma Frase

Brigatinibe (BRIGATINIBE) é um inibidor de tirosina quinase ALK, originalmente utilizado no tratamento do câncer de pulmão de células não pequenas (CPCNP) ALK-positivo. Atualmente, **não há indicações previstas pelo modelo TxGNN** para este fármaco, e os dados disponíveis no Evidence Pack apresentam lacunas significativas que impedem uma avaliação completa de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | CPCNP ALK-positivo (informação de referência — campo não preenchido no registro) |
| Nova Indicação Prevista | **Nenhuma previsão disponível** |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | **L5** (sem previsão do modelo nem estudos associados) |
| Situação no Mercado Brasileiro | ✓ Comercializado (已上市) |
| Número de Registros | 1 |
| Decisão Recomendada | **Hold** |

---

## Por que Não Há Previsão Disponível?

Brigatinibe é um inibidor seletivo da quinase ALK (anaplastic lymphoma kinase), pertencente à classe das terapias-alvo de segunda geração para CPCNP. Seu mecanismo de ação envolve a inibição potente de ALK e de várias mutações de resistência, incluindo a mutação G1202R que confere resistência ao crizotinibe.

O modelo TxGNN não gerou previsões de novas indicações para este fármaco. Isso pode estar relacionado a diversos fatores: (1) a ausência do identificador DrugBank (drugbank_id) impede o mapeamento adequado ao grafo de conhecimento; (2) não foram fornecidos dados sobre o mecanismo de ação (MOA) no Evidence Pack, o que limita a análise de conectividade no grafo; (3) o fármaco pode não constar no conjunto de nós do grafo de conhecimento TxGNN (node.csv/kg.csv).

Para que o pipeline de reposicionamento funcione adequadamente, é necessário primeiro resolver o mapeamento DrugBank e confirmar a presença do fármaco no grafo de conhecimento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados a novas indicações registrados no Evidence Pack.

---

## Evidências da Literatura

Atualmente não há literatura relacionada a novas indicações disponível no Evidence Pack.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| (não informado) | (não informado) | (não informado) | (não informado) |

> **Nota:** O registro consta como existente (1 licença ativa, status "已上市"), porém os campos detalhados não foram preenchidos no Evidence Pack. Recomenda-se consultar diretamente a base da ANVISA para obter as informações completas.

---

## Citotoxicidade

Brigatinibe é um fármaco antineoplásico (inibidor de ALK), portanto esta seção é aplicável.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | **Terapia-alvo** (inibidor de tirosina quinase ALK, 2ª geração) |
| Risco de Mielossupressão | Baixo a médio (linfopenia e anemia podem ocorrer; menos frequente que quimioterapia citotóxica convencional) |
| Classificação de Emetogenicidade | Baixa (inibidores de TKI orais geralmente apresentam baixo potencial emetogênico) |
| Itens de Monitoramento | CBC com diferencial, função hepática (ALT/AST), lipase, amilase, função pulmonar (risco de pneumonite), pressão arterial, frequência cardíaca, glicemia |
| Proteção no Manuseio | Seguir precauções padrão para medicamentos antineoplásicos orais conforme regulamentos vigentes |

---

## Considerações de Segurança

> Consulte a bula para informações completas de segurança. Os dados de advertências, contraindicações e interações medicamentosas não foram preenchidos no Evidence Pack atual.

**Informações de referência conhecidas para brigatinibe (a serem confirmadas via bula):**
- **Pneumonite/Doença Pulmonar Intersticial**: Risco de eventos pulmonares graves, especialmente nos primeiros 7 dias de tratamento — motivo pelo qual o esquema posológico inicia com dose escalonada (90 mg → 180 mg)
- **Hipertensão**: Monitoramento regular da pressão arterial recomendado
- **Bradicardia**: Monitoramento cardíaco necessário
- **Distúrbios visuais**: Relatos de alterações visuais em ensaios clínicos
- **Elevação de CPK**: Monitoramento de creatina fosfoquinase recomendado
- **Elevação de enzimas pancreáticas**: Monitoramento de lipase e amilase

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há previsões do modelo TxGNN para novas indicações de brigatinibe, e o Evidence Pack apresenta lacunas críticas (DrugBank ID ausente, MOA não disponível, campos de registro vazios, dados de segurança não preenchidos). Sem esses dados fundamentais, não é possível realizar uma avaliação de reposicionamento.

**Para prosseguir, é necessário:**
- Obter o DrugBank ID de brigatinibe (provável: **DB12267**) e confirmar sua presença no grafo de conhecimento TxGNN
- Preencher os dados do mecanismo de ação (MOA) via consulta ao DrugBank API
- Completar os campos de registro regulatório (número de registro, nome comercial, forma farmacêutica, indicação aprovada)
- Obter e analisar a bula (advertências, contraindicações, interações medicamentosas)
- Re-executar o pipeline TxGNN com o mapeamento DrugBank correto para verificar se há previsões de reposicionamento
- Caso não haja previsões mesmo após mapeamento correto, considerar que o perfil de seletividade de brigatinibe (altamente específico para ALK) pode limitar seu potencial de reposicionamento para indicações não-ALK

---

> ⚠️ **Aviso**: Este relatório é gerado para fins de pesquisa apenas e **não constitui aconselhamento médico**. Candidatos a reposicionamento de fármacos devem ser validados por meio de ensaios clínicos antes de qualquer aplicação clínica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

