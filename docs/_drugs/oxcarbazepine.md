---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepina: Da Epilepsia Focal para a Epilepsia Visual

## Resumo em Uma Frase

Oxcarbazepina (OXC) é um antiepiléptico de segunda geração, amplamente utilizado no tratamento de crises epilépticas de início focal em adultos e crianças.
O modelo TxGNN prevê que pode ser eficaz para **Epilepsia Visual (Visual Epilepsy)**,
atualmente com **1 ensaio clínico** e **19 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia focal / crises de início parcial |
| Nova Indicação Prevista | Epilepsia Visual (Visual Epilepsy) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Não há dados formais de mecanismo de ação (MOA) disponíveis neste pacote de evidências. Com base na literatura estabelecida, a OXC é o análogo cetônico da carbamazepina: seu metabólito ativo, o 10-monoidroxi-carbamazepina (MHD), bloqueia canais de sódio voltagem-dependentes (Nav1.2/Nav1.6) de forma dependente do uso (*use-dependent blockade*). Ao se ligar preferencialmente aos canais no estado inativado — mais prevalentes em neurônios com alta frequência de disparo — o MHD estabiliza a membrana neuronal hiperexcitada sem comprometer a transmissão sináptica normal em condições fisiológicas.

A epilepsia visual (fotossensível ou sensível a padrões geométricos) resulta de descarga hipersíncrona do córtex visual occipital em resposta a estímulos visuais. Trata-se de um subtipo de epilepsia de início **focal**, com o foco epileptogênico localizado no lobo occipital. O mecanismo de bloqueio Nav da OXC é diretamente compatível com esse perfil: ao suprimir a hiperexcitabilidade neuronal do córtex occipital e inibir a propagação das descargas paroxísticas, a OXC pode interromper o ciclo de disparo desencadeado pelo estímulo visual.

Múltiplas revisões de Tier 1 publicadas em periódicos de alto impacto (JAMA, Continuum, Seizure) consolidam o papel da OXC no tratamento das epilepsias focais. Um estudo observacional prospectivo Phase 4 (LICEO Study, n=111) avaliou a eficácia da OXC como biterapia de primeira linha em pacientes com epilepsia focal na prática clínica real, fornecendo suporte indireto extrapolável ao subtipo de epilepsia visual, que compartilha a mesma base fisiopatológica focal. **Atenção importante**: a OXC não é indicada para epilepsias generalizadas idiopáticas (p. ex., epilepsia mioclônica juvenil — JME), sendo imprescindível confirmar o fenótipo focal antes do uso.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Concluído | 111 | LICEO Study: estudo prospectivo observacional avaliando a eficácia de novos AEDs (gabapentina, lamotrigina, levetiracetam, OXC, pregabalina, tiagabina e topiramato) como primeira biterapia em pacientes com epilepsia focal; fornece dados reais de eficácia da OXC como tratamento combinado de primeira linha |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | ECR Multicêntrico | CNS Neuroscience & Therapeutics | Comparação randomizada aberta de OXC vs levetiracetam em monoterapia para epilepsia focal recém-diagnosticada na China; avalia eficácia, qualidade de vida e saúde mental dos pacientes |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Revisão Narrativa | JAMA | Revisão abrangente de medicamentos anticrises para adultos com epilepsia (65 milhões de pessoas afetadas mundialmente); objetivo primário: eliminar crises minimizando efeitos adversos dos AEDs |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Revisão Narrativa | Continuum | Atualização 2025 sobre todos os AEDs disponíveis para neurologistas; cobre farmacocinética, indicações e estratégias de uso individualizadas para cada agente |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Revisão Narrativa | Seizure | Revisão específica sobre o papel atual de CBZ e OXC no manejo da epilepsia, contextualizada no cenário de >30 AEDs disponíveis introduzidos nos últimos 30 anos |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Revisão Narrativa | Continuum | Referência clínica abrangente sobre AEDs com foco em farmacocinética, espectro de eficácia e indicações individuais; base para tratamento otimizado da epilepsia |
| [19445769](https://pubmed.ncbi.nlm.nih.gov/19445769/) | 2009 | Revisão Narrativa | BMJ Clinical Evidence | Síntese de evidências clínicas em epilepsia; ~70% dos pacientes alcançam remissão com tratamento farmacológico adequado; ~3% da população receberá diagnóstico ao longo da vida |
| [27845825](https://pubmed.ncbi.nlm.nih.gov/27845825/) | 2016 | Revisão Sistemática | Cochrane Database Syst Rev | Revisão sistemática sobre OXC como terapia adjuvante em epilepsia parcial fármaco-resistente (até 30% dos pacientes); nota: revisão posteriormente retirada da Cochrane, dados históricos relevantes |
| [10530693](https://pubmed.ncbi.nlm.nih.gov/10530693/) | 1999 | Perfil Farmacológico | Epilepsia | Artigo seminal descrevendo OXC como análogo cetônico de CBZ com perfil farmacocinético superior e melhor tolerabilidade; estabelece base para uso em crises parciais e tônico-clônicas generalizadas |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Revisão | Pharmacogenomics | Variabilidade interpopulacional relevante na eficácia e segurança de OXC decorrente de polimorfismos em enzimas metabólicas, transportadores e receptores farmacodinâmicos |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revisão | Expert Review of Neurotherapeutics | Farmacoterapia da neuralgia do trigêmeo; confirma eficácia de OXC via bloqueio Nav — evidência indireta relevante para o mecanismo anticonvulsivante em condições de hiperexcitabilidade neuronal |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A epilepsia visual é um subtipo de epilepsia focal occipital mecanisticamente compatível com o perfil de bloqueio Nav use-dependent da OXC/MHD. O suporte combinado de um ECR multicêntrico em epilepsia focal (PMID 35429132), um estudo observacional Phase 4 em prática clínica real, múltiplas revisões Tier-1 de alto impacto e escore TxGNN de 99,95% justificam o avanço — desde que confirmado o fenótipo focal do paciente e obtidos dados formais de segurança.

**Para prosseguir, é necessário:**
- Obter dados de segurança completos (advertências, contraindicações e interações medicamentosas) da bula oficial via ANVISA / DrugBank API (DB00776)
- Confirmar o mecanismo de ação detalhado (MOA) via consulta formal ao DrugBank
- Verificar possível comercialização de OXC no Brasil sob nomes como Trileptal® junto ao Bulário Eletrônico da ANVISA
- Confirmar que os pacientes-alvo apresentam epilepsia de início **focal** — excluir obrigatoriamente epilepsias generalizadas idiopáticas (JME, epilepsia ausência), nas quais a OXC pode agravar crises
- Realizar busca sistemática de séries de casos e relatos clínicos específicos para epilepsia visual tratada com OXC, para complementar a evidência indireta atual
---

