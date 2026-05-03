---
layout: default
title: Atracúrio Besylate
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 0
---

# Atracúrio Besylate
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

# Atracúrio Besilato: Avaliação Inconclusiva por Insuficiência de Dados

## Resumo em Uma Frase

Atracúrio Besilato é um agente bloqueador neuromuscular não despolarizante, classicamente utilizado como relaxante muscular em procedimentos cirúrgicos e durante ventilação mecânica.
O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual de análise, o que impossibilita a avaliação comparativa padrão.
A ausência de dados regulatórios brasileiros e de informações de segurança configurou **múltiplas lacunas críticas** que impedem a conclusão do relatório neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Bloqueio neuromuscular (anestesia/ventilação mecânica) |
| Nova Indicação Prevista | Nenhuma — TxGNN não gerou previsões |
| Pontuação de Previsão TxGNN | Indisponível |
| Nível de Evidência | L5 — sem previsão real ou estudos de reposicionamento identificados |
| Situação no Mercado Brasileiro | Não encontrado no registro consultado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Esta seção não se aplica ao ciclo atual, pois o modelo TxGNN não retornou nenhuma indicação candidata para Atracúrio Besilato.

Com base em conhecimento farmacológico geral, o Atracúrio Besilato é um bloqueador neuromuscular não despolarizante da classe benzilisoquinolínica. Atua competindo com a acetilcolina nos receptores nicotínicos da junção neuromuscular, produzindo paralisia muscular reversível. É metabolizado por hidrólise de Hofmann e por esterases plasmáticas, tornando-o relativamente independente de função hepática e renal — uma característica farmacológica distintiva com potencial relevância clínica em populações especiais.

A ausência de previsão pelo TxGNN pode refletir: (1) falha no mapeamento do fármaco ao grafo de conhecimento por divergência no nome INN, (2) ausência de candidatos com score mínimo para geração de output, ou (3) limitação do grafo de conhecimento para fármacos de uso exclusivamente hospitalar/anestésico. Recomenda-se verificar se o identificador DrugBank correto foi utilizado na consulta — o DrugBank ID esperado para atracurium seria **DB00732**.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota**: Atracúrio Besilato é um agente de uso exclusivamente hospitalar, administrado por via intravenosa com monitoramento contínuo. Possui contraindicações e advertências relevantes relacionadas a hipersensibilidade (incluindo reações anafiláticas), acúmulo de laudanosina (metabólito potencialmente neurotóxico em infusões prolongadas) e interações com anestésicos halogenados e antibióticos aminoglicosídeos. Dados formais não foram recuperados neste ciclo de coleta.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack não contém previsões TxGNN, dados regulatórios brasileiros ou informações de segurança estruturadas para Atracúrio Besilato, tornando impossível qualquer análise de reposicionamento neste ciclo. A decisão de "Hold" é mandatória até a resolução das lacunas identificadas.

**Para prosseguir, é necessário:**

1. **Verificar o mapeamento DrugBank** — confirmar se o fármaco foi corretamente identificado como `DB00732` (atracurium) antes de reexecutar o pipeline TxGNN
2. **Reprocessar com nome INN padronizado** — testar variações: `Atracurium Besylate`, `Atracurium besilate`, `atracurium` (sem sal) para garantir correspondência no grafo de conhecimento
3. **Consultar ANVISA** — verificar registros na base de dados ANVISA com variações do nome (Tracrium®, Atracúrio), pois o fármaco possui histórico de comercialização no Brasil
4. **Recuperar bula via ANVISA** — baixar PDF da bula para extrair advertências, contraindicações e interações (necessário para resolução dos Data Gaps DG001 e DG002)
5. **Reexecutar coleta de evidências** — após confirmar DrugBank ID, disparar coleta em ClinicalTrials.gov e PubMed para usos investigacionais do atracúrio (ex.: sedação em UTI, SDRA, status epilepticus refratário)
6. **Revisar limiar de score TxGNN** — verificar se há candidatos com score abaixo do limiar padrão que justifiquem análise manual exploratória
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

