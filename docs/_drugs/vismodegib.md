---
layout: default
title: Vismodegib
parent: Apenas Predição do Modelo (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vismodegib: nova indicação prevista, Câncer de pele (Skin Cancer) (nível de evidência L5). Indicação original: Antineoplásico"
monitor_inn: "vismodegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "prostate cancer/brain cancer susceptibility", "Brenner tumor", "prostate leiomyoma", "benign neoplasm of sweat gland"]
---

# Vismodegib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Vismodegibe: Do tratamento antineoplásico ao câncer de pele (carcinoma basocelular)

## Resumo em Uma Frase

Vismodegibe (ERIVEDGE) é um inibidor da via Hedgehog, registrado na ANVISA como antineoplásico.
O modelo TxGNN prevê que pode ser eficaz para **câncer de pele (Skin Cancer)**, a previsão com maior suporte de evidências entre as 10 candidatas analisadas, com **12 ensaios clínicos** e **20 publicações** apoiando esta direção.
Atenção: essa indicação corresponde, na prática, ao uso oncológico já estabelecido do fármaco (carcinoma basocelular avançado), e não a um reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Câncer de pele (Skin Cancer) |
| Pontuação de Previsão TxGNN | 99,82% |
| Nível de Evidência | L1 (conforme classificação dos dados; ver ressalva abaixo) |
| Situação no Mercado Brasileiro | ✗ Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Proceed with Guardrails |

**Ressalva sobre o nível de evidência:** os dados compilados classificam esta indicação como L1, mas nenhum ensaio de Phase 3 concluído aparece na lista. O nível reflete o fato de a indicação já ser estabelecida (estudo pivotal ERIVANCE, Phase 2, e aprovações internacionais). Pelos critérios estritos do relatório, as evidências apresentadas aqui seriam compatíveis com L2 ou inferior.

> Observação: o ranking do TxGNN apresenta outras nove candidatas. A de maior pontuação é meduloblastoma com nodularidade extensa (99,93%), mas sem ensaios ou literatura (L5). Optou-se por detalhar o câncer de pele por ter o maior volume de evidências.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o vismodegibe é um inibidor oral de pequena molécula da proteína Smoothened (SMO), que bloqueia a via de sinalização Hedgehog. A literatura revisada confirma essa descrição (PMID 24756807, 24359667).

O carcinoma basocelular (CBC) é impulsionado por sinalização Hedgehog aberrante, por perda de PTCH1 ou ativação de SMO. Ao inibir SMO, o vismodegibe atua diretamente sobre esse motor tumoral. É justamente esse o mecanismo do seu uso aprovado em CBC localmente avançado ou metastático, por isso a previsão do modelo é biologicamente coerente.

Como a indicação prevista coincide com o uso oncológico original, trata-se mais de uma confirmação do modelo do que de uma nova descoberta. Os ensaios mais interessantes exploram usos adjacentes: terapia neoadjuvante antes da cirurgia, associação com radioterapia, esquemas de dose intermitente e uso em síndromes com múltiplos CBCs.

## Evidências de Ensaios Clínicos

Foram selecionados os 10 ensaios mais relevantes, dentre os 12 identificados.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01543581](https://clinicaltrials.gov/study/NCT01543581) | Phase 2 | Concluído | 3 | Vismodegibe oral versus placebo, duplo-cego, antes da cirurgia de Mohs em CBC; amostra muito pequena limita a força da evidência |
| [NCT01835626](https://clinicaltrials.gov/study/NCT01835626) | Phase 2 | Concluído | 24 | Vismodegibe com radioterapia em CBC localmente avançado de cabeça e pescoço; avalia segurança e tolerabilidade |
| [NCT01631331](https://clinicaltrials.gov/study/NCT01631331) | Early Phase 1 | Concluído | 15 | Estudo piloto do vismodegibe como adjuvante à cirurgia em CBC esporádico |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | Recrutando | 80 | Registro prospectivo, na vida real, de vismodegibe e sonidegibe em CBC avançado ou múltiplo nos Países Baixos |
| [NCT05651828](https://clinicaltrials.gov/study/NCT05651828) | Early Phase 1 | Recrutando | 34 | Compara quatro esquemas de dose (dois personalizados intermitentes, um intermitente fixo e um contínuo) em CBC avançado |
| [NCT02690948](https://clinicaltrials.gov/study/NCT02690948) | Phase 1/2 | Concluído | 16 | Pembrolizumabe, com ou sem vismodegibe, em CBC irressecável ou metastático |
| [NCT02694224](https://clinicaltrials.gov/study/NCT02694224) | Phase 2 | Desconhecido | 40 | Randomizado: vismodegibe somado à quimioterapia neoadjuvante padrão em câncer de mama triplo-negativo (fora da indicação de pele) |
| [NCT06357988](https://clinicaltrials.gov/study/NCT06357988) | Phase 2 | Ativo, não recrutando | 34 | NCI-MATCH subprotocolo T: tumores (exceto CBC) com mutações em SMO ou PTCH1 |
| [NCT01071564](https://clinicaltrials.gov/study/NCT01071564) | Phase 1 | Encerrado | 13 | Vismodegibe com inibidor de Notch em câncer de mama avançado; encerrado com poucos participantes |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Ativo, não recrutando | 6.452 | NCI-MATCH, estudo guarda-chuva de terapia guiada por testes genéticos; relação apenas tangencial |

Nota: alguns ensaios (câncer de mama, MATCH) não são específicos para câncer de pele e entram apenas como contexto do uso do fármaco.

## Evidências da Literatura

Foram selecionadas as 10 publicações mais relevantes, priorizando diretrizes e revisões (não há RCT na lista).

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Diretriz | Eur J Cancer | Diretriz europeia consensual atualizada sobre diagnóstico e tratamento do CBC, com classificação em "fácil de tratar" e "difícil de tratar" |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Diretriz | Eur J Cancer | Diretrizes europeias interdisciplinares anteriores para o CBC |
| [22679179](https://pubmed.ncbi.nlm.nih.gov/22679179/) | 2012 | Revisão | Clin Cancer Res | Aprovação do vismodegibe pela FDA em CBC metastático ou localmente avançado, baseada em estudo Phase 2 não randomizado |
| [22653209](https://pubmed.ncbi.nlm.nih.gov/22653209/) | 2012 | Revisão | Nat Rev Drug Discov | Descrição do vismodegibe como inibidor oral da via Hedgehog e base de sua aprovação |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Revisão | Cell | Vismodegibe e sonidegibe inibem SMO; ambos aprovados em CBC localmente avançado, e o vismodegibe também em CBC metastático |
| [24756807](https://pubmed.ncbi.nlm.nih.gov/24756807/) | 2014 | Revisão | Recent Results Cancer Res | Vismodegibe liga-se ao SMO; via Hedgehog também implicada em meduloblastoma e outros tumores |
| [23719880](https://pubmed.ncbi.nlm.nih.gov/23719880/) | 2013 | Revisão | Am J Health Syst Pharm | Revisão de farmacologia, eficácia, eventos adversos, custo e lugar na terapia |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Revisão | Int J Mol Sci | Revisão abrangente do CBC, com aspectos moleculares e mecanismos de resistência a terapias sistêmicas |
| [24359667](https://pubmed.ncbi.nlm.nih.gov/24359667/) | 2014 | Revisão | Actas Dermosifiliogr | Vismodegibe foi o primeiro inibidor seletivo da via Hedgehog aprovado pela FDA para CBC avançado |
| [26833519](https://pubmed.ncbi.nlm.nih.gov/26833519/) | 2016 | Revisão | Clin Med (Lond) | Visão geral do câncer de pele não melanoma, incluindo subtipos e opções terapêuticas |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101000664 (cancelado) | ERIVEDGE | Não informada | Antineoplásico |

O único registro do vismodegibe na ANVISA consta como **cancelado**, portanto não há produto com registro válido no Brasil nos dados compilados. A disponibilidade deve ser verificada antes de qualquer iniciativa.

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor da via Hedgehog/SMO), e não citotóxico convencional |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte a bula; em geral, avaliar função hepática e renal, peso e eletrólitos (por causa de espasmos musculares), além de teste de gravidez antes e durante o tratamento |
| Proteção no Manuseio | Consulte a bula e os regulamentos locais de manuseio de antineoplásicos orais; o risco embriofetal exige cuidados com cápsulas |

## Considerações de Segurança

- **Advertências principais (segundo a análise dos dados compilados):** toxicidade embriofetal (exige contracepção), espasmos musculares, alopecia, disgeusia (alteração do paladar) e perda de peso. Em crianças, há preocupação com toxicidade na placa de crescimento ósseo, relevante para populações pediátricas, como nos casos descritos em xeroderma pigmentoso.
- **Interações medicamentosas:** foram identificadas 56 interações no total. Entre as listadas, a de nível **moderado** é com a **claritromicina**. As demais exibidas são de nível **leve**, em sua maioria com fármacos que reduzem a acidez gástrica: inibidores de bomba de prótons (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina) e antiácidos (hidróxido de alumínio, carbonato de cálcio, óxido/hidróxido/carbonato de magnésio, magaldrato, citrato e bicarbonato de sódio).

As advertências e contraindicações da bula da ANVISA não estavam disponíveis nos dados compilados; consulte a bula para as informações oficiais de segurança.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo é sólido (inibição de SMO em tumor dependente de Hedgehog) e há ensaios de Phase 2, diretrizes e revisões na área. Contudo, a indicação coincide com o uso oncológico original, o registro brasileiro está cancelado e não há dados de bula, então a decisão exige salvaguardas.

**Para prosseguir, é necessário:**
- Verificar a situação regulatória e a disponibilidade real do produto no Brasil (registro cancelado).
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna considerada bloqueante para a triagem de segurança.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Definir um plano de gestão de risco: programa de contracepção e prevenção de gravidez, monitoramento de espasmos musculares, peso e paladar, e cautela com população pediátrica.
- Revisar o nível de evidência, já que nenhum Phase 3 concluído consta na lista e os ensaios Phase 2 têm amostras pequenas.

**Observação sobre as demais candidatas:** xeroderma pigmentoso (99,91%) tem apenas relatos de caso de vismodegibe em CBCs múltiplos (L4), sendo uma questão de pesquisa; meduloblastoma com nodularidade extensa tem plausibilidade mecanística (subgrupo SHH), mas sem evidência (L5, Hold). As demais (ictiose epidermolítica anular, epidermólise bolhosa simples, suscetibilidade a câncer de próstata/cérebro, tumor de Brenner, carcinoma adenocístico cutâneo, leiomioma de próstata e neoplasia benigna de glândula sudorípara) dependem apenas do escore do modelo e permanecem em Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

