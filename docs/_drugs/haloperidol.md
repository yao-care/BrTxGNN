---
layout: default
title: Haloperidol
parent: Apenas Predição do Modelo (L5)
nav_order: 350
evidence_level: L5
indication_count: 9
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-24
description: "Haloperidol: nova indicação prevista, Doença congênita de glicosilação com fucosilação defeituosa (congenital disorder of glycosylation with defective fucosy… (nível de evidência L5). Indicação origi…"
---

# Haloperidol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Haloperidol: antipsicótico bloqueador de receptores de dopamina D2 → doença congênita de glicosilação com fucosilação defeituosa (congenital disorder of glycosylation with defective fucosylation)
{: .text-alpha }

## Resumo em Uma Frase

Haloperidol é um antipsicótico típico, que atua principalmente bloqueando receptores de dopamina D2.
O modelo TxGNN prevê que pode ser eficaz para **doença congênita de glicosilação com fucosilação defeituosa (congenital disorder of glycosylation with defective fucosylation)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Doença congênita de glicosilação com fucosilação defeituosa (congenital disorder of glycosylation with defective fucosylation) |
| Pontuação de Previsão TxGNN | 0,9991 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 12 de 30) |
| Número de Registros | 30 (ativos: 12) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Haloperidol (tradução não oficial): “O mecanismo de ação do decanoato de haloperidol no tratamento da esquizofrenia em adultos não está esclarecido. No entanto, seu efeito na esquizofrenia pode ser mediado por sua atividade como antagonista dos receptores centrais de dopamina do tipo 2.” Texto original em inglês: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), versão de 2026-11-03; acessado em 2026-11-19). Segundo informações conhecidas, o haloperidol é um antagonista de receptores de dopamina D2, classe dos antipsicóticos butirofenonas.

Não foi identificado vínculo mecanístico entre o bloqueio de dopamina D2 e defeitos de fucosilação na glicosilação de proteínas. A pontuação do TxGNN é muito alta (0,9991), mas resulta apenas de um cálculo do modelo: não há ensaios, nem literatura, nem justificativa biológica plausível que a sustente.

Por isso, esta previsão deve ser tratada como hipótese a ser explorada, e não como direção terapêutica sustentada por dados.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

A lista de registros pode estar incompleta.

<!-- review:begin br-lic-20261106-haloperidol-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Os dados compilados indicam 5 registros válidos e 15 cancelados, e a lista de registros pode estar incompleta. Os detalhes de cada registro não estão disponíveis nos dados compilados.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-haloperidol-1 -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram registradas 100 interações; entre as exemplificadas, as de gravidade **maior** incluem bupropiona, morfina, claritromicina e dolasetrona. Há ainda várias de gravidade moderada (por exemplo, famotidina, epinefrina, hidrocortisona, anfotericina B, atropina, loperamida e bisacodil).

Para advertências e contraindicações em bula, consulte a bula aprovada pela ANVISA.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas na pontuação do modelo, sem ensaios clínicos, sem literatura e sem vínculo mecanístico identificável; não há base para avançar.

**Para prosseguir, é necessário:**
- Estabelecer uma hipótese mecanística plausível entre a ação do haloperidol e a via de fucosilação, apoiada por estudos pré-clínicos.
- Obter dados do mecanismo de ação e das advertências e contraindicações da bula na ANVISA.
- Verificar a lista completa de registros no Brasil.
- Avaliar o perfil de segurança (prolongamento do QT, sintomas extrapiramidais, interações) antes de qualquer estudo em população com doença metabólica rara.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Os dados compilados indicam 5 registros válidos e 15 cancelados, e a Os detalhes de cada registro não estão disponíveis nos dados compilados” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

