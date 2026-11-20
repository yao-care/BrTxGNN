---
layout: default
title: Agomelatina
parent: Apenas Predição do Modelo (L5)
nav_order: 32
evidence_level: L5
indication_count: 7
drugbank_id: DB06594
monitor_inn: "Agomelatine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "neurotic disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type", "Keppen-Lubinsky syndrome"]
last_modified_at: 2026-11-20
description: "Agomelatina: nova indicação prevista, Paroxismo tortícolo benigno da infância (benign paroxysmal torticollis of infancy) (nível de evidência L5). No Brasil, registros na ANVISA: 7 (ativos: 5)"
---

# Agomelatina
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Agomelatina: Paroxismo tortícolo benigno da infância (benign paroxysmal torticollis of infancy)
{: .text-alpha }

## Resumo em Uma Frase

Agomelatina é um antidepressivo com ação melatonérgica e serotoninérgica, com registro no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **paroxismo tortícolo benigno da infância (benign paroxysmal torticollis of infancy)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Paroxismo tortícolo benigno da infância (benign paroxysmal torticollis of infancy) |
| Pontuação de Previsão TxGNN | 0.9996 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 7) |
| Número de Registros | 7 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Agomelatina atua como agonista dos receptores de melatonina MT1/MT2 e antagonista do receptor serotoninérgico 5-HT2C. Segundo o ChEMBL (EMBL-EBI), o mecanismo de ação registrado para Agomelatina é (tradução não oficial): “Agonista dos receptores de melatonina; antagonista do receptor de serotonina 2c (5-HT2c)”. Texto original em inglês: "Melatonin receptor agonist; Serotonin 2c (5-HT2c) receptor antagonist" ([ChEMBL CHEMBL10878 (agomelatine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL10878), CC BY-SA 3.0; acessado em 2026-11-19).

O paroxismo tortícolo benigno da infância é um distúrbio neurológico paroxístico da primeira infância, considerado um equivalente migranoso. Um vínculo com a farmacologia da agomelatina é possível em tese (modulação serotoninérgica e do ritmo circadiano), mas é especulativo: nenhum estudo clínico ou publicação sustenta essa relação.

A pontuação elevada (0,9996) reflete apenas a previsão do modelo. Também não há dados de segurança nem de dose da agomelatina em lactentes, população-alvo desta condição.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 102351276 | Agomelatina (EMS) | Não informada | Não registrada nos dados locais |
| 112780073 | Valdoxan (Servier) | Não informada | Não registrada nos dados locais |
| 112780082 | Agoxom (Servier) | Não informada | Não registrada nos dados locais |
| 155730062 | Elencos (Teva) | Não informada | Não registrada nos dados locais |
| 155730063 | Agomelatina (Teva) | Não informada | Não registrada nos dados locais |

Foram identificados 7 registros, dos quais 5 válidos e 2 cancelados; a tabela lista os 5 principais.

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão não tem nenhum ensaio clínico nem publicação que estude diretamente a condição (nível L5). Também faltam dados de segurança e de dose em lactentes, e o vínculo mecanístico é especulativo.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações)
- Complementar os dados de mecanismo de ação a partir de fonte farmacológica confiável
- Realizar revisão sistemática da literatura sobre melatonina e moduladores serotoninérgicos no paroxismo tortícolo benigno da infância
- Avaliar a viabilidade de uso pediátrico (segurança, dose e forma farmacêutica adequada para lactentes)

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Agomelatina é um fármaco psicotrópico comercializado no Brasil com **7 registros ativos** na ANVISA” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Verificar a fonte dos dados regulatórios: o `query_log` indica fonte `tfda` (Taiwan FDA) — confirmar se os registros correspondem efetivamen” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte (revisado em 2026-11-20; versão anterior guardada no registro) | [ChEMBL CHEMBL10878 (agomelatine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL10878) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

