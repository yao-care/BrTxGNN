---
layout: default
title: Ezetimibe
parent: Apenas Predição do Modelo (L5)
nav_order: 310
evidence_level: L5
indication_count: 1
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-31
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
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 34 de 64) |
| Número de Registros | 64 (ativos: 34) |
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

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100290076 | EZETROL | ORGANON FARMACÊUTICA LTDA. | Ativo |
| 100290135 | VYTORIN | ORGANON FARMACÊUTICA LTDA. | Ativo |
| 100290214 | ZETIA | ORGANON FARMACÊUTICA LTDA. | Ativo |
| 100290215 | ZETSIM | ORGANON FARMACÊUTICA LTDA. | Ativo |
| 100330210 | PLENANCE EZE | LIBBS FARMACÊUTICA LTDA | Ativo |
| 100470538 | EZETIMIBA | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 101460091 | SINVASCOR EZE | LABORATÓRIOS BALDACCI LTDA | Ativo |
| 102351132 | EZETIMIBA | EMS S/A | Ativo |
| 102351139 | EZETIMIBA + SINVASTATINA | EMS S/A | Ativo |
| 104540195 | NUSTENDI | DAIICHI SANKYO BRASIL FARMACÊUTICA LTDA | Ativo |
| 105250108 | ROSUCOR EZE | TORRENT DO BRASIL LTDA | Ativo |
| 105730018 | RUNNER EZE | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730139 | ROSUVASTATINA CÁLCICA + EZETIMIBA | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730719 | TREZETE | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105830814 | EZETIMIBA + SINVASTATINA | GERMED FARMACEUTICA LTDA | Ativo |
| 109170123 | EZETIMIBA | MEDQUIMICA INDUSTRIA FARMACEUTICA LTDA. | Ativo |
| 109740234 | POSICOR | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740235 | POSICOR SIN | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740296 | EZETIMIBA + SINVASTATINA | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740297 | EZETIMIBA | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 118190316 | EMIBAZET SINV | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 118190425 | SINZETAB | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 118190494 | EZETIMIBA | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 123520302 | EZETIMIBA + SINVASTATINA | RANBAXY FARMACÊUTICA LTDA | Ativo |
| 135170028 | EZETIMIBA | ALTHAIA S.A. INDUSTRIA FARMACEUTICA | Ativo |
| 135170030 | ZETERINA | ALTHAIA S.A. INDUSTRIA FARMACEUTICA | Ativo |
| 155840553 | EZETIMIBA | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Ativo |
| 155840647 | EZETIMIBA + SINVASTATINA | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Ativo |
| 156510106 | EZETIMIBA + SINVASTATINA | ZYDUS NIKKHO FARMACÊUTICA LTDA | Ativo |
| 167730407 | EZETIMIBA | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

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

