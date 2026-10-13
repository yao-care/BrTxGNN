---
layout: default
title: Felodipine
parent: Apenas Predição do Modelo (L5)
nav_order: 312
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

# Felodipino: Da hipertensão arterial à hipertensão pulmonar (previsão do modelo)

## Resumo em Uma Frase

Felodipino é um bloqueador dos canais de cálcio do tipo di-hidropiridínico, originalmente registrado no Brasil como anti-hipertensivo (associações medicamentosas).
O modelo TxGNN prevê que ele pode ser eficaz para **hipertensão pulmonar de mecanismo multifatorial incerto (pulmonary hypertension with unclear multifactorial mechanism)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta previsão específica.

> Observação: entre as previsões listadas, as que contam com alguma literatura são a **cor pulmonale crônico** (3 publicações) e a **angina de Prinzmetal** (7 publicações). Elas são discutidas ao longo do relatório como alternativas mais bem fundamentadas.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-hipertensivos – associações medicamentosas |
| Nova Indicação Prevista | Hipertensão pulmonar de mecanismo multifatorial incerto (pulmonary hypertension with unclear multifactorial mechanism) |
| Pontuação de Previsão TxGNN | 99,91% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o felodipino é um bloqueador dos canais de cálcio do tipo L, de seletividade vascular, que relaxa a musculatura lisa dos vasos e provoca vasodilatação. Sua eficácia como anti-hipertensivo é bem estabelecida, e mecanisticamente a vasodilatação poderia ser aplicável à circulação pulmonar.

A relação entre a indicação original e a nova é a redução da resistência vascular. Contudo, a previsão deve ser vista com cautela: os bloqueadores de cálcio só beneficiam um pequeno subgrupo de pacientes com hipertensão arterial pulmonar vasorreativa, e não doenças de mecanismo multifatorial ou incerto. Nesse caso, a pontuação elevada (0,999) é apenas uma previsão computacional.

Outras previsões do modelo seguem o mesmo padrão. Na hipertensão pulmonar por doença pulmonar ou hipoxia, a vasodilatação pode piorar a relação ventilação-perfusão e as trocas gasosas. Na hipertensão renovascular maligna e na doença renal hipertensiva maligna, a previsão é em grande parte uma extensão da indicação anti-hipertensiva já conhecida. Para a síndrome de Braddock, não há racional mecanístico evidente.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (hipertensão pulmonar de mecanismo incerto), atualmente não há literatura relacionada. Abaixo, a literatura disponível para as previsões de menor pontuação, porém com algum suporte:

**Cor pulmonale crônico (pontuação TxGNN 99,19%; nível L4)**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2838319](https://pubmed.ncbi.nlm.nih.gov/2838319/) | 1988 | Estudo hemodinâmico | Eur Respir J | Em 11 pacientes com DPOC grave, a infusão de felodipino reduziu a resistência vascular pulmonar (18%) e sistêmica (33%) e aumentou o débito cardíaco (33%) e as frações de ejeção ventriculares |
| [2487551](https://pubmed.ncbi.nlm.nih.gov/2487551/) | 1989 | Estudo hemodinâmico agudo | Cardiovasc Drugs Ther | Efeitos agudos do felodipino na hemodinâmica central e no fluxo sanguíneo regional em 10 pacientes com insuficiência cardíaca congestiva grave |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Revisão | Cardiovasc Drugs Ther | Uso e eficácia comparativa dos bloqueadores de cálcio na hipertensão e arritmias supraventriculares |

**Angina de Prinzmetal (pontuação TxGNN 99,07%; nível L4)**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7744087](https://pubmed.ncbi.nlm.nih.gov/7744087/) | 1995 | Duplo-cego, randomizado, cruzado (angina estável) | Eur Heart J | Felodipino ER 10 mg e nifedipino SR melhoraram a duração do exercício (66 s e 50 s) em 43 pacientes |
| [1746458](https://pubmed.ncbi.nlm.nih.gov/1746458/) | 1991 | Estudo clínico comparativo | Am J Cardiol | Felodipino 1x/dia comparado a nifedipino 4x/dia em 30 pacientes com angina de Prinzmetal, com monitorização Holter de 24 h |
| [8013514](https://pubmed.ncbi.nlm.nih.gov/8013514/) | 1994 | Estudo clínico | Eur Heart J | Felodipino ER 20 mg/dia em 14 pacientes com angina variante, avaliando a prevenção de isquemia induzida por ergonovina |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Estudo clínico | Am J Cardiol | Efeito do felodipino em crises isquêmicas induzidas por hiperventilação na angina variante (sem resumo disponível) |
| [7728649](https://pubmed.ncbi.nlm.nih.gov/7728649/) | 1995 | Revisão | Can J Cardiol | Os bloqueadores de cálcio são fármacos de primeira escolha na angina de Prinzmetal, devido à ação antivasoespástica |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Revisão | Herz | Terapia diferenciada com antagonistas de cálcio |

Um relato de caso (PMID 15222138, angina de Prinzmetal induzida por nicergolina) não trata do felodipino e foi desconsiderado.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116180241 (cancelado) | SELOZOK FIX | Não informada | Anti-hipertensivos – associações medicamentosas |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: o grafo de conhecimento do TxGNN (PrimeKG) associa o fármaco a relações de contraindicação com, entre outras, doença renal, doença hepática, doença da vesícula biliar, angioedema (inclusive hereditário), neutropenia e agranulocitose, estenose aórtica, estados hipotensivos, cardiomiopatia hipertrófica, infarto do miocárdio, doença arterial coronariana e aterosclerose.
- **Interações medicamentosas**: foram identificadas 246 interações. Entre as listadas, a única de gravidade **maior** é com **dolasetrona**. As de gravidade **moderada** incluem corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), bupropiona, aprepitanto, morfina, ácido acetilsalicílico, cimetidina, claritromicina, inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), sulfato de magnésio, dronabinol, nabilona e sais de cálcio.

Para advertências e contraindicações da bula, consulte a bula aprovada, pois esses dados não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (hipertensão pulmonar de mecanismo incerto) tem apenas suporte computacional (L5), sem ensaios ou publicações, e há ressalvas fisiopatológicas (benefício limitado dos bloqueadores de cálcio fora do subgrupo vasorreativo; risco na hipoxia). Além disso, o único registro brasileiro está cancelado.
- As melhores evidências são para a angina de Prinzmetal (L4, estudos pequenos e antigos, com alternativas já disponíveis) e para o cor pulmonale crônico (L4, apenas estudos hemodinâmicos agudos), ambos classificados como questão de pesquisa.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação a partir do DrugBank
- Bula do ANVISA com advertências e contraindicações (lacuna bloqueante para a triagem de segurança)
- Confirmação do desenho dos estudos (randomização, desfechos) na angina de Prinzmetal e definição de vantagem frente aos bloqueadores de cálcio já disponíveis
- Avaliação da viabilidade regulatória e comercial, dado que o registro está cancelado
- Se houver interesse em hipertensão pulmonar, evidências específicas (ensaios) em subgrupos vasorreativos e avaliação da via de administração e formulação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

