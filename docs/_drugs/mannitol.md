---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Mannitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Usando `txgnn-pipeline` para orientar o formato e rigor da análise de reposicionamento.

---

# Mannitol: De Diurético Osmótico à Síndrome Nefrogênica de Antidiurese Inapropriada

## Resumo em Uma Frase

Mannitol é um álcool de açúcar hexahídrico com uso clínico estabelecido como diurético osmótico — principalmente para redução da pressão intracraniana, edema cerebral agudo e promoção de diurese forçada em situações críticas.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis — NSIAD)**, atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.
A força das evidências é limitada e a previsão apresenta preocupações mecanísticas relevantes que exigem cautela antes de qualquer avanço clínico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado na ANVISA — uso clínico estabelecido como diurético osmótico (hipertensão intracraniana, edema cerebral) |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (NSIAD) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (base ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação disponíveis na base de dados. Segundo informações conhecidas, Mannitol é um açúcar osmoticamente ativo que, ao elevar a osmolaridade do plasma, promove o deslocamento de água livre dos compartimentos intracelular e intersticial para o intravascular, seguido de excreção renal aumentada. Esse mecanismo é a base do seu uso consolidado em condições de sobrecarga hídrica e elevação da pressão intracraniana — sem que haja reabsorção tubular significativa do próprio Mannitol.

A NSIAD é causada por mutações com ganho de função no receptor AVPR2 (receptor V2 da vasopressina), levando à ativação constitutiva independente de arginina-vasopressina. O resultado é retenção persistente de água livre e hiponatremia dilucional grave. Em tese, um agente osmótico como o Mannitol poderia promover a excreção de água livre e aliviar a hiponatremia, criando uma plausibilidade mecanística superficial que justifica o alto escore do TxGNN.

No entanto, a aplicação clínica de Mannitol em hiponatremia é um procedimento de alto risco fora de indicação aprovada. A expansão volêmica aguda provocada pelo Mannitol pode precipitar edema pulmonar em pacientes já com hiponatremia grave — risco documentado na literatura (PMID 981097). O único estudo identificado para esta indicação (PMID 26706473) é uma revisão educacional sobre armadilhas diagnósticas na avaliação de hiponatremia, citando o Mannitol apenas no contexto do **gap osmolar** como causa de interferência diagnóstica, e **não** como agente terapêutico para NSIAD. O tratamento padrão para NSIAD é a restrição hídrica e antagonistas do receptor V2 (vaptans). A previsão do TxGNN deve ser interpretada com cautela diante dessas contradições mecanísticas.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Educational Review / Expert Opinion | European Journal of Internal Medicine | Descreve as 10 principais armadilhas na avaliação de pacientes com hiponatremia; Mannitol é mencionado no contexto do gap osmolar como causa de confusão diagnóstica — **não** como tratamento para NSIAD |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis são insuficientes para apoiar o reposicionamento de Mannitol para NSIAD: há zero ensaios clínicos, apenas uma publicação de revisão educacional sem caráter terapêutico direto, e preocupações mecanísticas concretas — o uso de diurético osmótico em pacientes com hiponatremia grave pode ser contraproducente e clinicamente perigoso (risco de edema pulmonar por expansão volêmica). A previsão do TxGNN provavelmente reflete uma proximidade de grafo entre "diuréticos" e "distúrbios de sódio", sem respaldo clínico real.

**Para prosseguir, seria necessário:**
- Obter dados de mecanismo de ação (MOA) do Mannitol via DrugBank API para análise de relevância mecanística completa
- Revisão sistemática de casos clínicos onde Mannitol foi utilizado em contexto de hiponatremia grave, com avaliação de desfechos
- Avaliação de segurança específica para uso em NSIAD, incluindo risco de edema pulmonar, expansão volêmica e sobrecarga cardíaca
- Consulta a especialistas em nefrologia e endocrinologia para avaliação de viabilidade clínica
- Verificar e atualizar o status regulatório do Mannitol junto à ANVISA, pois a ausência de registros na base de dados pode refletir lacuna de dados e não ausência real de comercialização no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

