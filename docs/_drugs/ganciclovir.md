---
layout: default
title: Ganciclovir
parent: Apenas Predição do Modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ganciclovir: nova indicação prevista, Pneumonia por Citomegalovírus (Cytomegalovirus Pneumonia) (nível de evidência L5). Indicação original: Retinite por citomegalovírus"
---

# Ganciclovir
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

# Ganciclovir: Da retinite por citomegalovírus à pneumonia por citomegalovírus

## Resumo em Uma Frase

Ganciclovir é um antiviral análogo de nucleosídeo, originalmente usado no tratamento da retinite por citomegalovírus (CMV) e da ceratite por herpes simples.
O modelo TxGNN prevê que pode ser eficaz para **Pneumonia por Citomegalovírus (Cytomegalovirus Pneumonia)**,
atualmente com **1 ensaio clínico** e **20 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Retinite por citomegalovírus (o cadastro de registros no Brasil não traz texto de indicação; a indicação original vem do grafo de conhecimento, que também lista ceratite por herpes simples) |
| Nova Indicação Prevista | Pneumonia por Citomegalovírus (Cytomegalovirus Pneumonia) |
| Pontuação de Previsão TxGNN | 97,56% |
| Nível de Evidência | L1 (atribuído pela análise do conjunto de dados; ver ressalva abaixo) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

> **Ressalva sobre o nível de evidência:** o único ensaio clínico disponível é de Fase 4, e não um RCT de Fase 3 em pneumonia por CMV confirmada. O nível L1 baseia-se nesse ensaio somado às orientações clínicas consistentes, portanto deve ser interpretado com cautela.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o ganciclovir é um análogo de nucleosídeo fosforilado por cinases virais (UL97) que inibe a DNA polimerase do CMV. É um mecanismo antiviral direto contra o patógeno causador.

A retinite por CMV e a pneumonia por CMV são manifestações da mesma infecção viral em órgãos-alvo diferentes, especialmente em pacientes imunocomprometidos (transplantados de medula óssea, de órgãos sólidos e pessoas com AIDS). Como o agente causador é o mesmo, é mecanisticamente coerente que o fármaco atue também nos pulmões.

É importante notar que esta é, em grande parte, uma indicação já prevista em bula em diversos países ou uma extensão de uso, e não um reposicionamento genuíno. A literatura revisada reflete o tratamento padrão de pneumonia por CMV em transplantados.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02152358](https://clinicaltrials.gov/study/NCT02152358) | Phase 4 | Concluído | 317 | Tratamento preemptivo com ganciclovir (CMV) ou aciclovir (HSV) em pacientes de UTI em ventilação mecânica prolongada, com objetivo de aumentar os dias livres de ventilador no dia 60. Estudo randomizado, duplo-cego e multicêntrico; resultados não detalhados nos dados compilados |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39774866](https://pubmed.ncbi.nlm.nih.gov/39774866/) | 2025 | Revisão | Intensive Care Medicine | Apresentação clínica, fatores de risco e manejo da infecção por CMV em pacientes imunocomprometidos na UTI |
| [8668848](https://pubmed.ncbi.nlm.nih.gov/8668848/) | 1995 | Revisão | Seminars in Respiratory Infections | Apresentação, diagnóstico e tratamento da pneumonia por CMV; mortalidade próxima de 100% sem tratamento em transplantados alogênicos de medula |
| [8274605](https://pubmed.ncbi.nlm.nih.gov/8274605/) | 1993 | Revisão | Clinical Infectious Diseases | Prevenção e tratamento da pneumonia por CMV em transplantados, com papel crescente do ganciclovir |
| [2161731](https://pubmed.ncbi.nlm.nih.gov/2161731/) | 1990 | Revisão | Drugs | Atividade antiviral, farmacocinética e eficácia; considerado terapia de primeira linha em infecções por CMV com risco à vida ou à visão |
| [32134483](https://pubmed.ncbi.nlm.nih.gov/32134483/) | 2020 | Revisão | The Journal of Infectious Diseases | Avanços terapêuticos contra CMV, incluindo ganciclovir e valganciclovir na prevenção e tratamento em transplantados |
| [2847610](https://pubmed.ncbi.nlm.nih.gov/2847610/) | 1988 | Estudo clínico | Annals of Internal Medicine | Ganciclovir associado a imunoglobulina anti-CMV intravenosa em pneumonia por CMV após transplante de medula óssea |
| [2847609](https://pubmed.ncbi.nlm.nih.gov/2847609/) | 1988 | Relato de casos | Annals of Internal Medicine | Pneumonite intersticial por CMV tratada com sucesso com ganciclovir e imunoglobulina em altas doses |
| [3035246](https://pubmed.ncbi.nlm.nih.gov/3035246/) | 1987 | Série clínica | JAMA | 31 pacientes imunocomprometidos com doença grave por CMV (incluindo pneumonia) tratados com ganciclovir intravenoso |
| [2847292](https://pubmed.ncbi.nlm.nih.gov/2847292/) | 1988 | Série clínica | Reviews of Infectious Diseases | 28 de 39 infecções por CMV (72%) melhoraram com ganciclovir, com eliminação do vírus nas culturas |
| [8390734](https://pubmed.ncbi.nlm.nih.gov/8390734/) | 1993 | Coorte | Transplantation | Fatores de risco e resposta à terapia na pneumonia por CMV após transplante de medula (incidência de 8,8%) |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (não são texto de bula): o grafo de conhecimento associa o ganciclovir a contraindicações em condições como neutropenia, agranulocitose, trombocitopenia, anemia, doença renal, asma, doença pulmonar obstrutiva crônica, síndrome coronariana aguda, estenose aórtica, bloqueio atrioventricular, insuficiência respiratória, uveíte e conjuntivite. Esses itens exigem verificação na bula oficial.
- **Interações medicamentosas** (100 interações identificadas; principais de gravidade moderada): anfotericina B (incluindo formulações lipídicas, lipossomais e de sulfato de colesterila), trospio e nitisinona. Há ainda interações de gravidade desconhecida com fármacos como vancomicina, ácido acetilsalicílico, morfina, prednisona e inibidores de bomba de prótons (omeprazol, pantoprazol, lansoprazol).
- **Medidas de proteção sugeridas pela análise:** monitoramento de mielossupressão, ajuste de dose pela função renal e vigilância de resistência viral.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- O mecanismo antiviral direto é coerente com a nova indicação, e há ampla literatura sobre o tratamento da pneumonia por CMV com ganciclovir em transplantados, além de um ensaio de Fase 4 concluído (n=317). Contudo, esse ensaio não é específico para pneumonia por CMV confirmada, e o fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada (advertências e contraindicações), pois esses dados ainda não estão disponíveis
- Complementar os dados de mecanismo de ação (MOA) a partir do DrugBank
- Confirmar a etiologia viral (por exemplo, por PCR) antes do uso
- Definir plano de monitoramento hematológico (hemograma) e de função renal, com ajuste de dose
- Avaliar a situação regulatória no Brasil, já que não há registro vigente
- Planejar vigilância de resistência viral
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

