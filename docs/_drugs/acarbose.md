---
layout: default
title: Acarbose
parent: Apenas Predição do Modelo (L5)
nav_order: 16
evidence_level: L5
indication_count: 9
monitor_inn: "ACARBOSE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-23
description: "Acarbose: nova indicação prevista, Síndrome da pessoa rígida clássica (nível de evidência L5). Indicação original: Diabetes mellitus tipo 2"
---

# Acarbose
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Acarbose: Do diabetes mellitus tipo 2 à síndrome da pessoa rígida clássica
{: .text-alpha }

## Resumo em Uma Frase

Acarbose é um inibidor da alfa-glicosidase intestinal, originalmente usado no tratamento do diabetes mellitus tipo 2.
O modelo TxGNN prevê que pode ser eficaz para a **síndrome da pessoa rígida clássica (classic stiff person syndrome)**, mas há **0 ensaios clínicos** e **0 publicações** que estudem diretamente essa doença; trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diabetes mellitus tipo 2 (relação registrada no grafo de conhecimento; os registros locais não trazem texto de indicação aprovada) |
| Nova Indicação Prevista | Síndrome da pessoa rígida clássica |
| Pontuação de Previsão TxGNN | 0,9965 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 4) |
| Número de Registros | 4 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a acarbose atua na luz intestinal inibindo as alfa-glicosidases, o que retarda a absorção de carboidratos e reduz a glicemia pós-prandial.

A síndrome da pessoa rígida é um distúrbio autoimune da neurotransmissão GABAérgica, geralmente associado a anticorpos anti-GAD65. Não foi identificado vínculo mecanístico plausível com a acarbose. A pontuação alta (0,9965) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, possivelmente a autoimunidade a GAD65 compartilhada com o diabetes, e não evidência biológica.

Em conclusão, a previsão não tem sustentação biológica nem clínica nos dados disponíveis e deve ser tratada como hipótese computacional.

Outras previsões do modelo também têm nível L5 e carecem de estudos diretos: síndrome do membro rígido focal, síndrome de disfunção responsiva à tiamina, opsismodisplasia, lipodistrofias localizadas (induzida por fármacos, centrífuga, induzida por pressão e idiopática) e agenesia pancreática.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a síndrome da pessoa rígida clássica. (As publicações recuperadas para a previsão de agenesia pancreática, de menor posição, tratam de diabetes tipo 2, síndrome autoimune da insulina e modelos animais, e não abordam a doença prevista aqui.)

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada | Situação |
|---------|------|------|-----------|------|
| Registro 135690035 | AGLUCOSE (EMS Sigma Pharma) | Não informada | Texto de indicação não disponível | Válido |
| Registro 104290084 | GLUCOBAY (Bayer) | Não informada | Texto de indicação não disponível | Cancelado |
| Registro 100200132 | STABILIC (União Química) | Não informada | Texto de indicação não disponível | Cancelado |
| Registro 170560074 | GLUCOBAY (Bayer) | Não informada | Texto de indicação não disponível | Cancelado |

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não são texto de bula): doença renal, piureter, doença hepática, doença da vesícula biliar, cirrose hepática, doença inflamatória intestinal, hipoglicemia e lesão.
- **Interações medicamentosas**: foram identificadas 100 interações no total; as 20 listadas incluem principalmente nível moderado, por exemplo acetazolamida, salbutamol, babosa (folha de Aloe vera), alpelisibe, amprenavir, aripiprazol, asenapina, asparaginases, atazanavir, bedaquilina, bendroflumetiazida, benzfetamina, benzotiazida e betametasona. Há também interações de nível leve, como albiglutida, alclometasona tópica, ácido lipoico, amcinonida e anisindiona.

Consulte a bula para advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é puramente computacional (L5), sem ensaios nem publicações sobre a síndrome da pessoa rígida clássica, e sem vínculo mecanístico plausível com a acarbose.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), ainda ausente.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Demonstrar um racional biológico direto, com estudos pré-clínicos ou clínicos na doença-alvo, antes de qualquer reavaliação.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

