---
layout: default
title: Metronidazole
parent: Apenas Predição do Modelo (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Metronidazole: nova indicação prevista, Pneumocistose (Pneumocystosis) (nível de evidência L5). Indicação original: Amebicidas, giardicidas e tricomonicidas"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
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

## Metronidazol: De antiprotozoário e antibacteriano para pneumocistose (previsão com evidência muito fraca)
{: .text-alpha }

## Resumo em Uma Frase

Metronidazol é um antimicrobiano nitroimidazólico, registrado no Brasil como amebicida, giardicida e tricomonicida, e também como antiinfeccioso e produto de ação em pele e mucosas.
O modelo TxGNN prevê que pode ser eficaz para **pneumocistose (Pneumocystosis)**, mas não há **nenhum ensaio clínico** e a literatura recuperada (**10 publicações**) é composta por revisões gerais e relatos de caso, sem demonstrar eficácia do fármaco contra *Pneumocystis*.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Amebicidas, giardicidas e tricomonicidas |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 0,9999 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 41 de 141) |
| Número de Registros | 141 (ativos: 41) |
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

Foram encontrados 20 registros válidos; o medicamento está comercializado. Listados os cinco principais:

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100410129 | ENDONIDAZOL | FRESENIUS KABI BRASIL LTDA | Ativo |
| 100410158 | METRONIDAZOL | FRESENIUS KABI BRASIL LTDA | Ativo |
| 100850107 | METRONACK | LABORATORIOS B. BRAUN S/A | Ativo |
| 103110119 | METRONIDAZOL | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Ativo |
| 103110148 | HIDAZOL | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Ativo |
| 103110154 | METRONIDAZOL | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Ativo |
| 103460020 | METRONIDAZOL | BEKER PRODUTOS FÁRMACO HOSPITALARES LTDA | Ativo |
| 103700007 | COLPATRIN | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700071 | HELMIZOL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700664 | METRONIDAZOL + NISTATINA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700714 | METRONIDAZOL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103870046 | METRONIDAZOL | HYPOFARMA - INSTITUTO DE HYPODERMIA E FARMÁCIA LTD | Ativo |
| 103900059 | COLPISTAR | FARMOQUÍMICA S/A | Ativo |
| 104910064 | METRONIDAZOL | JP INDUSTRIA FARMACEUTICA S/A | Ativo |
| 105710103 | FLAGIMAX | BELFAR LTDA | Ativo |
| 105710140 | METRONIDAZOL | BELFAR LTDA | Ativo |
| 106830115 | METRONIFLEX | BAXTER HOSPITALAR LTDA | Ativo |
| 107150089 | TRICOMAX | CAZI QUIMICA FARMACEUTICA INDUSTRIA E COMERCIO LTD | Ativo |
| 110360273 | FLAGYL | HEMAFARMA COM E IND FARMACEUTICA LTDA | Ativo |
| 110390103 | FURP-METRONIDAZOL | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Ativo |
| 110850014 | NIDAZOFARMA | FARMACE INDÚSTRIA QUÍMICO-FARMACÊUTICA CEARENSE LT | Ativo |
| 118190327 | METRONIDAZOL | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 118190446 | MEFLAGIN | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 125680043 | METRONIDAZOL | PRATI DONADUZZI & CIA LTDA | Ativo |
| 125680044 | METRONIDAZOL + NISTATINA | PRATI DONADUZZI & CIA LTDA | Ativo |
| 125680182 | METRONIDAZOL | PRATI DONADUZZI & CIA LTDA | Ativo |
| 129160007 | ROZEX | GALDERMA BRASIL LTDA | Ativo |
| 135640005 | GYNOTRAN | EXELTIS LABORATORIO FARMACEUTICO LTDA | Ativo |
| 135640013 | METRONIDAZOL + NITRATO DE MICONAZOL | EXELTIS LABORATORIO FARMACEUTICO LTDA | Ativo |
| 143810134 | METRONIDAZOL | CIMED INDUSTRIA S.A | Ativo |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

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
- Não há ensaios clínicos, a literatura é indireta e não sustenta eficácia contra *Pneumocystis*, e o mecanismo do metronidazol é incompatível com um fungo; a pontuação alta vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Além disso, o medicamento está comercializado no Brasil, com 20 registros válidos.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação e das advertências e contraindicações da bula (ANVISA), hoje ausentes.
- Verificar se há atividade in vitro/in vivo contra *Pneumocystis* antes de qualquer avanço (hoje não há base para isso).
- Reorientar a avaliação para indicações com plausibilidade maior (pôliposis em capuz, proctossigmoidite ulcerativa, úlcera vulvar de Crohn/amebiana), que exigem revisão sistemática e estudos controlados.
- Esclarecer a situação regulatória e formas farmacêuticas disponíveis.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

