---
layout: default
title: Tisagenlecleucel
parent: Apenas Predição do Modelo (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tisagenlecleucel: nova indicação prevista, Colite de Crohn (Crohn's colitis) (nível de evidência L5). Indicação original: Não disponível nos dados de registro da ANVISA"
monitor_inn: "Tisagenlecleucel"
predicted_indications: ["Crohn's colitis", "multiple endocrine neoplasia", "idiopathic aplastic anemia", "adrenal gland hyperfunction", "HER2 positive breast carcinoma", "ankylosing spondylitis", "lymphoadenopathic mastocytosis with eosinophilia", "systemic mastocytosis", "Smouldering systemic mastocytosis", "rheumatoid vasculitis"]
---

# Tisagenlecleucel
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

## Tisagenlecleucel: De terapia CAR-T anti-CD19 para a colite de Crohn (previsão do modelo)
{: .text-alpha }

## Resumo em Uma Frase

Tisagenlecleucel é uma terapia celular CAR-T dirigida ao antígeno CD19, que depleta células B e é utilizada em neoplasias hematológicas de células B. Os dados compilados para este relatório não trazem uma indicação original registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Colite de Crohn (Crohn's colitis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão baseada em grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro da ANVISA |
| Nova Indicação Prevista | Colite de Crohn (Crohn's colitis) |
| Pontuação de Previsão TxGNN | 91,39% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base consultada. Segundo informações conhecidas, tisagenlecleucel é uma terapia CAR-T dirigida a CD19, que elimina células B. Seu uso estabelecido é em neoplasias de células B, e não há indicação registrada no Brasil nos dados compilados.

Para a doença de Crohn, a justificativa mecanística é **fraca**. A patologia é conduzida principalmente por células T e pela imunidade inata, e não por células B. A pontuação elevada do TxGNN (0,914) reflete apenas uma associação no grafo de conhecimento, sem respaldo de ensaios ou literatura nos dados disponíveis.

Além disso, os riscos conhecidos da terapia, como linfodepleção, síndrome de liberação de citocinas e infecções, seriam preocupações importantes em pacientes com doença inflamatória intestinal.

### Outras previsões do modelo (todas L5, Hold)

Outras indicações previstas também não têm ensaios clínicos nem literatura nos dados compilados:

| Posição | Doença prevista | Pontuação TxGNN | Avaliação mecanística resumida |
|------|------|------|------|
| 2 | Neoplasia endócrina múltipla | 91,34% | Sem vínculo claro; tecidos endócrinos geralmente não expressam CD19 |
| 3 | Anemia aplástica idiopática | 89,69% | Rationale indireto e fraco; risco de agravar citopenias |
| 4 | Hiperfunção da glândula adrenal | 88,34% | Sem vínculo plausível; processo não é de células B CD19+ |
| 5 | Carcinoma de mama HER2 positivo | 88,02% | Células tumorais não expressam CD19; exigiria outro produto (anti-HER2) |
| 6 | Espondilite anquilosante | 87,11% | Doença dirigida por IL-17/IL-23 e TNF; rationale fraco |
| 7 | Mastocitose linfadenopática com eosinofilia | 87,04% | Neoplasia de mastócitos; alvo incompatível |
| 8 | Mastocitose sistêmica | 87,00% | Doença clonal de mastócitos (KIT); sem base mecanística |
| 9 | Mastocitose sistêmica indolente (smouldering) | 86,83% | Alvo incompatível e relação risco-benefício desfavorável |
| 10 | Vasculite reumatoide | 86,24% | Rationale teórico e indireto (células B produtoras de autoanticorpos); especulativo |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 41 interações nos dados compilados. Entre as listadas, destacam-se as de gravidade **maior** com:
  - Deferiprona
  - Samário (153Sm) lexidronam
  - Adalimumabe
  - Baricitinibe
  - Certolizumabe pegol
  - Cladribina
  - Leflunomida
  - Natalizumabe

  Também há interações de gravidade **moderada** com, por exemplo, estrôncio-89, roflumilaste, cloranfenicol, alefacepte, alentuzumabe, anaquinra, azatioprina, canaquinumabe, fumarato de dimetila, niraparibe e ocrelizumabe. Em geral, trata-se de imunossupressores e agentes mielossupressores, com risco aditivo de imunossupressão e citopenias.
- **Riscos esperados da classe (conforme avaliação mecanística)**: linfodepleção, síndrome de liberação de citocinas, risco de infecção e citopenias prolongadas.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é apenas computacional (L5), sem ensaios clínicos nem literatura, com racional mecanístico fraco para a colite de Crohn e perfil de risco elevado. O produto também não é comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula/advertências e contraindicações na ANVISA
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca sistemática de ensaios clínicos e literatura sobre CAR-T anti-CD19 em doenças autoimunes e inflamatórias intestinais
- Avaliar a viabilidade regulatória e a relação risco-benefício antes de qualquer estudo exploratório
- Se houver interesse em autoimunidade, priorizar doenças mediadas por células B (por exemplo, vasculite reumatoide), que têm racional teórico mais plausível
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

