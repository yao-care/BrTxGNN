---
layout: default
title: Evolocumab
parent: Apenas Predição do Modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Evolocumab: nova indicação prevista, Forma sintomática de hemofilia em portadoras do sexo feminino (sympto… (nível de evidência L5). Indicação original: Antilipêmicos"
monitor_inn: "evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

# Evolocumabe: De antilipêmico a hemofilia sintomática em portadoras (previsão sem respaldo clínico)

## Resumo em Uma Frase

Evolocumabe é um anticorpo monoclonal inibidor da PCSK9, originalmente registrado no Brasil como antilipêmico (redução do colesterol).
O modelo TxGNN prevê que pode ser eficaz para **forma sintomática de hemofilia em portadoras do sexo feminino (symptomatic form of hemophilia in female carriers)**,
mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Forma sintomática de hemofilia em portadoras do sexo feminino (symptomatic form of hemophilia in female carriers) |
| Pontuação de Previsão TxGNN | 99,82% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o evolocumabe é um anticorpo monoclonal que se liga à PCSK9 (proproteína convertase subtilisina/kexina tipo 9), aumentando a disponibilidade de receptores de LDL e reduzindo o LDL-colesterol. Foi aprovado na Europa (julho de 2015) e nos EUA (agosto de 2015) para hipercolesterolemia familiar heterozigótica e homozigótica e para hipercolesterolemia primária não familiar.

**Não foi identificada relação mecanística plausível** entre a inibição da PCSK9 e a deficiência dos fatores VIII/IX ligada ao X em portadoras. A pontuação TxGNN muito alta (0,998) parece ser um artefato do grafo de conhecimento, sem respaldo em qualquer ensaio clínico ou publicação. A similaridade com a indicação original não foi avaliada.

### Outras previsões avaliadas

Todas as previsões a seguir também têm nível de evidência L5, sem ensaios nem literatura, e recomendação **Hold**:

| Posição | Indicação prevista | Pontuação TxGNN | Avaliação do vínculo mecanístico |
|------|------|------|------|
| 2 | Deficiência familiar de apolipoproteína C-II | 99,50% | Vínculo lipídico, porém fraco: a deficiência causa quilomicronemia e hipertrigliceridemia grave, e a inibição da PCSK9 atua principalmente sobre o LDL-C, com efeito limitado sobre quilomícrons |
| 3 | Púrpura trombocitopênica | 99,42% | Nenhum vínculo estabelecido |
| 4 | Deficiência de fator XI | 99,29% | Sem mecanismo plausível; o fármaco não atua na cascata de coagulação |
| 5 | Hemofilia A com anormalidade vascular | 99,22% | Sem efeito conhecido sobre o fator VIII; provável viés de vizinhança no grafo |
| 6 | Doença de atividade catalítica | 99,08% | Categoria ampla e inespecífica de ontologia, não avaliável como indicação |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada | Situação |
|---------|------|------|-----------|------|
| Registro nº 102440007 | REPATHA | Não informada | Antilipêmicos | Cancelado |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foi registrada apenas uma relação farmacológica, com o alvo PCSK9 (o próprio alvo terapêutico do evolocumabe), sem classificação de gravidade. Não se trata de interação medicamentosa clinicamente relevante.

Os dados de advertências e contraindicações da bula não estavam disponíveis. Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão não tem nenhum ensaio clínico ou publicação, não há vínculo mecanístico plausível com a deficiência de fatores de coagulação, e a alta pontuação do TxGNN parece ser artefato do grafo de conhecimento. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pendência que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (consulta ao DrugBank)
- Justificar biologicamente o vínculo entre a inibição da PCSK9 e a hemostasia, antes de qualquer estudo
- Se houver interesse em reposicionamento, priorizar indicações com maior plausibilidade biológica em vez das previsões listadas, todas com evidência L5
- Esclarecer a situação regulatória do produto no Brasil (registro cancelado)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

