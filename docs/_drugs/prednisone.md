---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Prednisone
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

Com base no Evidence Pack fornecido para Prednisone, vou gerar o relatório de avaliação de reposicionamento.

---

# Prednisone: De doenças inflamatórias e autoimunes à alopecia areata

## Resumo em Uma Frase

Prednisone é um glicocorticoide sistêmico amplamente utilizado no tratamento de condições inflamatórias, autoimunes e alérgicas — de artrite reumatoide a doenças pulmonares obstrutivas. O modelo TxGNN prevê que pode ser eficaz para **Alopecia Areata**, condição autoimune que causa perda de cabelo focal a total, atualmente com **1 ensaio clínico de Fase 3 concluído** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Condições inflamatórias, autoimunes e alérgicas (glicocorticoide sistêmico de amplo espectro) |
| Nova Indicação Prevista | Alopecia Areata |
| Pontuação de Previsão TxGNN | 99.99% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não localizado na base de dados consultada (0 registros) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Prednisone é um pró-fármaco convertido em prednisolone pelo fígado. Pertence à classe dos glicocorticoides e exerce efeito anti-inflamatório e imunomodulador por meio de receptores nucleares intracelulares, suprimindo a transcrição de citocinas pró-inflamatórias (IL-1, IL-6, TNF-α) e inibindo a proliferação e ativação de linfócitos T. Não há dados detalhados sobre o mecanismo de ação no registro formal deste medicamento no banco de dados consultado; contudo, seu perfil farmacológico como corticosteroide sistêmico é extensamente documentado na literatura médica global.

A alopecia areata é reconhecida como uma doença autoimune mediada por linfócitos T CD8+, que atacam os folículos capilares em fase anágena, rompendo o chamado "privilégio imunológico" folicular e provocando queda de cabelo focal, parcial ou total (totalis/universalis). Como os glicocorticoides sistêmicos suprimem diretamente essa resposta imune autorreativa mediada por células T, o prednisone representa uma das intervenções terapêuticas mais logicamente alinhadas com a fisiopatologia da alopecia areata — tornando a previsão do TxGNN mecanisticamente coerente e clinicamente plausível.

O uso de prednisone em alopecia areata tem raízes históricas documentadas desde 1956 (Lubowe; Funk) e persiste como opção terapêutica nos casos mais graves, especialmente em esquema de pulso oral mensal e em combinação com metotrexato. A publicação de um ensaio clínico de Fase 3 randomizado (NCT02037191) na JAMA Dermatology em 2023 consolidou a base de evidências para essa abordagem, confirmando que a combinação metotrexato + prednisone em baixas doses supera o metotrexato isolado em pacientes com alopecia areata totalis ou universalis.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Concluído | 90 | RCT duplo-cego multicêntrico: metotrexato vs. metotrexato + prednisone em baixa dose vs. placebo em alopecia areata grave (totalis/universalis) — único ensaio de Fase 3 diretamente relevante para prednisone em AA |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Phase 2 | Concluído | 456 | Enpatoran em LES e lúpus cutâneo (SCLE/DLE); doenças autoimunes cutâneas com fisiopatologia imunológica parcialmente compartilhada com AA; corticosteroide como terapia de fundo |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Phase 3 | Concluído | 778 | Baricitinib (inibidor JAK-1/2) em LES — relevante pois baricitinib é aprovado para AA grave; corticosteroide como tratamento padrão de base |
| [NCT01283139](https://clinicaltrials.gov/study/NCT01283139) | Phase 2 | Concluído | 834 | Sifalimumab (anti-IFN-α) em LES moderado a grave — contexto de supressão imune via interferon, mecanismo com sobreposição à fisiopatologia da AA |
| [NCT02953821](https://clinicaltrials.gov/study/NCT02953821) | Phase 4 | Concluído | 172 | Acthar Gel (hormônio corticotrófico) vs. placebo em LES ativo apesar de corticosteroide moderado — estudo de imunomodulação mediada por corticoide em doença autoimune sistêmica |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | RCT duplo-cego de 2 etapas: metotrexato + prednisone em baixa dose superior ao metotrexato isolado em AA totalis/universalis — maior evidência contemporânea para o uso de prednisone em AA grave |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case Series | Clin Exp Dermatology | Série de 8 casos: baricitinib + baixas doses de corticosteroide produziu melhora expressiva em AA muito grave (SALT ≥ 95), onde baricitinib isolado era ineficaz |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Case Series | Dermatology (Basel) | Metotrexato combinado com corticosteroides em dose baixa a moderada demonstrou eficácia em AA grave com resposta refratária a tratamentos anteriores |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Case Series | Ann Dermatol Venereol | Pulso oral mensal de prednisone avaliado em AA: esquema com boa tolerabilidade e resultados favoráveis em termos de recrescimento capilar |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Case Series | JAAD | Ciclosporina sistêmica + prednisone em baixa dose em AA grave crônica: avaliação clínica e imunopatológica com documentação de resposta imune |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Case Series | Int J Dermatology | Corticosteroides sistêmicos como tratamento efetivo de AA grave: maioria dos pacientes respondeu, embora com riscos de efeitos adversos de longo prazo |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Arch Dermatology | Revisão abrangente de terapias para AA: prednisone entre os agentes com eficácia documentada, com análise crítica das limitações metodológicas dos estudos disponíveis |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Case Series | Arch Dermatology | Seguimento médio de 15 meses após suspensão: resposta inicial ao prednisone em dias alternados em AA, mas benefício de longo prazo limitado e efeitos adversos (acne, obesidade, opacidades lenticulares, hipertensão leve) notáveis |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Clinical Study | Arch Dermatology | Estudos imunológicos em AA e tratamento com prednisone — um dos primeiros trabalhos a associar resposta imune com eficácia do corticosteroide sistêmico em AA |
| [23962142](https://pubmed.ncbi.nlm.nih.gov/23962142/) | 2013 | Case Report | J Cutaneous Pathology | Alopecia difusa com mucinose folicular proeminente semelhante a AA: remissão completa da alopecia com prednisone oral |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um ensaio clínico de Fase 3 randomizado, duplo-cego e concluído (NCT02037191, publicado na JAMA Dermatology em 2023) demonstrando que prednisone em baixa dose combinado com metotrexato é eficaz para formas graves de alopecia areata, respaldado por literatura histórica consolidada desde 1956 e uma pontuação TxGNN de 99,99%. No entanto, o benefício de longo prazo é limitado, os efeitos adversos dos corticosteroides sistêmicos são clinicamente relevantes, o fármaco não foi localizado no banco de dados regulatório brasileiro consultado, e os dados formais de segurança estão ausentes neste pacote de evidências.

**Para prosseguir, é necessário:**
- Verificar o status de registro na ANVISA — prednisone é um genérico amplamente disponível globalmente e pode estar sub-representado ou cadastrado sob nomenclatura diferente no banco consultado
- Obter dados completos de segurança (advertências, contraindicações e interações medicamentosas a partir da bula brasileira ou referência internacional como FDA/EMA)
- Definir protocolo de dosagem adequado: pulso oral mensal, dose diária fracionada ou esquema combinado com metotrexato
- Estabelecer plano de monitoramento de efeitos adversos de longo prazo de corticosteroide sistêmico: densidade óssea (osteoporose), glicemia (diabetes esteroide-induzida), pressão arterial, catarata subcapsular posterior e supressão do eixo HPA
- Delimitar critérios de elegibilidade dos pacientes: gravidade da AA (SALT score), comorbidades que contraindicam corticosteroide sistêmico (diabetes descompensado, hipertensão não controlada, tuberculose ativa, osteoporose grave)
---

