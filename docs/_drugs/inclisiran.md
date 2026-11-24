---
layout: default
title: Inclisiran
parent: Apenas Predição do Modelo (L5)
nav_order: 365
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Inclisiran: nova indicação prevista, Deficiência de potássio (potassium deficiency disease) (nível de evidência L5). Indicação original: Antilipêmicos"
monitor_inn: "inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
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

## Inclisirana: De antilipêmico para deficiência de potássio (previsão do modelo, sem evidências de suporte)
{: .text-alpha }

## Resumo em Uma Frase

Inclisirana é um siRNA que silencia o PCSK9, registrado na ANVISA na categoria de antilipêmicos (redutores de lipídios).
O modelo TxGNN prevê que pode ser eficaz para **deficiência de potássio (potassium deficiency disease)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** que apoiem esta direção. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Deficiência de potássio (potassium deficiency disease) |
| Pontuação de Previsão TxGNN | 0,9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Inclisiran (tradução não oficial): “A inclisirana é um ácido ribonucleico interferente pequeno (siRNA) de fita dupla, conjugado na fita senso com N-acetilgalactosamina (GalNAc) triantenária para facilitar a captação pelos hepatócitos. Nos hepatócitos, a inclisirana utiliza o mecanismo de interferência por RNA e direciona a degradação catalítica do mRNA da PCSK9.” Texto original em inglês: "Inclisiran is a double-stranded small interfering ribonucleic acid (siRNA), conjugated on the sense strand with triantennary N-Acetylgalactosamine (GalNAc) to facilitate uptake by hepatocytes. In hepatocytes, inclisiran utilizes the RNA interference mechanism and directs catalytic breakdown of mRNA for PCSK9." ([DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44), versão de 2026-08-19; acessado em 2026-11-19). Segundo informações conhecidas, a inclisirana é um RNA interferente pequeno (siRNA) que atua sobre o RNA mensageiro do PCSK9, reduzindo o colesterol LDL (LDL-C). Sua eficácia está associada ao controle de lipídios, e não à regulação de eletrólitos.

Não foi identificada relação plausível entre o silenciamento do PCSK9 e a homeostase do potássio. A pontuação alta do TxGNN (0,9993) decorre apenas da previsão do modelo TxGNN (aprendizado profundo), sem ensaios ou literatura que a sustentem. Por isso, a razoabilidade mecanística desta previsão é **fraca** e deve ser tratada como hipótese a ser verificada, não como indicação de eficácia.

Outras indicações previstas, todas também sem evidência de suporte (nível L5): doença esofágica, coarctação atípica da aorta, enxaqueca (incluindo enxaqueca com aura do tronco encefálico e suscetibilidade genética), malformação esofágica não sindrômica, malformação aórtica, úlcera esofágica e doença de Raynaud. Para nenhuma delas há mecanismo estabelecido.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a deficiência de potássio.

Observação sobre outra indicação prevista (malformação aórtica, 8ª posição): dois ensaios de Fase 3 em andamento foram associados ao termo, mas seus títulos indicam estudos pediátricos em hipercolesterolemia familiar, e não em malformação aórtica. Trata-se provavelmente de erro de mapeamento de termos, sem valor como evidência direta:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recrutando | 60 | Inclisirana vs placebo (1 ano) e depois aberto (1 ano), em crianças de 6 a <12 anos com hipercolesterolemia familiar heterozigótica; sem resultados |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recrutando | 9 | Mesmo desenho, em crianças de 2 a <12 anos com hipercolesterolemia familiar homozigótica; sem resultados |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 100681184 | SYBRAVA | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para deficiência de potássio não tem ensaios, literatura nem mecanismo plausível (nível L5).

<!-- review:begin br-lic-20261106-inclisiran-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão para deficiência de potássio não tem ensaios, literatura nem mecanismo plausível (nível L5). Além disso, o único registro brasileiro está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-inclisiran-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada sem esses dados.
- Confirmar o mecanismo de ação no DrugBank.
- Realizar revisão sistemática da literatura sobre PCSK9/inclisirana e homeostase do potássio para verificar se há alguma hipótese biológica.
- Confirmar os registros no ClinicalTrials.gov para descartar erro de mapeamento nos ensaios associados à malformação aórtica.
- Esclarecer a situação regulatória (cancelamento do registro) e a disponibilidade comercial do produto no Brasil.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o único registro brasileiro está cancelado” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-12 | Tabela: registro 100681184 (SYBRAVA) está ativo, não cancelado | Substituído pela tabela de registros gerada por programa (antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

