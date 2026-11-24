---
layout: default
title: Paclitaxel
parent: Apenas Predição do Modelo (L5)
nav_order: 504
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Paclitaxel: nova indicação prevista, Parameningeal embryonal rhabdomyosarcoma (nível de evidência L5). No Brasil, registros na ANVISA: 49 (ativos: 15)"
---

# Paclitaxel
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Paclitaxel: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## Resumo em Uma Frase

Paclitaxel é um quimioterápico antimicrotúbulo (taxano), cujas indicações originais registradas na base de conhecimento do modelo estão ligadas principalmente ao câncer de ovário.
O modelo TxGNN prevê que pode ser eficaz para o **carcinoma de mama feminino (female breast carcinoma)**, atualmente com **40 ensaios clínicos** e **18 publicações** apoiando esta direção. Vale notar que o câncer de mama já é uma indicação estabelecida dos taxanos, de modo que se trata mais de um uso consolidado do que de reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Parameningeal embryonal rhabdomyosarcoma |
| Pontuação de Previsão TxGNN | 0.9973 |
| Nível de Evidência | L5 (L1 não atribuído ao carcinoma de mama feminino, pois os ensaios Phase 3 listados não testam diretamente o paclitaxel como variável principal) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 49) |
| Número de Registros | 49 (ativos: 15) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Paclitaxel (tradução não oficial): “O paclitaxel em partículas ligadas a proteínas para suspensão injetável (ligado à albumina) é um inibidor de microtúbulos que promove a montagem de microtúbulos a partir de dímeros de tubulina e estabiliza os microtúbulos impedindo a despolimerização. Essa estabilidade resulta na inibição da reorganização dinâmica normal da rede de microtúbulos, que é essencial para as funções celulares vitais da interfase e da mitose.” Texto original em inglês: "Paclitaxel protein-bound particles for injectable suspension (albumin-bound) is a microtubule inhibitor that promotes the assembly of microtubules from tubulin dimers and stabilizes microtubules by preventing depolymerization. This stability results in the inhibition of the normal dynamic reorganization of the microtubule network that is essential for vital interphase and mitotic cellular functions." ([DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c), versão de 2025-09-17; acessado em 2026-11-19). Segundo o conhecimento farmacológico estabelecido, o paclitaxel estabiliza os microtúbulos e impede a desmontagem do fuso mitótico, causando parada do ciclo celular em G2/M e apoptose em células tumorais de divisão rápida.

Como esse efeito antimitótico não depende de um órgão-alvo específico, ele se aplica tanto ao câncer de ovário quanto ao de mama. A literatura revisada confirma que os taxanos são componentes baseados em evidência no tratamento de carcinomas avançados de mama, pulmão e ovário, e que o paclitaxel foi aprovado para o tratamento adjuvante do câncer de mama em estágio inicial com linfonodos positivos.

A previsão do modelo é, portanto, coerente com a prática clínica. Observa-se ainda que a lista de indicações originais da fonte contém apenas condições ovarianas (além de hipertensão e glaucoma), o que representa uma lacuna no registro de origem, e não um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

Foram identificados 40 ensaios para esta indicação; abaixo estão os mais relevantes (priorizando estudos concluídos com paclitaxel como componente direto).

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Concluído | 50 | Paclitaxel semanal de 1 hora associado a trastuzumabe em câncer de mama metastático ou recorrente |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Desconhecido | Não informado | Comparação randomizada de dois esquemas de docetaxel ou paclitaxel em câncer de mama metastático |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Phase 2 | Concluído | 36 | Piloto com PSC 833 para modular a resistência a múltiplas drogas ao paclitaxel em câncer de mama metastático |
| [NCT00006110](https://clinicaltrials.gov/study/NCT00006110) | Phase 2 | Concluído | 82 | AC seguido de paclitaxel, com ou sem Herceptin, em câncer de mama estágios IIB a IV |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Concluído | Não informado | Gencitabina + paclitaxel versus paclitaxel em câncer de mama localmente recorrente ou metastático |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Concluído | 580 | Lapatinibe + paclitaxel versus paclitaxel isolado em primeira linha de câncer de mama avançado |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Concluído | 652 | Quimioterapia com taxano + lapatinibe versus trastuzumabe em câncer de mama HER2-positivo metastático |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Concluído | 632 | Nab-paclitaxel versus paclitaxel em base solvente, neoadjuvante, em câncer de mama HER2-negativo de alto risco |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Concluído | 478 | Docetaxel versus paclitaxel após FEC com densidade de dose em câncer de mama com linfonodos positivos |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Concluído | 455 | Neo-ALTTO: lapatinibe, trastuzumabe ou ambos, com paclitaxel, no cenário neoadjuvante HER2-positivo |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revisão | Lancet | Paclitaxel e docetaxel têm atividade substancial em carcinomas avançados de mama, pulmão e ovário; paclitaxel aprovado nos EUA para adjuvância em câncer de mama inicial com linfonodos positivos |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisão | Drug and Therapeutics Bulletin | Revisão do paclitaxel e docetaxel em câncer de mama e ovário, com ampliação da licença para mama metastático |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Estudo clínico Phase 2 | Cancer | Doxorrubicina + paclitaxel em câncer de mama metastático; importância da terapia adjuvante prévia com antraciclina |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Revisão | Cancer | Papel do paclitaxel no tratamento multimodal do carcinoma inflamatório de mama |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Estudo de escalonamento de dose | Annals of Oncology | Determinação da dose máxima tolerada de paclitaxel + ciclofosfamida em câncer de mama avançado |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Estudo translacional | Nature Communications | Variações germinativas em TEKT4 associadas à resistência ao paclitaxel no câncer de mama |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Revisão | Seminars in Oncology Nursing | Visão geral histórica do desenvolvimento do paclitaxel |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Pré-clínico (in vitro) | Journal of Cellular Physiology | ZD6474 potencializa os efeitos antiproliferativos e apoptóticos do paclitaxel em células de carcinoma de mama |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | Pré-clínico | Cancer Chemotherapy and Pharmacology | Silenciamento de SRSF3 sensibiliza células de câncer de mama ao paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Pré-clínico/computacional | Chemical Biology & Drug Design | Combinações de paclitaxel contra carcinoma de mama e identificação de biomarcadores in vivo |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330115 | ONTAX | LIBBS FARMACÊUTICA LTDA | Ativo |
| 100410155 | PACLITAXEL | FRESENIUS KABI BRASIL LTDA | Ativo |
| 100430899 | PACLITAXEL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 106460227 | TAXILAN | LABORATORIO QUIMICO FARMACEUTICO BERGAMO LTDA | Ativo |
| 116370126 | PACLITAXEL | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370208 | TOXXEL | BLAU FARMACÊUTICA S.A. | Ativo |
| 116880021 | EVOTAXEL | FARMARIN INDUSTRIA E COMERCIO LTDA | Ativo |
| 125760033 | ABRAXANE | UNITED MEDICAL LTDA | Ativo |
| 155370001 | PANTIUM | ACCORD FARMACÊUTICA LTDA | Ativo |
| 155370004 | PACLITAXEL | ACCORD FARMACÊUTICA LTDA | Ativo |
| 165070027 | POKLI | CAMBER FARMACEUTICA LTDA | Ativo |
| 165070033 | PACLITAXEL | CAMBER FARMACEUTICA LTDA | Ativo |
| 186060002 | PACLIMEIZ | GADOR DO BRASIL - COMÉRCIO DE PRODUTOS FARMACÊUTIC | Ativo |
| 188300046 | MYLTOL | VIATRIS FARMACEUTICA DO BRASIL LTDA | Ativo |
| 189770005 | TAXOL | BIOPAS BRASIL PRODUTOS FARMACEUTICOS LTDA | Ativo |
| 100430516 | PACLITAX | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100431153 | PACLITAX | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100470409 | TARVEXOL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100470553 | PACLITAXEL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100470560 | TARVEXOL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100630173 | TACLIPAXOL | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100680889 | TARVEXOL | NOVARTIS BIOCIENCIAS S.A | Cancelado |
| 101620232 | ONXEL | LABORATÓRIOS PIERRE FABRE DO BRASIL LTDA | Cancelado |
| 101800151 | TAXOL | BRISTOL-MYERS SQUIBB FARMACÊUTICA LTDA | Cancelado |
| 102980142 | PAXEL | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Cancelado |
| 104450137 | EVOTAXEL | LABORATORIO SINTERAPICO INDUSTRIAL FTCO LTDA | Cancelado |
| 106460139 | TAXILAN | LABORATORIO QUIMICO FARMACEUTICO BERGAMO LTDA | Cancelado |
| 106460217 | AKSSUS | LABORATORIO QUIMICO FARMACEUTICO BERGAMO LTDA | Cancelado |
| 108580189 | PROTAXEL | PRODOTTI LABORATÓRIO FARMACÊUTICO LTDA. | Cancelado |
| 110130234 | PACLITAXEL | GLENMARK FARMACÊUTICA LTDA | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro), de 49 registros nos dados. A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

<!-- licenses:end -->

## Considerações de Segurança

- **Doenças com contraindicação ou precaução na base de conhecimento (não é texto de bula):** neutropenia, agranulocitose, trombocitopenia, anemia, doença hepática, doença renal, doença da vesícula biliar, neuropatia periférica, infarto do miocárdio, parada cardíaca súbita, hiperbilirrubinemia (incluindo síndrome de Gilbert), diabetes mellitus e cetoacidose diabética, asma, psoríase, hipotensão, transtornos de ansiedade e distúrbios neuróticos/distímicos.
- **Interações medicamentosas (100 identificadas; principais):**
  - Moderadas: aprepitanto, cimetidina, claritromicina, clotrimazol, dexametasona, eliglustate, metronidazol, miconazol, rolapitanto, rosuvastatina, sinvastatina, tinidazol, troglitazona.
  - Menores: ácido ascórbico, levofloxacino.
  - Nível desconhecido: glimepirida, doxiciclina, morfina, metformina, omeprazol.
- **Eventos adversos descritos na literatura:** neuropatia periférica induzida por taxano, pneumonite, uveíte, lesões epiteliais da córnea e síndrome de eritema tenar periarticular com onicólise.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (taxano, estabilizador de microtúbulos) |
| Risco de Mielossupressão | Alto (neutropenia é a toxicidade limitante de dose; a base de conhecimento também associa trombocitopenia, anemia e agranulocitose) |
| Classificação de Emetogenicidade | Baixa a média |
| Itens de Monitoramento | Hemograma completo com diferencial, função hepática (bilirrubina e transaminases) e renal, avaliação neurológica periférica, sinais de hipersensibilidade durante a infusão |
| Proteção no Manuseio | Necessário seguir os regulamentos de manuseio de medicamentos citotóxicos |

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há dezenas de ensaios clínicos de Phase 2 e 3 e literatura consistente com o uso de paclitaxel no câncer de mama, e a pontuação do TxGNN é muito alta. Porém, trata-se de um uso já estabelecido (não de reposicionamento novo), e os ensaios Phase 3 em sua maioria testam outros agentes, com o paclitaxel como base da quimioterapia.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada pela ANVISA (advertências e contraindicações), uma lacuna bloqueante para a triagem de segurança.
- Obter dados formais de mecanismo de ação (por exemplo, via DrugBank).
- Corrigir a lista de indicações originais da fonte (ausência do câncer de mama e presença de hipertensão e glaucoma).
- Estabelecer plano de monitoramento hematológico, neurológico e de hipersensibilidade, e de gestão de interações medicamentosas (especialmente inibidores e indutores de CYP).

**Observação sobre outras indicações previstas:** o câncer de mama RE-positivo (L1 com ressalva, pois os Phase 3 listados avaliam outros agentes), o RE-negativo e o resistente a hormônio (L2) seguem a mesma lógica e podem avançar com salvaguardas.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

