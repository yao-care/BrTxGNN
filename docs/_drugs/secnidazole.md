---
layout: default
title: Secnidazole
parent: Apenas Predição do Modelo (L5)
nav_order: 580
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "Secnidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vaginal discharge", "vulvar neoplasm", "leukoplakia of vagina", "vulvovaginal candidiasis"]
description: "Secnidazole: nova indicação prevista, Postmenopausal atrophic vaginitis (nível de evidência L5). Indicação original: AMEBICIDAS, GIARDICIDAS E TRICOMONICIDAS"
---

# Secnidazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Secnidazole: Postmenopausal atrophic vaginitis
{: .text-alpha }

## Resumo em Uma Frase

Secnidazol é um antimicrobiano da classe dos 5-nitroimidazóis, originalmente registrado no Brasil como amebicida, giardicida e tricomonicida.
O modelo TxGNN prevê que pode ser eficaz para **corrimento vaginal (vaginal discharge)**,
atualmente com **3 ensaios clínicos** e **17 publicações** apoiando esta direção.

*Observação:* a previsão de maior pontuação do modelo é "vaginite atrófica pós-menopausa". Ela não tem nenhuma evidência e, mecanisticamente, não é plausível. Por isso, este relatório destaca a previsão de maior suporte (corrimento vaginal), que é, na prática, uma extensão da indicação original e não um reposicionamento propriamente dito.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | AMEBICIDAS, GIARDICIDAS E TRICOMONICIDAS |
| Nova Indicação Prevista | Postmenopausal atrophic vaginitis |
| Pontuação de Previsão TxGNN | 0.9970 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 22 de 61) |
| Número de Registros | 61 (ativos: 22) |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o secnidazol é um 5-nitroimidazol, da mesma classe do metronidazol e do tinidazol. Sua forma reduzida danifica o DNA de bactérias anaeróbias e protozoários. Tem meia-vida longa (cerca de 17 horas, contra cerca de 8 horas do metronidazol), o que permite tratamento em dose única.

Corrimento vaginal é um sintoma, causado na maioria das vezes por vaginose bacteriana ou tricomoníase. Ambas são sensíveis aos 5-nitroimidazóis. Por isso, a previsão se sobrepõe em grande parte à indicação original (tricomonicida) e é mais uma extensão de indicação do que um reposicionamento novo.

Importante: as evidências disponíveis referem-se à vaginose bacteriana e à tricomoníase, não ao corrimento como sintoma isolado. O secnidazol não é eficaz contra candidíase (fungo) nem contra causas virais, como o herpes. Nesses casos, é necessário identificar o agente causal antes do uso.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Phase 3 | Concluído | 147 | Ensaio randomizado, duplo-cego e controlado por placebo de dose oral única de secnidazol 2 g em mulheres com tricomoníase; é a evidência direta de eficácia mais forte do grupo |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Phase 3 | Concluído | 118 | Fluconazol + secnidazol para corrimento vaginal sintomático (vaginite mista); por ser uma combinação, é difícil atribuir o efeito ao secnidazol isolado |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Phase 4 | Concluído | 40 | Estudo aberto de segurança com dose única de secnidazol 2 g em adolescentes com vaginose bacteriana; apoia a segurança, mas não a eficácia comparativa |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33768237](https://pubmed.ncbi.nlm.nih.gov/33768237/) | 2021 | RCT (Fase 3) | Clin Infect Dis | Eficácia e segurança de secnidazol oral em dose única versus placebo na tricomoníase em mulheres |
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | RCT (Fase 3) | Am J Obstet Gynecol | Secnidazol 2 g em dose única versus placebo na vaginose bacteriana |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | RCT (Fase 3) | Infect Dis Obstet Gynecol | Estudo duplo-cego de não inferioridade: secnidazol versus metronidazol na vaginose bacteriana |
| [28697102](https://pubmed.ncbi.nlm.nih.gov/28697102/) | 2017 | RCT (Fase 2) | Obstet Gynecol | Secnidazol em dose única oral versus placebo na vaginose bacteriana |
| [29132478](https://pubmed.ncbi.nlm.nih.gov/29132478/) | 2017 | RCT | JCPSP | Clindamicina vaginal em múltiplas doses versus secnidazol oral em dose única na vaginose bacteriana |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Revisão sistemática e meta-análise | Eur J Obstet Gynecol Reprod Biol | Eficácia e segurança de secnidazol 2 g em dose única na vaginose bacteriana |
| [31638955](https://pubmed.ncbi.nlm.nih.gov/31638955/) | 2019 | Revisão sistemática | BMC Womens Health | Efetividade do secnidazol no tratamento da vaginose bacteriana |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Revisão sistemática e meta-análise em rede | Front Cell Infect Microbiol | Comparação de eficácia e segurança de vários fármacos para vaginose bacteriana |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | Estudo comparativo | Indian J Pharmacol | Taxas de cura de dose única de metronidazol, tinidazol, secnidazol e ornidazol na vaginose bacteriana |
| [37550019](https://pubmed.ncbi.nlm.nih.gov/37550019/) | 2023 | Análise post hoc de subgrupo (Fase 3) | BMJ Open | Eficácia do secnidazol em dose única na tricomoníase em mulheres coinfectadas com vaginose bacteriana |

---

## Informações de Comercialização no Brasil

O medicamento está comercializado no Brasil. Os 5 principais:

<!-- review:begin br-lic-20261106-secnidazole-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Há 20 registros válidos de secnidazol nos dados compilados, e o medicamento está comercializado no Brasil.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 61 registros para este medicamento, 22 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-secnidazole-1 -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100380096 | SECTIL | BRASTERAPICA PHARMACEUTICA LTDA. | Ativo |
| 100380097 | SECNIDAZOL | BRASTERAPICA PHARMACEUTICA LTDA. | Ativo |
| 100470297 | SECNIHEXAL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100470559 | SECNIDAZOL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 102350670 | SECNIDAZOL | EMS S/A | Ativo |
| 103700456 | SECNIDAZOL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103850093 | SECFAR | LABORATÓRIO FARMACÊUTICO ELOFAR LTDA | Ativo |
| 103900165 | GYNOPAC | FARMOQUÍMICA S/A | Ativo |
| 103920107 | SECDAZOL | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920194 | SECNIDAZOL | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 105350110 | SECNIMAX | LABORATÓRIO GLOBO SA | Ativo |
| 105350187 | SECNIDAZOL | LABORATÓRIO GLOBO SA | Ativo |
| 105830947 | SECNIDAZOL | GERMED FARMACEUTICA LTDA | Ativo |
| 118190323 | SECNIDAZOL | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 118190411 | NQUÍASE | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 123520145 | SECNIDAZOL | RANBAXY FARMACÊUTICA LTDA | Ativo |
| 125680172 | SECNIDAZOL | PRATI DONADUZZI & CIA LTDA | Ativo |
| 135690590 | UNIGYN | EMS SIGMA PHARMA LTDA | Ativo |
| 141070131 | SECNIDAZOL | PHARLAB INDÚSTRIA FARMACÊUTICA S.A. | Ativo |
| 141070639 | DECNAZOL | PHARLAB INDÚSTRIA FARMACÊUTICA S.A. | Ativo |
| 164250013 | SECNIDAL | MOKSHA8 BRASIL INDUSTRIA E COMERCIO DE MEDICAMENTO | Ativo |
| 183260071 | SECNIDAZOL | SANOFI MEDLEY FARMACÊUTICA LTDA. | Ativo |
| 100380067 | SECTIL | BRASTERAPICA PHARMACEUTICA LTDA. | Cancelado |
| 100470527 | SECNIDAZOL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100890348 | SECNIDAZOL | MERCK S/A | Cancelado |
| 100930258 | SECSIM | MANTECORP INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A. | Cancelado |
| 101810380 | SECNIDAZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 102350531 | SECNAXIDOL | EMS S/A | Cancelado |
| 102351294 | SECNAXIDOL | EMS S/A | Cancelado |
| 102940098 | SECNIDALIN | NEOLATINA COMÉRCIO E INDÚSTRIA FARMACEUTICA S.A | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

---

## Considerações de Segurança

- **Interações Medicamentosas:** foram identificadas 92 interações, sendo as listadas abaixo de gravidade moderada. Entre as principais:
  - Outros nitroimidazóis: metronidazol e tinidazol
  - Estatinas: rosuvastatina, sinvastatina e atorvastatina
  - Antineoplásicos: paclitaxel, carboplatina, bortezomibe, carfilzomibe, cabazitaxel, brentuximabe vedotina e trastuzumabe entansina
  - Outros: amiodarona, levodopa, adalimumabe, certolizumabe pegol, auranofina, picossulfato, iodeto I-123 e I-131

  Recomenda-se revisar a lista completa de medicamentos em uso antes da prescrição. Como cautela de classe dos nitroimidazóis, evitar também o álcool.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há ensaios de Fase 3 concluídos e controlados por placebo, além de revisões sistemáticas, para vaginose bacteriana e tricomoníase, as principais causas de corrimento vaginal. Trata-se, porém, de uma extensão da indicação original.

<!-- review:begin br-lic-20261106-secnidazole-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Trata-se, porém, de uma extensão da indicação original, e o medicamento está comercializado no Brasil, com 20 registros válidos.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 61 registros para este medicamento, 22 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-secnidazole-2 -->

**Para prosseguir, é necessário:**
- Confirmar a disponibilidade local do produto e a situação regulatória
- Obter a bula da ANVISA para advertências e contraindicações
- Obter dados do mecanismo de ação (MOA)
- Confirmar a etiologia (vaginose bacteriana, tricomoníase ou candidíase) antes do uso, com diagnóstico por NAAT ou microscopia; tratar também os parceiros na tricomoníase
- Considerar a alta taxa de recorrência da vaginose bacteriana (PMID 31403349)
- Revisar as interações medicamentosas

<!-- review:begin br-lic-20261106-secnidazole-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Confirmar a disponibilidade local do produto e a situação regulatória, já que não há registro válido” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 61 registros para este medicamento, 22 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-secnidazole-3 -->

**Outras previsões do modelo (não recomendadas no momento):**
- **Candidíase vulvovaginal** (0.9916): evidência L3; o secnidazol não tem atividade antifúngica relevante, e o único sinal vem de um estudo de combinação com fluconazol; pergunta de pesquisa.
- **Vaginite atrófica pós-menopausa** (0.9970), **úlcera vulvar**, **neoplasia vulvar**, **leucoplasia vaginal**, **vulvovaginite herpética** e **impetigo bolhoso**: sem evidência (L5), sem mecanismo plausível; Hold.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Há 20 registros válidos de secnidazol nos dados compilados, e o” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “e o medicamento está comercializado no Brasil, com 20 registros válidos” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que não há registro válido” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

