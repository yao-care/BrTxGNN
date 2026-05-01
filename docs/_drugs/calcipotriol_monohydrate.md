---
layout: default
title: Calcipotriol Monohydrate
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 0
---

# Calcipotriol Monohydrate
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

# Calcipotriol Monoidratado: Avaliação de Reposicionamento — Dados Insuficientes

## Resumo em Uma Frase

Calcipotriol monoidratado é um análogo sintético da vitamina D₃, reconhecido pelo uso tópico no tratamento da psoríase.
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco na execução atual,
pois a ausência de DrugBank ID impediu o mapeamento no grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não identificada na base regulatória consultada |
| Nova Indicação Prevista | Nenhuma previsão gerada |
| Pontuação de Previsão TxGNN | N/D |
| Nível de Evidência | N/D |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Avaliação Está Incompleta?

O pipeline TxGNN retornou uma lista de previsões vazia para Calcipotriol Monoidratado. Três fatores explicam essa falha:

**1. Ausência de DrugBank ID.** O grafo de conhecimento do TxGNN é indexado por identificadores DrugBank. Sem esse vínculo, o modelo não consegue posicionar o fármaco na rede de relações droga-doença e, portanto, não emite pontuações de reposicionamento.

**2. Possível mismatch de nomenclatura.** O nome registrado como "CALCIPOTRIOL MONOHYDRATE" inclui a forma hidratada, que pode não ter correspondência direta no vocabulário do normalizador. O INN canônico é simplesmente "calcipotriol" (DB00208 no DrugBank), e a forma monoidratada é uma variante farmacêutica do mesmo princípio ativo.

**3. Data gaps críticos em cascata.** Sem MOA, sem advertências e sem indicações originais mapeadas, os filtros de entrada do pipeline bloquearam a progressão para as etapas de previsão e coleta de evidências.

---

## Informações de Comercialização no Brasil

Calcipotriol monoidratado **não possui nenhum registro ativo** na base regulatória consultada (0 licenças encontradas). Isso indica que, caso haja interesse em lançamento, seria necessário iniciar um processo de registro do zero junto à ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Sem previsões TxGNN e sem DrugBank ID mapeado, não há base técnica para avaliar candidatos de reposicionamento. O relatório não pode avançar além desta etapa sem a correção dos dados de entrada.

**Para prosseguir, é necessário:**
- Confirmar o DrugBank ID correto — provável candidato: **DB00208** (Calcipotriol)
- Verificar se o normalizador aceita "CALCIPOTRIOL MONOHYDRATE" como variante de "calcipotriol"; ajustar o dicionário de sinônimos se necessário
- Re-executar o pipeline após a correção do mapeamento para gerar previsões TxGNN
- Obter MOA completo via DrugBank API (mecanismo de ação via receptor VDR — Vitamin D Receptor)
- Consultar a bula TFDA para extrair advertências e contraindicações e preencher os campos de segurança
- Verificar se existem registros ANVISA sob nomes alternativos (ex.: "calcipotriol", "calcipotriene") antes de concluir que o produto está totalmente ausente do mercado brasileiro
---

