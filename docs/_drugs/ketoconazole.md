---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

A skill txgnn-pipeline não tem orientações específicas para geração de relatórios — prossigo diretamente com base nas instruções do sistema.

---

# Cetoconazol: Do tratamento antifúngico à acne

## Resumo em Uma Frase

Cetoconazol é um antifúngico azólico de amplo espectro, originalmente utilizado no tratamento de infecções fúngicas sistêmicas e superficiais.
O modelo TxGNN prevê que pode ser eficaz para **Acne (acne disease)**,
atualmente com **1 ensaio clínico** e **15 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção fúngica (antifúngico de amplo espectro) |
| Nova Indicação Prevista | Acne (acne disease) |
| Pontuação de Previsão TxGNN | 99,80% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não registrado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento farmacológico estabelecido, o cetoconazol é um antifúngico da classe dos azóis que atua bloqueando a enzima CYP51 (lanosterol 14α-desmetilase), interrompendo a síntese de ergosterol e comprometendo a integridade da membrana celular fúngica. Adicionalmente, o cetoconazol exerce ação antiandrogênica por inibição das enzimas CYP17A1 e CYP11A1, reduzindo a biossíntese de andrógenos adrenais e gonadais.

Para a acne, dois mecanismos independentes e biologicamente plausíveis sustentam a previsão: **(1) ação antifúngica** direcionada a *Malassezia spp.*, fungo lipofílico colonizador dos folículos sebáceos capaz de induzir e agravar inflamação na acne vulgaris e na foliculite por Pityrosporum — condição frequentemente confundida com acne bacteriana; e **(2) ação antiandrogênica**, que reduz a produção de sebo ao suprimir a síntese de andrógenos, abordando diretamente o mecanismo central da acne hormonal.

A formulação tópica a 2% é clinicamente estratégica: minimiza a absorção sistêmica e contorna o principal risco associado à via oral (hepatotoxicidade grave, que levou à restrição ou retirada do cetoconazol sistêmico do mercado nos EUA e na UE), mantendo concentração farmacológica ativa no nível das glândulas sebáceas e folículos pilosos — exatamente o sítio de ação relevante para a acne.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | N/A | Ativo (sem novas inclusões) | 52 | Ensaio randomizado controlado comparando cetoconazol tópico 2% vs. adapaleno 2% para acne comedonal e papulopustular leve (12 semanas). Objetivo: avaliar se cetoconazol pode ser alternativa ao retinoide tópico com menos efeitos adversos. Sem resultados publicados até o momento. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Estudo in vitro | Microbiology and Immunology | Cetoconazol inibiu a atividade da lipase de *P. acnes*, enzima que metaboliza o sebo e desencadeia inflamação cutânea; resultado apoia mecanismo anti-acne direto independente da ação antifúngica clássica. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudo in vitro | Biological & Pharmaceutical Bulletin | Azóis, incluindo cetoconazol, demonstraram atividade in vitro contra *P. acnes*, sendo relevantes para cepas resistentes a antibióticos convencionais como tetraciclina e macrolídeos. |
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | RCT | Pituitary | Levocetoconazol (enantiômero S do cetoconazol) demonstrou eficácia clínica no hipercortisolismo da Síndrome de Cushing no estudo de Fase 3 SONICS, confirmando a potente ação inibitória da classe sobre a esteroidogênese adrenal (CYP17A1/CYP11A1). |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | Keio Journal of Medicine | Revisão de doenças cutâneas associadas a *Malassezia/Pityrosporum*, incluindo ptiríase versicolor, foliculite e dermatite seborreica; cetoconazol apresentado como principal agente terapêutico eficaz. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Série de Casos | Clinical and Experimental Dermatology | Avaliação de 62 casos de foliculite por *Pityrosporum* frequentemente confundida com acne vulgaris na prática clínica; cetoconazol demonstrou eficácia terapêutica nessa condição clinicamente similar à acne. |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | Revisão abrangente de tratamentos sistêmicos para acne moderada a grave; antiandrogênios (incluindo inibidores de CYP) mencionados como alternativas relevantes na acne hormonal e resistente a antibióticos. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | BMJ Clinical Evidence | Revisão de SOP para PCOS, condição associada a hiperandrogenismo, acne e hirsutismo; fundamenta o uso de antiandrogênios (incluindo cetoconazol) no manejo da acne de etiologia hormonal. |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Estudo Clínico | Polski Tygodnik Lekarski | Terapia das manifestações hiperandrogênicas em PCOS com antiandrogênios produziu redução de acne, hirsutismo e seborreia em 3 meses, reforçando o papel da via androgênica na patogênese da acne. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Série de Casos | Archives of Dermatology | Pústulas neonatais associadas a *Malassezia furfur* foram confundidas com acne neonatal; tratamento com cetoconazol mostrou-se eficaz, documentando ação terapêutica cutânea direta do fármaco. |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | Pharmaceuticals (Basel) | Revisão do potencial terapêutico do adapaleno — medicamento comparador no ensaio NCT07237763 —, incluindo seu mecanismo em acne vulgaris; relevante para contextualizar o benchmark do estudo ativo. |

---

## Informações de Comercialização no Brasil

A busca na base regulatória brasileira não retornou registros de cetoconazol com os parâmetros utilizados (`total_licenses` = 0).

> **Nota:** O cetoconazol possui formulações tópicas (creme 2%, shampoo 2%) com ampla presença histórica no mercado brasileiro. Recomenda-se verificação direta no portal **ANVISA — Consulta de Medicamentos** (consultas.anvisa.gov.br) para confirmação atualizada dos registros vigentes, especialmente para formas farmacêuticas tópicas.

---

## Considerações de Segurança

Não há dados de advertências ou contraindicações disponíveis neste Evidence Pack.

> Consulte a bula para informações de segurança.

**Ponto de atenção relevante (identificado na literatura e no racional de reposicionamento):** O cetoconazol **sistêmico (oral)** apresenta risco significativo de hepatotoxicidade grave e idiossincrática, tendo sua indicação restringida ou suspensa em vários países para uso de primeira linha em infecções não invasivas. Para a indicação em acne, a via de administração deve ser **exclusivamente tópica** — a absorção sistêmica da formulação tópica 2% é mínima e o perfil de segurança é substancialmente mais favorável.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O cetoconazol tópico 2% possui mecanismo de ação duplo, biologicamente plausível e respaldado por estudos laboratoriais (inibição de lipase de *P. acnes*, atividade anti-*Pityrosporum*), revisões de literatura e um ensaio clínico randomizado ativo que o compara diretamente ao adapaleno. A ausência de resultados publicados do RCT e a falta de dados regulatórios brasileiros confirmados impedem uma recomendação "Go" neste momento.

**Para prosseguir, é necessário:**
- Aguardar publicação dos resultados do ensaio **NCT07237763** (comparação direta cetoconazol 2% vs. adapaleno 2%)
- Confirmar registros atualizados na **ANVISA** para formulações tópicas de cetoconazol já comercializadas no Brasil
- Definir explicitamente que a via de administração é **exclusivamente tópica** — o uso oral não deve ser considerado para esta indicação dermatológica
- Obter dados completos de MOA do DrugBank (remediar Data Gap DG002) para análise mecanística formal
- Obter dados de advertências e contraindicações do rótulo brasileiro (remediar Data Gap DG001) para avaliação de segurança completa (S1)
- Avaliar perfil de segurança da formulação tópica em populações específicas relevantes para acne (adolescentes, gestantes, lactantes)
---

