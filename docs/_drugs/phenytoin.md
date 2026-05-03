---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

Usando o skill `txgnn-pipeline` como referência e seguindo o formato do prompt v5, vou gerar o relatório baseado no Evidence Pack fornecido.

**Nota editorial:** A indicação de rank 1 (neoplasia do nervo trigêmeo) foi identificada pelo próprio `repurposing_rationale` como artefato do modelo. O relatório foca na indicação de maior suporte clínico (**rank 9 — nevralgia do trigêmeo, L3, Proceed with Guardrails**), com transparência completa sobre o ranking bruto do TxGNN.

---

# Phenytoin: De Epilepsia para Nevralgia do Trigêmeo

## Resumo em Uma Frase

Phenytoin (fenitoína) é um anticonvulsivante clássico utilizado no tratamento de epilepsia e convulsões tônico-clônicas. O modelo TxGNN identifica a **Nevralgia do Trigêmeo (Trigeminal Neuralgia)** como a indicação com maior suporte clínico para reposicionamento (escore TxGNN 99.97%, rank 9), atualmente com **1 ensaio clínico prospectivo** e **19 publicações** apoiando esta direção. A indicação de maior escore bruto — neoplasia do nervo trigêmeo (rank 1, 99.99%) — foi identificada como artefato de confusão terminológica no modelo e não apresenta evidências clínicas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Epilepsia / Convulsões |
| Nova Indicação Prevista | Nevralgia do Trigêmeo (Trigeminal Neuralgia) |
| Pontuação de Previsão TxGNN | 99.97% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Phenytoin atua como bloqueador de canais de sódio dependentes de voltagem (Nav), estabilizando neurônios na fase de inativação prolongada e suprimindo descargas repetitivas de alta frequência. Este mecanismo é diretamente relevante à fisiopatologia da nevralgia do trigêmeo: a condição decorre de desmielinização focal da raiz do nervo trigêmeo, gerando descargas ectópicas paroxísticas nos neurônios sensoriais trigeminais. O bloqueio Nav pela fenitoína suprime essas descargas de forma análoga à carbamazepina — o fármaco de primeira linha consagrado para esta indicação.

A via intravenosa de Phenytoin ganhou uso clínico estabelecido em crises agudas de nevralgia do trigêmeo, preenchendo uma lacuna terapêutica real: quando a dor intensa impede a alimentação oral, os fármacos de primeira linha tornam-se inacessíveis, e a fenitoína IV funciona como opção de resgate hospitalar. Estudos comparativos recentes avaliaram diretamente sua eficácia frente à lacosamida IV neste contexto.

> **Nota sobre o Rank 1 do TxGNN:** A indicação "neoplasia do nervo trigêmeo" recebeu escore 99.99% (rank 1), porém é interpretada como artefato de confusão terminológica entre "neuralgia" e "neoplasm" no grafo de conhecimento. Phenytoin não possui mecanismo antitumoral conhecido, e o bloqueio de Nav não demonstra efeito sobre proliferação ou progressão tumoral. Esta previsão não representa oportunidade terapêutica real — **decisão: Hold**.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Concluído | 15 | Estudo prospectivo sistemático de Phenytoin IV para exacerbações agudas de nevralgia do trigêmeo; avalia viabilidade como alternativa de resgate quando o tratamento oral está comprometido pela intensidade da dor e incapacidade de deglutição |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Diretriz Clínica | Eur J Neurology | Diretrizes da Academia Europeia de Neurologia para nevralgia do trigêmeo; define padrão de manejo farmacológico e inclui opções de resgate IV |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Observacional Comparativo | Cephalalgia | Lacosamida vs Phenytoin IV em 144 casos de nevralgia do trigêmeo aguda; análise descritiva de eficácia e segurança comparativas — maior série publicada para Phenytoin IV nesta indicação |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Série de Casos | Headache | Phenytoin IV como resgate em crise de nevralgia do trigêmeo; coorte retrospectiva com análise de resposta analgésica |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Revisão Narrativa | Molecular Pain | Revisão abrangente de fisiopatologia e farmacoterapia da nevralgia do trigêmeo; descreve o papel do bloqueio Nav no contexto do tratamento |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Research | Análise crítica comparando Phenytoin vs Carbamazepina na nevralgia do trigêmeo: tratamento baseado em marketing versus evidências; questiona a posição secundária do Phenytoin |
| [39993829](https://pubmed.ncbi.nlm.nih.gov/39993829/) | 2024 | Review | Clin Med Research | Manejo hospitalar de crises agudas de nevralgia do trigêmeo; Phenytoin IV posicionado no protocolo de resgate com orientações práticas |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Revisão Sistemática | BMJ Clinical Evidence | Revisão de evidências para tratamentos da nevralgia do trigêmeo; análise comparativa de intervenções médicas e cirúrgicas, incluindo anticonvulsivantes |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurologic Clinics | Nevralgia do trigêmeo e glossofaríngea; anticonvulsivantes como agentes mais eficazes — discute papel histórico e atual do Phenytoin |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Anticonvulsivantes no manejo de cefaleia em salvas e nevralgia do trigêmeo; contextualiza Phenytoin no arsenal terapêutico |
| [6487105](https://pubmed.ncbi.nlm.nih.gov/6487105/) | 1984 | Review | Arch Neurology | Etiologia e patogênese da nevralgia do trigêmeo; mecanismo periférico/central dos fármacos eficazes — referência seminal que contextualiza o uso de Phenytoin |

---

## Informações de Comercialização no Brasil

Phenytoin **não possui registro ativo na ANVISA** e não é comercializado no Brasil. Esta é uma barreira regulatória significativa para qualquer estratégia de uso clínico nacional — qualquer iniciativa requer processo de registro ou importação excepcional.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe suporte clínico de nível L3 — diretriz europeia de neurologia e estudo observacional comparativo com 144 casos — para o uso de Phenytoin IV como resgate em crises agudas de nevralgia do trigêmeo. O mecanismo de bloqueio Nav é fisiopatologicamente direto e análogo à carbamazepina de primeira linha, e há precedente de uso clínico estabelecido internacionalmente.

**Para prosseguir, é necessário:**
- **Barreira regulatória:** Phenytoin não possui registro na ANVISA — avaliar viabilidade de registro específico ou importação excepcional para uso hospitalar
- **Lacunas de segurança:** Obter advertências e contraindicações completas da bula (gap DG001) e mecanismo de ação detalhado do DrugBank (gap DG002)
- **Evidência clínica:** Conduzir ensaio clínico randomizado controlado comparando Phenytoin IV vs lacosamida IV em crises agudas de nevralgia do trigêmeo
- **Monitoramento:** Definir protocolo de monitoramento de concentração sérica (janela terapêutica estreita: 10–20 µg/mL) e protocolo de infusão IV segura (risco de arritmia e hipotensão com infusão rápida)
- **Interações:** Mapear DDIs relevantes para a população-alvo, frequentemente em polifarmácia
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

