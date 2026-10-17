---
layout: default
title: Clobutinol
parent: Apenas Predição do Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clobutinol: nova indicação prevista, Febre tifoide (typhoid fever) (nível de evidência L5). Indicação original: Não há indicação registrada na ANVISA (conhecido como antitussígeno d…"
monitor_inn: "Clobutinol"
predicted_indications: ["typhoid fever", "mucocutaneous leishmaniasis", "leishmaniasis, diffuse cutaneous", "diffuse scleroderma", "pneumonia", "trigonitis", "bronchiolitis obliterans with obstructive pulmonary disease", "paratyphoid fever", "cystitis", "combined immunodeficiency due to DOCK8 deficiency"]
---

# Clobutinol
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

# Clobutinol: Do antitussígeno de ação central à febre tifoide

## Resumo em Uma Frase

Clobutinol é um antitussígeno de ação central, usado para suprimir a tosse e retirado do mercado em 2007 por causar prolongamento do intervalo QT.
O modelo TxGNN prevê que pode ser eficaz para **febre tifoide (typhoid fever)**, mas **não há ensaios clínicos nem publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não há indicação registrada na ANVISA (conhecido como antitussígeno de ação central) |
| Nova Indicação Prevista | Febre tifoide (typhoid fever) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o clobutinol é um antitussígeno de ação central, que reduz a tosse de forma sintomática. Foi retirado do mercado em 2007 por causa do prolongamento do intervalo QT e do bloqueio do canal hERG.

Não há relação mecanística estabelecida entre a supressão central da tosse e a febre tifoide. O clobutinol não tem atividade antibacteriana conhecida contra *Salmonella* Typhi. A pontuação elevada do TxGNN vem apenas de padrões no grafo de conhecimento e, por si só, não demonstra benefício terapêutico.

Os demais candidatos previstos têm a mesma limitação: não há evidência clínica ou da literatura e não há mecanismo plausível. São eles: leishmaniose mucocutânea, leishmaniose cutânea difusa, esclerodermia difusa, pneumonia, trigonite, bronquiolite obliterante com doença pulmonar obstrutiva, febre paratifoide, cistite e imunodeficiência combinada por deficiência de DOCK8. Na pneumonia, suprimir a tosse pode até ser indesejável. Na esclerodermia, o risco cardíaco e de arritmia agrava a preocupação com um fármaco que prolonga o QT.

## Considerações de Segurança

- **Contraindicação segundo o grafo de conhecimento**: síndrome do QT longo (relação extraída do grafo de conhecimento do TxGNN, não do texto da bula).
- **Risco conhecido**: prolongamento do intervalo QT e bloqueio do canal hERG, motivo da retirada do mercado em 2007.
- **Interações medicamentosas**: não foram encontradas interações nos dados compilados para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é apenas computacional (L5), sem ensaios clínicos, sem literatura e sem mecanismo plausível. O fármaco não é comercializado no Brasil e tem um risco cardíaco grave que motivou sua retirada do mercado.

**Para prosseguir, é necessário:**
- Estabelecer uma hipótese mecanística plausível entre o clobutinol e a febre tifoide (por exemplo, atividade antibacteriana *in vitro* contra *Salmonella* Typhi)
- Obter dados de mecanismo de ação detalhados
- Obter as advertências e contraindicações da bula
- Avaliar a segurança cardíaca (QT/hERG) para qualquer uso proposto
- Confirmar a viabilidade regulatória, já que não há registro vigente no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

