---
layout: default
title: Clomifene
parent: Apenas Predição do Modelo (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Clomifene
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Clomifeno: De produtos para uso em ginecologia e obstetrícia para anovulação

## Resumo em Uma Frase

Clomifeno (clomifene) foi originalmente registrado na ANVISA na categoria "outros produtos para uso em ginecologia e obstetrícia", sendo usado na indução da ovulação.
O modelo TxGNN prevê que pode ser eficaz para **46,XY distúrbio do desenvolvimento sexual por defeito de esteroidogênese testicular (46,XY disorder of sex development due to testicular steroidogenesis defect)**, a previsão de maior pontuação, mas **sem nenhum ensaio clínico ou publicação** que a apoie.
A previsão com maior respaldo de evidências é **anovulação (anovulation)**, com **3 ensaios clínicos** e **20 publicações**. Porém, trata-se da confirmação de um uso já estabelecido, e não de um reposicionamento novo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para uso em ginecologia e obstetrícia |
| Nova Indicação Prevista | 46,XY distúrbio do desenvolvimento sexual por defeito de esteroidogênese testicular (46,XY disorder of sex development due to testicular steroidogenesis defect) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L5 (para a previsão de maior pontuação) |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

> **Observação:** entre as 10 previsões avaliadas, a de maior pontuação (46,XY DSD) não tem evidências. Somente a 10ª, **anovulação** (pontuação de 99,52%), tem evidências reais (nível L1, decisão *Proceed with Guardrails*). Ela é analisada nas seções seguintes, pois é a única com dados clínicos.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base consultada. Segundo informações farmacológicas conhecidas, o clomifeno é um modulador seletivo do receptor de estrogênio (SERM), com ligação ao receptor de estrogênio alfa (ESR1). Ele bloqueia o *feedback* negativo do estrogênio no hipotálamo, aumentando a pulsatilidade do GnRH e a secreção de FSH e LH, o que estimula o desenvolvimento folicular e a ovulação.

**Para a previsão de maior pontuação (46,XY DSD por defeito de esteroidogênese testicular):** o vínculo mecanístico é fraco e especulativo. O defeito é uma falha enzimática primária da gônada, e aumentar as gonadotrofinas dificilmente o corrigiria. Não há evidências clínicas.

**Para anovulação:** o mecanismo descrito acima é o fundamento do uso já consolidado do clomifeno. A anovulação é o núcleo da indicação já conhecida do fármaco, portanto trata-se de confirmação e não de reposicionamento. As demais previsões (septos vaginais, síndrome do X frágil em portadoras, BPES e trissomias/tetrassomias parciais) não têm plausibilidade farmacológica evidente e provavelmente refletem a proximidade no grafo de conhecimento, sem relação causal. Em algumas (X frágil, BPES), há apenas um elo indireto com insuficiência ovariana, que o clomifeno não trataria na causa.

## Evidências de Ensaios Clínicos

Para a indicação **anovulação** (única previsão com ensaios registrados):

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00478504](https://clinicaltrials.gov/study/NCT00478504) | Phase 4 | Concluído | 159 | Ensaio randomizado, duplo-cego, cruzado, comparando letrozol com citrato de clomifeno na indução da ovulação em mulheres com síndrome dos ovários policísticos (SOP); avalia taxas de gravidez, gestações múltiplas e nascidos vivos |
| [NCT02544776](https://clinicaltrials.gov/study/NCT02544776) | Não aplicável | Concluído | 60 | Anlodipino com Clomid em pacientes com SOP: o anlodipino parece promissor para melhorar o fluxo sanguíneo uterino e ovariano, o tamanho do folículo pré-ovulatório, a progesterona na fase lútea média e o desfecho gestacional |
| [NCT07398924](https://clinicaltrials.gov/study/NCT07398924) | Não aplicável | Concluído | 90 | Estradiol vaginal versus guaifenesina oral em mulheres em indução da ovulação com citrato de clomifeno, avaliando espessura endometrial, muco cervical e taxa de gravidez clínica (o clomifeno é o agente de fundo) |

Para as demais previsões, atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para **anovulação** (10 das 20 publicações, priorizando as de maior nível de evidência):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29273245](https://pubmed.ncbi.nlm.nih.gov/29273245/) | 2018 | Ensaio randomizado fatorial (classificado como revisão sistemática Cochrane) | Lancet | Gonadotrofinas versus clomifeno, com ou sem inseminação intrauterina, em mulheres com anovulação normogonadotrófica e falha ao clomifeno (M-OVIN) |
| [22128296](https://pubmed.ncbi.nlm.nih.gov/22128296/) | 2012 | RCT | Human Reproduction | Clomifeno versus FSH em baixa dose como tratamento de primeira linha na anovulação associada à SOP |
| [35351379](https://pubmed.ncbi.nlm.nih.gov/35351379/) | 2022 | Revisão sistemática/meta-análise | Reprod Biomed Online | Influência da etnia nos resultados da indução da ovulação com clomifeno na SOP |
| [14576245](https://pubmed.ncbi.nlm.nih.gov/14576245/) | 2003 | Revisão sistemática/meta-análise | BMJ | Eficácia da metformina na SOP |
| [12917943](https://pubmed.ncbi.nlm.nih.gov/12917943/) | 2003 | Revisão sistemática (Cochrane) | Cochrane Database Syst Rev | Fármacos sensibilizadores da insulina na SOP |
| [18487613](https://pubmed.ncbi.nlm.nih.gov/18487613/) | 2008 | Análise de subgrupos de RCT | Human Reproduction | Avalia se a adição de metformina ao clomifeno aumenta a gravidez em subgrupos de mulheres com SOP |
| [17137400](https://pubmed.ncbi.nlm.nih.gov/17137400/) | 2006 | Revisão | Drugs | Inibidores de aromatase na indução da ovulação; o clomifeno é a primeira linha há quase meio século, mas tem efeitos antiestrogênicos no endométrio e no muco cervical e risco de gestação múltipla |
| [21406133](https://pubmed.ncbi.nlm.nih.gov/21406133/) | 2010 | Revisão | BMJ Clin Evid | Visão geral da infertilidade feminina e suas causas, incluindo falha ovulatória |
| [31296604](https://pubmed.ncbi.nlm.nih.gov/31296604/) | 2019 | Revisão | J Clin Pathol | Investigação e manejo da subfertilidade |
| [8521770](https://pubmed.ncbi.nlm.nih.gov/8521770/) | 1995 | Revisão (tipo não classificado) | Drugs | O clomifeno é geralmente a primeira escolha na amenorreia; menotropinas ou GnRH quando falha |

Para as demais previsões, atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 135690591 (cancelado) | INDUX | Não informada | Outros produtos para uso em ginecologia e obstetrícia |
| Registro nº 183260245 (cancelado) | CLOMID | Não informada | Outros produtos para uso em ginecologia e obstetrícia |

## Considerações de Segurança

- **Contraindicações (baseadas no grafo de conhecimento TxGNN, não no texto da bula):** transtornos de ansiedade, transtornos neuróticos e distimia; doença hepática; doença da vesícula biliar; hipotireoidismo (incluindo mixedema e hipotireoidismo congênito); insuficiência adrenal (doença de Addison); tromboflebite; síndrome dos ovários policísticos; endometriose; câncer de endométrio/corpo uterino; tireotoxicose/hipertireoidismo/doença de Graves; tumores hipofisários; cisto ovariano; síndrome de hiperestimulação ovariana; distúrbios visuais e cegueira.
- **Interações medicamentosas:** interação **grave (Major)** com **bexaroteno**. Também há dados farmacológicos de ligação ao receptor de estrogênio alfa (ESR1) e ao canal VRAC, sem classificação de gravidade.
- **Monitoramento sugerido para anovulação:** gestação múltipla, hiperestimulação ovariana e limite de duração do tratamento.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold** (para a previsão de maior pontuação, 46,XY DSD e as demais previsões sem evidências)
**Anovulação: Proceed with Guardrails**, ressalvando que se trata de uso já estabelecido, e não de reposicionamento novo.

**Justificativa:**
- A previsão de maior pontuação (99,90%) é puramente computacional, sem ensaios, sem literatura e com mecanismo implausível; deve permanecer em espera (nível L5).
- Para anovulação, há um ensaio de Fase 4 concluído, duplo-cego e randomizado, além de várias revisões sistemáticas. Porém, as evidências são principalmente comparativas ou em subpopulações com SOP, e ambos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA com advertências e contraindicações (lacuna de dados bloqueante para a triagem de segurança)
- Obter dados detalhados do mecanismo de ação (MOA), por exemplo via DrugBank
- Verificar a situação regulatória atual do clomifeno no Brasil (registros hoje apenas cancelados) e a existência de outros produtos vigentes
- Definir plano de monitoramento para gestação múltipla, hiperestimulação ovariana e limite de duração do tratamento
- Não avançar com as previsões sem evidências (46,XY DSD, septos vaginais, X frágil, BPES, trissomias/tetrassomias) sem estudos pré-clínicos ou clínicos que sustentem um mecanismo plausível
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

