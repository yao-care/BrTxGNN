---
layout: default
title: Terbutalina Sulfate
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 0
---

# Terbutalina Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Terbutalina Sulfato: Avaliação Preliminar — Sem Previsão TxGNN Disponível

## Resumo em Uma Frase

Terbutalina Sulfato é um broncodilatador da classe dos agonistas beta-2 adrenérgicos, amplamente conhecido no tratamento de broncoespasmo associado à asma e à DPOC.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco com os dados atualmente disponíveis, impossibilitando a análise de novas indicações.
A ausência de registro no Brasil, de dados de mecanismo de ação e de indicação primária documentada no pack inviabiliza uma avaliação completa neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no pack (sem registro ativo na ANVISA) |
| Nova Indicação Prevista | Sem previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | L5 — sem estudos disponíveis no contexto desta avaliação |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou nenhuma previsão de reposicionamento para Terbutalina Sulfato, e o fármaco não possui qualquer registro ativo na ANVISA segundo os dados consultados em 26/03/2026. Com lacunas críticas em segurança (advertências, contraindicações) e em mecanismo de ação, não há base suficiente para avançar a análise neste ciclo.

**Para prosseguir, é necessário:**

- **[Bloqueante]** Obter o DrugBank ID correto para Terbutalina Sulfato e reexecutar a consulta ao TxGNN — sem este identificador, o modelo não gera previsões
- **[Bloqueante]** Verificar se a consulta à ANVISA utilizou a grafia correta do INN (`terbutaline sulfate` ou `sulfato de terbutalina`) e reprocessar; o fármaco é comercialmente conhecido no Brasil sob a marca **Bricanyl®**, o que sugere possível falha de busca por grafia
- **[Alta Prioridade]** Obter dados de mecanismo de ação (MOA) via DrugBank API para viabilizar a análise de relevância mecanística
- **[Alta Prioridade]** Recuperar advertências e contraindicações da bula registrada na ANVISA para completar a avaliação de segurança (Fase S1)
- Após resolução das lacunas acima, regenerar o Evidence Pack e iniciar nova rodada de avaliação

> ⚠️ **Nota metodológica:** A ausência de resultados na consulta TFDA/ANVISA é inconsistente com o conhecimento farmacológico estabelecido sobre este fármaco. Recomenda-se verificar o pipeline de consulta antes de assumir que o medicamento está genuinamente ausente do mercado brasileiro.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

