---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando o skill `txgnn-pipeline` como contexto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Omeprazole: De inibidor da bomba de prótons ao refluxo duodenogástrico

## Resumo em Uma Frase

Omeprazole é um inibidor da bomba de prótons (PPI), amplamente utilizado no tratamento de doenças ácido-pépticas, como doença do refluxo gastroesofágico (DRGE) e úlcera péptica, por meio da supressão da secreção de ácido gástrico via bloqueio da H⁺/K⁺-ATPase.
O modelo TxGNN prevê que pode ser eficaz para o **Refluxo Duodenogástrico (Duodenogastric Reflux)**, condição em que o conteúdo duodenal (bile e suco pancreático) retorna ao estômago, e onde o Omeprazole poderia atuar indiretamente na redução do dano combinado ácido-biliar à mucosa gástrica.
Atualmente, há **1 ensaio clínico** identificado com relevância apenas indireta (estudo diagnóstico, grau C) e **nenhuma publicação** de literatura diretamente relacionada a esta indicação específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível nos registros consultados |
| Nova Indicação Prevista | Refluxo Duodenogástrico (Duodenogastric Reflux) |
| Pontuação de Previsão TxGNN | 99,64% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais de mecanismo de ação (MOA) disponíveis na base de dados consultada. Com base nas informações presentes no Evidence Pack, o Omeprazole é um inibidor da bomba de prótons que atua bloqueando a enzima H⁺/K⁺-ATPase nas células parietais gástricas, reduzindo de forma potente e prolongada a secreção de ácido gástrico. Esta classe farmacológica (PPI) é a mais amplamente prescrita no mundo para condições ácido-dependentes.

O refluxo duodenogástrico caracteriza-se pelo retorno de conteúdo duodenal — bile e enzimas pancreáticas — ao estômago, decorrente primariamente de disfunção do esfíncter pilórico. A relação mecanística com o Omeprazole é **indireta**: o fármaco não atua sobre a bile nem corrige a disfunção pilórica, mas pode reduzir o dano à mucosa gástrica quando há coexistência de refluxo ácido e biliar (refluxo misto), ao eliminar o componente ácido do dano combinado. Esta é, portanto, uma aplicação de extensão de mecanismo, e não uma indicação de primeira linha para este diagnóstico específico.

A plausibilidade biológica existe — e Omeprazole é frequentemente usado na prática clínica para manejo sintomático de refluxo misto — mas a ausência de ensaios clínicos terapêuticos desenhados especificamente para refluxo duodenogástrico como desfecho primário enfraquece significativamente a base de evidências para reposicionamento formal.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Concluído | 157 | Estudo diagnóstico avaliando imagem endoscópica tri-modal (NBI + AFI + WLI) para diferenciar dispepsia funcional de doença por refluxo (ácido e biliar). Não avalia a eficácia do Omeprazole como intervenção terapêutica; ausência de desfecho farmacológico primário. |

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Omeprazole possui **1 registro ativo** no Brasil com situação de comercializado. Os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) não constam no Evidence Pack consultado.

> Para verificar os registros completos, consulte diretamente o [Consulta a Produtos e Medicamentos — ANVISA](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O único ensaio clínico identificado é puramente diagnóstico (não avalia Omeprazole como terapêutica, grau de relevância C), não há literatura de suporte, e o mecanismo de ação é apenas indiretamente relacionado à fisiopatologia do refluxo duodenogástrico — um diagnóstico cuja causa primária (disfunção do esfíncter pilórico) não é alvo do Omeprazole. A previsão do TxGNN (99,64%) reflete provavelmente a forte sobreposição de coocorrência clínica entre DRGE e refluxo duodenogástrico nos dados do grafo de conhecimento, e não uma relação causal tratável.

**Para prosseguir, é necessário:**
- Completar os dados de MOA via DrugBank API (DG002) para confirmação formal do perfil mecanístico
- Identificar ensaios clínicos randomizados que avaliem PPI especificamente no desfecho de refluxo duodenogástrico (não apenas DRGE)
- Realizar revisão sistemática da literatura sobre Omeprazole ou PPIs em refluxo biliar e duodenogástrico
- Fazer download e análise da bula registrada na ANVISA para completar os dados de advertências e contraindicações (DG001 — bloqueador)
- Consultar especialistas em gastroenterologia para avaliar se o refluxo duodenogástrico representa uma indicação clínica distinta e tratável com PPI
---

