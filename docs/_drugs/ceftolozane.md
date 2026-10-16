---
layout: default
title: Ceftolozane
parent: Apenas Predição do Modelo (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceftolozane: nova indicação prevista, Uretrite por Ureaplasma (Ureaplasma urethritis) (nível de evidência L5). Indicação original: Outras cefalosporinas e penêmicos"
monitor_inn: "ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
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

# Ceftolozana: De outras cefalosporinas e penêmicos para uretrite por Ureaplasma

## Resumo em Uma Frase

Ceftolozana é um antibiótico beta-lactâmico (cefalosporina), registrado na ANVISA na categoria "outras cefalosporinas e penêmicos".
O modelo TxGNN prevê que pode ser eficaz para **Uretrite por Ureaplasma (Ureaplasma urethritis)**, mas **não há ensaios clínicos nem publicações** que apoiem essa previsão. Além disso, a plausibilidade biológica é muito baixa.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outras cefalosporinas e penêmicos |
| Nova Indicação Prevista | Uretrite por Ureaplasma (Ureaplasma urethritis) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a ceftolozana é uma cefalosporina que inibe a síntese da parede celular bacteriana, otimizada para *Pseudomonas aeruginosa* e bacilos Gram-negativos multirresistentes. Está disponível apenas como combinação intravenosa com tazobactam.

**Neste caso, a previsão não parece razoável.** As espécies de *Ureaplasma* não possuem parede celular, de modo que os beta-lactâmicos são esperados como intrinsecamente ineficazes. A pontuação alta do TxGNN provavelmente é um artefato do grafo de conhecimento associado à classe "uretrite", e não reflete plausibilidade biológica.

Outras previsões do modelo também foram avaliadas. Uretrite gonocócica e doença inflamatória uterina têm vínculo apenas indireto, por efeito de classe, e já existem tratamentos de primeira linha estabelecidos. Pielonefrite xantogranulomatosa tem relação indireta com infecções urinárias, mas exige tratamento cirúrgico. Já as demais previsões (síndrome de hiperviscosidade policlonal, hiperamilasemia, tuberculose urogenital, analbuminemia congênita, incompatibilidade de grupo sanguíneo e doença hematológica pré-maligna) não têm base mecanística plausível.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (uretrite por Ureaplasma), atualmente não há literatura relacionada. A única publicação identificada entre as previsões avaliadas refere-se à pielonefrite xantogranulomatosa (previsão de posição 4), e é uma evidência indireta:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Revisão | Current Opinion in Infectious Diseases | Revisão geral sobre infecções urinárias febris, incluindo pielonefrite e urossepse; não avalia a ceftolozana diretamente |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101710231 (cancelado) | ZERBAXA | Não informada | Outras cefalosporinas e penêmicos |

## Considerações de Segurança

**Interações Medicamentosas** (11 interações de gravidade moderada identificadas):
- **Aminoglicosídeos**: canamicina, neomicina, estreptomicina, amicacina (inclusive lipossomal) e gentamicina
- **Anticoagulantes**: dicumarol e varfarina
- **Outros**: cloranfenicol, etinilestradiol e ácido micofenólico

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas no modelo (L5), sem ensaios clínicos nem literatura. Além disso, a ausência de parede celular no *Ureaplasma* torna o mecanismo da ceftolozana biologicamente implausível. O único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação confirmados (DrugBank)
- Advertências e contraindicações extraídas da bula na ANVISA
- Dados de sensibilidade *in vitro* de *Ureaplasma* à ceftolozana, que provavelmente refutariam a hipótese
- Se houver interesse em reposicionamento, priorizar indicações com plausibilidade biológica, como infecções urinárias complicadas ou intra-abdominais por Gram-negativos, e não as previsões de maior pontuação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

