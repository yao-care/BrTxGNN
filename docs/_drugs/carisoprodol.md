---
layout: default
title: Carisoprodol
parent: Apenas Predição do Modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Carisoprodol: nova indicação prevista, Insônia (insomnia) (nível de evidência L5). Indicação original: Relaxante muscular esquelético de ação central"
monitor_inn: "CARISOPRODOL"
predicted_indications: ["insomnia (disease)"]
---

# Carisoprodol
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

## Carisoprodol: Do relaxante muscular à insônia
{: .text-alpha }

## Resumo em Uma Frase

Carisoprodol é um relaxante muscular de ação central. Não há indicação original registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **Insônia (insomnia)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão indireta sobre câimbras noturnas) relacionada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Relaxante muscular esquelético de ação central (sem texto de indicação aprovada nos dados de registro) |
| Nova Indicação Prevista | Insônia (insomnia) |
| Pontuação de Previsão TxGNN | 0,9902 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 18 de 52) |
| Número de Registros | 52 (ativos: 18) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Carisoprodol (tradução não oficial): “O mecanismo de ação do carisoprodol no alívio do desconforto associado a condições musculoesqueléticas agudas dolorosas não foi claramente identificado. Em estudos com animais, o relaxamento muscular induzido pelo carisoprodol está associado à atividade interneuronal alterada na medula espinhal e na formação reticular descendente do cérebro.” Texto original em inglês: "The mechanism of action of carisoprodol in relieving discomfort associated with acute painful musculoskeletal conditions has not been clearly identified. In animal studies, muscle relaxation induced by carisoprodol is associated with altered interneuronal activity in the spinal cord and in the descending reticular formation of the brain." ([DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa), versão de 2026-11-03; acessado em 2026-11-19). Segundo conhecimento farmacológico geral, o carisoprodol é um relaxante muscular esquelético de ação central. Seu metabólito ativo, o meprobamato, tem efeitos sedativos e ansiolíticos semelhantes aos dos barbitúricos, e o próprio carisoprodol parece modular receptores GABA-A.

Essa farmacologia sedativa oferece um elo teórico plausível com a insônia: a depressão do sistema nervoso central pode favorecer o início e a manutenção do sono. Contudo, essa ligação foi inferida da farmacologia geral e não de dados fornecidos.

A pontuação elevada do TxGNN (0,9902) é uma previsão computacional e não equivale a evidência clínica. Não há dados sobre a similaridade entre a indicação original e a nova indicação.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Revisão | American Family Physician | Revisão sobre câimbras noturnas nas pernas, que podem causar insônia intensa. Trata-se de evidência indireta: não avalia o carisoprodol como tratamento para insônia. |

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento (PrimeKG, não extraídas da bula)**: epilepsia, doença renal, doença hepática, doença da vesícula biliar, trombocitopenia, hipotireoidismo (incluindo mixedema e hipotireoidismo congênito), doença ulcerosa péptica, doença inflamatória intestinal, hiperplasia prostática benigna, distúrbios hipotensivos, gota, abuso/dependência de substâncias, hemofilia, anemia (incluindo macrocítica), colite por *Clostridium difficile*, enterocolite necrosante perinatal, parada cardíaca súbita, doenças da condução cardíaca, insuficiência respiratória e insuficiência adrenal (incluindo doença de Addison e formas congênitas).
- **Interações Medicamentosas**: foram identificadas 100 interações. Entre as listadas:
  - **Graves (Major)**: morfina e morfina lipossomal.
  - **Moderadas**: dronabinol, metoclopramida, nabilona, ópio, sibutramina, difenoxina e difenoxilato. O risco principal é a depressão aditiva do sistema nervoso central.
  - **Nível desconhecido**: fentermina, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, metformina, omeprazol, sucralfato, rosiglitazona e lansoprazol.
- **Preocupações gerais**: sedação, potencial de dependência e abuso, e alta carga de interações com depressores do SNC, relevantes para qualquer uso como hipnótico.

As advertências e contraindicações da bula não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão baseia-se apenas no modelo (nível L5), sem ensaios clínicos e com uma única publicação indireta.

<!-- review:begin br-lic-20261106-carisoprodol-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão baseia-se apenas no modelo (nível L5), sem ensaios clínicos e com uma única publicação indireta. Além disso, o fármaco não está registrado no Brasil e apresenta importantes preocupações de segurança (dependência, sedação e interações com depressores do SNC).” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-carisoprodol-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações) para a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Buscar evidências clínicas diretas do carisoprodol ou do meprobamato na insônia.
- Avaliar o risco de dependência e abuso frente aos hipnóticos já disponíveis.
- Verificar a situação regulatória do fármaco no Brasil, já que não há registros.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o fármaco não está registrado no Brasil e apresenta importantes preocupações de segurança (dependência, sedação e interações com” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Carisoprodol Tablets, Usp, 350 Mg (carisoprodol) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1f08f4af-37c2-49b5-a4e3-284414f866fa) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

