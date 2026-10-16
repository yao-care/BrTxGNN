---
layout: default
title: Elexacaftor
parent: Apenas Predição do Modelo (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Elexacaftor: nova indicação prevista, Artrite Reumatoide (Rheumatoid Arthritis) (nível de evidência L5). Indicação original: Fibrose cística"
---

# Elexacaftor
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

# Elexacaftor: Da fibrose cística à artrite reumatoide

## Resumo em Uma Frase

Elexacaftor é um corretor da proteína CFTR, usado em combinação tripla (com tezacaftor e ivacaftor) no tratamento da fibrose cística.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, mas até o momento não há **nenhum ensaio clínico** nem **nenhuma publicação** que apoie esta direção; a previsão se baseia apenas em cálculo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrose cística |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 98,11% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, o elexacaftor faz parte de uma terapia tripla para fibrose cística, junto com tezacaftor e ivacaftor. Ele atua sobre o canal CFTR, aumentando a quantidade de canais corretamente dobrados na membrana celular (função de corretor), com um pequeno efeito potencializador do canal. Em conjunto, a combinação restaura o fluxo de cloreto e ajuda a equilibrar sal e água nas superfícies epiteliais. Dados farmacológicos também indicam efeitos fora do alvo sobre alguns canais de potássio.

Não há, nos dados compilados, uma ligação mecanística plausível entre a modulação do CFTR e a artrite reumatoide, uma doença autoimune inflamatória das articulações. A previsão vem exclusivamente da pontuação do grafo de conhecimento do TxGNN (0,981) e não foi corroborada por estudos clínicos ou publicações. A similaridade com a indicação original também não foi avaliada.

Por isso, a previsão deve ser tratada como uma hipótese computacional a ser investigada, e não como indício de eficácia.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 9 interações. Oito têm gravidade moderada: empagliflozina, repaglinida, rifaximina, rosuvastatina, sinvastatina, selexipague, revefenacina e etinilestradiol. A nona refere-se à interação farmacológica com o alvo CFTR, sem classificação de gravidade.
- Não há dados de advertências e contraindicações da bula. Consulte a bula para informações adicionais de segurança.
- Outros achados da literatura, no contexto da fibrose cística, incluem um caso de hipervitaminose A com hipertensão intracraniana após o início da terapia tripla e uma avaliação do risco de síndrome metabólica após um ano de exposição. Esses dados não se referem à artrite reumatoide.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para artrite reumatoide tem pontuação alta no modelo, mas nenhuma evidência clínica, de literatura ou mecanística a sustenta (nível L5). Além disso, o medicamento não está comercializado no Brasil e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (MOA), por exemplo, consultando a API do DrugBank
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa necessária para a triagem de segurança
- Realizar revisão sistemática da literatura e avaliar se há uma hipótese biológica plausível ligando o CFTR à artrite reumatoide
- Se a hipótese se sustentar, buscar evidências pré-clínicas antes de qualquer ensaio clínico
- Avaliar a situação regulatória no Brasil, já que não há registro vigente
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

