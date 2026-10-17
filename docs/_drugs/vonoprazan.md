---
layout: default
title: Vonoprazan
parent: Apenas Predição do Modelo (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vonoprazan: nova indicação prevista, Doença ulcerosa péptica ativa (active peptic ulcer disease) (nível de evidência L5). Indicação original: Medicamentos para úlcera péptica e doenças de refluxo gas…"
monitor_inn: "vonoprazan"
predicted_indications: ["hiatus hernia (disease)", "achlorhydria", "pylorospasm", "Dieulafoy lesion", "cascade stomach", "gastric dilatation", "hemorrhagic duodenitis"]
---

# Vonoprazan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

# Vonoprazana: Da úlcera péptica e doença do refluxo gastroesofágico à doença ulcerosa péptica ativa

## Resumo em Uma Frase

Vonoprazana é um bloqueador de ácido competitivo com o potássio (P-CAB), originalmente usado no tratamento de úlcera péptica e doença do refluxo gastroesofágico.
O modelo TxGNN prevê que pode ser eficaz para **doença ulcerosa péptica ativa (active peptic ulcer disease)**, mas, para esse termo exato, **não há ensaios clínicos nem publicações** nos dados compilados para este relatório. O apoio vem apenas da previsão do modelo e do conhecimento de base.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Medicamentos para úlcera péptica e doenças de refluxo gastroesofágico |
| Nova Indicação Prevista | Doença ulcerosa péptica ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a vonoprazana é um bloqueador de ácido competitivo com o potássio (P-CAB) que inibe a H+/K+-ATPase gástrica (alvo ATP4A) e suprime a secreção de ácido gástrico. Esse tipo de ação é coerente com a cicatrização de úlceras pépticas.

A indicação original (úlcera péptica e doenças de refluxo) já está estreitamente ligada à nova indicação prevista: ambas são doenças relacionadas ao ácido. Por isso, a previsão tem plausibilidade mecanística, mas é em grande parte uma extensão da indicação já existente, e não uma indicação verdadeiramente nova.

Vale lembrar que a vonoprazana já foi aprovada em outros países, como o Japão (2015) para úlcera gastroduodenal e esofagite de refluxo, e os EUA (2022–2023) para erradicação de *H. pylori* e esofagite erosiva. Esses dados reforçam a plausibilidade, mas não constituem evidência específica para "doença ulcerosa péptica ativa" nos dados compilados.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada diretamente a esta indicação nos dados compilados.

Para referência, outras indicações previstas tiveram literatura indireta sobre úlceras pépticas, por exemplo:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27891632](https://pubmed.ncbi.nlm.nih.gov/27891632/) | 2017 | RCT | Aliment Pharmacol Ther | Dois ensaios fase 3 de não inferioridade comparando vonoprazana e lansoprazol em úlceras gástricas ou duodenais |
| [39294424](https://pubmed.ncbi.nlm.nih.gov/39294424/) | 2024 | Revisão sistemática/meta-análise | Dig Dis Sci | Compara vonoprazana e IBPs no tratamento e prevenção de úlceras gástricas e/ou duodenais; a eficácia nessas úlceras ainda é controversa |
| [38582271](https://pubmed.ncbi.nlm.nih.gov/38582271/) | 2024 | Ensaio comparativo randomizado | Gastroenterology | Vonoprazana versus IBP intravenoso na prevenção de ressangramento de úlceras de alto risco após hemostasia endoscópica |
| [33620586](https://pubmed.ncbi.nlm.nih.gov/33620586/) | 2021 | Diretriz | J Gastroenterol | Diretriz japonesa baseada em evidências para doença ulcerosa péptica (2020) |

Esses estudos têm caráter indireto e não substituem evidência específica da indicação prevista.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 106390282 (cancelado) | INZELM | Não informada | MEDICAMENTOS PARA ÚLCERA PÉPTICA E DOENÇAS DE REFLUXO GASTRESOFÁGICO |

---

## Considerações de Segurança

- **Interações Medicamentosas**: a consulta de interações foi concluída, mas retornou apenas a informação farmacológica do alvo (ATP4A), sem interações medicamentosas clínicas classificadas.
- **Observações da literatura**: há relatos de caso de alterações da mucosa gástrica (hiperemia, lesões de aparência de glóbulos brancos) e de hipersecreção ácida de rebote após uso prolongado (6 anos), que merecem atenção em tratamentos longos.

Para as demais informações de segurança (advertências e contraindicações), consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do modelo é alta (99,97%), mas não há ensaios nem publicações diretas para "doença ulcerosa péptica ativa" (L5). Além disso, a indicação prevista praticamente coincide com a indicação original, e o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança.
- Complementar os dados do mecanismo de ação (DrugBank).
- Buscar evidência direta (ensaios clínicos e literatura) para doença ulcerosa péptica ativa, avaliando os ensaios fase 3 em úlcera gástrica/duodenal já publicados.
- Esclarecer o motivo do cancelamento do registro e a situação regulatória atual no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

