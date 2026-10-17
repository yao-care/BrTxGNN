---
layout: default
title: Tenecteplase
parent: Apenas Predição do Modelo (L5)
nav_order: 610
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tenecteplase: nova indicação prevista, Infarto do miocárdio posteroinferior (posteroinferior myocardial infa… (nível de evidência L5). Indicação original: Infarto do miocárdio, trombose coronariana"
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
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

# Tenecteplase: Do infarto agudo do miocárdio ao infarto do miocárdio posteroinferior

## Resumo em Uma Frase

Tenecteplase é um ativador do plasminogênio tecidual, específico para fibrina, originalmente associado ao tratamento do infarto do miocárdio e da trombose coronariana.
O modelo TxGNN prevê que pode ser eficaz para **infarto do miocárdio posteroinferior (posteroinferior myocardial infarction)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta previsão específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infarto do miocárdio, trombose coronariana (conforme o grafo de conhecimento TxGNN; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Infarto do miocárdio posteroinferior (posteroinferior myocardial infarction) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados nos dados compilados. Segundo informações conhecidas, a tenecteplase é um ativador do plasminogênio tecidual específico para fibrina, que dissolve trombos coronarianos. Sua eficácia no infarto do miocárdio já é estabelecida, e mecanisticamente pode ser aplicável a subtipos anatômicos dessa doença.

O infarto posteroinferior é um subtipo anatômico do infarto agudo do miocárdio, que já é uma indicação original do fármaco. A previsão, portanto, parece refletir a proximidade com a indicação-mãe no grafo de conhecimento, e não uma nova evidência. Em outras palavras, o potencial de reposicionamento é limitado: trata-se mais de uma extensão natural da indicação existente do que de um uso verdadeiramente novo.

Outras previsões do modelo seguem a mesma lógica (infarto posterolateral e septal). Já as previsões para doenças como deleção parcial do braço curto do cromossomo 16, anemias hemolíticas hereditárias e deficiência de piruvato quinase não têm vínculo mecanístico plausível com a fibrinólise e provavelmente são artefatos do grafo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (infarto posteroinferior).

Como referência, as publicações recuperadas para previsões vizinhas (infarto septal e estenose coronariana) são apenas indiretamente relevantes. Destacam-se:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Estudo randomizado de viabilidade/segurança (40 pacientes) | Am J Cardiol | Tenecteplase intracoronária em baixa dose (4 mg) durante ICP primária no IAMCSST: viabilidade e segurança avaliadas contra solução salina |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | Estudo comparativo | J Am Coll Cardiol | Angioplastia facilitada por tenecteplase vs. tenecteplase isolada em IAMCSST de alto risco (CAPITAL AMI) |
| [17102829](https://pubmed.ncbi.nlm.nih.gov/17102829/) | 2006 | Estudo piloto de viabilidade | Can J Cardiol | Transferência para ICP urgente após trombólise no IAMCSST (TRANSFER-AMI) |
| [23975441](https://pubmed.ncbi.nlm.nih.gov/23975441/) | 2014 | Série clínica | J Thromb Thrombolysis | Eficácia e segurança da tenecteplase ajustada ao peso em 30 pacientes com embolia pulmonar aguda |
| [18183355](https://pubmed.ncbi.nlm.nih.gov/18183355/) | 2009 | Relato de caso | J Thromb Thrombolysis | Embolia pulmonar maciça que simulava infarto septal, tratada com tenecteplase |
| [42220791](https://pubmed.ncbi.nlm.nih.gov/42220791/) | 2026 | Relato de caso | Cureus | Ruptura do septo ventricular após reperfusão fármaco-invasiva com tenecteplase em IAMCSST anterior |

Nenhuma delas fornece evidência direta de eficácia para o infarto posteroinferior como indicação distinta.

## Considerações de Segurança

- **Interações Medicamentosas** (100 interações registradas; principais exemplos):
  - **Gravidade maior**: abciximabe, apixabana, acalabrutinibe, avapritinibe, betrixabana, deferasirox, ibritumomabe tiuxetana, tositumomabe. A maioria envolve aumento do risco de sangramento com anticoagulantes, antiagregantes e outros fármacos que afetam a hemostasia.
  - **Gravidade moderada**: ácido acetilsalicílico, ibuprofeno, cetorolaco, celecoxibe, diclofenaco tópico, ácido aminocaproico, ácidos graxos ômega-3, fenfluramina, dexfenfluramina e sibutramina.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal é um subtipo anatômico de uma indicação já existente (infarto do miocárdio), sem ensaios clínicos nem publicações específicas; o nível de evidência é L5 e a pontuação alta do modelo não é respaldada por dados reais. O fármaco não possui registro comercializado no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) detalhados a partir do DrugBank
- Bula da ANVISA com advertências e contraindicações, hoje indisponível e que bloqueia a triagem de segurança
- Esclarecer a situação regulatória no Brasil (não há registros vigentes)
- Evidências clínicas específicas para o infarto posteroinferior, ou confirmação de que a indicação já está coberta pela indicação geral de infarto do miocárdio
- Entre as demais previsões, apenas a estenose coronariana (nível L3, estudo de viabilidade de tenecteplase intracoronária) justifica uma questão de pesquisa; as previsões de doenças hematológicas e cromossômicas devem ser descartadas como provável artefato do grafo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

