---
layout: default
title: Dexlansoprazole
parent: Apenas Predição do Modelo (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Dexlansoprazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Dexlansoprazol: De antiácido e antiulceroso para doença ulcerosa péptica ativa

## Resumo em Uma Frase

Dexlansoprazol (DEXILANT) é um inibidor da bomba de prótons, originalmente registrado na ANVISA na categoria de antiácidos e antiulcerosos.
O modelo TxGNN prevê que pode ser eficaz para **doença ulcerosa péptica ativa (active peptic ulcer disease)**,
mas, até o momento, a previsão conta com apenas **2 ensaios clínicos de Fase 3** (voltados à esofagite erosiva, portanto com apoio apenas indireto) e **3 publicações** associadas a essa indicação.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiácidos e antiulcerosos |
| Nova Indicação Prevista | Doença ulcerosa péptica ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L4 (ensaios disponíveis são de esofagite erosiva; evidência direta para úlcera não confirmada) |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o dexlansoprazol é um inibidor da bomba de prótons (H+/K+ ATPase) das células parietais gástricas, com formulação de liberação dupla e retardada que prolonga a supressão ácida. Essa é a base do efeito da classe dos IBPs na cicatrização de úlceras pépticas ácido-dependentes.

A indicação original (antiácidos e antiulcerosos) e a nova indicação prevista são, na prática, muito próximas: ambas dependem da redução da acidez gástrica. Por isso, o score alto do modelo é biologicamente plausível, embora em parte reflita a proximidade do fármaco com o tema "úlcera" na rede de conhecimento.

É importante ressaltar que os dois ensaios de Fase 3 listados parecem avaliar a cicatrização de **esofagite erosiva**, e não de úlcera péptica. Eles fornecem dados de segurança e de supressão ácida, mas apenas apoio indireto à cicatrização de úlcera. A evidência para a classe dos IBPs em úlcera péptica é robusta; dados específicos do dexlansoprazol ainda não foram confirmados.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Concluído | 2054 | Dexlansoprazol MR (60 e 90 mg/dia) vs. lansoprazol 30 mg por 8 semanas na cicatrização de esofagite erosiva; apoio indireto para úlcera |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Concluído | 2038 | Estudo companheiro, mesmo desenho; dados de segurança e supressão ácida |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisão sistemática/Meta-análise | The American Journal of Gastroenterology | Compara bloqueadores ácidos competitivos de potássio (P-CAB) com IBPs na cicatrização de esofagite grau C/D |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Revisão | Current Opinion in Investigational Drugs | Desenvolvimento do dexlansoprazol, formulação de liberação modificada de um enantiômero do lansoprazol, para esofagite de refluxo |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Pré-clínico/Mecanístico | Journal of the Chinese Medical Association | Supressão da ATPase vacuolar e estresse do retículo endoplasmático por IBPs, em contexto de risco de câncer gástrico com uso prolongado |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 106390261 (cancelado) | DEXILANT | Não informada | Antiácidos e antiulcerosos |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: doença hepática, doença da vesícula biliar, osteoporose, osteoporose pós-menopausa e fratura óssea.
- **Interações medicamentosas**: foram identificadas 118 interações; entre as listadas, destacam-se as de gravidade **maior** com **acalabrutinibe** e **atazanavir**. Há também interações moderadas, por exemplo com furosemida, hidroclorotiazida, gefitinibe, bosutinibe, anfotericina B, amicacina, ampicilina, fosamprenavir, foscarnete, fostamatinibe, anfetamina e bumetanida, além de interações menores, como com ácido acetilsalicílico, axitinibe, brivaracetam e cianocobalamina.

Consulte a bula para informações complementares de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- O mecanismo é plausível e a evidência de classe dos IBPs em úlcera péptica é forte, mas os ensaios de Fase 3 do dexlansoprazol são de esofagite erosiva, sem confirmação de desfechos de úlcera. Além disso, o único registro no Brasil está cancelado e há lacunas de dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações) para a triagem de segurança.
- Confirmar o mecanismo de ação em fonte primária (DrugBank).
- Confirmar o mapeamento das doenças nos ensaios de Fase 3 e acompanhar os resultados do ensaio de Fase 4 NCT07344506 (em recrutamento, 942 participantes, erradicação de *H. pylori*).
- Avaliar a situação regulatória no Brasil (registro cancelado) e a viabilidade de nova submissão ou de alternativas disponíveis da classe.
- Revisar o risco associado às contraindicações do grafo (doença hepática, osteoporose/fraturas) e às interações de gravidade maior.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

