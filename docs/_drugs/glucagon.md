---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glucagon: Do Tratamento da Hipoglicemia à Síndrome do Intestino Irritável

## Resumo em Uma Frase

Glucagon é um hormônio pancreático peptídico utilizado principalmente no tratamento de hipoglicemia grave e como agente antiespasmódico gastrointestinal em procedimentos endoscópicos diagnósticos. O modelo TxGNN prevê que pode ser eficaz para **Síndrome do Intestino Irritável (Irritable Bowel Syndrome)**, atualmente com **11 ensaios clínicos** e **20 publicações** apoiando esta direção — embora a maioria das evidências seja indireta, referindo-se a agonistas do receptor de GLP-1 (classe homóloga), e não ao glucagon em si.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipoglicemia grave; adjuvante antiespasmódico em imagens e endoscopias gastrointestinais |
| Nova Indicação Prevista | Síndrome do Intestino Irritável (Irritable Bowel Syndrome) |
| Pontuação de Previsão TxGNN | 99,24% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Glucagon (DB00040) é um peptídeo hormonal de 29 aminoácidos codificado pelo gene proglucagon — a mesma fonte genética do glucagon-like peptide-1 (GLP-1). Ambos pertencem à família dos glucagon peptídeos e compartilham homologia estrutural significativa, embora atuem por receptores distintos: o receptor de glucagon (GCGR) e o receptor de GLP-1 (GLP-1R). Clinicamente, o glucagon já é reconhecido pelo seu efeito de relaxamento da musculatura lisa gastrointestinal (ação antiespasmódica), explorado antes de procedimentos endoscópicos. Essa propriedade sugere um potencial efeito modulador sobre a motilidade intestinal alterada que caracteriza a SII.

A relevância mecanística para a SII, contudo, vem majoritariamente do eixo GLP-1: os receptores GLP-1R estão amplamente expressos no sistema nervoso entérico, regulando peristalse, sensibilização visceral à dor e integridade da barreira mucosa intestinal. Estudos clínicos com ROSE-010 (análogo peptídico da classe proglucagon) demonstraram redução da dor e melhora da motilidade em pacientes com SII-C, e uma revisão sistemática de 2025 (PMID 40134805) consolida esses achados para a classe dos GLP-1 RAs em SII. Um único estudo identificou redução dos níveis séricos de GLP-1 em SII-C correlacionada à dor abdominal (PMID 28215540), reforçando o papel do eixo proglucagon na fisiopatologia da doença.

No entanto, o alto score TxGNN (0,9924) reflete primariamente o sinal de homologia familiar (proglucagon) e não evidência clínica direta do glucagon na SII. A distinção entre GCGR e GLP-1R é farmacologicamente crítica: o glucagon em si carece de estudos clínicos prospectivos em SII, e a extrapolação do efeito de classe a partir de GLP-1 RAs requer validação experimental independente antes de avançar no pipeline de reposicionamento.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Concluído | 52 | ROSE-010 (análogo da família proglucagon) avaliado em mulheres com SII-C; estuda atraso no esvaziamento gástrico e acomodação gástrica sem retardo do trânsito colônico — evidência mais direta da classe na SII |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Concluído | 12 | Comparação de GLP-1 nativo e ROSE-010 em estudos in vivo e in vitro; investigação do efeito inibitório sobre motilidade antro-duodeno-jejunal prandial — suporte mecanístico para a família proglucagon |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Encerrado precocemente | 8 | Liraglutide (GLP-1 RA) em pacientes com anastomose íleo-bolsa anal e alta frequência evacuatória; encerrado por dificuldade de recrutamento — evidência muito limitada pelo tamanho amostral |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Concluído | 66 | Exercício contínuo moderado vs. intervalo de alta intensidade em SII obesos e pré-diabéticos; mede variações no GLP endógeno — sem intervenção com glucagon exógeno |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Concluído | 37 | Mecanismo de ação do butirato no cólon humano em contexto de SII — estudo de fisiologia de fundo sem relação direta com glucagon |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Ativo, sem novos recrutamentos | 375 | Estabelecimento de organoides de intestino delgado para avaliar agentes terapêuticos — pesquisa de ciências básicas, sem intervenção farmacológica direta |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Concluído | 33 | Intervenção nutricional direcionada ao microbioma intestinal para integridade da barreira GI em hipóxia hipobárica — sem relação direta com glucagon |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Concluído | 33 | Pão de centeio integral no eixo microbiota-intestino-cérebro em adultos saudáveis — pesquisa dietética de contexto, sem intervenção farmacológica |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Concluído | 41 | Efeito da taxa de ingestão de alimentos ultraprocessados sobre comportamento alimentar e respostas metabólicas — sem relevância direta para SII ou glucagon |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Status desconhecido | 110 | Dieta de baixa energia vs. dieta combinada com balão intragástrico em adultos com obesidade — contexto metabólico-comportamental sem relação com SII ou glucagon |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisão Sistemática | Frontiers in Endocrinology | Meta-análise confirmando melhora dos sintomas de SII com GLP-1 RAs; demonstra que GLP-1 e ROSE-010 inibem o complexo motor migratório e reduzem motilidade GI em pacientes com SII — evidência de mais alto nível disponível para a classe |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Resultado de Ensaio Clínico | Scandinavian Journal of Gastroenterology | Cross-análise de dados clínicos de ROSE-010 em SII; identifica a subpopulação mais responsiva ao tratamento (IBS-C, sexo feminino) — evidência clínica mais direta da família proglucagon na SII |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Revisão Sistemática | The Journal of Headache and Pain | Revisão sistemática do papel dos GLP-1 RAs em distúrbios de dor e cefaleia; avalia potencial analgésico visceral relevante para o componente de dor da SII |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Observacional | Annals of Gastroenterology | Dados de vida real sobre prescrição e descontinuação de GLP-1 RAs em pacientes com SII; evidencia a relação entre efeitos GI adversos e descontinuação — relevante para o perfil de segurança de reposicionamento |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisão | Experimental Physiology | Revisão sobre o papel das células L secretoras de GLP-1 na fisiopatologia da SII (estresse, imunidade, microbiota, bile); fornece base mecanística para a hipótese de reposicionamento |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Estudo Clínico | Clinics and Research in Hepatology and Gastroenterology | Níveis séricos de GLP-1 reduzidos correlacionados com dor abdominal em SII-C; expressão do receptor GLP-1 no cólon confirmada — suporte biomarker para o eixo proglucagon-SII |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Pré-clínico | Neurogastroenterology and Motility | Exendin-4 (GLP-1 RA) ameliorou disfunção gastrointestinal no modelo animal de SII (rato WKY); fornece suporte mecanístico pré-clínico para o eixo GLP-1R na SII |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Experimental/Hipótese | Advances in Experimental Medicine and Biology | Proposta de GLP-1 aerossolizado para tratamento simultâneo de diabetes e SII; sinaliza o potencial translacional do eixo incretin-SII e discute desafios de formulação |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Revisão | The Journal of Clinical Investigation | Revisão atualizada sobre mecanismos de interação intestino-cérebro; destaca o papel crescente das terapias baseadas em GLP-1 e dos circuitos enteroendócrino-neurais — contextualiza o momento científico atual |
| [3617051](https://pubmed.ncbi.nlm.nih.gov/3617051/) | 1987 | Estudo Clínico | Tohoku Journal of Experimental Medicine | Dados históricos sobre motilidade colônica e hormônios GI sob estresse psicológico em pacientes com SII; estabelece precedente para o papel de hormônios como o glucagon na fisiopatologia da SII |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O score elevado do TxGNN (99,24%) reflete homologia do gene proglucagon com GLP-1, e não evidência clínica direta de eficácia do glucagon na SII. A totalidade dos estudos identificados investiga agonistas do receptor GLP-1 (GLP-1 RAs) — moléculas que atuam em receptor distinto (GLP-1R vs. GCGR) e possuem perfil farmacológico diferente do glucagon. Não existe, até o momento, nenhum ensaio clínico prospectivo testando glucagon diretamente em pacientes com SII.

**Para prosseguir, é necessário:**
- Obter advertências, contraindicações e dados de segurança completos da bula oficial (DG001 — bloqueante)
- Obter dados de mecanismo de ação (MOA) do DrugBank para caracterizar com precisão a seletividade do glucagon por GCGR vs. GLP-1R (DG002)
- Realizar busca bibliográfica direcionada por estudos usando glucagon (não GLP-1 RAs) em distúrbios funcionais intestinais e SII
- Avaliar se o efeito antiespasmódico GI do glucagon — já documentado em endoscopia — é farmacologicamente sustentável e relevante para a SII
- Caso as lacunas acima mostrem sinal favorável, desenhar um estudo exploratório de Fase 1/2 com glucagon especificamente em SII antes de avançar no pipeline de reposicionamento
---

