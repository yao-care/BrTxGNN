---
layout: default
title: Ocrelizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 482
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

# Ocrelizumabe: De imunossupressor seletivo a carcinoma de mama HER2 positivo

## Resumo em Uma Frase

Ocrelizumabe (OCREVUS) é um anticorpo monoclonal anti-CD20 que depleta células B, registrado na ANVISA na categoria de imunossupressores seletivos.
O modelo TxGNN prevê que pode ser eficaz para **carcinoma de mama HER2 positivo (HER2 positive breast carcinoma)**, mas **não há ensaios clínicos nem publicações** específicos para essa indicação que sustentem a previsão. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressores seletivos |
| Nova Indicação Prevista | Carcinoma de mama HER2 positivo (HER2 positive breast carcinoma) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o ocrelizumabe é um anticorpo monoclonal humanizado que se liga ao CD20 e depleta células B. Está aprovado em outros países para esclerose múltipla, e seu uso está ligado à imunossupressão seletiva.

Não se estabelece uma relação mecanística entre a indicação original e a nova indicação. O carcinoma de mama HER2 positivo é impulsionado pela amplificação do HER2, e o CD20 não é um alvo terapêutico reconhecido nessa doença. A pontuação elevada do TxGNN (0,999) reflete apenas proximidade no grafo de conhecimento, sem respaldo em estudos.

As demais previsões do modelo (câncer de mama com receptor de progesterona positivo ou negativo, subtipo normal-like, tumor de mama luminal A/B) apresentam pontuações semelhantes (0,998), também sem evidências. Os escores idênticos de duas dessas entradas sugerem um artefato da vizinhança no grafo, e não um sinal específico de doença.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101000666 (cancelado) | OCREVUS | Não informada | Imunossupressores seletivos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 280 interações no total. Entre as principais:
  - **Moderadas**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona); radiofármacos e agentes radiomarcados (iobenguano I-131, ibritumomabe tiuxetana, tositumomabe, samário-153 lexidronam); albendazol, pentamidina e levamisol.
  - **Leves**: sais de zinco (sulfato, acetato, gluconato, cloreto).

Consulte a bula para advertências e contraindicações.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem alta pontuação no modelo, mas nenhum ensaio clínico nem publicação a sustenta, e não há plausibilidade mecanística (CD20 não é alvo reconhecido no câncer de mama HER2 positivo). O nível de evidência é L5.
- O único registro no Brasil está cancelado, e não há dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA para análise de advertências e contraindicações
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos que testem se a depleção de células B/CD20 tem papel biológico no câncer de mama HER2 positivo
- Verificar a situação regulatória atual do produto no Brasil, já que o registro consta como cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

