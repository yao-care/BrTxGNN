---
layout: default
title: Bisoprolol
parent: Apenas Predição do Modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Bisoprolol: nova indicação prevista, Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disea… (nível de evidência L5). Indicação original: Hipertensão arterial (transtorno hipertensivo)"
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Bisoprolol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

## Bisoprolol: Da hipertensão arterial à doença renal hipertensiva maligna
{: .text-alpha }

## Resumo em Uma Frase

Bisoprolol é um betabloqueador seletivo beta-1, originalmente usado no tratamento da hipertensão arterial.
O modelo TxGNN prevê que pode ser eficaz para **Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial (transtorno hipertensivo) |
| Nova Indicação Prevista | Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o bisoprolol é um bloqueador seletivo dos receptores beta-1 adrenérgicos, com eficácia comprovada na hipertensão, e mecanisticamente pode ser aplicável a complicações hipertensivas de órgãos-alvo.

A doença renal hipertensiva maligna é uma complicação grave da hipertensão, com lesão renal causada por pressão arterial muito elevada. Por isso, é plausível supor que um fármaco que reduz a pressão arterial e a liberação de renina (por bloqueio beta-1 nas células justaglomerulares) possa ter algum papel.

Há, porém, ressalvas importantes. A pontuação alta do TxGNN (0,999) é apenas uma previsão do modelo. No manejo da hipertensão maligna, em geral são usados agentes intravenosos no cenário agudo, e os betabloqueadores não são tratamento de primeira linha. O valor incremental do bisoprolol nessa condição é incerto.

### Outras previsões do modelo

Outras indicações previstas também têm apenas evidência de modelo, com decisão **Hold**:

| Indicação Prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Hipertensão renovascular maligna | 99,94% | L5 | O bloqueio beta-1 reduz a renina, mas o tratamento definitivo usa inibidores do SRA ou revascularização |
| Hipertensão pulmonar de mecanismo multifatorial incerto | 99,93% | L5 | Vínculo mecanístico fraco; preocupação com efeito inotrópico negativo na falência do ventrículo direito |
| Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,93% | L4 | Apenas evidência indireta (ver abaixo) |
| Síndrome de Braddock | 99,91% | L5 | Sem racional mecanístico identificável; condição rara |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação principal (doença renal hipertensiva maligna) nem para as demais indicações previstas.

## Evidências da Literatura

Não há literatura relacionada à indicação principal. A única indicação com literatura é a hipertensão pulmonar por doença pulmonar e/ou hipóxia, e todos os trabalhos são indiretos (nenhum estudou pacientes com hipertensão pulmonar):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Estudo clínico comparativo | Int J Cardiol | Estudo CARNEBI: comparação multiparamétrica de carvedilol, nebivolol e bisoprolol em insuficiência cardíaca moderada |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Efeitos respiratórios dos betabloqueadores na insuficiência cardíaca; o conceito de que seriam contraindicados com função pulmonar alterada vem sendo questionado |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Estudo fisiológico | Med Sci Sports Exerc | Contribuição do bloqueio beta-adrenérgico e do metabo-quimiorreflexo para a capacidade de exercício |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Estudo fisiológico observacional | J Am Soc Echocardiogr | Adaptação do ventrículo esquerdo à hipóxia aguda, com e sem inibição beta-1 |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | Pré-clínico | Fundam Clin Pharmacol | Bisoprolol protege células miocárdicas da lesão de isquemia-reperfusão via PI3K/AKT/GSK3β |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | In vitro | Nan Fang Yi Ke Da Xue Xue Bao | Efeitos do pré-tratamento com bisoprolol na lesão por hipóxia/reoxigenação em cardiomiócitos H9c2 |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Pré-clínico (animal) | Int Immunopharmacol | Diosmina e bisoprolol combinados atenuam a cardiotoxicidade e a disfunção endotelial induzidas por cloreto de cobalto |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Relato de caso | Hypertens Res | Dois casos de feocromocitoma associado à tetralogia de Fallot (relevância limitada) |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: o grafo de conhecimento do TxGNN associa o bisoprolol a condições como asma (incluindo intrínseca e alérgica), diabetes mellitus e cetoacidose diabética, doença renal, doença hepática (incluindo coma e encefalopatia hepática), pancreatite, doença da vesícula biliar, lúpus eritematoso sistêmico, psoríase, gota, hiperuricemia, hiperparatireoidismo, hipercalcemia, nefrocalcinose, anúria, miastenia gravis, transtornos de ansiedade e distímico, deficiência de potássio e icterícia neonatal. Essas associações exigem confirmação na bula.
- **Interações Medicamentosas**: foram identificadas 100 interações no total. As amostras listadas incluem principalmente interações de gravidade **moderada**, como com epinefrina, bupropiona, morfina, atropina, hioscina/hiosciamina, metescopolamina, corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), acetoexamida e sais de cálcio (acetato, carbonato, citrato, gliconato). Interações **leves** incluem ácido acetilsalicílico, hidróxido de alumínio e attapulgita.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo (99,94%), mas não há ensaios clínicos nem literatura (nível L5). Além disso, os betabloqueadores não são tratamento de primeira linha na hipertensão maligna, e o fármaco não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem esses dados
- Complementar os dados de mecanismo de ação (consulta ao DrugBank)
- Realizar revisão sistemática da literatura sobre betabloqueadores em hipertensão maligna e hipertensão renovascular
- Avaliar a situação regulatória no Brasil, já que não há registros vigentes
- Definir o valor incremental frente às terapias padrão (inibidores do SRA, agentes intravenosos, revascularização)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

