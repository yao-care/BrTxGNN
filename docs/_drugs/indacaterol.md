---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

Usando o prompt de sistema de **Relatório de Avaliação de Reposicionamento de Fármacos (v5)** para gerar o relatório completo com base no Evidence Pack fornecido.

---

# Indacaterol: Do DPOC à Síndrome Nefrogênica de Antidiurese Inapropriada

## Resumo em Uma Frase

Indacaterol é um agonista β₂-adrenérgico de ação ultralonga (ultra-LABA), administrado por via inalatória e originalmente aprovado para o tratamento da Doença Pulmonar Obstrutiva Crônica (DPOC) e asma brônquica.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome Nefrogênica de Antidiurese Inapropriada (nephrogenic syndrome of inappropriate antidiuresis, NSIAD)**, com pontuação de predição de 99,54%.
Atualmente, **não há ensaios clínicos nem publicações científicas** que apoiem esta direção, e a racionalidade mecanística é considerada fraca.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | DPOC e Asma Brônquica (dados ANVISA não disponíveis; inferido a partir das evidências clínicas) |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (NSIAD) |
| Pontuação de Previsão TxGNN | 99,54% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 5 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Indacaterol é um ultra-LABA que atua por ligação de alta afinidade ao receptor β₂-adrenérgico (β₂-AR) nas células musculares lisas dos brônquios. Essa ligação ativa a via Gs/adenilato ciclase → cAMP/PKA, produzindo broncodilatação sustentada por até 24 horas com uma única inalação diária. Secundariamente, estabiliza mastócitos e reduz a liberação de mediadores inflamatórios. É importante notar que, entre as previsões do TxGNN para Indacaterol, a indicação de **doença brônquica (bronchial disease)** ocupa o 7º lugar em pontuação e é classificada como L1 — porém trata-se exatamente da **indicação original aprovada do fármaco**, confirmando a robustez do modelo, mas não configurando reposicionamento.

A NSIAD é uma condição rara causada por mutações com ganho de função no receptor AVPR2 (receptor V2 da vasopressina), que geram ativação constitutiva e persistente da via Gs/cAMP nas células dos túbulos coletores renais. O resultado é reabsorção de água independente de ADH, levando à hiponatremia e hiposmolalidade. A conexão hipotética com Indacaterol identificada pelo TxGNN reside na sobreposição de via de sinalização: β₂-AR e AVPR2 compartilham o mesmo eixo Gs/cAMP.

Contudo, a racionalidade mecanística é problemática por duas razões fundamentais. Primeiro, ativar adicionalmente o β₂-AR em células tubulares renais com cAMP já cronicamente elevado tenderia a agravar, e não a corrigir, o desequilíbrio hídrico subjacente. Segundo, Indacaterol é formulado exclusivamente como inalatório com exposição sistêmica muito baixa, tornando improvável que atinja concentrações renais farmacologicamente relevantes. Esta é uma previsão que ilustra um caso clássico de supergeneralização por parte do modelo: alta pontuação derivada de similaridade de via de sinalização, mas baixa plausibilidade clínica real.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para NSIAD com Indacaterol.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para NSIAD com Indacaterol.

---

## Informações de Comercialização no Brasil

Os dados individuais dos registros (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no Evidence Pack atual — todos os campos de licença retornaram vazios na consulta realizada em 2026-03-24.

| Situação | Detalhe |
|----------|---------|
| Registros ativos | 5 registros confirmados |
| Status de comercialização | ✓ Comercializado no Brasil |
| Dados individuais de registro | Não disponíveis — consulte o portal da ANVISA para detalhes |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para NSIAD apresenta pontuação altíssima (99,54%), mas a racionalidade mecanística é inversa ao esperado — ativar β₂-AR em uma condição de excesso de sinalização cAMP renal é potencialmente contraproducente — e a exposição sistêmica do fármaco inalatório é insuficiente para atingir o tecido-alvo renal em concentrações terapêuticas. Não existe nenhum dado clínico ou pré-clínico que sustente esta indicação.

> ⚠️ **Contexto importante:** Entre todas as 10 indicações previstas pelo TxGNN para Indacaterol neste Evidence Pack, **apenas "doença brônquica" (rank 7) atingiu nível de evidência L1** — porém essa indicação corresponde à aplicação clínica original do fármaco, não a um candidato de reposicionamento. As demais 9 indicações previstas, incluindo NSIAD, são todas L5/Hold, sugerindo que o TxGNN ainda não identificou candidatos de reposicionamento com suporte clínico para Indacaterol.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos em modelos de NSIAD para verificar se a modulação de β₂-AR exerce algum efeito sobre o transporte de água nas células do túbulo coletor renal
- Dados de farmacocinética renal para Indacaterol inalatório — ou investigação de formulações sistêmicas alternativas caso haja hipótese plausível
- Recuperação dos dados completos de registro ANVISA: número de registro, nome comercial, forma farmacêutica, indicação aprovada e advertências da bula (remediação dos gaps DG001 e DG002)
- Revisão bibliográfica dirigida sobre a expressão e função de β₂-AR na fisiologia tubular renal
- Reavaliação do Evidence Pack após coleta de dados de mecanismo de ação (DrugBank API — gap DG002)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

