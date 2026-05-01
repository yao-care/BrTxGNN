---
layout: default
title: Tetracycline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 0
---

# Tetracycline Hydrochloride
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

# Cloridrato de Tetraciclina: Avaliação de Reposicionamento — Dados Insuficientes para Análise

## Resumo em Uma Frase

Cloridrato de Tetraciclina (Tetracycline Hydrochloride) é um antibiótico de amplo espectro da classe das tetraciclinas, historicamente utilizado no tratamento de diversas infecções bacterianas.
O modelo TxGNN **não gerou nenhuma previsão de reposicionamento** para este fármaco no presente ciclo de análise,
e **não há registros de comercialização no Brasil** recuperados neste Evidence Pack, impossibilitando uma avaliação completa.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível neste Evidence Pack |
| Nova Indicação Prevista | Nenhuma previsão gerada pelo TxGNN |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | Abaixo de L5 (sem previsões do modelo) |
| Situação no Mercado Brasileiro | Não comercializado (0 registros na ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Não É Possível Avaliar o Reposicionamento

O pipeline de coleta de dados apresentou as seguintes lacunas críticas que impedem a análise:

**Ausência de previsões TxGNN:** A etapa mais fundamental do relatório — a previsão de nova indicação — não produziu resultados. Isso pode indicar que o fármaco não foi mapeado corretamente ao vocabulário do DrugBank no conhecimento do modelo, ou que sua entrada no pipeline de predição foi interrompida antes da geração de candidatos.

**Dados regulatórios brasileiros ausentes:** A consulta à ANVISA retornou 0 registros para "TETRACYCLINE HYDROCHLORIDE". Isso não significa necessariamente que o fármaco seja inexistente no Brasil — pode haver divergência no nome de busca (e.g., "Tetraciclina", "Tetracycline base") ou registros sob nomes de combinações. A consulta ao DrugBank retornou 1 resultado (status: *success*), mas as informações não foram integradas ao Evidence Pack.

**Mecanismo de ação e segurança não disponíveis:** Sem o DrugBank ID vinculado e sem o PDF da bula processado, os campos de MOA, advertências e contraindicações permanecem em branco.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em seus campos mais críticos — não há previsão de indicação, não há dados regulatórios nacionais e não há informações de segurança processadas. Prosseguir com qualquer avaliação neste estado representaria um risco de análise baseada em dados nulos.

**Para prosseguir, é necessário:**
- **[Alta prioridade]** Recuperar e integrar o registro DrugBank identificado (1 resultado encontrado) para obter DrugBank ID, MOA e categorias farmacológicas
- **[Alta prioridade]** Re-executar o pipeline TxGNN com o DrugBank ID correto para gerar previsões de reposicionamento
- **[Alta prioridade]** Ampliar a busca na ANVISA com variações do nome: "Tetraciclina", "Tetracycline", "Tetracycline HCl", incluindo combinações (ex.: pomadas, colírios)
- **[Média prioridade]** Processar a bula oficial (ANVISA ou DrugBank) para preencher advertências, contraindicações e interações medicamentosas
- Verificar se o fármaco deve ser pesquisado como componente de combinação (ex.: com bismuto, metronidazol) que poderia alterar o escopo da análise
---

