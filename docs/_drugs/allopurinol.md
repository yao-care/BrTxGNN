---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: Da Hiperuricemia à Porfiria Hepática

## Resumo em Uma Frase

Allopurinol é um inibidor da xantina oxidase (XO) clássico, utilizado no tratamento da gota e da hiperuricemia. O modelo TxGNN prevê que pode ser eficaz para a **Porfiria Hepática (Hepatic Porphyria)**, com **0 ensaios clínicos** e **2 publicações** indiretamente relacionadas disponíveis como suporte. As evidências identificadas são hipotéticas e indiretas, indicando que esta direção ainda requer validação experimental dedicada antes de qualquer consideração clínica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Gota e hiperuricemia |
| Nova Indicação Prevista | Porfiria Hepática (Hepatic Porphyria) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento farmacológico estabelecido, allopurinol inibe competitivamente a xantina oxidase (XO), enzima responsável pela conversão de hipoxantina e xantina em ácido úrico. Como efeito secundário, essa inibição reduz a produção de espécies reativas de oxigênio (ROS) geradas pela XO, conferindo ao fármaco propriedades antioxidantes adicionais.

A porfiria hepática aguda tem como evento central a hiperativação da 5-aminolevulinato sintase 1 (ALAS1), enzima limitante da biossíntese do heme hepático. A hipótese de conexão metabólica, proposta em publicação recente (PMID 31443750), sugere que o catabolismo das purinas — via XO — pode interferir na regulação do pool de heme livre no citosol hepático. A inibição da XO pelo allopurinol poderia, teoricamente, reduzir essa interferência e aliviar a pressão sobre ALAS1, moderando a produção excessiva de precursores tóxicos do heme característicos das crises porfíricas.

Contudo, essa conexão permanece no nível de hipótese especulativa. Nenhum estudo experimental testou diretamente o allopurinol em modelos de porfiria hepática. A pontuação elevada do TxGNN (99,95%) provavelmente reflete similaridades estruturais no grafo de conhecimento entre as vias metabólicas envolvidas, e não evidência clínica ou pré-clínica direta. A previsão merece investigação, mas requer validação básica antes de qualquer avanço.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hipótese / Revisão narrativa | *Medical Hypotheses* | Propõe alvo metabólico de ALAS1 via inibição do uso de heme pela triptofano 2,3-dioxigenase (TDO) como terapia para porfirias hepáticas agudas; allopurinol não é testado diretamente, mas a via XO é mencionada no contexto do metabolismo das purinas |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Estudo animal (rato) | *Biochemical Pharmacology* | Examina efeitos agudos de carbamazepina sobre o metabolismo hepático do heme em ratos, incluindo a depleção do pool de heme regulatório e indução de ALAS1; allopurinol não é o objeto do estudo, mas o modelo experimental é relevante para entender a dinâmica porfírica |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação TxGNN elevada (99,95%), o nível de evidência é L4 — sustentado exclusivamente por hipóteses mecanísticas indiretas e estudos em modelos animais não relacionados diretamente ao allopurinol. A ausência total de ensaios clínicos e de estudos experimentais dedicados impede qualquer avanço responsável sem etapas de validação prévias.

**Para prosseguir, é necessário:**
- Conduzir estudos pré-clínicos dedicados (modelos murinos de porfiria aguda ou culturas de hepatócitos) testando allopurinol diretamente
- Obter dados completos de mecanismo de ação (MOA) via consulta à API do DrugBank
- Recuperar informações de segurança, advertências e contraindicações da bula oficial (ANVISA)
- Avaliar a situação regulatória e viabilidade de registro no Brasil, dado que o fármaco não está comercializado no país
- Ampliar a busca na literatura com termos combinados (allopurinol + xanthine oxidase + heme biosynthesis + ALAS1) para identificar eventuais evidências mecanísticas mais robustas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

