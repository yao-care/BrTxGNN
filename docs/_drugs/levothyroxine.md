---
layout: default
title: Levothyroxine
parent: Apenas Predição do Modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Levothyroxine: nova indicação prevista, Bócio nodular (Nodular Goiter) (nível de evidência L5). Indicação original: Hormônios tireoidianos simples ou associados entre si"
monitor_inn: "Levothyroxine"
predicted_indications: ["endemic goiter", "renal hypodysplasia/aplasia", "nodular goiter (disease)", "bilateral renal agenesis", "nontoxic goiter", "lingual goiter", "dyshormonogenic goiter", "substernal goiter", "Potter sequence", "Carney complex"]
---

# Levothyroxine
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

# Levotiroxina: Da reposição de hormônios tireoidianos ao bócio nodular

## Resumo em Uma Frase

A levotiroxina é um hormônio tireoidiano sintético, registrado no Brasil para o grupo de "hormônios tireoidianos simples ou associados entre si".
O modelo TxGNN prevê que pode ser eficaz para o **bócio nodular (Nodular Goiter)**, a indicação prevista com o maior respaldo de evidências entre as 10 candidatas, atualmente com **2 ensaios clínicos** e **19 publicações** apoiando esta direção.

> Observação: a previsão de maior pontuação do modelo foi o *bócio endêmico* (99,81%), mas sem ensaios registrados (apenas literatura). A previsão com evidências mais robustas é o bócio nodular, que é o foco deste relatório. As demais candidatas estão resumidas ao final.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hormônios tireoidianos simples ou associados entre si |
| Nova Indicação Prevista | Bócio nodular (Nodular Goiter) |
| Pontuação de Previsão TxGNN | 99,64% |
| Nível de Evidência | L1 (atribuído de forma conservadora; L2 é uma alternativa defensável) |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 6 (todos cancelados) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a levotiroxina é a forma sintética da tiroxina (T4) e atua repondo o hormônio tireoidiano e suprimindo a secreção de TSH pela hipófise.

O bócio nodular depende, em parte, do estímulo do TSH sobre as células foliculares da tireoide. Ao reduzir o TSH, a levotiroxina pode limitar o crescimento do tecido nodular. Essa lógica é a base da chamada "terapia supressiva" e liga diretamente a indicação original (reposição hormonal tireoidiana) à nova.

Essa plausibilidade biológica, porém, não equivale a benefício clínico comprovado. A literatura revisada aponta redução de volume modesta e inconsistente, retorno do crescimento após a suspensão e riscos de hipertireoidismo subclínico iatrogênico (perda óssea, fibrilação atrial). Por isso, iodo radioativo e cirurgia costumam ser preferidos em muitos cenários.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00277589](https://clinicaltrials.gov/study/NCT00277589) | Phase 4 | Concluído | 1024 | Ensaio randomizado, cego para o observador e controlado por placebo de terapia adaptada ao TSH em bócio nodular; desfecho primário: variação do volume total dos nódulos |
| [NCT00941551](https://clinicaltrials.gov/study/NCT00941551) | N/A | Concluído | 150 | Ensaio randomizado com seguimento de 5 anos: lobectomia unilateral com ou sem levotiroxina pós-operatória, avaliando recorrência de bócio nodular no lobo contralateral |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10426591](https://pubmed.ncbi.nlm.nih.gov/10426591/) | 1999 | Estudo clínico | Endocrine Journal | Terapia supressiva por 6 meses em 35 pacientes com bócio difuso e 35 com bócio nodular eutireoideu; avaliou volumes da tireoide e dos nódulos e tireoglobulina |
| [10382684](https://pubmed.ncbi.nlm.nih.gov/10382684/) | 1999 | Coorte retrospectiva | Endocrine Research | Comparou terapia supressiva e de reposição com levotiroxina em nódulo solitário e bócio multinodular |
| [20683172](https://pubmed.ncbi.nlm.nih.gov/20683172/) | 2010 | Estudo clínico | Endocrine Journal | Efeitos de curto prazo da levotiroxina em 71 mulheres pré-menopausa com doença multinodular |
| [19636201](https://pubmed.ncbi.nlm.nih.gov/19636201/) | 2009 | Retrospectivo | J Endocrinol Invest | Efeito da levotiroxina na recorrência nodular após hemitireoidectomia por bócio nodular benigno |
| [8844728](https://pubmed.ncbi.nlm.nih.gov/8844728/) | 1996 | Revisão | Otolaryngol Clin North Am | Avaliação e manejo do bócio multinodular |
| [39475129](https://pubmed.ncbi.nlm.nih.gov/39475129/) | 2024 | Revisão | Endokrynologia Polska | Atualização sobre opções de tratamento da tireoidite autoimune |
| [34867359](https://pubmed.ncbi.nlm.nih.gov/34867359/) | 2021 | Revisão | Frontiers in Pharmacology | Medicina de precisão na tireoidite autoimune e no hipotireoidismo |
| [25189867](https://pubmed.ncbi.nlm.nih.gov/25189867/) | 2015 | Revisão | Eur J Endocrinol | TSH recombinante e iodo radioativo como alternativa no bócio multinodular benigno |
| [12397534](https://pubmed.ncbi.nlm.nih.gov/12397534/) | 2002 | Coorte | Exp Clin Endocrinol Diabetes | Seguimento de longo prazo (3 a 12 anos) do crescimento de nódulos tireoidianos benignos em 109 pacientes |
| [36316779](https://pubmed.ncbi.nlm.nih.gov/36316779/) | 2022 | Estudo de desfechos | Thyroid Research | Desfechos de longo prazo após bócio nodular tóxico |

## Informações de Comercialização no Brasil

Todos os 6 registros encontrados estão **cancelados**; atualmente não há registro válido de levotiroxina nos dados compilados.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100890359 | Euthyrox | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro 105530329 | Synthroid | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro 100890416 | Levotiroxina Sódica | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro 183260353 | Puran T4 | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro 105730366 | Levoid | Não informada | Hormônios tireoidianos simples ou associados entre si |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: o grafo de conhecimento do TxGNN associa a levotiroxina a contraindicações em: hipertensão arterial, hipopituitarismo e deficiências hormonais hipofisárias (incluindo deficiência isolada de hormônio do crescimento, hipogonadismo hipogonadotrófico e síndrome de Kallmann), síndrome de Sheehan, osteoporose (inclusive pós-menopausa), diabetes mellitus, cetoacidose diabética, doença arterial coronariana e infarto do miocárdio, além de doenças do timo. Essas informações não vêm da bula e devem ser confirmadas nela.
- **Riscos relatados na literatura**: hipertireoidismo subclínico iatrogênico pode causar perda óssea e arritmias, como fibrilação atrial, com a supressão do TSH.
- **Interações medicamentosas** (100 registradas; principais, em sua maioria de gravidade moderada):
  - Antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida, albiglutida, dulaglutida): possível alteração do controle glicêmico.
  - Inibidores da bomba de prótons (omeprazol, rabeprazol, dexlansoprazol): podem reduzir a absorção da levotiroxina.
  - Sais de cálcio e magnésio (fosfato e acetato de cálcio, óxido de magnésio): podem reduzir a absorção.
  - Simpatomiméticos (epinefrina, isometepteno, dietilpropiona): possível potencialização dos efeitos cardiovasculares.
  - Cimetidina: interação de gravidade leve.

Para advertências e contraindicações oficiais, consulte a bula.

## Outras Indicações Previstas (Resumo)

| Indicação | Pontuação TxGNN | Nível | Recomendação | Comentário |
|------|------|------|------|------|
| Bócio endêmico | 99,81% | L3 | Proceed with Guardrails | Estudos multicêntricos e comparativos (levotiroxina, iodo ou combinação); sem ensaios registrados |
| Bócio não tóxico | 99,36% | L3 | Proceed with Guardrails | Um ensaio randomizado vs. iodo radioativo (PMID 11238476); revisões indicam benefício modesto; sobreposição com o bócio nodular |
| Bócio lingual | 99,36% | L4 | Pergunta de pesquisa | Apenas relatos de caso |
| Bócio disormonogênico | 99,36% | L4 | Pergunta de pesquisa | Apenas estudo pré-clínico indireto |
| Bócio subesternal | 99,36% | L4 | Hold | A cirurgia é o tratamento principal; sem evidência direta |
| Hipodisplasia/aplasia renal, agenesia renal bilateral, sequência de Potter, complexo de Carney | 99,18% a 99,66% | L5 | Hold | Sem evidências nem vínculo mecanístico plausível; as três primeiras são malformações congênitas que a reposição tireoidiana não trataria |

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Para o bócio nodular, há dois ensaios randomizados concluídos (um de fase 4 com 1.024 participantes, controlado por placebo), o que sustenta o nível L1 de forma conservadora, já que nenhum é fase 3. A literatura, porém, mostra benefício limitado e inconsistente, com riscos de supressão excessiva do TSH.

**Para prosseguir, é necessário:**
- Obter e analisar os resultados completos de NCT00277589 e NCT00941551, que não constam nos dados compilados.
- Completar os dados de mecanismo de ação e de advertências e contraindicações da bula da ANVISA.
- Resolver a situação regulatória: todos os 6 registros estão cancelados, então é preciso verificar a disponibilidade de produto com registro válido.
- Definir salvaguardas: meta cuidadosa de TSH, restrição a pacientes selecionados (por exemplo, deficiência de iodo, mais jovens, nódulos pequenos) e monitoramento ósseo e cardíaco.
- Revisar o texto completo do ensaio randomizado do bócio não tóxico (PMID 11238476) e consolidar a análise com a do bócio nodular, dada a sobreposição.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

