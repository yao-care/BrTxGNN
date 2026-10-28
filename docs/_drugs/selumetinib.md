---
layout: default
title: Selumetinib
parent: Apenas Predição do Modelo (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Selumetinib: nova indicação prevista, Lentiginose generalizada familiar (familial generalized lentiginosis) (nível de evidência L5). Indicação original: Agentes antineoplásicos e imunomoduladores"
monitor_inn: "selumetinib"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "rhabdoid tumor", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "acromelanosis", "Moynahan syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "peripheral nerve schwannoma", "trigeminal schwannoma"]
---

# Selumetinib
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

## Selumetinibe: De agente antineoplásico e imunomodulador a lentiginose generalizada familiar
{: .text-alpha }

## Resumo em Uma Frase

Selumetinibe (KOSELUGO) é um inibidor de MEK registrado na ANVISA na categoria "agentes antineoplásicos e imunomoduladores".
O modelo TxGNN prevê que pode ser eficaz para **lentiginose generalizada familiar (familial generalized lentiginosis)**, mas, para esta indicação, **não há ensaios clínicos nem publicações** nos dados compilados; a previsão é puramente computacional.

Observação: entre as 10 previsões, a que reúne mais evidências é **schwannoma de nervo periférico** (3 ensaios clínicos e 6 publicações). Ela é apresentada abaixo como referência complementar.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos e imunomoduladores |
| Nova Indicação Prevista | Lentiginose generalizada familiar (familial generalized lentiginosis) |
| Pontuação de Previsão TxGNN | 0,9996 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, selumetinibe é um inibidor de MEK1/2 da via RAS-RAF-MEK-ERK, usado em tumores ligados a essa via, e mecanisticamente pode ser aplicável a doenças com desregulação da via MAPK.

Síndromes de lentiginose pigmentar frequentemente envolvem desregulação da via RAS/MAPK (biologia semelhante às RASopatias), de modo que a inibição de MEK é plausível. Ainda assim, não foram recuperados ensaios nem literatura, e a pontuação elevada do TxGNN é apenas uma previsão computacional.

Outras previsões do ranking seguem o mesmo padrão: várias síndromes pigmentares ou raras (acromelanose, síndrome de Moynahan, entre outras) têm justificativa mecanística fraca ou inexistente. Já o **schwannoma de nervo periférico** tem justificativa mais sólida: schwannomas associados à NF2 e à NF1 envolvem perda de merlina/neurofibromina e ativação da via RAS-RAF-MEK-ERK.

## Evidências de Ensaios Clínicos

Para lentiginose generalizada familiar, atualmente não há ensaios clínicos relacionados registrados.

Para referência, ensaios das previsões com mais evidências:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03095248](https://clinicaltrials.gov/study/NCT03095248) | Phase 2 | Encerrado (terminado) | 10 | Selumetinibe em tumores relacionados à NF2 (schwannoma). Encerrado precocemente, com poder limitado; sem conclusão de eficácia nos dados disponíveis |
| [NCT07707947](https://clinicaltrials.gov/study/NCT07707947) | Phase 2 | Ainda não recrutando | 20 | Estudo de braço único de inibidor de MEK1/2 (selumetinibe) em schwannomatose relacionada à NF2; sem resultados |
| [NCT07713745](https://clinicaltrials.gov/study/NCT07713745) | Phase 2 | Ainda não recrutando | 200 | Plataforma adaptativa PRIME-NF2 em schwannomatose NF2; papel do selumetinibe não especificado; sem resultados |
| [NCT03155620](https://clinicaltrials.gov/study/NCT03155620) | Phase 2 | Ativo, sem recrutamento | 1377 | Pediatric MATCH, triagem molecular em tumores pediátricos (inclui tumor rabdoide); selumetinibe é um dos braços, sem dados de eficácia específicos |

## Evidências da Literatura

Para lentiginose generalizada familiar, atualmente não há literatura relacionada.

Literatura das previsões relacionadas (schwannoma e tumor rabdoide):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37906356](https://pubmed.ncbi.nlm.nih.gov/37906356/) | 2023 | Revisão | Current Oncology Reports | Manejo de tumores do sistema nervoso na neurofibromatose; inibidores de MEK mostraram benefício |
| [37046591](https://pubmed.ncbi.nlm.nih.gov/37046591/) | 2023 | Diretriz de especialistas | Cancers | Recomendações EURACAN para tumores de nervos periféricos e cranianos; evidência escassa pela raridade |
| [38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/) | 2023 | Relato de caso | Mol Ther Methods Clin Dev | Resposta parcial ao selumetinibe em ependimoma associado à NF2 |
| [38216572](https://pubmed.ncbi.nlm.nih.gov/38216572/) | 2024 | Pré-clínico | Nature Communications | Interações entre supressores tumorais da NF1/NF2 na desdiferenciação de tumores de células de Schwann e resistência ao tratamento |
| [25638158](https://pubmed.ncbi.nlm.nih.gov/25638158/) | 2015 | Pré-clínico | Oncotarget | A via MAPK é alvo terapêutico em tumores teratoides/rabdoides atípicos após disrupção de LIN28 |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116180285 (cancelado) | KOSELUGO | Não informada | Agentes antineoplásicos e imunomoduladores |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de MEK1/2) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 84 interações, com 20 listadas nos dados compilados.
  - **Maior gravidade (Major)**: aprepitanto, dexametasona, claritromicina e cobicistate.
  - **Gravidade moderada**: ácido acetilsalicílico, cimetidina, metreleptina, clotrimazol, fenilbutirato de glicerol, troglitazona, deferasirox, além de antitrombóticos/antiagregantes (abciximabe, antitrombina III, apixabana, dipiridamol, betrixabana, bivalirudina, cangrelor, caplacizumabe e cilostazol).
  - Atenção especial a inibidores/indutores de enzimas metabólicas e a combinações com antitrombóticos (risco aditivo de sangramento).

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para lentiginose generalizada familiar, a evidência é apenas a previsão do modelo (L5), sem ensaios nem literatura. O registro brasileiro está cancelado, e não há dados de bula.
- A indicação com evidência mais avançada, schwannoma de nervo periférico (L3), segue como questão de pesquisa: o único ensaio com selumetinibe nessa área foi encerrado com 10 participantes, sem resultados fornecidos.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA (advertências e contraindicações) e esclarecer a situação do registro cancelado.
- Complementar os dados do mecanismo de ação.
- Buscar evidências específicas para lentiginose generalizada familiar (relatos de caso, estudos pré-clínicos).
- Acompanhar os resultados dos estudos de fase 2 em NF2 e avaliar priorizar o schwannoma como indicação-alvo.
- Avaliar compatibilidade de via de administração e formas farmacêuticas disponíveis.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

