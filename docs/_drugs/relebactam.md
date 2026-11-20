---
layout: default
title: Relebactam
parent: Apenas Predição do Modelo (L5)
nav_order: 562
evidence_level: L5
indication_count: 3
monitor_inn: "Relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
last_modified_at: 2026-11-20
description: "Relebactam: nova indicação prevista, Hiperamilasemia (nível de evidência L5). Indicação original: Infecção do trato urinário e pielonefrite"
---

# Relebactam
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Relebactam: Da infecção do trato urinário à hiperamilasemia
{: .text-alpha }

## Resumo em Uma Frase

Relebactam é um inibidor de beta-lactamase, originalmente usado no tratamento de infecção do trato urinário e pielonefrite.
O modelo TxGNN prevê que pode ser eficaz para **Hiperamilasemia (Hyperamylasemia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção do trato urinário e pielonefrite (relação registrada no grafo de conhecimento; o texto de indicação do registro local está vazio) |
| Nova Indicação Prevista | Hiperamilasemia |
| Pontuação de Previsão TxGNN | 0,9922 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo o ChEMBL (EMBL-EBI), o mecanismo de ação registrado para Relebactam é (tradução não oficial): “Inibidor da beta-lactamase SHV-1; Inibidor da beta-lactamase bacteriana TEM; Inibidor de beta-lactamase; Inibidor da beta-lactamase hidrolisadora de carbapenêmicos KPC” Texto original em inglês: "Beta-lactamase SHV-1 inhibitor; Bacterial beta-lactamase TEM inhibitor; Beta-lactamase inhibitor; Carbapenem-hydrolyzing beta-lactamase KPC inhibitor" ([ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605), CC BY-SA 3.0; acessado em 2026-11-19). Segundo informações conhecidas, o relebactam é um inibidor de beta-lactamase (classe dos diazabiciclooctanos), usado em associação com imipenem/cilastatina para restaurar a atividade contra bactérias Gram-negativas resistentes.

Não foi identificado um vínculo mecanístico claro entre o relebactam e a hiperamilasemia. O fármaco não tem efeito conhecido sobre o metabolismo da amilase nem sobre a regulação de enzimas pancreáticas. Qualquer associação seria especulativa (por exemplo, via comprometimento pancreático ou salivar relacionado a infecções) e não é sustentada pelos dados disponíveis.

A pontuação alta (0,9922) é uma previsão do modelo TxGNN (aprendizado profundo) e, isoladamente, não constitui evidência biológica ou clínica. Outras previsões do modelo, como a síndrome de hiperviscosidade policlonal e a analbuminemia congênita, também não têm fundamento mecanístico plausível.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101710236 | RECARBRIO | Não informada | Não informada no registro |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

Não foram encontradas interações medicamentosas registradas nos dados compilados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura sobre relebactam em hiperamilasemia, e não existe vínculo mecanístico plausível. A previsão é apenas do modelo (nível L5).

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), hoje uma lacuna bloqueante para a triagem de segurança.
- Obter os dados de mecanismo de ação no DrugBank.
- Realizar busca sistemática de literatura e de registros de ensaios sobre relebactam e elevação de amilase (inclusive como possível evento adverso, e não como indicação).
- Gerar evidência pré-clínica ou mecanística antes de qualquer consideração de reposicionamento.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

