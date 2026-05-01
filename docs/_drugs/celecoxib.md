---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

A skill foi verificada. O conteúdo desta tarefa — gerar relatório de reposicionamento a partir de Evidence Pack — é coberto pelas instruções do agente especializado no system prompt. Procedendo à geração do relatório.

---

# Celecoxib: Da artrite reumatoide à espondilopatia inflamatória

## Resumo em Uma Frase

Celecoxib é um inibidor seletivo da ciclooxigenase-2 (COX-2), amplamente aprovado para o tratamento da artrite reumatoide, osteoartrite e dor aguda em adultos.
O modelo TxGNN prevê que pode ser eficaz para **Espondilopatia Inflamatória (Inflammatory Spondylopathy)**,
com **19 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Artrite reumatoide / Osteoartrite (inibidor seletivo de COX-2) |
| Nova Indicação Prevista | Espondilopatia Inflamatória (Inflammatory Spondylopathy) |
| Pontuação de Previsão TxGNN | 99.80% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Celecoxib atua como inibidor seletivo da ciclooxigenase-2 (COX-2), a principal isoforma enzimática responsável pela síntese de prostaglandinas pró-inflamatórias (PGE2, PGI2, TXA2) em tecidos inflamados. Ao suprimir especificamente a COX-2 — sem bloquear a COX-1, protetora da mucosa gástrica —, o fármaco reduz os mediadores de dor e destruição articular com menor toxicidade gastrointestinal em comparação com os AINEs não seletivos. Essa seletividade confere vantagem clínica relevante no uso contínuo e de longo prazo.

A espondilopatia inflamatória — grupo que abrange espondilite anquilosante (EA) e espondiloartrite axial (axSpA) — tem como mecanismo patológico central a inflamação crônica mediada por COX-2 na coluna vertebral, enteses e articulações sacroilíacas, com progressão para anquilose espinhal. Vale destacar que o celecoxib já está aprovado para espondilite anquilosante em países como EUA, União Europeia e Japão, o que torna a previsão do TxGNN não apenas plausível, mas apoiada por um histórico regulatório consolidado — configurando uma extensão de indicação, e não um reposicionamento de alto risco.

Evidências de 2025 (PMID: 39757202) identificaram o celecoxib como o **único NSAID capaz de inibir a progressão óssea radiográfica** (sindesmofitose) na espondiloartrite, sugerindo um efeito modificador de doença independente da inibição genérica de COX — possivelmente mediado pela regulação da via PGE2/Wnt/BMP. O ensaio CONSUL (NCT02758782, Phase 4, n=156) confirmou que a adição de celecoxib ao golimumabe reduziu a progressão estrutural espinhal em 2 anos em pacientes com axSpA radiográfica, consolidando a base mecanística da previsão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Concluído | 458 | Celecoxib 200 mg QD e BID vs diclofenaco 75 mg SR BID em EA por 12 semanas; avaliação de eficácia sintomática e segurança |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Concluído | 240 | Celecoxib 200 mg QD vs diclofenaco 75 mg SR QD em pacientes chineses com EA; estudo multicêntrico duplo-cego com fase de extensão de 6 semanas |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Concluído | 330 | Duas doses de celecoxib (200 mg e 400 mg) vs diclofenaco em EA por 12 semanas, confirmando resultados de estudo anterior |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Concluído | 156 | Ensaio CONSUL: celecoxib + golimumabe vs golimumabe isolado — progressão estrutural espinhal em axSpA radiográfica ao longo de 2 anos |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Concluído | 150 | Etanercepte e celecoxib isolados ou combinados em EA ativa; desfecho primário: escore MRI SPARCC da articulação sacroilíaca |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Concluído | 12 | Efeito de NSAIDs (incluindo celecoxib) em lesões inflamatórias de axSpA mensuradas por ressonância magnética |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminado | 42 | Série de ensaios N-of-1: inibidor seletivo de COX-2 vs não seletivo em axSpA; abordagem de medicina de precisão (encerrado por causas operacionais) |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Desconhecido | 106 | Naxozol vs celecoxib em OA/AR/EA: proteção gastrointestinal e alívio da dor — estudo ativo controlado duplo-cego multicêntrico |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminado | 9 | Estudo-piloto randomizado duplo-cego de 4 AINEs em axSpA por 6 semanas; interrompido por recrutamento insuficiente |
| [NCT01709656](https://clinicaltrials.gov/study/NCT01709656) | N/A | Concluído | 120 | Células-tronco mesenquimais vs controle com NSAIDs em EA ativa; coleta de biomarcadores (PBMCs e soro) antes e após 24 semanas |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT / Estudo Comparativo | Clinical Rheumatology | Celecoxib e imrecoxib afetam inflamação da articulação sacroilíaca em axSpA via regulação de metabolismo ósseo e angiogênese |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Celecoxib vs imrecoxib em axSpA: correlação entre escores de imagem e níveis séricos de DKK-1; avaliação em semanas 4 e 12 |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimode + celecoxib vs placebo em axSpA ativa: ensaio randomizado duplo-cego placebo-controlado |
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Revisão Sistemática / Meta-análise | BMB Reports | Celecoxib é o único NSAID a inibir progressão óssea em espondiloartrite; efeito potencialmente independente da inibição de COX |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT (análise CONSUL) | Annals of the Rheumatic Diseases | Celecoxib + anti-TNF vs anti-TNF isolado: redução da progressão radiográfica espinhal em axSpA ao longo de 2 anos |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Coorte Comparativa | Scandinavian Journal of Rheumatology | Risco cardiovascular e sangramento GI comparáveis entre celecoxib e nsNSAIDs em EA; coorte retrospectiva nacional |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Revisão Sistemática | Drugs | Celecoxib como primeiro COX-2 seletivo: revisão abrangente de eficácia sintomática e segurança em OA, AR e EA em adultos |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2015 | Coorte Nacional | Arthritis Care & Research | Segurança de etoricoxibe, celecoxib e nsNSAIDs em EA e outras SpA: eventos gastrointestinais, renovasculares e cardiovasculares — coorte sueca |
| [39315555](https://pubmed.ncbi.nlm.nih.gov/39315555/) | 2024 | Coorte | Reumatismo | Função hepática (AST/ALT) e renal (creatinina sérica) em pacientes com EA em uso contínuo de NSAIDs por longo prazo |
| [17983259](https://pubmed.ncbi.nlm.nih.gov/17983259/) | 2007 | Revisão | Drugs | Revisão abrangente de celecoxib no manejo de artrite e dor aguda; perfil de eficácia e segurança após uma década de uso clínico |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Celecoxib possui dois ensaios Phase 3 concluídos diretamente em EA/axSpA (n=458 e n=240), múltiplos estudos Phase 4 confirmados e evidências de 2025 que o identificam como o único NSAID com ação modificadora de progressão óssea em espondiloartrite. A base mecanística é sólida (COX-2 → PGE2 → Wnt/BMP), e o fármaco já detém aprovação regulatória para essa indicação em diversos países, configurando risco regulatório relativamente baixo no Brasil.

**Para prosseguir, é necessário:**
- Recuperar os dados detalhados dos 20 registros na ANVISA (nomes comerciais, formas farmacêuticas, indicações aprovadas em bula) para verificar se EA/axSpA já consta como indicação local
- Obter advertências, contraindicações e interações medicamentosas completas da bula ANVISA (dados de segurança atualmente indisponíveis)
- Avaliar necessidade de estudo de uso real (real-world evidence) brasileiro, dado que os ensaios Phase 3 foram conduzidos principalmente em populações asiáticas e europeias
- Definir protocolo de monitoramento cardiovascular e renal para uso contínuo em pacientes com espondilopatia, especialmente em uso combinado com agentes biológicos (anti-TNF)
---

