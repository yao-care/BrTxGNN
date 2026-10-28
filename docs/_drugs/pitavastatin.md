---
layout: default
title: Pitavastatin
parent: Apenas Predição do Modelo (L5)
nav_order: 530
evidence_level: L5
indication_count: 4
monitor_inn: "pitavastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-10-28
description: "Pitavastatin: nova indicação prevista, Deficiência da proteína de transferência de ésteres de colesterol (pr… (nível de evidência L5). Indicação original: Antilipêmicos"
---

# Pitavastatin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Pitavastatina: De antilipêmico à deficiência da proteína de transferência de ésteres de colesterol
{: .text-alpha }

## Resumo em Uma Frase

Pitavastatina é uma estatina, registrada no Brasil como antilipêmico (medicamento para reduzir lipídios no sangue).
O modelo TxGNN prevê, com maior pontuação bruta, **deficiência da proteína de transferência de ésteres de colesterol (CETP)**, mas essa previsão não tem nenhum estudo de apoio. A direção com mais respaldo é **infecção por HIV (HIV infectious disease)**, com **1 ensaio clínico** e **18 publicações**; porém, o benefício demonstrado é na prevenção de doença cardiovascular em pessoas com HIV, e não no tratamento do vírus.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Deficiência da proteína de transferência de ésteres de colesterol (primeira da lista de previsões); a previsão mais bem sustentada por evidências é HIV |
| Pontuação de Previsão TxGNN | 0,9998 (CETP); 0,9997 (HIV) |
| Nível de Evidência | L5 para a deficiência de CETP; L1 para HIV (ver observação abaixo) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 7) |
| Número de Registros | 7 (ativos: 7) |
| Decisão Recomendada | Hold para a deficiência de CETP; Proceed with Guardrails para HIV |

*Observação:* a previsão de maior pontuação (CETP) não tem ensaios nem publicações. O restante do relatório detalha a previsão de HIV, que concentra todas as evidências disponíveis. Como o estudo principal (REPRIEVE) foi um ensaio randomizado de fase 3 concluído, mas o ensaio listado nos dados compilados é apenas indiretamente relacionado, a classificação L1 se apoia na publicação do REPRIEVE (NEJM 2023) e em seus subestudos.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a pitavastatina pertence à classe das estatinas (inibidores da HMG-CoA redutase), com eficácia reconhecida na redução de lipídios, e mecanisticamente pode ser aplicável a populações com risco cardiovascular elevado.

Pessoas com HIV têm risco cardiovascular cerca de 50% maior do que pessoas sem HIV, por causa de inflamação crônica, ativação imune e efeitos metabólicos da terapia antirretroviral. As estatinas reduzem o LDL-colesterol e têm efeitos anti-inflamatórios e de estabilização de placas. O subestudo mecanístico do REPRIEVE (JAMA Cardiology, 2024) mostrou efeitos da pitavastatina sobre a doença arterial coronariana e biomarcadores inflamatórios.

**Ressalva importante:** a pitavastatina não é antiviral e não trata a infecção por HIV. A indicação deve ser formulada como redução do risco cardiovascular em pessoas com HIV. A relação com a deficiência de CETP (condição genética com HDL-C elevado, geralmente sem necessidade de estatina), com o transtorno do neurodesenvolvimento raro e com a síndrome da imunodeficiência felina (doença veterinária) é especulativa ou sem relevância clínica humana.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06317051](https://clinicaltrials.gov/study/NCT06317051) | Phase 3/4 | Ativo, sem recrutamento | 300 | Ensaio fatorial: dapagliflozina vs placebo e rosuvastatina/ezetimiba vs pitavastatina em pessoas com HIV em uso de inibidores de integrase e risco metabólico elevado. Relevância indireta; conclusão prevista para dezembro de 2027 |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37486775](https://pubmed.ncbi.nlm.nih.gov/37486775/) | 2023 | RCT | N Engl J Med | Ensaio REPRIEVE: pitavastatina para prevenção de doença cardiovascular em pessoas com HIV |
| [38381407](https://pubmed.ncbi.nlm.nih.gov/38381407/) | 2024 | RCT (subestudo mecanístico) | JAMA Cardiol | Pitavastatina reduziu eventos cardiovasculares maiores (MACE) em 35% em mediana de 5,1 anos; efeitos sobre placa coronariana e biomarcadores inflamatórios |
| [39661372](https://pubmed.ncbi.nlm.nih.gov/39661372/) | 2025 | Análise secundária de RCT | JAMA Cardiol | Vias de procolágeno e estabilização de placa com pitavastatina |
| [40482662](https://pubmed.ncbi.nlm.nih.gov/40482662/) | 2025 | Coorte (dentro de RCT) | Lancet HIV | Associação entre uso de antirretrovirais e MACE no REPRIEVE |
| [41195533](https://pubmed.ncbi.nlm.nih.gov/41195533/) | 2026 | Coorte (análise secundária) | Arterioscler Thromb Vasc Biol | Hematopoese clonal e eventos cardíacos maiores em pessoas com HIV |
| [41378479](https://pubmed.ncbi.nlm.nih.gov/41378479/) | 2025 | Análise do REPRIEVE | J Am Heart Assoc | ECG basal e desfechos cardiovasculares em pessoas com HIV |
| [38294226](https://pubmed.ncbi.nlm.nih.gov/38294226/) | 2025 | Revisão | Cardiol Rev | Pitavastatina na prevenção de doença cardiovascular em pessoas vivendo com HIV |
| [42127259](https://pubmed.ncbi.nlm.nih.gov/42127259/) | 2026 | Revisão | Top Antivir Med | Comorbidades do HIV na CROI 2026, incluindo análises do REPRIEVE |
| [29804227](https://pubmed.ncbi.nlm.nih.gov/29804227/) | 2018 | Revisão | Curr Infect Dis Rep | Benefícios e riscos da terapia com estatinas na população com HIV |
| [37991867](https://pubmed.ncbi.nlm.nih.gov/37991867/) | 2023 | Correspondência | N Engl J Med | Comentário sobre o ensaio REPRIEVE |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 109740355 | Pitavastatina Cálcica | — | Antilipêmicos |
| Registro 141070657 | Pitavastatina Cálcica | — | Antilipêmicos |
| Registro 103720245 | Lester | — | Antilipêmicos |
| Registro 100330206 | Ebatz | — | Antilipêmicos |
| Registro 100431355 | Pivast | — | Antilipêmicos |

Há 7 registros válidos de medicamento de ingrediente único; os 5 principais estão listados acima (os demais: 100431110, Pitavastatina Cálcica, e 109740346, Livalo).

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não provêm da bula): doença hepática, doença da vesícula biliar, hipotireoidismo, mixedema, hipotireoidismo congênito, miopatia, doenças musculares, paralisia periódica familiar, distúrbios hipotensivos, rabdomiólise, fasciite nodular, insuficiência renal e lesões.
- **Interações medicamentosas**: foram registradas 86 interações. Entre as listadas, a de gravidade **maior** é com **eritromicina**. Entre as moderadas estão rosuvastatina, sinvastatina, cobicistate, eltrombopague, cloroquina, hidroxicloroquina, metronidazol, naltrexona, dissulfiram e etanol. Varfarina e dicumarol têm interação leve. Em pessoas com HIV, a coadministração com antirretrovirais (por exemplo, alguns inibidores de protease e o cobicistate) exige revisão.
- Em contexto de HIV, recomenda-se monitorar toxicidade muscular e efeitos sobre a glicemia.

Para advertências e contraindicações de bula, consulte a bula aprovada pela ANVISA.

## Conclusão e Próximos Passos

**Decisão: Hold (deficiência de CETP) / Proceed with Guardrails (HIV, como prevenção cardiovascular)**

**Justificativa:**
- A previsão de maior pontuação (CETP) é apenas do modelo, sem estudos, e não há necessidade terapêutica clara. Já para pessoas com HIV, há um grande ensaio randomizado (REPRIEVE) e vários subestudos mostrando redução de eventos cardiovasculares, mas o benefício se refere à prevenção cardiovascular, não ao tratamento do HIV.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), ausente nos dados compilados.
- Complementar os dados de mecanismo de ação.
- Confirmar a identificação do REPRIEVE e seus dados de registro, que não constam da lista de ensaios.
- Avaliar o registro de uma indicação específica de prevenção cardiovascular em pessoas com HIV, evitando qualquer sugestão de efeito antiviral.
- Definir plano de revisão de interações com terapia antirretroviral e monitoramento de segurança muscular e glicêmica.
- Descartar as previsões de transtorno do neurodesenvolvimento raro e de imunodeficiência felina por falta de evidência ou relevância humana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

