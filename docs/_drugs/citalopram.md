---
layout: default
title: Citalopram
parent: Evidência Moderada (L3-L4)
nav_order: 224
evidence_level: L3
indication_count: 5
monitor_inn: "CITALOPRAM"
predicted_indications: ["obsessive-compulsive disorder", "paranoid personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder"]
last_modified_at: 2026-11-25
description: "Citalopram: nova indicação prevista, Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder) (nível de evidência L3). No Brasil, registros na ANVISA: 55 (ativos: 22)"
---

# Citalopram
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **5** 
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

## Citalopram: inibidor seletivo da recaptação de serotonina (ISRS) → Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder)
{: .text-alpha }

## Resumo em Uma Frase

Citalopram é um inibidor seletivo da recaptação de serotonina (ISRS), usado principalmente em transtornos depressivos e de ansiedade.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder)**,
atualmente com **4 ensaios clínicos** registrados (nenhum estudando o citalopram diretamente) e **16 publicações** recuperadas, das quais várias avaliam o citalopram especificamente no TOC.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder) |
| Pontuação de Previsão TxGNN | 0,9974 |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 22 de 55) |
| Número de Registros | 55 (ativos: 22) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Citalopram (tradução não oficial): “O mecanismo de ação do citalopram não está claro, mas presume-se que esteja relacionado à potencialização da atividade serotoninérgica no sistema nervoso central (SNC), resultante da inibição da recaptação neuronal de serotonina (5-HT) no SNC.” Texto original em inglês: "The mechanism of action of citalopram is unclear, but is presumed to be related to potentiation of serotonergic activity in the central nervous system (CNS) resulting from its inhibition of CNS neuronal reuptake of serotonin (5-HT)." ([DailyMed: Celexa (citalopram) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4259d9b1-de34-43a4-85a8-41dd214e9177), versão de 2023-10-09; acessado em 2026-11-19). Ainda assim, o citalopram é um ISRS, e o mecanismo dessa classe é bem estabelecido: bloqueio da recaptação de serotonina, com aumento da disponibilidade desse neurotransmissor na fenda sináptica.

A disfunção serotoninérgica é central na fisiopatologia do TOC, e os ISRS são uma classe de primeira linha no tratamento farmacológico dessa condição. Isso torna biologicamente coerente que o citalopram seja aplicável ao TOC, e a pontuação elevada do modelo concorda com esse raciocínio.

A literatura recuperada inclui estudos abertos e pequenos estudos clínicos com citalopram no TOC, em adultos e em crianças e adolescentes, o que sustenta a previsão. Porém, esses estudos são em sua maioria pequenos e abertos, sem ensaios controlados robustos com citalopram nos dados compilados.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Concluído | 78 | Avalia ISRS, terapia de exposição e prevenção de resposta (ERP) e a combinação em TOC, além de preditores de resposta em população chinesa; o citalopram pode estar entre os ISRS, mas não é confirmado |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Concluído | 124 | TOC pediátrico com resposta parcial a inibidores da recaptação de serotonina; testa se a terapia cognitivo-comportamental melhora o efeito do tratamento; agente não identificado como citalopram |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Concluído | 158 | TCC em grupo versus fluoxetina em TOC; fármaco estudado é a fluoxetina, contexto apenas indireto |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | Concluído | 43 | Estudo piloto da microbiota intestinal em TOC e após 12 semanas de ISRS; sem evidência terapêutica para o citalopram |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Estudo clínico randomizado aberto | European Psychiatry | Citalopram isolado versus citalopram com clomipramina em TOC resistente (16 adultos, 90 dias) |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Estudo simples-cego | J Clin Psychopharmacol | Compara a eficácia antiobsessiva de fluvoxamina, paroxetina e citalopram em 30 pacientes |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Estudo aberto (pediátrico) | Psychiatry Clin Neurosci | Citalopram por 8 semanas em 15 crianças e adolescentes com TOC, doses de 20–30 mg/dia |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Estudo aberto | J Child Adolesc Psychopharmacol | 23 crianças e adolescentes; após 10 semanas, melhora significativa nos escores Y-BOCS/CY-BOCS (30 → 21; p < 0,001) |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Coorte (preliminar) | CNS Drugs | Relação preliminar entre concentrações de citalopram e resposta clínica no TOC |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Revisão/comentário | Int Clin Psychopharmacol | Discute o citalopram no TOC além da depressão e a ligação histórica entre TOC e inibidores da recaptação de serotonina |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Revisão | BMJ Clinical Evidence | Epidemiologia e curso do TOC (cerca de 1% dos homens e 1,5% das mulheres adultas) |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Revisão | World J Biol Psychiatry | O TOC responde a intervenções psicológicas e a medicação serotoninérgica |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Revisão | Curr Med Chem | Fármacos passados, presentes e futuros para o TOC, com papel central do sistema serotoninérgico |
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Revisão sistemática/meta-análise | Nordic J Psychiatry | Fluoxetina no TOC pediátrico; contexto de classe, não do citalopram |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330107 | PROCIMAX | LIBBS FARMACÊUTICA LTDA | Ativo |
| 100431271 | CITALOPRAM | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431387 | CITTÀ | EUROFARMA LABORATORIOS S.A. | Ativo |
| 102350864 | BROMIDRATO DE CITALOPRAM | EMS S/A | Ativo |
| 102980300 | DENYL | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 103700611 | BROMIDRATO DE CITALOPRAM | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 104750043 | CIPRAMIL | LUNDBECK BRASIL LTDA | Ativo |
| 105250016 | ALCYTAM | TORRENT DO BRASIL LTDA | Ativo |
| 105250066 | BROMIDRATO DE CITALOPRAM | TORRENT DO BRASIL LTDA | Ativo |
| 105730543 | CITALOPRAM | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730587 | MAXAPRAN | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105830563 | BROMIDRATO DE CITALOPRAM | GERMED FARMACEUTICA LTDA | Ativo |
| 109740331 | BROMIDRATO DE CITALOPRAM | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 118190328 | BROMIDRATO DE CITALOPRAM | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 123520101 | CITALOPRAM | RANBAXY FARMACÊUTICA LTDA | Ativo |
| 125680272 | BROMIDRATO DE CITALOPRAM | PRATI DONADUZZI & CIA LTDA | Ativo |
| 125680303 | NYPRAM | PRATI DONADUZZI & CIA LTDA | Ativo |
| 151670018 | BROMIDRATO DE CITALOPRAM | AUROBINDO PHARMA INDÚSTRIA FARMACÊUTICA LIMITADA | Ativo |
| 155840593 | CITALOPRAM | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Ativo |
| 156510011 | CITALOPRAM | ZYDUS NIKKHO FARMACÊUTICA LTDA | Ativo |
| 167730235 | BROMIDRATO DE CITALOPRAM | LEGRAND PHARMA INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 183260165 | CITALOPRAM (PORT. 344/98, L-C1) | SANOFI MEDLEY FARMACÊUTICA LTDA. | Ativo |
| 100430035 | CITALOPRAM | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100430919 | CITTÀ | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100470377 | CITALOPRAM | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100630281 | BROMIDRATO DE CITALOPRAM | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100681143 | CITALOPRAM | NOVARTIS BIOCIENCIAS S.A | Cancelado |
| 100890286 | CITALOPRAM | MERCK S/A | Cancelado |
| 100890297 | CITALOPRAM | MERCK S/A | Cancelado |
| 100890345 | CELAPRAM | MERCK S/A | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro), de 55 registros nos dados. A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

<!-- licenses:end -->

Segundo os dados de registro, o citalopram consta como comercializado no Brasil, com registros válidos e cancelados (números atualizados no resumo rápido e na tabela acima).

<!-- review:begin br-lic-20261125-citalopram-1 -->

> **Correção de verificação (2026-11-25)**: Texto original: “com 5 registros válidos e 15 cancelados; a lista de registros pode estar incompleta.” Corrigido conforme os dados abertos de medicamentos da ANVISA: os números citados vinham de dados que incluíam registros de escitalopram (outro fármaco, o enantiômero S do citalopram), já retirados; a tabela acima traz todos os registros de citalopram nos dados (os números atualizados estão no resumo rápido e na tabela). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261125-citalopram-1 -->

## Considerações de Segurança

- **Contraindicações e condições de risco a considerar**: os dados compilados apontam relação de risco com síndrome do QT longo (inclusive familiar), torsades de pointes, epilepsia, transtorno bipolar, doença hepática, doença da vesícula biliar, deficiência de potássio, distúrbios de coagulação, doença cardíaca e cardiovascular, síndrome neuroléptica maligna, síndrome de secreção inapropriada de ADH e síndrome serotoninérgica. Estas informações não vêm de texto de bula.
- **Interações medicamentosas**: foram registradas 100 interações. Entre as de nível maior estão bupropiona, omeprazol, cimetidina, cisaprida, claritromicina, lorcasserina, dexfenfluramina, dietilpropiona e dolasetrona. Há também interações moderadas (por exemplo, famotidina, loperamida, morfina, ácido acetilsalicílico) e menores (aprepitanto, clotrimazol).
- **Pontos de atenção**: prolongamento do intervalo QT dose-dependente, risco de suicídio e dose adequada à idade no uso pediátrico.

Consulte a bula para as advertências oficiais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- O mecanismo da classe ISRS é coerente com o TOC e há estudos clínicos pequenos, em sua maioria abertos, com o próprio citalopram nessa condição. Faltam, porém, ensaios controlados robustos e dados de bula, o que justifica avançar com cautela.

**Para prosseguir, é necessário:**
- Obter as advertências e contraindicações da bula na ANVISA
- Confirmar o mecanismo de ação a partir de fonte oficial
- Buscar ou conduzir ensaios controlados com citalopram especificamente no TOC
- Estabelecer plano de monitoramento do QT e de triagem de interações medicamentosas
- Definir cuidados específicos para o uso pediátrico (risco de suicídio e dose por idade)

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Celexa (citalopram) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4259d9b1-de34-43a4-85a8-41dd214e9177) |
| 2026-11-25 | “com 5 registros válidos e 15 cancelados; a lista de registros pode estar incompleta.” → “com registros válidos e cancelados (números atualizados no resumo rápido e na tabela acima).” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

