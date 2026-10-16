---
layout: default
title: Zanamivir
parent: Apenas Predição do Modelo (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Zanamivir: nova indicação prevista, Pielonefrite (Pyelonephritis) (nível de evidência L5). Indicação original: Influenza"
monitor_inn: "Zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "disorder of phenylalanine metabolism", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "legionnaire disease, susceptibility to", "susceptibility to HIV infection", "dengue virus, susceptibility to", "aspergillosis, susceptibility to", "Schistosoma mansoni infection, susceptibility"]
---

# Zanamivir
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

# Zanamivir: Da influenza à pielonefrite (previsão sem evidências de suporte)

## Resumo em Uma Frase

Zanamivir é um inibidor da neuraminidase viral, originalmente usado no tratamento da influenza.
O modelo TxGNN prevê que pode ser eficaz para **Pielonefrite (Pyelonephritis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Influenza |
| Nova Indicação Prevista | Pielonefrite (Pyelonephritis) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, o zanamivir é um inibidor da neuraminidase do vírus influenza, e sua eficácia em influenza é o uso original do fármaco.

Não foi identificado vínculo mecanístico plausível com a pielonefrite. Essa doença é tipicamente uma infecção bacteriana do rim, enquanto o alvo do zanamivir (a neuraminidase viral) não é o mecanismo central dessas infecções. A pontuação elevada do TxGNN (0,998) reflete apenas uma associação no grafo de conhecimento, sem respaldo em ensaios clínicos ou literatura nos dados compilados. A previsão deve, portanto, ser tratada com cautela e considerada especulativa.

## Considerações sobre as Demais Previsões

As outras nove indicações previstas também têm nível de evidência L5 e recomendação Hold. Nenhuma tem ensaios clínicos.

| Posição | Indicação Prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Distúrbio do metabolismo da tirosina | 99,02% | Três artigos recuperados tratam de resistência à neuraminidase na influenza, sem relação biológica com a doença (correspondência por palavras-chave) |
| 3 | Síndrome de Pierre Robin teratogênica | 98,94% | Sem vínculo mecanístico; condição craniofacial congênita |
| 4 | Distúrbio do metabolismo da fenilalanina | 98,86% | Sem vínculo mecanístico |
| 5 | Hiperfenilalaninemia/fenilcetonúria responsiva à tetraidrobiopterina | 98,41% | Sem vínculo mecanístico |
| 6 | Suscetibilidade à doença dos legionários | 98,40% | Vínculo fraco e especulativo (pneumonia bacteriana) |
| 7 | Suscetibilidade à infecção por HIV | 98,40% | O único artigo recuperado trata de mutações em influenza H1N1, não de HIV |
| 8 | Suscetibilidade ao vírus da dengue | 98,40% | O flavivírus não depende de neuraminidase |
| 9 | Suscetibilidade à aspergilose | 98,40% | Sem atividade antifúngica conhecida |
| 10 | Suscetibilidade à infecção por *Schistosoma mansoni* | 98,35% | Sem vínculo mecanístico |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (pielonefrite).

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento** (não provêm de bula): epilepsia, doença pulmonar obstrutiva crônica (DPOC), DPOC grave de início precoce, doença brônquica e delírio. Convém confirmar esses itens na bula antes de qualquer uso.
- **Interações medicamentosas** (8 identificadas):
  - Insulina humana inalatória de ação rápida: gravidade **moderada**.
  - Claritromicina, loratadina, montelucaste, cetotifeno, fexofenadina, ibuprofeno e diclofenaco: gravidade não classificada.

Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do TxGNN é alta, mas não há ensaios clínicos, literatura ou mecanismo plausível que sustentem o uso do zanamivir na pielonefrite. O fármaco também não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) para avaliar o vínculo mecanístico.
- Bula da ANVISA com advertências e contraindicações, atualmente ausente e que impede a triagem de segurança.
- Evidência pré-clínica ou clínica de atividade em pielonefrite, ou a reavaliação de outras previsões com maior plausibilidade biológica.
- Análise de compatibilidade de via de administração. O zanamivir é usado principalmente por via inalatória, o que pode não ser adequado para infecção renal.
- Avaliação regulatória sobre a ausência de registro no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

