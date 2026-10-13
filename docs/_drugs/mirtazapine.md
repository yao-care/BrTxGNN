---
layout: default
title: Mirtazapine
parent: Apenas Predição do Modelo (L5)
nav_order: 462
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Mirtazapina: De antidepressivo à síndrome de Ohdo (previsão sem evidências clínicas)

## Resumo em Uma Frase

Mirtazapina é um antidepressivo, registrado na ANVISA na classe dos "antidepressivos".
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Ohdo e variantes (Ohdo syndrome and variants)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidepressivos |
| Nova Indicação Prevista | Síndrome de Ohdo e variantes (Ohdo syndrome and variants) |
| Pontuação de Previsão TxGNN | 99,42% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a mirtazapina é um antidepressivo noradrenérgico e serotoninérgico específico, com antagonismo de receptores alfa-2 adrenérgicos, 5-HT2/5-HT3 e H1.

A síndrome de Ohdo (incluindo as variantes relacionadas ao gene KAT6B) é um transtorno genético raro da regulação da cromatina, com deficiência intelectual e alterações craniofaciais e do desenvolvimento. Não há via mecanística plausível que ligue a mirtazapina à patologia epigenética de base.

A pontuação elevada do TxGNN provavelmente reflete vizinhança no grafo de conhecimento (por exemplo, anotações compartilhadas de fenótipos neuropsiquiátricos ou do neurodesenvolvimento), e não um mecanismo biológico causal. Qualquer benefício seria, no máximo, sintomático (como sono ou humor) e exigiria justificativa própria.

Outras previsões do modelo seguem a mesma lógica:
- **Blefarofimose – deficiência intelectual, tipo Ohdo** (pontuação 99,11%): essencialmente a mesma entidade da previsão principal, portanto não constitui um sinal independente.
- **Torcicolo paroxístico benigno da infância** (pontuação 99,11%): condição autolimitada, ligada a variantes de CACNA1A e a equivalentes de enxaqueca. Uma ligação especulativa seria a modulação serotoninérgica/anti-histamínica, mas não há evidência direta, a doença costuma regredir espontaneamente e a segurança da mirtazapina em lactentes não está estabelecida.

## Informações de Comercialização no Brasil

Todos os 20 registros encontrados são de medicamentos de componente único e estão **cancelados**; não há registro válido atualmente. Exibem-se os 5 primeiros.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| 103700791 | Mirtazapina | Não informada | Antidepressivos |
| 100470464 | Razapina | Não informada | Antidepressivos |
| 103700765 | Mirtazapina | Não informada | Antidepressivos |
| 105830944 | Mirtazapina | Não informada | Antidepressivos |
| 100290224 | Remeron | Não informada | Antidepressivos |

Entre os demais registros cancelados constam também as marcas Myzapy, Myrtz ODT e Menelat.

## Considerações de Segurança

- **Contraindicações e condições de risco (grafo de conhecimento, não texto de bula)**: o grafo de conhecimento do TxGNN associa a mirtazapina a condições como epilepsia, transtorno bipolar em fase maníaca, doença hepática, doença da vesícula biliar, neutropenia, agranulocitose, hipotensão e hipotensão ortostática, hipertrigliceridemia, obesidade, acidente vascular cerebral e doenças cerebrovasculares, infarto do miocárdio e trombose coronariana, hemoglobinopatias, insuficiência renal, síndrome serotoninérgica e acatisia induzida por fármacos. Esses itens exigem confirmação na bula.
- **Interações Medicamentosas**: foram identificadas 100 interações; as 20 primeiras listadas incluem 5 de gravidade **maior** e as demais moderadas.
  - Maior: bupropiona, lorcasserina, dolasetrona, palonosetrona.
  - Moderada (exemplos): famotidina, loperamida, aprepitanto, morfina, dexametasona, cimetidina, claritromicina, levofloxacino, dronabinol, nabilona, eliglustate, ácido obeticólico.
  - Também constam laxantes e preparos intestinais (bisacodil, ácido picossulfúrico, polietilenoglicol, sulfato de sódio).

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura, e sem plausibilidade mecanística. Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação da mirtazapina (DrugBank) e análise de sua ligação com a biologia da síndrome de Ohdo
- Advertências e contraindicações da bula na ANVISA, para a triagem de segurança
- Revisão sistemática da literatura e de registros de ensaios, incluindo evidências pré-clínicas
- Justificativa clínica para um possível uso sintomático (sono ou humor), com avaliação de segurança em crianças
- Verificação da situação regulatória, dado que não há registro válido no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

