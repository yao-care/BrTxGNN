---
layout: default
title: Megestrol Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 439
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
description: "Megestrol Acetate: nova indicação prevista, Hereditary breast ovarian cancer syndrome (nível de evidência L5). Indicação original: ANTINEOPLASICO"
---

# Megestrol Acetate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Megestrol Acetate: Hereditary breast ovarian cancer syndrome
{: .text-alpha }

## Resumo em Uma Frase

O acetato de megestrol é uma progestina sintética, registrada no Brasil com a indicação genérica de "antineoplásico".
O modelo TxGNN prevê que pode ser eficaz para **carcinoma endometrial do corpo uterino (uterine corpus endometrial carcinoma)**,
atualmente com **1 ensaio clínico** (Phase 2, concluído) apoiando esta direção. Não há literatura específica associada a esta indicação nos dados compilados.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTINEOPLASICO |
| Nova Indicação Prevista | Hereditary breast ovarian cancer syndrome |
| Pontuação de Previsão TxGNN | 0.9989 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

O acetato de megestrol é uma progestina sintética que atua nos receptores de progesterona. A terapia com progestágenos é uma abordagem hormonal estabelecida para o carcinoma endometrial com receptores hormonais positivos, pois induz diferenciação e supressão do crescimento das células endometriais. Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Megestrol Acetate (tradução não oficial): “Vários pesquisadores relataram a propriedade estimulante do apetite do acetato de megestrol e seu possível uso na caquexia. O mecanismo exato pelo qual o acetato de megestrol produz efeitos na anorexia e na caquexia é desconhecido até o momento.” Texto original em inglês: "Several investigators have reported on the appetite enhancing property of megestrol acetate and its possible use in cachexia. The precise mechanism by which megestrol acetate produces effects in anorexia and cachexia is unknown at the present time." ([DailyMed: megestrol acetate prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc921d5-e423-4379-a345-151e87d13651), versão de 2026-04-14; acessado em 2026-11-19).

A indicação original (antineoplásico, de forma genérica) já situa o fármaco em oncologia, e o câncer endometrial é um tumor classicamente sensível a hormônios. Por isso, o uso de um progestágeno nesse cenário tem lógica biológica.

O ensaio disponível (NCT00729586) é um estudo Phase 2 randomizado e concluído, em que um regime hormonal contendo megestrol (com tamoxifeno) foi comparado com temsirolimus. Como a pergunta principal do estudo era sobre o temsirolimus, a evidência para o megestrol isolado é indireta.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Concluído | 73 | Temsirolimus isolado ou associado a terapia hormonal (megestrol + tamoxifeno) em câncer endometrial avançado, persistente ou recorrente. O megestrol faz parte de um braço combinado, o que limita a atribuição do efeito ao fármaco isolado. |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 106460123 | FEMIGESTROL | Ativo |

<!-- licenses:end -->

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal (progestina), não é citotóxico convencional |
| Risco de Mielossupressão | Baixo (sem dados específicos compilados; consulte a bula) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Glicemia, pressão arterial, função hepática e renal; função adrenal em uso prolongado ou em altas doses |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento (não provenientes da bula)**: hipertensão, doença renal, doença hepática, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, insuficiência adrenocortical (doença de Addison), hipogonadismo masculino, menopausa precoce e síndrome de insensibilidade androgênica.
- **Interações Medicamentosas**: foram identificadas 100 interações, das quais as principais listadas (todas de nível moderado) são com antidiabéticos: acarbose, metformina, pioglitazona, glimepirida, repaglinida, clorpropamida, inibidores de DPP-4 (alogliptina, linagliptina, saxagliptina, sitagliptina), inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), agonistas de GLP-1 (albiglutida, dulaglutida, semaglutida) e insulinas (asparte, degludeca). Também há interação moderada com aprepitanto e claritromicina. O efeito sobre a glicemia é coerente com a contraindicação em hiperglicemia/diabetes.
- Os dados de advertências e contraindicações da bula brasileira não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há um ensaio Phase 2 randomizado e concluído em câncer endometrial com regime que inclui megestrol, e a progestina tem fundamento hormonal plausível nessa doença. Contudo, a evidência é indireta (braço combinado), não há literatura específica para esta indicação.

<!-- review:begin br-lic-20261106-megestrol_acetate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Contudo, a evidência é indireta (braço combinado), não há literatura específica para esta indicação, e o único registro brasileiro está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-megestrol_acetate-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar os resultados do NCT00729586, especialmente a contribuição do braço com megestrol.
- Obter a bula da ANVISA para avaliar advertências e contraindicações (lacuna de dados bloqueante para a triagem de segurança).
- Confirmar o mecanismo de ação em fontes como o DrugBank.
- Estabelecer plano de monitoramento para pacientes com diabetes, hipertensão e doença hepática/renal, além de avaliar interações com antidiabéticos.

<!-- review:begin br-lic-20261106-megestrol_acetate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Confirmar o mecanismo de ação em fontes como o DrugBank. / Definir a situação regulatória: o registro está cancelado, e seria necessário um novo registro ou outra via de acesso.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-megestrol_acetate-2 -->

## Outras Previsões do Modelo (Contexto)

A previsão com melhor sustentação é a de câncer de ovário, que tem um ensaio Phase 3 concluído (NCT00005975, n=288) e estudos Phase 2 de megestrol em doença refratária à platina (PMID 11593052, PMID 9856656). No entanto, o ensaio Phase 3 avaliou fogachos em mulheres tratadas para câncer de mama, não atividade antitumoral, e resultados não foram fornecidos; por isso, esse nível L1 deve ser interpretado com cautela e a recomendação é tratá-la como questão de pesquisa. As demais previsões (por exemplo, carcinossarcoma uterino, com evidência apenas indireta, e tumores raros) permanecem em **Hold**, com evidência limitada à previsão do modelo.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “e o único registro brasileiro está cancelado” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Definir a situação regulatória: o registro está cancelado, e seria necessário um novo registro ou outra via de acesso” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-12 | Tabela: registro 106460123 (FEMIGESTROL) está ativo, não cancelado | Substituído pela tabela de registros gerada por programa (antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: megestrol acetate prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc921d5-e423-4379-a345-151e87d13651) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

