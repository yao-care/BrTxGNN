---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill as context, agora vou gerar o relatório a partir do Evidence Pack fornecido.

---

# Pregabalin: Da Dor Neuropática à Tendinite

## Resumo em Uma Frase

Pregabalin é um gabapentinoide aprovado para o tratamento da dor neuropática, epilepsia parcial em adultos e transtorno de ansiedade generalizada.
O modelo TxGNN prevê que pode ser eficaz para **Tendinite (Tendinitis)**, atualmente com **0 ensaios clínicos diretos** e **6 publicações** identificadas — a maioria referente à analgesia perioperatória em cirurgia do manguito rotador, não ao tratamento da tendinite propriamente dita.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dor neuropática / Epilepsia parcial / Transtorno de ansiedade generalizada |
| Nova Indicação Prevista | Tendinite (Tendinitis) |
| Pontuação de Previsão TxGNN | 99,71% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Pregabalin é um ligante seletivo da subunidade α2-δ dos canais de cálcio voltagem-dependentes. Ao ocupar esse sítio, reduz o influxo de cálcio nos terminais pré-sinápticos hiperexcitados e, consequentemente, diminui a liberação de neurotransmissores excitatórios — glutamato, noradrenalina e substância P. Esse mecanismo explica sua eficácia estabelecida em dor neuropática e convulsões parciais. Estudos de neuroimagem in vivo confirmaram que o pregabalin também eleva o limiar para a Depressão Alastrante Cortical (CSD), evento central na fisiopatologia da epilepsia e da enxaqueca.

A tendinite, entretanto, é uma condição primariamente inflamatória, com dor de natureza nociceptiva periférica. Não há efeito anti-inflamatório direto sobre o tecido tendinoso descrito para o pregabalin, nem ação sobre prostaglandinas ou citocinas locais. A literatura identificada restringe-se à analgesia perioperatória em reparo artroscópico do manguito rotador — contexto cirúrgico agudo, distinto do manejo clínico da tendinite. Esses achados não podem ser extrapolados diretamente a uma indicação terapêutica para inflamação tendinosa.

A pontuação TxGNN elevada (99,71%) provavelmente reflete associações topológicas no grafo de conhecimento entre os nós "dor musculoesquelética", "inflamação de partes moles" e "canais de cálcio", e não uma evidência biológica direta. Trata-se de um sinal de hipótese exploratória: eventualmente, subtipos de tendinite crônica com componente de sensibilização central poderiam se beneficiar do perfil de modulação do pregabalin — mas essa hipótese ainda carece de qualquer estudo clínico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para pregabalin em tendinite.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Pregabalin perioperatório produziu scores de dor equivalentes ao bloqueio interescaleno do plexo braquial após reparo artroscópico do manguito rotador, com menor consumo de opioides |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Coorte retrospectivo | J Orthop Sci | Avaliação do efeito poupador de opioides do pregabalin após reparo artroscópico do manguito rotador; resultados conflitantes com estudos anteriores |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Relato de Caso / Revisão | Praxis | Caso de incapacidade associada a fluoroquinolona (ciprofloxacino) com tendinopatia; fisiopatologia atribuída a dano ao sistema redox, sem relação com pregabalin |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Relato de Caso | Pain Practice | Neuropatia do nervo cutâneo femoral posterior pós-maratona, secundária a tendinite do isquiotibial; destaca a sobreposição de dor neuropática e tendinosa |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Síndrome do piriforme tratada por neurólise ciática e liberação do tendão do piriforme; discute síndrome glútea profunda e diagnóstico diferencial |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Estudo animal | Adv Pharmacol Pharm Sci | Extrato de C. quadrangularis (planta usada empiricamente em tendões lesados) atenuou neuropatia periférica induzida por vincristina em ratos; pregabalin utilizado como controle positivo de referência |

---

## Informações de Comercialização no Brasil

O pregabalin possui **20 registros ativos** no Brasil (situação: Comercializado). Os dados individuais dos registros — nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack. Consulte o portal da ANVISA para informações completas sobre cada registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A tendinite é uma condição de dor nociceptiva/inflamatória, e o mecanismo de ação do pregabalin — modulação da subunidade α2-δ de canais de cálcio — tem baixa correspondência com essa fisiopatologia. Não existem ensaios clínicos registrados para esta indicação, e a literatura disponível cobre exclusivamente analgesia perioperatória em cirurgia de tendão, contexto que não pode ser extrapolado ao tratamento da tendinite.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos específicos avaliando pregabalin em modelos de tendinite (inflamação tendinosa induzida)
- Investigação da hipótese de subtipos de tendinite crônica com sensibilização central como possível nicho de benefício
- Dados completos de MOA confirmados por fontes regulatórias (DrugBank / bula ANVISA)
- Dados de segurança e contraindicações extraídos da bula oficial
- Reavaliação da indicação de rank 5 (**Enxaqueca**) como candidato prioritário, que apresenta nível de evidência L2, 3 ensaios clínicos e 19 publicações, com fundamentação mecanicista mais sólida
---

