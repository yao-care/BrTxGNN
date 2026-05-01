---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorfina: Da dependência opioide à porfiria intermitente aguda

## Resumo em Uma Frase

Buprenorfina é um analgésico opioide de ação parcial, amplamente utilizado no tratamento da dor moderada a grave e no manejo da dependência de opioides.
O modelo TxGNN prevê que pode ser eficaz para **Porfiria Intermitente Aguda (Acute Intermittent Porphyria)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Tratamento da dor moderada a grave e dependência de opioides |
| Nova Indicação Prevista | Porfiria Intermitente Aguda (Acute Intermittent Porphyria) |
| Pontuação de Previsão TxGNN | 99.41% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em conhecimento farmacológico estabelecido, buprenorfina é um agonista parcial dos receptores μ-opioides e antagonista dos receptores κ-opioides. Sua alta afinidade aliada à baixa eficácia intrínseca nos receptores μ confere um perfil de segurança diferenciado em relação a opioides plenos — incluindo menor risco de depressão respiratória —, o que a torna relevante em contextos clínicos com janelas terapêuticas estreitas.

A porfiria intermitente aguda (AIP) é uma doença metabólica rara causada por deficiência da enzima HMBS (hidroximetilbilano sintase), resultando em acúmulo de percursores de porfirinas (ALA e PBG). Crises agudas podem ser desencadeadas por inúmeros fármacos — barbitúricos, sulfonamidas, certos anticonvulsivantes — tornando o manejo farmacológico perioperatório especialmente desafiador.

O vínculo sugerido pela previsão TxGNN não representa um reposicionamento para tratar a patologia de base da AIP, mas sim o reconhecimento de que buprenorfina pode figurar como opção analgésica relativamente segura em pacientes portadores da doença. Não há suporte mecanístico para inibição da via de biossíntese do heme ou redução do acúmulo de precursores de porfirina — a conexão é de contexto de segurança farmacológica, não de terapia etiológica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui – Japanese Journal of Anesthesiology | Relato de manejo anestésico em paciente de 40 anos com AIP submetida a histerectomia radical por tumor maligno ovariano; descreve as precauções com fármacos indutores de crises e a estratégia de analgesia perioperatória adotada |

---

## Informações de Comercialização no Brasil

Buprenorfina não possui registro ativo na ANVISA e não é comercializada no mercado brasileiro. Não há licenças ativas a listar.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A única evidência disponível é um relato de caso de 1993 sobre manejo anestésico em pacientes com AIP, sem nenhum ensaio clínico registrado e sem estudo dedicado ao reposicionamento terapêutico. O vínculo é fundamentalmente indireto: buprenorfina aparece no contexto como analgésico perioperatório relativamente seguro em AIP — e não como agente modificador da doença de base. A pontuação TxGNN de 99.41% provavelmente reflete conexões no grafo de conhecimento relacionadas ao perfil de segurança farmacológica em condições metabólicas raras, e não uma hipótese de reposicionamento convencional.

**Para prosseguir, é necessário:**
- Confirmação do MOA detalhado de buprenorfina via DrugBank API (DG002 pendente)
- Download e análise da bula (DG001 pendente) para avaliar advertências e contraindicações formais
- Revisão das diretrizes da European Porphyria Network (E-POC) e listas de fármacos seguros/inseguros em AIP
- Pesquisa ampliada em PubMed com termos combinados como *"buprenorphine porphyria safety"* e *"opioids acute intermittent porphyria"*
- Caso haja interesse clínico real, seria necessário registro na ANVISA antes de qualquer uso no Brasil
---

