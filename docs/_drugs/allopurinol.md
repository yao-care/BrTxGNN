---
layout: default
title: Allopurinol
parent: Apenas Predição do Modelo (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-28
description: "Allopurinol: nova indicação prevista, Porfiria hepática (hepatic porphyria) (nível de evidência L5). Indicação original: Antigotosos (gota)"
---

# Allopurinol
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

## Alopurinol: Da gota à porfiria hepática
{: .text-alpha }

## Resumo em Uma Frase

Alopurinol é um inibidor da xantina oxidase, registrado no Brasil na categoria de antigotosos, ou seja, usado originalmente no tratamento da gota.
O modelo TxGNN prevê que ele pode ser eficaz para **porfiria hepática (hepatic porphyria)**, mas atualmente há **0 ensaios clínicos** e apenas **2 publicações** relacionadas ao tema geral, sem nenhum estudo que teste o alopurinol nessa doença.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antigotosos (gota) |
| Nova Indicação Prevista | Porfiria hepática (hepatic porphyria) |
| Pontuação de Previsão TxGNN | 0,9995 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, o alopurinol inibe a xantina oxidase, enzima da via de degradação das purinas, reduzindo a produção de ácido úrico. É essa ação que sustenta seu uso na gota.

A ligação com a porfiria hepática é incerta. As crises de porfiria aguda são impulsionadas pela indução da enzima ALAS1, que controla a síntese do heme no fígado. Um fármaco que altere os estoques hepáticos de heme poderia, em teoria, ser relevante, mas também prejudicial; a direção do efeito não está definida. Os dados compilados não demonstram que o alopurinol tenha essa ação, e a pontuação alta do modelo, por si só, não constitui evidência.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Nenhuma das publicações abaixo testa o alopurinol em pacientes com porfiria; são estudos sobre o tema em geral.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisão (hipótese) | Medical Hypotheses | Propõe tratar porfirias hepáticas agudas por meio do controle metabólico da ALAS1, com triptofano ou inibição do uso de heme pela triptofano 2,3-dioxigenase. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Pré-clínico (animal) | Biochemical Pharmacology | Em ratos, a carbamazepina em dose baixa alterou o metabolismo do heme hepático, em linha com o mecanismo pelo qual agrava porfirias. |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 183260035 | ALOPURINOL | Não informada | Antigotosos |
| Registro nº 100470331 | ALOPURINOL | Não informada | Antigotosos |
| Registro nº 100681154 | ALOPURINOL | Não informada | Antigotosos |
| Registro nº 137640122 | ZYLORIC | Não informada | Não informada |
| Registro nº 125680191 | ALOPURINOL | Não informada | Antigotosos |

---

## Considerações de Segurança

- **Contraindicações e condições de risco registradas no grafo de conhecimento** (relações do grafo, não texto de bula): doença hepática, doença da vesícula biliar, função renal comprometida, vasculite de hipersensibilidade, angeíte leucocitoclástica cutânea, vasculite cutânea alérgica e doença anti-membrana basal glomerular.
- **Interações Medicamentosas**: foram identificadas 100 interações no total. As de nível moderado incluem hidróxido de alumínio, atapulgita, caulim, magaldrato e sucralfato. Amoxicilina e clorpropamida são de nível leve. Há ainda interações de nível não classificado, como calcitriol, vitamina A, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, acarbose, morfina, metformina, omeprazol, rosiglitazona e palonosetrona.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas no modelo (nível L5): não há ensaios clínicos nem estudos que avaliem o alopurinol na porfiria hepática. Além disso, a perturbação do metabolismo do heme poderia agravar a doença.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA e analisar advertências e contraindicações, lacuna que impede a triagem de segurança.
- Levantar dados de mecanismo de ação e investigar o efeito do alopurinol sobre o heme hepático e a ALAS1.
- Realizar estudos pré-clínicos que mostrem a direção do efeito (benefício ou agravamento) antes de qualquer estudo clínico.
- Verificar se a pontuação alta é específica da doença ou se reflete semelhanças que o modelo TxGNN (deep learning) aprendeu entre doenças relacionadas, e não evidência biológica, já que várias outras doenças hepáticas têm pontuações praticamente idênticas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

