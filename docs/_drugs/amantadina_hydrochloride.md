---
noindex: true
sitemap: false
layout: default
title: Amantadina Hydrochloride
parent: Apenas Predição do Modelo (L5)
nav_order: 46
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amantadina Hydrochloride
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
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

## Amantadina Hidrocloreto: Avaliação de Reposicionamento Inconclusiva — Dados Insuficientes
{: .text-alpha }

## Resumo em Uma Frase

Amantadina Hidrocloreto (AMANTADINA HYDROCHLORIDE) é um fármaco com histórico clínico documentado na literatura médica internacional, porém **nenhuma indicação prevista foi gerada pelo modelo TxGNN** neste ciclo de avaliação.

<!-- review:begin br-lic-20261106-amantadina_hydrochloride-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Amantadina Hidrocloreto (AMANTADINA HYDROCHLORIDE) é um fármaco com histórico clínico documentado na literatura médica internacional, porém **nenhuma indicação prevista foi gerada pelo modelo TxGNN** neste ciclo de avaliação. A ausência de registros no mercado brasileiro e a falta do DrugBank ID impedem o mapeamento do fármaco na rede de conhecimento TxGNN, inviabilizando uma análise completa de reposicionamento neste momento.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amantadina_hydrochloride-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (0 registros encontrados no banco regulatório brasileiro) |
| Nova Indicação Prevista | Nenhuma previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | Não aplicável |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Não Há Previsão Disponível?

Uma hipótese provável é que o nome consultado mistura o idioma português ("amantadina") com o inglês ("hydrochloride"), podendo não corresponder ao formato cadastrado nos sistemas da ANVISA — onde o equivalente seria "Amantadina Cloridrato" ou "Cloridrato de Amantadina".

<!-- review:begin br-lic-20261106-amantadina_hydrochloride-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A consulta ao banco de dados regulatório brasileiro retornou **0 registros** para o nome "AMANTADINA HYDROCHLORIDE". Uma hipótese provável é que o nome consultado mistura o idioma português ("amantadina") com o inglês ("hydrochloride"), podendo não corresponder ao formato cadastrado nos sistemas da ANVISA — onde o equivalente seria "Amantadina Cloridrato" ou "Cloridrato de Amantadina".” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amantadina_hydrochloride-2 -->

Além disso, a ausência do **DrugBank ID** é um bloqueio crítico: sem esse identificador, o fármaco não pode ser mapeado como nó na rede do conhecimento TxGNN, o que impede a geração de qualquer previsão de reposicionamento pelo modelo de aprendizado profundo ou pelo método de grafo de conhecimento (KG).

Por fim, a indisponibilidade dos dados de **mecanismo de ação (MOA)** e das **advertências e contraindicações** oficiais impede tanto a análise de plausibilidade biológica quanto a triagem inicial de segurança — etapas obrigatórias antes de qualquer recomendação clínica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Os dados mínimos necessários para uma avaliação estruturada de reposicionamento — DrugBank ID, MOA e informações de segurança regulatória — estão ausentes neste pacote de evidências.

<!-- review:begin br-lic-20261106-amantadina_hydrochloride-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco não possui registros no mercado brasileiro e não gerou previsões TxGNN. Os dados mínimos necessários para uma avaliação estruturada de reposicionamento — DrugBank ID, MOA e informações de segurança regulatória — estão ausentes neste pacote de evidências.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-amantadina_hydrochloride-3 -->

**Para prosseguir, é necessário:**
- **[Bloqueante]** Revisar o nome de busca no sistema ANVISA: tentar "Cloridrato de Amantadina", "Amantadina Cloridrato" ou "Amantadine Hydrochloride"
- **[Bloqueante]** Coletar advertências, contraindicações e dados de segurança da bula oficial (fonte: ANVISA / bula do fabricante)
- **[Alta prioridade]** Obter o DrugBank ID para habilitar o mapeamento e a geração de previsões TxGNN
- **[Alta prioridade]** Consultar a API do DrugBank para obter dados de MOA e categorias farmacológicas
- Após resolução dos itens acima, reprocessar o Evidence Pack e gerar novo ciclo de avaliação

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A ausência de registros no mercado brasileiro e a falta do DrugBank ID impedem o mapeamento do fármaco na rede de conhecimento TxGNN, inviab” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “A consulta ao banco de dados regulatório brasileiro retornou **0 registros** para o nome "AMANTADINA HYDROCHLORIDE"” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco não possui registros no mercado brasileiro e não gerou previsões TxGNN” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

