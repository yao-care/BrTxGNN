---
layout: default
title: Lithium Carbonate
parent: Apenas Predição do Modelo (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Lithium Carbonate: nova indicação prevista, Pseudoacondroplasia (pseudoachondroplasia) (nível de evidência L5). Indicação original: Antidepressivos"
monitor_inn: "Lithium carbonate"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
---

# Lithium Carbonate
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

## Carbonato de lítio: De antidepressivo à pseudoacondroplasia
{: .text-alpha }

## Resumo em Uma Frase

O carbonato de lítio foi originalmente registrado na ANVISA na categoria "antidepressivos".
O modelo TxGNN prevê que pode ser eficaz para **pseudoacondroplasia (pseudoachondroplasia)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção: trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidepressivos |
| Nova Indicação Prevista | Pseudoacondroplasia (pseudoachondroplasia) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 10 de 10) |
| Número de Registros | 10 (ativos: 10) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Lithium Carbonate (tradução não oficial): “O mecanismo de ação do lítio como agente estabilizador do humor é desconhecido.” Texto original em inglês: "The mechanism of action of lithium as a mood stabilizing agent is unknown." ([DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544), versão de 2022-11-03; acessado em 2026-11-19). Segundo informações conhecidas, o lítio inibe a GSK-3β e modula a via Wnt/β-catenina, o que pode influenciar a biologia dos condrócitos.

A relação com a indicação original é fraca: o carbonato de lítio é usado em psiquiatria, enquanto a pseudoacondroplasia é uma displasia esquelética rara. A doença é causada por mutações no gene COMP, que levam a estresse do retículo endoplasmático e morte de condrócitos. Um vínculo mecanístico direto com o lítio é especulativo e não é sustentado pelos dados disponíveis.

A pontuação alta do TxGNN (0,9998) vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica nem clínica. Outras previsões do mesmo fármaco (por exemplo, displasia acromesomélica tipo Hunter-Thompson, braquiolmia, síndrome WHIM) também se concentram em displasias esqueléticas e imunodeficiências raras, sem suporte clínico fornecido.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para a pseudoacondroplasia.

---

## Informações de Comercialização no Brasil

Os 10 registros encontram-se válidos (10 de 10 licenças válidas). A forma farmacêutica não consta nos dados compilados.

<!-- review:begin br-lic-20261106-lithium_carbonate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “*Mostrados os 5 primeiros de 10 registros, todos cancelados.*” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 10 registros para este medicamento, 10 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-lithium_carbonate-1 -->

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 100430518 | CARBOLITIUM | Ativo |
| 100431166 | CARBONATO DE LÍTIO | Ativo |
| 100630260 | CARBONATO DE LÍTIO | Ativo |
| 102980545 | CARBONATO DE LÍTIO | Ativo |
| 102980556 | LITERATA | Ativo |
| 103720250 | CARLIT | Ativo |
| 109740309 | BILYT | Ativo |
| 109740347 | CARBONATO DE LÍTIO | Ativo |
| 113430167 | CARBONATO DE LÍTIO | Ativo |
| 113430215 | BIPOLIT | Ativo |

<!-- licenses:end -->

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: doença renal, hipotireoidismo (inclusive congênito), mixedema, transtorno cognitivo, psoríase e parapsoríase, parada cardíaca súbita, doença do sistema de condução cardíaco, diabetes insípido (inclusive central e neuro-hipofisário) e piureter.
- **Interações medicamentosas** (100 interações registradas; principais):
  - **Maior gravidade**: bupropiona, lorcaserina.
  - **Moderada**: acarbose, famotidina, metformina, pioglitazona, loperamida, mesalazina, morfina, metronidazol, claritromicina, canagliflozina, clorpropamida, citrato de potássio, entre outras.
  - **Menor**: doxiciclina, epinefrina, ácido acetilsalicílico.

As advertências e contraindicações da bula não estavam disponíveis; consulte a bula para informações completas de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a pseudoacondroplasia, e o vínculo mecanístico é especulativo. Além disso, o medicamento está comercializado no Brasil, com 10 de 10 registros válidos, e a triagem de segurança não pôde ser concluída.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações).
- Complementar os dados de mecanismo de ação (consulta ao DrugBank).
- Realizar estudos pré-clínicos (por exemplo, modelos celulares ou animais com mutação em COMP) para testar a hipótese.
- Avaliar o perfil de segurança do lítio (janela terapêutica estreita, função renal e tireoidiana) na população-alvo, em geral pediátrica.
- Esclarecer a situação regulatória do produto no Brasil.

<!-- review:begin br-lic-20261106-lithium_carbonate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Esclarecer a situação regulatória do produto no Brasil, já que não há registro vigente.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 10 registros para este medicamento, 10 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-lithium_carbonate-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “*Mostrados os 5 primeiros de 10 registros, todos cancelados.*” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que não há registro vigente” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

