---
layout: default
title: Hemin
parent: Apenas Predição do Modelo (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Hemin: nova indicação prevista, Púrpura Trombocitopênica (Thrombocytopenic Purpura) (nível de evidência L5). Indicação original: Outros derivados do sangue e substitutos"
monitor_inn: "hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Hemina: De derivados do sangue para púrpura trombocitopênica
{: .text-alpha }

## Resumo em Uma Frase

A hemina (PANHEMATIN) está registrada na ANVISA na categoria "outros derivados do sangue e substitutos". É uma fonte de heme, conhecida pelo uso em crises de porfiria aguda.
O modelo TxGNN prevê que pode ser eficaz para **Púrpura Trombocitopênica (Thrombocytopenic Purpura)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica. A previsão é apenas computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros derivados do sangue e substitutos |
| Nova Indicação Prevista | Púrpura Trombocitopênica (Thrombocytopenic Purpura) |
| Pontuação de Previsão TxGNN | 0,9979 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a hemina é um agente de reposição de heme que induz a heme oxigenase-1 e é usado em crises de porfiria aguda.

A relação entre a indicação original (derivado do sangue) e a púrpura trombocitopênica (destruição imunomediada de plaquetas) é apenas especulativa. Os dados não sustentam um elo mecanístico claro. A pontuação alta (0,9979) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica nem de eficácia.

Outras previsões do modelo, como hemofilia, deficiência de inibidor de C1, doença de von Willebrand e trombofilia hereditária, também carecem de evidência direta. Há ainda uma preocupação de segurança: efeitos anticoagulantes transitórios e tromboflebite no local de infusão foram relatados para a hemina, o que torna incerto o uso em distúrbios da coagulação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para a púrpura trombocitopênica.

Observação: para a segunda previsão (hemofilia), foram recuperadas três publicações, todas sobre o givosirana (terapia de RNAi) em porfiria hepática aguda. Elas não avaliam a hemina nem a hemofilia, e por isso não sustentam a previsão.

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 171260002 | PANHEMATIN | RECORDATI RARE DISEASES COMÉRCIO DE MEDICAMENTOS L | Ativo |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 74 interações. Entre as principais:
  - **Maior gravidade**: etinilestradiol, estradiol, estrogênios conjugados, butalbital, amobarbital e fenobarbital.
  - **Gravidade moderada**: ácido acetilsalicílico, abciximabe, alteplase, anagrelida, apixabana, dipiridamol, antitrombina (humana e alfa), acalabrutinibe, avapritinibe, betrixabana, ibritumomabe tiuxetana, tositumomabe (I-131) e trastuzumabe entansina.
  - Muitas delas envolvem anticoagulantes, antiagregantes e trombolíticos, o que exige cautela por causa do possível efeito anticoagulante da hemina.
- Os dados de advertências e contraindicações da bula ainda não foram obtidos. Consulte a bula para essas informações.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas em pontuação computacional (nível L5), sem ensaios clínicos nem literatura, e sem mecanismo plausível demonstrado.
- Faltam dados de segurança da bula.

<!-- review:begin br-lic-20261106-hemin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O único registro no Brasil está cancelado, e faltam dados de segurança da bula.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-hemin-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Complementar os dados do mecanismo de ação (por exemplo, consultando o DrugBank).
- Realizar busca dirigida de literatura sobre a hemina em púrpura trombocitopênica e em outros distúrbios hematológicos.
- Avaliar o risco anticoagulante e trombótico antes de qualquer estudo.
- Fazer estudos pré-clínicos ou de mecanismo, caso a hipótese seja mantida.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O único registro no Brasil está cancelado, e f” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

