---
noindex: true
sitemap: false
layout: default
title: Abiraterona Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Abiraterona Acetate
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

## Abiraterona Acetato: Do Câncer de Próstata a Indicações Não Preditas — Dados Insuficientes para Ciclo Atual
{: .text-alpha }

## Resumo

Abiraterona Acetato é um inibidor da enzima CYP17A1, aprovado internacionalmente para o tratamento do câncer de próstata resistente à castração (CRPC), atuando ao bloquear a biossíntese de andrógenos em tecidos tumorais, adrenais e testiculares.
O modelo TxGNN **não identificou novas indicações de reposicionamento** para este fármaco no ciclo atual, pois há **duas lacunas críticas de dados** — ausência de informações regulatórias e de mecanismo de ação — que interromperam o pipeline de análise.
A avaliação completa está bloqueada até que as lacunas sejam sanadas.

<!-- review:begin br-lic-20261106-abiraterona_acetate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco **não possui registros vigentes no Brasil**, e a avaliação completa está bloqueada até que as lacunas sejam sanadas.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 16 registros para este medicamento, 15 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-abiraterona_acetate-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata resistente à castração *(baseado em conhecimento geral; não registrado no Evidence Pack)* |
| Nova Indicação Prevista | Nenhuma previsão disponível no ciclo atual |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 16) |
| Número de Registros | 16 (ativos: 15) |
| Decisão Recomendada | **Hold** |

---

## Citotoxicidade

Abiraterona Acetato é classificado como antineoplásico por sua indicação primária no tratamento do câncer de próstata, ainda que atue como terapia hormonal-alvo (inibição enzimática), e não como quimioterapia citotóxica convencional.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo hormonal — Inibidor de biossíntese androgênica (CYP17A1); não é citotóxico convencional |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Baixa (baseado na classe farmacológica — inibidor hormonal de uso oral) |
| Itens de Monitoramento | Função hepática (ALT/AST), potássio sérico, pressão arterial, hemograma completo (CBC), testosterona e PSA |
| Proteção no Manuseio | Seguir regulamentos padrão de manuseio de antineoplásicos; evitar contato com gestantes ou pessoas que tentam conceber |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou candidatos de reposicionamento para Abiraterona Acetato neste ciclo, e a análise de segurança está bloqueada pela ausência de bula ANVISA.

<!-- review:begin br-lic-20261106-abiraterona_acetate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN não gerou candidatos de reposicionamento para Abiraterona Acetato neste ciclo, e a análise de segurança está bloqueada pela ausência de bula ANVISA. O fármaco também não possui registro ativo no Brasil, o que impõe barreiras regulatórias adicionais a qualquer desenvolvimento clínico local.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 16 registros para este medicamento, 15 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-abiraterona_acetate-2 -->

**Para prosseguir, é necessário:**
- **[DG001 — Bloqueante]** Baixar e extrair informações da bula da ANVISA (advertências, contraindicações, populações especiais)
- **[DG002 — Alta prioridade]** Consultar a API do DrugBank para obter dados de mecanismo de ação (MOA), categorias farmacológicas e interações medicamentosas
- Re-executar o pipeline TxGNN com o Evidence Pack completo após resolução das lacunas
- Avaliar viabilidade regulatória: caso surjam candidatos de reposicionamento, será necessário verificar o caminho de registro na ANVISA (importação, registro novo ou uso compassivo)

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco **não possui registros vigentes no Brasil**, e a” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “O fármaco também não possui registro ativo no Brasil, o que impõe barreiras regulatórias adicionais a qualquer desenvolvimento clínico local” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

