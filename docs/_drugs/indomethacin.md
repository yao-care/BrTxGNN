---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

Usando o skill `txgnn-pipeline` como contexto de pipeline. Gerando o relatório de avaliação de reposicionamento agora.

---

# Indomethacin: De Artrite Reumatoide para Artrite Idiopática Juvenil

## Resumo em Uma Frase

Indomethacin é um anti-inflamatório não-esteroidal (AINE) clássico com décadas de uso documentado no tratamento de artrite reumatoide, espondilite anquilosante e gota aguda em adultos. O modelo TxGNN avaliou 10 indicações candidatas; a com maior respaldo evidencial é a **Artrite Idiopática Juvenil (Juvenile Idiopathic Arthritis)**, com pontuação de **99,84%** e **20 publicações** na literatura — incluindo 1 ensaio clínico duplo-cego. O fármaco não possui registros na ANVISA, mas seu mecanismo COX-1/2 é diretamente relevante para a fisiopatologia inflamatória da JIA.

---

## Panorama das 10 Indicações Previstas

> Esta é uma avaliação multi-indicação (`TW-DB00328-multi`). A tabela abaixo resume todas as indicações; o restante do relatório aprofunda a indicação com melhor evidência clínica (rank 8 — JIA).

| Ranking | Indicação | Score TxGNN | Nível de Evidência | Recomendação |
|---------|-----------|:-----------:|:-----------------:|:------------:|
| 1 | Brachydactyly-syndactyly syndrome | 99,97% | L5 | Hold |
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99,97% | L5 | Hold |
| 3 | Acromesomelic dysplasia, Hunter-Thompson type | 99,89% | L5 | Hold |
| 4 | WHIM syndrome | 99,88% | L5 | Hold |
| 5 | Brachyolmia-amelogenesis imperfecta syndrome | 99,87% | L5 | Hold |
| 6 | Brachyolmia | 99,87% | L5 | Hold |
| 7 | Myosclerosis | 99,86% | L5 | Hold |
| **8** | **Artrite Idiopática Juvenil** ⭐ | **99,84%** | **L2** | **Proceed with Guardrails** |
| 9 | RF+ polyarticular juvenile idiopathic arthritis | 99,84% | L5 | Hold |
| 10 | Rheumatoid nodulosis | 99,83% | L4 | Research Question |

> ⚠️ **Nota sobre ranks 1–7 e 9:** As indicações de topo (doenças raras de desenvolvimento ósseo/malformações congênitas) receberam scores altos por similaridade topológica no grafo de conhecimento, sem base biológica para COX-inibição. São consideradas **falsos positivos** do modelo neste contexto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Artrite reumatoide, espondilite anquilosante e gota aguda (uso global estabelecido; sem registro ANVISA) |
| Nova Indicação Prevista | Artrite Idiopática Juvenil (Juvenile Idiopathic Arthritis) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Indomethacin atua como inibidor potente e não-seletivo de COX-1 e COX-2, enzimas responsáveis pela síntese de prostaglandinas — em especial a PGE₂. A inibição dessas vias reduz diretamente a inflamação sinovial, o edema articular e a dor, que são os principais alvos terapêuticos na Artrite Idiopática Juvenil.

A JIA é a doença reumática crônica mais comum na infância, caracterizada por inflamação sinovial persistente mediada por prostaglandinas e citocinas. A PGE₂ está altamente expressa nas articulações inflamadas de crianças com JIA, o que torna os AINEs uma classe terapêutica com fundamento fisiopatológico sólido. De fato, as diretrizes do ACR 2019 ainda incluem AINEs como opção de controle inicial de sintomas nessa condição.

O uso específico de indomethacin em artrite juvenil é documentado desde a década de 1960. Embora hoje sejam preferidos AINEs com melhor perfil de tolerabilidade pediátrica (como naproxeno e ibuprofeno), o indomethacin permanece referência farmacológica relevante para o mecanismo anti-inflamatório nessa indicação — o que confere base biológica clara à previsão do TxGNN.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos registrados relacionados ao uso de Indomethacin especificamente para Artrite Idiopática Juvenil.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|:---:|------|-----------|-------------------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT duplo-cego | South African Medical Journal | Ensaio cruzado em 30 crianças com artrite crônica juvenil; indomethacin e cetoprofeno foram seguros e eficazes como analgésicos e anti-inflamatórios, com indomethacin emergindo como fármaco preferido |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Review | Balkan Medical Journal | Revisão abrangente da JIA — doença reumática crônica mais frequente na infância; descreve subgrupos clínicos, manifestações sistêmicas e modalidades terapêuticas, incluindo AINEs |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Review | Drugs | AINEs como naproxeno, tolmetina, ibuprofeno e indomethacin listados como tratamento padrão para ARJ; discute progressão para DMARDs e corticosteroides |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | British Journal of Rheumatology | AINEs em doenças reumáticas pediátricas: indomethacin indicado para febre sistêmica na AJC, porém com maior toxicidade que alternativas para controle articular; diclofenaco e naproxeno preferidos |
| [22573189](https://pubmed.ncbi.nlm.nih.gov/22573189/) | 2012 | Review | Swiss Medical Weekly | JIA sistêmica (doença de Still): curso crônico, impacto familiar e desafio com imunossupressores convencionais; contextualiza papel dos AINEs no manejo inicial |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Review | Clinical Pharmacokinetics | Farmacocinética clínica dos AINEs em artrite juvenil; aborda parâmetros PK específicos de indomethacin em crianças e implicações para dosagem |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | Estudo clínico | Arzneimittel-Forschung | Terapia de longo prazo com indomethacin em ARJ e doença de Still; um dos primeiros registros de uso pediátrico prolongado do fármaco |
| [28086918](https://pubmed.ncbi.nlm.nih.gov/28086918/) | 2017 | Coorte retrospectiva | Pediatric Rheumatology Online Journal | JIA oligoarticular com monoartrite atípica em articulações incomuns; demonstra espectro clínico e necessidade de controle anti-inflamatório individualizado |
| [7417361](https://pubmed.ncbi.nlm.nih.gov/7417361/) | 1980 | Coorte comparativa | Arthritis and Rheumatism | Comparação de ARJ entre EUA e URSS; evolução semelhante em ambos os países independente do esquema terapêutico, com uso documentado de indomethacin |
| [4251212](https://pubmed.ncbi.nlm.nih.gov/4251212/) | 1971 | Review | Clinical Orthopaedics | Reavaliação crítica da ARJ: abordagem diagnóstica e terapêutica da época, incluindo indomethacin como opção disponível |

---

## Informações de Comercialização no Brasil

Indomethacin **não possui registros ativos na ANVISA**. O fármaco não está comercializado no mercado brasileiro com base nos dados disponíveis (consulta realizada em 2026-03-09, 0 registros encontrados).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ Nota importante: Indomethacin tem perfil de tolerabilidade reconhecidamente inferior a outros AINEs em uso pediátrico (maior incidência de efeitos gastrointestinais e no SNC). Este aspecto deve ser avaliado cuidadosamente antes de qualquer uso em crianças com JIA.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há evidências históricas consistentes do uso de indomethacin em artrite juvenil — incluindo 1 RCT duplo-cego e múltiplas revisões clínicas com citação direta do fármaco — e o mecanismo COX-1/2 é biologicamente coerente com a fisiopatologia inflamatória da JIA. As diretrizes contemporâneas (ACR 2019) ainda reconhecem os AINEs como opção terapêutica inicial, sustentando a relevância clínica da previsão.

**Para prosseguir, é necessário:**

- **Segurança pediátrica:** Obter dados completos de contraindicações, advertências e interações medicamentosas (bula oficial); indomethacin tem perfil de tolerabilidade inferior a outros AINEs em crianças
- **Registro regulatório:** Verificar ausência de registro na ANVISA antes de qualquer uso ou estudo clínico no Brasil; avaliar necessidade de importação ou registro específico
- **Atualização de evidências:** Os estudos disponíveis são majoritariamente de 1967–1993; uma revisão sistemática atualizada é necessária para confirmar posicionamento frente a alternativas modernas (naproxeno, celecoxib, biológicos)
- **Indicação secundária a monitorar:** Rheumatoid nodulosis (rank 10) apresenta nível L4 e recomendação "Research Question" — pode ser candidata a estudo exploratório de baixo custo
- **Avaliação dos ranks 1–7 e 9:** As 8 previsões com recomendação "Hold" envolvem doenças raras de desenvolvimento ósseo/congênitas sem relação biológica com COX-inibição; devem ser descartadas como artefatos de topologia do grafo do TxGNN
---

