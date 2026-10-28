---
layout: default
title: Norelgestromin
parent: Apenas Predição do Modelo (L5)
nav_order: 477
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Norelgestromin: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L5). Indicação original: Anticoncepcionais"
monitor_inn: "norelgestromin"
predicted_indications: ["amenorrhea (disease)"]
---

# Norelgestromin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Norelgestromina: Do contraceptivo transdérmico à amenorreia
{: .text-alpha }

## Resumo em Uma Frase

Norelgestromina é um progestágeno, metabólito ativo do norgestimato, usado originalmente como anticoncepcional (adesivo transdérmico EVRA, associado ao etinilestradiol).
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (amenorrhea)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticoncepcionais |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 0,9951 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados. Segundo informações conhecidas, a norelgestromina é o metabólito progestágeno ativo do norgestimato e é liberada em adesivo transdérmico contraceptivo junto com etinilestradiol. Sua atividade progestogênica (agonismo do receptor de progesterona) suprime a liberação de gonadotrofinas e estabiliza o endométrio, o que é biologicamente plausível para distúrbios menstruais de origem hormonal.

A relação entre a indicação original e a nova é frágil. A amenorreia é um efeito conhecido da contracepção hormonal, e não um alvo terapêutico claramente estabelecido. Além disso, a direção do efeito é ambígua: induzir amenorreia (efeito desejado ou tolerado em alguns contextos) é diferente de tratar a amenorreia patológica, em que progestágenos exógenos servem principalmente para provocar sangramento por privação ou proteger o endométrio, e não para restaurar a ovulação.

A pontuação muito alta (0,9951) é uma previsão baseada em modelo e pode refletir a associação da classe do fármaco com condições menstruais e reprodutivas, e não evidência independente.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 191290002 (cancelado) | EVRA | Não informada | Anticoncepcionais |

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento (não extraídas da bula)**: o grafo de conhecimento do TxGNN (PrimeKG) associa o fármaco a contraindicações em diversas condições, entre elas:
  - Cardiovasculares e metabólicas: hipertensão, doença arterial coronariana, tromboflebite, hiperlipidemia (inclusive familial), hipertrigliceridemia, diabetes mellitus, cetoacidose diabética e hiperglicemia.
  - Hepáticas, biliares e renais: doença hepática, doença da vesícula biliar e doença renal.
  - Neurológicas e psiquiátricas: epilepsia, enxaqueca, transtornos de ansiedade, transtornos neuróticos e distimia.
  - Outras: porfirias, lúpus eritematoso sistêmico (inclusive pediátrico), asma (formas intrínseca e alérgica) e carcinoma de mama feminino.
- **Interações Medicamentosas**: foi identificada 1 interação de gravidade **Maior** com **sugamadex** (fonte: DDInter).

As advertências e contraindicações da bula não estavam disponíveis nos dados compilados para este relatório. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para amenorreia (nível L5, apenas previsão do modelo).
- O mecanismo é incerto e a direção do efeito é ambígua.
- O único registro brasileiro está cancelado.
- O perfil de contraindicações é extenso e não pôde ser confirmado pela bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem ela.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar busca sistemática de literatura e de ensaios clínicos sobre progestágenos no tratamento da amenorreia.
- Definir se o objetivo é induzir amenorreia ou tratar amenorreia patológica.
- Avaliar a viabilidade regulatória e de via de administração, já que o registro atual está cancelado.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

