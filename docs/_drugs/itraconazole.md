---
layout: default
title: Itraconazole
parent: Apenas Predição do Modelo (L5)
nav_order: 378
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Itraconazole: nova indicação prevista, Pneumocistose (Pneumocystosis) (nível de evidência L5). Indicação original: Antimicóticos sistêmicos"
monitor_inn: "ITRACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Itraconazol: De antimicótico sistêmico a pneumocistose
{: .text-alpha }

## Resumo em Uma Frase

Itraconazol é um antifúngico azólico, originalmente registrado na ANVISA como antimicótico sistêmico.
O modelo TxGNN prevê que pode ser eficaz para **Pneumocistose (Pneumocystosis)**, mas atualmente há **0 ensaios clínicos** e **20 publicações** associadas a esta direção, a maioria revisões e relatos de casos, sem evidência direta de eficácia. Os dados compilados indicam ainda que a previsão tem baixa plausibilidade mecanística.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimicóticos sistêmicos |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 0,9934 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 13 de 49) |
| Número de Registros | 49 (ativos: 13) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo o conhecimento geral da classe, o itraconazol é um antifúngico azólico que inibe a lanosterol 14-alfa-desmetilase (CYP51), bloqueando a síntese de ergosterol na membrana fúngica. Esta descrição é inferida do conhecimento da classe, e não dos dados fornecidos.

A relação entre a indicação original (infecções fúngicas sistêmicas) e a nova indicação (pneumocistose, infecção pulmonar oportunista em imunossuprimidos) é, em princípio, de proximidade clínica: ambas ocorrem em pacientes imunocomprometidos, como os com HIV, transplantados e neutropênicos. É provável que a pontuação elevada do TxGNN reflita essa proximidade na rede de conhecimento, e não um vínculo mecanístico real.

Há uma limitação importante: o *Pneumocystis jirovecii* não possui ergosterol na membrana, utilizando colesterol, de modo que o alvo clássico dos azólicos não é plausível neste organismo. Um estudo de caracterização da enzima Erg11 do *Pneumocystis carinii* (PMID 12606318) também aponta que esse organismo é intrinsecamente resistente aos antifúngicos azólicos. Portanto, a previsão deve ser interpretada com cautela.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Não há estudo que teste diretamente o itraconazol no tratamento da pneumocistose. A literatura listada é, em sua maioria, contextual (infecções oportunistas em imunossuprimidos). Seleção das publicações mais relevantes:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT (fase III, duplo-cego, controlado por placebo) | HIV Medicine | Itraconazol em cápsulas como profilaxia de infecções fúngicas profundas em pacientes com HIV imunodeficientes; o resumo disponível não informa resultados nem trata da pneumocistose |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Estudo de mecanismo | Am J Respir Cell Mol Biol | Clonagem da Erg11 de *P. carinii*; o organismo é intrinsecamente resistente aos azólicos |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisão | Drugs | Terapia e profilaxia de infecções protozoárias sistêmicas, incluindo *P. carinii* |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisão | Clin Pharmacokinet | Penetração de anti-infecciosos, incluindo antifúngicos, no fluido de revestimento epitelial pulmonar |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisão | BMJ Clin Evid | Profilaxia primária e secundária de infecções oportunistas em HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisão | Clin Infect Dis | Profilaxia antimicrobiana na neutropenia febril; o sulfametoxazol-trimetoprima é altamente eficaz contra pneumonia por *P. carinii* |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisão | Semin Respir Infect | Infecções após transplante de pulmão |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revisão | Curr Clin Top Infect Dis | Profilaxia e tratamento de infecções em receptores de transplante de medula óssea |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Coorte | Transplant Proc | Infecções fúngicas invasivas após transplante renal |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Série de casos | Medicine | Histoplasmose disseminada na AIDS: achados clínicos, diagnóstico e tratamento |

## Informações de Comercialização no Brasil

Todos os 13 registros encontram-se válidos. Os cinco principais:

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431188 | ITRACONAZOL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 102350382 | ITRALEX | EMS S/A | Ativo |
| 102351205 | ITRACONAZOL | EMS S/A | Ativo |
| 105830937 | ITRACONAZOL | GERMED FARMACEUTICA LTDA | Ativo |
| 110390215 | ITRACONAZOL | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Ativo |
| 112360028 | SPORANOX | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 118190377 | ITRACONAZOL | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 118190470 | FUNOK | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 125680170 | ITRACONAZOL | PRATI DONADUZZI & CIA LTDA | Ativo |
| 135690703 | ITRASPOR | EMS SIGMA PHARMA LTDA | Ativo |
| 154230009 | TRAXONOL | GEOLAB INDÚSTRIA FARMACÊUTICA S/A | Ativo |
| 154230260 | ITRACONAZOL | GEOLAB INDÚSTRIA FARMACÊUTICA S/A | Ativo |
| 167730588 | ITRACONAZOL | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100380078 | ICONAZOL | BRASTERAPICA PHARMACEUTICA LTDA. | Cancelado |
| 100430631 | EUTRAMIX | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100470286 | ITRAHEXAL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100890213 | VOLFAX | MERCK S/A | Cancelado |
| 102700106 | TRACOZON | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 103700450 | FUNGONAX | LABORATÓRIO TEUTO BRASILEIRO S/A | Cancelado |
| 103920095 | TRACOZOL | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Cancelado |
| 103940443 | TRANAZOL | LABORATÓRIO AMERICANO DE FARMACOTERAPIA S/A | Cancelado |
| 104041933 | TRACONAX | LUPER INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 104080072 | ITRACOTAN | ROYTON QUÍMICA FARMACÊUTICA LTDA | Cancelado |
| 104300031 | MICONAL | DIFFUCAP - CHEMOBRÁS QUÍMICA E FARMACÊUTICA LTDA | Cancelado |
| 104400097 | SPOZOL | CELLERA FARMACEUTICA S.A. | Cancelado |
| 104650212 | NEO ITRAX | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 105350130 | GLOBO ITRACONAZOL | LABORATÓRIO GLOBO SA | Cancelado |
| 105730215 | TRACONAL | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Cancelado |
| 105830155 | MONITRAX | GERMED FARMACEUTICA LTDA | Cancelado |
| 105830175 | ITRASPOR | GERMED FARMACEUTICA LTDA | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

## Considerações de Segurança

- **Contraindicações (inferidas do grafo de conhecimento TxGNN/PrimeKG, não do texto da bula)**: síndrome do QT longo (inclusive familiar), torsades de pointes, insuficiência cardíaca congestiva, miocardiopatias, doença arterial coronariana e isquemia miocárdica, doença hepática e lesão hepática induzida por fármacos, doença renal e insuficiência renal, doença pulmonar obstrutiva crônica, neuropatia periférica, deficiência de potássio, acloridria, perda auditiva e distúrbios visuais.
- **Interações Medicamentosas** (100 interações registradas; exemplos entre as principais):
  - **Graves (Major)**: loperamida, triancinolona, budesonida.
  - **Moderadas**: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol (redução da acidez gástrica pode diminuir a absorção), hidrocortisona, dexametasona, betametasona, alosetrona, aprepitanto.
  - **Leves**: metformina, pioglitazona, clorpropamida, anfotericina B.

As advertências e contraindicações oficiais da bula da ANVISA não estavam disponíveis nos dados compilados; consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia apenas no modelo (L5): não há ensaios clínicos, e a literatura é contextual. Além disso, o *Pneumocystis* não possui ergosterol e é intrinsecamente resistente aos azólicos, o que enfraquece o racional mecanístico. Há também alternativas estabelecidas (por exemplo, sulfametoxazol-trimetoprima), e o medicamento é comercializado no Brasil, com 13 registros válidos de 13.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) obtidos do DrugBank.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Evidência pré-clínica ou clínica direta de atividade do itraconazol contra *Pneumocystis*, que justifique reconsiderar a decisão.
- Avaliação do perfil de segurança (QT, hepático, cardíaco e interações) em pacientes imunossuprimidos, população-alvo típica.
- Esclarecimento da situação regulatória, já que não há registro vigente no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

