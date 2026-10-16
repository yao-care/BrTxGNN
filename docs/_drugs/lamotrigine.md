---
layout: default
title: Lamotrigine
parent: Evidência Alta (L1-L2)
nav_order: 388
evidence_level: L2
indication_count: 9
last_modified_at: 2026-10-13
description: "Lamotrigine: nova indicação prevista, Neuralgia do trigêmeo (Trigeminal Neuralgia) (nível de evidência L2). Indicação original: Anticonvulsivantes"
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "eating seizures", "startle epilepsy", "micturation-induced seizures", "orgasm-induced seizures", "audiogenic seizures", "thinking seizures", "reading seizures"]
---

# Lamotrigine
{: .fs-9 }

Nível de evidência: **L2** | Indicações previstas: **9** 
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

# Lamotrigina: De anticonvulsivante a neuralgia do trigêmeo

## Resumo em Uma Frase

Lamotrigina é um medicamento antiepiléptico (anticonvulsivante), registrado originalmente na ANVISA nas categorias "anticonvulsivantes" e "outros psicolépticos".
O modelo TxGNN prevê que pode ser eficaz para a **neuralgia do trigêmeo (Trigeminal Neuralgia)**, atualmente com **2 ensaios clínicos** e **18 publicações** apoiando esta direção.

Observação: a previsão de maior pontuação do modelo foi "neoplasia do nervo trigêmeo", mas as evidências recuperadas tratam de neuralgia do trigêmeo, e não de tratamento de tumor. Por isso, este relatório avalia a segunda previsão (neuralgia do trigêmeo), que é a mais bem sustentada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticonvulsivantes |
| Nova Indicação Prevista | Neuralgia do trigêmeo (Trigeminal Neuralgia) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Proceed with Guardrails |

A previsão de topo do modelo (neoplasia do nervo trigêmeo, 99,97%) tem apenas evidência L5 e recomendação "Hold": a pontuação alta parece refletir a proximidade no grafo com a neuralgia do trigêmeo, e não um efeito antitumoral.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a lamotrigina bloqueia canais de sódio dependentes de voltagem e inibe a liberação de glutamato, e sua eficácia como anticonvulsivante está estabelecida.

A neuralgia do trigêmeo é uma dor facial paroxística, associada a desmielinização focal e descargas neurais aberrantes. Esse mecanismo é o mesmo alvo dos fármacos de primeira linha, carbamazepina e oxcarbazepina, que também são antiepilépticos bloqueadores de canais de sódio. Assim, é coerente que um anticonvulsivante com ação semelhante possa aliviar as crises.

A diretriz da Academia Europeia de Neurologia e diversas revisões citam a lamotrigina como opção adjuvante ou de segunda linha. Os dados diretos de ensaios, porém, são pequenos.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Concluído | 21 | Comparação direta de eficácia e segurança da lamotrigina com a carbamazepina na neuralgia do trigêmeo; amostra muito pequena |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Sem fase formal (NA) | Concluído | 20 | Estudo adjuvante duplo-cego controlado por placebo (Lamictal) em neuralgia do trigêmeo, avaliando redução das crises e segurança |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Diretriz | Eur J Neurol | Diretriz da Academia Europeia de Neurologia para o manejo da neuralgia do trigêmeo |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Revisão sistemática | Biomedicines | Revisão guarda-chuva sobre eficácia e efeitos adversos dos fármacos usados na neuralgia do trigêmeo |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revisão | Expert Rev Neurother | Atualização da farmacoterapia: carbamazepina e oxcarbazepina são eficazes, mas com efeitos adversos limitantes; anticonvulsivantes de terceira geração são opções promissoras |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Revisão | Pract Neurol | Guia prático com novos critérios diagnósticos e decisões de tratamento clínico e cirúrgico |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Revisão | Mol Pain | Visão geral da fisiopatologia e dos tratamentos farmacológicos |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Revisão | Drugs | Opções farmacológicas atuais e inovadoras para neuralgia do trigêmeo típica e atípica |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Revisão | No Shinkei Geka | Carbamazepina como primeira linha; lamotrigina, baclofeno e outros são usados off-label no Japão e considerados eficazes |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Revisão | Headache | Uso de antiepilépticos no manejo da cefaleia em salvas e da neuralgia do trigêmeo |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Revisão | BMJ Clin Evid | Revisão clínica da neuralgia do trigêmeo e de suas opções de tratamento |
| [21493636](https://pubmed.ncbi.nlm.nih.gov/21493636/) | 2011 | Revisão | Postgrad Med J | Diagnóstico e manejo da neuralgia do trigêmeo |

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados; nenhum está vigente. Principais exemplos:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101070006 | Lamictal | Não informada | Anticonvulsivantes |
| Registro 146820082 | Lamosyn | Não informada | Anticonvulsivantes |
| Registro 100431059 | Léptico | Não informada | Anticonvulsivantes |
| Registro 109740271 | Forlut | Não informada | Anticonvulsivantes |
| Registro 156510087 | Nepil | Não informada | Anticonvulsivantes |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: o grafo associa a lamotrigina a doenças como transtornos de ansiedade, transtorno neurótico, distimia, doença hepática, doença da vesícula biliar, trombocitopenia, neutropenia, agranulocitose, anemias (incluindo macrocítica e aplástica), pancitopenia e meningite não infecciosa. Esses itens exigem confirmação na bula.
- **Interações medicamentosas**: foram identificadas 100 interações. Entre as de nível moderado estão morfina (inclusive lipossomal), ópio, dronabinol, nabilona, metoclopramida e orlistate. A interação com metformina é de nível leve. Há ainda vários itens de nível desconhecido (por exemplo, omeprazol, pantoprazol, lansoprazol, doxiciclina e vancomicina).

As advertências e contraindicações da bula não estão disponíveis nos dados compilados; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há dois ensaios clínicos concluídos em neuralgia do trigêmeo (um Phase 2/3 contra carbamazepina) e respaldo de diretrizes e revisões, mas ambos os ensaios são muito pequenos (n=21 e n=20) e não há Phase 3 confirmatório. Por isso o nível é L2, e não L1.
- Todos os registros brasileiros estão cancelados, o que exige verificação regulatória antes de qualquer avanço.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Esclarecer a situação regulatória no Brasil (registros cancelados) e a disponibilidade de produto com registro vigente.
- Planejar um ensaio de confirmação com amostra maior, ou revisão sistemática dos dados existentes.
- Definir plano de monitoramento hematológico, hepático e cutâneo, dado o perfil de risco apontado pelo grafo.

Previsões adicionais de menor evidência (todas "Hold", exceto a epilepsia por sobressalto, classificada como questão de pesquisa): epilepsia por sobressalto (relatos de casos favoráveis à lamotrigina), crises audiogênicas (apenas modelos animais), crises alimentares, crises induzidas por micção, por orgasmo, por pensamento e por leitura (sem evidência direta).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

