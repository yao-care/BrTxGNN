---
layout: default
title: Carmustina
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 0
---

# Carmustina
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

# Carmustina: Avaliação de Reposicionamento — Previsão TxGNN Indisponível

## Resumo

Carmustina (BCNU) é um agente alquilante da classe nitrosoureia, com uso estabelecido no tratamento de tumores do sistema nervoso central — incluindo glioblastoma multiforme e astrocitoma anaplásico — além de linfomas de Hodgkin, linfomas não-Hodgkin e mieloma múltiplo.

Nesta avaliação, o modelo TxGNN **não retornou previsões de reposicionamento** para este fármaco. Foram confirmados **6 registros** no mercado brasileiro, porém os detalhes das licenças (indicações aprovadas, formas farmacêuticas) não foram recuperados neste ciclo de coleta. A análise de reposicionamento não pode ser concluída sem dados adicionais.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Neoplasias do SNC, linfomas, mieloma múltiplo *(baseado em conhecimento clínico; detalhes ANVISA não recuperados)* |
| Nova Indicação Prevista | Sem previsão disponível |
| Pontuação de Previsão TxGNN | Indisponível |
| Nível de Evidência | Indisponível |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

Carmustina é classificada como agente antineoplásico citotóxico da classe nitrosoureia, com perfil de toxicidade bem documentado na literatura clínica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — agente alquilante da classe Nitrosoureia |
| Risco de Mielossupressão | **Alto** — mielossupressão cumulativa e de início tardio; nadir típico entre 4–6 semanas após administração |
| Classificação de Emetogenicidade | Médio a Alto (dependente de dose e via de administração) |
| Itens de Monitoramento | Hemograma completo com diferencial e plaquetas; transaminases e bilirrubina; creatinina e ureia; função pulmonar (risco de fibrose pulmonar com uso prolongado) |
| Proteção no Manuseio | Obrigatório seguir regulamentos de manuseio de citotóxicos; agente com potencial mutagênico, teratogênico e carcinogênico reconhecido |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para Carmustina neste ciclo de avaliação, inviabilizando a análise comparativa de indicações. Adicionalmente, os detalhes dos registros regulatórios brasileiros (indicações aprovadas, advertências, contraindicações) não foram recuperados, impossibilitando a avaliação completa de segurança.

**Para prosseguir, é necessário:**
- Mapear o **DrugBank ID** de Carmustina (BCNU) e reexecutar a previsão TxGNN para obter candidatos de reposicionamento
- Recuperar os detalhes dos **6 registros** na ANVISA: números de registro, nomes comerciais, formas farmacêuticas e indicações aprovadas
- Baixar e analisar a **bula oficial** para extrair advertências, contraindicações e interações medicamentosas
- Consultar o **DrugBank** para obter dados completos de mecanismo de ação (MOA) e perfil de segurança
---

