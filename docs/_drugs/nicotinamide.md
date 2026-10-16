---
layout: default
title: Nicotinamide
parent: Apenas Predição do Modelo (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nicotinamide: nova indicação prevista, Zinco plasmático elevado (zinc, elevated plasma) (nível de evidência L5). Indicação original: Antianêmicos à base de ferro (associações medicamentosas)"
---

# Nicotinamide
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Nicotinamida: De complexo vitamínico B para zinco plasmático elevado

## Resumo em Uma Frase

Nicotinamida (vitamina B3) foi originalmente usada em polivitamínicos, complexos vitamínicos B, estimulantes do apetite e antianêmicos associados ao ferro.
O modelo TxGNN prevê que pode ser eficaz para **zinco plasmático elevado (zinc, elevated plasma)**, mas atualmente há **0 ensaios clínicos** e apenas **2 publicações** recuperadas, nenhuma delas abordando diretamente essa relação. A previsão é, portanto, essencialmente teórica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antianêmicos à base de ferro (associações medicamentosas) |
| Nova Indicação Prevista | Zinco plasmático elevado (zinc, elevated plasma) |
| Pontuação de Previsão TxGNN | 97,83% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a nicotinamida é a forma amida da vitamina B3 e precursora do NAD+, coenzima central do metabolismo energético e de reações de oxirredução. No Brasil, foi usada sobretudo em associações vitamínicas (complexo B, polivitamínicos) e estimulantes do apetite.

A relação entre essas indicações originais (suplementação nutricional) e o zinco plasmático elevado é fraca. A análise dos dados compilados não identificou vínculo mecanístico crível. As duas publicações recuperadas tratam de hiperinsulinemia/COVID-19 e de enzimas antioxidantes em rim de ratos hipertensos, e nenhuma aborda nicotinamida para excesso de zinco.

A pontuação alta do TxGNN provavelmente é um artefato do grafo de conhecimento, por exemplo, vias compartilhadas de enzimas dependentes de metais ou de oxirredução. Por isso, a previsão deve ser tratada com cautela.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [32938758](https://pubmed.ncbi.nlm.nih.gov/32938758/) | 2020 | Revisão | Open Heart | Discute hiperinsulinemia, magnésio, vitamina D e trombose na COVID-19. Não aborda nicotinamida nem zinco elevado |
| [15361776](https://pubmed.ncbi.nlm.nih.gov/15361776/) | 2004 | Estudo animal | Journal of Hypertension | Enzimas antioxidantes (SOD, catalase, GPX) no rim de ratos espontaneamente hipertensos com dieta rica em antioxidantes. Sem relação direta com a indicação |

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 144930034 | FORTEVIT | Não informada | Antianêmicos à base de ferro - associações medicamentosas |
| Registro 138410051 | COMPLE B | Não informada | Polivitamínicos sem minerais |
| Registro 102351340 | COMPLEXO B | Não informada | Complexo vitamínico B (somente) |
| Registro 170560017 | BENEROC | Não informada | Polivitamínicos sem minerais |
| Registro 100380038 | PETIVIT BC | Não informada | Estimulantes do apetite |

## Considerações de Segurança

- **Contraindicações (relações do grafo de conhecimento, não da bula):** doença renal, doença hepática, doença da vesícula biliar, úlcera péptica, diabetes mellitus, cetoacidose diabética, gota, doenças da coagulação sanguínea, síndrome coronariana aguda, doenças da tireoide, hemocromatose hereditária, hemossiderose, doença de Wilson, hemofilia, rabdomiólise, hipotensão, entre outras.
- **Interações Medicamentosas:** 64 interações registradas, quase todas de nível moderado. As principais envolvem antidiabéticos (metformina, acarbose, pioglitazona, inibidores de SGLT2 como dapagliflozina, canagliflozina e empagliflozina, inibidores de DPP-4 como linagliptina e alogliptina, agonistas de GLP-1 como dulaglutida e albiglutida, clorpropamida), asparaginases, metotrexato, clofarabina, brentuximabe vedotina, efavirenz e canabidiol. A interação com carbamazepina é de nível leve.

Os dados de advertências e contraindicações da bula na ANVISA não estavam disponíveis. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação alta do TxGNN (97,83%), não há ensaios clínicos nem literatura que sustentem o uso da nicotinamida para zinco plasmático elevado, e não existe mecanismo plausível identificado. Além disso, não há registros vigentes no Brasil.

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação (consulta ao DrugBank).
- Baixar e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Realizar busca dirigida da literatura sobre nicotinamida e metabolismo do zinco.
- Avaliar a viabilidade regulatória, já que todos os 20 registros estão cancelados.

## Observação sobre Outras Indicações Previstas

Entre as demais previsões, a de maior interesse é a **síndrome de Werner** (pontuação TxGNN de 88,61%, nível de evidência L2, classificada como "questão de pesquisa"). Há um ensaio randomizado, duplo-cego e cruzado de 2025 (PMID [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/)) que usou **ribosídeo de nicotinamida**, um precursor de NAD+ relacionado, mas distinto da nicotinamida. Estudos pré-clínicos mostram que o aumento de NAD+ restaura a mitofagia em modelos da doença (PMID [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/) e [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/)). A evidência para a nicotinamida em si é indireta, e a fase e o tamanho amostral desse ensaio não foram verificados. Essa indicação merece uma avaliação própria e mais aprofundada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

