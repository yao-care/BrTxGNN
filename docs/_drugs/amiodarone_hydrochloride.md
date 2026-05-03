---
layout: default
title: Amiodarone Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 0
---

# Amiodarone Hydrochloride
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

# Cloridrato de Amiodarona: Avaliação de Reposicionamento Inconclusiva — Sem Previsões TxGNN Disponíveis

---

## Resumo

O Cloridrato de Amiodarona é um antiarrítmico da Classe III amplamente consolidado na prática clínica, reconhecido pelo tratamento de arritmias ventriculares e supraventriculares graves refratárias. Neste ciclo de execução, **o modelo TxGNN não gerou nenhuma previsão de nova indicação** para este fármaco, inviabilizando a análise de reposicionamento. A ausência do `drugbank_id` no Evidence Pack é o provável fator limitante, pois impede o mapeamento correto do fármaco no grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsão de modelo disponível) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Esta seção não se aplica ao presente ciclo, pois **nenhuma nova indicação foi prevista pelo modelo TxGNN**.

Como contexto, o Cloridrato de Amiodarona atua principalmente por bloqueio de canais de potássio (efeito Classe III), com bloqueio adicional de canais de sódio, cálcio e atividade betabloqueadora não competitiva. Esse perfil multicanal confere ampla atividade antiarrítmica, mas também é responsável por seu extenso perfil de efeitos adversos (toxicidade tireoidiana, pulmonar, hepática e ocular).

A ausência de previsões neste ciclo provavelmente decorre da falta do `drugbank_id` no Evidence Pack, que é o identificador utilizado pelo pipeline TxGNN para localizar o nó do fármaco no grafo de conhecimento e calcular pontuações de reposicionamento. Sem esse vínculo, o modelo não consegue processar o candidato.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Nenhuma previsão de reposicionamento foi gerada pelo TxGNN neste ciclo. A ausência de `drugbank_id`, de indicações originais cadastradas e de dados de MOA impede a execução do pipeline de análise de forma completa.

**Para prosseguir, é necessário:**
- **Mapear o DrugBank ID**: O ID canônico da amiodarona no DrugBank é `DB01118` — incluí-lo no Evidence Pack e re-executar o pipeline TxGNN
- **Recuperar MOA estruturado**: Consultar a API do DrugBank com `DB01118` para obter mecanismo de ação, categorias farmacológicas e alvos moleculares
- **Obter dados regulatórios brasileiros**: Verificar registros na ANVISA (o fármaco é amplamente comercializado no Brasil sob nomes como Ancoron® e Atlansil®, mas não constou na consulta TFDA)
- **Baixar e analisar a bula (PDF)**: Para recuperar advertências, contraindicações e interações medicamentosas relevantes, especialmente dado o perfil de toxicidade conhecido da amiodarona
- **Re-executar o pipeline completo** após sanadas as lacunas acima (DG001 e DG002 identificadas no `meta.data_gaps`)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

