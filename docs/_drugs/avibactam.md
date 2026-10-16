---
layout: default
title: Avibactam
parent: Apenas Predição do Modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Avibactam: nova indicação prevista, Pneumonia estreptocócica (streptococcal pneumonia) (nível de evidência L5). Indicação original: Pielonefrite (segundo as indicações do grafo de conhecimento TxGNN/…"
monitor_inn: "Avibactam"
predicted_indications: ["streptococcal pneumonia", "influenza, severe, susceptibility to", "ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "staphylococcus aureus infection", "renal tuberculosis", "squamous cell lung carcinoma", "congenital analbuminemia"]
---

# Avibactam
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

# Avibactam: Da pielonefrite à pneumonia estreptocócica

## Resumo em Uma Frase

Avibactam é um inibidor de beta-lactamases, originalmente usado no tratamento da pielonefrite (sempre em associação com um antibiótico beta-lactâmico).
O modelo TxGNN prevê que pode ser eficaz para **pneumonia estreptocócica (streptococcal pneumonia)**,
mas, no momento, há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Pielonefrite (segundo as indicações do grafo de conhecimento TxGNN/PrimeKG; não há texto de indicação aprovada no Brasil) |
| Nova Indicação Prevista | Pneumonia estreptocócica (streptococcal pneumonia) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o avibactam é um inibidor de beta-lactamases sem atividade antibacteriana intrínseca, usado apenas em combinação com um beta-lactâmico (por exemplo, ceftazidima). Sua utilidade em pielonefrite decorre da proteção do antibiótico associado contra enzimas bacterianas que o destruiriam.

A relação com a nova indicação é fraca. A resistência do *Streptococcus pneumoniae* é mediada principalmente por alterações nas proteínas ligadoras de penicilina (PBPs), e não por beta-lactamases. Por isso, o inibidor tende a acrescentar pouco benefício plausível. A pontuação elevada do TxGNN reflete apenas associação na rede de conhecimento, sem respaldo de ensaios ou literatura.

### Outras indicações previstas

Os demais candidatos também têm nível de evidência baixo e recomendação Hold:

| Posição | Indicação prevista | Pontuação TxGNN | Nível | Comentário |
|------|------|------|------|------|
| 2 | Suscetibilidade a influenza grave | 99,28% | L5 | Sem vínculo mecanístico plausível; o avibactam não tem ação antiviral. |
| 3 | Tuberculose de ureter | 99,11% | L5 | Racional teórico: inibição in vitro da beta-lactamase BlaC do *M. tuberculosis*; sem estudos. |
| 4 | Esquistossomose urinária | 99,06% | L5 | Sem alvo antiparasitário conhecido. |
| 5 | Síndrome de hiperviscosidade policlonal | 99,01% | L5 | Sem vínculo mecanístico identificável. |
| 6 | Hiperamilasemia | 99,01% | L5 | Achado laboratorial, não alvo terapêutico. |
| 7 | Infecção por *Staphylococcus aureus* | 98,97% | L4 | Racional parcial (penicilinase estafilocócica é de classe A), mas a resistência à meticilina depende de PBP2a, não abordada pelo avibactam. |
| 8 | Tuberculose renal | 98,93% | L5 | Racional teórico via BlaC; o único artigo recuperado não trata de tuberculose. |
| 9 | Carcinoma pulmonar de células escamosas | 98,86% | L5 | Sem vínculo plausível. |
| 10 | Analbuminemia congênita | 98,84% | L5 | Provável artefato do grafo. |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (pneumonia estreptocócica), atualmente não há literatura relacionada.

Para a indicação de infecção por *S. aureus* (posição 7), foram recuperados trabalhos de caráter geral, nenhum com evidência clínica direta. Os mais relevantes:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40910659](https://pubmed.ncbi.nlm.nih.gov/40910659/) | 2025 | Revisão | Curr Opin Crit Care | Resume recomendações para infecções graves por patógenos MDR/XDR (infecções de corrente sanguínea e pneumonia associada à ventilação), com foco em ensaios randomizados. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisão | Int J Antimicrob Agents | Compara uso off-label e recomendações formais de antibióticos novos e convencionais contra bactérias multirresistentes. |
| [28314920](https://pubmed.ncbi.nlm.nih.gov/28314920/) | 2017 | Revisão | Med Klin Intensivmed Notfmed | Apresenta seis antibióticos novos, incluindo ceftazidima/avibactam; parte baseada apenas em opinião de especialistas. |
| [22733066](https://pubmed.ncbi.nlm.nih.gov/22733066/) | 2012 | Estudo in vitro | Antimicrob Agents Chemother | Atividade de ceftarolina-avibactam contra Gram-negativos produtores de beta-lactamases e MRSA. |
| [24041891](https://pubmed.ncbi.nlm.nih.gov/24041891/) | 2013 | Estudo in vivo (murino) | Antimicrob Agents Chemother | Eficácia de exposições humanizadas de ceftarolina fosamil-avibactam em modelo polimicrobiano. |
| [25667169](https://pubmed.ncbi.nlm.nih.gov/25667169/) | 2015 | Revisão | Langenbecks Arch Surg | Novas moléculas em desenvolvimento contra patógenos multirresistentes (ESKAPE). |

Para a tuberculose renal (posição 8), o único artigo recuperado, [29507064](https://pubmed.ncbi.nlm.nih.gov/29507064/) (2018, coorte, *Antimicrob Agents Chemother*), trata de fatores de risco para falha de tratamento com ceftazidima-avibactam em infecções por Enterobacteriaceae resistentes a carbapenêmicos. Não aborda tuberculose e, portanto, não constitui evidência para esta indicação.

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem pontuação alta no TxGNN, mas nenhum ensaio clínico nem publicação a sustenta (L5). O mecanismo de resistência do pneumococo (alteração de PBPs) não é afetado por um inibidor de beta-lactamases.
- O avibactam não é comercializado no Brasil (0 registros) e os dados de segurança da bula não estão disponíveis, o que impede avançar para a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter as advertências e contraindicações da bula na ANVISA (lacuna bloqueante).
- Obter dados de mecanismo de ação no DrugBank.
- Gerar evidência clínica ou pré-clínica direta para a indicação, em especial dados de suscetibilidade do *S. pneumoniae* à combinação avibactam + beta-lactâmico.
- Se houver interesse em alternativas, priorizar indicações com racional mais plausível (infecção por *S. aureus* e tuberculose, via BlaC), com estudos in vitro e pré-clínicos específicos antes de qualquer avanço clínico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

