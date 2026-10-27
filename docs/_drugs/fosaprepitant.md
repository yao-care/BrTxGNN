---
layout: default
title: Fosaprepitant
parent: Apenas Predição do Modelo (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fosaprepitant: nova indicação prevista, Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrom… (nível de evidência L5). Indicação original: Antieméticos e antinauseantes"
monitor_inn: "fosaprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

## Fosaprepitant: De antiemético a síndrome nefrogênica de antidiurese inapropriada
{: .text-alpha }

## Resumo em Uma Frase

Fosaprepitant (fosaprepitanto dimeglumina) é um pró-fármaco do aprepitanto, originalmente registrado no Brasil como antiemético e antinauseante.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antieméticos e antinauseantes |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 8 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o fosaprepitant é um pró-fármaco do aprepitanto, um antagonista do receptor de neurocinina-1 (NK1), e sua eficácia como antiemético (por exemplo, na prevenção de náuseas e vômitos associados à quimioterapia) é reconhecida.

A relação entre a indicação original e a nova indicação é fraca. A síndrome nefrogênica de antidiurese inapropriada é um distúrbio do manejo renal da água, ligado à via da vasopressina. Uma conexão com o antagonismo NK1 é especulativa, e nenhum mecanismo de suporte foi estabelecido com os dados disponíveis.

A pontuação elevada do TxGNN (99,92%) reflete uma previsão computacional baseada em grafo de conhecimento e, isoladamente, não é suficiente para justificar o avanço desta indicação.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 106460228 | Fosaprepitanto dimeglumina | Não informada | Antieméticos e antinauseantes |
| Registro nº 106460229 | Enek | Não informada | Antieméticos e antinauseantes |
| Registro nº 151430042 | Fosaprepitanto dimeglumina | Não informada | Antieméticos e antinauseantes |
| Registro nº 155370078 | Fosaprepitanto dimeglumina | Não informada | Antieméticos e antinauseantes |
| Registro nº 165070030 | Fopitant | Não informada | Antieméticos e antinauseantes |

Observação: são 8 registros no total, todos com situação cancelada; a tabela mostra os 5 primeiros. Entre os demais estão Emend Injetável (101710225) e Foza (155370085).

---

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento TxGNN, não texto de bula)**: insuficiência hepática (liver failure).
- **Interações Medicamentosas**: foram identificadas 158 interações no total. Entre as principais:
  - **Graves (Major)**: eliglustate, naloxegol.
  - **Moderadas**: corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), claritromicina, cimetidina, miconazol, dronabinol, inibidores de bomba de prótons (rabeprazol, lansoprazol), pioglitazona, saxagliptina, glimepirida, nateglinida, alosetrona, naldemedina.

Consulte a bula para as demais informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão não tem nenhum ensaio clínico ou publicação de suporte e nenhum mecanismo plausível identificado (nível L5). Além disso, todos os registros brasileiros do fármaco estão cancelados, o que limita a viabilidade local.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação (MOA) e uma hipótese biológica que ligue o antagonismo NK1 à via da vasopressina/manejo renal de água
- Revisão sistemática da literatura e de bases de ensaios clínicos para a indicação prevista
- Bula da ANVISA (advertências e contraindicações), ainda não disponível
- Esclarecimento da situação regulatória (motivo dos cancelamentos) e da disponibilidade de via injetável no Brasil
- Plano de segurança considerando a insuficiência hepática e as interações medicamentosas graves

---

### Nota sobre outras indicações previstas

Entre as demais previsões do modelo, apenas **retinite** (L4) tem algum suporte: um estudo pré-clínico em camundongos (PMID 32058829, 2021, *Ocular Immunology and Inflammation*) indica que o fosaprepitant bloqueou a expressão do receptor NK1 induzida por radiação UVR-B em tecidos oculares. Trata-se de evidência indireta, sem estudos em pacientes com retinite, classificada como "questão de pesquisa". As outras previsões (pneumocistose, hanseníase, meningite criptocócica, neoplasia endócrina múltipla, abscesso intracraniano, malária por *P. falciparum*, equinococose e hiperargininemia) não têm evidência e permanecem em Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

