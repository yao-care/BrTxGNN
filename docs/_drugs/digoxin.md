---
layout: default
title: Digoxin
parent: Apenas Predição do Modelo (L5)
nav_order: 269
evidence_level: L5
indication_count: 5
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-11-24
description: "Digoxin: nova indicação prevista, Angina de Prinzmetal (Prinzmetal angina) (nível de evidência L5). No Brasil, registros na ANVISA: 56 (ativos: 6)"
---

# Digoxin
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

## Digoxina: glicosídeo cardíaco (inibidor da Na+/K+-ATPase) → Angina de Prinzmetal (Prinzmetal angina)
{: .text-alpha }

## Resumo em Uma Frase

Digoxina é um glicosídeo cardíaco, utilizado como medicamento cardiovascular de longa data.
O modelo TxGNN prevê que pode ser eficaz para **Angina de Prinzmetal (Prinzmetal angina)**, mas não há **nenhum ensaio clínico** e apenas **1 publicação** (uma revisão sobre cronofarmacologia no tratamento anti-hipertensivo, que não aborda a digoxina nem a angina vasospástica) associada a esta previsão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Angina de Prinzmetal (Prinzmetal angina) |
| Pontuação de Previsão TxGNN | 0,9981 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 56) |
| Número de Registros | 56 (ativos: 6) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Digoxin (tradução não oficial): “Todas as ações da digoxina são mediadas por meio de seus efeitos sobre a Na-K ATPase. Essa enzima, a “bomba de sódio”, é responsável por manter o meio intracelular em todo o organismo, transportando íons sódio para fora das células e íons potássio para dentro delas.” Texto original em inglês: "All of digoxin’s actions are mediated through its effects on Na-K ATPase. This enzyme, the “sodium pump,” is responsible for maintaining the intracellular milieu throughout the body by moving sodium ions out of and potassium ions into cells." ([DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707), versão de 2025-10-17; acessado em 2026-11-19). Sabe-se que a digoxina atua classicamente inibindo a Na+/K+-ATPase, com efeito inotrópico positivo e redução da condução atrioventricular.

A angina de Prinzmetal (vasoespástica) é causada por espasmo das artérias coronárias e é tratada tipicamente com bloqueadores dos canais de cálcio e nitratos. O efeito inotrópico da digoxina não oferece benefício claro contra o vasoespasmo e, teoricamente, poderia até agravá-lo. A pontuação do modelo é muito alta (0,9981), mas não encontramos justificativa mecanística respaldada por evidências. A previsão deve ser vista como um sinal computacional, ainda não sustentado por dados biológicos ou clínicos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Revisão | Acta Physiologica et Pharmacologica Bulgarica | Revisão sobre cronofarmacologia e ritmos circadianos no tratamento anti-hipertensivo; não aborda digoxina nem angina vasospástica |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 103700458 | DIGOXINA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700665 | CARDCOR | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103920166 | DIGOXINA | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 110390027 | FURP-DIGOXINA | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Ativo |
| 125680092 | DIGOXINA | PRATI DONADUZZI & CIA LTDA | Ativo |
| 141070059 | DIGOXINA | PHARLAB INDÚSTRIA FARMACÊUTICA S.A. | Ativo |
| 100020077 | CARDIOXINA | LABORATORIO SEDABEL LTDA | Cancelado |
| 100140073 | DIGOCARD | QUIMICA FARMACEUTICA NIKKHO DO BRASIL LTDA | Cancelado |
| 100250079 | DIGOXINA | GLAXO WELLCOME S/A | Cancelado |
| 100250084 | DIGOXINA | GLAXO WELLCOME S/A | Cancelado |
| 100330047 | TRENDEN | LIBBS FARMACÊUTICA LTDA | Cancelado |
| 100430095 | NADROXEN | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100920039 | NIILIS | LABORATORIO INDUSTRIAL FARMACÊUTICO LIFAR LTDA | Cancelado |
| 101070200 | DIGOXINA | GLAXOSMITHKLINE BRASIL LTDA | Cancelado |
| 101460071 | DIGOBAL | LABORATÓRIOS BALDACCI LTDA | Cancelado |
| 101620135 | DARROWCOR | LABORATÓRIOS PIERRE FABRE DO BRASIL LTDA | Cancelado |
| 102350310 | DIGOXIL | EMS S/A | Cancelado |
| 102350876 | DIGOXINA | EMS S/A | Cancelado |
| 102700113 | DIGITAX | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 102940094 | CARDIONIL | NEOLATINA COMÉRCIO E INDÚSTRIA FARMACEUTICA S.A | Cancelado |
| 102980009 | DIGOCRIS | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Cancelado |
| 103110055 | CARDIOXINA | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Cancelado |
| 103700107 | CARDCOR | LABORATÓRIO TEUTO BRASILEIRO S/A | Cancelado |
| 103920071 | DIGOXAN | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Cancelado |
| 104040183 | GOXIN | LUPER INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 104650200 | NEO DIGOXIN | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104650415 | DIGOXINA | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104970209 | UNI - DIGOXIN | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |
| 105350115 | CARDGOX | LABORATÓRIO GLOBO SA | Cancelado |
| 105430074 | CARODESIN | INSTITUTO FARMOTERAPICO NEOVITA LTDA | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro), de 56 registros nos dados. A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as listadas, a maioria é de gravidade moderada, por exemplo com acarbose, rabeprazol, doxiciclina, epinefrina, hidrocortisona, colecalciferol, metformina, anfotericina B, bupropiona, triancinolona, ácido acetilsalicílico, dexametasona, betametasona, tetraciclina e fosfato de cálcio. Interações de gravidade leve incluem albiglutida, hiosciamina, atropina e glicopirrônio.

Para demais advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Apesar da pontuação TxGNN elevada, não há ensaios clínicos nem estudos que avaliem a digoxina na angina de Prinzmetal, e o mecanismo de ação conhecido não sustenta um benefício (com possível risco teórico de piora do vasoespasmo). O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação e uma hipótese biológica plausível para o vasoespasmo coronariano
- Estudos pré-clínicos ou observacionais que avaliem diretamente a digoxina na angina vasoespástica
- Revisão das advertências e contraindicações da bula aprovada pela ANVISA
- Análise de segurança cardiovascular específica para esta população

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

