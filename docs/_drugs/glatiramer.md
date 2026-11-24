---
layout: default
title: Glatiramer
parent: Apenas Predição do Modelo (L5)
nav_order: 343
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Glatiramer: nova indicação prevista, Hemoglobinopatia (hemoglobinopathy) (nível de evidência L5). Indicação original: Imunomodulador"
monitor_inn: "glatiramer"
predicted_indications: ["hemoglobinopathy"]
---

# Glatiramer
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

## Glatirâmer: De imunomodulador a hemoglobinopatia
{: .text-alpha }

## Resumo em Uma Frase

O acetato de glatirâmer é um imunomodulador, originalmente registrado na ANVISA com a indicação genérica "imunomodulador" (uso conhecido em esclerose múltipla).
O modelo TxGNN prevê que pode ser eficaz para **hemoglobinopatia (hemoglobinopathy)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** vinculada, que não aborda diretamente essa direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunomodulador |
| Nova Indicação Prevista | Hemoglobinopatia (hemoglobinopathy) |
| Pontuação de Previsão TxGNN | 0,9903 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 5) |
| Número de Registros | 5 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Glatiramer (tradução não oficial): “O(s) mecanismo(s) pelo(s) qual(is) o acetato de glatirâmer exerce seus efeitos em pacientes com EM não é(são) totalmente compreendido(s). No entanto, acredita-se que o acetato de glatirâmer atue modificando processos imunológicos que se acredita serem responsáveis pela patogênese da EM.” Texto original em inglês: "The mechanism(s) by which glatiramer acetate exerts its effects in patients with MS are not fully understood. However, glatiramer acetate is thought to act by modifying immune processes that are believed to be responsible for the pathogenesis of MS." ([DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716), versão de 2026-10-26; acessado em 2026-11-19). Segundo informações conhecidas, o glatirâmer é um imunomodulador usado na esclerose múltipla, mas os dados compilados para este relatório não permitem estabelecer uma via plausível que o ligue à fisiopatologia das hemoglobinopatias (por exemplo, desequilíbrio das cadeias de globina, polimerização da hemoglobina ou hemólise crônica).

A previsão se apoia apenas na pontuação elevada do modelo TxGNN (deep learning) (0,9903), que pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, e não evidência biológica. A única publicação vinculada (PMID 28372806) descreve um caso de distúrbios imunes após a suspensão do natalizumabe em esclerose múltipla, em uma paciente que por acaso tinha histórico de beta-talassemia. Não avalia o glatirâmer como tratamento de hemoglobinopatia e, portanto, não oferece suporte direto nem indireto claro.

Assim, a razoabilidade biológica da previsão permanece não demonstrada e deve ser tratada como hipótese gerada por modelo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Relato de caso/Revisão (inferido pelo título) | Revue neurologique | Caso de mulher de 35 anos com esclerose múltipla (e histórico de beta-talassemia, bulimia e asma) que apresentou múltiplos distúrbios imunes após a suspensão do natalizumabe. Não trata de glatirâmer em hemoglobinopatia. |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 155730001 | COPAXONE | TEVA FARMACÊUTICA LTDA. | Ativo |
| 155730064 | ACETATO DE GLATIRÂMER | TEVA FARMACÊUTICA LTDA. | Ativo |
| 156260032 | GLAMETIX | LABORATÓRIOS BAGÓ DO BRASIL S/A | Ativo |
| 112130203 | COPAXONE | BIOSINTÉTICA FARMACÊUTICA LTDA | Cancelado |
| 155730056 | ACETATO DE GLATIRÂMER | TEVA FARMACÊUTICA LTDA. | Cancelado |

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas**: foi identificada 1 interação de gravidade **Maior** com o **natalizumabe** (fonte: DDInter). Recomenda-se evitar ou avaliar cuidadosamente a associação.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia somente na pontuação do modelo (nível L5), sem ensaios clínicos, sem mecanismo plausível e com literatura não relacionada à indicação prevista. Além disso, o medicamento é comercializado no Brasil, com 3 registros válidos de 3.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação do glatirâmer (por exemplo, via DrugBank) e analisar se há ligação com a fisiopatologia das hemoglobinopatias.
- Obter a bula na ANVISA para avaliar advertências e contraindicações (lacuna bloqueante para a triagem de segurança).
- Realizar busca sistemática de literatura e estudos pré-clínicos que sustentem a hipótese.
- Esclarecer a situação regulatória e a compatibilidade de via de administração e forma farmacêutica.
- Avaliar o risco da interação de gravidade maior com o natalizumabe, em especial em pacientes com esclerose múltipla.

<!-- review:begin br-lic-20261031-glatiramer-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecer a situação regulatória (registros cancelados) e a compatibilidade de via de administração e forma farmacêutica.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-glatiramer-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registros cancelados)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Glatopa (glatiramer acetate) prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0679689e-8930-4d6a-b922-5125082b2716) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

