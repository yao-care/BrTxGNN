---
layout: default
title: Tolnaftate
parent: Apenas Predição do Modelo (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tolnaftate: nova indicação prevista, Doença infecciosa ectotrix (ectothrix infectious disease) (nível de evidência L5). Indicação original: Anti-infecciosos tópicos – associações medicamentosas"
monitor_inn: "Tolnaftate"
predicted_indications: ["ectothrix infectious disease", "Majocchi granuloma", "endothrix infectious disease", "ophthalmic herpes zoster", "orbital cellulitis", "infectious mononucleosis"]
---

# Tolnaftate
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

# Tolnaftato: Do uso antifúngico/anti-infeccioso tópico à infecção dermatofítica ectotrix

## Resumo em Uma Frase

Tolnaftato é um antifúngico tópico, registrado no Brasil apenas em associações medicamentosas (com valerato de betametasona, sulfato de gentamicina e clioquinol), classificadas como anti-infecciosos tópicos e glicocorticoides tópicos em associação.
O modelo TxGNN prevê que pode ser eficaz para **doença infecciosa ectotrix (ectothrix infectious disease)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta indicação.
Trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-infecciosos tópicos – associações medicamentosas |
| Nova Indicação Prevista | Doença infecciosa ectotrix (ectothrix infectious disease) |
| Pontuação de Previsão TxGNN | 98,59% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o tolnaftato é um tiocarbamato que inibe a esqualeno epoxidase fúngica, bloqueando a síntese de ergosterol. Esse mecanismo é, em princípio, ativo contra dermatófitos.

A infecção ectotrix é uma infecção dermatofítica do pelo, com esporos na parte externa da haste. Por isso, o mecanismo antifúngico é plausível. Existe, porém, uma limitação importante: infecções que envolvem o folículo piloso em geral exigem terapia sistêmica, pois a penetração de agentes tópicos é fraca.

A pontuação alta do TxGNN (98,59%) é apenas uma previsão. Não há ensaios nem literatura que a sustentem.

### Outras indicações previstas (contexto)

| Posição | Indicação prevista | Pontuação | Nível | Comentário |
|---|---|---|---|---|
| 2 | Granuloma de Majocchi | 98,59% | L5 | Infecção profunda folicular/dérmica; terapia tópica isolada geralmente é inadequada |
| 3 | Candidíase cutânea | 98,54% | L4 | Atividade do tolnaftato contra *Candida* é fraca e inconsistente; azólicos são o padrão |
| 4 | Doença infecciosa endotrix | 98,51% | L5 | Esporos dentro da haste; terapia sistêmica é o padrão |
| 5 | Micose superficial | 98,48% | L3 | Corresponde essencialmente ao uso já existente do fármaco |
| 6 | Tinea profunda | 98,14% | L5 | Penetração tópica limitada em tecido profundo |
| 7–10 | Herpes zóster oftálmico, celulite orbitária, mononucleose infecciosa | 90,1–92,2% | L5 | Sem plausibilidade mecanística; provável artefato do grafo |

A **micose superficial** é a indicação com maior suporte (L3), mas é basicamente o uso já estabelecido do tolnaftato, não um reposicionamento genuíno.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação principal prevista.

---

## Evidências da Literatura

Não há literatura relacionada à indicação principal (infecção ectotrix). Para a indicação mais bem apoiada (micose superficial), os principais estudos são:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10398626](https://pubmed.ncbi.nlm.nih.gov/10398626/) | 1999 | Revisão sistemática | BMJ | Eficácia e custo-efetividade de tratamentos tópicos para infecções fúngicas da pele e unhas dos pés |
| [1090684](https://pubmed.ncbi.nlm.nih.gov/1090684/) | 1975 | Ensaio controlado | J Invest Dermatol | Griseofulvina tópica, tolnaftato e placebo no tratamento tópico de dermatofitoses superficiais |
| [4619464](https://pubmed.ncbi.nlm.nih.gov/4619464/) | 1974 | Ensaio comparativo duplo-cego | Postgrad Med J | Clotrimazol versus tolnaftato em dermatofitoses superficiais |
| [778288](https://pubmed.ncbi.nlm.nih.gov/778288/) | 1976 | Revisão | J Invest Dermatol | O tolnaftato para dermatofitose foi um dos grandes avanços no tratamento de micoses superficiais |
| [1379146](https://pubmed.ncbi.nlm.nih.gov/1379146/) | 1992 | Revisão | Drugs | Diagnóstico e recomendações de tratamento das infecções fúngicas superficiais da pele |
| [14288003](https://pubmed.ncbi.nlm.nih.gov/14288003/) | 1964 | Estudo clínico | Antimicrob Agents Chemother | Efeito do tolnaftato em infecções fúngicas superficiais |
| [14288002](https://pubmed.ncbi.nlm.nih.gov/14288002/) | 1964 | Estudo clínico | Antimicrob Agents Chemother | Efeito do tolnaftato em infecções micóticas superficiais |
| [5844107](https://pubmed.ncbi.nlm.nih.gov/5844107/) | 1965 | Estudo clínico | Am J Dis Child | Tolnaftato em infecções fúngicas superficiais |

Para candidíase cutânea, há também um estudo randomizado comparativo ([6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/), 1981, J Int Med Res) de 154 pacientes, comparando dois cremes de corticosteroide com antimicrobianos. Um deles continha tolnaftato (betametasona, gentamicina, iodoclorhidroxiquina e tolnaftato), e as respostas terapêuticas foram equivalentes.

Observação: a maior parte da literatura é das décadas de 1960 a 1970 e não é específica para infecções ectotrix.

---

## Informações de Comercialização no Brasil

Todos os 20 registros estão **cancelados**. Principais exemplos:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 154230248 | Valerato de betametasona + sulfato de gentamicina + tolnaftato + clioquinol | — | Anti-infecciosos tópicos – associações medicamentosas |
| Registro nº 100431406 | Permut | — | Glicocorticoides tópicos – associação medicamentosa |
| Registro nº 104400194 | Cremederme | — | Glicocorticoides tópicos – associação medicamentosa |
| Registro nº 102351178 | Dermatisan | — | Anti-infecciosos tópicos – associações medicamentosas |
| Registro nº 103700231 | Tetraderm | — | Glicocorticoides tópicos – associação medicamentosa |

---

## Considerações de Segurança

Os dados compilados para este relatório não incluem advertências, contraindicações nem interações medicamentosas. Consulte a bula para informações de segurança.

Observação: as previsões que envolvem uso próximo ao olho (herpes zóster oftálmico) levantam preocupação adicional de segurança com aplicação tópica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para infecção ectotrix tem apenas suporte computacional (L5), sem ensaios ou literatura. Há ainda limitação farmacológica, pois a penetração tópica em infecções do pelo é fraca. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), o que hoje impede a triagem de segurança.
- Complementar os dados de mecanismo de ação via DrugBank.
- Avaliar a compatibilidade de via de administração (tópica) com a infecção folicular, que normalmente exige terapia sistêmica.
- Priorizar a avaliação de indicações mais específicas e melhor sustentadas (por exemplo, micose superficial), reconhecendo que representam uso já estabelecido.
- Verificar a situação regulatória atual, dado que não há registros vigentes no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

