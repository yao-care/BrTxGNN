---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 1
---

# Folic Acid
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

# Ácido Fólico: Da Deficiência de Folato à Doença Metabólica da Biotina

## Resumo em Uma Frase

Ácido fólico (vitamina B9) é amplamente utilizado na prevenção de defeitos do tubo neural, no tratamento da anemia megaloblástica e na reposição de folato em situações de deficiência. O modelo TxGNN prevê que pode ter utilidade terapêutica na **Doença Metabólica da Biotina (Biotin Metabolic Disease)**, com base na sobreposição de vias metabólicas entre folato e biotina. Foram identificados **13 ensaios clínicos** e **20 publicações**, embora a grande maioria seja de relevância indireta para esta indicação específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Prevenção de defeitos do tubo neural; tratamento de anemia megaloblástica e deficiência de folato |
| Nova Indicação Prevista | Doença Metabólica da Biotina (Biotin Metabolic Disease) |
| Pontuação de Previsão TxGNN | 99,49% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Ácido fólico (vitamina B9/folato) e biotina (vitamina B7) são ambos membros do complexo vitamínico B e participam de vias metabólicas funcionalmente sobrepostas — em especial o **metabolismo de carbono único** (*one-carbon metabolism*) e a síntese de coenzimas. Nas principais doenças metabólicas da biotina — deficiência de biotinidase e deficiência de holocarboxilase sintetase — a disfunção das carboxilases dependentes de biotina pode interferir no ciclo do folato e no metabolismo de ácidos orgânicos, criando uma ligação bioquímica entre os dois nutrientes.

A ponte mecanística é, no entanto, de natureza **indireta**: a disfunção das carboxilases dependentes de biotina afeta o metabolismo de propionil-CoA e metilmalonil-CoA, o que pode perturbar secundariamente o ciclo do folato e a homeostase da homocisteína. Adicionalmente, ambos os nutrientes exercem papel protetor no desenvolvimento neurológico — um dos principais desfechos clínicos afetados nas doenças metabólicas da biotina. O alto escore TxGNN (0,9949) reflete a proximidade dos dois nós no grafo de conhecimento, mas essa conexão é primariamente de compartilhamento de vias, não de ação terapêutica direta.

É fundamental ressaltar que **o ácido fólico não é o tratamento padrão para doenças metabólicas da biotina** — a terapia de primeira linha consiste na suplementação com biotina em altas doses. A hipótese de reposicionamento aqui investigada é de **suporte metabólico auxiliar**, não de substituição terapêutica.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Aviso**: Nenhum dos ensaios clínicos identificados testa diretamente o ácido fólico como intervenção terapêutica para doença metabólica da biotina. Todos são de relevância indireta (Grau C).

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Concluído | 6.824 | Programa Baby Detect: rastreamento genômico neonatal universal para 126 doenças genéticas graves, incluindo doenças do metabolismo da biotina; não envolve intervenção com ácido fólico |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Desconhecido | 200 | Estudo cruzado duplo-cego de terapia de suporte metabólico com CoQ10 ubiquinol e complexo vitamínico B e E em autismo idiopático e síndrome de Phelan-McDermid |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Fase 2 | Concluído | 75 | Suplementação de vitaminas e minerais em complicações de diabetes tipo 2 (nefropatia/neuropatia); população e desfecho distintos da indicação-alvo |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Concluído | 30 | Comparação de complexo vitamínico B natural vs. sintético em humanos; avalia biodisponibilidade de vitaminas incluindo biotina e folato, não trata doença metabólica |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Fase 4 | Ativo (não recrutando) | 794 | ECR sobre suplementação pré-natal de iodo e neurodesenvolvimento infantil; intervenção principal é iodo, não folato |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Concluído | 40 | Intervenção multi-micronutrientes (incluindo folato) em cuidados paliativos para insuficiência cardíaca congestiva |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Concluído | 99 | Absorção de vitaminas transdérmicas (incluindo biotina e folato) em pacientes pós-cirurgia bariátrica; foco em farmacocinética, não em tratamento de doença metabólica |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Concluído | 39 | Tratamento do estresse oxidativo e patologia metabólica do autismo com intervenção nutricional direcionada; alvo distinto da indicação-alvo |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Concluído | 202 | Efeito de multivitamínicos/minerais (com/sem ácidos graxos ômega-3) sobre impulsividade e agressividade em indivíduos com histórico antissocial |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | N/A | Ativo (não recrutando) | 20 | Estudo exploratório piloto de microbioma intestinal e intervenções prebióticas personalizadas na recuperação de dependência alcoólica |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Revisão de distúrbios responsivos a vitaminas (cobalamina, folato, biotina); discute a base para tratamento de erros inatos do metabolismo com altas doses vitamínicas |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Distúrbios do movimento em erros inatos do metabolismo tratáveis; inclui doenças dependentes de biotina com resposta à suplementação |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sciences | Mecanismos moleculares da deficiência de B12; destaca a relação metabólica entre síntese de succinil-CoA (dependente de biotina), folato e homocisteína |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics N Am | Aminoacidopatias responsivas a megadoses vitamínicas; fundamento clínico histórico para o conceito de vitamino-responsividade em erros inatos do metabolismo |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Review | Advances in Human Genetics | Distúrbios metabólicos herdados responsivos a vitaminas; base conceitual para reposicionamento de vitaminas em erros inatos |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Review | Archives de Pédiatrie | Epilepsia neonatal e erros inatos do metabolismo; inclui discussão de doenças tratáveis com vitaminas do complexo B, entre elas biotina e folato |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica | Três mecanismos pelos quais vitaminas interferem na patogênese de doenças metabólicas: má absorção, erro no metabolismo vitamínico e síndromes vitamino-dependentes |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Síndrome de dependência vitamínica; revisão clínica de distúrbios de dependência de coenzimas, incluindo biotina-dependência |
| [6396715](https://pubmed.ncbi.nlm.nih.gov/6396715/) | 1984 | Review | Progress in Food & Nutrition Science | Imunidade celular em deficiências nutricionais; papel de biotina e piridoxina na manutenção da celularidade tímica e imunidade mediada por células |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Arch Biochem Biophys | "Metabolic tune-up": papel dos micronutrientes (incluindo folato e cofatores como biotina) na otimização metabólica e prevenção de danos ao DNA |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora a ligação metabólica entre folato e biotina seja biologicamente plausível — ambos participam do metabolismo de carbono único e vias de coenzimas —, a evidência clínica direta para o uso de ácido fólico em doença metabólica da biotina é inexistente. Todos os 13 ensaios clínicos identificados são de relevância indireta (Grau C), e a literatura disponível consiste majoritariamente em revisões narrativas que mencionam a relação entre as duas vitaminas no contexto de erros inatos do metabolismo, sem estudos de intervenção específicos.

**Para prosseguir, é necessário:**
- Conduzir ou identificar estudos pré-clínicos (*in vitro* / modelos animais) avaliando especificamente o efeito do ácido fólico em modelos de deficiência de biotinidase ou holocarboxilase sintetase
- Realizar revisão sistemática focada na relação mecanística folato-biotina em doenças metabólicas raras
- Obter dados de segurança completos (bula ANVISA/TFDA, advertências e contraindicações) para viabilizar a avaliação S1
- Consultar o DrugBank para dados completos de mecanismo de ação (MOA) — atualmente ausentes
- Avaliar se o ácido fólico poderia atuar como **adjuvante** em pacientes com doença metabólica da biotina já em tratamento padrão com biotina, em vez de substituto terapêutico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

