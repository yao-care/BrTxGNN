---
layout: default
title: Tramadol
parent: Apenas Predição do Modelo (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tramadol: nova indicação prevista, Displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasi… (nível de evidência L5). Indicação original: Osteoartrite / artropatia"
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
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

# Tramadol: Da osteoartrite à displasia acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Tramadol é um analgésico opioide de ação central, associado nas bases de conhecimento do modelo a osteoartrite e artropatias.
O modelo TxGNN prevê que pode ser eficaz para **displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasia, Hunter-Thompson type)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Osteoartrite / artropatia (conforme o grafo de conhecimento do modelo; não há registro no Brasil) |
| Nova Indicação Prevista | Displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasia, Hunter-Thompson type) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o tramadol é um opioide com atividade adicional de inibição da recaptação de monoaminas, usado para dor; sua relação com osteoartrite e artropatia vem do grafo de conhecimento do modelo.

A displasia acromesomélica tipo Hunter-Thompson é uma displasia esquelética rara, causada por defeitos em CDMP1/GDF5. Não se conhece mecanismo pelo qual o tramadol modifique a doença de base. Qualquer benefício plausível se limitaria ao alívio sintomático da dor, não à modificação da doença.

A pontuação alta provavelmente reflete a proximidade na rede de conhecimento com fenótipos esqueléticos e articulares das indicações originais, e não evidência biológica ou clínica direta. Por isso, a previsão deve ser tratada com cautela.

### Outras previsões do modelo (todas com nível L5)

| Posição | Doença prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Síndrome braquiolmia-amelogênese imperfeita | 99,99% | Sem ligação mecanística conhecida |
| 3 | Miosclerose | 99,99% | Possível alívio sintomático da dor, sem evidência |
| 4 | Braquiolmia | 99,99% | Sem mecanismo conhecido |
| 5 | Pseudoacondroplasia | 99,98% | Analgesia sintomática conceitualmente plausível (dor articular e osteoartrite precoces) |
| 6 | Espondiloartropatia (suscetibilidade) | 99,97% | Sem ação anti-inflamatória |
| 7 | Artrite idiopática juvenil | 99,92% | Uma publicação indireta, sobre cetoprofeno |
| 8 | Artrite juvenil por defeito em LACC1 | 99,92% | Sem evidência |
| 9 | Nodulose reumatoide | 99,92% | Sem evidência |
| 10 | AIJ poliarticular com fator reumatoide positivo | 99,90% | Sem atividade modificadora da doença |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal prevista. Para a artrite idiopática juvenil (7ª previsão), foi fornecida apenas uma revisão indireta, que trata do cetoprofeno e não do tramadol:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/) | 2010 | Revisão | Paediatric Drugs | Farmacocinética, eficácia e tolerabilidade do AINE cetoprofeno em pacientes pediátricos; não fornece evidência clínica para o tramadol |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento do modelo** (não se trata de texto de bula): hipertensão, insuficiência hepática, doença hepática e cirrose, epilepsia, transtornos de ansiedade e neuróticos, distimia, doenças da vesícula biliar, diabetes mellitus e cetoacidose diabética, abuso/dependência de substâncias, hiperlipidemia (inclusive familiar), insuficiência respiratória, intoxicação por paracetamol, síndrome serotoninérgica, pseudotumor cerebral e hipertensão intracraniana, abstinência de álcool e de substâncias, síndrome de Wernicke-Korsakoff e infecções do sistema nervoso central.
- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as listadas, as de gravidade **maior** incluem alvimopano, bupropiona, cisaprida, dexfenfluramina, dietilpropiona, dolasetrona, dronabinol, efedrina e fenfluramina. Interações de gravidade **moderada** incluem atropina, bisacodil, óleo de rícino, cimetidina, claritromicina, clidínio, dicicloverina, eliglustate, eluxadolina, famotidina e glicerina.
- Pontos de atenção adicionais para uso pediátrico (relevantes nas previsões de artrite juvenil): metabolismo ultrarrápido via CYP2D6 e depressão respiratória.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia somente na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura, e não há mecanismo plausível de modificação da doença. O fármaco não está registrado no Brasil e tem perfil de segurança que exige cautela.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (por exemplo, via DrugBank) para analisar a ligação mecanística.
- Obter e analisar a bula na ANVISA (advertências e contraindicações oficiais), etapa bloqueante para a triagem de segurança.
- Realizar revisão da literatura específica sobre tramadol nas doenças previstas, especialmente como analgesia sintomática em displasias esqueléticas e artrites.
- Esclarecer a situação regulatória no Brasil, já que não há registros vigentes.
- Definir, caso se avance, uma avaliação de segurança para populações específicas (pediatria, insuficiência hepática, risco de dependência e de síndrome serotoninérgica).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

