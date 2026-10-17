---
layout: default
title: Vildagliptin
parent: Apenas Predição do Modelo (L5)
nav_order: 669
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vildagliptin: nova indicação prevista, Síndrome da pessoa rígida clássica (Classic Stiff Person Syndrome) (nível de evidência L5). Indicação original: Diabetes mellitus tipo 2"
monitor_inn: "VILDAGLIPTIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Vildagliptin
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

# Vildagliptina: Do diabetes mellitus tipo 2 à síndrome da pessoa rígida clássica

## Resumo em Uma Frase

A vildagliptina é um inibidor da dipeptidil peptidase-4 (DPP-4), originalmente usado no tratamento do diabetes mellitus tipo 2.
O modelo TxGNN prevê que pode ser eficaz para a **síndrome da pessoa rígida clássica (Classic Stiff Person Syndrome)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diabetes mellitus tipo 2 |
| Nova Indicação Prevista | Síndrome da pessoa rígida clássica (Classic Stiff Person Syndrome) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a vildagliptina inibe a DPP-4. Isso aumenta os níveis de GLP-1 e GIP ativos e reduz a secreção de glucagon, o que melhora o controle glicêmico no diabetes tipo 2. Os dados de farmacologia também listam como alvos as enzimas DPP-8 e DPP-9 e o canal TRPV4.

Na prática, **não há uma ligação mecanística sustentada pelos dados** entre essa inibição e a síndrome da pessoa rígida. Essa doença é um distúrbio autoimune do sistema GABAérgico, geralmente associado a anticorpos anti-GAD65, e a inibição da DPP-4 não tem conexão estabelecida com ela. A pontuação alta provavelmente reflete a proximidade entre doenças e fenótipos no grafo de conhecimento, como a associação com diabetes, e não um efeito terapêutico demonstrado.

A pontuação idêntica da síndrome do membro rígido focal, uma variante da mesma doença, reforça essa leitura. As duas previsões vêm da mesma vizinhança no grafo e não constituem evidências independentes.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

Consulte a bula para informações de segurança. Os dados compilados não trazem advertências nem contraindicações da bula brasileira. As entradas de interação são apenas alvos farmacológicos da vildagliptina (DPP-4, DPP-8, DPP-9 e TRPV4), não interações medicamentosas clínicas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (99,88%), mas não há ensaios, literatura ou ligação mecanística plausível. O nível de evidência é L5, e o fármaco não está comercializado no Brasil (0 registros).

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), uma lacuna que impede a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank) e avaliar se existe alguma hipótese biológica que ligue a inibição da DPP-4 à síndrome da pessoa rígida.
- Realizar uma busca sistemática de literatura e de registros de ensaios específica para esta indicação.
- Considerar priorizar outra previsão do mesmo fármaco com suporte clínico real: o **diabetes mellitus tipo 1** (pontuação 99,37%, nível L2). Há um ensaio de Fase 2 concluído (NCT02803892, rapamicina + vildagliptina, n=55), com publicação de RCT duplo-cego (PMID 33124663). O resultado de eficácia não consta nos dados compilados, e há um ensaio de Fase 3 com status desconhecido (NCT01559025, n=44). Também existe um relato de caso de pancreatite provavelmente associada à vildagliptina, que representa um sinal de segurança a monitorar.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

