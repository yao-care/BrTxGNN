---
layout: default
title: Ioversol
parent: Apenas Predição do Modelo (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ioversol: nova indicação prevista, Suscetibilidade à osteoartrite (osteoarthritis susceptibility) (nível de evidência L5). Indicação original: Não disponível nos registros da ANVISA (agente de contra…"
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
---

# Ioversol
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

# Ioversol: De agente de contraste iodado para osteoartrite (previsão sem evidência de suporte)

## Resumo em Uma Frase

Ioversol é um meio de contraste iodado usado em exames de imagem diagnóstica. Não há indicação original registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que possa ser eficaz para **suscetibilidade à osteoartrite (osteoarthritis susceptibility)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente baseada em grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos registros da ANVISA (agente de contraste iodado para diagnóstico por imagem) |
| Nova Indicação Prevista | Suscetibilidade à osteoartrite (osteoarthritis susceptibility) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, ioversol é um meio de contraste iodado, utilizado como auxiliar de diagnóstico por imagem, e não possui atividade farmacológica terapêutica conhecida.

Não foi identificado vínculo mecanístico entre ioversol e genes ou vias relacionados à suscetibilidade à osteoartrite. A pontuação alta (0,997) reflete apenas proximidade no grafo de conhecimento, sem ensaios ou literatura de suporte. Por isso, a previsão deve ser tratada com grande cautela.

As demais previsões do modelo também carecem de plausibilidade biológica ou de evidências:

| Posição | Doença prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|------|
| 2 | Osteoartrite | 99,63% | L4 | Um único artigo indireto, sobre embolização, e não sobre ioversol |
| 3 | Artrite reumatoide | 99,56% | L5 | Literatura sem relação com ioversol |
| 4 | Braquiolmia | 99,36% | L5 | Displasia esquelética genética rara, sem mecanismo plausível |
| 5 | Hemoglobinopatia | 99,33% | L5 | Sem mecanismo identificado |
| 6 | Síndrome braquiolmia-amelogênese imperfeita | 99,32% | L5 | Síndrome genética rara, sem evidências |
| 7 | Displasia acromesomélica tipo Hunter-Thompson | 99,32% | L5 | Displasia monogênica, sem conexão mecanística |
| 8 | Miosclerose | 99,29% | L5 | Sem relação conhecida |
| 9 | Síndrome de microftalmia colobomatosa com displasia rizomélica | 99,26% | L5 | Síndrome ultrarrara, sem mecanismo plausível |
| 10 | Alopecia | 99,25% | L5 | Sem racional mecanístico |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (suscetibilidade à osteoartrite), não há literatura relacionada. Para a segunda previsão (osteoartrite), foi encontrado um único artigo, de relevância indireta:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensaio intervencionista | Diagnostic and Interventional Imaging | Estudo LipioJoint-1: avalia a segurança e a eficácia da embolização transitória da artéria genicular com emulsão à base de óleo etiodado em osteoartrite de joelho. O ioversol não é o agente ativo; a associação provavelmente decorre da menção conjunta de agentes de contraste. |

## Considerações de Segurança

**Interações Medicamentosas**: a consulta identificou 100 interações registradas. Entre as principais, de gravidade **maior**:

- Metformina
- Anfotericina B (incluindo as formulações lipídica, de sulfato de colesterila e lipossomal)
- Mesalazina, balsalazida, olsalazina e sulfasalazina
- Aminoglicosídeos: vancomicina, canamicina, neomicina e estreptomicina
- Polimixina B

De gravidade **moderada**: manitol.

Há também interações de gravidade não classificada com atropina, famotidina, ácido acetilsalicílico, morfina e omeprazol.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas na pontuação do grafo, sem ensaios clínicos, sem literatura direta e sem mecanismo plausível. O ioversol é um agente de contraste diagnóstico, sem atividade terapêutica conhecida nas doenças previstas. Além disso, não está comercializado no Brasil (sem registros ativos).

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos que demonstrem algum efeito biológico relevante em osteoartrite antes de considerar qualquer avanço
- Verificar a viabilidade de via de administração e a situação regulatória, já que não há produto registrado no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

