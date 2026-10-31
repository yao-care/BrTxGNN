---
layout: default
title: Posaconazole
parent: Apenas Predição do Modelo (L5)
nav_order: 535
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Posaconazole: nova indicação prevista, Pneumocistose (Pneumocystosis) (nível de evidência L4). Indicação original: Antimicóticos sistêmicos"
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Posaconazol: De antimicótico sistêmico à pneumocistose
{: .text-alpha }

## Resumo em Uma Frase

Posaconazol é um antifúngico triazólico, registrado no Brasil na categoria "antimicóticos sistêmicos" (NOXAFIL).
O modelo TxGNN prevê que pode ser eficaz para **pneumocistose (Pneumocystosis)**, mas há apenas **1 ensaio clínico** (que não testa o posaconazol diretamente) e **5 publicações** (todas de caráter geral) ligados a essa direção. Na prática, a previsão carece de apoio direto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimicóticos sistêmicos |
| Nova Indicação Prevista | Pneumocistose (Pneumocystosis) |
| Pontuação de Previsão TxGNN | 0,9977 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Os dados compilados para este relatório não trazem o mecanismo de ação do fármaco. Pelo conhecimento geral, o posaconazol é um triazol que inibe a lanosterol 14-alfa-desmetilase (CYP51), bloqueando a síntese de ergosterol na membrana do fungo. Isso explica sua ação em infecções fúngicas invasivas, e é daí que provavelmente vem o sinal do modelo: a associação do fármaco com a classe dos antifúngicos.

Para a pneumocistose, porém, a lógica mecanística é fraca. *Pneumocystis jirovecii* difere da maioria dos fungos: sua membrana contém colesterol em vez de ergosterol e não possui a via típica de biossíntese de ergosterol. Assim, não se espera que os azóis funcionem, e a pontuação muito alta (0,9977) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. O tratamento padrão é sulfametoxazol-trimetoprima, e azóis não são recomendados para pneumonia por *Pneumocystis*.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Concluído | 602 | Rezafungina intravenosa vs. regime antimicrobiano padrão na prevenção de doenças fúngicas invasivas em transplante alogênico de medula/sangue (estudo ReSPECT). O posaconazol não é o fármaco em investigação; no máximo participa como comparador ou profilaxia de base. Não fornece evidência direta para pneumocistose. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Revisão | The Lancet Infectious Diseases | Recomendações da Sociedade Britânica de Micologia Médica (atualização 2025) para o diagnóstico de doenças fúngicas graves. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Revisão | Zhonghua Jie He He Hu Xi Za Zhi | Diretrizes chinesas (edição 2025) para diagnóstico e manejo de doenças fúngicas pulmonares invasivas. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revisão | Swiss Medical Weekly | Panorama de candidíase invasiva, aspergilose, criptococose e pneumonia por *Pneumocystis*; cita a redução de infecções fúngicas com a profilaxia com posaconazol em pacientes hemato-oncológicos de alto risco. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisão | Clinical Pharmacokinetics | Penetração de antifúngicos e outros anti-infecciosos no líquido de revestimento epitelial pulmonar. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Coorte | Transplant Infectious Disease | Complicações infecciosas na doença enxerto contra hospedeiro aguda após transplante de fígado. |

Nenhum desses trabalhos demonstra eficácia do posaconazol contra a pneumocistose.

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101710196 | NOXAFIL | MERCK SHARP & DOHME FARMACEUTICA LTDA. | Ativo |
| 166140011 | NOXAFIL | SCHERING-PLOUGH PRODUTOS FARMACÊUTICOS LTDA | Cancelado |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 269 interações. Entre as de nível **maior** estão loperamida, triamcinolona e budesonida. Entre as de nível **moderado** estão famotidina, ranitidina, omeprazol, rabeprazol, cimetidina, claritromicina, aprepitanto, dexametasona, hidrocortisona, betametasona, bisacodil, picossulfato, polietilenoglicol e saxagliptina.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do modelo é muito alta, mas o mecanismo do azol não se aplica ao *Pneumocystis* (ausência de ergosterol), não há ensaio clínico com posaconazol para essa indicação e a literatura é apenas geral. O nível de evidência é L4, e o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação confirmados em fonte primária (DrugBank).
- Estudos pré-clínicos ou clínicos que avaliem diretamente o posaconazol contra *Pneumocystis*, incluindo comparação com sulfametoxazol-trimetoprima.
- Bula da ANVISA com advertências e contraindicações, hoje ausentes e que impedem a triagem de segurança.
- Esclarecimento da situação regulatória e das formas farmacêuticas disponíveis.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

