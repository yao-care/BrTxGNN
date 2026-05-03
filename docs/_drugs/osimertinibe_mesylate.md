---
layout: default
title: Osimertinibe Mesylate
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 0
---

# Osimertinibe Mesylate
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

# Osimertinibe Mesilato: Sem Previsão TxGNN – Avaliação Incompleta

## Resumo em Uma Frase

Osimertinibe mesilato é a forma de sal mesilato do osimertinibe (Tagrisso®), inibidor de tirosina quinase EGFR de terceira geração indicado para o tratamento de câncer de pulmão de células não pequenas (CPNPC) com mutações ativadoras de EGFR.
Neste ciclo de execução, o modelo TxGNN **não gerou nenhuma previsão de reposicionamento**, possivelmente porque o fármaco foi identificado pelo nome da forma de sal ("OSIMERTINIBE MESYLATE") em vez do DCI, impossibilitando o mapeamento correto no grafo de conhecimento.
A busca regulatória retornou **0 registros** e os dados de segurança apresentam lacunas críticas, sendo necessária coleta adicional antes de qualquer avaliação de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | CPNPC localmente avançado ou metastático com mutação EGFR (T790M, deleção exon 19, mutação L858R exon 21) ¹ |
| Nova Indicação Prevista | Não disponível — TxGNN não gerou previsão neste ciclo |
| Pontuação de Previsão TxGNN | N/A |
| Nível de Evidência | N/A |
| Situação no Mercado Brasileiro | ✗ Não identificado na busca regulatória (0 registros) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

> ¹ Indicação obtida a partir do conhecimento farmacológico consolidado do osimertinibe (Tagrisso®); o Evidence Pack não contém dados regulatórios locais.

---

## Citotoxicidade

O osimertinibe é classificado como agente antineoplásico (EGFR-TKI), portanto esta seção se aplica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — Inibidor de Tirosina Quinase EGFR de 3ª geração (classe EGFR-TKI) |
| Risco de Mielossupressão | Baixo a médio (leucopenia e trombocitopenia menos frequentes do que com quimioterapia citotóxica convencional) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo (CBC), função hepática (ALT/AST/bilirrubina), ECG (intervalo QTc), monitoramento de sintomas respiratórios (pneumonite/DPI) |
| Proteção no Manuseio | Necessário seguir precauções padrão de manuseio de agentes antineoplásicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A ausência de previsões TxGNN combinada com lacunas críticas nos dados de segurança, mecanismo de ação e registros regulatórios torna inviável conduzir uma avaliação de reposicionamento neste ciclo. A causa raiz mais provável é uma falha de mapeamento pelo uso do nome da forma de sal em vez do DCI.

**Para prosseguir, é necessário:**

- **Corrigir a identificação do fármaco**: Re-executar o pipeline utilizando o DCI `OSIMERTINIBE` (sem o sufixo `MESYLATE`) para garantir mapeamento correto no grafo de conhecimento TxGNN — a busca DrugBank já retornou 1 resultado (`result_count: 1`), indicando que o mapeamento parcial é viável com a nomenclatura correta
- **Verificar o registro regulatório**: Confirmar a situação do Tagrisso® (osimertinibe) no órgão competente; os 0 resultados provavelmente são artefato da busca pelo nome da forma de sal e não refletem a situação real de comercialização
- **Obter dados de MOA** (severidade: Alta): Consultar a entrada DrugBank do osimertinibe para mecanismo de ação detalhado, necessário para a análise de relevância mecanística
- **Obter dados de segurança** (severidade: Bloqueante): Baixar e analisar a bula vigente para advertências, contraindicações e interações medicamentosas, requisito obrigatório para avançar para a avaliação de segurança inicial (S1)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

