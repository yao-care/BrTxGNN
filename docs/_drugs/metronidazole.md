---
layout: default
title: Metronidazole
parent: Apenas Predição do Modelo (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metronidazole: nova indicação prevista, Pneumocistose (Pneumocystosis) (nível de evidência L5). Indicação original: Amebicidas, giardicidas e tricomonicidas"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

# Metronidazol: De antiprotozoário e antibacteriano para pneumocistose (previsão com evidência muito fraca)

## Resumo em Uma Frase

Metronidazol é um antimicrobiano nitroimidazólico, registrado no Brasil como amebicida, giardicida e tricomonicida, e também como antiinfeccioso e produto de ação em pele e mucosas.
O modelo TxGNN prevê que pode ser eficaz para **pneumocistose (Pneumocystosis)**, mas não há **nenhum ensaio clínico** e a literatura recuperada (**10 publicações**) é composta por revisões gerais e relatos de caso, sem demonstrar eficácia do fármaco contra *Pneumocystis*.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Amebicidas, giardicidas e tricomonicidas |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nas informações compiladas para este relatório. Segundo informações conhecidas, o metronidazol atua sobre bactérias anaeróbias e protozoários por ativação redutora do seu grupo nitro, que gera metabólitos tóxicos para o DNA do microrganismo.

Neste caso, **a previsão é pouco razoável do ponto de vista mecanístico**. *Pneumocystis* é um fungo e não possui a via de nitrorredutases necessária para ativar o metronidazol. A pontuação alta do TxGNN provavelmente é um artefato de proximidade na rede de conhecimento (o fármaco e a doença aparecem frequentemente em contextos de infecções oportunistas e antiparasitários), e não um sinal biológico real. O tratamento padrão da pneumocistose é sulfametoxazol-trimetoprima.

Outras previsões do modelo têm respaldo mais plausível, embora ainda indireto: **proctossigmoidite ulcerativa**, **pôliposis em capuz (cap polyposis)** e **úlcera de vulva** (esta última, em geral associada à doença de Crohn vulvar ou amebíase cutânea). Ficam como hipóteses de pesquisa, não como a indicação principal avaliada aqui.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Prioridade para os tipos de estudo mais robustos; nenhum é RCT.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revisão | Mayo Clinic Proceedings | Panorama geral dos antiparasitários; não demonstra eficácia do metronidazol contra *Pneumocystis* |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisão | American Family Physician | Metronidazol indicado para colite amebiana, amebíase extraintestinal e tricomoníase; para pneumonia por *Pneumocystis*, o fármaco de escolha é trimetoprima-sulfametoxazol |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revisão | Clinical Pharmacokinetics | Justificativa farmacocinética da terapia antiprotozoária, sem evidência para pneumocistose |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisão | Clinical Pharmacy | Revisão do tratamento de complicações infecciosas da AIDS; *P. carinii* é a mais comum |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revisão | Topics in Antiviral Medicine | Infecções oportunistas relacionadas ao HIV continuam relevantes; sem apoio ao metronidazol |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revisão | Reviews of Infectious Diseases | Crítica de ensaios de profilaxia antimicrobiana; não relacionada à indicação |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Relato de caso | Am Rev Respir Dis | Pneumonia por *P. carinii* e citomegalovírus em adulto previamente tratado com metronidazol e tetraciclina; sem indício de benefício |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Relato de caso | Kansenshogaku Zasshi | Paciente com amebíase tratado com metronidazol, depois com pneumocistose na evolução da AIDS |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Relato de caso | J Formos Med Assoc | Perfuração de cólon por citomegalovírus e colite amebiana em paciente com AIDS |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Relato de caso | J Med Case Reports | Abscesso cerebelar por *Streptococcus intermedius* como apresentação de sarcoidose; sem relação com a indicação prevista |

---

## Informações de Comercialização no Brasil

Todos os 20 registros encontrados estão **cancelados**; não há registro válido. Listados os cinco principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 143810134 | Metronidazol | Não informada | Amebicidas, giardicidas e tricomonicidas |
| Registro 106830115 | Metroniflex | Não informada | Amebicidas, giardicidas e tricomonicidas |
| Registro 110360273 | Flagyl | Não informada | Amebicidas, giardicidas e tricomonicidas |
| Registro 129160007 | Rozex | Não informada | Outros produtos com ação na pele e mucosas |
| Registro 100850107 | Metronack | Não informada | Antiinfecciosos |

---

## Considerações de Segurança

- **Contraindicações e condições de risco (base de conhecimento do TxGNN, não texto de bula):** insuficiência hepática e doença hepática, epilepsia e doenças cerebrais, doença renal, doenças hematológicas (neutropenia, agranulocitose, leucopenia), distúrbios de coagulação, neuropatia periférica e doenças do sistema nervoso periférico, doenças do nervo óptico e das vias visuais, insuficiência cardíaca congestiva, diabetes e cetoacidose diabética, gota, doença da vesícula biliar, dermatite, meningite não infecciosa, piureter e dependência/abuso de substâncias.
- **Interações Medicamentosas** (100 interações registradas; principais):
  - **Maior gravidade:** etanol (risco de reação tipo dissulfiram).
  - **Moderadas:** paclitaxel, adalimumabe, trastuzumabe entansina, etinilestradiol, estradiol, butalbital, amiodarona, celecoxibe, amobarbital, loperamida.
  - **Menores:** abiraterona, tramadol, famotidina, salbutamol, alfuzosina, amissulprida, amitriptilina, anagrelida, propofol.

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos, a literatura é indireta e não sustenta eficácia contra *Pneumocystis*, e o mecanismo do metronidazol é incompatível com um fungo; a pontuação alta do modelo parece artefato de rede. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação e das advertências e contraindicações da bula (ANVISA), hoje ausentes.
- Verificar se há atividade in vitro/in vivo contra *Pneumocystis* antes de qualquer avanço (hoje não há base para isso).
- Reorientar a avaliação para indicações com plausibilidade maior (pôliposis em capuz, proctossigmoidite ulcerativa, úlcera vulvar de Crohn/amebiana), que exigem revisão sistemática e estudos controlados.
- Esclarecer a situação regulatória (registros cancelados) e formas farmacêuticas disponíveis.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

