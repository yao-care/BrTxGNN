---
layout: default
title: Bortezomibe
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 0
---

# Bortezomibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# BORTEZOMIBE: Avaliação Preliminar para Reposicionamento

## Resumo em Uma Frase

Bortezomibe é um inibidor de proteassoma amplamente utilizado no tratamento do mieloma múltiplo e do linfoma de células do manto. Até o momento, o modelo TxGNN **não gerou previsões de novas indicações** para este fármaco. O presente relatório constitui uma avaliação preliminar, pendente de complementação de dados essenciais (mecanismo de ação, indicações aprovadas, informações de segurança) para que o pipeline de reposicionamento possa ser executado.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Mieloma múltiplo / Linfoma de células do manto *(dado não disponível no pack — inferido do conhecimento farmacológico)* |
| Nova Indicação Prevista | **Nenhuma previsão disponível** |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | **L5** (dados insuficientes para avaliação) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, **não há previsão de nova indicação gerada pelo TxGNN** para o bortezomibe. O pipeline de reposicionamento ainda não foi executado ou não identificou candidatos com pontuação suficiente.

No entanto, do ponto de vista farmacológico, o bortezomibe possui um mecanismo de ação bem caracterizado: é um **inibidor reversível do proteassoma 26S**, que bloqueia a degradação de proteínas reguladoras do ciclo celular e da apoptose. Esse mecanismo — centrado na inibição da via NF-κB e no acúmulo de proteínas pró-apoptóticas — tem sido investigado em contextos além da oncologia hematológica, incluindo doenças autoimunes (como lúpus e rejeição de transplante mediada por anticorpos).

Para que o modelo TxGNN possa gerar previsões confiáveis, é necessário primeiro completar o mapeamento DrugBank (DrugBank ID: **DB00188**) e assegurar que o fármaco esteja corretamente vinculado ao grafo de conhecimento. A ausência de dados de MOA e de indicações aprovadas no Evidence Pack atual impede a análise de correlação mecanística.

---

## Evidências de Ensaios Clínicos

Atualmente não há previsão de nova indicação, portanto não foram coletadas evidências de ensaios clínicos direcionados ao reposicionamento.

---

## Evidências da Literatura

Atualmente não há previsão de nova indicação, portanto não foram coletadas evidências da literatura direcionadas ao reposicionamento.

---

## Informações de Comercialização no Brasil

O bortezomibe possui **20 registros** com status "Comercializado". No entanto, os detalhes dos registros (número, nome comercial, forma farmacêutica e indicação aprovada) **não foram preenchidos no Evidence Pack atual**.

> ⚠️ É necessário complementar os dados de registro junto à ANVISA para completar esta seção.

---

## Citotoxicidade

O bortezomibe é um fármaco **antineoplásico** classificado como inibidor de proteassoma. Esta seção é aplicável.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | **Terapia-alvo** (inibidor de proteassoma 26S — não é citotóxico convencional) |
| Risco de Mielossupressão | **Alto** (trombocitopenia é muito frequente, neutropenia frequente; trombocitopenia cíclica é característica do bortezomibe) |
| Classificação de Emetogenicidade | **Baixa a média** |
| Itens de Monitoramento | CBC com diferencial (especial atenção a plaquetas), função hepática e renal, glicemia, eletrólitos, avaliação neurológica periférica periódica |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de citotóxicos (uso de EPI adequado: luvas, avental, proteção ocular durante preparo) |

> **Nota adicional:** A neuropatia periférica é um efeito adverso dose-limitante do bortezomibe e deve ser monitorada em cada ciclo de tratamento.

---

## Considerações de Segurança

Os dados de segurança (advertências, contraindicações e interações medicamentosas) **não estão disponíveis** no Evidence Pack atual.

> Consulte a bula para informações de segurança. Recomenda-se buscar os dados junto ao DrugBank (DB00188) e à bula aprovada pela ANVISA.

**Informações de segurança conhecidas do bortezomibe (referência geral):**
- **Advertências Principais**: Trombocitopenia, neuropatia periférica, hipotensão ortostática, insuficiência cardíaca, toxicidade pulmonar, síndrome de lise tumoral, reativação de herpes zoster
- **Contraindicações**: Hipersensibilidade ao bortezomibe, boro ou manitol; contraindicado administração intratecal
- **Interações Medicamentosas relevantes**: Inibidores/indutores de CYP3A4, hipoglicemiantes orais (risco de hipo/hiperglicemia), uso concomitante com outros agentes neurotóxicos

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack apresenta lacunas críticas que impedem a avaliação de reposicionamento: (1) não há previsão de nova indicação pelo TxGNN, (2) o mapeamento DrugBank está ausente, (3) os dados de registro, indicações aprovadas e segurança estão incompletos. Sem esses dados fundamentais, não é possível avançar no pipeline de avaliação.

**Para prosseguir, é necessário:**
- Completar o mapeamento DrugBank (ID provável: **DB00188**) e vincular o fármaco ao grafo de conhecimento do TxGNN
- Executar o pipeline de previsão TxGNN (KG + DL) com o DrugBank ID correto
- Preencher os dados de registro ANVISA (nome comercial, forma farmacêutica, indicação aprovada) para os 20 registros identificados
- Obter dados de segurança: advertências, contraindicações e interações medicamentosas a partir da bula aprovada
- Obter e registrar o mecanismo de ação (MOA) detalhado via DrugBank API
- Após completar os dados acima, reexecutar a geração do Evidence Pack e reavaliação
---

