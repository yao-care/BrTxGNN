---
layout: default
title: Tenecteplase
parent: Apenas Predição do Modelo (L5)
nav_order: 610
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
description: "Tenecteplase: nova indicação prevista, Congenital coronary artery anomaly (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Tenecteplase
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Resumo em Uma Frase

Tenecteplase é um ativador do plasminogênio tecidual, específico para fibrina, originalmente associado ao tratamento do infarto do miocárdio e da trombose coronariana.
O modelo TxGNN prevê que pode ser eficaz para **infarto do miocárdio posteroinferior (posteroinferior myocardial infarction)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta previsão específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Congenital coronary artery anomaly |
| Pontuação de Previsão TxGNN | 0.9961 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados nos dados compilados. Segundo informações conhecidas, a tenecteplase é um ativador do plasminogênio tecidual específico para fibrina, que dissolve trombos coronarianos. Sua eficácia no infarto do miocárdio já é estabelecida, e mecanisticamente pode ser aplicável a subtipos anatômicos dessa doença.


As previsões para doenças como deleção parcial do braço curto do cromossomo 16, anemias hemolíticas hereditárias e deficiência de piruvato quinase não têm vínculo mecanístico plausível com a fibrinólise. Os scores vêm do modelo TxGNN (deep learning) e podem refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica.

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
- Entre as demais previsões, apenas a estenose coronariana (nível L3, estudo de viabilidade de tenecteplase intracoronária) justifica uma questão de pesquisa; as previsões de doenças hematológicas e cromossômicas devem ser descartadas, pois os scores vêm do modelo TxGNN (deep learning) e podem refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

