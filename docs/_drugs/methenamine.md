---
layout: default
title: Methenamine
parent: Apenas Predição do Modelo (L5)
nav_order: 449
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Methenamine: nova indicação prevista, Uretrite por Ureaplasma (Ureaplasma urethritis) (nível de evidência L5). Indicação original: Antissépticos urinários – associações medicamentosas"
monitor_inn: "methenamine"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Methenamine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

# Metenamina: De antissépticos urinários para uretrite por Ureaplasma

## Resumo em Uma Frase

Metenamina é um antisséptico urinário, originalmente registrado no Brasil como associação medicamentosa de antissépticos urinários.
O modelo TxGNN prevê que pode ser eficaz para **uretrite por Ureaplasma (Ureaplasma urethritis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** que apoiem diretamente esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antissépticos urinários – associações medicamentosas |
| Nova Indicação Prevista | Uretrite por Ureaplasma (Ureaplasma urethritis) |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a metenamina é um pró-fármaco antisséptico urinário: em urina ácida (pH < 6), é hidrolisada em formaldeído, que exerce atividade bactericida inespecífica. Seu uso estabelecido é a profilaxia de infecções do trato urinário.

A uretrite é uma infecção da uretra, de modo que há exposição urinária plausível ao fármaco. Isso explica, em parte, a pontuação elevada do modelo.

Há, porém, limitações importantes. O *Ureaplasma* produz urease, o que pode elevar o pH urinário e prejudicar a liberação de formaldeído. Além disso, a uretrite é principalmente uma infecção da mucosa, e não do lúmen urinário, o que limita a exposição ao fármaco. A pontuação do TxGNN é apenas uma previsão computacional, sem respaldo de evidências clínicas.

### Outras previsões do modelo (todas sem suporte clínico)

| Indicação prevista | Pontuação TxGNN | Comentário |
|------|------|------|
| Uretrite gonocócica | 99,79% | Tratada com antibióticos sistêmicos (ex.: ceftriaxona); a metenamina é profilática e sem papel estabelecido em infecção tecidual ativa. Uso de agente não comprovado seria inadequado do ponto de vista de resistência antimicrobiana e saúde pública. |
| Doença inflamatória uterina | 99,77% | O fármaco não atinge concentrações antibacterianas relevantes no tecido uterino; vínculo mecanístico fraco. |
| Pielonefrite xantogranulomatosa | 99,73% | Infecção parenquimatosa e obstrutiva; a metenamina atua apenas na urina e a urease de *Proteus* bloqueia a liberação de formaldeído. O tratamento é cirúrgico mais antibióticos sistêmicos. |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (uretrite por Ureaplasma), atualmente não há literatura relacionada. Para as demais previsões, as publicações recuperadas não mostram eficácia da metenamina:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29369919](https://pubmed.ncbi.nlm.nih.gov/29369919/) | 2019 | Relato/série de casos | Int J Gynecol Pathol | Sete casos de endometrite actinomicótica em biópsias endometriais, a maioria com DIU de longa permanência. Patógeno e contexto diferentes; a metenamina aparece apenas como coloração histológica (prata metenamina), sem dados de eficácia do fármaco. |
| [19642728](https://pubmed.ncbi.nlm.nih.gov/19642728/) | 2009 | Série patológica/revisão | Arch Pathol Lab Med | Doenças renais não neoplásicas são comuns em peças de nefrectomia por tumor. Não há evidência sobre tratamento com metenamina. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104440066 (cancelado) | SEPURIN | Não informada | Antissépticos urinários – associações medicamentosas |
| Registro 102351376 (cancelado) | CYSTEX DUO | Não informada | Antissépticos urinários – associações medicamentosas |
| Registro 102350283 (cancelado) | CYSTEX | Não informada | Antissépticos urinários – associações medicamentosas |

## Considerações de Segurança

Não há advertências ou contraindicações da bula nos dados compilados; consulte a bula para essas informações.

- **Contraindicações descritas no grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): insuficiência hepática e doenças hepáticas (incluindo cirrose), doença renal, hipertensão, insuficiência cardíaca congestiva, doença arterial coronariana, parada cardíaca súbita, doenças da condução cardíaca, diabetes mellitus e cetoacidose diabética, hiperplasia prostática benigna, distúrbios de coagulação e hemofilia, anemias (incluindo macrocítica), deficiência de G6PD, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, doenças da vesícula biliar, gastrite, piureter, cistinúria, galactosemia, doença de depósito de glicogênio, miastenia gravis e doenças da junção neuromuscular.
- **Interações medicamentosas** (14 identificadas):
  - **Maior gravidade**: sulfassalazina e sulfametizol (as sulfonamidas podem formar precipitados insolúveis com o formaldeído na urina).
  - **Gravidade moderada**: agentes alcalinizantes da urina e antiácidos, que reduzem a acidez urinária e, com isso, a liberação de formaldeído — hidróxido de alumínio, carbonato de cálcio, magaldrato, carbonato, hidróxido e óxido de magnésio, citrato de potássio, citrato de sódio, acetato de sódio, bicarbonato de sódio e trometamina; além de picossulfato.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem apenas respaldo computacional (L5), sem ensaios clínicos nem literatura direta. Há obstáculos mecanísticos relevantes (urease do *Ureaplasma*, infecção de mucosa) e os registros brasileiros estão todos cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a lacuna de segurança bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação (ex.: via DrugBank).
- Estudos in vitro de atividade do formaldeído contra *Ureaplasma* em diferentes pHs e na presença de urease.
- Revisão sistemática da literatura sobre metenamina em uretrite e infecções genitais.
- Avaliar a viabilidade regulatória, dado que não há registro vigente no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

