---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: Da hipertensão ocular ao glaucoma de ângulo aberto tipo 1

## Resumo em Uma Frase

Brinzolamide é um inibidor tópico da anidrase carbônica II (CA-II), aprovado globalmente para o tratamento do glaucoma de ângulo aberto primário e hipertensão ocular, porém **não registrado no Brasil**. O modelo TxGNN prevê que pode ser eficaz para **Glaucoma de Ângulo Aberto Tipo 1 — Glaucoma 1, Open Angle** (pontuação 97,70%), atualmente com **48 ensaios clínicos** e **20 publicações** apoiando esta direção. A previsão de maior pontuação (99,48%) é para o **glaucoma hereditário primário**, porém sem evidência clínica direta disponível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glaucoma de ângulo aberto primário e hipertensão ocular (indicação aprovada globalmente; sem registro no Brasil) |
| Nova Indicação Prevista | Glaucoma de ângulo aberto tipo 1 (Glaucoma 1, Open Angle) |
| Pontuação de Previsão TxGNN | 97,70% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Brinzolamide é um inibidor altamente específico da anidrase carbônica tipo II (CA-II), enzima presente no epitélio do corpo ciliar. Ao inibir essa enzima, reduz a formação de íons bicarbonato e, consequentemente, a produção de humor aquoso, resultando em diminuição da pressão intraocular (PIO) de até 18% em relação ao basal. Formulado como suspensão oftálmica a 1% (Azopt®), é administrado duas ou três vezes ao dia e está aprovado em múltiplos países — incluindo Estados Unidos, União Europeia e Japão — para o manejo do glaucoma de ângulo aberto primário (GPAA) e hipertensão ocular (HO), tanto em monoterapia quanto como terapia adjuvante a betabloqueadores ou análogos de prostaglandinas.

O glaucoma de ângulo aberto tipo 1 (GLC1A) é uma forma hereditária de glaucoma de ângulo aberto mapeada no locus cromossômico 1q21-q31, frequentemente associada a mutações no gene *MYOC* (miocilina). Embora tenha uma base genética distinta, a via patológica final é compartilhada com o GPAA esporádico: obstrução progressiva da drenagem do humor aquoso pela malha trabecular, elevação sustentada da PIO e degeneração progressiva das células ganglionares da retina e seus axônios. Portanto, a estratégia farmacológica de redução da PIO por inibição da CA-II é diretamente aplicável a este subtipo genético.

Adicionalmente, o TxGNN identificou consistência notável nas previsões dentro do espectro glaucomatoso: glaucoma hereditário primário (99,48%), glaucoma genérico (96,92%), glaucoma de ângulo aberto (96,72%) e glaucoma de ângulo fechado (96,60%). Essa convergência reforça a robustez do sinal preditivo e a plausibilidade farmacológica do brinzolamide como agente terapêutico para o amplo espectro de condições glaucomatosas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01309204](https://clinicaltrials.gov/study/NCT01309204) | Phase 3 | Concluído | 1184 | Eficácia e segurança de brinzolamide/brimonidina combinação fixa vs componentes individuais concomitantes em pacientes com glaucoma de ângulo aberto ou HO |
| [NCT01297920](https://clinicaltrials.gov/study/NCT01297920) | Phase 3 | Concluído | 1062 | RCT duplo-cego de 3 meses com extensão de segurança: brinzolamide 1%/brimonidina 0,2% vs componentes individuais para redução da PIO |
| [NCT01297517](https://clinicaltrials.gov/study/NCT01297517) | Phase 3 | Concluído | 1001 | Eficácia e segurança da combinação fixa brinzolamide/brimonidina vs monoterapias em glaucoma de ângulo aberto e/ou HO |
| [NCT02512042](https://clinicaltrials.gov/study/NCT02512042) | Phase 3 | Concluído | 973 | Estudo multicêntrico de bioequivalência: brinzolamide genérico 1% vs Azopt® em glaucoma crônico de ângulo aberto ou HO |
| [NCT03896633](https://clinicaltrials.gov/study/NCT03896633) | Phase 1/2 | Concluído | 637 | Equivalência terapêutica de brinzolamide genérico 1% vs Azopt® — grande amostra confirma qualidade farmacêutica |
| [NCT01357616](https://clinicaltrials.gov/study/NCT01357616) | Phase 3 | Concluído | 328 | AZARGA® (brinzolamide/timolol) vs AZOPT® e timolol separados em pacientes chineses com glaucoma de ângulo aberto — RCT Phase 3 direto |
| [NCT01937299](https://clinicaltrials.gov/study/NCT01937299) | Phase 4 | Concluído | 307 | Efeito aditivo de SIMBRINZA® (brinzolamide/brimonidina) como terapia adjuvante a travoprosta (TRAVATAN Z®) |
| [NCT02325518](https://clinicaltrials.gov/study/NCT02325518) | Phase 4 | Concluído | 218 | Brinzolamide 1%/timolol 0,5% vs dorzolamida 2%/timolol 0,5% — eficácia comparativa na redução da PIO |
| [NCT00761995](https://clinicaltrials.gov/study/NCT00761995) | Phase 4 | Concluído | 200 | Brinzolamide TID vs dorzolamida TID na redução da PIO em glaucoma de ângulo aberto ou HO |
| [NCT01340014](https://clinicaltrials.gov/study/NCT01340014) | Phase 4 | Concluído | 112 | Estudo de preferência do paciente: AZARGA® vs COSOPT® quanto ao conforto ocular após uma semana de uso |

> **Nota:** Foram identificados **48 ensaios clínicos** registrados no ClinicalTrials.gov. Os 10 mais relevantes são apresentados acima, priorizados por fase do estudo, tamanho amostral e status de conclusão.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Revisão Sistemática | Ophthalmology | Meta-análise em rede comparando eficácia de medicamentos de primeira linha para GPAA; brinzolamide incluído entre os agentes avaliados |
| [26648686](https://pubmed.ncbi.nlm.nih.gov/26648686/) | 2015 | Eficácia Clínica | Clin Ophthalmol | Eficácia clínica da combinação fixa brinzolamide 1%/brimonidina 0,2% para GPAA e HO; benefícios de adesão com combinações fixas |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | Estudo Comparativo (Phase 3) | Cureus | RCT comparando brinzolamide/timolol vs dorzolamida/timolol em pacientes indianos com GPAA; eficácia e segurança demonstradas |
| [38598266](https://pubmed.ncbi.nlm.nih.gov/38598266/) | 2024 | Estudo Comparativo | J Ocul Pharmacol Ther | Estudo prospectivo de 1 ano: brinzolamide-brimonidina vs latanoprosta-timolol em GPAA e HO (n=200) |
| [14565787](https://pubmed.ncbi.nlm.nih.gov/14565787/) | 2003 | Revisão do Fármaco | Drugs & Aging | Revisão abrangente: brinzolamide como inibidor específico de CA; reduz PIO como monoterapia ou adjuvante em GPAA e HO |
| [18312166](https://pubmed.ncbi.nlm.nih.gov/18312166/) | 2008 | Monografia | Expert Opin Pharmacother | Brinzolamide reduz PIO em até 18% do basal e pode melhorar o fluxo sanguíneo retiniano sem efeitos sistêmicos significativos |
| [25732405](https://pubmed.ncbi.nlm.nih.gov/25732405/) | 2015 | Revisão do Fármaco | Drugs & Aging | Simbrinza® (brinzolamide/brimonidina): revisão de dados de Phase 3 mostrando superioridade sobre monoterapias |
| [10665518](https://pubmed.ncbi.nlm.nih.gov/10665518/) | 2000 | RCT | Surv Ophthalmol | Estudo multicêntrico randomizado: brinzolamide 1% como terapia primária vs dorzolamida 2% e placebo em GPAA/HO |
| [36556275](https://pubmed.ncbi.nlm.nih.gov/36556275/) | 2022 | Estudo Observacional | J Pers Med | Eficácia, segurança e satisfação na troca para combinação fixa brinzolamide/brimonidina em pacientes com glaucoma |
| [24966670](https://pubmed.ncbi.nlm.nih.gov/24966670/) | 2014 | Avaliação Crítica | Patient Prefer Adherence | Combinações fixas simplificam esquemas terapêuticos e melhoram adesão; brinzolamide/brimonidina como opção sem betabloqueador |

---

## Informações de Comercialização no Brasil

Brinzolamide **não possui registro** junto à ANVISA e **não está comercializado no Brasil**. Não foram encontrados registros de licenças ou nomes comerciais no mercado nacional.

Internacionalmente, o fármaco está disponível nas seguintes apresentações:

| Nome Comercial | Fabricante | Forma Farmacêutica | Mercados |
|---------|------|------|-----------|
| Azopt® | Alcon/Novartis | Suspensão oftálmica 1% | EUA, UE, Japão, e outros |
| AZARGA® | Alcon/Novartis | Suspensão oftálmica (brinzolamide 1% / timolol 0,5%) | EUA, UE, e outros |
| Simbrinza® | Alcon/Novartis | Suspensão oftálmica (brinzolamide 1% / brimonidina 0,2%) | EUA, UE |

---

## Considerações de Segurança

> Dados de advertências, contraindicações e interações medicamentosas para o mercado brasileiro não estão disponíveis, pois o produto não possui registro junto à ANVISA. Consulte a bula do fabricante (Azopt® Prescribing Information) para informações completas de segurança.
>
> Com base na literatura global, efeitos adversos comuns incluem: visão turva transitória, disgeusia (gosto amargo), desconforto ocular e blefarite. Por se tratar de uma sulfonamida, reações de hipersensibilidade cruzada com outras sulfonamidas devem ser consideradas.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Brinzolamide possui evidência clínica de nível **L1** (múltiplos RCTs Phase 3 concluídos, com amostras superiores a 1.000 pacientes) demonstrando eficácia e segurança no tratamento do glaucoma de ângulo aberto e hipertensão ocular. O mecanismo de ação — inibição da CA-II com redução da produção de humor aquoso — é diretamente relevante para o glaucoma de ângulo aberto tipo 1, cuja via patológica final (elevação da PIO e neuropatia óptica) é compartilhada com o GPAA. O fármaco já está aprovado para esta classe de indicação em múltiplos países.

**Para prosseguir, é necessário:**
- Submissão de dossiê regulatório para registro junto à **ANVISA** (se desejado para o mercado brasileiro)
- Obtenção da bula completa com **advertências, contraindicações e interações medicamentosas**
- Consulta ao **DrugBank** para dados detalhados do mecanismo de ação (MOA)
- Avaliação de **custo-efetividade e acessibilidade** no contexto do SUS
- Consideração de estudo específico para glaucoma de ângulo aberto tipo 1 (subtipo genético *MYOC*), dado que a evidência existente abrange o GPAA em geral, sem estratificação por subtipo genético
- Análise complementar de viabilidade para as indicações adicionais previstas pelo TxGNN (glaucoma hereditário primário, glaucoma de ângulo fechado) que apresentam evidência emergente

---

> ⚠️ **Aviso:** Este relatório é gerado para fins de pesquisa e não constitui aconselhamento médico. Todas as previsões de reposicionamento de fármacos requerem validação clínica antes de qualquer aplicação terapêutica. Dados com corte em 2026-04-05.
---

