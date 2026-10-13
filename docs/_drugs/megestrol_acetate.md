---
layout: default
title: Megestrol Acetate
parent: Evidência Alta (L1-L2)
nav_order: 439
evidence_level: L2
indication_count: 10
---

# Megestrol Acetate
{: .fs-9 }

Nível de evidência: **L2** | Indicações previstas: **10** 
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

# Acetato de Megestrol: De antineoplásico (indicação genérica) para carcinoma endometrial do corpo uterino

## Resumo em Uma Frase

O acetato de megestrol é uma progestina sintética, registrada no Brasil com a indicação genérica de "antineoplásico".
O modelo TxGNN prevê que pode ser eficaz para **carcinoma endometrial do corpo uterino (uterine corpus endometrial carcinoma)**,
atualmente com **1 ensaio clínico** (Phase 2, concluído) apoiando esta direção. Não há literatura específica associada a esta indicação nos dados compilados.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Carcinoma endometrial do corpo uterino (uterine corpus endometrial carcinoma) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 (0 válidos, 1 cancelado) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

O acetato de megestrol é uma progestina sintética que atua nos receptores de progesterona. A terapia com progestágenos é uma abordagem hormonal estabelecida para o carcinoma endometrial com receptores hormonais positivos, pois induz diferenciação e supressão do crescimento das células endometriais. Atualmente, não há dados detalhados de mecanismo de ação no registro do fármaco; a descrição acima baseia-se no conhecimento farmacológico geral da classe.

A indicação original (antineoplásico, de forma genérica) já situa o fármaco em oncologia, e o câncer endometrial é um tumor classicamente sensível a hormônios. Por isso, o uso de um progestágeno nesse cenário tem lógica biológica.

O ensaio disponível (NCT00729586) é um estudo Phase 2 randomizado e concluído, em que um regime hormonal contendo megestrol (com tamoxifeno) foi comparado com temsirolimus. Como a pergunta principal do estudo era sobre o temsirolimus, a evidência para o megestrol isolado é indireta.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Concluído | 73 | Temsirolimus isolado ou associado a terapia hormonal (megestrol + tamoxifeno) em câncer endometrial avançado, persistente ou recorrente. O megestrol faz parte de um braço combinado, o que limita a atribuição do efeito ao fármaco isolado. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 106460123 (cancelado) | FEMIGESTROL | Não informada | Antineoplásico |

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
- Há um ensaio Phase 2 randomizado e concluído em câncer endometrial com regime que inclui megestrol, e a progestina tem fundamento hormonal plausível nessa doença. Contudo, a evidência é indireta (braço combinado), não há literatura específica para esta indicação, e o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar os resultados do NCT00729586, especialmente a contribuição do braço com megestrol.
- Obter a bula da ANVISA para avaliar advertências e contraindicações (lacuna de dados bloqueante para a triagem de segurança).
- Confirmar o mecanismo de ação em fontes como o DrugBank.
- Definir a situação regulatória: o registro está cancelado, e seria necessário um novo registro ou outra via de acesso.
- Estabelecer plano de monitoramento para pacientes com diabetes, hipertensão e doença hepática/renal, além de avaliar interações com antidiabéticos.

## Outras Previsões do Modelo (Contexto)

A previsão com melhor sustentação é a de câncer de ovário, que tem um ensaio Phase 3 concluído (NCT00005975, n=288) e estudos Phase 2 de megestrol em doença refratária à platina (PMID 11593052, PMID 9856656). No entanto, o ensaio Phase 3 avaliou fogachos em mulheres tratadas para câncer de mama, não atividade antitumoral, e resultados não foram fornecidos; por isso, esse nível L1 deve ser interpretado com cautela e a recomendação é tratá-la como questão de pesquisa. As demais previsões (por exemplo, carcinossarcoma uterino, com evidência apenas indireta, e tumores raros) permanecem em **Hold**, com evidência limitada à previsão do modelo.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

