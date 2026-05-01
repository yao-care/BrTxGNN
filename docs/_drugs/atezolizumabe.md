---
layout: default
title: Atezolizumabe
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 0
---

# Atezolizumabe
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

# Atezolizumabe: Avaliação de Reposicionamento — Sem Previsão TxGNN Disponível

---

## Resumo em Uma Frase

Atezolizumabe é um anticorpo monoclonal anti-PD-L1 (inibidor de checkpoint imunológico) utilizado no tratamento oncológico.
O Evidence Pack atual **não contém previsões TxGNN** para novas indicações — o pipeline de predição não retornou candidatos para este fármaco.
As lacunas de dados de severidade *Blocking* e *High* precisam ser corrigidas antes de qualquer análise de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/D (nenhuma previsão gerada) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Esta seção não é aplicável no momento — o Evidence Pack não contém previsões TxGNN para atezolizumabe, e portanto não há relação de reposicionamento a avaliar.

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base em informações conhecidas, atezolizumabe é um anticorpo monoclonal humanizado da classe IgG1 que se liga à proteína PD-L1 (*Programmed Death-Ligand 1*), bloqueando sua interação com os receptores PD-1 e B7.1 nos linfócitos T. Este mecanismo desinibe a resposta imunológica antitumoral, potencialmente aplicável a qualquer neoplasia com expressão de PD-L1.

Para que a análise de reposicionamento possa ser conduzida, é necessário primeiro corrigir as lacunas de dados identificadas (DG001 e DG002) e reexecutar o pipeline TxGNN.

---

## Informações de Comercialização no Brasil

O fármaco consta como **comercializado** com **1 registro** no mercado brasileiro. No entanto, os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não estão disponíveis** no Evidence Pack atual — os campos retornaram vazios na consulta à base regulatória.

---

## Citotoxicidade

> Atezolizumabe é um antineoplásico da classe imunoterapia. Esta seção é exibida por se enquadrar nos critérios de fármaco antineoplásico.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | Imunoterapia — Inibidor de Checkpoint Imunológico (anti-PD-L1); **não** é citotóxico convencional |
| Risco de Mielossupressão | Baixo (ação imunomediada; não suprime diretamente a medula óssea) |
| Classificação de Emetogenicidade | Mínima |
| Itens de Monitoramento | Função tireoidiana (TSH), enzimas hepáticas (ALT/AST), função pulmonar, glicemia, função suprarrenal, creatinina |
| Proteção no Manuseio | Seguir protocolos de anticorpos monoclonais; sem risco de citotoxicidade por contato direto |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> As advertências e contraindicações constam como lacuna de dados de severidade **Blocking** (DG001). A remediação recomendada é o download e análise do PDF da bula disponível na base regulatória.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em camadas críticas: nenhuma previsão TxGNN foi gerada, os detalhes do registro regulatório estão vazios e as informações de segurança apresentam lacunas classificadas como *Blocking* — tornando inviável qualquer recomendação de reposicionamento neste momento.

**Para prosseguir, é necessário:**
- **[DG001 — Blocking]** Baixar e analisar o PDF da bula (ANVISA/TFDA) para obter advertências principais e contraindicações
- **[DG002 — High]** Consultar a API do DrugBank para obter o DrugBank ID, MOA completo e categorias farmacológicas
- **Reexecutar o pipeline TxGNN** para gerar candidatos de novas indicações — sem previsões, o relatório de reposicionamento não pode ser produzido
- **Completar os dados de registro**: número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada
- **Após obtenção das previsões**, retornar para avaliação completa, incluindo análise de ensaios clínicos e literatura
---

