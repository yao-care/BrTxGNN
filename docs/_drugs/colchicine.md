---
layout: default
title: Colchicine
parent: Apenas Predição do Modelo (L5)
nav_order: 241
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Colchicine: nova indicação prevista, Febre Familiar do Mediterrâneo… (nível de evidência L5). Indicação original: Antiinflamatórios antirreumáticos (e antigotosos)"
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

# Colchicina: De antiinflamatório/antigotoso para Febre Familiar do Mediterrâneo

## Resumo em Uma Frase

Colchicina é um fármaco originalmente classificado no Brasil como antiinflamatório antirreumático e antigotoso.
O modelo TxGNN prevê que pode ser eficaz para **Febre Familiar do Mediterrâneo, autossômica dominante (familial Mediterranean fever, autosomal dominant)**,
atualmente com **0 ensaios clínicos registrados** e **20 publicações** (em sua maioria revisões) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiinflamatórios antirreumáticos (e antigotosos) |
| Nova Indicação Prevista | Febre Familiar do Mediterrâneo, autossômica dominante (familial Mediterranean fever, autosomal dominant) |
| Pontuação de Previsão TxGNN | 99,38% |
| Nível de Evidência | L1 (atribuído com base em ensaios clássicos de fase 3 controlados por placebo, dos anos 1970-80, que não constam nos dados compilados e precisam ser verificados; pelos dados disponíveis, a evidência seria L3) |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 7 (todos cancelados) |
| Decisão Recomendada | Proceed with Guardrails |

> Observação: a indicação com maior pontuação TxGNN é a malária por *Plasmodium falciparum* (99,60%), mas ela tem apenas evidência L5 e racional fraco (Hold). Este relatório foca na Febre Familiar do Mediterrâneo, que tem a evidência mais robusta entre as três indicações previstas. A terceira indicação (dermatofibrossarcoma protuberans, 99,37%) também está em L5 e Hold.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação na base compilada. Segundo conhecimento estabelecido, a colchicina liga-se à tubulina e inibe a polimerização dos microtúbulos. Com isso, reduz a quimiotaxia e a degranulação de neutrófilos e suprime a ativação de IL-1β ligada ao inflamassoma NLRP3/pirina.

A Febre Familiar do Mediterrâneo (FMF) é causada por mutações de ganho de função no gene *MEFV* (pirina), que geram inflamação excessiva mediada por IL-1β, com crises de febre e serosite. A relação com a indicação original é direta: em ambas as situações (gota e FMF) há inflamação neutrofílica, e a colchicina atua nessa via. Ela é o tratamento de primeira linha da FMF, usado para prevenir crises e a amiloidose AA, conforme descrito em diretrizes e revisões (por exemplo, PMIDs 37298536, 32806879 e 30686512).

Um ponto de atenção: o rótulo "autossômica dominante" corresponde a um subtipo; a FMF típica tem herança autossômica recessiva, então o mapeamento na ontologia de doenças deve ser conferido.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Foram identificadas 20 publicações, majoritariamente revisões. Seguem as 10 mais relevantes:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37298536](https://pubmed.ncbi.nlm.nih.gov/37298536/) | 2023 | Revisão | Int J Mol Sci | Atualização sobre FMF, a doença autoinflamatória prototípica, incluindo resistência ao tratamento e adesão |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Revisão | Turk J Med Sci | Da patogênese ao tratamento: FMF é causada por mutações de ganho de função em *MEFV* (pirina); novidades em diagnóstico e terapia |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Revisão | N Engl J Med | Canaquinumabe em síndromes febris autoinflamatórias recorrentes, incluindo FMF (contexto de segunda linha) |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Revisão | Presse Med | FMF é a síndrome febril periódica hereditária mais frequente e antiga; associada a mutações em *MEFV* |
| [28413100](https://pubmed.ncbi.nlm.nih.gov/28413100/) | 2017 | Revisão | Semin Arthritis Rheum | Colchicina é o padrão-ouro; até 5% dos pacientes são resistentes ou intolerantes; alternativas terapêuticas |
| [38925725](https://pubmed.ncbi.nlm.nih.gov/38925725/) | 2024 | Revisão/comentário | J Am Coll Cardiol | Inflamação, colchicina e doença aterosclerótica na FMF |
| [25649364](https://pubmed.ncbi.nlm.nih.gov/25649364/) | 2014 | Revisão | Acta Med (Hradec Kralove) | A colchicina é o agente que reduz o desenvolvimento de amiloidose e a frequência/gravidade das crises |
| [25760087](https://pubmed.ncbi.nlm.nih.gov/25760087/) | 2015 | Revisão | Curr Med Chem | Agentes biológicos na FMF; 5% a 10% dos pacientes são resistentes ou intolerantes à colchicina |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Revisão | Clin Exp Rheumatol | Inibição de IL-1 na FMF; colchicina é a droga de escolha desde 1972; níveis regulados por glicoproteína-P e CYP3A4 |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Revisão | Curr Med Chem | Colchicina, biológicos e outras opções no tratamento da FMF |

## Informações de Comercialização no Brasil

Todos os 7 registros encontrados estão cancelados; atualmente não há registro válido.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 120190075 | COXYM | Não informada | Antiinflamatórios antirreumáticos |
| Registro 101180109 | COLCHIS | Não informada | Antigotosos |
| Registro 154230203 | COLCHICINA | Não informada | Antigotosos |
| Registro 118190144 | COLCHICINA | Não informada | Antiinflamatórios antirreumáticos |
| Registro 118190397 | GOLTRITE | Não informada | Antiinflamatórios antirreumáticos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Não aplicável como antineoplásico; trata-se de agente antimitótico (inibidor de microtúbulos) com toxicidade sistêmica |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula (o grafo de conhecimento associa o fármaco a contraindicações em neutropenia, leucopenia, agranulocitose, trombocitopenia e anemia aplástica) |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula (intolerância gastrointestinal é relatada na literatura) |
| Itens de Monitoramento | Hemograma completo, função hepática e renal, sinais de miotoxicidade |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Contraindicações e condições de risco (segundo o grafo de conhecimento TxGNN/PrimeKG, não o texto da bula)**: insuficiência hepática, insuficiência renal, doenças hematológicas (trombocitopenia, leucopenia, agranulocitose, neutropenia e anemia aplástica), úlcera péptica, miopatia e rabdomiólise, doenças diarreicas e nefropatia aguda por urato.
- **Interações medicamentosas** (100 interações registradas; principais exemplos):
  - **Graves**: aprepitanto, claritromicina, eliglustate, rolapitanto, rosuvastatina, sinvastatina, cobicistate, deferiprona.
  - **Moderadas**: metronidazol, cimetidina, eluxadolina, miconazol, tinidazol, deferasirox, ticagrelor, cloroquina, benznidazol, dissulfiram, fostamatinibe, cloreto de estrôncio Sr-89.
  - O risco está ligado principalmente a inibidores de CYP3A4/glicoproteína-P e a estatinas (miotoxicidade).

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- A colchicina é o tratamento de primeira linha estabelecido para a FMF, com mecanismo diretamente ligado à via da pirina/IL-1β e ampla documentação em revisões e diretrizes. Porém, os dados compilados não trazem ensaios registrados nem estudos primários, e o mercado brasileiro tem apenas registros cancelados.

**Para prosseguir, é necessário:**
- Verificar os ensaios clássicos controlados por placebo que sustentam o nível L1, pois não constam nos dados compilados.
- Obter a bula da ANVISA (advertências e contraindicações), hoje ausente, e os dados formais de mecanismo de ação.
- Confirmar a disponibilidade local do produto, já que todos os registros estão cancelados.
- Definir salvaguardas: ajuste de dose por função renal e hepática, triagem de interações com CYP3A4/glicoproteína-P, monitoramento de intolerância gastrointestinal e miotoxicidade, e uso de inibidor de IL-1 (por exemplo, canaquinumabe) em casos resistentes ou intolerantes.
- Revisar o mapeamento do subtipo "autossômico dominante" na ontologia de doenças.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

