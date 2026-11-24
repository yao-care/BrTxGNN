---
layout: default
title: Caspofungin
parent: Apenas Predição do Modelo (L5)
nav_order: 200
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Caspofungin: nova indicação prevista, Anormalidade da secreção de gastrina (gastrin secretion abnormality) (nível de evidência L5). Indicação original: Antifúngicos (ANTI-FUNGICOS)"
monitor_inn: "caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungina: De antifúngico para anormalidade da secreção de gastrina
{: .text-alpha }

## Resumo em Uma Frase

Caspofungina é um antifúngico da classe das equinocandinas, registrado no Brasil com indicação original "anti-fúngicos".
O modelo TxGNN prevê que pode ser eficaz para **anormalidade da secreção de gastrina (gastrin secretion abnormality)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antifúngicos (ANTI-FUNGICOS) |
| Nova Indicação Prevista | Anormalidade da secreção de gastrina (gastrin secretion abnormality) |
| Pontuação de Previsão TxGNN | 0,9944 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 4 de 6) |
| Número de Registros | 6 (ativos: 4) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Caspofungin (tradução não oficial): “A caspofungina é um fármaco antifúngico da classe das equinocandinas. […] A caspofungina, uma equinocandina, inibe a síntese de beta (1,3)-D-glucano, um componente essencial da parede celular de espécies suscetíveis de Aspergillus e de Candida. O beta (1,3)-D-glucano não está presente em células de mamíferos.” Texto original em inglês: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), versão de 2024-10-11; acessado em 2026-11-19). Segundo informações conhecidas, a caspofungina é uma equinocandina que inibe a enzima beta-(1,3)-D-glucano sintase, interrompendo a síntese da parede celular dos fungos. Sua eficácia como antifúngico está estabelecida.

Não há um vínculo mecanístico conhecido com a nova indicação. A secreção de gastrina é regulada pelas células G, pelo pH gástrico e pela sinalização da somatostatina, e nenhum desses elementos é alvo conhecido da caspofungina. A pontuação elevada do TxGNN (0,9944) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

Qualquer associação seria especulativa, por exemplo um efeito indireto via colonização fúngica gástrica ou intestinal, ou um efeito fora do alvo (off-target). Nenhuma dessas hipóteses está documentada nos dados compilados para este relatório. A compatibilidade de vias de administração e a similaridade com a indicação original também ainda não foram avaliadas.

## Informações de Comercialização no Brasil

O medicamento está comercializado no Brasil: há registros válidos e cancelados (números atualizados no resumo rápido).

<!-- review:begin br-lic-20261112-caspofungin-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “5 dos 5 registros são válidos” Corrigido conforme os dados abertos de medicamentos da ANVISA: o número ou a situação dos registros informado não correspondia aos dados; o texto não traz mais números fixos, e os números atualizados estão no resumo rápido e na tabela de registros desta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261112-caspofungin-1 -->

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431107 | ACETATO DE CASPOFUNGINA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431156 | BERK | EUROFARMA LABORATORIOS S.A. | Ativo |
| 151430075 | ACETATO DE CASPOFUNGINA | DR. REDDYS FARMACÊUTICA DO BRASIL LTDA | Ativo |
| 151430076 | KAZFONA | DR. REDDYS FARMACÊUTICA DO BRASIL LTDA | Ativo |
| 100290033 | CANCIDAS | ORGANON FARMACÊUTICA LTDA. | Cancelado |
| 101710226 | CANCIDAS | MERCK SHARP & DOHME FARMACEUTICA LTDA. | Cancelado |

<!-- licenses:end -->

## Considerações de Segurança

- **Contraindicações (base de conhecimento TxGNN, não derivadas da bula):** doença hepática, doença da vesícula biliar e deficiência de potássio.
- **Interações Medicamentosas:** foram identificadas 81 interações no total. As de maior relevância são:
  - **Dexametasona**: gravidade **Maior**
  - **Naltrexona**: gravidade **Moderada**
  - Há ainda interações de gravidade não classificada, como pantoprazol, omeprazol, lansoprazol, vancomicina, anfotericina B, nistatina, prednisona, prednisolona, hidrocortisona, sinvastatina, cloreto de potássio, entre outras.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia apenas no modelo (L5), sem ensaios clínicos, sem literatura e sem vínculo mecanístico plausível. Além disso, o medicamento está comercializado no Brasil e há interação medicamentosa de gravidade maior com a dexametasona.

<!-- review:begin br-lic-20261106-caspofungin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Além disso, o medicamento está comercializado no Brasil (5 de 5 registros válidos) e há interação medicamentosa de gravidade maior com a dexametasona.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-caspofungin-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação via DrugBank.
- Realizar revisão de literatura e busca de estudos pré-clínicos que sustentem uma hipótese mecanística para a secreção de gastrina.
- Avaliar a compatibilidade de vias de administração (a caspofungina é de uso intravenoso) e a similaridade com a indicação original.
- Esclarecer a situação regulatória.

<!-- review:begin br-lic-20261106-caspofungin-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Esclarecer a situação regulatória, já que não há registro válido no Brasil.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-caspofungin-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “(5 de 5 registros válidos)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que não há registro válido no Brasil” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-24 | “5 dos 5 registros são válidos” → “há registros válidos e cancelados (números atualizados no resumo rápido)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

