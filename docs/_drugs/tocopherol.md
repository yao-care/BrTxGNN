---
layout: default
title: Tocopherol
parent: Apenas Predição do Modelo (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
---

# Tocopherol
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

# Tocoferol: De produtos dermatológicos e vitamínicos para colangite esclerosante

## Resumo em Uma Frase

Tocoferol (vitamina E) foi registrado no Brasil em produtos de ação sobre pele e mucosas, em associações anti-inflamatórias/antirreumáticas e em associações vitamínicas.
O modelo TxGNN prevê que pode ser eficaz para **colangite esclerosante (sclerosing cholangitis)**, mas **não há ensaios clínicos** e apenas **1 publicação** observacional apoia essa direção. Trata-se, portanto, de uma previsão do modelo sem sustentação clínica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos com ação na pele e mucosas |
| Nova Indicação Prevista | Colangite esclerosante (Sclerosing Cholangitis) |
| Pontuação de Previsão TxGNN | 98,84% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o tocoferol é uma vitamina lipossolúvel com atividade antioxidante, usada no Brasil em produtos dermatológicos, em associações anti-inflamatórias e em suplementos vitamínicos.

A colestase crônica causa má absorção de vitaminas lipossolúveis (A, D, E e K) e está associada a estresse oxidativo e dano hepático. Por isso, a suplementação de vitamina E é biologicamente plausível. Contudo, o único estudo recuperado (2000) é observacional e mede níveis plasmáticos de antioxidantes; **não testa o tocoferol como tratamento**.

O escore de 98,84% é uma previsão computacional. A relação entre a indicação original (uso dermatológico e nutricional) e a nova indicação (doença hepática colestática) é indireta e ainda não foi avaliada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10735930](https://pubmed.ncbi.nlm.nih.gov/10735930/) | 2000 | Coorte | Aliment Pharmacol Ther | Descreve níveis plasmáticos de antioxidantes em doenças hepáticas colestáticas crônicas; a colestase leva à má absorção de vitaminas lipossolúveis e radicais livres podem participar do dano hepático. Não testa o tocoferol como terapia. |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102980212 (cancelado) | VITADERME | Não informada | Outros produtos com ação na pele e mucosas |
| Registro 110520001 (cancelado) | SALONPAS | Não informada | Anti-inflamatórios e antirreumáticos - associações medicamentosas |
| Registro 167730285 (cancelado) | NATUS GERIN | Não informada | Vitaminas ou minerais associados a outros fármacos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

---

## Outras Indicações Previstas (Visão Geral)

Para contexto, o modelo também previu outras indicações com pontuações semelhantes. A tabela resume a força da evidência de cada uma:

| Indicação | Pontuação TxGNN | Nível de Evidência | Resumo |
|------|------|------|------|
| Hipertensão pulmonar | 98,49% | L4 | Estudos majoritariamente em animais (frangos, ratos); sem dados em humanos |
| Artrite reumatoide | 98,44% | L3 | Coortes observacionais e ECR pequeno com suplemento combinado; resultados mistos |
| Alopecia | 98,06% | L4 | Evidência indireta; estudos pequenos sobre alopecia induzida por doxorrubicina, com resultados negativos em humanos |
| Insuficiência cardíaca congestiva | 97,83% | L3 | Ensaios grandes de vitamina E em doença cardiovascular foram neutros; revisões sugerem possível dano |
| Doença vascular periférica | 97,60% | L4 | Evidência indireta e fraca; um ensaio registrado (NCT04502849) não testa tocoferol como intervenção |
| Hipotricose simples do couro cabeludo, hipotricose congênita com milia, cardiopatia cifoescoliótica, alopecia areata difusa | 98,38% a 98,12% | L5 | Apenas previsão do modelo, sem estudos |

Entre essas, a **artrite reumatoide** é a que tem maior suporte relativo (L3, classificada como questão de pesquisa), embora ainda sem ensaio de fase 3 que teste o tocoferol isoladamente.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para colangite esclerosante, existe apenas uma publicação observacional e nenhum ensaio clínico; a pontuação alta do modelo não é respaldada por dados clínicos. Além disso, todos os registros brasileiros do tocoferol estão cancelados.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA para avaliar advertências e contraindicações (lacuna que impede a triagem de segurança)
- Obter dados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar revisão sistemática da literatura sobre vitamina E em doenças colestáticas e colangite esclerosante
- Considerar priorizar a artrite reumatoide, que tem a evidência mais consistente entre as indicações previstas, com avaliação de viabilidade de ensaio clínico
- Avaliar a compatibilidade de vias de administração e a estratégia regulatória, dado o status de registros cancelados
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

