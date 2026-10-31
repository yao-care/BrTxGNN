---
layout: default
title: Valsartan
parent: Evidência Moderada (L3-L4)
nav_order: 664
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan: nova indicação prevista, Malignant hypertensive renal disease (nível de evidência L4). Indicação original: Não consta nos dados locais"
---

# Valsartan
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **6** 
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

## Valsartan: Malignant hypertensive renal disease
{: .text-alpha }

## Resumo em Uma Frase

Valsartana é um bloqueador do receptor de angiotensina II do tipo 1 (AT1), originalmente usado no tratamento da hipertensão arterial.
O modelo TxGNN prevê que pode ser eficaz para **hipertensão renovascular maligna (malignant renovascular hypertension)**,
atualmente com **0 ensaios clínicos** e **1 publicação** (estudo pré-clínico em modelo animal) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Malignant hypertensive renal disease |
| Pontuação de Previsão TxGNN | 0.9997 |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 46 de 144) |
| Número de Registros | 144 (ativos: 46) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a valsartana é um bloqueador do receptor AT1 da angiotensina II, sua eficácia na hipertensão arterial está estabelecida e, mecanisticamente, pode ser aplicável à hipertensão renovascular maligna.

A angiotensina II está elevada na hipertensão maligna e impulsiona a lesão vascular e renal. O único artigo associado (PMID 11560862, 2001) mostra, em modelo animal, que o bloqueio do receptor AT1 preveniu a hipertensão maligna letal, com relação com a inflamação renal. É um vínculo biologicamente plausível, mas de **efeito de classe**: não é específico da valsartana e não é clínico.

Além disso, a nova indicação está muito próxima da indicação já existente (hipertensão). Trata-se mais de uma extensão do uso aprovado do que de um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Pré-clínico (modelo animal) | Circulation | O bloqueio do receptor AT1 da angiotensina II preveniu a hipertensão maligna letal, mesmo sem efeito de redução da pressão arterial, com relação com a inflamação renal |

## Considerações de Segurança

Os dados de advertências e contraindicações da bula não estavam disponíveis. As informações abaixo vêm das predições do modelo TxGNN (deep learning), cujos scores podem refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e **não** de evidência biológica nem do texto da bula.

- **Contraindicações/condições de atenção (grafo de conhecimento)**:
  - Hepáticas e biliares: insuficiência hepática, doença hepática, encefalopatia/coma hepático, doença da vesícula biliar, icterícia neonatal, pancreatite
  - Renais e vasculares: anúria, comprometimento da função renal, obstrução da artéria renal, hipotensão
  - Angioedema (incluindo hereditário, adquirido e induzido por bloqueadores do sistema renina-angiotensina-aldosterona)
  - Metabólicas e eletrolíticas: deficiência de potássio, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, hiperparatireoidismo, osteíte fibrosa, gota, hiperuricemia, diabetes mellitus, cetoacidose diabética
  - Hematológicas e imunológicas: neutropenia, agranulocitose, lúpus eritematoso sistêmico (inclusive pediátrico)
- **Interações medicamentosas**: foram identificadas 100 interações; entre as listadas, destacam-se:
  - **Graves (Major)**: cloreto de potássio e bicarbonato de potássio (risco de hipercalemia)
  - **Moderadas**: hidrocortisona, eluxadolina, exenatida, polietilenoglicol com eletrólitos e diversas insulinas (humana, asparte, degludeca, detemir, glargina, glulisina, lispro, entre outras)

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A única evidência é um estudo pré-clínico de efeito de classe (bloqueio AT1), sem ensaios clínicos e sem dados específicos da valsartana nesta indicação. Além disso, a valsartana não tem registro ativo no Brasil segundo os dados compilados, e a indicação é uma extensão da hipertensão já tratada.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), uma lacuna que bloqueia a triagem de segurança
- Obter dados detalhados do mecanismo de ação (MOA), por exemplo, via DrugBank
- Confirmar a situação regulatória da valsartana no Brasil, inclusive em associações
- Buscar evidência clínica específica (ensaios ou estudos observacionais) em hipertensão maligna/renovascular
- Avaliar se a indicação já está coberta pelo uso aprovado em hipertensão

---

### Outras Indicações Previstas (para referência)

| Indicação prevista | Pontuação TxGNN | Nível de Evidência | Observação | Recomendação |
|------|------|------|------|------|
| Doença renal hipertensiva maligna | 0,9997 | L4 | Único artigo trata da avosentana (antagonista de endotelina), não da valsartana; evidência apenas indireta | Hold |
| Hipertensão pulmonar de mecanismo multifatorial incerto | 0,9997 | L5 | Apenas previsão do modelo, sem ensaios nem literatura | Hold |
| Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 0,9997 | L4 | Estudos pré-clínicos de valsartana/sacubitril-valsartana ligados à biologia da hipóxia (ex.: via HIF-1α); a maioria dos artigos trata de outros órgãos ou outros fármacos; sem ensaios clínicos | Questão de pesquisa |
| Síndrome de Braddock | 0,9996 | L5 | Apenas previsão do modelo | Hold |
| Cor pulmonale crônico | 0,9958 | L4 | Evidência indireta (sacubitril/valsartana em insuficiência cardíaca; um estudo pré-clínico de remodelamento do ventrículo direito, PMID 32552157). O único ensaio associado (NCT02966665, Fase 1, 420 participantes, em recrutamento) é sobre exercício e função vascular na hipertensão, com correspondência fraca | Questão de pesquisa |
| Angina de Prinzmetal | 0,9945 | L5 | O único artigo (PMID 20555232) trata de alternância da onda T, sem relação com o tratamento | Hold |
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

