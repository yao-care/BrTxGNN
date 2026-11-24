---
layout: default
title: Evolocumab
parent: Apenas Predição do Modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
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

## Evolocumabe: De antilipêmico a forma sintomática de hemofilia em portadoras do sexo feminino (previsão sem respaldo clínico)
{: .text-alpha }

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
| Pontuação de Previsão TxGNN | 0,9982 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Evolocumab (tradução não oficial): “O evolocumabe é uma IgG2 monoclonal humana dirigida contra a pró-proteína convertase subtilisina/kexina tipo 9 (PCSK9) humana. A PCSK9 liga-se ao receptor de lipoproteína de baixa densidade (LDLR) na superfície dos hepatócitos para promover a degradação do LDLR no fígado.” Texto original em inglês: "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), versão de 2026-10-12; acessado em 2026-11-19). Segundo informações conhecidas, o evolocumabe é um anticorpo monoclonal que se liga à PCSK9 (proproteína convertase subtilisina/kexina tipo 9), aumentando a disponibilidade de receptores de LDL e reduzindo o LDL-colesterol. Foi aprovado na Europa (julho de 2015) e nos EUA (agosto de 2015) para hipercolesterolemia familiar heterozigótica e homozigótica e para hipercolesterolemia primária não familiar.

**Não foi identificada relação mecanística plausível** entre a inibição da PCSK9 e a deficiência dos fatores VIII/IX ligada ao X em portadoras. A pontuação muito alta (0,9982) vem do modelo TxGNN (deep learning) e pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica; não há respaldo em qualquer ensaio clínico ou publicação. A similaridade com a indicação original não foi avaliada.

### Outras previsões avaliadas

Todas as previsões a seguir também têm nível de evidência L5, sem ensaios nem literatura, e recomendação **Hold**:

| Posição | Indicação prevista | Pontuação TxGNN | Avaliação do vínculo mecanístico |
|------|------|------|------|
| 2 | Deficiência familiar de apolipoproteína C-II | 0,9950 | Vínculo lipídico, porém fraco: a deficiência causa quilomicronemia e hipertrigliceridemia grave, e a inibição da PCSK9 atua principalmente sobre o LDL-C, com efeito limitado sobre quilomícrons |
| 3 | Púrpura trombocitopênica | 0,9942 | Nenhum vínculo estabelecido |
| 4 | Deficiência de fator XI | 0,9929 | Sem mecanismo plausível; o fármaco não atua na cascata de coagulação |
| 5 | Hemofilia A com anormalidade vascular | 0,9922 | Sem efeito conhecido sobre o fator VIII; a pontuação do modelo TxGNN (deep learning) pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica |
| 6 | Doença de atividade catalítica | 0,9908 | Categoria ampla e inespecífica de ontologia, não avaliável como indicação |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102440007 | REPATHA | AMGEN BIOTECNOLOGIA DO BRASIL LTDA. | Ativo |

<!-- licenses:end -->

---

## Considerações de Segurança

- **Interações Medicamentosas**: foi registrada apenas uma relação farmacológica, com o alvo PCSK9 (o próprio alvo terapêutico do evolocumabe), sem classificação de gravidade. Não se trata de interação medicamentosa clinicamente relevante.

Os dados de advertências e contraindicações da bula não estavam disponíveis. Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão não tem nenhum ensaio clínico ou publicação, não há vínculo mecanístico plausível com a deficiência de fatores de coagulação, e a alta pontuação do modelo TxGNN (deep learning) pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica. No Brasil, o medicamento é comercializado, com 1 registro válido de 1.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pendência que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (consulta ao DrugBank)
- Justificar biologicamente o vínculo entre a inibição da PCSK9 e a hemostasia, antes de qualquer estudo
- Se houver interesse em reposicionamento, priorizar indicações com maior plausibilidade biológica em vez das previsões listadas, todas com evidência L5
- Esclarecer a situação regulatória do produto no Brasil

<!-- review:begin br-lic-20261031-evolocumab-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecer a situação regulatória do produto no Brasil (registro cancelado)” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-evolocumab-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registro cancelado)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

