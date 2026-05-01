---
layout: default
title: Bazedoxifeno Acetate
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 0
---

# Bazedoxifeno Acetate
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

# Bazedoxifeno Acetato: Dados Insuficientes para Avaliação de Reposicionamento

## Resumo em Uma Frase

Bazedoxifeno Acetato é um modulador seletivo do receptor de estrogênio (SERM) de terceira geração, indicado no âmbito internacional para sintomas vasomotores da menopausa e proteção óssea em mulheres pós-menopáusicas. O presente pacote de evidências **não contém previsões do modelo TxGNN** nem registro regulatório ativo no Brasil, impossibilitando a análise completa de reposicionamento neste momento. Para prosseguir, são necessárias ações de remediação nos itens de dados classificados como bloqueantes.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (nenhum registro ativo no Brasil) |
| Nova Indicação Prevista | Sem previsão disponível (pipeline TxGNN não executado) |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | L5 — apenas dados de log de consulta, sem estudos nem previsão de modelo |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no pacote de evidências recebido. Com base em conhecimento farmacológico publicado, Bazedoxifeno Acetato pertence à classe dos SERMs (Selective Estrogen Receptor Modulators) de terceira geração, com perfil tecido-específico diferenciado em relação a fármacos mais antigos da mesma classe, como tamoxifeno e raloxifeno. Nos Estados Unidos e na Europa, é aprovado em combinação com estrogênios conjugados (Duavee®/Duavive®) para tratamento de sintomas vasomotores moderados a intensos em mulheres pós-menopáusicas sem útero intacto que não tolerem progestogênio.

Seu mecanismo central envolve agonismo/antagonismo seletivo nos receptores ERα e ERβ com especificidade tecidual: age como agonista no osso (prevenindo perda de densidade mineral óssea) e como antagonista no endométrio (dispensando adição de progestogênio para proteção uterina). Esse perfil dual é relevante para possíveis investigações de reposicionamento em condições hormônio-dependentes, como certos subtipos de neoplasias mamárias ou endometriais, bem como osteoporose em contextos clínicos específicos.

Entretanto, **nenhuma dessas hipóteses foi confirmada pelo modelo TxGNN** neste pacote, pois o pipeline não foi executado com os dados do DrugBank disponíveis. Qualquer análise de reposicionamento apresentada aqui seria especulativa e não se baseia nas previsões computacionais do sistema.

---

## Lacunas de Dados Identificadas

| ID | Severidade | Item Faltante | Impacto | Ação Necessária |
|----|-----------|---------------|---------|-----------------|
| DG001 | 🔴 **Bloqueante** | Advertências e contraindicações (bula ANVISA) | Impede avaliação inicial de segurança (S1) | Baixar bula em PDF no portal da ANVISA e extrair dados |
| DG002 | 🟠 **Alta** | Mecanismo de ação (MOA) | Compromete análise de plausibilidade mecanística | Consultar API do DrugBank (1 resultado já disponível no log) |

---

## Informações de Comercialização no Brasil

O fármaco **não possui registros ativos** na base de dados consultada. Nenhuma licença foi encontrada na consulta à ANVISA realizada em 26/03/2026.

> Embora Bazedoxifeno seja aprovado pelo FDA (EUA) e pela EMA (União Europeia), não há comercialização registrada no Brasil até a data de corte deste relatório (05/04/2026).

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Os dados de advertências e contraindicações não foram coletados neste ciclo (DG001 — Bloqueante). A consulta de interações medicamentosas (DDI) não retornou resultados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O pacote de evidências está incompleto em pontos fundamentais: ausência de previsões TxGNN, nenhum registro regulatório ativo no Brasil e dados de segurança (advertências, contraindicações) não coletados. Não é possível emitir recomendação de reposicionamento sem esses elementos mínimos.

**Para prosseguir, é necessário:**
- **[Prioridade 1 — Bloqueante]** Obter a bula ou ficha técnica com advertências e contraindicações via portal da ANVISA (DG001)
- **[Prioridade 2 — Alta]** Processar o resultado já obtido do DrugBank (1 registro confirmado no log de consulta em 26/03/2026) para recuperar DrugBank ID, MOA e categorias farmacológicas (DG002)
- **[Prioridade 3]** Com o DrugBank ID em mãos, executar o pipeline TxGNN (KG + DL) para gerar previsões de reposicionamento e criar um novo pacote de evidências completo
- **[Prioridade 4]** Caso necessário, verificar aprovações internacionais (FDA/EMA) como referência de indicações originais até que o registro brasileiro seja obtido
---

