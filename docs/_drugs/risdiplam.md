---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Risdiplam
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

Using `txgnn-pipeline` to confirm report generation context — confirmed, this is the BrTxGNN pipeline. Proceeding to generate the pharmacist evaluation report based on the Evidence Pack.

---

# Risdiplam: Da Atrofia Muscular Espinhal à Acne

## Resumo em Uma Frase

Risdiplam é um modificador de splicing do gene SMN2, aprovado para o tratamento da Atrofia Muscular Espinhal (AME) em todas as faixas etárias.
O modelo TxGNN prevê que pode ser eficaz para **Acne (acne (disease))**, porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.
A análise mecanística disponível indica ausência de plausibilidade biológica para esta previsão, sugerindo que o resultado reflete um artefato do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Atrofia Muscular Espinhal (AME) |
| Nova Indicação Prevista | Acne (acne (disease)) |
| Pontuação de Previsão TxGNN | 99.45% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Risdiplam é um modificador de splicing de RNA pequeno molecular, pertencente a uma nova classe terapêutica de modificadores de splicing do pré-mRNA. Seu mecanismo de ação consiste em estabilizar a inclusão do éxon 7 durante a transcrição do gene SMN2, aumentando a produção de proteína SMN (Survival Motor Neuron) funcional — essencial para a sobrevivência dos neurônios motores. Dados detalhados do mecanismo de ação não constam no pacote de evidências atual (lacuna DG002), mas o contexto molecular é derivado das análises de plausibilidade incluídas.

A acne é uma doença inflamatória crônica da unidade pilossebácea, mediada por colonização de *Cutibacterium acnes*, hiperprodução de sebo e resposta imune inata com participação das vias IL-1β e TNF-α. Esses processos não têm relação fisiopatológica conhecida com a via de splicing do SMN2. A Atrofia Muscular Espinhal e a acne não compartilham alvos moleculares, vias de sinalização nem mecanismos de patogênese que justifiquem a extrapolação terapêutica.

De acordo com a análise mecanística embutida no pacote de evidências, **não existe suporte bibliográfico para uma conexão entre a via SMN2 e a patologia da acne**. A pontuação elevada atribuída pelo TxGNN (99,45%) provavelmente decorre de uma associação artificial entre nós de "pele" no grafo de conhecimento, e não de uma conexão biológica genuína. Esta previsão deve ser interpretada com cautela e não justifica investigação clínica no estágio atual.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Consta 1 registro ativo no sistema regulatório brasileiro. Os dados detalhados (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não foram capturados nesta extração. Consulte o portal da ANVISA para informações completas sobre o registro vigente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Esta previsão apresenta nível de evidência L5 (exclusivamente predição do modelo, sem qualquer estudo real publicado) e ausência demonstrada de plausibilidade mecanística — a via de modificação de splicing do SMN2 não tem relação conhecida com a patogênese da acne. A alta pontuação TxGNN reflete, com elevada probabilidade, um artefato de agrupamento de nós de pele no grafo de conhecimento, e não uma conexão terapêutica genuína.

**Para prosseguir, seria necessário:**
- Resolução da lacuna DG001: baixar a bula ANVISA em PDF e extrair advertências, contraindicações e dados de segurança
- Resolução da lacuna DG002: consultar a API do DrugBank para dados completos de MOA e categorias farmacológicas
- Evidências pré-clínicas em modelos de acne (nível mínimo L4) para elevar o estágio de avaliação
- Reavaliação da plausibilidade mecanística por especialista em dermatologia antes de qualquer estudo exploratório
- Dados detalhados do registro ANVISA (número de registro, indicação aprovada, forma farmacêutica)
---

