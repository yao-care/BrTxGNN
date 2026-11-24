---
layout: default
title: Norelgestromin
parent: Apenas Predição do Modelo (L5)
nav_order: 477
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
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
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para norelgestromin and ethinyl estradiol (associação que contém Norelgestromin) (tradução não oficial): “A NGMN é o progestagênio ativo amplamente responsável pela atividade progestacional que ocorre em mulheres após a aplicação do sistema transdérmico de norelgestromina e etinilestradiol.” Texto original em inglês: "NGMN is the active progestin largely responsible for the progestational activity that occurs in women following application of norelgestromin and ethinyl estradiol transdermal system." ([DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02), versão de 2026-04-16; acessado em 2026-11-19). Segundo informações conhecidas, a norelgestromina é o metabólito progestágeno ativo do norgestimato e é liberada em adesivo transdérmico contraceptivo junto com etinilestradiol. Sua atividade progestogênica (agonismo do receptor de progesterona) suprime a liberação de gonadotrofinas e estabiliza o endométrio, o que é biologicamente plausível para distúrbios menstruais de origem hormonal.

A relação entre a indicação original e a nova é frágil. A amenorreia é um efeito conhecido da contracepção hormonal, e não um alvo terapêutico claramente estabelecido. Além disso, a direção do efeito é ambígua: induzir amenorreia (efeito desejado ou tolerado em alguns contextos) é diferente de tratar a amenorreia patológica, em que progestágenos exógenos servem principalmente para provocar sangramento por privação ou proteger o endométrio, e não para restaurar a ovulação.

A pontuação muito alta (0,9951) é uma previsão baseada em modelo e pode refletir a associação da classe do fármaco com condições menstruais e reprodutivas, e não evidência independente.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 191290002 | EVRA | GEDEON RICHTER DO BRASIL IMPORTADORA, EXPORTADORA  | Ativo |
| 112363359 | EVRA | JANSSEN-CILAG FARMACÊUTICA LTDA | Cancelado |

<!-- licenses:end -->

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
- O perfil de contraindicações é extenso e não pôde ser confirmado pela bula.

<!-- review:begin br-lic-20261106-norelgestromin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O mecanismo é incerto e a direção do efeito é ambígua. / O único registro brasileiro está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-norelgestromin-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem ela.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar busca sistemática de literatura e de ensaios clínicos sobre progestágenos no tratamento da amenorreia.
- Definir se o objetivo é induzir amenorreia ou tratar amenorreia patológica.
- Avaliar a viabilidade regulatória e de via de administração.

<!-- review:begin br-lic-20261106-norelgestromin-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Avaliar a viabilidade regulatória e de via de administração, já que o registro atual está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-norelgestromin-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O único registro brasileiro está cancelado” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que o registro atual está cancelado” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

