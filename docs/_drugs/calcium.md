---
layout: default
title: Calcium
parent: Apenas Predição do Modelo (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Calcium: nova indicação prevista, Doença trombótica (Thrombotic Disease) (nível de evidência L5). Indicação original: Não disponível"
monitor_inn: "Calcium"
predicted_indications: ["thrombotic disease", "hemoglobinopathy", "female breast carcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "exostosis", "pyropoikilocytosis, hereditary", "vein disease", "non-inflammatory vasculopathy"]
---

# Calcium
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

## Cálcio: Da ausência de indicação registrada à doença trombótica
{: .text-alpha }

## Resumo em Uma Frase

O cálcio é um mineral essencial; não há indicação original registrada na ANVISA nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **doença trombótica (thrombotic disease)**,
mas **nenhum dos 2 ensaios clínicos** listados testa o cálcio, e a literatura encontrada é, em sua maior parte, indireta. A previsão é apenas computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (sem registros na ANVISA) |
| Nova Indicação Prevista | Doença trombótica (Thrombotic Disease) |
| Pontuação de Previsão TxGNN | 98,25% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. O cálcio é um cofator necessário na cascata de coagulação e na ativação plaquetária, por isso existe uma conexão biológica plausível com a trombose.

Contudo, a direção do efeito é desfavorável: o cálcio tende a **promover** a coagulação, e não a tratá-la. A literatura recuperada trata do papel do cálcio na ativação plaquetária (por exemplo, entrada de cálcio operada por reservas e fluxos de Ca²⁺ em plaquetas) e na trombo-inflamação. Isso descreve fisiopatologia, não benefício terapêutico.

A pontuação alta (0,98) reflete apenas a proximidade no grafo de conhecimento, sem respaldo clínico. A previsão deve ser tratada como hipótese a ser examinada com cautela, não como indicação de eficácia.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04319627](https://clinicaltrials.gov/study/NCT04319627) | Phase 3 | Recrutando | 2700 | Estatinas somadas a anticoagulantes para reduzir eventos venosos em tromboembolismo venoso; não testa cálcio |
| [NCT03692754](https://clinicaltrials.gov/study/NCT03692754) | Phase 2/3 | Desconhecido | 30 | Atorvastatina em trombocitopenia imune primária; não envolve cálcio |

Nenhum ensaio avalia o cálcio; ambos têm relevância baixa para esta previsão.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30530092](https://pubmed.ncbi.nlm.nih.gov/30530092/) | 2019 | Revisão | Cell Calcium | Entrada de cálcio operada por reservas (SOCE) na trombose e na trombo-inflamação |
| [38880165](https://pubmed.ncbi.nlm.nih.gov/38880165/) | 2024 | Revisão | Life Sciences | Alterações nos fluxos de cálcio e no metabolismo mitocondrial na ativação plaquetária |
| [39796525](https://pubmed.ncbi.nlm.nih.gov/39796525/) | 2024 | Revisão | Nutrients | Deficiência de vitamina D e risco de doença trombótica |
| [35993516](https://pubmed.ncbi.nlm.nih.gov/35993516/) | 2022 | Revisão | Am J Physiol Cell Physiol | Plaquetas pró-coagulantes na trombo-inflamação |
| [7648691](https://pubmed.ncbi.nlm.nih.gov/7648691/) | 1995 | Revisão | Circulation | Classificação histológica de lesões ateroscleróticas avançadas |
| [41055696](https://pubmed.ncbi.nlm.nih.gov/41055696/) | 2026 | Pré-clínico | Blood | STK10 regula a função plaquetária na trombose arterial |
| [40540747](https://pubmed.ncbi.nlm.nih.gov/40540747/) | 2025 | Pré-clínico | Blood | Canais LRRC8 regulam a ativação plaquetária e a trombose arterial |

Os estudos descrevem mecanismos de trombose, e não o uso do cálcio como tratamento.

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram identificadas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia apenas no modelo, sem ensaios com cálcio e com direção de efeito mecanisticamente desfavorável (o cálcio é pró-coagulante). Por isso, não há base para avançar.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação e de segurança (advertências e contraindicações da bula) ainda não disponíveis
- Evidência clínica direta com cálcio na doença trombótica, o que hoje não existe
- Justificativa farmacológica de que o cálcio poderia reduzir, e não aumentar, o risco trombótico

**Observação sobre outras previsões:** outras doenças previstas (por exemplo, hemoglobinopatias, câncer de mama feminino e beta-talassemia) também carecem de evidência direta de benefício do cálcio. O papel do cálcio nelas seria, no máximo, de suporte (saúde óssea, distúrbios endócrinos), e não de modificação da doença.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

