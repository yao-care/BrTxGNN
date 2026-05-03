---
layout: default
title: Trihexyphenidyl
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trihexyphenidyl: Do Parkinson e Distonia ao Transtorno de Déficit de Atenção e Hiperatividade

## Resumo em Uma Frase

Trihexyphenidyl é um fármaco anticolinérgico amplamente utilizado como tratamento auxiliar da doença de Parkinson e de síndromes distônicas, atuando pelo bloqueio de receptores muscarínicos M1 nos gânglios da base.
O modelo TxGNN prevê que pode ser eficaz para o **Transtorno de Déficit de Atenção e Hiperatividade (ADHD)**, contudo há **0 ensaios clínicos** e apenas **1 publicação** — uma série de casos não relacionada diretamente ao TDAH — apoiando esta direção.
Importantemente, a análise mecanística aponta para uma **contradição farmacológica**: o bloqueio colinérgico pode prejudicar, e não melhorar, a função cognitiva e atencional no contexto do TDAH.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson e distonia (não registrado no Brasil) |
| Nova Indicação Prevista | Transtorno de Déficit de Atenção e Hiperatividade (ADHD) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, os dados formais de mecanismo de ação do Trihexyphenidyl não estão disponíveis neste pacote de evidências. Com base na literatura clínica consolidada, o fármaco é um antagonista muscarínico (anticolinérgico) que bloqueia receptores M1 de acetilcolina no sistema nervoso central, restaurando o equilíbrio dopaminérgico/colinérgico nos gânglios da base. É por esse mecanismo que atua eficazmente no alívio de tremor, rigidez e distonia — condições nas quais há excesso relativo de tônus colinérgico em relação ao dopaminérgico.

A previsão do TxGNN para o TDAH provavelmente decorre de sobreposições na rede de conhecimento: o Trihexyphenidyl está conectado a múltiplos distúrbios neurológicos (Parkinson, distonia, tiques), e o TDAH compartilha nódulos de comorbidade com algumas dessas condições — especialmente tiques e síndrome de Tourette. O modelo inferiu uma associação a partir de conexões indiretas no grafo de conhecimento, não de uma relação mecanística direta.

Contudo, existe uma **contradição farmacológica fundamental**: o TDAH é tratado aumentando a sinalização dopaminérgica e noradrenérgica no córtex pré-frontal (metilfenidato, anfetaminas, atomoxetina). O bloqueio colinérgico pelo Trihexyphenidyl pode, na prática, prejudicar a cognição e a regulação da atenção — efeito diametralmente oposto ao desejado. Não há evidência clínica de benefício no TDAH e há razão mecanística para suspeitar de risco de piora cognitiva, especialmente em crianças.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case Series | Movement Disorders | Série de casos descrevendo co-ocorrência de tiques e distonia idiopática persistente em múltiplos pacientes; aborda exclusivamente distonia, sem dados sobre TDAH — a relevância para esta previsão é indireta e periférica |

---

## Informações de Comercialização no Brasil

Trihexyphenidyl **não possui registro ativo na ANVISA** e não é comercializado no Brasil. Nenhuma licença foi identificada na consulta realizada em 2026-03-09.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para TDAH carece de suporte mecanístico e apresenta contradição farmacológica direta: o bloqueio colinérgico promovido pelo Trihexyphenidyl pode agravar déficits cognitivos e atencionais, contrariando o objetivo terapêutico central do TDAH. Não há ensaios clínicos registrados e a única publicação encontrada é uma série de casos sobre distonia, sem relação direta com o TDAH.

**Para prosseguir, é necessário:**
- Obter dados formais de mecanismo de ação via API do DrugBank (pendência DG002)
- Obter a bula/monografia oficial para levantamento completo de advertências, contraindicações e interações medicamentosas (pendência DG001)
- Reavaliar as indicações de menor rank com melhor plausibilidade mecanística: a indicação de **rank 5 — PLA2G6-associated neurodegeneration (PLAN)** — apresenta a conexão mecanística mais sólida de todo o pacote, pois o PLAN pode manifestar parkinsonismo e distonia, condições para as quais o Trihexyphenidyl já é tratamento estabelecido; esta indicação foi classificada como **Research Question** e é o candidato mais promissor para investigação adicional
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

