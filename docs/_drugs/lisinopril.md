---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: Da Hipertensão Arterial ao Infarto do Miocárdio Posterolateral

## Resumo em Uma Frase

Lisinopril é um inibidor da enzima conversora de angiotensina (IECA), amplamente utilizado no tratamento da hipertensão arterial, insuficiência cardíaca e manejo pós-infarto do miocárdio. O modelo TxGNN prevê que pode ser eficaz especificamente para o **Infarto do Miocárdio Posterolateral (posterolateral myocardial infarction)**, um subtipo anatômico que compromete a parede posterior e lateral do ventrículo esquerdo. Atualmente, **não há ensaios clínicos específicos** nem **publicações diretas** voltados a este subtipo anatômico, restringindo a evidência ao nível mecanístico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro ANVISA (uso clínico estabelecido: hipertensão arterial, insuficiência cardíaca) |
| Nova Indicação Prevista | Infarto do Miocárdio Posterolateral (posterolateral myocardial infarction) |
| Pontuação de Previsão TxGNN | 99.90% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação disponíveis neste pacote de evidências. Com base em conhecimento farmacológico estabelecido, Lisinopril pertence à classe dos IECAs e atua bloqueando a conversão de angiotensina I em angiotensina II — um potente vasoconstritor e mediador de fibrose cardíaca. Ao reduzir os níveis de angiotensina II, o Lisinopril diminui a pré e pós-carga ventricular, inibe a ativação neuro-hormonal excessiva e suprime o remodelamento ventricular esquerdo (LV remodeling) após evento isquêmico agudo.

A relação mecanística com o infarto posterolateral é biologicamente coerente: IECAs já possuem eficácia comprovada no manejo pós-infarto do miocárdio em termos amplos, sustentada pelos ensaios Phase 3 GISSI-3 e ISIS-4. O infarto posterolateral é um subtipo anatômico específico — geralmente associado à oclusão da artéria circunflexa (CX) ou à artéria coronária direita dominante —, comprometendo a parede posterior e lateral do ventrículo esquerdo, com maior risco de disfunção sistólica residual e remodelamento desfavorável.

A previsão do TxGNN é mecanisticamente plausível, mas constitui essencialmente uma extrapolação de evidências de IAM geral para um subtipo anatômico específico. Não foram identificados ensaios clínicos nem publicações científicas exclusivamente focados no infarto posterolateral como alvo independente, tornando esta indicação uma hipótese de pesquisa válida, porém sem suporte clínico direto.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Lisinopril em infarto do miocárdio posterolateral.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Lisinopril em infarto do miocárdio posterolateral.

---

## Informações de Comercialização no Brasil

O Lisinopril possui **20 registros** na ANVISA com situação **Comercializado**. Os detalhes individuais dos registros (nome comercial, forma farmacêutica e indicação aprovada) não foram capturados no conjunto de dados atual. Para consulta completa, acesse o portal da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para infarto do miocárdio posterolateral apresenta plausibilidade mecanística sólida via inibição do eixo RAAS, mas ausência completa de evidências clínicas específicas para este subtipo anatômico. Sem estudos de subgrupo que confirmem benefício diferenciado no subtipo posterolateral, a indicação permanece como hipótese de pesquisa (L4), insuficiente para decisão de desenvolvimento clínico.

> 📌 **Recomendação de Prioridade:** Dentro do conjunto de previsões deste pacote, a indicação de **Doença Cardíaca Pulmonar Crônica** (rank 9, evidência L3, recomendação "Proceed with Guardrails") apresenta dois estudos clínicos diretos com Lisinopril — PMID [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) (2003, uso de Lisinopril em cor pulmonale crônico) e PMID [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) (2006, correção de hipertensão pulmonar com Lisinopril em IHD + DPOC) — e representa o alvo de reposicionamento mais maduro para priorização imediata neste pacote.

**Para prosseguir com infarto do miocárdio posterolateral, é necessário:**
- Obter texto completo das indicações aprovadas nos 20 registros ANVISA (download das bulas em PDF)
- Obter dados detalhados de MOA via API DrugBank (DB00722) para análise de mecanismo completa
- Identificar análises de subgrupo estratificadas por localização anatômica do infarto nos grandes ensaios GISSI-3, ISIS-4 e CONSENSUS
- Confirmar advertências e contraindicações na bula oficial — especialmente em contextos de estenose de artéria renal, onde IECAs representam risco de insuficiência renal aguda
- Avaliar paralelamente a indicação de Doença Cardíaca Pulmonar Crônica, que já possui base clínica suficiente para a próxima etapa de desenvolvimento
---

