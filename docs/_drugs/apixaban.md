---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: Da Anticoagulação ao Transtorno de Enxaqueca

## Resumo em Uma Frase

Apixaban é um inibidor seletivo e direto do fator Xa (FXa), amplamente aprovado para prevenção de AVC em fibrilação atrial não valvar e para o tratamento e prevenção do tromboembolismo venoso (TEV).
O modelo TxGNN prevê que pode ser eficaz para o **Transtorno de Enxaqueca (Migraine Disorder)**, atualmente com **1 ensaio clínico** tangencialmente relacionado e **nenhuma publicação direta** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Prevenção de AVC e embolismo sistêmico (fibrilação atrial não valvar); tratamento e prevenção do TEV |
| Nova Indicação Prevista | Transtorno de Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,02% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

A hipótese mecanística parte da relação entre a inibição do FXa e a via trigeminal-vascular da enxaqueca. Ao bloquear o FXa, o apixaban reduz a geração de trombina; esta, por sua vez, é capaz de ativar o receptor PAR-1 em neurônios trigeminais e células endoteliais cerebrais, uma via diretamente implicada no processo neuroinflamatório que precede a crise de enxaqueca. Trata-se de uma hipótese biologicamente plausível, mas ainda sem confirmação experimental direta.

Existe ainda uma conexão epidemiológica de interesse: pacientes com forame oval patente (FOP) apresentam prevalência significativamente maior de enxaqueca com aura, possivelmente mediada por microembolias paradoxais que ativam a cascata trigeminal. Nesse contexto específico, a anticoagulação poderia teoricamente reduzir o gatilho tromboembólico das crises em portadores de FOP — e é exatamente esse o cenário do único ensaio clínico identificado nesta busca.

No entanto, o apixaban não possui mecanismo de ação estabelecido sobre o transtorno de enxaqueca enquanto doença primária. A previsão elevada do TxGNN (99,02%) reflete associações estruturais no grafo de conhecimento médico — não equivale a evidência clínica de eficácia. A ausência de literatura direta e a classificação L4 indicam que esta hipótese permanece no estágio pré-clínico/mecanístico.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Concluído | 664 | Ensaio randomizado comparando fechamento percutâneo de FOP, anticoagulantes orais e antiplaquetários para prevenção de AVC recorrente em pacientes com FOP. A enxaqueca não é desfecho primário nem secundário pré-especificado; qualquer dado sobre enxaqueca seria observação incidental da comparação entre estratégias anticoagulantes vs. antiplaquetárias. |

> **Nota de relevância**: Este ensaio tem relevância indireta para a hipótese de enxaqueca (Grau C). Seu desenho e desfechos primários são focados em prevenção de AVC, não em tratamento da enxaqueca.

---

## Informações de Comercialização no Brasil

O apixaban está registrado no Brasil com **20 registros ativos na ANVISA**, confirmando ampla presença no mercado nacional. Os detalhes individuais de nome comercial, forma farmacêutica e texto de indicação aprovada não foram recuperados na consulta automatizada desta versão do Evidence Pack.

Para consultar os registros completos, acesse o portal oficial:
👉 [Consultas ANVISA — Medicamentos](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> Os dados de advertências, contraindicações e interações medicamentosas não foram recuperados nesta versão do Evidence Pack (lacuna de dados identificada). Recomenda-se consultar diretamente a bula registrada na ANVISA e o banco de dados DrugBank (DB06605) antes de qualquer análise clínica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para enxaqueca apoia-se em uma plausibilidade mecanística indireta (FXa → trombina → PAR-1 → neuroinflamação trigeminal) e no contexto epidemiológico FOP-enxaqueca, porém conta com apenas um ensaio clínico de Fase 3 tangencialmente relacionado e nenhuma publicação científica direta. O nível de evidência L4 indica que a hipótese está no início da escada de validação clínica, sendo prematuro avançar sem dados confirmatórios.

> **Nota estratégica**: Entre todas as previsões do TxGNN para o apixaban neste Evidence Pack, a indicação de **Hipertensão Pulmonar** (rank 8) apresenta evidências consideravelmente mais robustas (nível L3: 8 ensaios clínicos, 19 publicações, incluindo protocolo de RCT piloto específico — PMID [27932335](https://pubmed.ncbi.nlm.nih.gov/27932335/) — e estudos observacionais em CTEPH). Recomenda-se priorizar a geração de um relatório dedicado para essa indicação.

**Para prosseguir com a hipótese de enxaqueca, é necessário:**
- Recuperar os dados completos de MOA via DrugBank API (DB06605) para fortalecer a análise mecanística
- Realizar busca sistemática nos dados secundários dos ensaios de fechamento de FOP (CLOSE, REDUCE, DEFENSE-PFO) para identificar desfechos incidentais de enxaqueca no braço anticoagulante
- Conduzir revisão de literatura com estratégia expandida (termos: "anticoagulation AND migraine", "FXa inhibitor AND trigeminovascular", "FOP AND migraine AND anticoagulation")
- Avaliar dados de biobancos ou estudos de vida real para identificar sinal epidemiológico entre uso de apixaban e frequência de enxaqueca
- Obter detalhes das 20 indicações aprovadas nos registros ANVISA para completar o perfil regulatório brasileiro

---

*Este relatório é gerado automaticamente com base em dados do Evidence Pack (v4, corte: 2026-04-04) e destina-se exclusivamente a fins de pesquisa. Os resultados do modelo TxGNN são previsões computacionais e não constituem evidência clínica estabelecida. Qualquer aplicação terapêutica requer validação clínica independente.*
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

