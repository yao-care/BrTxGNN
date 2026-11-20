---
layout: default
title: Rifaximin
parent: Apenas Predição do Modelo (L5)
nav_order: 566
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
description: "Rifaximin: nova indicação prevista, Candidíase oral (oral candidiasis) (nível de evidência L5). Indicação original: RIFAXIMINA"
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Rifaximina: Da indicação original registrada à candidíase oral (previsão sem suporte clínico)
{: .text-alpha }

## Resumo em Uma Frase

Rifaximina é um antibiótico oral pouco absorvido, registrado na ANVISA com o nome XIFAXAN, cujo texto de indicação consta apenas como "RIFAXIMINA".
O modelo TxGNN prevê que pode ser eficaz para **candidíase oral (oral candidiasis)**, mas não há **nenhum ensaio clínico** e há apenas **1 publicação**, que sugere risco, e não benefício.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | RIFAXIMINA (o texto da indicação no registro não detalha a doença-alvo) |
| Nova Indicação Prevista | Candidíase oral (oral candidiasis) |
| Pontuação de Previsão TxGNN | 0,9975 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Rifaximin (tradução não oficial): “A rifaximina é um medicamento antibacteriano. […] A rifaximina é um derivado semissintético da rifampicina e atua ligando-se à subunidade beta da RNA polimerase DNA-dependente bacteriana, bloqueando uma das etapas da transcrição. Isso resulta na inibição da síntese proteica bacteriana e, consequentemente, inibe o crescimento das bactérias.” Texto original em inglês: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), versão de 2025-08-27; acessado em 2026-11-19). Segundo informações conhecidas, a rifaximina é um antibacteriano da classe das rifamicinas, não absorvido, que atua sobre a RNA polimerase bacteriana. Não tem atividade antifúngica conhecida.

Por isso, não se identifica uma ligação mecanística plausível entre a indicação original (infecções bacterianas intestinais) e a candidíase oral. A pontuação alta do TxGNN (0.9975) é uma previsão do modelo TxGNN (aprendizado profundo), pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica, e conflita com as evidências clínicas disponíveis.

O único sinal na literatura aponta na direção oposta: o uso de rifaximina favoreceu infecções por *Candida* resistente à micafungina em receptores de transplante alogênico de células-tronco hematopoéticas, provavelmente por alterar o microbioma intestinal. Trata-se de um sinal de dano, não terapêutico.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Coorte | Annals of Hematology | Em pacientes submetidos a transplante alogênico de células-tronco hematopoéticas, o uso de rifaximina como profilaxia intestinal favoreceu infecções por *Candida* resistente à micafungina |

Atualmente não há ensaios clínicos relacionados registrados.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 109740276 | XIFAXAN | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740225 | XIFAXAN | BIOLAB SANUS FARMACÊUTICA LTDA | Cancelado |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas**: foram identificadas 69 interações. Entre as principais:
  - **Grave**: vacina viva contra cólera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderadas**: varfarina, ciclosporina, tolvaptana, cabozantinibe, alpelisibe, apalutamida, brigatinibe, capmatinibe, daclatasvir, ledipasvir, darolutamida, elagolix, eliglustate, enasidenibe, encorafenibe, elexacaftor, istradefilina, ácido bempedoico e ácido picossulfúrico.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem mecanismo antifúngico plausível, e a única publicação indica que a rifaximina pode favorecer candidíase.

<!-- review:begin br-lic-20261106-rifaximin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Não há ensaios clínicos nem mecanismo antifúngico plausível, e a única publicação indica que a rifaximina pode favorecer candidíase. Além disso, o único registro no Brasil está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-rifaximin-1 -->

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) e evidência de atividade antifúngica ou de efeito benéfico sobre a candidíase oral.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Avaliação do risco de candidíase associado ao uso de rifaximina, incluindo a seleção de *Candida* resistente.
- Esclarecimento da situação regulatória do registro cancelado e da forma farmacêutica.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o único registro no Brasil está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

