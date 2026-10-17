---
layout: default
title: Citalopram
parent: Apenas Predição do Modelo (L5)
nav_order: 224
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Citalopram: nova indicação prevista, Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder) (nível de evidência L5). Indicação original: Transtorno de ansiedade, transtorno neurótico, transt…"
monitor_inn: "CITALOPRAM"
predicted_indications: ["schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder"]
---

# Citalopram
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

# Citalopram: Da depressão ao transtorno obsessivo-compulsivo

## Resumo em Uma Frase

Citalopram é um inibidor seletivo da recaptação de serotonina (ISRS), originalmente usado no tratamento de transtornos depressivos e de ansiedade.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder)**,
atualmente com **4 ensaios clínicos** (a maioria com evidência apenas indireta) e **16 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Transtorno de ansiedade, transtorno neurótico, transtorno distímico, depressão unipolar, depressão endógena, transtorno depressivo maior |
| Nova Indicação Prevista | Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L3 (ver observação abaixo) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

**Observação sobre o nível de evidência:** os dados compilados atribuem L1 a esta indicação, mas isso não se sustenta pelos critérios do relatório. Há apenas um ensaio de Fase 3 concluído (NCT00074815), e ele não testa o citalopram diretamente. Os demais suportes são estudos abertos, coortes e revisões, o que corresponde a L3.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o citalopram é um ISRS: bloqueia o transportador de serotonina e aumenta a disponibilidade desse neurotransmissor nas sinapses.

A disfunção serotoninérgica é central na fisiopatologia do TOC, e os ISRS são uma classe de primeira linha no tratamento farmacológico dessa doença. Depressão, ansiedade e TOC compartilham circuitos e vias serotoninérgicas, o que torna plausível a extensão do uso. A pontuação elevada do TxGNN (99,74%) concorda com essa lógica.

Há também estudos específicos com citalopram em TOC, embora pequenos e em sua maioria abertos, incluindo populações resistentes ao tratamento e pediátricas.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Concluído | 78 | Avalia a eficácia de ERP (terapia de exposição e prevenção de resposta), ISRS e a combinação em TOC, além de preditores de resposta em população chinesa. O citalopram pode estar entre os ISRS, mas isso não está confirmado. |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Concluído | 124 | TCC aplicada por psicólogos ou psiquiatras para melhorar o efeito de inibidores da recaptação de serotonina em crianças com TOC e resposta parcial. Não confirma o citalopram como agente estudado. |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Concluído | 158 | TCC em grupo versus fluoxetina em TOC. Evidência apenas indireta, de classe. |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | Concluído | 43 | Estudo piloto da microbiota intestinal em TOC versus controles saudáveis, com acompanhamento de 12 semanas de ISRS. Não fornece evidência terapêutica para o citalopram. |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Estudo clínico aberto randomizado | Eur Psychiatry | Citalopram isolado versus citalopram com clomipramina em 16 adultos com TOC resistente ao tratamento, por 90 dias. |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Estudo simples-cego | J Clin Psychopharmacol | Compara a eficácia antiobsessiva de fluvoxamina, paroxetina e citalopram em 30 pacientes com TOC. |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Estudo aberto (pediátrico) | Psychiatry Clin Neurosci | Citalopram (20-30 mg/dia) por 8 semanas em 15 crianças e adolescentes com TOC; avaliação de eficácia e tolerabilidade. |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Estudo aberto (pediátrico) | J Child Adolesc Psychopharmacol | Em 23 crianças e adolescentes, 10 semanas de citalopram reduziram significativamente o escore Y-BOCS/CY-BOCS (30 para 21; p < 0,001). |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Coorte (preliminar) | CNS Drugs | Investiga a relação entre concentrações de citalopram e resposta clínica em TOC. |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Revisão/Comentário | Int Clin Psychopharmacol | Discute o citalopram no TOC, no contexto da resposta específica do TOC aos inibidores da recaptação de serotonina. |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Revisão | BMJ Clin Evid | Panorama de prevalência, curso e tratamento do TOC. |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Revisão | Curr Med Chem | Fármacos passados, presentes e futuros para o TOC; papel central dos ISRS. |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: síndrome do QT longo (incluindo a forma familiar), torsades de pointes, epilepsia, transtorno bipolar e transtorno afetivo maior, doença hepática, doença da vesícula biliar, deficiência de potássio, distúrbios da coagulação, doença cardíaca e cardiovascular, síndrome neuroléptica maligna, síndrome de secreção inapropriada de ADH (inclusive a forma nefrogênica) e síndrome serotoninérgica.
- **Interações Medicamentosas**: foram registradas 100 interações. Entre as listadas, as de gravidade **maior** incluem bupropiona, omeprazol, lorcaserina, cimetidina, cisaprida, claritromicina, dexfenfluramina, dietilpropiona e dolasetrona (muitas com risco de prolongamento do QT ou de síndrome serotoninérgica). Há ainda interações moderadas (por exemplo, famotidina, loperamida, morfina e ácido acetilsalicílico) e menores (aprepitanto e clotrimazol).
- **Prolongamento do QT**: o risco dose-dependente é conhecido e exige triagem cuidadosa de coadministração.
- **Uso pediátrico**: requer atenção especial a ideação suicida e à dose adequada à idade.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo serotoninérgico é bem estabelecido, os ISRS são tratamento de primeira linha para TOC e há estudos específicos com citalopram, embora pequenos e abertos. Faltam ensaios controlados que testem o citalopram diretamente, e o fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Verificar a situação regulatória e a disponibilidade do citalopram no Brasil, pois não há registro ativo.
- Obter as advertências e contraindicações da bula da ANVISA, ainda ausentes.
- Complementar os dados de mecanismo de ação (DrugBank).
- Confirmar os braços de intervenção dos ensaios NCT02022709 e NCT00074815.
- Definir um plano de monitoramento do QT, da triagem de interações e da segurança pediátrica.

**Outras indicações previstas (todas com decisão Hold):** transtorno de personalidade esquizotípica, esquizoide, histriônica e paranoide, todos com pontuação de 99,68%. Não há ensaios clínicos nem literatura direta que sustentem essas previsões. No caso da personalidade paranoide, os três artigos encontrados são apenas indiretos. A pontuação idêntica sugere um sinal genérico do grafo, e não evidência específica de cada transtorno.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

