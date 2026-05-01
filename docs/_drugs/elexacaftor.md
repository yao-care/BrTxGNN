---
layout: default
title: Elexacaftor
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Elexacaftor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Elexacaftor: Da Fibrose Cística à Artrite Reumatoide

## Resumo em Uma Frase

Elexacaftor é um corretor da proteína CFTR, comercializado como parte da combinação tripla Elexacaftor/Tezacaftor/Ivacaftor (ETI) para o tratamento da Fibrose Cística (FC) em pacientes com pelo menos uma mutação F508del.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, atualmente com **1 ensaio clínico** de relevância indireta e **nenhuma publicação** direta apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Fibrose Cística (Cystic Fibrosis) |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 98,11% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Elexacaftor é um corretor molecular do CFTR (Cystic Fibrosis Transmembrane conductance Regulator): ele estabiliza o dobramento da proteína CFTR mutante F508del, permitindo que ela seja processada e transportada corretamente até a membrana celular. Atualmente, não há dados detalhados sobre o mecanismo de ação completo disponíveis neste Evidence Pack. Com base no conhecimento estabelecido, Elexacaftor faz parte da combinação ETI (Trikafta®/Kaftrio®) — sua eficácia na Fibrose Cística está amplamente documentada como modulador primário da proteína CFTR.

O elo hipotético com a Artrite Reumatoide parte da observação de que o CFTR é expresso em neutrófilos e linfócitos T. Pacientes com FC apresentam disfunção de neutrófilos e inflamação sistêmica exacerbada (elevação de IL-8 e TNF-α), marcadores inflamatórios que também desempenham papel central na patogênese da AR. Estudos recentes demonstram que o tratamento com ETI altera o fenótipo e a função dos neutrófilos circulantes em pacientes com FC, o que fornece uma pista biológica inicial para a sobreposição entre as duas condições.

Contudo, esta conexão permanece altamente especulativa. Não existe nenhum estudo mecanístico que investigue diretamente o efeito do Elexacaftor no tecido sinovial ou nas células imunes articulares características da AR. A previsão do TxGNN reflete, provavelmente, a sobreposição de vias inflamatórias no grafo de conhecimento — e não evidências clínicas ou pré-clínicas estabelecidas para esta indicação.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Concluído | 47 | Estudo prospectivo analisando função e fenótipo de neutrófilos em pacientes com FC, avaliando o impacto da infecção crônica por *Pseudomonas aeruginosa*, do tratamento com moduladores CFTR e de exacerbações agudas. Relevância para AR classificada como indireta (Grau C): neutrófilos são componentes do processo inflamatório articular, mas o ensaio não foi desenhado para AR e não constitui evidência de reposicionamento. |

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Elexacaftor está registrado no Brasil com **2 registros ativos** e situação de comercialização confirmada. Os detalhes individuais de cada registro (número do registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no presente Evidence Pack. Consulte o banco de dados da ANVISA para informações completas dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para Artrite Reumatoide apoia-se em sobreposição de vias inflamatórias no grafo de conhecimento (CFTR em neutrófilos/células T), sem qualquer evidência pré-clínica ou clínica direta nesta indicação. O único ensaio recuperado é tangencial (foco em fenótipo de neutrófilos em FC), e nenhuma publicação direta foi identificada — configurando nível de evidência L5 e estágio de decisão S0.

> **Observação estratégica:** Embora Artrite Reumatoide seja a indicação com maior pontuação TxGNN (98,11%), a análise do Evidence Pack revela que **Hipertensão Pulmonar** (rank 10, score 97,45%) apresenta evidências substancialmente mais sólidas: 1 ensaio clínico com relevância Grau B (NCT07363304, 150 participantes em recrutamento), 7 publicações incluindo dados de MRI funcional mostrando melhora de perfusão pulmonar pós-ETI, e mecanismo biológico direto (melhora de CFTR → melhora V/Q → redução de HP secundária à hipóxia). Nível de evidência L4, estágio S1. Recomenda-se avaliar Hipertensão Pulmonar como candidatura prioritária para aprofundamento.

**Para prosseguir com Artrite Reumatoide, é necessário:**
- Estudos pré-clínicos em modelos animais de AR tratados com moduladores CFTR
- Dados de MOA detalhados para Elexacaftor (obter via DrugBank API — DG002)
- Análise de expressão de CFTR em sinoviócitos e células imunes do líquido sinovial
- Avaliação de segurança completa (download e análise da bula — DG001 Blocking)
- Revisão de literatura expandida (CFTR + inflamação autoimune + neutrófilos)
---

