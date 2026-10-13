---
layout: default
title: Methylergometrine
parent: Apenas Predição do Modelo (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Methylergometrine
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

# Metilergometrina: De ocitócico não hormonal para hipertricose

## Resumo em Uma Frase

A metilergometrina (methylergometrine) é um alcaloide semissintético do ergot, originalmente registrado no Brasil como **ocitócico não hormonal**.
O modelo TxGNN prevê que pode ser eficaz para **hipertricose (hypertrichosis)**, mas **não há ensaios clínicos nem publicações** que apoiem esta previsão. Trata-se apenas de uma previsão do modelo, sem plausibilidade mecanística identificada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Ocitócicos não hormonais |
| Nova Indicação Prevista | Hipertricose (hypertrichosis) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este fármaco. Segundo informações conhecidas, a metilergometrina é um alcaloide semissintético do ergot que age sobre a musculatura lisa uterina e sobre receptores serotoninérgicos e alfa-adrenérgicos. Sua utilização original está ligada à contração uterina.

**A previsão não parece razoável do ponto de vista biológico.** Não há vínculo mecanístico claro entre o fármaco e a hipertricose. A pontuação elevada do TxGNN parece refletir proximidade na rede de conhecimento, e não uma justificativa biológica real. A hipertricose é, aliás, um efeito adverso reconhecido de outros agentes (como o minoxidil), e não um alvo terapêutico desta classe de fármacos.

Outras previsões do mesmo modelo seguem o mesmo padrão. Para as demais indicações previstas, a avaliação é a seguinte:

- **Enxaqueca (migraine disorder, 99,84%)**: é a única com plausibilidade biológica. A metilergometrina é o metabólito ativo da metisergida, antiga profilaxia da enxaqueca. Há apenas duas publicações indiretas (nível L4) e nenhum dado clínico do fármaco nessa condição.
- **Hipertensão pulmonar (99,86%)**: a previsão é implausível e levanta preocupação de segurança, pois a atividade vasoconstritora e serotoninérgica tende a piorar o tônus vascular pulmonar.
- **Enxaqueca com aura do tronco encefálico (99,77%)**: vasoconstritores costumam ser desaconselhados nessa condição, por risco isquêmico teórico.
- **Demais previsões** (hipertricose universal congênita tipo Ambras, síndromes malformativas, anomalia de haste capilar, cardiopatia cifoescoliótica, síndrome nefrogênica de antidiurese inapropriada): sem mecanismo plausível e com nível L5.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (hipertricose), atualmente não há literatura relacionada. As únicas publicações encontradas referem-se à indicação secundária de enxaqueca e são indiretas:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Revisão | Cephalalgia | Revisão histórica da metisergida na enxaqueca, sintetizada a partir do LSD e desenvolvida como fármaco antisserotonina |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Revisão | Circulation | Compara o potencial vasoconstritor coronariano de antienxaquecosos (ergotamina, di-hidroergotamina, metisergida e seu metabólito metilergometrina, triptanos) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104970126 (cancelado) | ERGOMETRIN | Não informada | Ocitócicos não hormonais |

## Considerações de Segurança

- **Contraindicações (base de conhecimento do TxGNN, não bula)**: o grafo de conhecimento associa o fármaco a doenças como hipertensão, epilepsia, doença renal, doença hepática, doença da vesícula biliar, AVC e doenças cerebrovasculares, infarto cerebral, arteriosclerose obliterante, síndrome HELLP e piureter.
- **Interações medicamentosas**: foram registradas 92 interações. Entre as de nível **grave (Major)** estão isometepteno, epinefrina (incluindo formas oftálmica e tópica), lorcasserina, claritromicina e efedrina (incluindo nasal). Entre as de nível **moderado** estão doxiciclina, tetraciclina, minociclina, aprepitanto, dexametasona, cimetidina, eluxadolina, clotrimazol, miconazol, glicerol fenilbutirato, metreleptina e troglitazona.
- **Riscos de classe**: vasoconstrição, efeitos coronarianos e, com uso prolongado de ergóticos, fibrose e valvulopatia.

As advertências e contraindicações oficiais da bula não estavam disponíveis; consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hipertricose é apenas um resultado do modelo (L5), sem ensaios, sem literatura e sem mecanismo plausível. Além disso, o único registro no Brasil está cancelado e há preocupações de segurança relevantes.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (MOA) do fármaco.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem esses dados.
- Caso se deseje explorar alguma direção, a enxaqueca é a única com racional biológico (via metisergida). Seria necessária uma revisão de literatura específica e uma avaliação de segurança vascular, tratando-a como questão de pesquisa e não como candidata a desenvolvimento.
- Esclarecer a situação regulatória, já que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

