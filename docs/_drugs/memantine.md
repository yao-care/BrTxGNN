---
layout: default
title: Memantine
parent: Apenas Predição do Modelo (L5)
nav_order: 442
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "Memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Memantine: nova indicação prevista, Hipertensão pulmonar (pulmonary hypertension) (nível de evidência L5). Indicação original: OUTROS PRODUTOS QUE ATUAM SOBRE O SISTEMA NERVOSO"
---

# Memantine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Memantine: Hipertensão pulmonar (pulmonary hypertension)
{: .text-alpha }

## Resumo em Uma Frase

Memantina (cloridrato de memantina) foi registrada na ANVISA na categoria genérica de "outros produtos que atuam sobre o sistema nervoso". É um antagonista do receptor NMDA, conhecido no uso clínico para doenças neurológicas.
O modelo TxGNN prevê que pode ser eficaz para **hipertensão pulmonar (pulmonary hypertension)**, mas essa previsão tem apenas **2 publicações** sem relação direta com o fármaco e **nenhum ensaio clínico**.
A direção melhor sustentada pelos dados é a **enxaqueca (migraine disorder)**, com **1 ensaio clínico de Fase 3 concluído** e **18 publicações**. Por isso, o título do relatório destaca a enxaqueca.

> **Nota sobre a escolha da indicação:** a primeira previsão do TxGNN (hipertensão pulmonar) tem evidência de nível L5. A segunda previsão (enxaqueca) tem a evidência mais robusta entre as 10 previsões. Este relatório apresenta as duas, com foco na enxaqueca.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | OUTROS PRODUTOS QUE ATUAM SOBRE O SISTEMA NERVOSO; OUTROS MEDICAMENTOS QUE ATUAM SOBRE O SISTEMA NERVOSO |
| Nova Indicação Prevista (1ª do ranking) | Hipertensão pulmonar (pulmonary hypertension) |
| Nova Indicação com Maior Evidência (2ª do ranking) | Pulmonary hypertension |
| Pontuação de Previsão TxGNN | 0.9954 |
| Nível de Evidência | Hipertensão pulmonar: L5; enxaqueca: L1 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 41 de 58) |
| Número de Registros | 58 (ativos: 41) |
| Decisão Recomendada | Hipertensão pulmonar: Hold; enxaqueca: Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a memantina é um antagonista não competitivo do receptor NMDA de glutamato, e seu uso neurológico foi estabelecido. Mecanisticamente, pode ser aplicável a condições em que o glutamato tem papel importante.

**Enxaqueca:** a depressão cortical alastrante e a sensibilização central mediadas por glutamato estão implicadas na enxaqueca. Ao bloquear o receptor NMDA, a memantina pode reduzir esses processos. Revisões sobre antagonistas de NMDA como agentes antienxaqueca, uma metanálise de ensaios randomizados e uma revisão sistemática sobre prevenção de cefaleias primárias apoiam essa lógica. Porém, um comentário na revista *Headache* resume a situação como "grande promessa, pouca evidência".

**Hipertensão pulmonar:** a expressão de receptores NMDA na vasculatura pulmonar foi proposta como contribuinte para o remodelamento vascular, o que torna o antagonismo de NMDA teoricamente plausível. Contudo, os dois artigos recuperados não tratam de memantina nessa doença: um aborda a regulação da sensibilidade à insulina e do metabolismo lipídico pelo receptor NMDA, e o outro é um estudo farmacocinético de um composto distinto (MN-08, derivado nitrato da memantina). A pontuação alta do modelo não tem respaldo em evidência clínica ou pré-clínica direta.

## Evidências de Ensaios Clínicos

**Enxaqueca (migraine disorder):**

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Concluído | 33 | Memantina vs. valproato de sódio na profilaxia da enxaqueca episódica (2019-2020). Avaliação direta da indicação, mas a amostra pequena limita o poder estatístico. |

Para hipertensão pulmonar, atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

**Enxaqueca (principais publicações, de um total de 18):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Metanálise de RCTs | Clin Neuropharmacol | Avalia memantina vs. placebo em enxaqueca; a eficácia é considerada controversa |
| [35467554](https://pubmed.ncbi.nlm.nih.gov/35467554/) | 2022 | Metanálise de RCTs | Clin Neuropharmacol | Efetividade e segurança da memantina vs. placebo em cefaleia |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Revisão sistemática | Headache | Eficácia e segurança da memantina na profilaxia da enxaqueca episódica |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Revisão sistemática | Ann Pharmacother | Dados de eficácia e segurança da memantina na prevenção de cefaleias primárias |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Metanálise em rede | Front Pharmacol | Comparação de eficácia e segurança de preventivos orais da enxaqueca em adultos |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Revisão | Naunyn-Schmiedebergs Arch Pharmacol | Memantina e cetamina como possíveis agentes antienxaqueca |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Comentário/Revisão | Headache | "Grande promessa, pouca evidência" para memantina na enxaqueca |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Estudo retrospectivo | J Headache Pain | Série de 60 casos com memantina como preventivo de enxaqueca |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Diretriz clínica | Ann Intern Med | Diretriz VA/DoD 2023 para tratamento e prevenção de enxaqueca e cefaleia tensional |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Revisão | Neurotherapeutics | Glutamato e seus receptores como alvos terapêuticos na enxaqueca |

**Hipertensão pulmonar (2 publicações, ambas indiretas):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Pré-clínico/mecanístico | Theranostics | O eixo glutamato/NMDAR regula a sensibilidade à insulina e o metabolismo lipídico; menciona o papel do eixo em hipertensão arterial pulmonar |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Fase 1 (PK/segurança) | Clin Drug Investig | Estudo do MN-08, derivado nitrato da memantina, em voluntários saudáveis chineses; composto distinto |

**Outras previsões de destaque (resumo):**
- **Enxaqueca com aura do tronco encefálico (L3):** sem ensaios específicos; há um RCT em enxaqueca sem aura (PMID 26638119) e revisões, com evidência extrapolada.
- **Enxaqueca com ou sem aura, suscetibilidade (L2):** entrada de suscetibilidade genética; a evidência clínica é melhor atribuída à indicação "enxaqueca".
- **Cardiopatia cifoescoliótica (L5):** sem ensaios nem literatura.

## Informações de Comercialização no Brasil

Há 20 registros **válidos**; o medicamento é comercializado. Principais registros (5 de 20):

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330159 | ZIDER | LIBBS FARMACÊUTICA LTDA | Ativo |
| 100330216 | ZIDER | LIBBS FARMACÊUTICA LTDA | Ativo |
| 100431040 | HEIMER | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431134 | CLORIDRATO DE MEMANTINA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100470579 | CLORIDRATO DE MEMANTINA | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100681175 | CLORIDRATO DE MEMANTINA | NOVARTIS BIOCIENCIAS S.A | Ativo |
| 101180592 | ALOIS | APSEN FARMACEUTICA S/A | Ativo |
| 101180614 | CLORIDRATO DE MEMANTINA | APSEN FARMACEUTICA S/A | Ativo |
| 101180615 | ALOIS | APSEN FARMACEUTICA S/A | Ativo |
| 101180627 | CLORIDRATO DE DONEPEZILA + CLORIDRATO DE MEMANTINA | APSEN FARMACEUTICA S/A | Ativo |
| 101180628 | ALOIS DUO | APSEN FARMACEUTICA S/A | Ativo |
| 101180645 | ALOIS DUO PACK | APSEN FARMACEUTICA S/A | Ativo |
| 102351324 | MORIALE ODT | EMS S/A | Ativo |
| 102351380 | MORIALE DUO | EMS S/A | Ativo |
| 102351385 | CLORIDRATO DE DONEPEZILA + CLORIDRATO DE MEMANTINA | EMS S/A | Ativo |
| 102351403 | CLORIDRATO DE MEMANTINA | EMS S/A | Ativo |
| 102980577 | LÁBREA DUO | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 103700595 | CLORIDRATO DE MEMANTINA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700597 | MEMORALL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 104750050 | EBIX | LUNDBECK BRASIL LTDA | Ativo |
| 105250086 | MEALZ | TORRENT DO BRASIL LTDA | Ativo |
| 105250104 | CLORIDRATO DE MEMANTINA | TORRENT DO BRASIL LTDA | Ativo |
| 105250127 | EPÉZ DUO | TORRENT DO BRASIL LTDA | Ativo |
| 105730046 | COMFECT DUO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730467 | DONILA DUO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730502 | VIE | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730570 | CLORIDRATO DE MEMANTINA | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730736 | CLORIDRATO DE DONEPEZILA + CLORIDRATO DE MEMANTINA | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105831018 | CLORIDRATO DE MEMANTINA | GERMED FARMACEUTICA LTDA | Ativo |
| 109740286 | KAMPPI | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (TxGNN/PrimeKG, não é texto de bula):** doença hepática, doença da vesícula biliar e comprometimento da função renal.
- **Interações medicamentosas:** foram identificadas 100 interações no total; entre as 20 listadas, as de gravidade **moderada** envolvem anticolinérgicos/antiespasmódicos: hioscina (hiosciamina), atropina, glicopirrônio, clidínio, diciclomina, metescopolamina, propantelina, escopolamina, tróspio e mepenzolato. Interações **leves** incluem ranitidina, metformina, cimetidina e citrato de potássio. Há ainda interações de gravidade não classificada com glimepirida, doxiciclina, lansoprazol, loperamida, famotidina e ácido acetilsalicílico.
- Para advertências e contraindicações da bula, consulte a bula; esses dados ainda não foram obtidos.

## Conclusão e Próximos Passos

**Decisão:**
- **Hipertensão pulmonar (1ª previsão): Hold**
- **Enxaqueca (2ª previsão): Proceed with Guardrails**

**Justificativa:**
- Hipertensão pulmonar: a pontuação do modelo é alta (0,9954), mas não há ensaios nem literatura direta; o único elo é teórico (NMDA na vasculatura pulmonar).
- Enxaqueca: há um ensaio de Fase 3 concluído e várias metanálises e revisões sistemáticas. Porém, o ensaio é pequeno (33 participantes), a eficácia segue descrita como controversa e há poucos ensaios robustos. Além disso, não há registro válido no Brasil, e os dados de segurança da bula estão ausentes.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança.
- Complementar os dados de mecanismo de ação (consulta ao DrugBank).
- Avaliar a situação regulatória: o medicamento é comercializado e há 20 registros válidos, de modo que seria preciso verificar a via de acesso para a nova indicação.
- Para enxaqueca: examinar os resultados completos do NCT04698525 e as metanálises (PMID 33961371 e 35467554) e planejar ensaio de maior porte, com plano de monitoramento de segurança (função renal e hepática, interações com anticolinérgicos).
- Para hipertensão pulmonar: gerar evidência pré-clínica direta com memantina antes de qualquer avanço.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

