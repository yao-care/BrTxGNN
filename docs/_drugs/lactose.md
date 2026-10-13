---
layout: default
title: Lactose
parent: Apenas Predição do Modelo (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Lactose
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

# Lactose: Da intolerância à lactose ao sangramento de varizes esofágicas

## Resumo em Uma Frase

A lactose é um dissacarídeo usado como açúcar alimentar e excipiente farmacêutico, associado originalmente à intolerância à lactose.
O modelo TxGNN prevê que possa ser eficaz para **varizes esofágicas com sangramento (esophageal varices with bleeding)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de um sinal puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Intolerância à lactose |
| Nova Indicação Prevista | Varizes esofágicas com sangramento (esophageal varices with bleeding) |
| Pontuação de Previsão TxGNN | 99,93% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a lactose é um dissacarídeo de uso alimentar e excipiente em medicamentos. Não foi identificado um vínculo mecanístico plausível com as varizes esofágicas.

A pontuação alta do modelo provavelmente reflete uma confusão com açúcares estruturalmente semelhantes. A lactulose, outro dissacarídeo sintético, é usada na encefalopatia hepática e em contextos de sangramento varicoso. A previsão, portanto, parece ser um artefato do grafo de conhecimento, e não uma hipótese biológica sustentada.

A previsão para varizes esofágicas sem sangramento tem pontuação idêntica, o que reforça a suspeita de artefato. As demais previsões de maior pontuação (varizes em geral, síndrome de Steel, cistinose, hipofosfatasia, entre outras) também não têm vínculo mecanístico identificado, nem ensaios ou literatura de apoio.

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão está no nível L5 (apenas modelo), sem ensaios clínicos, sem literatura e sem mecanismo plausível. O fármaco não tem registro no Brasil, e os dados de segurança da bula não estão disponíveis.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Esclarecer o mecanismo de ação a partir do DrugBank
- Verificar se a previsão não resulta de confusão com a lactulose ou de artefato do grafo de conhecimento
- Identificar estudos pré-clínicos ou observacionais que sustentem alguma relação com a hipertensão portal ou varizes antes de reconsiderar a decisão
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

