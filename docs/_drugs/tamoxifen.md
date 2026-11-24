---
layout: default
title: Tamoxifen
parent: Apenas Predição do Modelo (L5)
nav_order: 605
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Tamoxifen"
predicted_indications: ["mammary Paget disease", "Ehrlich tumor carcinoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Tamoxifen: nova indicação prevista, Doença de Paget mamária (mammary Paget disease) (nível de evidência L5). No Brasil, registros na ANVISA: 30 (ativos: 11)"
---

# Tamoxifen
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

## Tamoxifen: Doença de Paget mamária (mammary Paget disease)
{: .text-alpha }

## Resumo em Uma Frase

Tamoxifeno é um modulador seletivo do receptor de estrogênio, originalmente usado no tratamento do carcinoma de mama feminino (incluindo carcinoma ductal invasivo e adenocarcinoma ductal de mama).
O modelo TxGNN prevê que pode ser eficaz para a **Doença de Paget mamária (Mammary Paget Disease)**, mas por ora há apenas **1 ensaio clínico** (sem relação direta com a doença) e **10 publicações** (casos clínicos, séries cirúrgicas e revisões) nessa direção.

> **Observação importante:** entre as 10 indicações previstas, a de maior pontuação (Paget mamária) tem evidência fraca. A previsão com melhor sustentação clínica é o **carcinoma de mama in situ (DCIS)**, tratado em seção própria mais adiante.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Doença de Paget mamária (mammary Paget disease) |
| Pontuação de Previsão TxGNN | 0.9969 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 11 de 30) |
| Número de Registros | 30 (ativos: 11) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Tamoxifen (tradução não oficial): “O tamoxifeno é um agonista/antagonista estrogênico. O tamoxifeno compete com o estrogênio pela ligação ao receptor de estrogênio, o que pode resultar em uma diminuição do crescimento dependente da sinalização do receptor de estrogênio no tecido mamário. O tamoxifeno demonstrou atividade antitumoral contra linhagens celulares de câncer de mama humano xenoenxertadas em camundongos.” Texto original em inglês: "Tamoxifen is an estrogen agonist/antagonist. Tamoxifen competes with estrogen for binding to the estrogen receptor, which can result in a decrease in estrogen receptor signaling-dependent growth in breast tissue. Tamoxifen has demonstrated antitumor activity against human breast cancer cell lines xenografted in mice." ([DailyMed: Soltamox (tamoxifen citrate) prescribing information, Mayne Pharma](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e6ff055-590c-41e6-9530-1fdf04cdbd02), versão de 2021-11-29; acessado em 2026-11-19). Segundo informações conhecidas, o tamoxifeno é um modulador seletivo do receptor de estrogênio (SERM) que antagoniza competitivamente o receptor de estrogênio (ER) no tecido mamário. Sua eficácia no câncer de mama com receptor hormonal positivo está bem estabelecida.

A doença de Paget mamária costuma estar associada a carcinoma ductal *in situ* ou a câncer de mama invasivo, frequentemente ER-positivos. Por isso, o antagonismo do ER é biologicamente plausível. Há um relato de caso de resposta ao tamoxifeno em doença de Paget extramamária metastática com receptor hormonal positivo, e outro de resposta em um caso extenso de Paget do mamilo.

Contudo, a evidência é **indireta**. A pontuação TxGNN muito alta reflete a proximidade na rede de conhecimento com o câncer de mama, e não dados específicos sobre a doença de Paget.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Concluído | 313 | Acetato de medroxiprogesterona vs. observação na prevenção de patologia endometrial em mulheres pós-menopausadas tratadas com tamoxifeno (inclui pacientes com Paget do mamilo). Não testa a eficácia do tamoxifeno na doença de Paget. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-análise | Breast Care | Recorrência local após mastectomia e cirurgia conservadora na Paget da mama; taxa total de recorrência de 20–40% |
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Relato de caso | Investigational New Drugs | Tratamento bem-sucedido de Paget extramamária metastática, receptor hormonal positivo, com tamoxifeno |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Relato de caso | Breast | Paget do mamilo extensa com resposta ao tamoxifeno, associada à radioterapia |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Série/Revisão | Br J Surg | 48 mulheres com Paget do mamilo; maioria tratada com mastectomia, um caso com tamoxifeno |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Coorte | Niger J Clin Pract | Série de 8 casos de Paget do complexo mamilo-areolar na Nigéria |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Relato de caso | Clin Breast Cancer | Paget do mamilo como recidiva local após tratamento conservador |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Coorte/caso | Arch Gynecol Obstet | Paget vulvar e mamária com câncer subjacente sincrônico |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Relato de caso | Surg Today | Câncer de mama bilateral sincrônico com Paget e carcinoma ductal invasivo |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Relato de caso | Am Surg | Paget da mama masculina e revisão de 32 casos da literatura |
| [18288984](https://pubmed.ncbi.nlm.nih.gov/18288984/) | 2008 | Revisão | Curr Med Chem | Terapias para perda óssea; relevância tangencial |

---

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431482 | TAMOXIN | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431499 | CITRATO DE TAMOXIFENO | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100470280 | CITRATO DE TAMOXIFENO | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 102351241 | CITRATO DE TAMOXIFENO | EMS S/A | Ativo |
| 102351270 | TACFEN | EMS S/A | Ativo |
| 105830927 | CITRATO DE TAMOXIFENO | GERMED FARMACEUTICA LTDA | Ativo |
| 116180036 | NOLVADEX | ASTRAZENECA DO BRASIL LTDA | Ativo |
| 116370027 | TAXOFEN | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370130 | CITRATO DE TAMOXIFENO | BLAU FARMACÊUTICA S.A. | Ativo |
| 118190332 | CITRATO DE TAMOXIFENO | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 167730587 | CITRATO DE TAMOXIFENO | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100430582 | TAMOXIN | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100430982 | CITRATO DE TAMOXIFENO | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100470414 | FESTONE | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100680938 | FESTONE | NOVARTIS BIOCIENCIAS S.A | Cancelado |
| 101620208 | TAXARIM | LABORATÓRIOS PIERRE FABRE DO BRASIL LTDA | Cancelado |
| 102980144 | TAMOX | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Cancelado |
| 104970267 | TAMOXITRAT | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |
| 109860020 | TAMOX | IBFARMA INDUSTRIA DE BIOTECNOLOGIA FTCA LTDA. | Cancelado |
| 112130077 | BIOXIFENO | BIOSINTÉTICA FARMACÊUTICA LTDA | Cancelado |
| 112130351 | CITRATO DE TAMOXIFENO | BIOSINTÉTICA FARMACÊUTICA LTDA | Cancelado |
| 112330052 | CITRATO DE TAMOXIFENO | LABORATORIO QUIMICO FARMACEUTICO DA AERONAUTICA | Cancelado |
| 112830070 | TAMOXYTA | LABORATORIO ITAFARMA LTDA | Cancelado |
| 121170105 | TAMOPLEX | ASTA MÉDICA LTDA | Cancelado |
| 122050046 | BILEM | LABORATORIO ENILA IND. E COM. DE PROD. QUIM. E FAR | Cancelado |
| 122140005 | TECNOTAX | ADIUM S.A. | Cancelado |
| 123610016 | TAMOOEX | UCB BIOPHARMA LTDA. | Cancelado |
| 124870012 | TAMOXIFENO | PAYAM NEDA | Cancelado |
| 126750304 | CITRATO DE TAMOXIFENO | NOVA QUIMICA FARMACÊUTICA S/A | Cancelado |
| 150820022 | TAMOPLEX | ASTA MÉDICA-ONCOLOGIA LTDA | Cancelado |

<!-- licenses:end -->

<!-- review:begin br-lic-20261124c-tamoxifen-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “Essa informação diverge da realidade esperada para um fármaco amplamente usado e **deve ser verificada** diretamente na ANVISA.” Removido: a frase se referia a uma afirmação sobre os registros removida anteriormente e ficou sem sentido; esta seção agora traz a tabela de registros gerada por programa a partir dos dados abertos de medicamentos da ANVISA (os números atualizados estão no resumo rápido e na tabela). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124c-tamoxifen-1 -->

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal (SERM); não é citotóxico convencional |
| Risco de Mielossupressão | Baixo; porém o conhecimento do fármaco associa leucopenia e trombocitopenia (ver contraindicações) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma, função hepática, cálcio sérico, avaliação endometrial e sinais de tromboembolismo |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

---

## Considerações de Segurança

- **Contraindicações (base de conhecimento, não bula):** trombocitopenia, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, acidente vascular cerebral e doenças cerebrovasculares, infarto cerebral, embolia pulmonar, leucopenia, distúrbios da visão e cegueira.
- **Interações medicamentosas:** foram identificadas 100 interações. Entre as de gravidade **maior** constam: bupropiona, lorcaserina, cimetidina, dolasetrona, eliglustate, cisaprida, dexfenfluramina e fenfluramina. Há também interações moderadas (por exemplo, famotidina, loperamida, aprepitanto, dexametasona, claritromicina, granisetrona e levofloxacino) e menores (fidaxomicina).

> As advertências e contraindicações da bula da ANVISA não estavam disponíveis. Consulte a bula para informações de segurança completas.

---

## Outras Indicações Previstas (Resumo)

| # | Indicação | Pontuação | Nível | Recomendação |
|---|---|---|---|---|
| 2 | Adenocarcinoma cribriforme intraductal de mama | 0,9969 | L5 | Hold |
| 4 | **Carcinoma de mama in situ (DCIS)** | 0,9967 | **L1** | **Proceed with Guardrails** |
| 5 | Carcinoma sebáceo de mama | 0,9967 | L5 | Hold |
| 6 | Carcinoma tubular invasivo de mama | 0,9967 | L4 | Research Question |
| 7 | Carcinoma de mama resistente a hormônio | 0,9967 | L2 | Research Question |
| 8 | Câncer de mama ER-positivo | 0,9967 | L1 | Proceed with Guardrails |
| 9 | Carcinoma de Ehrlich (modelo murino) | 0,9967 | L4 | Hold |
| 10 | Rabdomiossarcoma embrionário botrioide de vagina | 0,9967 | L5 | Hold |

**Destaque, DCIS:** há ensaio fase 3 randomizado e controlado por placebo com tamoxifeno em baixa dose (TAM-01, [PMID 36917758](https://pubmed.ncbi.nlm.nih.gov/36917758/) e [PMID 30973790](https://pubmed.ncbi.nlm.nih.gov/30973790/)), com redução de eventos de câncer de mama, além de outros estudos fase 3 concluídos (por exemplo, [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) e [NCT00053898](https://clinicaltrials.gov/study/NCT00053898)). Essa indicação, porém, é uma extensão do uso já estabelecido em câncer de mama, e não um reposicionamento propriamente novo. Para o câncer de mama ER-positivo, vale a mesma ressalva.

**Alerta, basal-like:** esses tumores são em sua maioria ER-negativos, e um estudo sugere que a exposição ao tamoxifeno pode favorecer fenótipo de células-tronco; não há evidência clínica de benefício.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, doença de Paget mamária)

**Justificativa:**
- A evidência para Paget mamária se limita a relatos de caso e séries cirúrgicas, sem ensaio que teste o tamoxifeno nessa doença (nível L4). A pontuação do modelo reflete proximidade com o câncer de mama, não dados específicos.
- Para o **DCIS** (L1), a recomendação seria **Proceed with Guardrails**, restrita a doença com receptor hormonal positivo, considerando regimes de baixa dose.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) do tamoxifeno, ausentes nos dados compilados.
- Bula da ANVISA (advertências e contraindicações) e verificação da situação de comercialização e dos registros no Brasil.
- Para Paget mamária: estudos prospectivos ou séries com status de receptor hormonal e desfecho com tamoxifeno.
- Plano de monitoramento de risco endometrial, tromboembolismo e CYP2D6, bem como revisão das 100 interações medicamentosas, em especial as de gravidade maior.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Soltamox (tamoxifen citrate) prescribing information, Mayne Pharma](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e6ff055-590c-41e6-9530-1fdf04cdbd02) |
| 2026-11-24 | Removido: “Essa informação diverge da realidade esperada para um fármaco amplamente usado e **deve ser verificada** diretamente na ANVISA.” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

