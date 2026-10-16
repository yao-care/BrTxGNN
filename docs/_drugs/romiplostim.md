---
layout: default
title: Romiplostim
parent: Apenas Predição do Modelo (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Romiplostim: nova indicação prevista, Distúrbio primário de liberação plaquetária (primary release disorder… (nível de evidência L5). Indicação original: Anemia aplástica idiopática…"
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
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

# Romiplostim: Da anemia aplástica e trombocitopenia autoimune a distúrbio de liberação plaquetária (previsão primária)

## Resumo em Uma Frase

Romiplostim é um agonista do receptor de trombopoietina, originalmente associado ao tratamento de anemia aplástica (incluindo a forma idiopática) e de trombocitopenia autoimune.
O modelo TxGNN prevê que pode ser eficaz para **distúrbio primário de liberação plaquetária (primary release disorder of platelets)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (sobre um tema diferente, a trombocitopenia imune) ligada a esta direção. A previsão é, portanto, essencialmente teórica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anemia aplástica idiopática, anemia aplástica e trombocitopenia autoimune (conforme o grafo de conhecimento; não há texto de indicação aprovado no Brasil) |
| Nova Indicação Prevista | Distúrbio primário de liberação plaquetária (primary release disorder of platelets) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, o romiplostim é um peptídeo agonista do receptor de trombopoietina (MPL), que estimula a maturação dos megacariócitos e aumenta a produção de plaquetas. Seu uso estabelecido é na trombocitopenia imune (PTI) crônica, e a farmacologia o relaciona ao receptor MPL.

A relação com a nova indicação é fraca. O distúrbio de liberação plaquetária é um defeito de **função** (secreção de grânulos), e não de **contagem** de plaquetas. Aumentar a produção dificilmente corrigiria esse defeito funcional. O único artigo encontrado trata de PTI, na qual autoanticorpos inibem a formação de pró-plaquetas, e não da doença prevista.

A pontuação muito alta do TxGNN provavelmente reflete a proximidade na rede do conhecimento com a PTI e com nós relacionados a plaquetas, e não evidência de benefício clínico.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Pesquisa básica/mecanística (PTI) | Haematologica | Em estudo in vitro, soro e IgG de pacientes com PTI inibiram a formação de pró-plaquetas pelos megacariócitos e prejudicaram a produção de plaquetas. Trata-se de outra doença, não do distúrbio de liberação plaquetária. |

## Outras Indicações Previstas (Contexto)

| Posição | Doença prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|------|
| 2 | Pseudo-doença de von Willebrand | 99,99% | L5 | Defeito de ganho de função da GPIb; sem vínculo mecanístico nem evidências |
| 3 | Trombastenia de Glanzmann | 99,99% | L5 | Defeito qualitativo (integrina αIIbβ3) com contagem normal; risco trombótico sem benefício claro |
| 4 | Trombocitopenia aloimune fetal e neonatal | 99,99% | L4 | Evidência indireta: extrapolação da PTI, relatos de caso e revisões; nenhum estudo avalia romiplostim na doença; faltam dados de segurança fetal e de transferência placentária |
| 5 | Síndrome de Scott | 99,97% | L5 | Defeito funcional (TMEM16F/ANO6); sem evidências |
| 6 | Doença hemorrágica por trombocitopenia constitucional | 99,95% | L5 | Categoria ampla; alguns subtipos podem responder, sem dados específicos |
| 7 | Diátese hemorrágica por defeito de receptor de colágeno | 99,95% | L5 | Defeito qualitativo; sem evidências |
| 8 | Distúrbio hemorrágico do tipo plaquetário | 99,93% | L5 | Grupo genérico; provável efeito de proximidade no grafo |
| 9 | Macrotrombocitopenia autossômica dominante | 99,88% | L5 | Hipotético em algumas formas hereditárias; sem evidências |
| 10 | Síndrome de Ehlers-Danlos, tipo fibronectinêmico | 99,85% | L5 | Sem vínculo plausível; provável artefato da rede |

Entre as alternativas, a **trombocitopenia aloimune fetal e neonatal** é a única com racionalidade conceitual (L4), derivada das seis publicações recuperadas, todas sobre PTI ou agentes trombopoéticos em geral (revisões, relatos de caso e um relato com eltrombopague, outro fármaco). Ela pode merecer uma pergunta de pesquisa específica.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 2 entradas. A interação de nível **Maior** é com o **carfilzomibe**. Além disso, o romiplostim atua sobre o receptor de trombopoietina (MPL), por farmacologia.

Para as demais informações de segurança (advertências e contraindicações), consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal não tem ensaios clínicos, e a única publicação trata de outra doença (PTI). O mecanismo (aumentar a contagem de plaquetas) não corrige um defeito de função plaquetária, e o fármaco não possui registro no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois o fármaco não tem registro local.
- Complementar os dados do mecanismo de ação (MOA) a partir do DrugBank.
- Avaliar, como pergunta de pesquisa separada, a trombocitopenia aloimune fetal e neonatal, com dados de segurança fetal e de transferência placentária.
- Verificar se há qualquer estudo direto do romiplostim em distúrbios de liberação plaquetária antes de qualquer avanço.
- Confirmar a situação regulatória do romiplostim no Brasil (ausência de registros nos dados compilados).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

