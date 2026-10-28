---
layout: default
title: Rifaximin
parent: Apenas Predição do Modelo (L5)
nav_order: 566
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Rifaximin: nova indicação prevista, Candidíase oral (oral candidiasis) (nível de evidência L4). Indicação original: RIFAXIMINA"
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
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, a rifaximina é um antibacteriano da classe das rifamicinas, não absorvido, que atua sobre a RNA polimerase bacteriana. Não tem atividade antifúngica conhecida.

Por isso, não se identifica uma ligação mecanística plausível entre a indicação original (infecções bacterianas intestinais) e a candidíase oral. A pontuação alta do TxGNN (0.9975) é uma previsão do modelo TxGNN (aprendizado profundo), pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica, e conflita com as evidências clínicas disponíveis.

O único sinal na literatura aponta na direção oposta: o uso de rifaximina favoreceu infecções por *Candida* resistente à micafungina em receptores de transplante alogênico de células-tronco hematopoéticas, provavelmente por alterar o microbioma intestinal. Trata-se de um sinal de dano, não terapêutico.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Coorte | Annals of Hematology | Em pacientes submetidos a transplante alogênico de células-tronco hematopoéticas, o uso de rifaximina como profilaxia intestinal favoreceu infecções por *Candida* resistente à micafungina |

Atualmente não há ensaios clínicos relacionados registrados.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 109740276 (cancelado) | XIFAXAN | Não informada | RIFAXIMINA |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas**: foram identificadas 69 interações. Entre as principais:
  - **Grave**: vacina viva contra cólera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderadas**: varfarina, ciclosporina, tolvaptana, cabozantinibe, alpelisibe, apalutamida, brigatinibe, capmatinibe, daclatasvir, ledipasvir, darolutamida, elagolix, eliglustate, enasidenibe, encorafenibe, elexacaftor, istradefilina, ácido bempedoico e ácido picossulfúrico.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem mecanismo antifúngico plausível, e a única publicação indica que a rifaximina pode favorecer candidíase. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) e evidência de atividade antifúngica ou de efeito benéfico sobre a candidíase oral.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Avaliação do risco de candidíase associado ao uso de rifaximina, incluindo a seleção de *Candida* resistente.
- Esclarecimento da situação regulatória do registro cancelado e da forma farmacêutica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

