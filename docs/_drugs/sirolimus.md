---
layout: default
title: Sirolimus
parent: Evidência Moderada (L3-L4)
nav_order: 587
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Sirolimus: nova indicação prevista, Lipossarcoma (Liposarcoma) (nível de evidência L3). Indicação original: Agente imunossupressor"
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "vulva sarcoma"]
---

# Sirolimus
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **10** 
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

# Sirolimo: De agente imunossupressor para lipossarcoma

## Resumo em Uma Frase

O sirolimo (Rapamune) foi registrado no Brasil como agente imunossupressor.
O modelo TxGNN prevê que ele pode ser eficaz para **lipossarcoma (liposarcoma)**.
Hoje essa direção conta com **1 ensaio clínico** e **7 publicações**, mas sem nenhum estudo randomizado específico para a doença.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agente imunossupressor |
| Nova Indicação Prevista | Lipossarcoma (Liposarcoma) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nas informações compiladas para este relatório. Segundo informações conhecidas, o sirolimo é um inibidor da via mTOR (mTORC1), com eficácia reconhecida como imunossupressor, e mecanisticamente pode ser aplicável ao lipossarcoma.

A sinalização PI3K/AKT/mTOR costuma estar ativada em sarcomas de partes moles, incluindo o lipossarcoma. Em modelos animais, a inibição de mTOR pode frear o crescimento tumoral. Isso dá uma justificativa biológica plausível para testar o sirolimo nessa doença.

A relação com a indicação original é indireta. O uso como imunossupressor (por exemplo, em transplantes) e o uso antitumoral partilham o mesmo alvo, mas se trata de contextos clínicos distintos. Um estudo de transplante renal sugere menor risco de câncer com regimes baseados em sirolimo, porém isso diz respeito à prevenção e não ao tratamento do lipossarcoma.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Concluído | 70 | Braço único e multicêntrico, com sirolimo + ciclofosfamida em lipossarcoma mixoide e condrossarcoma metastáticos ou irressecáveis. Parte da premissa de que a inibição de mTOR pode frear o crescimento tumoral. O desenho de braço único e a combinação dificultam isolar a contribuição do sirolimo. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | Em transplante renal, a retirada precoce da ciclosporina com sirolimo reduziu o risco de câncer. A relevância é indireta, pois não se trata de sarcoma. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Revisão dos avanços moleculares e terapêuticos em sarcomas de partes moles. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Racional e resultados de ensaios com agentes-alvo em sarcomas avançados. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Tratamentos-alvo para sarcomas e tumores raros do tecido conjuntivo, agrupados por alterações moleculares. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Efeito de imunossupressores e vírus no desenvolvimento de tumores malignos em transplantados renais. Relevância indireta. |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Coorte | Fam Cancer | Coorte retrospectiva da síndrome de hamartoma tumoral PTEN, com risco aumentado de malignidade. Relevância indireta. |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Relato de caso | Diagn Pathol | Três casos de anomalia vascular fibroadiposa (FAVA), com ênfase na via mTOR. Relevância indireta. |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 121100453 (cancelado) | Rapamune | — | Agente imunossupressor |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações. Entre as de gravidade **maior** estão anfotericina B (inclusive a formulação em complexo lipídico), mesalazina, balsalazida e claritromicina. Entre as de gravidade **moderada** estão corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida e triancinolona), antidiabéticos (metformina, pioglitazona, acarbose, alogliptina, canagliflozina, dapagliflozina e clorpropamida), albiglutida, aprepitanto e cimetidina.
- **Contraindicações segundo o grafo de conhecimento do TxGNN** (relações fármaco-doença, não texto de bula): hipertensão, doença renal, doença hepática, doença da vesícula biliar, hiperglicemia e diabetes, cetoacidose diabética, hiperlipidemia e hipertrigliceridemia, doenças cerebrovasculares e AVC, hiperbilirrubinemia, doença pulmonar intersticial, infecções (incluindo pneumocistose e citomegalovírus), leucoencefalopatia multifocal progressiva, derrame pericárdico e câncer (incluindo câncer cerebral e carcinoma embrionário). A presença de "câncer" nessa lista exige avaliação cuidadosa em um contexto oncológico.

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A evidência para lipossarcoma se resume a um ensaio de Fase 2 de braço único, com combinação medicamentosa, e a literatura é composta sobretudo de revisões e dados indiretos. Não há estudo randomizado, e as advertências oficiais da bula brasileira não estavam disponíveis, o que impede a triagem de segurança.
- O registro brasileiro está cancelado, o que também limita a viabilidade local.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Obter dados do mecanismo de ação (MOA) em fontes como o DrugBank.
- Verificar os resultados publicados do NCT02821507 e a contribuição isolada do sirolimo na combinação.
- Buscar evidência randomizada ou comparativa específica para lipossarcoma.
- Avaliar o plano de monitoramento de interações e a exigência de nível sérico (vale mínimo) do sirolimo.
- Considerar a priorização de outras indicações previstas para o mesmo fármaco, com evidência mais forte. A mais robusta é a **linfangioleiomiomatose (lymphangiomyoma)**, com pontuação de 99,79%. Ela tem nível L1, incluindo o ensaio de Fase 3 MILES (NCT00414648, n=89), e é elegível a "Proceed with Guardrails".
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

