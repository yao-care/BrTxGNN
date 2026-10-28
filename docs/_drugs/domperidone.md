---
layout: default
title: Domperidone
parent: Apenas Predição do Modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Domperidone: nova indicação prevista, Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrom… (nível de evidência L5). Indicação original: Antieméticos e antinauseantes"
monitor_inn: "DOMPERIDONE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Domperidone
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

## Domperidona: De antieméticos e antinauseantes à síndrome nefrogênica de antidiurese inapropriada
{: .text-alpha }

## Resumo em Uma Frase

Domperidona é um antiemético e antinauseante, utilizado originalmente no controle de náuseas e vômitos.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antieméticos e antinauseantes |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| Pontuação de Previsão TxGNN | 0,9908 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 19 de 19) |
| Número de Registros | 19 (ativos: 19) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo a farmacologia geral, a domperidona é um antagonista periférico dos receptores de dopamina D2 (e também D3, conforme os dados de farmacologia compilados), usado para dispepsia, azia, dor epigástrica, náuseas e vômitos.

A NSIAD é causada por mutações de ganho de função no receptor V2 da vasopressina (AVPR2), que provocam retenção de água e hiponatremia independentemente da vasopressina. Não há um mecanismo plausível pelo qual um antagonista D2 inibiria a sinalização constitutivamente ativa do receptor V2, que ocorre a jusante do receptor.

A pontuação vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas (por exemplo, hiponatremia, náuseas ou vias relacionadas à vasopressina), e não evidência biológica nem um vínculo farmacológico validado. Deve ser tratada apenas como sinal gerador de hipóteses.

## Informações de Comercialização no Brasil

Todos os 19 registros encontram-se válidos; abaixo, os 5 primeiros. A forma farmacêutica não consta nos dados compilados.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 167730457 | Dompgran | Não informada | Antieméticos e antinauseantes |
| Registro nº 105830824 | Motiridona | Não informada | Antieméticos e antinauseantes |
| Registro nº 105710187 | Perigite | Não informada | Antieméticos e antinauseantes |
| Registro nº 135690689 | Molidon | Não informada | Antieméticos e antinauseantes |
| Registro nº 155840633 | Domperidona | Não informada | Antieméticos e antinauseantes |

## Considerações de Segurança

- **Possíveis contraindicações (grafo de conhecimento, não texto de bula)**: síndrome do QT longo, síndrome do QT longo familiar, torsades de pointes, doença hepática e doença da vesícula biliar.
- **Alvos farmacológicos**: antagonismo dos receptores D2 (DRD2) e D3 (DRD3). Não foram identificadas interações medicamentosas propriamente ditas com outros fármacos nos dados compilados.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A única sustentação é a pontuação elevada do TxGNN (0.9908), sem ensaios clínicos nem literatura, e sem mecanismo plausível que ligue o antagonismo D2 à fisiopatologia da NSIAD (ganho de função do AVPR2). Além disso, os sinais de risco cardíaco (QT longo, torsades de pointes) reforçam a cautela.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna considerada bloqueante para a triagem de segurança
- Obter dados de mecanismo de ação (MOA) no DrugBank
- Realizar revisão de literatura e estudos pré-clínicos que testem um vínculo mecanístico com o AVPR2 ou a homeostase da água
- Esclarecer o motivo do cancelamento dos registros no Brasil e a viabilidade regulatória de uma nova indicação
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original (ainda pendentes)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

