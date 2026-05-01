---
layout: default
title: Amlodipine Besylate
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Amlodipine Besylate
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

# Besilato de Amlodipina: Avaliação de Reposicionamento — Dados Insuficientes para Conclusão

## Resumo em Uma Frase

Besilato de Amlodipina é um bloqueador dos canais de cálcio da classe das diidropiridinas, amplamente reconhecido no tratamento da hipertensão arterial e da angina estável crônica.
Nesta avaliação, o modelo TxGNN **não retornou nenhuma indicação de reposicionamento** para este fármaco.
Além disso, a consulta regulatória retornou **0 registros** e os dados de segurança apresentaram lacunas críticas, impossibilitando a conclusão da avaliação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial / Angina estável crônica *(baseado em conhecimento farmacológico geral — dado ausente no Evidence Pack)* |
| Nova Indicação Prevista | Não identificada pelo TxGNN nesta avaliação |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 — sem estudos encontrados para indicação nova |
| Situação no Mercado | Não registrado (0 registros na base consultada) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Avaliação Está Incompleta?

Besilato de Amlodipina pertence à classe das diidropiridinas e atua bloqueando os canais de cálcio do tipo L em músculo liso vascular e células cardíacas. Esse mecanismo reduz a resistência vascular periférica, diminui a pós-carga cardíaca e alivia o espasmo coronariano — base consolidada do seu uso em hipertensão e angina. Trata-se de um dos fármacos cardiovasculares mais prescritos no mundo, com perfil farmacológico extensamente estudado.

No entanto, o Evidence Pack recebido apresenta duas lacunas críticas identificadas como **DG001** (ausência de advertências e contraindicações regulatórias) e **DG002** (ausência de dados formais de mecanismo de ação). A lacuna DG001 é classificada como **Bloqueante**, pois impede a conclusão da avaliação de segurança preliminar (etapa S1). Sem esse dado, qualquer recomendação de reposicionamento seria prematura.

Adicionalmente, a consulta ao modelo TxGNN não retornou candidatos de reposicionamento (`predicted_indications: []`). Isso pode indicar um problema no mapeamento do INN — o sufixo de sal **"BESYLATE"** pode não estar sendo reconhecido corretamente pelo sistema; a consulta deveria ser reprocessada utilizando apenas **"AMLODIPINE"** como termo de busca.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> *Nota: A consulta DDI retornou status `not_found` e os campos de advertências e contraindicações estão ausentes nesta versão do Evidence Pack. O log de consulta ao DrugBank registra 1 resultado (`result_count: 1`), mas os dados não foram extraídos para os campos correspondentes — verificar pipeline de extração.*

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não retornou indicações de reposicionamento para este fármaco, e as lacunas regulatórias e de segurança classificadas como críticas impedem qualquer análise conclusiva. A avaliação não pode avançar com os dados atualmente disponíveis.

**Para prosseguir, é necessário:**
- **Corrigir a consulta TxGNN**: reprocessar usando o INN simplificado `"AMLODIPINE"` (sem o sufixo do sal besylato), que é o termo indexado no grafo de conhecimento
- **Verificar a extração do DrugBank**: o log indica 1 resultado encontrado (`result_count: 1`), mas os campos `drugbank_id`, `original_moa` e `key_warnings` não foram populados — inspecionar o pipeline de extração
- **Verificar registros regulatórios**: para o contexto brasileiro, consultar diretamente a base da ANVISA — besilato de amlodipina (DCB: *anlodipino*) consta na RENAME e deve ter múltiplos registros ativos; a ausência de resultados sugere falha na consulta, não ausência real de registro
- **Reprocessar o Evidence Pack** após correções acima antes de nova emissão de relatório de reposicionamento
---

