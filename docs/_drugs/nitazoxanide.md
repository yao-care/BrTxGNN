---
layout: default
title: Nitazoxanide
parent: Apenas Predição do Modelo (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nitazoxanide: nova indicação prevista, Hiperamilasemia (hyperamylasemia) (nível de evidência L5). Indicação original: Antiparasitários"
monitor_inn: "Nitazoxanide"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "bubonic plague"]
---

# Nitazoxanide
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

## Nitazoxanida: De antiparasitário a hiperamilasemia
{: .text-alpha }

## Resumo em Uma Frase

Nitazoxanida é um antiparasitário, registrado na ANVISA na categoria "antiparasitários".
O modelo TxGNN prevê que pode ser eficaz para **hiperamilasemia (hyperamylasemia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão baseia-se apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiparasitários |
| Nova Indicação Prevista | Hiperamilasemia (hyperamylasemia) |
| Pontuação de Previsão TxGNN | 97,82% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados (nenhum registro vigente) |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a nitazoxanida (por meio do metabólito tizoxanida) é um agente antiparasitário e antiviral que inibe a enzima piruvato:ferredoxina oxidorredutase em organismos anaeróbios e modula vias do hospedeiro, como AMPK/mTOR e a resposta a proteínas mal enoveladas.

**Não foi identificado um vínculo mecanístico plausível** com a hiperamilasemia. Trata-se de um achado laboratorial (elevação da amilase sérica), e não de uma doença com alvo farmacológico definido. A pontuação alta do TxGNN provavelmente reflete proximidade no grafo de conhecimento, e não relevância biológica.

Outras indicações previstas, todas sem ensaios ou literatura, também carecem de justificativa mecanística sólida: síndrome de hiperviscosidade policlonal, analbuminemia congênita, incompatibilidade de grupo sanguíneo, doenças hematológicas pré-malignas, gamopatia monoclonal, peste septicêmica e peste bubônica. Para as condições hematológicas pré-malignas e a gamopatia monoclonal, há apenas um vínculo especulativo, baseado em efeitos antiproliferativos in vitro (vias Wnt/β-catenina, mTORC1 e STAT3).

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155840655 | Nitazoxanida | Não informada | Antiparasitários |
| Registro nº 135170032 | Nitazoxanida | Não informada | Antiparasitários |
| Registro nº 135170073 | Irosê | Não informada | Antiparasitários |
| Registro nº 101180647 | Nydda | Não informada | Antiparasitários |
| Registro nº 118190391 | Zoxylab | Não informada | Antiparasitários |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento (não da bula)**: o grafo de conhecimento do TxGNN associa o fármaco a contraindicações em doença renal, piureter, doença hepática, doença da vesícula biliar, diabetes mellitus e cetoacidose diabética. Esses itens precisam ser confirmados na bula.
- **Interações medicamentosas**: foram identificadas 22 interações, todas de nível moderado (20 detalhadas nos dados compilados):
  - **Sulfonilureias** (acetohexamida, clorpropamida, glimepirida, glipizida, glibenclamida, tolazamida, tolbutamida): risco potencial de hipoglicemia.
  - **Anticoagulantes** (varfarina, dicumarol): risco potencial de aumento do efeito anticoagulante.
  - **Benzodiazepínicos** (ácido clorazépico, diazepam, estazolam, flurazepam, lorazepam, midazolam, oxazepam, quazepam).
  - **Outros**: lidocaína, metotrexato e fenitoína.

Os dados de advertências e contraindicações da bula não estavam disponíveis. Consulte a bula para informações complementares de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a hiperamilasemia (nível L5), e a análise não identificou vínculo mecanístico plausível. A pontuação alta do modelo parece ser um artefato do grafo de conhecimento.
- Além disso, todos os 20 registros brasileiros estão cancelados, o que limita a viabilidade regulatória imediata.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pendência que bloqueia a triagem de segurança.
- Complementar os dados do mecanismo de ação (por exemplo, via consulta ao DrugBank).
- Verificar se a hiperamilasemia é um alvo terapêutico legítimo, já que se trata de um achado laboratorial, e não de uma doença.
- Realizar uma busca sistemática de literatura e de ensaios clínicos; sem evidência pré-clínica ou clínica, não se recomenda avançar.
- Avaliar o status regulatório (registros cancelados) e a compatibilidade de via de administração caso a indicação venha a ser reconsiderada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

