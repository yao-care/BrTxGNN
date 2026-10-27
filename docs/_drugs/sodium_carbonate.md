---
layout: default
title: Sodium Carbonate
parent: Apenas Predição do Modelo (L5)
nav_order: 589
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sodium Carbonate: nova indicação prevista, Síndrome da cauda equina (cauda equina syndrome) (nível de evidência L5). Indicação original: Antiácido"
monitor_inn: "Sodium carbonate"
predicted_indications: ["cauda equina syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "obsolete neurogenic bladder (disease)", "dry eye syndrome", "ventricular tachycardia", "obsolete bundle branch block", "panuveitis (disease)", "Sjogren syndrome", "catecholaminergic polymorphic ventricular tachycardia"]
---

# Sodium Carbonate
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

## Carbonato de sódio: Do antiácido à síndrome da cauda equina
{: .text-alpha }

## Resumo em Uma Frase

O carbonato de sódio é um agente antiácido/alcalinizante, usado no Brasil em produtos para azia e má digestão (como os sais de fruta).
O modelo TxGNN prevê que ele possa ser eficaz para **síndrome da cauda equina (cauda equina syndrome)**, mas não há **nenhum ensaio clínico** nem **nenhuma publicação** que apoie essa previsão. Trata-se de uma previsão puramente computacional, sem respaldo clínico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiácido |
| Nova Indicação Prevista | Síndrome da cauda equina (cauda equina syndrome) |
| Pontuação de Previsão TxGNN | 99,80% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 10 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o carbonato de sódio é um agente alcalino que neutraliza o ácido gástrico, e sua utilização como antiácido está registrada na ANVISA.

**Não há relação mecanística plausível** entre essa ação e a síndrome da cauda equina. Essa síndrome é uma emergência neurológica compressiva, cujo tratamento depende de descompressão cirúrgica. A pontuação alta do TxGNN parece ser um artefato do grafo de conhecimento, sem respaldo clínico ou na literatura.

### Outras previsões do modelo

As demais previsões de maior pontuação também carecem de sustentação. A tabela resume o panorama:

| Doença prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Anafilaxia | 99,72% | L5 | Um artigo sobre formulação sublingual de epinefrina; sem relação terapêutica com o carbonato de sódio |
| Anafilaxia induzida por exercício dependente de alimento | 99,63% | L5 | Sem mecanismo nem evidências |
| Bexiga neurogênica (termo obsoleto) | 99,62% | L5 | Termo obsoleto na ontologia |
| Síndrome do olho seco | 99,58% | L4 | Evidência indireta (spray oral) |
| Taquicardia ventricular | 99,18% | L5 | Sem evidências |
| Bloqueio de ramo (termo obsoleto) | 98,97% | L5 | Provável artefato do grafo |
| Pan-uveíte | 98,89% | L5 | Sem relação plausível |
| Síndrome de Sjögren | 98,82% | L3 | Único sinal modesto, em nível de sintoma |
| Taquicardia ventricular polimórfica catecolaminérgica | 98,72% | L5 | Sem ação sobre a via envolvida |

A previsão com algum respaldo, ainda que fraco, é a **síndrome de Sjögren** (apenas alívio sintomático da boca seca), mas ela não é a de maior pontuação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Para a indicação principal (síndrome da cauda equina), atualmente não há literatura relacionada.

Para fins de contexto, as publicações encontradas para outras previsões foram:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27813150](https://pubmed.ncbi.nlm.nih.gov/27813150/) | 2017 | Estudo clínico exploratório | Gerodontology | Avaliou um spray de bicarbonato/carbonato de sódio com xilitol, associado a higiene oral profissional, em pacientes com síndrome de Sjögren primária (boca seca). Relevante apenas para sintomas orais, não para a doença autoimune nem para o olho seco |
| [34600046](https://pubmed.ncbi.nlm.nih.gov/34600046/) | 2021 | Estudo pré-clínico/de formulação | Eur J Pharm Sci | Estabilidade e permeabilidade da epinefrina sublingual para anafilaxia; o carbonato de sódio, se relevante, seria apenas excipiente (ajuste de pH) |

---

## Informações de Comercialização no Brasil

Todos os registros estão **cancelados**; atualmente não há produto de carbonato de sódio isolado com registro válido.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 144930071 | Estomanol | Não informada | Antiácido |
| Registro 103920245 | Stomvyc | Não informada | Antiácido |
| Registro 143810164 | Frusalt | Não informada | Antiácido |
| Registro 104810124 | Digiazia | Não informada | Antiácido |
| Registro 104971402 | Frutaxx | Não informada | Antiácido |

Foram listados os 5 primeiros dos 10 registros (todos cancelados). Entre os demais estão Sal de Fruta Eno e Sonrisal.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

Não foram encontradas interações medicamentosas nos dados compilados para este relatório. Como observação, o carbonato de sódio é um álcali mais forte que o bicarbonato, com risco de irritação se usado por via sistêmica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para síndrome da cauda equina não tem ensaios, literatura nem mecanismo plausível (nível L5), e provavelmente é um artefato do grafo de conhecimento. Além disso, não há registro válido no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pendência que impede a triagem de segurança
- Obter dados do mecanismo de ação no DrugBank
- Se houver interesse em uma direção de pesquisa, priorizar a **síndrome de Sjögren** (alívio de sintomas orais) como questão de pesquisa, com revisão do texto completo do PMID 27813150 e, se justificado, um ensaio controlado
- Considerar a ausência de registros válidos no Brasil em qualquer planejamento de desenvolvimento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

