---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 6
---

# Iron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# IRON (Ferro): Da Anemia Ferropriva à Síndrome de Plummer-Vinson

## Resumo em Uma Frase

O ferro (IRON, DrugBank DB01592) é um micronutriente essencial amplamente comercializado no Brasil, cujo uso primário reconhecido é a correção da anemia por deficiência de ferro e estados de carência nutricional.
O modelo TxGNN identifica a **Síndrome de Plummer-Vinson (Plummer-Vinson Syndrome)** como a candidata com maior respaldo clínico-literário entre as 6 indicações previstas, com **0 ensaios clínicos dedicados** e **19 publicações científicas** confirmando que a suplementação de ferro é o pilar terapêutico desta síndrome rara — na prática, um uso padrão já estabelecido ainda não formalizado como indicação aprovada no DrugBank.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anemia por deficiência de ferro / suplementação nutricional |
| Nova Indicação Prevista | Síndrome de Plummer-Vinson (Plummer-Vinson Syndrome) |
| Pontuação de Previsão TxGNN | 99,89% (rank 2 entre todas as doenças modeladas) |
| Nível de Evidência | L3 (revisões sistemáticas e séries de casos) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

> **Nota sobre este relatório:** Este Evidence Pack é do tipo *multi-indication* (6 indicações previstas). O rank 1 ("anemia megaloblástica constitucional independente de B12/folato") recebeu recomendação **Hold** por ausência de evidências e provável falso positivo por proximidade semântica. O foco principal deste relatório é o rank 2 (Síndrome de Plummer-Vinson), candidata com maior relevância clínica e evidência real.

---

## Por que Esta Previsão é Razoável?

A Síndrome de Plummer-Vinson (PVS) — também conhecida como Paterson-Brown Kelly syndrome — é uma condição rara definida pela tríade clássica: **anemia por deficiência de ferro**, **disfagia** e **webs esofágicos cervicais**. A relação entre ferro e PVS não é uma analogia funcional: é uma **relação causal direta**. A depleção crônica de ferro compromete simultaneamente a produção de hemoglobina, a função de enzimas musculares ferro-dependentes (como a citocromo C oxidase) e a integridade da mucosa esofágica, levando à formação das membranas características. A suplementação de ferro restaura os estoques corporais, reverte a anemia e, em muitos casos, permite a regressão parcial ou completa dos webs — sendo a dilatação endoscópica reservada para disfagia refratária.

Em termos patofisiológicos, a PVS e a anemia ferropriva grave são essencialmente expressões do mesmo estado deficitário, diferindo na extensão das manifestações tecido-específicas. O score TxGNN de 99,89% reflete essa proximidade mecânica genuína, e não uma associação semântica superficial. Esta previsão é, portanto, classificada como **uso padrão clinicamente reconhecido** mas ainda não formalizado como indicação aprovada no DrugBank.

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) disponíveis no Evidence Pack (lacuna DG002 — severidade Alta). Por literatura geral, o ferro atua como cofator essencial para hemoglobina, mioglobina, enzimas do ciclo de Krebs (aconitase, succinato desidrogenase) e proteínas citocromo-dependentes, todas relevantes à fisiopatologia da PVS.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos registrados especificamente para o uso de ferro no tratamento da Síndrome de Plummer-Vinson.

> A ausência de ensaios clínicos dedicados é esperada para uma indicação de uso padrão estabelecido há décadas. A evidência acumulada provém de revisões consistentes e séries de casos publicadas ao longo de mais de 30 anos.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Narrative Review | Journal of Blood Medicine | PVS: tríade clássica, suplementação de ferro como tratamento central; revisão de epidemiologia e declínio da prevalência com melhora nutricional |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet Journal of Rare Diseases | Revisão abrangente de PVS: suplementação de ferro reverte anemia e pode resolver os webs esofágicos; dilatação reservada para disfagia residual |
| [38871147](https://pubmed.ncbi.nlm.nih.gov/38871147/) | 2024 | Review | Clinical Gastroenterology and Hepatology | Revisão atual da tríade PVS; papel central do ferro no manejo clínico; vigilância endoscópica pelo risco de carcinoma |
| [31208220](https://pubmed.ncbi.nlm.nih.gov/31208220/) | 2019 | Review | Ear, Nose & Throat Journal | Revisão de PVS; reposição de ferro como tratamento de primeira linha para anemia e possível regressão dos webs |
| [20890819](https://pubmed.ncbi.nlm.nih.gov/20890819/) | 2010 | Review | La Tunisie Médicale | PVS como condição rara em mulheres; ferro como eixo terapêutico principal da síndrome |
| [31417270](https://pubmed.ncbi.nlm.nih.gov/31417270/) | 2019 | Review | Journal of Multidisciplinary Healthcare | Abordagem multidisciplinar em PVS; ferro como pilar do manejo; risco de malignidade exige vigilância endoscópica de longo prazo |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Case Series | Diseases of the Esophagus | Dois casos de PVS tratados com suplementação de ferro resultando em eliminação completa dos sintomas |
| [34651287](https://pubmed.ncbi.nlm.nih.gov/34651287/) | 2022 | Case-based Review | Immunologic Research | PVS associada à Síndrome de Sjögren primária; ferro como tratamento da anemia subjacente comum às duas condições |
| [39760192](https://pubmed.ncbi.nlm.nih.gov/39760192/) | 2025 | Systematic Review | Oral Diseases | Manifestações de câncer de cabeça e pescoço em pacientes com PVS; ferro como base do manejo da síndrome subjacente |
| [7865729](https://pubmed.ncbi.nlm.nih.gov/7865729/) | 1994 | Historical Review | Journal of Gastroenterology and Hepatology | Análise histórica do declínio da incidência de PVS, atribuído à melhora nutricional e suplementação de ferro em populações de risco |

---

## Informações de Comercialização no Brasil

O IRON (DB01592) possui **20 registros** ativos com status **Comercializado** no Brasil. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack — os campos de licença constam em branco na fonte consultada. Recomenda-se consulta direta ao portal da ANVISA para obtenção dos dados completos.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A Síndrome de Plummer-Vinson é patofisiologicamente inseparável da deficiência de ferro, e a suplementação de ferro é reconhecida de forma unânime na literatura como tratamento de primeira linha desta síndrome. A evidência é consistente em revisões e séries de casos publicadas entre 1994 e 2026, e o produto já está comercializado no Brasil com 20 registros ANVISA, dispensando nova aprovação regulatória para a indicação subjacente de deficiência de ferro.

**Para prosseguir, é necessário:**
- Completar os dados de licença ANVISA (detalhes dos 20 registros) para verificar se alguma apresentação já contempla indicação explícita para PVS ou disfagia ferropriva
- Obter MOA detalhado no DrugBank (lacuna DG002 — severidade Alta)
- Obter advertências e contraindicações da bula (lacuna DG001 — severidade Bloqueante), em especial para risco de sobrecarga de ferro (hemocromatose, hemossiderose) e uso em populações especiais
- Avaliar a indicação secundária de **Distúrbio por Deficiência de Vitaminas** (rank 5, nível de evidência L2, com ensaio Phase 3 concluído — NCT01198574), que também recebeu recomendação "Proceed with Guardrails" e pode ser desenvolvida em relatório próprio
---

