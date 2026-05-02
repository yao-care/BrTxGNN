---
layout: default
title: Tiabendazol
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 0
---

# Tiabendazol
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

# Tiabendazol: Avaliação de Reposicionamento — Previsões Indisponíveis neste Ciclo

## Resumo em Uma Frase

Tiabendazol é um anti-helmíntico da classe benzimidazol, historicamente utilizado no tratamento de infecções parasitárias por nematódeos (como estrongiloidíase e larva migrans cutânea).
O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco neste ciclo de coleta, impossibilitando a análise de reposicionamento.
Com dados estruturais do fármaco incompletos e **0 previsões disponíveis**, é necessário complementar as informações antes de prosseguir.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não recuperada nos registros ANVISA consultados |
| Nova Indicação Prevista | Sem previsão disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | L5 (sem previsões — apenas presença regulatória confirmada) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Informações de Comercialização no Brasil

A consulta à ANVISA confirmou **20 registros ativos** para Tiabendazol. No entanto, os campos individuais de cada registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) **não foram recuperados neste ciclo** — todos retornaram como vazios no Evidence Pack.

Uma nova extração com acesso completo às fichas de registro é necessária para detalhar este quadro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pipeline TxGNN não retornou previsões de reposicionamento para Tiabendazol neste ciclo, e os dados estruturais essenciais do fármaco — mecanismo de ação (MOA), indicações originais aprovadas e informações de segurança — estão ausentes, inviabilizando qualquer análise de mecanismo ou perfil risco-benefício.

**Para prosseguir, é necessário:**
- Recuperar os detalhes completos dos 20 registros ANVISA (nome comercial, indicação aprovada, forma farmacêutica, fabricante)
- Obter o **DrugBank ID** e dados de mecanismo de ação via API DrugBank (a consulta retornou 1 resultado — confirmar se o mapeamento foi bem-sucedido)
- Baixar e analisar a bula ANVISA para extrair advertências, contraindicações e instruções de segurança
- Verificar se o fármaco consta no grafo de conhecimento TxGNN sob o nome em inglês **Thiabendazole**, e reexecutar o pipeline com o identificador correto para gerar previsões de novas indicações
---

