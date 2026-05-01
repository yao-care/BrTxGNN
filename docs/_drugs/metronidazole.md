---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

---

# Metronidazole: Das infecções anaeróbias à pneumocistose

## Resumo em Uma Frase

Metronidazole é um antibiótico nitroimidazólico clássico, amplamente utilizado no tratamento de infecções anaeróbias e protozoárias, incluindo amebíase, tricomoníase, giardíase, vaginose bacteriana e infecções pós-cirúrgicas.
O modelo TxGNN prevê que pode ser eficaz para **Pneumocistose (Pneumocystosis)**, com **0 ensaios clínicos relevantes** e **10 publicações** recuperadas — porém a análise mecanística indica que esta previsão é um **falso positivo por viés de co-ocorrência**, sem base farmacológica que a sustente.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções anaeróbias e protozoárias (dados regulatórios brasileiros não disponíveis no banco de dados atual) |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 99.99% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não consta no banco de dados regulatório |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Metronidazole atua por **ativação anaeróbia**: o anel nitroimidazólico é reduzido por ferredoxinas e flavodoxinas — proteínas encontradas exclusivamente em microrganismos com cadeia de transporte de elétrons anaeróbia. O metabólito ativo resultante provoca quebras na fita de DNA do patógeno, sendo eficaz contra bactérias anaeróbias estritas e certos protozoários (*Trichomonas vaginalis*, *Entamoeba histolytica*, *Giardia lamblia*).

*Pneumocystis jirovecii*, no entanto, foi **reclassificado como fungo Ascomiceto** em 1988 (anteriormente classificado como protozoário). Fungos possuem sistema de transporte de elétrons eucariótico e aeróbio, sendo incapazes de ativar o Metronidazole ao seu metabólito tóxico. O tratamento padrão para pneumocistose é trimetoprima-sulfametoxazol (TMP-SMX), com pentamidina como alternativa — Metronidazole não figura em nenhuma diretriz terapêutica desta infecção.

A alta pontuação TxGNN (99,99%) deve-se provavelmente a **viés de co-ocorrência lexical no grafo de conhecimento**: Metronidazole é frequentemente mencionado em literaturas sobre AIDS e infecções oportunistas, contexto clínico em que a pneumocistose também aparece — criando uma associação estatística que não reflete relação farmacológica real. Esta é uma limitação conhecida de modelos baseados em grafos treinados com dados de co-menção em textos médicos.

---

## Evidências de Ensaios Clínicos

Os 23 ensaios clínicos recuperados automaticamente são **inteiramente não relacionados** à combinação Metronidazole + pneumocistose — todos classificados como Grau C (nenhum envolve intervenção com Metronidazole em população com pneumocistose). Os estudos recuperados abrangem temas como mindfulness em atenção primária, redução do uso de opioides, suporte a cuidadores de pacientes com demência e rastreamento de diabetes.

> Atualmente não há ensaios clínicos relacionados registrados para Metronidazole em pneumocistose.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | Revisão das infecções oportunistas relacionadas ao HIV; pneumocistose é tratada com TMP-SMX ou pentamidina — Metronidazole não é citado como opção terapêutica para pneumocistose |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Complicações infecciosas da AIDS; PCP é a mais comum (58%); tratamento recomendado é pentamidina ou TMP-SMX, não Metronidazole |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | Revisão de agentes antiparasitários; Metronidazole listado para protozoários anaeróbios (amebíase, tricomoníase, giardíase) — Pneumocystis não incluído |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Revisão de antiparasitários; TMP-SMX indicado para pneumocistose; Metronidazole indicado para amebíase e tricomoníase — sem sobreposição |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Justificativa farmacocinética de terapias antiprotozoárias; foca em parasitos com cadeia anaeróbia — Pneumocystis não incluído como alvo do Metronidazole |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Revisão de drogas antiprotozoárias no Japão; sem evidência de atividade do Metronidazole contra Pneumocystis |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Rev Respir Dis | Caso de PCP em adulto previamente saudável; Metronidazole foi usado para infecção intestinal anaeróbia prévia, não para tratar pneumocistose |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | Dois casos de AIDS no Japão; Metronidazole tratou disenteria amébica concomitante — não foi usado para PCP |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formos Med Assoc | Perfuração de cólon em paciente com AIDS e amebíase; Metronidazole usado para amebíase — pneumocistose foi complicação concorrente, não alvo do tratamento |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Crítica aos ensaios de profilaxia antimicrobiana; discussão metodológica — sem relevância direta para Metronidazole em pneumocistose |

> **Nota interpretativa:** Nenhuma das 10 publicações documenta atividade do Metronidazole contra *Pneumocystis jirovecii*. A co-ocorrência nos textos reflete o contexto clínico compartilhado (AIDS com infecções mistas), e não uma relação terapêutica.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para Metronidazole em pneumocistose é farmacologicamente inviável: o mecanismo de ação do Metronidazole exige uma cadeia de transporte de elétrons anaeróbia para ativação, estrutura ausente em *Pneumocystis jirovecii* (fungo aeróbio eucariótico). A incompatibilidade mecanística é definitiva, não há ensaios clínicos relevantes, e a totalidade da literatura recuperada confirma que Metronidazole não é — e não deve ser — utilizado para tratar pneumocistose.

**Ações recomendadas:**
- **Não prosseguir** com esta hipótese de reposicionamento — investir recursos nesta direção não é justificável
- **Revisar o pipeline TxGNN** para identificar e filtrar falsos positivos gerados por viés de co-ocorrência em grafos de AIDS/infecções oportunistas
- **Priorizar indicações com suporte real** identificadas neste Evidence Pack:
  - **Cap polyposis** (Rank 9 | L3 | "Proceed with Guardrails"): dupla ação antibacteriana + anti-inflamatória; evidência mecanística direta (PMID 12141801); indicado para pilot RCT
  - **Ulcerative proctosigmoiditis** (Rank 3 | L3 | "Research Question"): prática clínica estabelecida em pouchitis; extensão lógica para proctossigmoidite ulcerativa
---

