---
layout: default
title: Pitavastatin
parent: Apenas Predição do Modelo (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatina: Da dislipidemia à hipercolesterolemia familiar homozigótica

## Resumo em Uma Frase

Pitavastatina cálcica é uma estatina, registrada na ANVISA como antilipêmico (redutor de lipídios no sangue).
O modelo TxGNN prevê que pode ser eficaz para **hipercolesterolemia familiar homozigótica (Homozygous Familial Hypercholesterolemia)**, mas, para essa indicação específica, há **0 ensaios clínicos** e apenas **2 publicações**, ambas indiretas (uma sobre dislipidemia em HIV e um relato de caso de outra condição).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Hipercolesterolemia familiar homozigótica (Homozygous Familial Hypercholesterolemia) |
| Pontuação de Previsão TxGNN | 99,996% |
| Nível de Evidência | L4 (classificação dos dados compilados para este relatório); pelas regras do prompt, tecnicamente L5, pois não há estudo direto |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 7 (todos cancelados) |
| Decisão Recomendada | Hold |

> Observação: outras previsões do mesmo fármaco têm evidência bem mais forte (ver "Conclusão e Próximos Passos"), mas esta avaliação segue a previsão de maior pontuação.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados para este fármaco. Segundo informações conhecidas, a pitavastatina é um inibidor da HMG-CoA redutase: reduz a síntese hepática de colesterol e aumenta os receptores hepáticos de LDL, o que diminui o LDL-colesterol. Sua eficácia como antilipêmico já é estabelecida.

A relação com a nova indicação é, em tese, direta: ambas envolvem colesterol elevado. Porém, na forma homozigótica da hipercolesterolemia familiar, a função do receptor de LDL é gravemente reduzida ou ausente. Assim, espera-se que a resposta às estatinas seja limitada e variável, pois é necessária alguma atividade residual do receptor. Na prática, a estatina costuma ser apenas adjuvante a inibidores de PCSK9, lomitapida ou aférese.

Portanto, o mecanismo é plausível, mas o benefício esperado é parcial. A pontuação alta do modelo não equivale a evidência clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Fase 4, indireto) | The Lancet HIV | Pitavastatina versus pravastatina em adultos com HIV-1 e dislipidemia (INTREPID); avalia segurança e eficácia. Não trata de HoFH |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Relato de caso | Journal of Clinical Lipidology | Dois casos de hipercolesterolemia autossômica recessiva (gene LDLRAP1), clinicamente indistinguível da HoFH, com resposta rápida de redução lipídica. É outra condição |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 109740355 | Pitavastatina Cálcica | Não informada | Antilipêmicos (cancelado) |
| Registro nº 141070657 | Pitavastatina Cálcica | Não informada | Antilipêmicos (cancelado) |
| Registro nº 103720245 | Lester | Não informada | Antilipêmicos (cancelado) |
| Registro nº 100330206 | Ebatz | Não informada | Antilipêmicos (cancelado) |
| Registro nº 100431355 | Pivast | Não informada | Antilipêmicos (cancelado) |

Há mais dois registros cancelados (nº 100431110, Pitavastatina Cálcica, e nº 109740346, Livalo), totalizando 7. Nenhum está vigente.

---

## Considerações de Segurança

- **Contraindicações e condições de risco (grafo de conhecimento, não texto de bula)**: doença hepática, doença da vesícula biliar, hipotireoidismo (incluindo mixedema e hipotireoidismo congênito), miopatia e doenças musculares, paralisia periódica familiar, distúrbios hipotensivos, rabdomiólise, fasciite nodular, insuficiência renal e lesões.
- **Interações medicamentosas**: foram identificadas 86 interações. Entre as principais:
  - **Grave**: eritromicina.
  - **Moderada**: rosuvastatina, sinvastatina, cobicistate, eltrombopague, eluxadolina, naltrexona, metronidazol, tinidazol, secnidazol, benznidazol, etanol, dissulfiram, cloroquina, hidroxicloroquina, zafirlucaste, cloranfenicol e dapsona.
  - **Leve**: varfarina e dicumarol.

Consulte a bula para advertências e contraindicações oficiais, pois não há dados de bula disponíveis.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaio clínico nem estudo direto em HoFH, e a fisiopatologia (receptor de LDL ausente ou muito reduzido) sugere eficácia limitada da estatina.
- Não há registro vigente no Brasil, e faltam dados de bula e de mecanismo de ação.

**Para prosseguir, é necessário:**
- Dados de eficácia de pitavastatina em pacientes com HoFH confirmada (estudos específicos, inclusive como adjuvante a PCSK9, lomitapida ou aférese).
- Obter e analisar a bula na ANVISA (advertências e contraindicações) e o mecanismo de ação no DrugBank.
- Verificar a disponibilidade local, já que todos os 7 registros estão cancelados.

**Previsões alternativas com evidência mais forte (para priorização):**
- **Hiperlipoproteinemia** (pontuação 99,995%; nível L1): estudos de Fase 3 e Fase 4 controlados com comparador ativo. Trata-se praticamente da indicação original, não de reposicionamento. Recomendação: *Proceed with Guardrails*, com atenção à carga de interações e ao status de mercado.
- **Hipercolesterolemia familiar** (99,988%; L2) e **hipercolesterolemia autossômica dominante** (99,975%; L2): estudos pediátricos e de longo prazo apoiam eficácia e segurança, mas o único ensaio listado (Fase 2, anticorpo anti-PCSK9) é indireto. *Proceed with Guardrails*.
- **Infecção por HIV** (99,967%; L1): trata-se de prevenção cardiovascular, não de tratamento do vírus. O ensaio REPRIEVE (NEJM 2023) mostrou redução de eventos cardiovasculares maiores com pitavastatina. *Proceed with Guardrails*, com monitoramento de interações com antirretrovirais, glicemia e sintomas musculares.
- **Deficiência de CETP, deficiência de colesterol 7-alfa-hidroxilase, transtorno do neurodesenvolvimento raro, deficiência de lipase hepática e síndrome da imunodeficiência adquirida felina**: sem estudos, apoio apenas computacional (L5). *Hold*; a última é condição veterinária, sem relevância clínica humana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

