---
layout: default
title: Pirfenidone
parent: Apenas Predição do Modelo (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Pirfenidone: nova indicação prevista, Mastocitoma extracutâneo (extracutaneous mastocytoma) (nível de evidência L5). Indicação original: Outros produtos para o aparelho respiratório"
monitor_inn: "pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
---

# Pirfenidone
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

## Pirfenidona: Do tratamento respiratório ao mastocitoma extracutâneo (previsão do modelo)
{: .text-alpha }

## Resumo em Uma Frase

Pirfenidona é um agente antifibrótico e anti-inflamatório, registrado no Brasil na categoria "outros produtos para o aparelho respiratório".
O modelo TxGNN prevê que ela possa ser eficaz para **mastocitoma extracutâneo (extracutaneous mastocytoma)**, mas essa previsão tem **0 ensaios clínicos** e **0 publicações** que a apoiem diretamente.
A pontuação é alta (0,9971), mas trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para o aparelho respiratório |
| Nova Indicação Prevista | Mastocitoma extracutâneo (extracutaneous mastocytoma) |
| Pontuação de Previsão TxGNN | 0,9971 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 3) |
| Número de Registros | 3 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a pirfenidona modula a sinalização de TGF-β e de TNF-α, com atividade antifibrótica e anti-inflamatória, e é usada na fibrose pulmonar.

A relação com a nova indicação é fraca. Neoplasias de mastócitos são tipicamente impulsionadas por sinalização via KIT, e a pirfenidona não é conhecida por atuar sobre esse alvo. Não há vínculo mecanístico direto sustentado pelos dados disponíveis, e a similaridade com a indicação original não foi avaliada.

A pontuação elevada, portanto, deve ser lida como um sinal computacional que precisa de validação independente, não como indício de eficácia.

### Outras indicações previstas (todas com nível L5, salvo indicação)

| Posição | Indicação prevista | Pontuação | Observação |
|------|------|------|------|
| 2 | Dermatofibrossarcoma protuberans | 0,9941 | Vínculo teórico via fibroblastos e TGF-β; o tratamento padrão é a inibição de PDGFR (ex.: imatinibe) |
| 3 | Mastocitose sistêmica agressiva | 0,9933 | Doença impulsionada por mutações de KIT, alvo não conhecido da pirfenidona |
| 4 | Fibrossarcoma cardíaco | 0,9929 | Provável proximidade na ontologia de sarcomas/fibroblastos |
| 5 | Fibrossarcoma convencional | 0,9926 | Existe sinal de segurança na literatura (sarcoma após uso de pirfenidona) |
| 6 | Febre mediterrânea familiar autossômica recessiva | 0,9925 | Efeito anti-inflamatório pré-clínico (IL-1β, TNF-α, NLRP3) é teoricamente relevante, mas hipotético |
| 7 | Fibrossarcoma renal | 0,9924 | Sem evidências; reflete a similaridade da classe de fibrossarcomas |
| 8 | Infarto hepático | 0,9924 | Evento isquêmico agudo, sem papel terapêutico plausível |
| 9 | Neoplasia fibroblástica | 0,9923 | Única com literatura (nível L4), de direção mista |
| 10 | Sarcoma fibromixoide de baixo grau | 0,9919 | Sem evidências |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação principal prevista (nem para as demais indicações listadas).

## Evidências da Literatura

Não há literatura relacionada à indicação principal (mastocitoma extracutâneo). A única indicação prevista com publicações é a **neoplasia fibroblástica** (posição 9), cujas referências estão abaixo, como contexto indireto:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Estudo clínico piloto | Am J Gastroenterol | Projeto piloto avaliando a pirfenidona (antifibrótico oral não citotóxico) em tumores desmoides na polipose adenomatosa familiar |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Relato de caso | Perm J | Sarcoma pleomórfico indiferenciado após uso de pirfenidona; dados de efeitos de longo prazo são escassos |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Relato de caso | Rheumatology (Oxford) | Dermatofibromas eruptivos múltiplos agravados por micofenolato e pirfenidona em paciente com esclerose sistêmica |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | Estudo in vitro | BMC Musculoskelet Disord | Ação antifibrótica da pirfenidona em fibroblastos derivados da doença de Dupuytren |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | Estudo in vitro | BMC Musculoskelet Disord | Efeitos sobre vias não-SMAD estimuladas por TGF-β1 em fibroblastos de Dupuytren |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Pré-clínico/revisão | Pharm Dev Technol | Pirfenidona como antifibrótico injetável potencial para a doença de Dupuytren |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 122140114 (cancelado) | EGURINEL | Não informada | Não informada |
| Registro 101000663 (cancelado) | ESBRIET | Não informada | Outros produtos para o aparelho respiratório |
| Registro 100470649 (cancelado) | PIRFENIDONA | Não informada | Outros produtos para o aparelho respiratório |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 109 interações no total; as 20 listadas nos dados compilados são todas de gravidade moderada. As principais incluem: bupropiona, omeprazol, cimetidina, eliglustate, ácido obeticólico, oxandrolona, naltrexona, lansoprazol, miconazol, nitisinona, esomeprazol, fenilbutirato de glicerol, rolapitanto, deferasirox, ticlopidina, lumefantrina, dissulfiram, primaquina, tiabendazol e ivacaftor.
- **Sinal de segurança na literatura**: relatos de caso de sarcoma pleomórfico indiferenciado após uso de pirfenidona e de dermatofibromas agravados pelo fármaco. São evidências anedóticas, mas devem ser examinadas antes de qualquer exploração em indicações oncológicas.

Consulte a bula para as demais informações de segurança (advertências e contraindicações).

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta, mas é apenas computacional (L5), sem ensaios nem literatura, sem vínculo mecanístico com a doença impulsionada por KIT, e o fármaco não tem registro vigente no Brasil (apenas registros cancelados).

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação (por exemplo, via DrugBank).
- Obter e analisar a bula na ANVISA (advertências e contraindicações), uma lacuna que bloqueia a triagem de segurança.
- Investigar o sinal de segurança relacionado a sarcomas e dermatofibromas.
- Realizar estudos pré-clínicos que testem a hipótese em modelos de neoplasias de mastócitos.
- Confirmar a situação regulatória, já que o medicamento está comercializado no Brasil, com 3 registros válidos de 3.
- Considerar, como alternativa de pesquisa, a indicação "neoplasia fibroblástica" (L4), somente após a avaliação de segurança.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

