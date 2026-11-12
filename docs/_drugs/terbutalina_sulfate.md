---
noindex: true
sitemap: false
layout: default
title: Terbutalina Sulfate
parent: Apenas Predição do Modelo (L5)
nav_order: 616
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Terbutalina Sulfate
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

## Terbutalina Sulfato: Avaliação Preliminar — Sem Previsão TxGNN Disponível
{: .text-alpha }

## Resumo em Uma Frase

Terbutalina Sulfato é um broncodilatador da classe dos agonistas beta-2 adrenérgicos, amplamente conhecido no tratamento de broncoespasmo associado à asma e à DPOC.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados atualmente disponíveis, impossibilitando a análise de novas indicações.

<!-- review:begin br-lic-20261106-terbutalina_sulfate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados atualmente disponíveis, impossibilitando a análise de novas indicações. / A ausência de registro no Brasil, de dados de mecanismo de ação e de indicação primária documentada no pack inviabiliza uma avaliação completa neste momento.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 6 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-terbutalina_sulfate-1 -->

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no pack (sem registro ativo na ANVISA) |
| Nova Indicação Prevista | Sem previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — sem estudos disponíveis no contexto desta avaliação |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 6) |
| Número de Registros | 6 (ativos: 5) |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Terbutalina Sulfato. Com lacunas críticas em segurança (advertências, contraindicações) e em mecanismo de ação, não há base suficiente para avançar a análise neste ciclo.

<!-- review:begin br-lic-20261106-terbutalina_sulfate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Terbutalina Sulfato, e o fármaco não possui qualquer registro ativo na ANVISA segundo os dados consultados em 26/03/2026.” Removido: a afirmação contradizia os dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 6 registros para este medicamento, 5 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-terbutalina_sulfate-2 -->

**Para prosseguir, é necessário:**

- **[Bloqueante]** Obter o DrugBank ID correto para Terbutalina Sulfato e reexecutar a consulta ao TxGNN — sem este identificador, o modelo não gera previsões
- **[Bloqueante]** Verificar se a consulta à ANVISA utilizou a grafia correta do INN (`terbutaline sulfate` ou `sulfato de terbutalina`) e reprocessar; o fármaco é comercialmente conhecido no Brasil sob a marca **Bricanyl®**, o que sugere possível falha de busca por grafia
- **[Alta Prioridade]** Obter dados de mecanismo de ação (MOA) via DrugBank API para viabilizar a análise de relevância mecanística
- **[Alta Prioridade]** Recuperar advertências e contraindicações da bula registrada na ANVISA para completar a avaliação de segurança (Fase S1)
- Após resolução das lacunas acima, regenerar o Evidence Pack e iniciar nova rodada de avaliação

> Recomenda-se verificar o pipeline de consulta antes de assumir que o medicamento está genuinamente ausente do mercado brasileiro.

<!-- review:begin br-lic-20261106-terbutalina_sulfate-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “> ⚠️ **Nota metodológica:** A ausência de resultados na consulta TFDA/ANVISA é inconsistente com o conhecimento farmacológico estabelecido sobre este fármaco. Recomenda-se verificar o pipeline de consulta antes de assumir que o medicamento está genuinamente ausente do mercado brasileiro.” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-terbutalina_sulfate-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A ausência de registro no Brasil, de dados de mecanismo de ação e de indicação primária documentada no pack inviabiliza uma avaliação comple” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “e o fármaco não possui qualquer registro ativo na ANVISA segundo os dados consultados em 26/03/2026” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “⚠️ **Nota metodológica:** A ausência de resultados na consulta TFDA/ANVISA é inconsistente com o conhecimento farmacológico estabelecido sob” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

