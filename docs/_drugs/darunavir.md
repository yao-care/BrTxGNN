---
layout: default
title: Darunavir
parent: Apenas Predição do Modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Darunavir: nova indicação prevista, Síndrome da imunodeficiência adquirida felina (feline acquired immuno… (nível de evidência L5). Indicação original: Infecção por HIV / AIDS"
monitor_inn: "DARUNAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Darunavir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Darunavir: Da infecção por HIV à imunodeficiência felina adquirida
{: .text-alpha }

## Resumo em Uma Frase

Darunavir é um inibidor de protease, originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que pode ser eficaz para **síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se de uma previsão exclusivamente do modelo, em indicação veterinária.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV / AIDS |
| Nova Indicação Prevista | Síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o darunavir faz parte da classe dos inibidores de protease do HIV, sua utilização em HIV/AIDS está estabelecida e, mecanisticamente, poderia ser aplicável a lentivírus relacionados.

O vírus da imunodeficiência felina (FIV) é um lentivírus aparentado ao HIV-1. No entanto, sua protease difere da protease do HIV-1 quanto à especificidade de substrato e à sensibilidade a inibidores. A atividade do darunavir contra a protease do FIV não está estabelecida. A pontuação muito alta do TxGNN (99,97%) baseia-se, portanto, apenas em inferência de similaridade entre doenças.

Trata-se de uma indicação veterinária, sem relevância direta para o reposicionamento de fármacos em humanos.

### Outras previsões do modelo (para contexto)

| Indicação prevista | Pontuação TxGNN | Nível | Comentário |
|------|------|------|------|
| Infecção pelo vírus da imunodeficiência símia (SIV) | 99,97% | L4 | Modelo animal do HIV; 4 estudos pré-clínicos em macacos, que avaliam esquemas de terapia antirretroviral combinada e não permitem confirmar a contribuição específica do darunavir. Sobrepõe-se à indicação já existente e agrega pouco valor de reposicionamento. |
| Transtorno do neurodesenvolvimento com marcha atáxica, ausência de fala e redução da substância branca cortical | 99,97% | L5 | Doença genética rara, sem vínculo mecanístico evidente com a inibição da protease do HIV; provável falso positivo. |
| Hiperlipidemia familiar combinada (termo obsoleto) | 99,19% | L5 | Inibidores de protease estão associados a dislipidemia, de modo que a associação pode refletir dano, e não benefício terapêutico. |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: insuficiência hepática, doença hepática, cirrose hepática, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, hepatite C (infecção crônica e geral), hepatite B crônica, hipertrigliceridemia, hemofilia (incluindo a forma sintomática em portadoras).
- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as 20 listadas, a maioria é de nível moderado, e uma é de nível **grave**:
  - **Grave**: cisaprida.
  - **Moderado (principais)**: antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, dapagliflozina, saxagliptina, clorpropamida, acetohexamida), corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), aprepitanto e claritromicina.

Consulte a bula para advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão de maior pontuação refere-se a uma doença veterinária (AIDS felina), sem ensaios clínicos nem literatura, e com atividade do darunavir contra a protease do FIV não demonstrada. As demais previsões são animais, sem vínculo mecanístico ou potencialmente direcionalmente enganosas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), uma lacuna bloqueante para a triagem de segurança; o fármaco não possui registro comercializado no Brasil.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Dados experimentais de atividade do darunavir contra a protease do FIV, caso haja interesse veterinário.
- Definir se há interesse em indicações humanas; as previsões atuais não oferecem candidato de reposicionamento humano com evidência.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

