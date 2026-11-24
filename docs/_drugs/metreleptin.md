---
layout: default
title: Metreleptin
parent: Apenas Predição do Modelo (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Metreleptin: nova indicação prevista, Lentiginose generalizada familiar (familial generalized lentiginosis) (nível de evidência L5). Indicação original: Outros produtos para o aparelho digestivo e me…"
monitor_inn: "metreleptin"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "Moynahan syndrome", "rhabdoid tumor", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "acromelanosis", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "benign neoplasm of adrenal gland", "peripheral nerve schwannoma"]
---

# Metreleptin
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

## Metreleptina: Da categoria de produtos para o aparelho digestivo e metabolismo à lentiginose generalizada familiar
{: .text-alpha }

## Resumo em Uma Frase

Metreleptina (MYALEPT) é um análogo recombinante da leptina, registrado na ANVISA na categoria "outros produtos para o aparelho digestivo e metabolismo".
O modelo TxGNN prevê que pode ser eficaz para **lentiginose generalizada familiar (familial generalized lentiginosis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho digestivo e metabolismo |
| Nova Indicação Prevista | Lentiginose generalizada familiar (familial generalized lentiginosis) |
| Pontuação de Previsão TxGNN | 0,9971 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Metreleptin (tradução não oficial): “Os adipócitos armazenam lipídios para atender às necessidades energéticas dos tecidos não adiposos durante o jejum. Em pacientes com lipodistrofia generalizada, a deficiência de tecido adiposo leva à hipertrigliceridemia e à deposição ectópica de gordura em tecidos não adiposos, como fígado e músculo, contribuindo para anormalidades metabólicas, incluindo resistência à insulina. […] MYALEPT (metreleptina) para injeção exerce sua função ligando-se ao receptor de leptina humano (ObR) e ativando-o; esse receptor pertence à família de receptores de citocinas de Classe I, que sinaliza por meio da via de transdução JAK/STAT.” Texto original em inglês: "Adipocytes store lipids to meet the fuel requirements of non-adipose tissues during fasting. In patients with generalized lipodystrophy, the deficiency of adipose tissue leads to hypertriglyceridemia and ectopic deposition of fat in non-adipose tissues such as liver and muscle, contributing to metabolic abnormalities including insulin resistance. […] MYALEPT (metreleptin) for injection exerts its function by binding to and activating the human leptin receptor (ObR), which belongs to the Class I cytokine family of receptors that signals through the JAK/STAT transduction pathway." ([DailyMed: Myalept (metreleptin) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3b50bbd-140b-425c-b5ec-d4682aad62bc), versão de 2024-03-25; acessado em 2026-11-19). Segundo o conhecimento geral, a metreleptina é um análogo recombinante da leptina que atua nos receptores de leptina para corrigir a deficiência desse hormônio na lipodistrofia.

A relação entre a indicação original (distúrbios metabólicos) e a nova indicação é fraca. A lentiginose generalizada familiar é um distúrbio pigmentar e não há conexão estabelecida com a sinalização da leptina. A pontuação alta do TxGNN (0,9971) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não uma base biológica demonstrada.

Portanto, a previsão não tem respaldo mecanístico claro. Também não há ensaios clínicos nem publicações que a sustentem. As demais previsões do modelo (por exemplo, síndrome gastrocutânea, síndrome de Moynahan, tumor rabdoide, acromelanose e schwannoma de nervo periférico) apresentam o mesmo problema: nenhuma tem evidência clínica ou mecanismo plausível. No caso do tumor rabdoide, a sinalização da leptina é discutida como promotora de crescimento em alguns cânceres, o que levanta preocupação de segurança.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100580123 | MYALEPT | CHIESI FARMACÊUTICA LTDA | Ativo |
| 175040002 | MYALEPT | AMRYT BRASIL COMERCIO E IMPORTACAO DE MEDICAMENTOS | Cancelado |

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 145 interações potenciais, a maioria de gravidade moderada. Exemplos incluem:
  - Abemaciclibe, acalabrutinibe, alpelisibe, avapritinibe, brigatinibe, cabozantinibe, capmatinibe e ceritinibe (moderada)
  - Fentanila, alfentanila, butorfanol e benzidrocodona (moderada)
  - Etinilestradiol, noretisterona e desogestrel (moderada)
  - Bictegravir, buspirona, cariprazina e clorpropamida (moderada)
  - Bortezomibe (leve)
- **Preocupação específica**: o uso em contexto oncológico (como no tumor rabdoide) exige cautela, pois a sinalização da leptina pode estar associada ao crescimento tumoral.

Para advertências e contraindicações, consulte a bula, pois essas informações não estão disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão baseia-se apenas em inferência computacional (nível L5), sem ensaios clínicos, sem literatura e sem mecanismo plausível.

<!-- review:begin br-lic-20261106-metreleptin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão baseia-se apenas em inferência computacional (nível L5), sem ensaios clínicos, sem literatura e sem mecanismo plausível. Além disso, o único registro no Brasil está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-metreleptin-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação via DrugBank
- Realizar revisão sistemática da literatura e de registros de ensaios para identificar qualquer base biológica entre a sinalização da leptina e distúrbios pigmentares
- Avaliar a situação regulatória e a disponibilidade do produto no Brasil, dado o registro cancelado
- Considerar priorizar outras indicações com maior plausibilidade biológica, como condições associadas à resistência à insulina

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o único registro no Brasil está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Myalept (metreleptin) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3b50bbd-140b-425c-b5ec-d4682aad62bc) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

