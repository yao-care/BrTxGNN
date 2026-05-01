---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: De antibiótico de amplo espectro para hiperamylasemia (Hyperamylasemia)

## Resumo em Uma Frase

Azithromycin é um antibiótico macrolídeo de amplo espectro, classicamente utilizado no tratamento de infecções bacterianas como pneumonia adquirida na comunidade, infecções de vias aéreas superiores e infecções sexualmente transmissíveis.
O modelo TxGNN prevê que pode ser eficaz para **Hiperamylasemia (Hyperamylasemia)**, com pontuação de previsão de **99,81%**;
entretanto, atualmente **não há ensaios clínicos nem publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (antibiótico macrolídeo de amplo espectro) |
| Nova Indicação Prevista | Hiperamylasemia (Hyperamylasemia) |
| Pontuação de Previsão TxGNN | 99,81% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Sem registros na base consultada |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base no conhecimento farmacológico estabelecido, Azithromycin é um antibiótico macrolídeo que atua por dois mecanismos principais: inibição da síntese proteica bacteriana por ligação à subunidade 50S do ribossomo 70S, e propriedades imunomoduladoras independentes do efeito antibacteriano (inibição da quimiotaxia de neutrófilos, redução da secreção de IL-8 e modulação de citocinas pró-inflamatórias).

A hiperamylasemia — elevação dos níveis séricos de amilase — decorre principalmente de lesão pancreática (pancreatite) ou das glândulas salivares, com fisiopatologia centrada em dano acinar, obstrução ductal ou causas metabólicas. Não existe conexão mecanística direta conhecida entre os alvos farmacológicos dos macrolídeos (inibição ribossômica bacteriana / imunomodulação) e a regulação dos níveis de amilase sérica.

A elevada pontuação do TxGNN (99,81%, rank 1.557 entre todos os candidatos) provavelmente reflete um efeito de proximidade no grafo de conhecimento — nós relacionados a doenças sanguíneas na vizinhança topológica do grafo — e não uma relação farmacológica direta. Na ausência de qualquer ensaio clínico ou publicação de suporte, esta previsão deve ser interpretada exclusivamente como sinal computacional de hipótese, não como evidência de eficácia clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Nenhum registro encontrado na base de dados consultada na data de corte (2026-04-05).

> **Nota:** Azithromycin é um antibiótico de uso amplamente difundido em todo o mundo, incluindo o Brasil. A ausência de registros pode refletir limitações da base de dados consultada. Recomenda-se verificação direta no banco de dados da ANVISA (Consulta de Medicamentos Registrados) antes de qualquer decisão regulatória.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há qualquer evidência clínica ou pré-clínica direta vinculando Azithromycin ao tratamento de hiperamylasemia, e a previsão TxGNN de nível L5 é sustentada exclusivamente pelo modelo computacional, sem fundamento biológico estabelecido que justifique avanço investigativo nesta indicação.

**Para prosseguir, é necessário:**
- Identificar base biológica plausível que conecte os mecanismos de ação dos macrolídeos à regulação da amilase sérica
- Realizar verificação cruzada com dados de farmacovigilância para identificar se há sinal de alteração de amilase como efeito adverso ou protetor do Azithromycin
- Obter dados de mecanismo de ação detalhados via DrugBank API (DG002 pendente)
- Consultar diretamente o banco de dados da ANVISA para confirmar situação regulatória no Brasil
- Caso surja hipótese mecanística plausível, conduzir estudos pré-clínicos antes de qualquer ensaio clínico
---

