---
layout: default
title: Medroxyprogesterone Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 437
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Medroxyprogesterone Acetate: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L4). Indicação original: Progestágenos simples"
monitor_inn: "Medroxyprogesterone acetate"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "renal hypoplasia (disease)", "blunt duct adenosis of breast", "apocrine adenosis of breast"]
---

# Medroxyprogesterone Acetate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Acetato de Medroxiprogesterona: Da contracepção à Amenorreia (Amenorrhea)
{: .text-alpha }

## Resumo em Uma Frase

O acetato de medroxiprogesterona (MPA) é um progestágeno sintético, registrado no Brasil como progestágeno simples e anticoncepcional.
O modelo TxGNN prevê que pode ser eficaz para **amenorreia (amenorrhea)**,
atualmente sem ensaios clínicos registrados, mas com **20 publicações** recuperadas (em sua maioria revisões indiretas, sobre contracepção).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Progestágenos simples |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 1,0000 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 8 de 8) |
| Número de Registros | 8 (ativos: 8) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o MPA é um progestágeno sintético. Na amenorreia secundária com estrogênio endógeno adequado, o desafio com progestágeno induz sangramento por privação ao transformar o endométrio preparado pelo estrogênio. Trata-se de um uso clínico consolidado, e a justificativa biológica é forte.

Porém, a literatura recuperada trata principalmente do uso contraceptivo (incluindo a amenorreia como efeito colateral do Depo-Provera), e não do tratamento da amenorreia. A evidência é, portanto, indireta, e a pontuação elevada do TxGNN é parcialmente explicada pelo conhecido efeito do fármaco de causar amenorreia.

Outras previsões do modelo incluem doença fibrocística da mama (L3, com dois relatos clínicos antigos e pequenos sobre o MPA), displasia mamária benigna, endometriose em diferentes localizações e hipoplasia renal. Esta última não tem vínculo mecanístico plausível e parece ser um artefato do modelo. Este relatório foca na previsão de maior pontuação.

## Evidências da Literatura

Nenhum ensaio clínico está registrado para esta indicação. A literatura recuperada é composta majoritariamente por revisões (tier 3) sobre contracepção hormonal.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisão sistemática (Cochrane) | Cochrane Database Syst Rev | Contraceptivos injetáveis combinados são método reversível e altamente eficaz; aceitabilidade pode ser limitada por alterações no padrão de sangramento |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisão sistemática (Cochrane) | Cochrane Database Syst Rev | Versão anterior da revisão sobre injetáveis combinados |
| [8178904](https://pubmed.ncbi.nlm.nih.gov/8178904/) | 1994 | Revisão | Am J Obstet Gynecol | DMPA 150 mg IM a cada 3 meses, com eficácia contraceptiva superior a 99%; aprovado pela FDA em 1992 |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Revisão | J Reprod Med | Aconselhamento e manejo de efeitos colaterais do DMPA |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Revisão | Int J Fertil Menopausal Stud | Opções contraceptivas de longa duração, com taxas anuais de gravidez inferiores a 1 por 100 mulheres-ano |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Revisão | Int J Gynaecol Obstet | Contracepção pós-parto, considerando a amenorreia pós-parto e a lactação |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Revisão | Drug Intell Clin Pharm | Infertilidade induzida por fármacos |
| [1604074](https://pubmed.ncbi.nlm.nih.gov/1604074/) | 1992 | Revisão | Rev Med Liege | Contracepção hormonal |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Revisão | MCN Am J Matern Child Nurs | Depo-Provera |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Revisão | IARC Monogr | Avaliação do risco carcinogênico do acetato de medroxiprogesterona |

## Informações de Comercialização no Brasil

Todos os 8 registros estão válidos; o medicamento está comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104971189 | DEMEDROX | Não informada | Progestágenos simples |
| Registro 121100400 | PROVERA | Não informada | Progestágenos simples |
| Registro 105830220 | CONTRACEP | Não informada | Progestágenos simples |
| Registro 121100367 | DEPO-PROVERA | Não informada | Progestágenos simples |
| Registro 110360266 | CYCLOFEMINA | Não informada | Anticoncepcionais |

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): hipertensão, insuficiência e doença hepática, doença renal, epilepsia, asma, diabetes mellitus e cetoacidose diabética, osteoporose, lúpus eritematoso sistêmico, hipotireoidismo, doença da vesícula biliar, hipertrigliceridemia, hipercalcemia, transtornos de ansiedade, abuso de substâncias e **carcinoma de mama feminino**.
- **Interações medicamentosas** (100 registradas; nível moderado nos principais exemplos): antidiabéticos (acarbose, metformina, glimepiridina, clorpropamida, inibidores de SGLT2 como canagliflozina, dapagliflozina e empagliflozina, inibidores de DPP-4 como alogliptina e saxagliptina, agonistas de GLP-1 como semaglutida, liraglutida e dulaglutida, e insulinas), além de aprepitanto, dexametasona e claritromicina.
- Em relação à doença fibrocística, os dados apontam que o sinal de segurança mamária do MPA em terapia hormonal combinada exige cautela.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem forte plausibilidade biológica, mas a evidência é indireta (L4), sem ensaios clínicos, e o fármaco não possui registro vigente no Brasil. Além disso, o uso do MPA para induzir sangramento de privação em amenorreia secundária já é prática clínica estabelecida, o que limita o caráter de "reposicionamento" da previsão.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA (advertências e contraindicações), atualmente ausente
- Obter dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca de literatura específica sobre MPA no tratamento da amenorreia (primária e secundária), e não apenas sobre contracepção
- Confirmar a situação regulatória atual e a viabilidade de nova submissão, considerando que o medicamento está comercializado, com 8 registros válidos de 8
- Avaliar o perfil de segurança (mama, hepático, metabólico, ósseo) para a população-alvo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

