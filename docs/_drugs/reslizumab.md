---
layout: default
title: Reslizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 563
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Reslizumab: nova indicação prevista, Trombocitopenia por destruição imune (thrombocytopenia due to immune… (nível de evidência L5). Indicação original: Outros medicamentos antiasmáticos"
monitor_inn: "reslizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
---

# Reslizumab
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

## Reslizumabe: De outros medicamentos antiasmáticos à trombocitopenia por destruição imune
{: .text-alpha }

## Resumo em Uma Frase

Reslizumabe (CINQAIR) é um anticorpo monoclonal anti-IL-5, registrado na ANVISA na categoria "outros medicamentos antiasmáticos".
O modelo TxGNN prevê que pode ser eficaz para **trombocitopenia por destruição imune (thrombocytopenia due to immune destruction)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros medicamentos antiasmáticos |
| Nova Indicação Prevista | Trombocitopenia por destruição imune (thrombocytopenia due to immune destruction) |
| Pontuação de Previsão TxGNN | 0,9953 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Reslizumabe é um anticorpo monoclonal anti-IL-5, que reduz os sinais de sobrevivência e ativação dos eosinófilos. Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório; a descrição acima baseia-se em conhecimento geral sobre a classe do fármaco.

A relação com a trombocitopenia imune é, por ora, apenas uma previsão do modelo (pontuação de 0,9953). Os dados compilados não sustentam um papel estabelecido do bloqueio de IL-5 na destruição plaquetária mediada por mecanismos imunes. A indicação original (asma, doença com componente eosinofílico) e a nova indicação (doença autoimune hematológica) são distintas, e a similaridade entre elas ainda não foi avaliada.

Portanto, a plausibilidade mecanística é limitada e exige investigação adicional antes de qualquer avanço.

### Outra previsão do modelo

O modelo também previu o **distúrbio primário de liberação plaquetária** (pontuação de 0,9925). A única publicação associada é uma revisão sobre o manejo da síndrome hipereosinofílica, incluindo o mepolizumabe (outro anti-IL-5). Ela trata de doença eosinofílica, não de distúrbios plaquetários, e oferece apenas contexto indireto sobre o bloqueio de IL-5, sem evidência clínica para essa indicação. Nenhum ensaio clínico foi identificado.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 155730045 | CINQAIR | TEVA FARMACÊUTICA LTDA. | Ativo |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo, mas não há ensaios clínicos nem literatura direta (nível L5).

<!-- review:begin br-lic-20261106-reslizumab-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão tem pontuação alta no modelo, mas não há ensaios clínicos nem literatura direta (nível L5). Além disso, o único registro brasileiro está cancelado e faltam dados de mecanismo e de segurança.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-reslizumab-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca de literatura e de ensaios clínicos sobre o bloqueio de IL-5 em trombocitopenia imune
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original
- Verificar a viabilidade regulatória

<!-- review:begin br-lic-20261106-reslizumab-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Verificar a viabilidade regulatória, dado que o registro no Brasil está cancelado” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-reslizumab-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Além disso, o único registro brasileiro está cancelado e faltam dados de mecanismo e de segurança” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “dado que o registro no Brasil está cancelado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

