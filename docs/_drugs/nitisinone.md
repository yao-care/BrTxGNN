---
layout: default
title: Nitisinone
parent: Apenas Predição do Modelo (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Nitisinone: nova indicação prevista, Acidose tubular renal (renal tubular acidosis) (nível de evidência L5). Indicação original: Outros produtos para o trato alimentar e metabolismo"
monitor_inn: "nitisinone"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
---

# Nitisinone
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

## Nitisinona: De produtos para o trato alimentar e metabolismo à acidose tubular renal
{: .text-alpha }

## Resumo em Uma Frase

Nitisinona (ORFADIN) foi originalmente registrada na ANVISA na categoria "outros produtos para o trato alimentar e metabolismo". Na prática, é usada na tirosinemia hereditária tipo 1.
O modelo TxGNN prevê que pode ser eficaz para **acidose tubular renal (renal tubular acidosis)**, mas **não há ensaios clínicos nem publicações** que apoiem esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o trato alimentar e metabolismo |
| Nova Indicação Prevista | Acidose tubular renal (renal tubular acidosis) |
| Pontuação de Previsão TxGNN | 0,9996 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 4) |
| Número de Registros | 4 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a nitisinona inibe a enzima 4-hidroxifenilpiruvato dioxigenase (HPPD) e é usada na tirosinemia hereditária tipo 1, doença em que metabólitos tóxicos (como a succinilacetona) podem causar tubulopatia proximal do tipo Fanconi.

A relação com a acidose tubular renal seria apenas indireta: ao reduzir a toxicidade tubular nessa doença de base, o fármaco poderia atenuar a disfunção dos túbulos renais. Não há evidência clínica ou da literatura que sustente essa ligação.

A pontuação alta do TxGNN (0,9996) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica, portanto não deve ser interpretada como prova de eficácia.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 138400002 | ORFADIN | INNOVATIVE MEDICINES BRASIL SP DISTRIBUICAO DE MED | Ativo |
| 138400003 | ORFADIN | INNOVATIVE MEDICINES BRASIL SP DISTRIBUICAO DE MED | Ativo |
| 175360002 | NITIKABS | PHARMEDIC PHARMACEUTICALS, IMPORTACAO, EXPORTACAO, | Ativo |
| 175360001 | NITIKABS | PHARMEDIC PHARMACEUTICALS IMPORTAÇÃO, DISTRIBUIÇÃO | Cancelado |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (relações fármaco-doença do grafo PrimeKG, não texto de bula): doença renal, piureter, trombocitopenia, leucopenia, hipofosfatemia e tirosinemia. A presença de "tirosinemia" nessa lista contrasta com o uso conhecido do fármaco e deve ser verificada.
- **Interações medicamentosas**: foram identificadas 201 interações. Entre as 20 listadas, a maioria é de gravidade moderada, por exemplo: abametapir (tópico), abiraterona, isotretinoína, nifedipino, ibuprofeno, aldesleucina, pioglitazona, amiodarona, anlodipino, amobarbital, apalutamida, aprepitanto, atazanavir, avatrombopague, baricitinibe, dexametasona, bexaroteno, bicalutamida e gengibre. A interação com armodafinila é de gravidade leve.

Para advertências e contraindicações da bula, consulte a bula aprovada, pois esses dados não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas no modelo (L5), sem ensaios clínicos ou literatura, e o mecanismo proposto é indireto.

**Para prosseguir, é necessário:**
- Obter os dados do mecanismo de ação (MOA) por meio do DrugBank.
- Baixar e analisar a bula da ANVISA para a triagem de segurança, hoje bloqueante.
- Realizar revisão sistemática da literatura sobre nitisinona e tubulopatia renal/acidose tubular.
- Avaliar estudos pré-clínicos que testem a hipótese de proteção tubular.
- Esclarecer a situação regulatória atual e a disponibilidade do produto no país.

---

**Outras previsões do modelo (todas com decisão Hold):**

| Posição | Doença prevista | Pontuação TxGNN | Nível de Evidência | Comentário |
|------|------|------|------|------|
| 2 | Galactosemia | 0,9995 | L5 | Apenas três revisões gerais sobre doenças hepáticas pediátricas; sobreposição de diagnóstico diferencial, sem racional terapêutico |
| 3 | Serpinopatia com polimerização tóxica de serpina | 0,9990 | L5 | Sem ligação mecanística clara |
| 4 | Deficiência de inibidor de C1 | 0,9990 | L5 | Sem ligação mecanística plausível |
| 5 | Doença de depósito de glicogênio | 0,9989 | L5 | Apenas uma revisão geral; sem evidência de efeito terapêutico |
| 6 | Doença do corpúsculo de poliglucosano do adulto | 0,9988 | L5 | Sem ligação mecanística evidente |
| 7 | Doença de depósito de glicogênio por deficiência de glicose-6-fosfatase | 0,9987 | L5 | Ligação apenas pela categoria geral de doenças metabólicas hepatorrenais |
| 8 | Síndrome de Griscelli | 0,9987 | L5 | Ligação tênue pela via da tirosina/melanina; a nitisinona eleva a tirosina e não corrige o defeito |
| 9 | Doença granulomatosa crônica ligada ao X | 0,9987 | L5 | Sem relação mecanística conhecida |
| 10 | Fenótipo ermine | 0,9987 | L5 | Ligação especulativa pela via tirosina/melanina |
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

