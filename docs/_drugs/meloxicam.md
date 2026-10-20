---
layout: default
title: Meloxicam
parent: Apenas Predição do Modelo (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Meloxicam: nova indicação prevista, Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasi… (nível de evidência L5). Indicação original: Artrite reumatoide, osteoartrite e artrite idio…"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
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

# Meloxicam: De artrite reumatoide e osteoartrite para a síndrome de displasia acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Meloxicam é um anti-inflamatório não esteroidal (AINE) com preferência pela COX-2, originalmente usado em condições articulares como artrite reumatoide, osteoartrite e artrite idiopática juvenil.
O modelo TxGNN prevê que pode ser eficaz para **displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Artrite reumatoide, osteoartrite e artrite idiopática juvenil (conforme o grafo de conhecimento do TxGNN; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o meloxicam é um AINE com preferência pela COX-2, que reduz a produção de prostaglandinas e, assim, alivia inflamação e dor articular. Sua eficácia em doenças articulares inflamatórias é conhecida.

A displasia acromesomélica tipo Hunter-Thompson é uma displasia esquelética rara, causada por mutações de perda de função em CDMP1/GDF5, que comprometem a formação da cartilagem (condrogênese). Não há mecanismo plausível pelo qual o meloxicam corrija esse defeito do fator de crescimento. No máximo, poderia oferecer alívio sintomático inespecífico da dor.

A pontuação alta (99,92%) provavelmente reflete a proximidade na rede do conhecimento com fenótipos esqueléticos e articulares, e não um vínculo terapêutico real. Esta previsão deve ser tratada com cautela.

## Outras Previsões do Modelo

Entre as 10 principais previsões, quase todas carecem de ensaios clínicos e literatura:

| Posição | Indicação prevista | Pontuação | Nível | Comentário |
|------|------|------|------|------|
| 2 | Síndrome braquiolmia-amelogênese imperfeita | 99,92% | L5 | Sem mecanismo COX-2 conhecido |
| 3 | Miosclerose | 99,90% | L5 | Possível alívio da dor, sem evidência de modificação da doença |
| 4 | Braquiolmia | 99,89% | L5 | Sem fator inflamatório a ser alvo |
| 5 | Pseudoacondroplasia | 99,81% | L5 | AINEs são usados para dor articular, mas sem evidência específica |
| 6 | Espondiloartropatia (suscetibilidade) | 99,52% | L5 | Sobreposição com a indicação já conhecida |
| 7 | Nodulose reumatoide | 99,51% | L5 | Plausibilidade indireta via artrite reumatoide |
| 8 | Artrite idiopática juvenil poliarticular FR-positiva | 99,44% | L4 | Dentro da família de AIJ; única literatura indireta |
| 9 | Síndrome WHIM | 99,38% | L5 | Sem relação com a via CXCR4 |
| 10 | Síndrome de microftalmia colobomatosa-displasia rizomélica | 99,36% | L5 | Sem mecanismo plausível |

A previsão mais próxima de uma hipótese coerente é a AIJ poliarticular FR-positiva (posição 8), por estar dentro da família da indicação já conhecida.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal.

Para a previsão de posição 8 (AIJ poliarticular FR-positiva), há uma publicação indireta:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Coorte/estudo de segurança (classe AINE) | Pediatric Rheumatology Online Journal | Registro de fase 4 que avaliou a segurança de longo prazo e dados de desenvolvimento em pacientes com AIJ tratados com celecoxibe ou AINEs não seletivos |

## Considerações de Segurança

- **Contraindicações (do grafo de conhecimento, não do texto da bula):** hipertensão, doença renal e insuficiência renal, insuficiência cardíaca congestiva, doenças cardiovasculares e cardíacas, infarto do miocárdio, trombose coronariana, acidente vascular cerebral e doenças cerebrovasculares, infarto cerebral, úlcera péptica ativa, gastrite, distúrbios da coagulação, anemia e hemoglobinopatias, diabetes mellitus e cetoacidose diabética, hiperlipidemia (incluindo familiar), abuso/dependência de substâncias e piureter.
- **Interações Medicamentosas:** 100 interações registradas; entre as exibidas, a maioria é de gravidade moderada:
  - Corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida)
  - Ácido acetilsalicílico
  - Antidiabéticos (metformina, clorpropamida, glimepirida)
  - Mesalazina e balsalazida
  - Aprepitanto
  - Vancomicina e canamicina
  - Citrato e bicarbonato de potássio
  - Laxantes e preparos intestinais (ácido picossulfúrico, polietilenoglicol com eletrólitos, sulfato de sódio)
  - Interação de gravidade leve: linaclotida

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é apenas do modelo (L5), sem ensaios clínicos nem literatura. O mecanismo de ação do meloxicam não tem relação plausível com o defeito genético da displasia, e o fármaco não está comercializado no Brasil. As contraindicações cardiovasculares, renais e gastrointestinais também pesam contra uma nova indicação sem benefício claro.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), ainda ausente nos dados compilados
- Obter dados do mecanismo de ação (MOA) no DrugBank
- Realizar estudos pré-clínicos ou de mecanismo que justifiquem uma relação entre COX-2/prostaglandinas e a patologia
- Priorizar, se houver interesse, a hipótese mais coerente (AIJ poliarticular FR-positiva), com revisão de estudos específicos do meloxicam
- Avaliar a viabilidade regulatória, já que não há registro vigente no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

