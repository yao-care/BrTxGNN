---
layout: default
title: Zanamivir
parent: Apenas Predição do Modelo (L5)
nav_order: 678
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Zanamivir: nova indicação prevista, Pielonefrite (Pyelonephritis) (nível de evidência L5). Indicação original: Influenza"
monitor_inn: "Zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Zanamivir: Da influenza à pielonefrite (previsão sem evidências de suporte)
{: .text-alpha }

## Resumo em Uma Frase

Zanamivir é um inibidor da neuraminidase viral, originalmente usado no tratamento da influenza.
O modelo TxGNN prevê que pode ser eficaz para **Pielonefrite (Pyelonephritis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Influenza |
| Nova Indicação Prevista | Pielonefrite (Pyelonephritis) |
| Pontuação de Previsão TxGNN | 0,9984 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Zanamivir (tradução não oficial): “O zanamivir é um medicamento antiviral com atividade contra o vírus influenza. […] O zanamivir é um inibidor da neuraminidase (NA) do vírus influenza, uma enzima que libera partículas virais da membrana plasmática das células infectadas e promove a disseminação do vírus no trato respiratório. Em ensaios de inibição da neuraminidase, o zanamivir é ativo contra todos os subtipos da enzima NA, de N1 a N9.” Texto original em inglês: "Zanamivir is an antiviral drug with activity against influenza virus. […] Zanamivir is an inhibitor of influenza virus neuraminidase (NA), an enzyme that releases viral particles from the plasma membrane of infected cells and promotes virus spread in the respiratory tract. In neuraminidase inhibition assays, zanamivir is active against all NA enzyme subtypes N1 to N9." ([DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d), versão de 2026-07-23; acessado em 2026-11-19). Segundo informações conhecidas, o zanamivir é um inibidor da neuraminidase do vírus influenza, e sua eficácia em influenza é o uso original do fármaco.

Não foi identificado vínculo mecanístico plausível com a pielonefrite. Essa doença é tipicamente uma infecção bacteriana do rim, enquanto o alvo do zanamivir (a neuraminidase viral) não é o mecanismo central dessas infecções. A pontuação elevada do TxGNN (0,9984) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica, sem respaldo em ensaios clínicos ou literatura nos dados compilados. A previsão deve, portanto, ser tratada com cautela e considerada especulativa.

## Considerações sobre as Demais Previsões

As outras nove indicações previstas também têm nível de evidência L5 e recomendação Hold. Nenhuma tem ensaios clínicos.

| Posição | Indicação Prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Distúrbio do metabolismo da tirosina | 0,9902 | Três artigos recuperados tratam de resistência à neuraminidase na influenza, sem relação biológica com a doença (correspondência por palavras-chave) |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (pielonefrite).

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento** (não provêm de bula): epilepsia, doença pulmonar obstrutiva crônica (DPOC), DPOC grave de início precoce, doença brônquica e delírio. Convém confirmar esses itens na bula antes de qualquer uso.
- **Interações medicamentosas** (8 identificadas):
  - Insulina humana inalatória de ação rápida: gravidade **moderada**.
  - Claritromicina, loratadina, montelucaste, cetotifeno, fexofenadina, ibuprofeno e diclofenaco: gravidade não classificada.

Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do TxGNN é alta, mas não há ensaios clínicos, literatura ou mecanismo plausível que sustentem o uso do zanamivir na pielonefrite.

<!-- review:begin br-lic-20261106-zanamivir-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A pontuação do TxGNN é alta, mas não há ensaios clínicos, literatura ou mecanismo plausível que sustentem o uso do zanamivir na pielonefrite. O fármaco também não está registrado no Brasil.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-zanamivir-1 -->

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) para avaliar o vínculo mecanístico.
- Bula da ANVISA com advertências e contraindicações, atualmente ausente e que impede a triagem de segurança.
- Evidência pré-clínica ou clínica de atividade em pielonefrite, ou a reavaliação de outras previsões com maior plausibilidade biológica.
- Análise de compatibilidade de via de administração. O zanamivir é usado principalmente por via inalatória, o que pode não ser adequado para infecção renal.

<!-- review:begin br-lic-20261106-zanamivir-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O zanamivir é usado principalmente por via inalatória, o que pode não ser adequado para infecção renal. / Avaliação regulatória sobre a ausência de registro no Brasil.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-zanamivir-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco também não está registrado no Brasil” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Avaliação regulatória sobre a ausência de registro no Brasil” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

