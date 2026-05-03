---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Phenobarbital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

O skill confirma que não há instruções adicionais específicas para geração de relatórios além do que está definido no sistema. Vou prosseguir com a elaboração do relatório completo a partir do Evidence Pack fornecido.

---

# Phenobarbital: Da epilepsia à neoplasia do nervo trigêmeo

## Resumo em Uma Frase

Phenobarbital é um anticonvulsivante barbitúrico clássico, utilizado globalmente no tratamento de epilepsia e crises convulsivas há décadas, sem registro ativo no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)**, porém apenas **1 publicação** tangencialmente relacionada foi identificada e **nenhum ensaio clínico** apoia esta direção.
A análise mecanística não identifica conexão causal plausível entre o mecanismo barbitúrico do Phenobarbital e o controle de tumores do nervo trigêmeo, sugerindo que esta previsão é um artefato do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Epilepsia e crises convulsivas (uso global estabelecido; ausência de registro no Brasil) |
| Nova Indicação Prevista | Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. De acordo com informações farmacológicas amplamente estabelecidas, o Phenobarbital é um barbitúrico que atua como modulador positivo dos receptores GABA-A, prolongando a abertura dos canais de cloreto e intensificando a inibição neuronal. Adicionalmente, bloqueia canais de sódio voltagem-dependentes, reduzindo a excitabilidade da membrana neuronal. Estes mecanismos conferem sua eficácia anticonvulsivante consolidada em décadas de uso clínico.

A relação entre o mecanismo do Phenobarbital e neoplasias do nervo trigêmeo é, no entanto, **extremamente limitada**. Tumores do nervo trigêmeo — como schwannomas, meningiomas do forame oval ou neurofibromas — são lesões de crescimento celular anormal que não respondem à modulação GABAérgica ou ao bloqueio de canais de sódio. O Phenobarbital não possui atividade antiproliferativa ou antitumoral conhecida sobre tecido nervoso periférico, e sua indicação em neoplasias não tem qualquer base farmacológica estabelecida.

O único estudo recuperado (PMID 9157801) descreve uma série de casos de **Síndrome de Sturge-Weber**, condição que envolve angioma leptomeníngeo no território do nervo trigêmeo. Nesse contexto, o Phenobarbital foi utilizado exclusivamente para controle de crises epilépticas associadas à síndrome — e não como agente antitumoral. A previsão do TxGNN parece derivar de um caminho espúrio no grafo de conhecimento do tipo "anticonvulsivante → Sturge-Weber → nervo trigêmeo → neoplasia trigêminal", sem suporte biológico real para reposicionamento oncológico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Série de Casos | Anales Españoles de Pediatría | Revisão de 14 casos de Síndrome de Sturge-Weber acompanhados por 25 anos; Phenobarbital utilizado para controle de epilepsia associada à síndrome — sem relação com tratamento de neoplasia do nervo trigêmeo |

---

## Informações de Comercialização no Brasil

O Phenobarbital **não possui registros ativos na ANVISA** e não está comercializado no Brasil. Nenhum produto foi localizado na base regulatória consultada (0 registros).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN de rank 1 (neoplasia do nervo trigêmeo) apresenta nível de evidência L5 — exclusivamente predição do modelo, sem ensaios clínicos e com única publicação sem relação direta à indicação. Não existe mecanismo biológico plausível que conecte a ação barbitúrica do Phenobarbital ao controle de tumores do nervo trigêmeo; a previsão é provavelmente um artefato de caminho no grafo de conhecimento via Síndrome de Sturge-Weber.

**Para prosseguir, é necessário:**
- Investigar o artefato de caminho no grafo TxGNN que gerou esta previsão (suspeita de viés via "Sturge-Weber → território do trigêmeo → neoplasia")
- Avaliar as previsões de ranks 2–9 — epilepsias reflexas (miccional, alimentar, audiogênica, surpresa, leitura) —, que apresentam maior suporte mecanístico e maior volume de evidências com o mesmo fármaco
- Regularizar o registro do Phenobarbital junto à ANVISA como etapa prévia a qualquer estudo clínico no Brasil
- Levantar dados de segurança completos (advertências, contraindicações, interações medicamentosas) a partir da bula do produto
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

