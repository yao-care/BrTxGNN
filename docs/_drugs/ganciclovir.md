---
layout: default
title: Ganciclovir
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Ganciclovir
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

# Ganciclovir: Da retinite por CMV à pneumonia por citomegalovírus

## Resumo em Uma Frase

Ganciclovir é um análogo de nucleosídeo antiviral utilizado no tratamento e profilaxia de infecções por citomegalovírus (CMV) em pacientes imunocomprometidos, incluindo retinite por CMV em pacientes com AIDS e profilaxia em receptores de transplante.
O modelo TxGNN prevê que pode ser eficaz para **Pneumonia por Citomegalovírus (Cytomegalovirus Pneumonia)**, atualmente com **9 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Retinite por CMV (AIDS); profilaxia e tratamento de infecções por CMV em transplantados |
| Nova Indicação Prevista | Pneumonia por Citomegalovírus (Cytomegalovirus Pneumonia) |
| Pontuação de Previsão TxGNN | 97,56% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 17 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Embora os dados formais de mecanismo de ação não estejam disponíveis neste pacote de evidências, Ganciclovir é amplamente documentado na literatura como um análogo de nucleosídeo que atua inibindo a **DNA polimerase viral do CMV** (codificada pelo gene UL54). O fármaco é fosforilado inicialmente pela quinase viral UL97, gerando um metabólito trifosfatado que compete com a desoxiguanosina trifosfato e bloqueia a replicação do DNA viral. Este mecanismo é direto, específico ao CMV e independente do órgão-alvo afetado.

A pneumonia por CMV representa a manifestação grave da infecção disseminada por CMV no parênquima pulmonar, predominantemente em hospedeiros imunocomprometidos — receptores de transplante de medula óssea, transplantados de órgãos sólidos, pacientes com AIDS e neonatos. Como a ação do Ganciclovir recai sobre a replicação viral em si (e não sobre um tecido específico), a extensão para pneumonia por CMV é uma aplicação biologicamente direta e coerente da mesma atividade terapêutica já reconhecida para retinite e outras formas de doença por CMV.

Esta previsão é reforçada por décadas de evidência clínica acumulada: já nos anos 1980, séries de casos documentaram o uso de Ganciclovir combinado com imunoglobulina IV para pneumonite intersticial por CMV pós-transplante de medula. Dois grandes ensaios controlados randomizados completados — um Phase 4 (n=317) e um Phase 2/3 (n=563) — avaliaram diretamente o Ganciclovir no contexto de pneumonia associada a CMV, conferindo solidez ao nível de evidência L1 atribuído pelo sistema de pontuação.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02152358](https://clinicaltrials.gov/study/NCT02152358) | Phase 4 | Concluído | 317 | RCT duplo-cego multicêntrico: terapia preemptiva com Ganciclovir (CMV viremia +) vs. Aciclovir (HSV +) em pacientes de UTI com ventilação mecânica prolongada; desfecho primário — dias livres de ventilador até o Dia 60 |
| [NCT03915366](https://clinicaltrials.gov/study/NCT03915366) | Phase 2/3 | Concluído | 563 | RCT aberto multicêntrico: tratamento empírico anti-CMV (e anti-TB) vs. cuidado padrão em lactentes HIV-positivos com pneumonia grave na África; avalia mortalidade aos 15 dias e 1 ano |
| [NCT01199562](https://clinicaltrials.gov/study/NCT01199562) | N/A | Ativo (não recrutando) | 153 | Estratégia modificada de manejo preemptivo de CMV após transplante alogênico de células hematopoéticas; Ganciclovir como intervenção e correlação com função imune inata |
| [NCT05708755](https://clinicaltrials.gov/study/NCT05708755) | Phase 2 | Recrutando | 50 | Avalia uso do painel inSIGHT™ CMV T Cell para guiar e minimizar a duração da profilaxia com valganciclovir em receptores de transplante pulmonar |
| [NCT04690933](https://clinicaltrials.gov/study/NCT04690933) | N/A | Concluído | 400 | Observatório de vida real: eficácia e resistência de moléculas anti-CMV (incluindo Ganciclovir) em receptores de transplante de células-tronco hematopoéticas; pneumonia intersticial como manifestação principal avaliada |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39774866](https://pubmed.ncbi.nlm.nih.gov/39774866/) | 2025 | Expert Review | Intensive Care Medicine | Revisão atual para intensivistas: apresentação clínica, fatores de risco e manejo de infecção por CMV em imunocomprometidos na UTI — posiciona Ganciclovir como pilar terapêutico |
| [40307889](https://pubmed.ncbi.nlm.nih.gov/40307889/) | 2025 | RCT SAP | Trials | Plano de análise estatística publicado do ensaio EMPIRICAL (NCT03915366): metodologia para avaliar eficácia/segurança do tratamento empírico anti-CMV em lactentes HIV com pneumonia grave |
| [8786764](https://pubmed.ncbi.nlm.nih.gov/8786764/) | 1996 | Drug Review | N Engl J Med | Revisão clássica do NEJM sobre Ganciclovir: farmacologia, espectro de atividade e eficácia clínica em infecções por CMV; considera-o terapia de primeira linha em doença CMV com risco de vida |
| [2161731](https://pubmed.ncbi.nlm.nih.gov/2161731/) | 1990 | Pharmacological Review | Drugs | Revisão farmacológica abrangente: atividade antiviral contra herpesvírus, propriedades farmacocinéticas e eficácia terapêutica do Ganciclovir em infecções por CMV em imunocomprometidos |
| [8274605](https://pubmed.ncbi.nlm.nih.gov/8274605/) | 1993 | Review | Clin Infect Dis | Estratégias de prevenção e tratamento de pneumonia por CMV em transplantados; documenta papel crescente do Ganciclovir tanto na profilaxia convencional quanto na terapia preemptiva |
| [8668848](https://pubmed.ncbi.nlm.nih.gov/8668848/) | 1995 | Review | Semin Respir Infect | Revisão sobre pneumonia por CMV em hospedeiros imunocomprometidos; destaca mortalidade próxima a 100% sem tratamento em transplantados de medula e papel do Ganciclovir no diagnóstico e terapia precoce |
| [2847609](https://pubmed.ncbi.nlm.nih.gov/2847609/) | 1988 | Case Series | Ann Intern Med | Pioneiro: avalia eficácia de Ganciclovir + imunoglobulina IV em alta dose para pneumonite intersticial por CMV pós-transplante alogênico de medula óssea |
| [2847610](https://pubmed.ncbi.nlm.nih.gov/2847610/) | 1988 | Case Series | Ann Intern Med | Confirma eficácia da combinação Ganciclovir + imunoglobulina CMV IV em pacientes com pneumonia por CMV pós-transplante de medula; série paralela ao PMID 2847609 |
| [37225488](https://pubmed.ncbi.nlm.nih.gov/37225488/) | 2024 | Case Report | Internal Medicine (Tokyo) | Pneumonia primária por CMV em adulto imunocompetente tratada com sucesso com valganciclovir + corticoterapia; ilustra espectro clínico além do hospedeiro imunocomprometido |
| [28888855](https://pubmed.ncbi.nlm.nih.gov/28888855/) | 2017 | Case Report | J Infect Chemother | Criança imunocompetente com pneumonia grave e falência de múltiplos órgãos por CMV tratada com Ganciclovir; relata arritmia como evento adverso associado ao fármaco |

---

## Informações de Comercialização no Brasil

O banco de dados ANVISA registra **17 registros** de Ganciclovir com status **comercializado** no Brasil. Os dados individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste pacote de evidências.

> Para consultar os registros completos, acesse: [Consultas ANVISA](https://consultas.anvisa.gov.br/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Dois grandes ensaios clínicos concluídos (Phase 4, n=317; Phase 2/3, n=563) avaliam diretamente o Ganciclovir no contexto de pneumonia por CMV, com mecanismo de ação biologicamente direto e décadas de documentação clínica desde os anos 1980 — a solidez das evidências justifica avançar com salvaguardas específicas.

**Para prosseguir, é necessário:**
- Recuperar advertências, contraindicações e interações medicamentosas da bula ANVISA (download do PDF da bula)
- Confirmar indicações aprovadas e formas farmacêuticas disponíveis nos 17 registros ANVISA (especialmente disponibilidade da formulação IV para uso hospitalar)
- Obter dados formais de mecanismo de ação via DrugBank API (DB01004)
- Definir plano de monitoramento hematológico (mielossupressão é efeito adverso relevante do Ganciclovir)
- Aguardar publicação dos resultados primários do ensaio NCT03915366 (EMPIRICAL) para consolidação do nível de evidência L1
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

