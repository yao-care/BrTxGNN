---
layout: default
title: Risdiplam
parent: Apenas Predição do Modelo (L5)
nav_order: 568
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-25
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)"]
description: "Risdiplam: nova indicação prevista, Acne (acne (disease)) (nível de evidência L5). No Brasil, registros na ANVISA: 2 (ativos: 2)"
---

# Risdiplam
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

## Risdiplam: Acne (acne (disease))
{: .text-alpha }

## Resumo em Uma Frase

Risdiplam é um modulador de splicing do gene SMN2, sem indicação aprovada registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **acne (disease)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Acne (acne (disease)) |
| Pontuação de Previsão TxGNN | 0.9945 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Risdiplam (tradução não oficial): “O risdiplam é um modificador do splicing do gene de sobrevivência do neurônio motor 2 (SMN2) desenvolvido para tratar pacientes com atrofia muscular espinhal (AME) causada por mutações no cromossomo 5q que levam à deficiência da proteína SMN. Por meio de ensaios in vitro e de estudos em modelos animais transgênicos de AME, demonstrou-se que o risdiplam aumenta a inclusão do éxon 7 nos transcritos de ácido ribonucleico mensageiro (mRNA) do SMN2 e a produção da proteína SMN completa no cérebro.” Texto original em inglês: "Risdiplam is a survival of motor neuron 2 (SMN2) splicing modifier designed to treat patients with spinal muscular atrophy (SMA) caused by mutations in chromosome 5q that lead to SMN protein deficiency. Using in vitro assays and studies in transgenic animal models of SMA, risdiplam was shown to increase exon 7 inclusion in SMN2 messenger ribonucleic acid (mRNA) transcripts and production of full-length SMN protein in the brain." ([DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e), versão de 2026-11-02; acessado em 2026-11-19). Segundo informações conhecidas, o risdiplam é um modulador de splicing do SMN2, que promove a inclusão do éxon 7 e aumenta a produção de proteína SMN funcional. Esse é o fundamento de seu uso na atrofia muscular espinhal, mas essa indicação não consta nos registros brasileiros analisados.

Não foi identificado mecanismo que sustente a previsão para acne. Não há relação estabelecida entre a modulação do splicing de SMN2 e a biologia das glândulas sebáceas ou a inflamação associada ao *C. acnes*. A pontuação elevada (0,9945) vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica, sem respaldo clínico ou de literatura.

Também vale notar que as terapias para acne da classe dos retinoides têm perfis de segurança distintos, e não há dados do risdiplam nesse cenário.

---

## Outras Indicações Previstas (Todas de Nível L5)

Nenhuma das demais previsões do modelo possui ensaios clínicos ou literatura. Todas estão em Hold.

| Posição | Indicação Prevista | Pontuação TxGNN | Observação |
|------|------|------|------|

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
| 101000670 | EVRYSDI | PRODUTOS ROCHE QUÍMICOS E FARMACÊUTICOS S.A. | Ativo |
| 101000681 | EVRYSDI GO | PRODUTOS ROCHE QUÍMICOS E FARMACÊUTICOS S.A. | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas** (2 interações de nível moderado):
  - Metformina (moderada)
  - Metilnaltrexona (moderada)

Para advertências e contraindicações, consulte a bula. Esses dados não estavam disponíveis para este relatório.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para acne baseia-se apenas na pontuação do modelo, sem ensaios clínicos, literatura ou mecanismo plausível.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), uma lacuna que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação no DrugBank
- Verificar a situação regulatória do risdiplam no Brasil e sua indicação original
- Realizar estudos pré-clínicos ou revisão da literatura que sustentem a ligação mecanística com acne
- Avaliar compatibilidade de via de administração e formulação para a nova indicação

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

