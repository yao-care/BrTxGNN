---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Usando o skill `txgnn-pipeline` para referência de contexto do projeto. O skill confirma que este é um relatório de avaliação clínica — procedendo à geração do relatório com base no Evidence Pack fornecido.

**Nota editorial**: O `predicted_indications[0]` (trigeminal nerve neoplasm, rank 1) foi explicitamente identificado no campo `repurposing_rationale` como confusão de modelo (nós vizinhos no grafo de conhecimento). Este relatório foca em `predicted_indications[1]` — **neuralgia do trigêmeo** (rank 2, L2, Proceed with Guardrails) — que apresenta evidência clínica real e justificativa mecanística fundamentada.

---

# Lamotrigine: Da Epilepsia à Neuralgia do Trigêmeo

## Resumo em Uma Frase

Lamotrigine é um anticonvulsivante estabelecido, utilizado no tratamento de epilepsia e transtorno bipolar, com mecanismo de ação baseado no bloqueio de canais de sódio voltagem-dependentes.
O modelo TxGNN prevê que pode ser eficaz para **Neuralgia do Trigêmeo (Trigeminal Neuralgia)**, com evidência de nível **L2** apoiada por **4 ensaios clínicos** e **19 publicações**.
A previsão é mecanisticamente sólida e reconhecida pelas Diretrizes da Academia Europeia de Neurologia (EAN) de 2019, que já listam a lamotrigina como terapia de segunda linha para esta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Epilepsia / Transtorno Bipolar |
| Nova Indicação Prevista | Neuralgia do Trigêmeo (Trigeminal Neuralgia) |
| Pontuação de Previsão TxGNN | 99.89% (Rank 2)¹ |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

> ¹ **Sobre o Rank 1 (Trigeminal Nerve Neoplasm, 99.97%):** Toda a literatura retornada para esta previsão refere-se à **neuralgia** do trigêmeo, não a neoplasias. A alta pontuação decorre de proximidade de nós no grafo de conhecimento entre entidades distintas — trata-se de confusão de modelo, não de evidência real. Este relatório foca na indicação de Rank 2, onde existe evidência clínica verificável.

---

## Por que Esta Previsão é Razoável?

Lamotrigine atua bloqueando **canais de sódio voltagem-dependentes (Nav1.3 / Nav1.7)**, estabilizando membranas neuronais hiperexcitáveis e suprimindo disparos ectópicos repetitivos. Este é precisamente o mesmo mecanismo da carbamazepina — o fármaco de primeira linha para neuralgia do trigêmeo. A sobreposição mecanística é direta: a neuralgia do trigêmeo é causada, em muitos casos, por compressão vascular da raiz do nervo com desmielinização focal, gerando transmissão axonal aberrante e descargas paroxísticas. Esse substrato fisiopatológico é idêntico ao alvo dos anticonvulsivantes com bloqueio de canal de sódio.

A relação entre a indicação original (epilepsia) e a nova indicação (neuralgia do trigêmeo) é, portanto, direta: ambas envolvem hiperexcitabilidade neuronal descontrolada mediada por canais de sódio. Não se trata de uma extrapolação especulativa, mas de uma extensão mecanisticamente lógica para um tecido nervoso periférico diferente — o ramo do nervo trigêmeo — onde o mesmo mecanismo opera de forma patológica.

O reconhecimento clínico desta relação já está consolidado: as **Diretrizes EAN 2019** listam explicitamente a lamotrigina como terapia de segunda linha para neuralgia do trigêmeo, e múltiplos estudos comparativos com carbamazepina foram conduzidos, validando a previsão do modelo TxGNN com evidência do mundo real.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Concluído | 21 | Comparação direta de lamotrigina vs. carbamazepina para neuralgia do trigêmeo — único RCT de Phase 2/3 disponível; amostra pequena (n=21) limita poder estatístico, mas constitui a evidência direta mais robusta |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Concluído | 20 | Estudo duplo-cego, controlado por placebo, como terapia adjuvante de lamotrigina (Lamictal) para neuralgia do trigêmeo — design exploratório |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Concluído | 6 | Avaliação dos efeitos da lamotrigina sobre dor facial neuropática (incluindo neuralgia do trigêmeo) por fMRI — fornece suporte mecanístico e neuroimagiológico |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Desconhecido | 132 | Comparação carbamazepina vs. oxcarbazepina na neuralgia do trigêmeo — referência indireta que contextualiza o ecossistema farmacológico da indicação; lamotrigina não testada diretamente |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Diretriz Clínica | European Journal of Neurology | Diretriz oficial da EAN para manejo da neuralgia do trigêmeo — reconhece lamotrigina como terapia alternativa de segunda linha |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Revisão Sistemática | Biomedicines | Umbrella review de ensaios clínicos randomizados sobre tratamentos farmacológicos para neuralgia do trigêmeo — avalia eficácia e efeitos adversos comparativos |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Revisão | Practical Neurology | Guia prático de neuralgia do trigêmeo com novos critérios diagnósticos e tomada de decisão terapêutica médica e cirúrgica |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Revisão | Molecular Pain | Revisão completa da fisiopatologia (trigeminotalâmica, gangliônica) aos tratamentos farmacológicos — inclui lamotrigina no contexto clínico |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revisão | Expert Review of Neurotherapeutics | Atualização sobre farmacoterapia para neuralgia do trigêmeo: limitações da carbamazepina, papel dos anticonvulsivantes de terceira geração e novos agentes adjuvantes |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Estudo Clínico | Journal of the Chinese Medical Association | Avaliação direta de eficácia e segurança de lamotrigina vs. carbamazepina em pacientes com neuralgia do trigêmeo |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Relato de Caso | Multiple Sclerosis and Related Disorders | Neuralgia do trigêmeo refratária tratada com sucesso com combinação pregabalina + lamotrigina em paciente com esclerose múltipla — suporte clínico para uso adjuvante |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Coorte | Pain | Estudo de trajetória de doença com 7,2 milhões de indivíduos (Registro Nacional Dinamarquês) — identifica comorbidades temporalmente associadas à neuralgia do trigêmeo |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Revisão | BMJ Clinical Evidence | Revisão de evidências clínicas sobre diagnóstico, epidemiologia e comparação de opções terapêuticas para neuralgia do trigêmeo |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Revisão | Asian Journal of Neurosurgery | Revisão sobre mecanismos periféricos e centrais, diagnóstico diferencial e opções farmacológicas e cirúrgicas para neuralgia do trigêmeo |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A lamotrigina possui mecanismo de ação diretamente aplicável à neuralgia do trigêmeo, conta com endosso explícito nas Diretrizes EAN 2019 como terapia de segunda linha, e há um RCT de Phase 2/3 concluído (NCT00913107) comparando diretamente lamotrigina vs. carbamazepina. O principal limitante é o tamanho amostral pequeno dos ensaios existentes (n=21) e a ausência de registro no mercado brasileiro.

**Para prosseguir, é necessário:**
- Obter dados completos de segurança da bula (advertências, contraindicações e interações medicamentosas — todos os campos ausentes nesta versão do Evidence Pack)
- Avaliar processo de registro na ANVISA ou via importação por uso compassivo, dado que o produto não está comercializado no Brasil
- Atenção especial ao risco de **Síndrome de Stevens-Johnson / necrólise epidérmica tóxica** — efeito adverso grave conhecido da lamotrigina que requer titulação gradual e monitoramento cuidadoso
- Conduzir ou aguardar RCTs de maior escala (atualmente n=21 é insuficiente para aprovação regulatória da nova indicação)
- As demais previsões do TxGNN neste bundle (startle epilepsy, audiogenic seizures, reading seizures) apresentam evidência entre L3–L4 com base apenas em estudos pré-clínicos ou séries de casos — recomenda-se reavaliação após obtenção de dados de segurança completos
---

