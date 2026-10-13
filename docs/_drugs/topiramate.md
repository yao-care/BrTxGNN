---
layout: default
title: Topiramate
parent: Apenas Predição do Modelo (L5)
nav_order: 647
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

# Topiramato: Do uso anticonvulsivante ao neoplasma do nervo trigêmeo

## Resumo em Uma Frase

Topiramato é um medicamento anticonvulsivante, registrado no Brasil para o tratamento de crises epilépticas.
O modelo TxGNN prevê que pode ser eficaz para **neoplasma do nervo trigêmeo (trigeminal nerve neoplasm)**, com pontuação de 99,70%. No entanto, **não há ensaios clínicos nem publicações** que apoiem essa direção; a previsão se baseia apenas no modelo.

> Observação importante: entre as previsões disponíveis, as indicações seguintes (crises reflexas, como epilepsia visual e crises provocadas por audição, leitura ou alimentação) são biologicamente muito mais plausíveis. Elas são discutidas ao final do relatório.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Neoplasma do nervo trigêmeo (trigeminal nerve neoplasm) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados compilados sobre o mecanismo de ação. Segundo informações conhecidas, o topiramato atua por bloqueio de canais de sódio, potencialização da ação do GABA-A, antagonismo de receptores glutamatérgicos AMPA/cainato e inibição da anidrase carbônica. Esses mecanismos explicam seu efeito em crises epilépticas.

**Para o neoplasma do nervo trigêmeo, a previsão não encontra respaldo mecanístico nos dados disponíveis.** Nenhuma dessas ações tem relevância antineoplásica estabelecida. O escore alto (0,997) reflete apenas padrões no grafo de conhecimento do modelo. Qualquer benefício se limitaria ao alívio sintomático (dor trigeminal ou crises), sem controle do tumor.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Todos os registros encontrados estão cancelados. Não há registro vigente.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155370023 | Topiramato | — | Anticonvulsivantes |
| Registro nº 155370024 | Arasid | — | Anticonvulsivantes |
| Registro nº 112363327 | Topamax | — | Anticonvulsivantes |
| Registro nº 100430959 | Amato | — | Anticonvulsivantes |
| Registro nº 100330158 | Égide | — | Anticonvulsivantes |

Há outros 15 registros cancelados (por exemplo, Toduze, Ritop, Têmpora e Vidmax), todos com a mesma indicação.

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** transtorno de ansiedade, transtorno neurótico, transtorno distímico, doença renal, piureter, doença hepática, doença da vesícula biliar, doença diarreica, hipertensão ocular, nefrolitíase (incluindo a suscetibilidade associada a SLC26A1), nefropatia aguda por urato, distúrbios de acidose, acidose metabólica, transtorno amnéstico e amnésia retrógrada.
- **Interações medicamentosas:** foram identificadas 100 interações; as principais entre as 20 listadas:
  - **Graves (Major):** metformina, hiosciamina, atropina, escopolamina, glicopirrônio, clidínio, diciclomina, mepenzolato, metescopolamina, propantelina e tróspio (anticolinérgicos em geral).
  - **Moderadas:** pioglitazona, morfina, dronabinol, fentermina, metoclopramida, fenilbutirato, nabilona, glibenclamida e fenilbutirato de glicerol.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para neoplasma do nervo trigêmeo é apenas do modelo (L5), sem ensaios, sem literatura e sem plausibilidade mecanística. Além disso, o medicamento não tem registro vigente no Brasil.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação e bulas da ANVISA (advertências e contraindicações).
- Evidência pré-clínica ou clínica de atividade antitumoral, se houver interesse nesta indicação.
- Esclarecer a situação regulatória (todos os registros estão cancelados).

### Outras previsões do modelo (para priorização)

| Doença prevista | Pontuação TxGNN | Nível | Observação |
|---|---|---|---|
| Epilepsia visual | 99,28% | L4 | Literatura geral de epilepsia; evidência indireta |
| Crises de pensamento | 99,21% | L4 | Revisões Cochrane de topiramato adjuvante em epilepsia parcial; indireta |
| Crises induzidas por micção | 99,21% | L4 | Literatura genérica; indireta |
| Crises alimentares | 99,21% | L4 | Literatura sobre transtornos alimentares, em grande parte fora do alvo |
| Crises audiogênicas | 99,21% | L4 | Modelos animais (DBA/2, GAERS) com efeito anticonvulsivante |
| Crises de leitura | 99,09% | L4 | Evidência indireta |
| Crises induzidas por orgasmo | 99,21% | L5 | Apenas previsão |
| Epilepsia de sobressalto | 99,21% | L5 | Apenas previsão |

Essas indicações são extensões do uso original em epilepsia e merecem ser tratadas como **perguntas de pesquisa**. Contudo, nenhuma tem ensaio clínico registrado, e a literatura recuperada é indireta.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

