---
layout: default
title: Cyclobenzaprine
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Cyclobenzaprine
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

Usando o skill `txgnn-pipeline` para orientação de relatório de reposicionamento de fármacos.

---

# Cyclobenzaprine: Do espasmo muscular agudo à Síndrome de Dor Miofascial

## Resumo em Uma Frase

Cyclobenzaprine é um relaxante muscular de ação central, aprovado pela FDA para o tratamento do espasmo muscular associado a condições musculoesqueléticas agudas e dolorosas.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Dor Miofascial (Myofascial Pain Syndrome)**,
atualmente com **17 ensaios clínicos** e **5 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Espasmo muscular associado a condições musculoesqueléticas agudas e dolorosas |
| Nova Indicação Prevista | Síndrome de Dor Miofascial (Myofascial Pain Syndrome) |
| Pontuação de Previsão TxGNN | 99.09% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote. Com base nas informações extraídas dos ensaios clínicos, Cyclobenzaprine é um relaxante muscular de ação central com estrutura química semelhante aos antidepressivos tricíclicos (TCA). O fármaco atua no tronco cerebral inibindo reflexos motores espinhais polissinápticos, reduzindo o tônus muscular excessivo e aliviando diretamente o espasmo persistente associado aos pontos-gatilho (*trigger points*) da síndrome de dor miofascial. Sua estrutura TCA confere adicionalmente um benefício analgésico central por meio da modulação de serotonina e noradrenalina.

A relação entre a indicação original (espasmo muscular agudo) e a nova indicação (MPS) é de proximidade patofisiológica direta: a MPS é caracterizada por espasmos musculares sustentados e pontos-gatilho que perpetuam o ciclo dor–espasmo–dor. O mecanismo relaxante muscular central do cyclobenzaprine tem potencial para interromper esse ciclo de forma etiologicamente justificada. Ensaios clínicos randomizados já testaram o fármaco diretamente em MPS mandibular e miofascial lombar, fornecendo evidências clínicas de primeiro nível.

Um elemento particularmente relevante é que a formulação sublingual de baixa dose (TNX-102 SL, 5,6 mg/noite), aprovada pela FDA em 2023 sob a marca **TONMYA**, destina-se ao tratamento da fibromialgia — condição que compartilha com a MPS os mecanismos centrais de sensibilização, dor muscular difusa e distúrbio do sono. Três ensaios de Fase 3 completados com n total superior a 1.400 pacientes sustentam essa aprovação, conferindo uma base indireta de evidências de nível L1 para a aplicação em MPS.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00635037](https://clinicaltrials.gov/study/NCT00635037) | N/A | Concluído | 30 | Comparação direta em MPS: acupuntura vs. injeção em ponto-gatilho combinada com cyclobenzaprine 10 mg/dia + dipirona; avaliou efeito analgésico e efeitos adversos em clínica de dor |
| [NCT02436096](https://clinicaltrials.gov/study/NCT02436096) | Phase 3 | Concluído | 519 | TNX-102 SL 2,8 mg noturno vs. placebo em fibromialgia (12 semanas); resultados positivos em dor, sono e sintomatologia geral — estudo pivô que embasou a aprovação FDA |
| [NCT04508621](https://clinicaltrials.gov/study/NCT04508621) | Phase 3 | Concluído | 514 | TNX-102 SL 5,6 mg noturno vs. placebo em fibromialgia (14 semanas); replicação com nova dose; avaliação primária de eficácia e segurança |
| [NCT05273749](https://clinicaltrials.gov/study/NCT05273749) | Phase 3 | Concluído | 457 | TNX-102 SL 5,6 mg noturno vs. placebo em fibromialgia (14 semanas); confirmação da eficácia e tolerabilidade da dose aprovada |
| [NCT04172831](https://clinicaltrials.gov/study/NCT04172831) | Phase 3 | Concluído | 503 | TNX-102 SL 5,6 mg noturno vs. placebo em fibromialgia (14 semanas); terceiro estudo confirmatório da série pivô |
| [NCT02015234](https://clinicaltrials.gov/study/NCT02015234) | Phase 3 | Concluído | 158 | Extensão aberta de 12 meses (F202): avaliação de segurança de longo prazo do TNX-102 SL em fibromialgia; pacientes provenientes do duplo-cego |
| [NCT02589275](https://clinicaltrials.gov/study/NCT02589275) | Phase 3 | Concluído | 375 | Extensão aberta de 3 meses (F301/F302): segurança e eficácia de longo prazo; pacientes que completaram os estudos F301 e F302 |
| [NCT01903265](https://clinicaltrials.gov/study/NCT01903265) | Phase 2b/3 | Concluído | 205 | Estudo BESTFIT: TNX-102 SL 2,8 mg em fibromialgia (12 semanas); estudo seminal que demonstrou efeitos benéficos em dor e sono, motivando o programa de Fase 3 |
| [NCT02829814](https://clinicaltrials.gov/study/NCT02829814) | Phase 3 | Encerrado precocemente | 51 | TNX-102 SL 2,8 mg em fibromialgia (12 semanas); encerrado antes da conclusão (n=51), fornece dados limitados de segurança |
| [NCT04704297](https://clinicaltrials.gov/study/NCT04704297) | Phase 4 | Recrutando | 180 | T-PIMPS: injeção em ponto-gatilho para MPS lombar em pronto-socorro; cyclobenzaprine como co-intervenção; avalia heterogeneidade de resultados em estudos anteriores |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12764337](https://pubmed.ncbi.nlm.nih.gov/12764337/) | 2003 | RCT | Annals of Emergency Medicine | Cyclobenzaprine + ibuprofeno vs. ibuprofeno isolado em distensão miofascial aguda no pronto-socorro; avaliou benefício analgésico adicional do relaxante muscular e perfil de efeitos adversos |
| [24822235](https://pubmed.ncbi.nlm.nih.gov/24822235/) | 2014 | RCT | Journal of Oral & Facial Pain and Headache | Cyclobenzaprine vs. tizanidina vs. placebo adicionados a programa de educação e autocuidado para dor miofascial mandibular ao despertar; comparação de eficácia clínica |
| [11889661](https://pubmed.ncbi.nlm.nih.gov/11889661/) | 2002 | RCT | Journal of Orofacial Pain | Cyclobenzaprine vs. clonazepam vs. placebo para dor miofascial mandibular ao despertar; relaxante muscular comparado a benzodiazepínico no tratamento da dor miofascial orofacial |
| [20673246](https://pubmed.ncbi.nlm.nih.gov/20673246/) | 2011 | RCT | Pain Practice | Acupuntura vs. injeção em ponto-gatilho + cyclobenzaprine + dipirona em síndrome de dor miofascial; comparação de eficácia analgésica entre modalidades farmacológica e não farmacológica |
| [3464212](https://pubmed.ncbi.nlm.nih.gov/3464212/) | 1986 | Review | The American Journal of Medicine | Síndrome fibrósica (precursor terminológico da fibromialgia/MPS): prevalência de 6–15% em clínica, razão F:M 5:1, múltiplos pontos-gatilho — contexto histórico da dor muscular crônica difusa |

---

## Informações de Comercialização no Brasil

Cyclobenzaprine **não possui registros ativos na ANVISA** e não está comercializado no Brasil. Nenhum produto com este princípio ativo foi identificado nas bases regulatórias brasileiras consultadas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A formulação sublingual de cyclobenzaprine (TNX-102 SL / TONMYA) obteve aprovação da FDA para fibromialgia em 2023, sustentada por ao menos três ensaios de Fase 3 completados com n total superior a 1.400 pacientes, além de extensões abertas de longo prazo. A fibromialgia compartilha com a síndrome de dor miofascial os mecanismos patofisiológicos centrais (sensibilização central, pontos-gatilho, dor muscular crônica), e ensaios clínicos randomizados testaram cyclobenzaprine diretamente em MPS. O conjunto de evidências fundamenta o avanço com cautela.

**Para prosseguir, é necessário:**
- Levantar advertências, contraindicações e interações medicamentosas na bula FDA/ANVISA — **item bloqueante** para avaliação completa de segurança (especialmente interações com IMAOs e outros depressores do SNC)
- Obter dados de MOA detalhados via DrugBank API (DB00924) para fortalecer a análise de mecanismo
- Avaliar viabilidade regulatória de registro no Brasil (ANVISA), dado que o produto não possui comercialização local
- Definir estratégia de formulação e posologia para MPS (oral IR 10 mg TID, ER 15–30 mg QD ou sublingual de baixa dose), considerando perfil de segurança diferenciado por formulação
- Mapear população-alvo específica: MPS aguda vs. crônica, subgrupo orofacial vs. axial vs. generalizado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

