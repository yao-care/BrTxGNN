---
layout: default
title: Apalutamida
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 0
---

# Apalutamida
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

# Apalutamida: Do Câncer de Próstata — Sem Previsão de Reposicionamento Disponível

## Resumo

Apalutamida é um inibidor do receptor androgênico (AR), aprovado no Brasil para o tratamento do câncer de próstata resistente à castração não metastático e do câncer de próstata metastático sensível à castração. O Evidence Pack atual **não contém previsões TxGNN** para novas indicações, e apresenta lacunas críticas de dados que impedem a análise completa de reposicionamento. Sem predições disponíveis, não é possível avaliar candidatos de reposicionamento neste momento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados de previsão TxGNN disponíveis para este fármaco. Segundo informações conhecidas, apalutamida é um inibidor do receptor androgênico (AR) de segunda geração, pertencente à classe das anti-androgênicos não esteroidais. Sua eficácia no câncer de próstata foi comprovada por ensaios clínicos de Fase 3 (SPARTAN e TITAN), e mecanisticamente poderia ser aplicável a outras neoplasias dependentes de sinalização androgênica — como câncer de mama com receptor androgênico positivo ou carcinoma hepatocelular.

No entanto, sem a execução do pipeline TxGNN, não é possível quantificar essa aplicabilidade nem priorizar candidatos com base na rede de conhecimento biológico. Esta seção será atualizada após a geração das previsões.

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (Inibidor do receptor androgênico — AR antagonist) |
| Risco de Mielossupressão | Baixo (não é um agente citotóxico convencional) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo, função hepática, sinais e sintomas de convulsão, pressão arterial |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN para novas indicações, o que impossibilita qualquer análise de reposicionamento neste momento. Adicionalmente, os campos regulatórios do registro ANVISA (nome comercial, forma farmacêutica, indicação aprovada) e os dados de segurança estão ausentes, configurando lacunas críticas que bloqueiam a avaliação completa.

**Para prosseguir, é necessário:**
- Executar o pipeline TxGNN para gerar previsões de reposicionamento (`predicted_indications`)
- Completar as informações do registro ANVISA: nome comercial, forma farmacêutica e texto completo da indicação aprovada
- Obter dados de MOA e categorias farmacológicas via DrugBank API (DB ID ainda não mapeado)
- Baixar e analisar a bula da ANVISA para extrair advertências, contraindicações e interações medicamentosas
- Verificar interações medicamentosas via base DDI (consulta retornou `not_found` — confirmar se a busca foi feita pelo nome INN correto)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

