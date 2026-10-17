---
layout: default
title: Alpelisib
parent: Apenas Predição do Modelo (L5)
nav_order: 42
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Alpelisib: nova indicação prevista, Hipertensão Pulmonar (Pulmonary Hypertension) (nível de evidência L5). Indicação original: Agentes antineoplásicos"
monitor_inn: "alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

# Alpelisibe: De agente antineoplásico a hipertensão pulmonar

## Resumo em Uma Frase

Alpelisibe (comercializado como PIQRAY) foi originalmente registrado na ANVISA como agente antineoplásico.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação**, que é um relato de caso de evento adverso pulmonar (e não de benefício), associada a esta previsão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 99,03% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Sabe-se que o alpelisibe é um inibidor da PI3K alfa usado em oncologia, e sua indicação original é a de agente antineoplásico. A relação com a hipertensão pulmonar é, no momento, apenas uma previsão computacional.

Em teoria, a via PI3K/Akt/mTOR está implicada no remodelamento vascular pulmonar, em particular na proliferação das células musculares lisas das artérias pulmonares. Por isso, inibir a PI3K alfa poderia, em princípio, ser relevante para a doença. Trata-se, porém, de uma hipótese biológica, não de um mecanismo estabelecido pelos dados disponíveis.

É importante ter cautela: a única publicação encontrada descreve **doença pulmonar intersticial induzida por alpelisibe** em uma paciente com câncer de mama avançado. Isso é um sinal de dano pulmonar, não de eficácia em hipertensão pulmonar. A pontuação alta do TxGNN (0,990) não deve ser interpretada como suporte ao reposicionamento sem validação pré-clínica e clínica independente.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Relato de caso | J Oncol Pharm Pract | Doença pulmonar intersticial induzida por alpelisibe em paciente com câncer de mama avançado (evento adverso, não evidência de eficácia) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100681165 (cancelado) | PIQRAY | Não informada | Agentes antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor da PI3K alfa) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Evento pulmonar relevante**: a literatura recuperada descreve doença pulmonar intersticial associada ao alpelisibe, o que é particularmente preocupante para uma indicação pulmonar.
- **Interações Medicamentosas**: foram identificadas 284 interações no total. As listadas, todas de gravidade moderada, incluem antidiabéticos (acarbose, metformina, pioglitazona, glimepirida, glipizida, alogliptina, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, albiglutida, dulaglutida, exenatida, acetohexamida, clorpropamida), além de alosetrona, bupropiona, dexametasona, dronabinol e fidaxomicina. Esse padrão é compatível com possível interferência no controle glicêmico.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão baseia-se apenas no modelo (nível L5), sem ensaios clínicos, e a única publicação relatada aponta para toxicidade pulmonar, não para benefício. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança
- Complementar os dados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar estudos pré-clínicos em modelos de hipertensão pulmonar, avaliando o balanço entre efeito antiproliferativo vascular e toxicidade pulmonar (doença intersticial)
- Revisar a literatura de forma sistemática em busca de evidências de eficácia, não apenas de eventos adversos
- Esclarecer a situação regulatória atual do alpelisibe no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

