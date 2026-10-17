---
layout: default
title: Brodalumab
parent: Evidência Moderada (L3-L4)
nav_order: 154
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Brodalumab: nova indicação prevista, Doença ocular (eye disease) (nível de evidência L4). Indicação original: Imunomodulador"
monitor_inn: "brodalumab"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "chronic relapsing inflammatory optic neuropathy", "isolated optic neuritis", "recurrent idiopathic neuroretinitis", "optic perineuritis", "episcleritis periodica fugax", "nodular episcleritis"]
---

# Brodalumab
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
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

# Brodalumabe: De imunomodulador a doença ocular (previsão do modelo)

## Resumo em Uma Frase

Brodalumabe (KYNTHEUM) é um anticorpo monoclonal antagonista do receptor A da interleucina-17 (IL-17RA), registrado na ANVISA com a indicação genérica de "imunomodulador".
O modelo TxGNN prevê que pode ser eficaz para **doença ocular (eye disease)**, mas atualmente há **0 ensaios clínicos** e apenas **3 publicações** de relevância limitada (nenhuma demonstra benefício terapêutico).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunomodulador |
| Nova Indicação Prevista | Doença ocular (eye disease) |
| Pontuação de Previsão TxGNN | 99,82% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

> Observação: a indicação prevista de maior pontuação no modelo é a estrongiloidíase (99,84%), mas sem nenhuma evidência (L5) e com risco de segurança plausível. Este relatório se concentra em "doença ocular", a primeira previsão com literatura associada.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o brodalumabe é um antagonista do IL-17RA: ao bloquear o receptor compartilhado, inibe a sinalização de várias isoformas de IL-17 (e não apenas a IL-17A). Esse perfil imunomodulador é o que sustenta seu uso original.

A sinalização de IL-17 está implicada em doenças inflamatórias e autoimunes oculares, como a uveíte, o que oferece uma justificativa plausível, porém indireta, para a previsão. "Doença ocular" é, contudo, uma categoria ampla e pouco específica, e a pontuação elevada pode refletir apenas similaridade no grafo de conhecimento.

A literatura recuperada não mostra benefício terapêutico. Ao contrário, o sinal aponta mais para possíveis preocupações de segurança do que para eficácia (ver seções abaixo).

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Farmacovigilância (mundo real) | Canadian Journal of Ophthalmology | Análise de eventos de uveíte notificados com medicamentos sistêmicos aprovados pela FDA; trata a uveíte como evento adverso, não como alvo terapêutico |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Relato de caso | Rheumatology International | Primeiro caso de doença de Behçet como reação paradoxal ao brodalumabe em paciente com osteíte crônica não bacteriana |
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Pré-clínico | Journal of Translational Medicine | O bloqueio de IL-17R com brodalumabe limitou a periodontite experimental; estudo não ocular, apenas apoia a ação anti-inflamatória do bloqueio de IL-17R |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 185690015 (cancelado) | KYNTHEUM | Não informada | Imunomodulador |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não bula)**: o grafo de conhecimento do TxGNN associa o brodalumabe como contraindicado em doença de Crohn, doença inflamatória intestinal e colite de Crohn.
- **Interações Medicamentosas**: foram identificadas 68 interações; entre as listadas, destacam-se as de gravidade **Major** com adalimumabe, baricitinibe, certolizumabe pegol e vacina BCG (cepa Tice, viva). Há também interações de gravidade moderada com roflumilaste, alefacepte, alentuzumabe, anakinra, canaquinumabe, vacinas vivas e toxoide tetânico, além de interações menores com sais de zinco. A combinação com outros imunossupressores e vacinas vivas exige cautela.
- **Sinais da literatura**: um caso de doença de Behçet (reação paradoxal) e a análise de farmacovigilância sobre uveíte sugerem que o bloqueio de IL-17 pode, em alguns casos, estar associado a eventos inflamatórios oculares/sistêmicos.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é sustentada apenas pelo modelo e por literatura indireta (pré-clínica, relato de caso e farmacovigilância), sem ensaios clínicos e sem demonstração de benefício. O registro brasileiro está cancelado e faltam dados de segurança da bula, o que impede avançar na triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), atualmente ausentes.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Definir uma indicação ocular específica (por exemplo, um subtipo de uveíte) em vez da categoria ampla "doença ocular".
- Realizar revisão sistemática e estudos pré-clínicos em modelos oculares para avaliar eficácia e o risco de eventos paradoxais.
- Esclarecer a situação regulatória (registro cancelado) e a viabilidade de disponibilidade no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

