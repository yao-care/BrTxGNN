---
layout: default
title: Ivacaftor
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Ivacaftor
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

O skill `txgnn-pipeline` está ativo. Vou proceder agora à geração do relatório de avaliação de reposicionamento com base no Evidence Pack fornecido.

---

# Ivacaftor: Da Fibrose Cística à Artrite Reumatoide

## Resumo em Uma Frase

Ivacaftor é um potenciador do canal CFTR (*Cystic Fibrosis Transmembrane Conductance Regulator*), originalmente aprovado para o tratamento da fibrose cística (FC) em pacientes portadores de mutações específicas do gene CFTR.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, atualmente com **1 ensaio clínico** e **1 publicação** apoiando esta direção.
A força das evidências disponíveis, no entanto, é ainda incipiente — ambas as fontes são indiretas e não foram desenhadas especificamente para avaliar Ivacaftor em artrite reumatoide.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Fibrose cística (FC) com mutação CFTR elegível |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 96,97% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 7 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimento consolidado da literatura, Ivacaftor (Kalydeco®) é um potenciador (*potentiator*) do canal de cloro CFTR: liga-se à proteína CFTR já presente na superfície celular e aumenta a probabilidade de abertura do canal, restaurando o transporte iônico em pacientes com mutações que comprometem a função do canal (ex.: G551D). A ação é altamente seletiva — Ivacaftor atua exclusivamente em células que expressam CFTR funcional na membrana.

A conexão com a artrite reumatoide (AR) é de natureza indireta e mecanisticamente especulativa. CFTR foi identificado em células do sistema imune inato, incluindo neutrófilos e macrófagos. Estudos em modelos de fibrose cística sugerem que a disfunção do CFTR potencializa a sinalização pró-inflamatória mediada por NF-κB e aumenta a geração de espécies reativas de oxigênio (ROS). Teoricamente, ao restaurar a função do CFTR nessas células imunes, Ivacaftor poderia atenuar a resposta inflamatória crônica que caracteriza a AR. Entretanto, essa hipótese foi gerada a partir de dados de pacientes com FC — não de populações com AR.

A AR e a fibrose cística compartilham fenótipos inflamatórios (neutrofilia, disfunção de macrófagos, elevação de citocinas), o que pode ter levado o modelo TxGNN a identificar uma sobreposição de nós (*nodes*) no grafo de conhecimento. A pontuação elevada (96,97%) deve ser interpretada com cautela: sem estudos translacionais diretos, a previsão permanece no estágio de hipótese biológica, sem suporte clínico suficiente para progressão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | NA (Observacional) | Concluído | 47 | Estudo prospectivo que analisa fenótipo e função de neutrófilos sanguíneos em pacientes com FC, incluindo impacto dos moduladores CFTR (entre eles Ivacaftor). Não é um ensaio de intervenção para AR. Relevância indireta: avalia o papel imunológico dos moduladores CFTR — base mecanística para a hipótese de reutilização em doenças inflamatórias. |

> ⚠️ **Nota:** O único ensaio identificado é observacional (Fase NA) e focado em FC. Não há ensaios clínicos registrados com Ivacaftor em artrite reumatoide como indicação primária.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/) | 2017 | Estudo Animal/Mecanístico | *Gastroenterology* | Restauração da atividade CFTR em ductos de glândulas salivares e pancreáticas de camundongos resgata a função acinar e reduz a inflamação em modelos de síndrome de Sjögren e pancreatite autoimune. Demonstra que CFTR tem papel na modulação inflamatória de tecidos exócrinos com componente autoimune — suporte mecanístico indireto para a hipótese em AR. |

> ⚠️ **Nota:** O único artigo identificado é um estudo animal em modelos de doença autoimune de glândulas exócrinas (Sjögren), não em artrite reumatoide. A relevância para AR é tangencial.

---

## Informações de Comercialização no Brasil

Ivacaftor possui **7 registros** ativos no mercado brasileiro. As informações detalhadas de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack — os campos de licença retornaram vazios na consulta regulatória.

> Para detalhes completos dos registros, consulte diretamente a base de dados da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para Ivacaftor em artrite reumatoide limitam-se a um ensaio observacional em FC (sem desfecho de AR) e um estudo animal em modelo de doença autoimune exócrina — ambos indiretamente relacionados. O nível de evidência L4 indica suporte apenas pré-clínico/mecanístico, insuficiente para justificar progressão clínica sem dados adicionais. A pontuação TxGNN elevada (96,97%) provavelmente reflete sobreposição topológica no grafo de conhecimento (nós imunológicos compartilhados), e não uma relação biológica direta validada.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA (mecanismo de ação) via DrugBank API — identificado como gap de alta prioridade (DG002)
- Recuperar bula completa da ANVISA para avaliação das advertências, contraindicações e interações medicamentosas (DG001 — classificado como bloqueante)
- Realizar revisão de literatura direcionada a CFTR + inflamação articular ou modelos murinos de artrite para validar a hipótese mecanística
- Identificar se há estudos translacionais ou biomarker studies usando moduladores CFTR em populações com doenças autoimunes sistêmicas (não apenas FC)
- Resgatar os detalhes dos 7 registros ANVISA (número, nome comercial, forma farmacêutica, indicação aprovada) para avaliação regulatória completa
---

