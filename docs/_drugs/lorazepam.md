---
layout: default
title: Lorazepam
parent: Apenas Predição do Modelo (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lorazepam: nova indicação prevista, Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) (nível de evidência L5). Indicação original: Transtorno de ansiedade, estado de mal epiléptico…"
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm", "reading seizures", "thinking seizures", "orgasm-induced seizures", "startle epilepsy", "micturation-induced seizures", "audiogenic seizures", "eating seizures", "acute encephalopathy with biphasic seizures and late reduced diffusion"]
---

# Lorazepam
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

# Lorazepam: De ansiedade e epilepsia para neoplasia do nervo trigêmeo (previsão do modelo)

## Resumo em Uma Frase

Lorazepam é um benzodiazepínico originalmente usado no tratamento de transtornos de ansiedade e de quadros convulsivos, como o estado de mal epiléptico.
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)**, mas **não há nenhum ensaio clínico e nenhuma publicação** que apoiem essa direção específica.
Entre as demais previsões, a de **insônia** é a que tem mais respaldo na literatura (2 estudos clínicos antigos com lorazepam).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Transtorno de ansiedade, estado de mal epiléptico, síndrome de Lennox-Gastaut e epilepsia de ausência (conforme o grafo de conhecimento; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados; requer verificação) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o lorazepam é um modulador alostérico positivo do receptor GABA-A, que reforça a neurotransmissão inibitória e produz efeito ansiolítico, sedativo e anticonvulsivante.

Para a neoplasia do nervo trigêmeo, **não há vínculo mecanístico estabelecido**. A pontuação muito alta do TxGNN (99,87%) vem apenas de padrões no grafo de conhecimento. No máximo, o lorazepam poderia aliviar sintomas associados a um tumor, como ansiedade ou crises convulsivas, sem qualquer racional antineoplásico.

Portanto, esta previsão deve ser tratada como uma hipótese computacional, e não como uma oportunidade real de reposicionamento.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada à neoplasia do nervo trigêmeo.

### Outras previsões do modelo (para referência)

| Posição | Indicação prevista | Pontuação | Nível | Observação |
|------|------|------|------|------|
| 2 | Insônia | 99,80% | L3 | Mecanismo plausível (efeito sedativo-hipnótico). Dois estudos clínicos antigos e pequenos: [PMID 3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) (1988, lorazepam vs. flurazepam, cruzado duplo-cego, 8 pacientes; lorazepam melhor na maioria dos parâmetros de sono) e [PMID 10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) (1999, lorazepam 3 vezes ao dia na insônia crônica). Diretrizes atuais limitam benzodiazepínicos ao uso de curto prazo por dependência e tolerância. |
| 3 | Crises de leitura | 99,64% | L4 | Evidência indireta: série de 5 casos com lorazepam adjuvante em epilepsia fotossensível ([PMID 11593256](https://pubmed.ncbi.nlm.nih.gov/11593256/)). Sem dados específicos. |
| 4 | Crises de pensamento | 99,63% | L4 | Literatura geral sobre farmacologia e convulsões; nada específico. |
| 5 | Crises induzidas por orgasmo | 99,63% | L5 | Apenas previsão do modelo. |
| 6 | Epilepsia por sobressalto | 99,63% | L5 | Apenas previsão do modelo. |
| 7 | Crises induzidas por micção | 99,63% | L4 | Literatura sobre manejo geral de crises e estado de mal epiléptico, incluindo o ensaio RAMPART ([PMID 22335736](https://pubmed.ncbi.nlm.nih.gov/22335736/)), que trata de indicação já existente. |
| 8 | Crises audiogênicas | 99,63% | L4 | Apenas estudos pré-clínicos em ratos (abstinência de lorazepam). |
| 9 | Crises alimentares | 99,63% | L5 | Único artigo vinculado é irrelevante (ciamemazina e etanol em roedores). |
| 10 | Encefalopatia aguda com crises bifásicas e difusão reduzida tardia | 99,47% | L5 | Uso apenas sintomático; sem estudos. |

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não o texto da bula)**: insuficiência e doença hepática, encefalopatia/coma hepático, doença renal, doença da vesícula biliar, glaucoma de ângulo aberto e de ângulo fechado, apneia do sono e síndromes de hipoventilação, insuficiência respiratória, porfirias, e transtornos relacionados ao uso de substâncias ou dependência.
- **Interações Medicamentosas**: 100 interações registradas. Entre as principais:
  - **Graves**: morfina e morfina lipossomal (depressão respiratória e do sistema nervoso central).
  - **Moderadas**: bupropiona, dronabinol, nabilona, teduglutida, metoclopramida, ópio e sibutramina.
  - **Leves**: antiácidos como hidróxido de alumínio, carbonato de cálcio, óxido, hidróxido e carbonato de magnésio, e magaldrato.
- **Outro ponto**: a toxicidade por propilenoglicol é relevante na administração parenteral (infusão intravenosa) de lorazepam.
- Consulte a bula para informações complementares de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para a neoplasia do nervo trigêmeo, não há ensaios, literatura nem racional mecanístico antineoplásico; a pontuação alta é apenas uma predição do grafo (nível L5).
- As indicações convulsivas previstas são, em grande parte, extensões de usos já existentes, e a insônia (L3) tem apoio limitado a estudos antigos e pequenos, com restrições de segurança bem conhecidas.

**Para prosseguir, é necessário:**
- Confirmar a situação de comercialização no Brasil (dados indicam "não comercializado" e 0 registros, o que precisa ser verificado na ANVISA).
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois esses dados ainda estão ausentes.
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank).
- Se houver interesse em insônia, realizar revisão sistemática da literatura mais recente, ponderando risco de dependência, tolerância e interações.
- Para a neoplasia do nervo trigêmeo, só considerar avanço se surgir evidência pré-clínica ou clínica específica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

