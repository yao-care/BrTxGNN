---
layout: default
title: Cefaclor
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Cefaclor
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

# Cefaclor: De infecções bacterianas à uretrite gonocócica

## Resumo em Uma Frase

Cefaclor é uma cefalosporina de segunda geração originalmente utilizada no tratamento de infecções bacterianas do trato respiratório, urinário e de pele.
O modelo TxGNN prevê que pode ser eficaz para **Uretrite Gonocócica (Gonococcal Urethritis)**, a indicação prevista com maior suporte de evidências entre as candidatas analisadas, com **0 ensaios clínicos registrados** e **6 publicações científicas** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (trato respiratório, urinário, pele e tecidos moles) |
| Nova Indicação Prevista | Uretrite Gonocócica (Gonococcal Urethritis) |
| Pontuação de Previsão TxGNN | 97.48% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nas fontes consultadas. Com base em conhecimento estabelecido da classe farmacológica, Cefaclor pertence às cefalosporinas de segunda geração (β-lactâmicos), cuja eficácia contra infecções bacterianas de diversas origens foi extensamente comprovada. Mecanisticamente, β-lactâmicos atuam inibindo proteínas ligadoras de penicilina (PBPs), interrompendo a síntese da parede celular bacteriana — mecanismo aplicável a bactérias gram-positivas e gram-negativas sensíveis.

*Neisseria gonorrhoeae*, agente etiológico da uretrite gonocócica, é uma bactéria gram-negativa que historicamente demonstrou sensibilidade a cefalosporinas, incluindo o Cefaclor. Estudos in vitro confirmam atividade inibitória (MIC) do Cefaclor contra cepas de *N. gonorrhoeae*, e múltiplos ensaios clínicos conduzidos entre 1979 e 1997 demonstraram taxas de cura superiores a 89% em uretrite gonocócica não complicada em homens.

A maior ressalva clínica relevante é a **resistência antimicrobiana emergente** de *N. gonorrhoeae* aos β-lactâmicos, fenômeno amplamente documentado a partir dos anos 2000. Os dados de suporte datam de décadas anteriores à disseminação de cepas resistentes, o que limita a extrapolação direta para o cenário epidemiológico atual sem um estudo de susceptibilidade contemporâneo.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Ensaio randomizado | Sexually Transmitted Diseases | Ensaio randomizado avaliando regimes de 2, 3 e 4 g de Cefaclor (com/sem probenecida) em uretrite gonocócica masculina; 66 pacientes com cultura confirmada |
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Ensaio clínico controlado | Postgraduate Medical Journal | 40 homens com uretrite gonocócica não complicada; Cefaclor 1 g em dose de ataque demonstrou atividade clínica contra *N. gonorrhoeae* |
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Ensaio clínico comparativo | British Journal of Venereal Diseases | 400 homens randomizados em 4 grupos; taxa de cura com Cefaclor 3 g + probenecida: 95,8%; Cefaclor isolado: 89,6% vs. espectinomicina: 98,9% |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Ensaio clínico controlado (dose única) | Medical Journal of Malaysia | Avaliação de tratamento com dose única oral de Cefaclor em uretrite gonocócica não complicada |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Estudo comparativo / Revisão | Genitourinary Medicine | Reavaliação da eficácia in vivo e in vitro do Cefaclor para infecção gonocócica não complicada; discute viabilidade como alternativa a cefalosporinas de 3ª geração em países em desenvolvimento |
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Relato de experiência clínica | Current Medical Research and Opinion | Série de 1.000 pacientes tratados com cefetamet pivoxil; Cefaclor utilizado como comparador em gonorreia com doses únicas de 1.500 mg e 1.200 mg de cefetamet |

---

## Informações de Comercialização no Brasil

O Cefaclor possui **20 registros ativos** na ANVISA, confirmando sua ampla presença no mercado brasileiro. As informações detalhadas de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estavam disponíveis na base de dados consultada para este relatório.

Para consulta completa dos registros, acesse: [Consulta de Medicamentos — ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Múltiplos ensaios clínicos controlados dos anos 1979–1997 demonstraram eficácia do Cefaclor em uretrite gonocócica não complicada com taxas de cura de 89–96%, apoiando a plausibilidade biológica da previsão TxGNN. Contudo, a resistência antimicrobiana crescente de *N. gonorrhoeae* aos β-lactâmicos desde os anos 2000 exige validação contemporânea antes de qualquer uso clínico.

**Para prosseguir, é necessário:**
- Perfil atualizado de susceptibilidade de *N. gonorrhoeae* a Cefaclor no contexto epidemiológico brasileiro (dados de resistência locais/regionais)
- Dados completos de segurança (advertências, contraindicações e interações medicamentosas via bula ANVISA)
- Detalhamento do mecanismo de ação (MOA) via DrugBank para análise de relação mecanística com *N. gonorrhoeae*
- Avaliação da viabilidade clínica frente aos protocolos atuais de tratamento de DST (diretrizes do Ministério da Saúde e OMS), que priorizam cefalosporinas de 3ª geração injetáveis para gonorreia
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

