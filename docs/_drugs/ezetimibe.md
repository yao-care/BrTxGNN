---
layout: default
title: Ezetimibe
parent: Apenas Predição do Modelo (L5)
nav_order: 310
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-29
description: "Ezetimibe: nova indicação prevista, Deficiência da proteína de transferência de ésteres de colesterol (nível de evidência L5). Indicação original: Antilipêmicos"
---

# Ezetimibe
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

## Ezetimiba: De antilipêmico para deficiência da proteína de transferência de ésteres de colesterol
{: .text-alpha }

## Resumo em Uma Frase

Ezetimiba é um medicamento registrado na ANVISA como antilipêmico, usado para reduzir o colesterol.
O modelo TxGNN prevê que pode ser eficaz para **deficiência da proteína de transferência de ésteres de colesterol (cholesterol-ester transfer protein deficiency)**, mas não há **nenhum ensaio clínico** e há apenas **2 publicações** indiretas (uma revisão geral sobre alvos de redução lipídica e um estudo em modelo animal), sem estudo que avalie diretamente esta doença.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Deficiência da proteína de transferência de ésteres de colesterol |
| Pontuação de Previsão TxGNN | 0,9909 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 16) |
| Número de Registros | Pelo menos 20 registros (a lista pode estar incompleta) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo conhecimento geral, a ezetimiba inibe a absorção intestinal de colesterol por meio da proteína NPC1L1, reduzindo o LDL-colesterol. Sua eficácia como antilipêmico consta nos registros da ANVISA.

A deficiência de CETP é uma condição genética caracterizada por HDL-colesterol elevado e metabolismo lipoproteico alterado. Existe um vínculo plausível por vias comuns do metabolismo lipídico, mas não há mecanismo direto nem justificativa clínica que mostre que a ezetimiba trate essa condição. Além disso, a deficiência de CETP costuma ser um fenótipo lipídico benigno ou até favorável, e não é reconhecida como condição que exija terapia de redução de LDL.

A pontuação alta do TxGNN (0,9909) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica ou clínica. A relação entre o fármaco e esta doença é, portanto, uma previsão computacional, não uma indicação aprovada.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revisão | European Heart Journal | Panorama dos alvos de terapias hipolipemiantes (LDL-C, triglicerídeos, apoB, Lp(a)); não trata diretamente da deficiência de CETP |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Estudo animal | Int J Mol Sci | Hamster com Ldlr heterozigoto como modelo para testar anticorpo anti-PCSK9 em hiperlipidemia e aterosclerose; menciona CETP apenas como característica do modelo |

## Informações de Comercialização no Brasil

Lista parcial (pelo menos 20 registros; abaixo, os 5 principais):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 103700686 | EZETIMIBA | Não informada | Antilipêmicos |
| Registro nº 103700687 | TEUMIB | Não informada | Antilipêmicos |
| Registro nº 100290076 | EZETROL | Não informada | Antilipêmicos |
| Registro nº 100290214 | ZETIA | Não informada | Antilipêmicos |
| Registro nº 135170030 | ZETERINA | Não informada | Antilipêmicos |

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (relações do grafo, não texto de bula): pancreatite, doença hepática, doença da vesícula biliar, miopatia, doença muscular, doença do músculo esquelético, paralisia periódica familiar, abuso/dependência de substâncias, rabdomiólise e fasciíte nodular.
- **Interações medicamentosas** (100 interações identificadas; principais de gravidade moderada): ácido quenodesoxicólico, eluxadolina, rosuvastatina e sinvastatina. Outras interações listadas têm gravidade não classificada (por exemplo, metformina, omeprazol, morfina, vancomicina).

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaio clínico nem estudo que avalie diretamente a deficiência de CETP com ezetimiba. A previsão vem apenas do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. A própria doença não costuma exigir tratamento redutor de LDL. O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Justificativa clínica de que a deficiência de CETP constitui uma necessidade terapêutica não atendida
- Dados do mecanismo de ação e análise mecanística específica para esta doença
- Estudos pré-clínicos ou observacionais que avaliem diretamente a ezetimiba nesta condição
- Advertências e contraindicações extraídas das bulas da ANVISA, ainda não disponíveis nos dados compilados
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

