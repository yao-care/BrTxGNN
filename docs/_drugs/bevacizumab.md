---
layout: default
title: Bevacizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bevacizumab: nova indicação prevista, Neoplasia de Epiglote (Epiglottis Neoplasm) (nível de evidência L5). Indicação original: Câncer peritoneal, câncer de mama, câncer de ovário…"
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Bevacizumabe: De neoplasias do peritônio, mama e glioblastoma para neoplasia de epiglote

## Resumo em Uma Frase

Bevacizumabe é um anticorpo monoclonal anti-VEGF, originalmente associado ao tratamento de cânceres peritoneais, de ovário, de mama, de cólon metastático e de glioblastoma.
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia de Epiglote (Epiglottis Neoplasm)**,
mas até o momento **não há ensaios clínicos nem publicações** que apoiem diretamente esta indicação: a previsão se baseia apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer peritoneal, câncer de mama, câncer de ovário, glioblastoma e câncer de cólon metastático, entre outros (segundo o grafo de conhecimento; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Neoplasia de Epiglote (Epiglottis Neoplasm) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados para este relatório) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o bevacizumabe neutraliza o VEGF-A (fator de crescimento do endotélio vascular A), bloqueando a angiogênese que alimenta o crescimento tumoral.

As indicações originais (cânceres peritoneais, ovário, mama, cólon metastático e glioblastoma) são tumores sólidos que dependem de neovascularização. A neoplasia de epiglote, um tumor de cabeça e pescoço, também pode depender de angiogênese, o que torna plausível uma ação do fármaco.

Essa plausibilidade é apenas teórica. A pontuação elevada do TxGNN (99,90%) é uma previsão computacional e não substitui evidência clínica. A similaridade formal com as indicações originais ainda não foi avaliada.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

Atualmente não há literatura relacionada para esta indicação.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 22 interações, sendo as de gravidade **maior** com:
  - Deferiprona
  - Samário (153Sm) lexidronato
  - Panitumumabe
  - Sunitinibe
  - Talidomida
- Outras interações de gravidade **moderada** incluem bisfosfonatos (alendronato, risedronato, etidronato, ibandronato, pamidronato, tiludronato), fatores de crescimento hematopoiético (filgrastim, pegfilgrastim, sargramostim), palifermina, estrôncio-89, rádio-223, romosozumabe, idelalisibe e fosfato de sódio monobásico (P32).

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para neoplasia de epiglote está no nível L5, sustentada apenas pelo modelo, sem ensaios ou literatura. Além disso, o fármaco não possui registro comercializado no Brasil e faltam dados de bula.

**Para prosseguir, é necessário:**
- Realizar busca dirigida de evidências clínicas e da literatura sobre bevacizumabe em neoplasias de epiglote e de laringe/cabeça e pescoço
- Obter dados do mecanismo de ação a partir do DrugBank
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pré-requisito para a triagem de segurança
- Esclarecer a situação regulatória no Brasil (o fármaco consta como não comercializado nos dados compilados)
- Avaliar a similaridade com as indicações originais e a compatibilidade da via de administração

---

## Observações sobre Outras Indicações Previstas

Entre as demais indicações previstas, destaca-se:

- **Neoplasia cística (Cystic Neoplasm)**: nível L1, mas apenas para o subconjunto de câncer de ovário (ensaio de Fase 3 NCT00565851, n=1052). O mapeamento para "neoplasia cística" é indireto e o bevacizumabe já tem indicações ovarianas sobrepostas, portanto **não representa um sinal real de reposicionamento**.
- **Neuroblastoma cervical**: nível L3, com apenas ensaios genéricos de Fase 1/2 e um relato de caso em neuroblastoma olfatório; sem evidência direta de eficácia.
- As demais (tumor benigno de língua, testículo e paratestículo, hipofaringe, assoalho da boca, papiloma invertido da cavidade nasal, mesenquimoma e schwannoma do forame jugular) estão em L4–L5, com evidência indireta ou ausente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

