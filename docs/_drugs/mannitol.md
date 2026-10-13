---
layout: default
title: Mannitol
parent: Apenas Predição do Modelo (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Manitol: Do uso como diurético osmótico à síndrome nefrogênica de antidiurese inapropriada

## Resumo em Uma Frase

Manitol é um diurético osmótico, registrado no Brasil principalmente como diurético e para reposição hidroeletrolítica e alimentação parenteral.
O modelo TxGNN prevê que ele possa ser eficaz para a **síndrome nefrogênica de antidiurese inapropriada (nephrogenic syndrome of inappropriate antidiuresis, NSIAD)**,
mas hoje há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão geral sobre hiponatremia, sem evidência específica do fármaco) ligada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Reposição hidroeletrolítica e alimentação parenteral |
| Nova Indicação Prevista | Síndrome nefrogênica de antidiurese inapropriada (nephrogenic syndrome of inappropriate antidiuresis) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o manitol é um diurético osmótico: ele é filtrado pelos rins e não é reabsorvido, arrastando água para a urina. Por isso, existe um vínculo teórico com a excreção de água.

A NSIAD, porém, é causada por mutação de ganho de função no receptor V2 da vasopressina (AVPR2), que mantém os rins retendo água de forma inadequada, com hiponatremia. A diurese osmótica não é um tratamento estabelecido para essa causa. Além disso, o manitol pode piorar a hiponatremia por deslocamentos osmóticos de água.

A pontuação alta do modelo, portanto, não é sustentada por plausibilidade mecanística clara. A única publicação encontrada é uma revisão geral sobre armadilhas na avaliação da hiponatremia, que não traz evidência específica sobre o manitol.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Revisão | European Journal of Internal Medicine | Descreve as dez armadilhas mais comuns na avaliação de pacientes com hiponatremia e os riscos de tratamento inadequado (sub ou, sobretudo, supertratamento). Não é evidência específica do manitol. |

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados. Principais registros (máximo de 5):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 117720008 | Solução de Manitol Equiplex | Não informada | Reposição hidroeletrolítica e alimentação parenteral |
| Registro 111200002 | Manitol a 20% Basa | Não informada | Diuréticos |
| Registro 106830090 | Manitol Baxter | Não informada | Diuréticos osmóticos |
| Registro 126800003 | Manitol 20% | Não informada | Diuréticos simples |
| Registro 104910067 | Manitol 3% | Não informada | Produtos para vias urinárias |

## Considerações de Segurança

- **Contraindicações (previstas pelo grafo de conhecimento do TxGNN, não extraídas de bula):** insuficiência hepática, doença hepática, encefalopatia/coma hepático, anúria, função renal prejudicada, edema pulmonar, hemorragia intracraniana, trombocitopenia, neutropenia, agranulocitose, anemias, porfirias, doenças da vesícula biliar, apneia do sono e transtornos relacionados ao uso de substâncias, entre outras.
- **Interações medicamentosas:** foram identificadas 100 interações no total. Entre as exibidas, a de nível **grave (Major)** é com **amicacina**. Interações de nível moderado incluem lamivudina, formoterol, salbutamol, amifostina, benazepril, captopril, carbamazepina, cisatracúrio, citalopram, canagliflozina, dapagliflozina, desvenlafaxina, bisacodil, ácido picossulfúrico, polietilenoglicol com eletrólitos, ácido iotalâmico e diatrizoato. A interação com doxiciclina é de nível leve.
- **Considerações específicas da indicação prevista:** a literatura aponta risco de sobrecarga de volume e edema pulmonar com manitol, e o fármaco poderia piorar a hiponatremia por deslocamento osmótico de água.

Consulte a bula para as advertências e contraindicações oficiais, pois não estão disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia apenas na pontuação do modelo (nível L5): não há ensaios clínicos, a única publicação não é específica do manitol, e o mecanismo da doença (ganho de função do AVPR2) não é plausivelmente tratável por diurese osmótica, com risco de piora da hiponatremia. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação do manitol (por exemplo, via DrugBank).
- Realizar revisão mecanística e pré-clínica que justifique um papel do manitol na NSIAD, considerando o risco de agravar a hiponatremia.
- Confirmar a situação regulatória (registros cancelados) e a disponibilidade de formas farmacêuticas e vias de administração compatíveis.
- Considerar priorizar outras previsões com evidência indireta mais plausível, como a doença cardíaca pulmonar aguda (nível L4), embora também careça de ensaios diretos.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

