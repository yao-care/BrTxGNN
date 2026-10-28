---
layout: default
title: Zinc Sulfate
parent: Evidência Moderada (L3-L4)
nav_order: 683
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-13
description: "Zinc Sulfate: nova indicação prevista, Faringite (Pharyngitis) (nível de evidência L3). Indicação original: Outros suplementos minerais, exceto de ferro e para reidratação"
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
---

# Zinc Sulfate
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **4** 
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

## Sulfato de Zinco: De suplemento mineral e descongestionante oftálmico para faringite
{: .text-alpha }

## Resumo em Uma Frase

O sulfato de zinco foi registrado no Brasil como suplemento mineral e como medicamento de ação oftálmica (descongestionante oftálmico).
O modelo TxGNN prevê que pode ser eficaz para **Faringite (Pharyngitis)**,
atualmente com **1 ensaio clínico** e **2 publicações** apoiando esta direção, ambos de relevância apenas indireta.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros suplementos minerais, exceto de ferro e para reidratação |
| Nova Indicação Prevista | Faringite (Pharyngitis) |
| Pontuação de Previsão TxGNN | 0,9985 |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 3) |
| Número de Registros | 3 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o sulfato de zinco é um sal mineral usado como suplemento e em colírios, e mecanisticamente pode ser aplicável a quadros de irritação da mucosa da garganta.

O zinco, quando liberado localmente (por exemplo, em pastilhas), pode reduzir a inflamação da mucosa, favorecer o reparo do epitélio e modular a resposta imune local, além de influenciar a função sensorial e o paladar. Esses efeitos são plausíveis para irritação e dor de garganta.

A ligação, porém, é indireta: o único ensaio clínico avaliou dor de garganta pós-operatória (relacionada à intubação), e não faringite infecciosa. Os registros brasileiros do fármaco (suplemento e uso oftálmico) também não têm relação direta com a nova indicação.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Não se aplica (NA) | Concluído | 87 | Estudo randomizado, duplo-cego e controlado por placebo sobre pastilhas orais de zinco no pré-operatório para reduzir a incidência de síndrome de dor de garganta pós-operatória. Desenho controlado, mas população pós-intubação, não faringite infecciosa. |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Suplementação de sulfato de zinco para aliviar mucosite oral e faringite induzidas por radiação em pacientes com câncer de cabeça e pescoço. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Relato/série de casos | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Recuperação de disgeusia prolongada pós-tonsilectomia; discute o possível papel da deficiência de zinco. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 117950003 (cancelado) | NESH ZINCO | Não informada | Outros suplementos minerais, exceto de ferro e para reidratação |
| Registro 103700113 (cancelado) | COLÍRIO TEUTO | Não informada | Outros medicamentos com ação no aparelho visual |
| Registro 102980488 (cancelado) | MAXIBELL | Não informada | Descongestionantes oftálmicos |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento TxGNN, não extraídas de bula)**: o grafo associa o fármaco a diversas condições, entre elas hipertensão, doença renal, doença hepática, diabetes mellitus e cetoacidose diabética, doenças cardiovasculares, hipercalcemia e nefrocalcinose, nefrolitíase, hipertireoidismo/doença de Graves e glaucoma de ângulo fechado. Trata-se de sinal computacional que exige verificação na bula.
- **Interações Medicamentosas**: foram identificadas 100 interações; entre as listadas, as de nível **moderado** incluem alendronato, risedronato, ibandronato (bisfosfonatos), tetraciclina e baloxavir marboxil. As demais listadas são de nível leve (por exemplo, corticoides como hidrocortisona, dexametasona, betametasona e triamcinolona, e imunobiológicos como abatacepte, adalimumabe e anakinra, além de azatioprina e baricitinibe).
- **Sinal de segurança específico da via nasal**: a literatura associa a irrigação intranasal de sulfato de zinco à toxicidade do epitélio olfatório (anosmia). Isso é relevante caso a via de administração seja ampliada para vias aéreas superiores.

As advertências e contraindicações da bula brasileira não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo (TxGNN, aprendizado profundo), mas as evidências são apenas indiretas (dor de garganta pós-operatória, mucosite por radiação), sem ensaio de Fase 2/3 em faringite infecciosa. Além disso, o medicamento está comercializado no Brasil, com 3 registros válidos de 3, mas faltam dados de bula e de mecanismo de ação, o que impede avançar na triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Obter dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar ensaio randomizado controlado em faringite aguda (infecciosa) com forma farmacêutica adequada (como pastilhas).
- Definir a via de administração e a forma farmacêutica viáveis e avaliar a compatibilidade com o status regulatório atual (registros cancelados).
- Avaliar os sinais de segurança do grafo de conhecimento e as interações de nível moderado antes de qualquer uso.

### Observação sobre as demais previsões

As outras indicações previstas têm suporte ainda mais fraco e não são recomendadas para avanço: **doença da cavidade nasal** (L5, Hold; literatura apenas pré-clínica e sinal de toxicidade olfatória), **laringofaringite aguda** (L4; única evidência trata de mucosite por radioquimioterapia) e **deficiência congênita de protrombina** (L5, Hold; sem justificativa mecanística nem evidência).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

