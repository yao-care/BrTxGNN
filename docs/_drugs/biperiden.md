---
layout: default
title: Biperiden
parent: Apenas Predição do Modelo (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Biperiden: nova indicação prevista, Encefalite Subaguda de Rasmussen (Rasmussen subacute encephalitis) (nível de evidência L5). Indicação original: Doença de Parkinson (e síndromes parkinsonianas rel…"
monitor_inn: "Biperiden"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "paralysis agitans, juvenile, of Hunt", "Lewy body dementia", "attention deficit-hyperactivity disorder", "X-linked intellectual disability-ataxia-apraxia syndrome"]
---

# Biperiden
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

## Biperideno: Da doença de Parkinson à encefalite de Rasmussen
{: .text-alpha }

## Resumo em Uma Frase

Biperideno é um anticolinérgico muscarínico (seletivo para M1), originalmente associado ao tratamento da doença de Parkinson e de síndromes parkinsonianas e distônicas relacionadas.
O modelo TxGNN prevê que pode ser eficaz para **Encefalite Subaguda de Rasmussen (Rasmussen subacute encephalitis)**, porém atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção, ou seja, trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Parkinson (e síndromes parkinsonianas relacionadas, segundo o grafo de conhecimento; não há texto de indicação aprovado no Brasil) |
| Nova Indicação Prevista | Encefalite Subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Biperideno é um anticolinérgico com seletividade pelo receptor muscarínico M1. Os dados compilados para este relatório não trazem uma descrição detalhada do mecanismo de ação; a informação acima vem do conhecimento farmacológico geral. Seu uso estabelecido está em condições com desequilíbrio colinérgico-dopaminérgico nos gânglios da base, como parkinsonismo e distonias.

A encefalite de Rasmussen é uma encefalite focal crônica, de natureza imunomediada, que causa crises epilépticas refratárias. A relação com a indicação original é distante: uma via plausível, mas não verificada, seria a modulação da sinalização colinérgica no córtex epileptogênico. Não há evidência clínica ou da literatura que sustente isso, e o alto escore do modelo pode refletir apenas proximidade na rede de conhecimento entre doenças neurológicas.

Outras previsões do modelo merecem nota: **síndrome de paralisia supranuclear progressiva-corticobasal** e **paralisia agitante juvenil de Hunt** têm plausibilidade biológica por compartilharem características motoras com as indicações originais (o uso seria apenas sintomático, e a segunda pode já estar coberta pela indicação de parkinsonismo). Já **demência com corpos de Lewy** tem direção de efeito desfavorável, pois anticolinérgicos tendem a piorar a cognição. Para **mielite**, **deficiência de transaldolase** e **deficiência de frutose-1,6-bisfosfatase**, não há racional mecanístico aparente.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (encefalite de Rasmussen).

Entre as indicações de menor ranking, apenas evidências indiretas foram encontradas (por exemplo, um estudo farmacológico com biperideno e rivastigmina em idosos saudáveis, relevante à demência com corpos de Lewy, e um relato de caso de biperideno no manejo de discinesia induzida por metilfenidato em TDAH). Nenhuma demonstra eficácia nessas novas indicações.

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não texto de bula)**: glaucoma de ângulo aberto e de ângulo fechado, hiperplasia prostática benigna, miastenia gravis, íleo paralítico, acalasia/megaesôfago, hérnia de hiato, colite ulcerativa e doença inflamatória intestinal, colite por *Clostridium difficile*, enterocolite necrosante perinatal, doença hepática, doença renal, doença da vesícula biliar, úlcera gástrica, doença pulmonar obstrutiva crônica, hipertensão, hipotensão, doença arterial coronariana, doenças de condução cardíaca e parada cardíaca súbita.
- **Interações Medicamentosas**: foram identificadas 75 interações no total. As de maior gravidade (**Major**) envolvem **cloreto de potássio** e **citrato de potássio**. Interações de gravidade moderada incluem outros anticolinérgicos (atropina, hioscina, diciclomina, glicopirrônio, propantelina, entre outros), opioides (morfina, ópio), loperamida, metoclopramida, dronabinol, nabilona, eluxadoline e pramlintida, principalmente por efeito anticolinérgico aditivo.

As advertências formais da bula brasileira não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para encefalite de Rasmussen tem escore alto, mas nenhuma evidência clínica ou da literatura (nível L5). Além disso, o biperideno não está registrado nem comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança.
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank).
- Realizar revisão de literatura e estudos pré-clínicos que avaliem o papel da sinalização colinérgica muscarínica na encefalite de Rasmussen.
- Considerar priorizar candidatas com maior plausibilidade biológica, como as síndromes parkinsonianas atípicas, com avaliação cuidadosa dos efeitos cognitivos adversos.
- Avaliar a viabilidade regulatória, já que o fármaco não possui registro no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

