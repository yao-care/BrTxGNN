---
noindex: true
sitemap: false
layout: default
title: Teriflunomida
parent: Apenas Predição do Modelo (L5)
nav_order: 617
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Teriflunomida
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

## Teriflunomida: De Esclerose Múltipla — Avaliação de Reposicionamento Incompleta
{: .text-alpha }

## Resumo

Teriflunomida é um agente imunomodulador oral aprovado para o tratamento de formas recidivantes da esclerose múltipla (EM), atuando como inibidor da enzima dihidroorotato desidrogenase (DHODH). O presente Evidence Pack não contém predições TxGNN processadas para este fármaco, impossibilitando a análise de reposicionamento neste momento. Os dados do pacote estão incompletos para suportar uma avaliação de nova indicação.

<!-- review:begin br-lic-20261106-teriflunomida-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Com 11 registros ativos no Brasil, há base regulatória estabelecida, mas os dados do pacote estão incompletos para suportar uma avaliação de nova indicação.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 11 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-teriflunomida-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Esclerose Múltipla recidivante (com base no INN e conhecimento farmacológico consolidado) |
| Nova Indicação Prevista | — Não disponível neste Evidence Pack |
| Pontuação de Previsão TxGNN | — Não disponível |
| Nível de Evidência | L5 (ausência de predição processada) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 11) |
| Número de Registros | 11 (ativos: 5) |
| Decisão Recomendada | **Hold** |

---

## Informações de Comercialização no Brasil

Entretanto, os campos de detalhamento dos registros (número, nome comercial, forma farmacêutica e texto de indicação aprovada) retornaram vazios na extração atual.

<!-- review:begin br-lic-20261106-teriflunomida-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O Evidence Pack confirma **11 registros ativos** de Teriflunomida no Brasil e status de comercialização ativo. Entretanto, os campos de detalhamento dos registros (número, nome comercial, forma farmacêutica e texto de indicação aprovada) retornaram vazios na extração atual.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 11 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-teriflunomida-2 -->

> Os dados de registro precisam ser complementados por consulta direta ao sistema DATAVISA/ANVISA para listar os produtos individualmente.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém predições TxGNN processadas (`predicted_indications` vazio), o que impossibilita a identificação de candidatos de reposicionamento. Adicionalmente, os dados de registro no Brasil e as informações de segurança não foram carregados com sucesso, bloqueando a avaliação regulatória e de risco.

**Para prosseguir, é necessário:**
- **[Crítico]** Executar o pipeline TxGNN com o identificador DrugBank correto de Teriflunomida (DB08880) para gerar as predições de reposicionamento
- **[Alto]** Recuperar o MOA completo via DrugBank API (Teriflunomida: inibidor de DHODH) para permitir análise de relacionamento mecanístico
- **[Alto]** Baixar e analisar a bula aprovada pela ANVISA para extrair advertências, contraindicações e interações medicamentosas
- Após a obtenção das predições, reavaliar o Evidence Pack completo seguindo o fluxo padrão L1–L5

<!-- review:begin br-lic-20261106-teriflunomida-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**[Crítico]** Executar o pipeline TxGNN com o identificador DrugBank correto de Teriflunomida (DB08880) para gerar as predições de reposicionamento / **[Crítico]** Reprocessar os dados ANVISA/TFDA para preencher os campos de registro (número, nome comercial, indicação aprovada)” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-teriflunomida-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Com 11 registros ativos no Brasil, há base regulatória estabelecida, mas o” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O Evidence Pack confirma **11 registros ativos** de Teriflunomida no Brasil e status de comercialização ativo” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “**[Crítico]** Reprocessar os dados ANVISA/TFDA para preencher os campos de registro (número, nome comercial, indicação aprovada)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

