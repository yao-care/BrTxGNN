---
layout: default
title: Galcanezumab
parent: Apenas Predição do Modelo (L5)
nav_order: 333
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Galcanezumab: nova indicação prevista, Deficiência de Cofator 2 da Heparina (Heparin Cofactor 2 Deficiency) (nível de evidência L5). Indicação original: Outras preparações antienxaqueca"
monitor_inn: "galcanezumab"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Galcanezumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Galcanezumabe: De preparações antienxaqueca para deficiência de cofator 2 da heparina
{: .text-alpha }

## Resumo em Uma Frase

Galcanezumabe é um anticorpo monoclonal originalmente usado na prevenção da enxaqueca (registrado na ANVISA como "outras preparações antienxaqueca").
O modelo TxGNN prevê que pode ser eficaz para **Deficiência de Cofator 2 da Heparina (Heparin Cofactor 2 Deficiency)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outras preparações antienxaqueca |
| Nova Indicação Prevista | Deficiência de Cofator 2 da Heparina (Heparin Cofactor 2 Deficiency) |
| Pontuação de Previsão TxGNN | 0,9950 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Galcanezumab (tradução não oficial): “O galcanezumabe-gnlm é um anticorpo monoclonal humanizado que se liga ao ligante peptídeo relacionado ao gene da calcitonina (CGRP) e bloqueia sua ligação ao receptor.” Texto original em inglês: "Galcanezumab-gnlm is a humanized monoclonal antibody that binds to calcitonin gene-related peptide (CGRP) ligand and blocks its binding to the receptor." ([DailyMed: Emgality (galcanezumab-gnlm) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33a147be-233a-40e8-a55e-e40936e28db0), versão de 2026-06-05; acessado em 2026-11-19). Segundo informações conhecidas, o galcanezumabe é um anticorpo monoclonal que neutraliza o peptídeo relacionado ao gene da calcitonina (CGRP) e é usado na prevenção da enxaqueca.

Não foi identificado vínculo mecanístico crível com a nova indicação. O cofator II da heparina é uma serpina que inibe a trombina de forma dependente de dermatan sulfato/heparina. As vias do CGRP e da inibição da coagulação mediada por serpinas não se sobrepõem, e um anticorpo anti-CGRP não repõe uma proteína plasmática deficiente.

A pontuação elevada do TxGNN (0,9950) vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica, clínica ou bibliográfica.

### Outras previsões avaliadas

| Posição | Indicação prevista | Pontuação TxGNN | Nível de Evidência | Recomendação |
|------|------|------|------|------|
| 2 | Deficiência de antitrombina tipo 2 | 0,9941 | L5 | Hold |
| 3 | Excesso de fator V com trombose espontânea | 0,9941 | L5 | Hold |

Em ambas, também não há vínculo mecanístico crível. No caso do excesso de fator V, os inibidores da via do CGRP têm considerações vasculares (vasoconstrição, hipertensão e eventos tipo Raynaud relatados no pós-comercialização). Qualquer interação com doença trombótica seria, portanto, uma preocupação de segurança, e não uma oportunidade terapêutica.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330224 | EMGALITY | LIBBS FARMACÊUTICA LTDA | Ativo |
| 112600200 | EMGALITY | ELI LILLY DO BRASIL LTDA | Cancelado |

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem literatura, e o mecanismo do galcanezumabe (bloqueio do CGRP) não tem relação plausível com a deficiência de cofator 2 da heparina.

<!-- review:begin br-lic-20261106-galcanezumab-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Não há ensaios clínicos nem literatura, e o mecanismo do galcanezumabe (bloqueio do CGRP) não tem relação plausível com a deficiência de cofator 2 da heparina. Além disso, o único registro no Brasil está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-galcanezumab-2 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois essa lacuna impede a triagem de segurança
- Complementar os dados do mecanismo de ação via DrugBank
- Apresentar justificativa biológica ou dados pré-clínicos que sustentem a hipótese, caso se queira reavaliar
- Esclarecer a situação regulatória atual do produto no Brasil

<!-- review:begin br-lic-20261031-galcanezumab-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecer a situação regulatória atual do produto no Brasil (registro cancelado)” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-galcanezumab-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registro cancelado)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Além disso, o único registro no Brasil está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Emgality (galcanezumab-gnlm) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33a147be-233a-40e8-a55e-e40936e28db0) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

