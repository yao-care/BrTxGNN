---
layout: default
title: Insulin Human
parent: Apenas Predição do Modelo (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Insulin Human: nova indicação prevista, Ooforite autoimune (autoimmune oophoritis) (nível de evidência L5). Indicação original: Antidiabéticos"
monitor_inn: "insulin human"
predicted_indications: ["autoimmune oophoritis", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
---

# Insulin Human
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

## Insulina humana: Do tratamento do diabetes à ooforite autoimune
{: .text-alpha }

## Resumo em Uma Frase

A insulina humana (Novolin R) é um hormônio utilizado originalmente como antidiabético, no controle da glicemia.
O modelo TxGNN prevê que ela poderia ser eficaz para **ooforite autoimune (autoimmune oophoritis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidiabéticos |
| Nova Indicação Prevista | Ooforite autoimune (autoimmune oophoritis) |
| Pontuação de Previsão TxGNN | 0,9984 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 13 de 13) |
| Número de Registros | 13 (ativos: 13) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a insulina humana é um hormônio que promove a captação de glicose pelas células e regula o metabolismo de carboidratos, lipídios e proteínas. Sua eficácia no diabetes está consolidada.

A relação entre a indicação original e a nova indicação é fraca. A sinalização da insulina nas células da granulosa e da teca do ovário é fisiologicamente relevante, mas não há evidência de que a insulina module a lesão ovariana autoimune. A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

Portanto, a plausibilidade biológica é limitada e especulativa. A ausência de dados de mecanismo de ação restringe a análise.

### Outras previsões do modelo (todas sem evidências clínicas)

| Doença prevista | Pontuação | Nível | Comentário |
|------|------|------|------|
| Síndrome do membro rígido focal | 0,9981 | L5 | Associação indireta: autoimunidade anti-GAD65 compartilhada com diabetes tipo 1; reflete comorbidade, não benefício terapêutico |
| Síndrome da pessoa rígida clássica | 0,9981 | L5 | Mesma lógica: comorbidade, sem efeito conhecido da insulina |
| Síndrome de disfunção responsiva à tiamina | 0,9980 | L5 | A insulina trata o diabetes associado (cuidado de suporte), não a doença de base |
| Opsismodisplasia | 0,9979 | L5 | Ligação especulativa via INPPL1 (SHIP2), regulador da via da insulina/PI3K |
| Lipodistrofia localizada induzida por fármaco | 0,9972 | L5 | Provável artefato: a própria insulina injetável causa lipodistrofia; alerta de segurança |
| Lipodistrofia centrífuga | 0,9970 | L5 | Sem evidência de eficácia |
| Lipoatrofia localizada induzida por pressão | 0,9970 | L5 | Causa mecânica; a insulina injetável pode causar lipoatrofia |
| Agenesia pancreática | 0,9970 | L4 | Reposição de insulina é terapia padrão, mas coerente com a indicação original, sem reposicionamento real |
| Lipodistrofia localizada idiopática | 0,9968 | L5 | Sem mecanismo estabelecido; a insulina pode causar lipodistrofia localizada |

---

## Informações de Comercialização no Brasil

Todos os 13 registros encontrados estão válidos; o medicamento é comercializado no Brasil.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 117660003 | Novolin R | Não informada | Antidiabéticos |
| Registro nº 116640008 | Insunorm N | Não informada | Antidiabéticos |
| Registro nº 112600181 | Humulin R | Não informada | Antidiabéticos |
| Registro nº 116640007 | Insunorm R | Não informada | Antidiabéticos |
| Registro nº 102351253 | Insuliv R | Não informada | Antidiabéticos |

Há outros 8 registros cancelados (incluindo Afrezza, Wosulin 70/30, Wosulin R, Novolin N e Humulin N), todos com a mesma indicação.

---

## Considerações de Segurança

- **Interações medicamentosas**: foram identificadas 297 interações. As principais, de gravidade moderada, incluem:
  - Outros antidiabéticos (metformina, pioglitazona, alogliptina, albiglutida): efeito hipoglicemiante aditivo.
  - Agentes simpatomiméticos e broncodilatadores (epinefrina, fenilefrina, pseudoefedrina, salbutamol): podem alterar a resposta glicêmica.
  - Corticosteroides (hidrocortisona), etinilestradiol e estradiol: podem reduzir o efeito da insulina.
  - Betabloqueador (acebutolol), benazepril, hidroclorotiazida, acetazolamida, doxiciclina, alpelisib e etanol.
  - Interações leves: corticosteroides tópicos (hidrocortisona tópica, alclometasona tópica).
- **Alerta específico do modelo**: a insulina injetável pode causar lipodistrofia localizada (lipohipertrofia e lipoatrofia) nos locais de aplicação. Isso torna contraproducente qualquer uso para as indicações de lipodistrofia previstas.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é apenas computacional (L5), sem ensaios clínicos nem literatura, e sem vínculo mecanístico demonstrado entre insulina e ooforite autoimune. Além disso, o medicamento é comercializado no Brasil, com 13 registros válidos de 13.

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação da insulina humana.
- Revisar a literatura e os registros de ensaios sobre insulina e ooforite autoimune.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pôde ser concluída.
- Esclarecer a situação regulatória atual, já que não há registro válido no Brasil.
- Se houver interesse em outras previsões, a agenesia pancreática (L4) é a única com coerência clínica, mas equivale à indicação original e não constitui reposicionamento.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

