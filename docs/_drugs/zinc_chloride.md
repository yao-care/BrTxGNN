---
layout: default
title: Zinc Chloride
parent: Apenas Predição do Modelo (L5)
nav_order: 681
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Zinc Chloride: nova indicação prevista, Retinopatia Diabética Não Proliferativa Grave (severe nonproliferativ… (nível de evidência L5). Indicação original: Nutrientes parenterais"
monitor_inn: "ZINC CHLORIDE"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "Sjogren syndrome", "dry eye syndrome"]
---

# Zinc Chloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

# Cloreto de Zinco: De nutriente parenteral para retinopatia diabética não proliferativa grave

## Resumo em Uma Frase

Cloreto de zinco é um oligoelemento originalmente usado como nutriente parenteral (nutrição parenteral).
O modelo TxGNN prevê que pode ser eficaz para **Retinopatia Diabética Não Proliferativa Grave (severe nonproliferative diabetic retinopathy)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Nutrientes parenterais |
| Nova Indicação Prevista | Retinopatia Diabética Não Proliferativa Grave (severe nonproliferative diabetic retinopathy) |
| Pontuação de Previsão TxGNN | 99,34% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o cloreto de zinco é uma fonte de zinco usada em nutrição parenteral para repor as necessidades desse oligoelemento. Sua eficácia como suplemento nutricional é estabelecida, e mecanisticamente poderia ser aplicável à retinopatia diabética.

O zinco participa da defesa antioxidante (por exemplo, na superóxido dismutase Cu/Zn) e do metabolismo da retina, o que pode se relacionar ao estresse oxidativo na retinopatia diabética. Essa ligação, porém, é especulativa e não é sustentada por evidências nos dados compilados para este relatório. A pontuação do modelo é muito alta, mas baseia-se apenas em relações do grafo de conhecimento.

Vale notar que o uso original (infusão intravenosa como nutriente) é muito diferente do uso previsto (doença ocular). A via de administração e a segurança ocular do cloreto de zinco para essa finalidade não foram avaliadas.

### Outras previsões do modelo

| Indicação Prevista | Pontuação TxGNN | Nível de Evidência | Comentário |
|------|------|------|------|
| Síndrome de Sjögren (Sjogren syndrome) | 99,18% | L5 | Zinco atua na regulação imune e na função epitelial/mucosa; hipótese sem evidência de apoio |
| Síndrome do olho seco (dry eye syndrome) | 99,18% | L5 | Racional plausível (integridade epitelial, cicatrização, ação antioxidante), mas não verificado; provavelmente não é independente da previsão de Sjögren, pois o olho seco é característica central dessa doença |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100410165 (cancelado) | ADDAVEN | Não informada | Nutrientes parenterais |

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento** (relações do modelo, não texto de bula): meta-hemoglobinemia, sulfo-hemoglobinemia, deficiência de G6PD, doença de depósito de glicogênio, cistinúria, galactosemia, deficiência de piruvato desidrogenase E3, meta-hemoglobinemia por deficiência de meta-hemoglobina redutase, doença de Wilson, doenças do metabolismo do ferro e hemocromatose hereditária.
- **Interações Medicamentosas**: foram identificadas 76 interações no total; as 20 listadas nos dados compilados incluem:
  - **Moderadas**: tetraciclina, minociclina, levofloxacino (provável redução da absorção por quelação; separar os horários de administração é uma medida usual, a confirmar em fontes oficiais).
  - **Leves**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona) e imunossupressores/imunobiológicos (abatacepte, adalimumabe, alefacepte, anakinra, imunoglobulinas antilinfocitárias/antitimocitárias, azatioprina, baricitinibe, basiliximabe, belatacepte).

Para advertências e contraindicações da bula, consulte a bula; não foi possível obter esses dados da ANVISA.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta, mas é apenas computacional (L5): não há ensaios clínicos nem literatura, não há dados de mecanismo de ação, o único registro no Brasil está cancelado e as informações de bula não foram obtidas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar busca sistemática de literatura pré-clínica e clínica sobre zinco em retinopatia diabética, síndrome de Sjögren e olho seco.
- Avaliar a compatibilidade de via e formulação (uso ocular/tópico vs. parenteral) e a segurança ocular.
- Considerar as previsões de Sjögren e olho seco em conjunto, dada sua relação biológica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

