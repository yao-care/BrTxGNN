---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Guaifenesin
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

# Guaifenesin: De expectorante a Doença da Cavidade Nasal

## Resumo em Uma Frase

Guaifenesin é um expectorante/mucolítico amplamente utilizado para o alívio do congestionamento respiratório e a fluidificação das secreções brônquicas.
O modelo TxGNN prevê que pode ser eficaz para **Doença da Cavidade Nasal (Nasal Cavity Disease)**,
atualmente com **1 ensaio clínico** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Expectorante — alívio de congestionamento e fluidificação de secreções das vias respiratórias |
| Nova Indicação Prevista | Doença da Cavidade Nasal (Nasal Cavity Disease) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) disponíveis neste Evidence Pack. Com base no conhecimento farmacológico consolidado, Guaifenesin é um agente mucolítico-expectorante que atua estimulando reflexos vagais gastrointestinais, aumentando o volume de fluido secretado pelas glândulas mucosas das vias respiratórias e reduzindo a viscosidade das secreções — o que facilita o transporte mucociliar e a eliminação do muco.

A doença da cavidade nasal, especialmente a rinite crônica, é caracterizada por hipersecreção e retenção de muco espessado nas vias nasais, com disfunção ciliomucociliar secundária. O mecanismo de Guaifenesin — diluição das secreções e restabelecimento do transporte mucociliar — corresponde diretamente a essa fisiopatologia, conferindo alta plausibilidade biológica à previsão do TxGNN.

Essa lógica é corroborada pelo único ensaio clínico existente, que avaliou especificamente guaifenesin oral em crianças com rinite crônica, e por relatos na literatura de seu uso em pacientes com fibrose cística (sinusite crônica) e em usuários de voz com alergias respiratórias nasais. A extrapolação da indicação original (vias aéreas inferiores) para as vias aéreas superiores é anatomicamente e mecanisticamente coerente.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Concluído | 30 | RCT piloto de guaifenesin oral em crianças (7–18 anos) com rinite crônica; avalia sintomas nasais pelo questionário SN-5, volume das vias aéreas nasais e propriedades biofísicas das secreções; hipótese de que guaifenesin reduz sintomas nasais ao longo de 14 dias |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review/Clinical Guidance | American Journal of Rhinology | Manejo de sinusite crônica em adultos com fibrose cística; guaifenesin incluído no protocolo terapêutico para controle de secreções nasossinusais espessadas em 22 pacientes, dos quais 8 submetidos à cirurgia sinusal |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Tratamento de alergias respiratórias ocultas em usuários de voz; decongestantes combinados com guaifenesin são recomendados como alternativa aos anti-histamínicos para controle de sintomas nasais sem ressecamento vocal |

---

## Informações de Comercialização no Brasil

Guaifenesin possui **20 registros** ativos no Brasil. Os detalhes individuais dos registros (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no conjunto de dados atual. Consulte diretamente a base de dados da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/) para obter as informações completas de cada produto.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um ensaio clínico de Fase 2 concluído que avalia diretamente guaifenesin em rinite crônica (doença da cavidade nasal), com plausibilidade mecanística alta e fármaco já comercializado no Brasil com 20 registros ativos. As evidências são suficientes para avançar com cautela, porém o ensaio é pediátrico e com amostra pequena (n=30), exigindo confirmação adicional.

**Para prosseguir, é necessário:**
- Obter os dados completos de mecanismo de ação (MOA) via DrugBank API — item DG002 (severidade: Alta)
- Levantar advertências, contraindicações e interações medicamentosas na bula ANVISA — item DG001 (severidade: Bloqueante, necessário para avaliação de segurança S1)
- Verificar os 20 registros individuais na ANVISA para confirmar formas farmacêuticas disponíveis e se a indicação nasal já está contemplada em algum produto
- Avaliar compatibilidade de via de administração para a nova indicação (oral vs. intranasal)
- Planejar ensaio clínico de Fase 2 em adultos com rinite crônica, dado que o único ensaio existente é pediátrico e de caráter piloto
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

