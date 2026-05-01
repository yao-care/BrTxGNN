---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azatioprina: Da Imunossupressão Sistêmica à Doença Inflamatória Intestinal

## Resumo em Uma Frase

Azatioprina é uma pró-droga imunossupressora da classe das tiopurinas, amplamente utilizada no mundo inteiro na prevenção de rejeição em transplantes de órgãos e no tratamento de doenças autoimunes — porém sem registro ativo na ANVISA segundo os dados disponíveis neste Evidence Pack. O modelo TxGNN prevê que pode ser eficaz para **Doença Inflamatória Intestinal (Inflammatory Bowel Disease)**, com pontuação de **99,52%**, atualmente com **múltiplos ensaios clínicos de Fase 3 concluídos** e **20 publicações** — incluindo três revisões sistemáticas Cochrane sobre colite ulcerosa — apoiando esta direção e conferindo nível de evidência **L1**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no mercado brasileiro (sem registro ANVISA) |
| Nova Indicação Prevista | Doença Inflamatória Intestinal (Inflammatory Bowel Disease) |
| Pontuação de Previsão TxGNN | 99,52% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Azatioprina é uma pró-droga que, no organismo, é convertida em nucleotídeos de 6-tioguanina (6-TGN). Esses metabólitos ativos exercem imunossupressão por três mecanismos complementares: (1) inibição competitiva da síntese de novo de purinas, reduzindo drasticamente os nucleotídeos disponíveis para a proliferação linfocitária; (2) incorporação ao DNA, induzindo apoptose seletiva de células T ativadas; e (3) bloqueio da via Rac1 GTPase → coestimulação CD28, interrompendo o segundo sinal necessário para a ativação completa de linfócitos T. Embora o mecanismo de ação formal não esteja disponível no Evidence Pack atual (dado ausente no DrugBank), este perfil farmacodinâmico está amplamente documentado na literatura científica internacional há mais de 45 anos.

A Doença Inflamatória Intestinal — que engloba a Doença de Crohn (DC) e a Colite Ulcerosa (CU) — é impulsionada por ativação anômala de linfócitos T CD4+: predomínio Th1/Th17 na DC e Th2/Th9 na CU, resultando em inflamação crônica e progressiva da mucosa gastrointestinal com ciclos de recidiva e remissão. A tripla ação da azatioprina sobre a proliferação, sobrevivência e ativação das células T encaixa-se diretamente na fisiopatologia central da DII, tornando esta previsão computacional mecanisticamente sólida e biologicamente coerente.

A robustez desta previsão é confirmada pela convergência entre o modelo TxGNN e décadas de evidências clínicas: as principais diretrizes internacionais (ECCO, ACG, AGA, GETECCU) já incorporaram azatioprina como imunomodulador de segunda linha para manutenção de remissão na DII. Vale destacar que a Colite Ulcerosa (Rank 9 neste painel, TxGNN: 99,33%) partilha a mesma base de evidências L1 e é contemplada diretamente pelas revisões sistemáticas Cochrane e pelos ensaios clínicos de Fase 3 aqui apresentados, reforçando duplamente a validade da previsão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Concluído | 508 | Comparação direta triplo-braço: Infliximab vs Azatioprina (IMURAN®) vs terapia combinada em Doença de Crohn naïve a imunossupressores — maior evidência direta do valor de AZA como tratamento ativo |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Concluído | 78 | Azatioprina vs mesalazina (duplo-cego) na prevenção de recorrência clínica pós-operatória em DC com recorrência endoscópica moderada a grave |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Concluído | 83 | Estudo multicêntrico randomizado aberto: AZA vs mesalazina para prevenção de recorrência pós-operatória na Doença de Crohn |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Desconhecido | 84 | AZA em dose baixa + Alopurinol vs AZA em dose padrão na Colite Ulcerosa — otimização terapêutica para reduzir taxa de falha (até 50%) e eventos adversos |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Encerrado precocemente | 31 | ACORDIS: Dose ótima baseada em peso de IMURAN® (azatioprina) em DC ativa com corticosteroide — dados de dose-resposta e segurança |
| [NCT01536535](https://clinicaltrials.gov/study/NCT01536535) | Phase 4 | Concluído | 431 | Estudo multicêntrico aberto em crianças/adolescentes com CU recém-diagnosticada: efetividade e segurança da terapia inicial padronizada incluindo AZA |
| [NCT05535946](https://clinicaltrials.gov/study/NCT05535946) | Phase 3 | Em andamento | 1.116 | Maior ensaio de manutenção em CU moderada a grave: AZA como terapia de referência ativa para comparação com novo agente (ABX464) — confirma centralidade de AZA na prática clínica atual |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Concluído | 192 | Estudo estratificado por risco: Metotrexato vs Azatioprina/6-MP na DC pediátrica de baixo risco — evidência comparativa direta de eficácia de AZA em população pediátrica |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Concluído | 65 | Estudo multicêntrico randomizado: IFX + AZA vs corticosteroide + AZA em CU grave aguda — valida o papel de AZA na estratégia de terapia combinada |
| [NCT01802593](https://clinicaltrials.gov/study/NCT01802593) | Phase 4 | Encerrado precocemente | 20 | Comparação de regimes de retirada de imunomodulador (AZA) para monoterapia com Infliximab em DC pediátrica — confirma o papel da AZA na manutenção da remissão |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | Revisão Cochrane (3ª atualização): AZA e 6-MP para manutenção de remissão na Colite Ulcerosa — síntese definitiva e mais recente de todas as evidências disponíveis |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE Trial: IFX + AZA vs AZA isolada em CU grave aguda responsiva a corticoides IV — ensaio randomizado controlado publicado no periódico Gut, demonstra efetividade de AZA em manutenção |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Segunda revisão Cochrane sobre AZA/6-MP na manutenção de remissão da CU — dados favoráveis ao uso contínuo na prática clínica |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Primeira revisão Cochrane: AZA/6-MP na CU — base evidencial histórica que fundamentou as diretrizes atuais |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-Analysis | Aliment Pharmacol Ther | Meta-análise da eficácia de AZA e 6-MP na CU — confirma superioridade sobre placebo na manutenção da remissão |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | Estado da arte das tiopurinas na DII: mecanismos de ação, eficácia, segurança, adesão terapêutica e perspectivas futuras |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Review | World J Gastroenterol | Otimização da terapia com AZA/6-MP na DII: correlação entre níveis de 6-TGN e eficácia clínica, prevenção de toxicidade hepática e mielossupressão |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanistic Review | Expert Rev Gastroenterol Hepatol | Novos insights moleculares do mecanismo de ação da AZA na DII: via Rac1 GTPase, apoptose T celular seletiva e implicações clínicas resultantes |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Pharmacogenomics Review | J Gastroenterol Hepatol | Farmacogenética da AZA/6-MP e monitorização de metabólitos na DII — base científica para terapia personalizada com TPMT e 6-TGN |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Translational | Cell Rep Med | Alta prevalência de Blautia wexlerae intestinal associada à falha terapêutica da AZA na DII — mecanismo microbiológico de resistência e implicações para monitoramento clínico |

---

## Informações de Comercialização no Brasil

Azatioprina não possui registros ativos na ANVISA conforme os dados consultados neste Evidence Pack. O fármaco apresenta **0 registros** e situação de mercado classificada como **não comercializado** no Brasil. A regularização do registro seria pré-requisito para qualquer estratégia de introdução no mercado nacional.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existem múltiplos ensaios clínicos de Fase 3 concluídos (NCT00094458, n=508; NCT00946946, n=78; NCT00976690, n=83) e três revisões sistemáticas Cochrane atualizadas (2012, 2016, 2025) documentando de forma consistente a eficácia da azatioprina na Doença Inflamatória Intestinal. O alinhamento entre a previsão TxGNN (99,52%), a coerência mecanística e o nível de evidência L1 sustenta com solidez a recomendação de avanço com salvaguardas.

**Para prosseguir, é necessário:**
- Regularizar o registro junto à ANVISA para viabilizar a comercialização no Brasil
- Complementar os dados do mecanismo de ação (MOA) via consulta à API do DrugBank (DB00993)
- Obter e analisar a bula atualizada com advertências, contraindicações e interações medicamentosas relevantes para a população brasileira
- Implementar protocolo de rastreio farmacogenômico (genotipagem de TPMT e/ou NUDT15) antes do início da terapia, especialmente relevante em populações com alta prevalência de variantes de risco (como populações asiáticas) para prevenção de leucopenia grave
- Mapear as especificidades epidemiológicas da DII no Brasil para adequação da estratégia terapêutica e regulatória local
---

