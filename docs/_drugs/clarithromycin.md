---
layout: default
title: Clarithromycin
parent: Apenas Predição do Modelo (L5)
nav_order: 226
evidence_level: L5
indication_count: 5
monitor_inn: "Clarithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-10-23
description: "Clarithromycin: nova indicação prevista, Hiperamilasemia (nível de evidência L5). Indicação original: Macrolídeos"
---

# Clarithromycin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

## Claritromicina: De macrolídeo antibacteriano à hiperamilasemia
{: .text-alpha }

## Resumo em Uma Frase

Claritromicina é um antibiótico macrolídeo sistêmico, registrado no Brasil na categoria de macrolídeos e antibióticos sistêmicos simples.
O modelo TxGNN prevê que pode ser eficaz para **hiperamilasemia (hyperamylasemia)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (um relato de caso) ligada a essa direção, sem estudo que avalie diretamente o efeito do fármaco sobre a doença.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Macrolídeos (classificação terapêutica registrada na ANVISA; o texto não detalha as doenças tratadas) |
| Nova Indicação Prevista | Hiperamilasemia |
| Pontuação de Previsão TxGNN | 0,9935 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | Pelo menos 20 registros (a lista pode estar incompleta) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a claritromicina é um antibiótico macrolídeo, cuja eficácia contra infecções bacterianas é bem estabelecida.

Não há relação mecanística plausível entre a claritromicina e a hiperamilasemia. A única publicação associada (PMID 15228140, 2004) é um relato de caso de infecção pulmonar por *Mycobacterium abscessus* acompanhada de macroamilasemia primária. Nesse caso, o antibiótico serve ao tratamento da infecção, e a coexistência com a elevação da amilase é incidental. O relato não mostra efeito do fármaco sobre os níveis de amilase.

A pontuação alta do TxGNN (modelo de deep learning) vem do modelo e pode refletir semelhanças que ele aprendeu entre doenças relacionadas, e não evidência biológica ou clínica. Como nenhum estudo citado avalia diretamente a hiperamilasemia como alvo terapêutico, o nível de evidência é L5, apesar de o relato de caso mencionar a condição.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Relato de caso | Nihon Kokyuki Gakkai Zasshi | Homem de 76 anos com infecção pulmonar por *M. abscessus* e macroamilasemia primária concomitante; não demonstra efeito do fármaco sobre a amilase |

## Informações de Comercialização no Brasil

Os registros abaixo correspondem aos cinco primeiros da lista, que pode estar incompleta (pelo menos 20 registros válidos de produtos com um único princípio ativo).

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105530200 | Klaricid | Não informada | Macrolídeos |
| Registro nº 155620025 | Claritromicina | Não informada | Macrolídeos |
| Registro nº 141070628 | Claritromicina | Não informada | Macrolídeos |
| Registro nº 125680366 | Claritromicina | Não informada | Macrolídeos |
| Registro nº 183260025 | Claritromicina | Não informada | Macrolídeos |

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (relações do grafo, não texto de bula): síndrome do QT longo, torsades de pointes, taquicardia ventricular (incluindo formas catecolaminérgica e infantil incessante), insuficiência hepática, doença hepática, colestase (incluindo formas intra-hepáticas benigna recorrente e familiar), porfirias, doença renal, doença da vesícula biliar, osteoporose (incluindo pós-menopausa), fratura óssea, colite por *Clostridium difficile*, enterocolite necrosante perinatal, miastenia gravis e doenças da junção neuromuscular, mononucleose infecciosa e síndrome de infecção crônica pelo vírus Epstein-Barr.
- **Interações medicamentosas**: foram identificadas 100 interações. Entre as listadas, as de gravidade **grave** incluem abemaciclibe, fentanila e acalabrutinibe. Há ainda várias de gravidade moderada (por exemplo, paclitaxel, tramadol, nifedipino, etinilestradiol, hidrocortisona, afatinibe, adenosina, acarbose e formoterol) e leves (dolutegravir, zidovudina, loratadina). A claritromicina inibe CYP3A4 e P-gp, o que acrescenta risco sem benefício demonstrado nesta indicação.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos, e a única publicação é um relato de caso em que a hiperamilasemia coexiste com a infecção, sem efeito do fármaco demonstrado. Não há mecanismo plausível, e a pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica. O perfil de interações e as contraindicações cardíacas e hepáticas aumentariam o risco sem benefício comprovado.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação da claritromicina.
- Estudos que avaliem diretamente o efeito do fármaco sobre a hiperamilasemia.
- Advertências e contraindicações extraídas da bula aprovada pela ANVISA.
- Análise de segurança, com foco em prolongamento do intervalo QT e interações via CYP3A4.

**Observação sobre outras previsões:** entre as demais indicações previstas, a ceratoconjuntivite epitelial punctata (PMID 38472959, estudo retrospectivo de 2024 em ceratoconjuntivite relacionada à meibomite) é a que tem base mais plausível, como questão de pesquisa. Síndrome de hiperviscosidade policlonal, analbuminemia congênita e incompatibilidade de grupo sanguíneo não têm evidências nem mecanismo plausível.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

