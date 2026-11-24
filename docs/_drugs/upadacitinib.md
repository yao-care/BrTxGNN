---
layout: default
title: Upadacitinib
parent: Apenas Predição do Modelo (L5)
nav_order: 660
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Upadacitinib: nova indicação prevista, Síndrome de microftalmia colobomatosa com displasia rizomélica (colob… (nível de evidência L5). Indicação original: Imunossupressores seletivos"
monitor_inn: "upadacitinib"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Upadacitinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Upadacitinibe: De imunossupressor seletivo para a síndrome de microftalmia colobomatosa com displasia rizomélica
{: .text-alpha }

## Resumo em Uma Frase

Upadacitinibe (RINVOQ) está registrado na ANVISA na categoria de imunossupressores seletivos.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressores seletivos |
| Nova Indicação Prevista | Síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Pontuação de Previsão TxGNN | 0,9961 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Upadacitinib (tradução não oficial): “O upadacitinibe é um inibidor da Janus quinase (JAK). As JAKs são enzimas intracelulares que transmitem sinais provenientes de interações entre citocinas ou fatores de crescimento e seus receptores na membrana celular, para influenciar processos celulares de hematopoiese e a função das células imunes.” Texto original em inglês: "Upadacitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Rinvoq (upadacitinib) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2966aec7-2ef0-923c-d8ff-fe1a957bf095), versão de 2026-06-30; acessado em 2026-11-19). Segundo informações conhecidas, o upadacitinibe pertence à classe dos inibidores de JAK (com atividade principalmente sobre a JAK1), que modulam a sinalização inflamatória mediada pela via JAK-STAT. Seu uso está associado à imunossupressão seletiva.

A síndrome prevista é uma malformação congênita rara, que afeta os olhos (microftalmia com coloboma) e o esqueleto (displasia rizomélica). Presumivelmente, ela decorre de alterações genéticas ou do desenvolvimento, e não de inflamação dependente de JAK. Não foi fornecido nenhum vínculo de via, alvo ou gene entre a inibição de JAK1 e essa condição, portanto não há relação biológica plausível evidente com a indicação original.

A pontuação muito alta (0,9961) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Deve ser tratada apenas como um sinal gerador de hipóteses, e não como evidência clínica.

> Observação: a segunda previsão do modelo, **síndrome de braquidactilia-sindactilia** (pontuação de 0,9958), também não tem ensaios clínicos nem literatura e apresenta a mesma limitação mecanística (malformação congênita do desenvolvimento, sem vínculo com a via JAK-STAT).

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 198600017 | RINVOQ | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 359 interações no total. As principais, de gravidade **Maior**, são:
  - Corticosteroides: hidrocortisona, triamcinolona (incluindo oftálmica), dexametasona, beclometasona, betametasona, budesonida, prednisona e prednisolona
  - Claritromicina
  - Cobicistate
  - Deferiprona
  - Iobenguano (I-131)
- Interações de gravidade **Moderada**: aprepitanto, cimetidina, miconazol e deferasirox.
- Interações de gravidade **Menor**: sulfato, acetato e gluconato de zinco.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se apoia somente na pontuação do modelo (nível L5), sem ensaios clínicos, sem literatura e sem racional mecanístico plausível.

<!-- review:begin br-lic-20261106-upadacitinib-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão se apoia somente na pontuação do modelo (nível L5), sem ensaios clínicos, sem literatura e sem racional mecanístico plausível. Além disso, o único registro no Brasil está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-upadacitinib-1 -->

**Para prosseguir, é necessário:**
- Obter os dados do mecanismo de ação (por exemplo, via DrugBank) e avaliar qualquer vínculo biológico entre a inibição de JAK1 e a síndrome prevista
- Baixar e analisar a bula na ANVISA para obter advertências e contraindicações, etapa que bloqueia a triagem de segurança
- Realizar busca sistemática de literatura e de registros de ensaios clínicos, além de estudos pré-clínicos que sustentem a hipótese
- Esclarecer a situação regulatória atual do fármaco no Brasil
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original, hoje pendentes

<!-- review:begin br-lic-20261106-upadacitinib-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Esclarecer a situação regulatória atual do fármaco no Brasil, já que o registro encontrado está cancelado” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-upadacitinib-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o único registro no Brasil está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que o registro encontrado está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-12 | Tabela: registro 198600017 (RINVOQ) está ativo, não cancelado | Substituído pela tabela de registros gerada por programa (antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Rinvoq (upadacitinib) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2966aec7-2ef0-923c-d8ff-fe1a957bf095) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

