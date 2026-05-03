---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Lornoxicam
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

Using `txgnn-pipeline` as context. The skill covers pipeline management but the report generation is fully specified in the system prompt. Proceeding directly with the report.

---

# Lornoxicam: Da Dor Musculoesquelética à Artrite Reumatoide

## Resumo em Uma Frase

Lornoxicam é um anti-inflamatório não esteroidal (AINE) da classe dos oxicams, originalmente utilizado para alívio de dor aguda e condições inflamatórias músculo-esqueléticas (osteoartrite e dor reumática).
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**,
atualmente com **0 ensaios clínicos específicos registrados** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dor aguda e inflamação músculo-esquelética (osteoartrite, dor reumática) |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 99.90% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Lornoxicam é um AINE oxicam com mecanismo de ação baseado na **inibição dual de COX-1 e COX-2** (cicloxigenases). Essa inibição bloqueia a biossíntese de prostanoides — especialmente a prostaglandina E2 (PGE2) e o tromboxano A2 (TXA2) —, que são mediadores centrais da inflamação e da nocicepção periférica. Diferencia-se dos oxicams clássicos (piroxicam, meloxicam) por apresentar meia-vida de eliminação mais curta (3–5 horas), o que pode conferir melhor perfil de tolerabilidade. Adicionalmente, dados farmacológicos sugerem um componente analgésico central mediado por fraca ativação de receptores κ-opioides, ampliando seu espectro terapêutico para além da analgesia puramente periférica.

Na artrite reumatoide (AR), a inflamação sinovial persistente é sustentada por um ciclo de citocinas pró-inflamatórias (IL-1β, TNF-α, IL-6) que estimulam a produção de PGE2 pelo endotélio sinovial e macrófagos. A inibição da COX-1/COX-2 por lornoxicam interrompe esse ciclo local, reduzindo a inflamação articular, o edema e a dor — que são os alvos sintomáticos centrais da AR. Embora AINEs não modifiquem a progressão radiológica da doença (papel reservado aos DMARDs), são recomendados pelas principais diretrizes internacionais (EULAR, ACR) como **terapia adjuvante sintomática de primeira linha** em AR ativa.

A conexão entre a indicação de origem (dor músculo-esquelética aguda) e a AR é farmacologicamente direta: trata-se do mesmo mecanismo COX-inibitório aplicado a um contexto inflamatório crônico articular. A literatura já documenta estudos clínicos de longo prazo e ensaios cruzados com lornoxicam em pacientes com AR (PMIDs 12207202 e 12404032), tornando esta previsão do TxGNN não apenas plausível, mas suportada por evidência clínica real — o que eleva sua credibilidade para além de uma simples inferência de modelo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados ao uso de Lornoxicam especificamente em artrite reumatoide registrados nas bases consultadas (ClinicalTrials.gov e ICTRP).

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [22469263](https://pubmed.ncbi.nlm.nih.gov/22469263/) | 2011 | Drug Monograph / Review | Profiles of Drug Substances | Perfil farmacológico completo de lornoxicam: uso indicado para distúrbios músculo-esqueléticos e articulares como osteoartrite e artrite reumatoide; inclui MOA, farmacocinética e análise de segurança |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Pharmacology Review | Drugs | Revisão abrangente: lornoxicam eficaz quanto a morfina e petidina na analgesia; ensaios preliminares demonstram potencial para dor e inflamação reumática |
| [12207202](https://pubmed.ncbi.nlm.nih.gov/12207202/) | 2002 | Clinical Study | Minerva Medica | Estudo de longo prazo avaliando eficácia terapêutica e segurança de lornoxicam em pacientes com artrite reumatoide |
| [12404032](https://pubmed.ncbi.nlm.nih.gov/12404032/) | 2002 | Clinical Study (Crossover DB) | Reumatismo | Ensaio cruzado duplo-cego: lornoxicam 8 mg e 16 mg/dia versus diclofenaco 150 mg/dia em pacientes com AR; avaliação de eficácia analgésica e segurança |
| [27086708](https://pubmed.ncbi.nlm.nih.gov/27086708/) | 2016 | Clinical Review | Pain Management | Avaliação da tolerabilidade do inibidor COX-1/COX-2 lornoxicam no tratamento de dor aguda e reumática, com foco em eventos gastrointestinais |
| [12240779](https://pubmed.ncbi.nlm.nih.gov/12240779/) | 2002 | Literature Review | Clinical Therapeutics | Revisão das relações dose-efeito de AINEs em AR e OA; contextualiza o posicionamento de lornoxicam no espectro de eficácia vs tolerabilidade |
| [29026298](https://pubmed.ncbi.nlm.nih.gov/29026298/) | 2017 | Animal Study | Int J Nanomedicine | Fórmula nanomicelar de lornoxicam em modelos experimentais de AR: maior eficácia terapêutica anti-inflamatória que lornoxicam livre em sistema de administração sistêmica |
| [18479176](https://pubmed.ncbi.nlm.nih.gov/18479176/) | 2008 | Phase I (Crossover) | Clinical Drug Investigation | Biodisponibilidade comparativa de lornoxicam 8 mg em comprimido de liberação rápida, comprimido padrão e injeção IM em voluntários saudáveis; suporte para escolha de forma farmacêutica em AR |
| [32792844](https://pubmed.ncbi.nlm.nih.gov/32792844/) | 2020 | Formulation Study | Saudi Pharmaceutical Journal | Gel microsponge celulósico com lornoxicam: efeito anti-inflamatório sustentado para manejo da dor artrítica, com redução de efeitos sistêmicos |
| [25553695](https://pubmed.ncbi.nlm.nih.gov/25553695/) | 2015 | Formulation Study | Pakistan J Pharmaceutical Sciences | Formulação pulsincap de mini-comprimidos com lornoxicam para administração cronorerapêutica em AR, direcionada ao pico de sintomas matinais |

---

## Informações de Comercialização no Brasil

Lornoxicam possui **3 registros ativos** junto à ANVISA (situação: Comercializado). Os dados individuais dos registros (número ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis neste Evidence Pack e devem ser consultados diretamente no [portal ANVISA](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança completas (advertências, contraindicações e interações medicamentosas não estão disponíveis neste Evidence Pack — ver Data Gaps DG001).

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A previsão do TxGNN é mecanisticamente sólida e conta com suporte da literatura clínica publicada: dois estudos clínicos diretos em pacientes com AR (inclusive um ensaio cruzado duplo-cego contra diclofenaco) e múltiplas revisões farmacológicas confirmam a eficácia e tolerabilidade de lornoxicam nesta indicação. A ausência de ensaios clínicos registrados em bases globais limita o nível de evidência a L3, impedindo uma recomendação "Go" plena.

**Para prosseguir, é necessário:**
- Recuperar os dados detalhados dos 3 registros ANVISA (número de registro, nome comercial, forma farmacêutica e indicação aprovada) via portal ANVISA
- Obter a bula completa em português para mapear advertências, contraindicações e interações medicamentosas (Data Gap DG001 — classificado como Blocking)
- Verificar se o rótulo ANVISA aprovado já contempla AR ou restringe-se a dor aguda e osteoartrite
- Buscar o status de publicação do ensaio clínico PMID 12207202 e do crossover 12404032 em bases de dados adicionais para completar a cadeia de evidências
- Considerar registro de ensaio clínico Phase 2/3 no Brasil caso os registros ANVISA não incluam AR na bula vigente
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

