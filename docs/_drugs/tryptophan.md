---
layout: default
title: Tryptophan
parent: 僅模型預測 (L5)
nav_order: 496
evidence_level: L5
indication_count: 10
---

# Tryptophan
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

O skill txgnn-pipeline cobre operações técnicas de pipeline, não a geração de relatório. As instruções do sistema prompt (v5) são a especificação completa para este agente. Prosseguindo com a geração do relatório.

---

# Triptofano: De suplemento nutricional à Síndrome das Pernas Inquietas

## Resumo em Uma Frase

Triptofano (L-triptofano) é um aminoácido essencial cujo papel mais reconhecido é o de precursor bioquímico da serotonina e da melatonina, sem indicação terapêutica formalmente aprovada no Brasil. O modelo TxGNN prevê que pode ser eficaz para a **Síndrome das Pernas Inquietas (Restless Legs Syndrome)**, com pontuação de 99,72%, porém atualmente **sem ensaios clínicos** e **sem publicações científicas** que apoiem diretamente esta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Aminoácido essencial / suplemento nutricional (sem indicação aprovada no Brasil) |
| Nova Indicação Prevista | Síndrome das Pernas Inquietas (Restless Legs Syndrome) |
| Pontuação de Previsão TxGNN | 99,72% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

O triptofano é o aminoácido essencial que inicia a via bioquímica: **L-triptofano → 5-HTP → Serotonina → Melatonina**. Por esta razão, é o substrato central para a regulação do humor, do ciclo sono-vigília e de diversas funções do sistema nervoso central. Não há dados formais de mecanismo de ação (MOA) disponíveis no DrugBank para este composto aplicados à Síndrome das Pernas Inquietas.

A Síndrome das Pernas Inquietas (RLS) é uma condição neurológica caracterizada por disfunção dopaminérgica nos gânglios basais — os tratamentos aprovados atuais atuam diretamente sobre receptores de dopamina (agonistas dopaminérgicos) ou sobre canais de cálcio. A hipótese que conecta o triptofano à RLS é indireta: dado que os sistemas serotoninérgico e dopaminérgico interagem no sistema nervoso central, a suplementação de triptofano poderia, em tese, modular indiretamente o equilíbrio dopaminérgico ao elevar os níveis de serotonina. Esta cadeia de eventos permanece altamente especulativa.

A alta pontuação do TxGNN (0,9972) provavelmente reflete uma **conexão topológica indireta** no grafo de conhecimento — triptofano → serotonina → interação serotonina-dopamina → RLS — e não uma relação terapêutica direta estabelecida. Nenhum estudo pré-clínico ou clínico publicado suporta especificamente este uso, tornando esta previsão uma **hipótese geradora de pesquisa**, e não uma evidência de eficácia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

**⚠️ Alerta histórico relevante:** Em 1989, mais de 1.500 pacientes que utilizaram L-triptofano como suplemento (para insônia e depressão) desenvolveram **Síndrome de Eosinofilia-Mialgia (EMS)**, doença potencialmente fatal com aproximadamente 40 óbitos registrados. A causa foi atribuída a impurezas do processo de fabricação (um lote de um único fabricante), e não ao triptofano em si. Este precedente — documentado no registro clínico [NCT00001918](https://clinicaltrials.gov/study/NCT00001918) — exige avaliação rigorosa de pureza farmacêutica e rastreabilidade de fabricação em qualquer desenvolvimento clínico futuro com este composto.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existem ensaios clínicos nem publicações científicas que apoiem diretamente o uso do triptofano para a Síndrome das Pernas Inquietas. A previsão do TxGNN baseia-se exclusivamente em conexões topológicas indiretas do grafo de conhecimento, sem evidência mecanística ou clínica de suporte. O triptofano não está registrado nem comercializado no Brasil, e seu histórico de segurança (EMS, 1989) requer due diligence adicional antes de qualquer desenvolvimento clínico.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos em modelos validados de RLS, investigando especificamente o eixo triptofano → serotonina → modulação dopaminérgica
- Confirmação do perfil de segurança com triptofano farmacêutico de alta pureza, incluindo análise de contaminantes associados ao EMS
- Dados de mecanismo de ação (MOA) específicos para o contexto de RLS
- Processo de registro na ANVISA antes de qualquer ensaio clínico no Brasil

---

> **Nota sobre o perfil completo de previsão:** Dentro do conjunto de indicações previstas pelo TxGNN para este fármaco, a **insônia** (Rank 4; TxGNN 99,47%; Nível de Evidência **L2**; Decisão: **Proceed with Guardrails**) apresenta suporte substancialmente maior, incluindo um RCT de 4 braços comparando L-triptofano a hipnóticos ativos ([PMID 6410442](https://pubmed.ncbi.nlm.nih.gov/6410442/), 1983, n=96), estudos de intervenção recentes ([PMID 40772548](https://pubmed.ncbi.nlm.nih.gov/40772548/), 2025) e revisões mecanísticas sobre a via triptofano → serotonina → melatonina aplicada ao sono ([PMID 40681828](https://pubmed.ncbi.nlm.nih.gov/40681828/), 2025). Essa indicação representa a direção de reposicionamento com maior maturidade de evidências para investigação prioritária.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

