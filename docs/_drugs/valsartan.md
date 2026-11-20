---
layout: default
title: Valsartan
parent: Apenas Predição do Modelo (L5)
nav_order: 664
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-13
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan: nova indicação prevista, Doença renal hipertensiva maligna (malignant hypertensive renal disease) (nível de evidência L5). No Brasil, registros na ANVISA: 144 (ativos: 44)"
---

# Valsartan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Valsartan: Doença renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumo em Uma Frase

Valsartana é um bloqueador do receptor de angiotensina II, medicamento já comercializado no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Doença renal hipertensiva maligna (malignant hypertensive renal disease)**.
Não há **nenhum ensaio clínico** e há apenas **1 publicação** associada, um estudo pré-clínico com outro fármaco (avosentan). Por isso, a previsão tem nível de evidência **L5**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Doença renal hipertensiva maligna (malignant hypertensive renal disease) |
| Pontuação de Previsão TxGNN | 0.9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 44 de 144) |
| Número de Registros | 144 (ativos: 44) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Valsartan (tradução não oficial): “A angiotensina II é formada a partir da angiotensina I em uma reação catalisada pela enzima conversora de angiotensina (ECA, cininase II). A angiotensina II é o principal agente pressor do sistema renina-angiotensina, com efeitos que incluem vasoconstrição, estimulação da síntese e liberação de aldosterona, estimulação cardíaca e reabsorção renal de sódio. […] Diovan (valsartana) bloqueia os efeitos vasoconstritores e secretores de aldosterona da angiotensina II ao bloquear seletivamente a ligação da angiotensina II ao receptor AT 1 em muitos tecidos, como o músculo liso vascular e a glândula adrenal.” Texto original em inglês: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213), versão de 2026-08-11; acessado em 2026-11-19). A valsartana pertence à classe dos bloqueadores do receptor de angiotensina II, que atuam sobre o sistema renina-angiotensina.

Esse sistema participa do controle da pressão arterial e da hemodinâmica renal. É plausível que seu bloqueio proteja o rim em quadros de pressão muito elevada, e esse é o raciocínio por trás da previsão do modelo.

Essa plausibilidade, porém, é apenas teórica. Nenhum estudo dos dados compilados avalia a valsartana nesta doença. O único trabalho associado investiga o avosentan, um antagonista do receptor de endotelina, e portanto é só uma evidência indireta.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Pré-clínico (outro fármaco: avosentan) | Pharmacological Research | Em ratos transgênicos que superexpressam renina e angiotensinogênio humanos, o avosentan (antagonista de endotelina) protegeu contra a nefropatia hipertensiva em doses que não causam retenção de líquidos. Não estuda a valsartana. |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações nos dados compilados. As de gravidade **maior** incluem:
  - cloreto de potássio;
  - bicarbonato de potássio.

  Em ambos os casos há risco de hiperpotassemia.
- **Interações de gravidade moderada**: incluem várias insulinas (humana, asparte, degludeca, detemir, glargina, glulisina, lispro), exenatida, hidrocortisona, eluxadolina e polietilenoglicol 3350 com eletrólitos.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia somente na pontuação do modelo (0,9997), sem ensaios clínicos e sem estudo da valsartana nesta doença, o que corresponde ao nível de evidência L5.
- O único artigo associado é pré-clínico e trata de outro fármaco.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos ou clínicos que avaliem a valsartana diretamente na doença renal hipertensiva maligna.
- Dados detalhados do mecanismo de ação.
- Revisão das advertências e contraindicações da bula aprovada pela ANVISA, ainda não disponíveis nos dados compilados.
- Avaliação de segurança renal, em particular do risco de hiperpotassemia e de alterações da função renal, em pacientes com lesão renal grave.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

