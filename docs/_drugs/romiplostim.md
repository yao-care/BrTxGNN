---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

Using **txgnn-pipeline** para garantir conformidade com o fluxo de relatórios TxGNN. Agora gerando o relatório completo a partir do Evidence Pack.

---

# Romiplostim: Da Trombocitopenia Imune ao Distúrbio Primário de Liberação Plaquetária

## Resumo em Uma Frase

Romiplostim (Nplate®) é um agonista do receptor de trombopoietina (TPO-RA), aprovado para o tratamento da trombocitopenia imune crônica (ITP), que estimula a produção de plaquetas pela ativação do receptor c-Mpl em megacariócitos da medula óssea.
O modelo TxGNN identificou **10 novas indicações potenciais** no espectro de distúrbios hemorrágicos plaquetários — a de maior pontuação é o **Distúrbio Primário de Liberação Plaquetária (primary release disorder of platelets)** com escore de 99,99983%, apoiada por 1 ensaio clínico e 2 publicações.
O destaque clínico desta avaliação é o **Distúrbio Hemorrágico do Tipo Plaquetário (platelet-type bleeding disorder)**, com **8 ensaios clínicos** (incluindo Phase 3 RCTs concluídos) e nível de evidência **L1**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Trombocitopenia imune crônica (ITP) |
| Nova Indicação Prevista (Top TxGNN) | Distúrbio Primário de Liberação Plaquetária (primary release disorder of platelets) |
| Pontuação de Previsão TxGNN | 99,99983% |
| Nível de Evidência | L4 (indicação top TxGNN) · **L1** (platelet-type bleeding disorder — melhor evidência) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold (indicação top TxGNN) · **Proceed with Guardrails** (platelet-type bleeding disorder) |

---

## Por que Esta Previsão é Razoável?

Romiplostim é um *peptibody* — fusão de peptídeos miméticos de trombopoietina com o domínio Fc de IgG1 humana. Ao se ligar ao receptor c-Mpl expresso nos megacariócitos, ativa as vias JAK2/STAT5 e MAPK, promovendo proliferação, diferenciação e maturação de precursores megacariocíticos. O resultado é o aumento sustentado da produção e liberação de plaquetas na circulação, de forma independente do mecanismo imunológico subjacente à trombocitopenia.

A plausibilidade das previsões do TxGNN reside no **fenótipo compartilhado de trombocitopenia ou disfunção hemorrágica plaquetária**. O "Distúrbio Primário de Liberação Plaquetária" envolve deficiência dos grânulos densos ou alfa, comprometendo a liberação de mediadores pró-agregação — a contagem de plaquetas é geralmente normal, mas o aumento do pool circulante induzido por Romiplostim poderia, em teoria, oferecer compensação numérica parcial. Esta hipótese, contudo, carece de validação experimental direta.

É essencial distinguir entre indicações mecanisticamente compatíveis e incompatíveis. Para condições de **qualidade plaquetária** — como Glanzmann (ausência de GPIIb/IIIa), Scott (defeito de escramblase) ou deficiência de receptor de colágeno — o aumento do número de plaquetas não corrige a disfunção molecular intrínseca, tornando a aplicação de Romiplostim mecanisticamente inviável. A exceção clinicamente válida é o **distúrbio hemorrágico do tipo plaquetário** (espectro ITP), onde o TPO-RA age diretamente sobre o déficit de produção, suportado por evidência robusta de nível L1.

---

## Panorama das 10 Indicações Previstas

| Rank | Indicação | Score TxGNN | Ensaios | Literatura | Evidência | Recomendação |
|------|-----------|-------------|---------|-----------|-----------|--------------|
| 1 | Distúrbio primário de liberação plaquetária | 99,99983% | 1 | 2 | L4 | Hold |
| 2 | Pseudo-doença de von Willebrand | 99,99977% | 0 | 0 | L5 | Hold |
| 3 | Trombastenia de Glanzmann | 99,99954% | 0 | 0 | L5 | Hold |
| 4 | Trombocitopenia aloimune fetal e neonatal (FNAIT) | 99,98730% | 0 | 2 | L4 | Research Question |
| 5 | Síndrome de Scott | 99,96656% | 0 | 0 | L5 | Hold |
| 6 | Distúrbio hemorrágico por trombocitopenia constitucional | 99,95290% | 0 | 0 | L5 | Hold |
| 7 | Diátese hemorrágica por defeito de receptor de colágeno | 99,95080% | 0 | 1 | L4 | Hold |
| **8** | **Distúrbio hemorrágico do tipo plaquetário** | **99,93190%** | **8** | **0** | **L1** | **Proceed with Guardrails** |
| 9 | Macrotrombocitopenia autossômica dominante (MYH9-RD) | 99,88074% | 0 | 1 | L4 | Research Question |
| 10 | Síndrome de Ehlers-Danlos tipo fibronectínico | 99,84516% | 0 | 0 | L5 | Hold |

---

## Evidências de Ensaios Clínicos

*(Indicação #1 — Distúrbio Primário de Liberação Plaquetária)*

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|--------|--------------|-------------------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Concluído | 10.039 | Estudo observacional de fatores de risco para trombose em ITP primária (doença autoimune rara). Caracteriza a população ITP como contexto epidemiológico; não avalia Romiplostim diretamente em distúrbio de liberação plaquetária. |

---

## Evidências da Literatura

*(Indicação #1 — Distúrbio Primário de Liberação Plaquetária)*

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Mechanistic/Translational | Haematologica | Autoanticorpos em ITP inibem a formação de proplatelet e a liberação plaquetária por megacariócitos in vitro, estabelecendo a ligação entre supressão da produção e deficiência de liberação. |
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Revisão sobre megacariocitopoiese: a TPO é o principal regulador da linhagem megacariocítica, da proliferação de progenitores à liberação plaquetária — fundamento mecanístico dos TPO-RAs. |

---

## Evidências de Ensaios Clínicos — Indicação de Destaque (L1)

*(Indicação #8 — Distúrbio Hemorrágico do Tipo Plaquetário — maior nível de evidência desta avaliação)*

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|--------|--------------|-------------------|
| [NCT03362177](https://clinicaltrials.gov/study/NCT03362177) | Phase 3 | Concluído | 165 | **RECITE**: RCT duplo-cego placebo-controlado de Romiplostim para trombocitopenia induzida por quimioterapia com oxaliplatina em cânceres GI, pancreático e colorretal. |
| [NCT05492409](https://clinicaltrials.gov/study/NCT05492409) | Phase 3 | Concluído | 160 | Estudo de extensão Phase 3 avaliando segurança e imunogenicidade de longo prazo do biossimilar GNR-069 em pacientes com ITP. |
| [NCT04638829](https://clinicaltrials.gov/study/NCT04638829) | Phase 4 | Concluído | 60 | Estudo prospectivo multicêntrico aberto: segurança e satisfação de tratamento após troca de Eltrombopag ou Romiplostim para Avatrombopag em ITP crônica adulta. |
| [NCT02298075](https://clinicaltrials.gov/study/NCT02298075) | N/A | Concluído | 148 | Estudo retrospectivo: taxa de resposta sustentada e duração da resposta após descontinuação de TPO-RA (Eltrombopag e Romiplostim) em ITP persistente ou crônica. |
| [NCT02046291](https://clinicaltrials.gov/study/NCT02046291) | Phase 1 | Concluído | 21 | Segurança de Romiplostim em falha de enxertia plaquetária pós-transplante de sangue de cordão umbilical: escalonamento de dose (4–10 mcg/kg/semana por 6 semanas). |
| [NCT07321626](https://clinicaltrials.gov/study/NCT07321626) | Phase 1 | Recrutando | 130 | Eficácia e segurança de Romiplostim N01 na reconstrução plaquetária pós-TCTH haploidentical em LMA, SMD e outras malignidades hematológicas (previsão: conclusão 12/2027). |
| [NCT02335268](https://clinicaltrials.gov/study/NCT02335268) | Phase 2 | Concluído | 77 | **EUROPE-trial**: Validação prospectiva de modelo preditivo de resposta ao Romiplostim em SMD baixo/intermediário-1 com trombocitopenia (TPO endógena e histórico transfusional como preditores). |
| [NCT02227576](https://clinicaltrials.gov/study/NCT02227576) | Phase 2 | Encerrado | 20 | Romiplostim como profilaxia secundária para trombocitopenia induzida por Temozolomide em glioblastoma recém-diagnosticado. Encerrado precocemente (20 pacientes); reduz força das conclusões. |

---

## Informações de Comercialização no Brasil

Romiplostim está registrado no Brasil com **3 registros ativos** e situação de mercado confirmada como comercializado. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada conforme bula) não estão disponíveis na base de dados desta avaliação.

> Para consultar os registros completos e a bula aprovada, acesse a base de dados da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota clínica baseada em literatura:** O uso prolongado de TPO-RAs como Romiplostim está associado a risco de fibrose medular (aumento de reticulina), risco aumentado de eventos tromboembólicos — especialmente em pacientes com fatores de risco pré-existentes — e trombocitopenia rebote após descontinuação abrupta. O estudo PMID 21902682 demonstrou aumento estatisticamente significativo de reticulina em biópsias de medula óssea de pacientes ITP em uso de TPO-RA. Monitorização periódica de hemograma completo (CBC com diferencial) é recomendada durante todo o tratamento.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

*(aplicável à Indicação #8 — Distúrbio Hemorrágico do Tipo Plaquetário, L1)*

**Justificativa:**
Romiplostim possui múltiplos ensaios Phase 3 concluídos e dados de uso real (Phase 4) que suportam sua eficácia no espectro de distúrbios hemorrágicos plaquetários por mecanismo imune, com evidência de nível L1. As demais 9 indicações previstas pelo TxGNN carecem de suporte mecanístico adequado (distúrbios de qualidade plaquetária) ou possuem apenas evidências exploratórias preliminares (FNAIT, MYH9-RD), mantendo recomendação de Hold ou Research Question.

**Para prosseguir, é necessário:**
- Confirmar dados completos dos 3 registros ANVISA (número de registro, nome comercial, forma farmacêutica e indicação aprovada na bula brasileira)
- Revisar bula brasileira para extrair advertências, contraindicações e protocolos de monitoramento específicos (actualmente classificados como Data Gap)
- Definir se "platelet-type bleeding disorder" representa extensão regulatória de indicação ou uso dentro do escopo já aprovado de ITP no Brasil
- Para indicações com recomendação **Research Question** (FNAIT — rank 4; MYH9-RD — rank 9), avaliar viabilidade de protocolos de estudo piloto, considerando que ambas possuem racional mecanístico parcial e evidências de caso/série
- Confirmar MOA completo via consulta à bula e DrugBank API (Data Gap classificado como severidade High)
---

