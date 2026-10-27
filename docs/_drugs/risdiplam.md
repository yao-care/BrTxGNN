---
layout: default
title: Risdiplam
parent: Apenas Predição do Modelo (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Risdiplam: nova indicação prevista, Acne (disease) (nível de evidência L5). Indicação original: Não disponível nos dados de registro da ANVISA"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)", "drug-induced osteoporosis", "zinc, elevated plasma", "common wart", "metastatic melanoma", "dermatitis", "non-cutaneous melanoma", "acrodermatitis chronica atrophicans", "epithelioid cell melanoma", "eyelid melanoma"]
---

# Risdiplam
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

## Risdiplam: De indicação original não registrada a acne (doença)
{: .text-alpha }

## Resumo em Uma Frase

Risdiplam é um modulador de splicing do gene SMN2, sem indicação aprovada registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **acne (disease)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro da ANVISA |
| Nova Indicação Prevista | Acne (disease) |
| Pontuação de Previsão TxGNN | 99,45% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o risdiplam é um modulador de splicing do SMN2, que promove a inclusão do éxon 7 e aumenta a produção de proteína SMN funcional. Esse é o fundamento de seu uso na atrofia muscular espinhal, mas essa indicação não consta nos registros brasileiros analisados.

Não foi identificado mecanismo que sustente a previsão para acne. Não há relação estabelecida entre a modulação do splicing de SMN2 e a biologia das glândulas sebáceas ou a inflamação associada ao *C. acnes*. A pontuação elevada (0,995) reflete apenas proximidade em grafo de conhecimento, sem respaldo clínico ou de literatura.

Também vale notar que as terapias para acne da classe dos retinoides têm perfis de segurança distintos, e não há dados do risdiplam nesse cenário.

---

## Outras Indicações Previstas (Todas de Nível L5)

Nenhuma das demais previsões do modelo possui ensaios clínicos ou literatura. Todas estão em Hold.

| Posição | Indicação Prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Osteoporose induzida por fármacos | 97,72% | A deficiência de SMN é discutida em relação à saúde óssea e muscular na AME, mas isso não estabelece efeito terapêutico. |
| 3 | Zinco plasmático elevado | 97,32% | Achado bioquímico, sem alvo terapêutico claro. |
| 4 | Verruga comum | 97,21% | Sem relação conhecida com a proliferação epitelial induzida por HPV. |
| 5 | Melanoma metastático | 96,84% | Especulativo; seriam necessários dados pré-clínicos e revisão de segurança. |
| 6 | Dermatite | 96,62% | Efeitos cutâneos adversos já foram relatados com o fármaco, portanto um benefício seria contraintuitivo. |
| 7 | Melanoma não cutâneo | 96,18% | Provável proximidade no grafo com outras entidades de melanoma. |
| 8 | Acrodermatite crônica atrófica | 96,11% | Manifestação tardia de infecção por *Borrelia*, tratada com antibióticos. |
| 9 | Melanoma de células epitelioides | 95,93% | Agrupa-se com outros subtipos de melanoma, sem dados de apoio. |
| 10 | Melanoma palpebral | 95,88% | Preocupação adicional com segurança ocular, dados achados retinianos em estudos não clínicos. |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

- **Interações Medicamentosas** (2 interações de nível moderado):
  - Metformina (moderada)
  - Metilnaltrexona (moderada)

Para advertências e contraindicações, consulte a bula. Esses dados não estavam disponíveis para este relatório.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para acne baseia-se apenas na pontuação do modelo, sem ensaios clínicos, literatura ou mecanismo plausível. O fármaco não está comercializado no Brasil, e faltam dados de segurança da bula, o que impede avançar para a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), uma lacuna que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação no DrugBank
- Verificar a situação regulatória do risdiplam no Brasil e sua indicação original
- Realizar estudos pré-clínicos ou revisão da literatura que sustentem a ligação mecanística com acne
- Avaliar compatibilidade de via de administração e formulação para a nova indicação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

