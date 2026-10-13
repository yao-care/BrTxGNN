---
layout: default
title: Allopurinol
parent: Evidência Moderada (L3-L4)
nav_order: 40
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
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

# Alopurinol: Do tratamento da gota à porfiria hepática

## Resumo em Uma Frase

O alopurinol é um inibidor da xantina oxidase, originalmente registrado no Brasil como antigotoso.
O modelo TxGNN prevê que pode ser eficaz para **porfiria hepática (hepatic porphyria)**,
mas atualmente há **0 ensaios clínicos** e apenas **2 publicações** (uma hipótese e um estudo animal, ambos indiretos) associadas a esta previsão. Nenhuma delas demonstra efeito terapêutico do alopurinol.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antigotosos (gota) |
| Nova Indicação Prevista | Porfiria hepática (hepatic porphyria) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 5 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o alopurinol é um inibidor da xantina oxidase, que reduz a produção de ácido úrico, e sua utilização em gota está estabelecida.

A ligação com a porfiria hepática é **indireta e especulativa**. Um artigo de hipótese de 2019 propõe direcionar a enzima 5-aminolevulinato sintase (ALAS1) por meio de triptofano e inibidores do uso de heme pelo triptofano 2,3-dioxigenase. Um estudo de 1992 em ratos avaliou os efeitos da carbamazepina sobre o metabolismo do heme hepático. Nenhum dos dois estudou o alopurinol nem mostrou efeito terapêutico dele em porfiria.

Não há um mecanismo claro que conecte a inibição da xantina oxidase à biossíntese do heme. Literatura antiga sugere que o alopurinol poderia influenciar o turnover de heme/citocromo P450 hepático, mas isso não é sustentado pelos dados compilados. A pontuação alta do modelo reflete sobretudo associações no grafo de conhecimento, não evidência específica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisão/hipótese | Medical Hypotheses | Propõe o direcionamento metabólico da ALAS1 hepática, via triptofano ou inibição do uso de heme pela triptofano 2,3-dioxigenase, como terapia das porfirias hepáticas agudas. Não envolve o alopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Pré-clínico (animal) | Biochemical Pharmacology | A carbamazepina, em dose muito baixa, agravou o metabolismo do heme em fígado de rato, potencializando a perda de heme utilizado pela triptofano pirrolase. Não envolve o alopurinol. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 183260035 | ALOPURINOL | Não informada | Antigotosos (cancelado) |
| Registro nº 100470331 | ALOPURINOL | Não informada | Antigotosos (cancelado) |
| Registro nº 100681154 | ALOPURINOL | Não informada | Antigotosos (cancelado) |
| Registro nº 137640122 | ZYLORIC | Não informada | Não informada (cancelado) |
| Registro nº 125680191 | ALOPURINOL | Não informada | Antigotosos (cancelado) |

## Considerações de Segurança

- **Contraindicações e condições de risco (grafo de conhecimento TxGNN, não texto de bula)**: doença hepática, doença da vesícula biliar, insuficiência da função renal, vasculite de hipersensibilidade, angeíte leucocitoclástica cutânea, vasculite cutânea alérgica e doença antimembrana basal glomerular. Chama atenção o fato de a porfiria hepática ser uma doença do fígado, o que exige cautela adicional.
- **Interações Medicamentosas** (100 interações registradas; principais exemplos):
  - Moderadas: hidróxido de alumínio, atapulgita, caulim, magaldrato e sucralfato (antiácidos e protetores de mucosa).
  - Leves: amoxicilina e clorpropamida.
  - Nível não classificado: calcitriol, vitamina A, pantoprazol, glimepirida, mesalazina, doxiciclina, clotrimazol, acarbose, morfina, metformina, omeprazol, rosiglitazona e palonosetrona.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia essencialmente no modelo: não há ensaios clínicos, e a literatura disponível é uma hipótese e um estudo animal que não envolvem o alopurinol. Além disso, todos os registros brasileiros estão cancelados e os dados de bula não estão disponíveis, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank e investigar a relação entre a inibição da xantina oxidase e o metabolismo do heme.
- Realizar estudos pré-clínicos específicos de alopurinol em modelos de porfiria hepática.
- Avaliar a segurança em pacientes com doença hepática, dada a presença dessa condição entre as contraindicações do grafo de conhecimento.
- Esclarecer a situação regulatória, já que não há registro vigente no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

