---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

A skill `txgnn-pipeline` foi invocada. Com base no Evidence Pack fornecido, segue o relatório completo de avaliação de reposicionamento para Latanoprost:

---

# Latanoprost: Do glaucoma de ângulo aberto ao glaucoma hereditário primário

## Resumo em Uma Frase

Latanoprost é um análogo sintético da prostaglandina F2α (PGF2α), amplamente utilizado no tratamento do glaucoma de ângulo aberto e da hipertensão ocular para reduzir a pressão intraocular (PIO).
O modelo TxGNN prevê que pode ser eficaz para **Glaucoma Hereditário Primário (Primary Hereditary Glaucoma)**,
atualmente com **1 ensaio clínico** concluído apoiando esta direção e **nenhuma publicação** indexada especificamente para esta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glaucoma de ângulo aberto / Hipertensão ocular (uso clínico estabelecido) |
| Nova Indicação Prevista | Glaucoma Hereditário Primário (Primary Hereditary Glaucoma) |
| Pontuação de Previsão TxGNN | 99.88% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Contudo, com base no conhecimento clínico consolidado, Latanoprost é um análogo sintético da prostaglandina F2α que atua como agonista seletivo do receptor FP. Ao ativar esse receptor no músculo ciliar e no epitélio da malha trabecular, promove aumento do fluxo uveoscleral, reduzindo a PIO. É considerado tratamento de primeira linha para o glaucoma primário de ângulo aberto no adulto em todo o mundo.

O glaucoma hereditário primário — também denominado glaucoma congênito ou glaucoma pediátrico — tem como mecanismo fisiopatológico central a goniodesgenesia: um defeito no desenvolvimento do ângulo da câmara anterior que compromete a drenagem do humor aquoso e resulta em elevação crónica da PIO. Este é precisamente o mesmo parâmetro terapêutico alvo do Latanoprost, tornando a extrapolação mecanística altamente coerente e biologicamente plausível.

Na prática clínica, Latanoprost já é utilizado de forma off-label em crianças com glaucoma refratário a procedimentos cirúrgicos. O ensaio identificado (NCT01527682) confirma essa realidade clínica e reforça que a previsão do TxGNN representa uma extensão natural e bem fundamentada do uso já estabelecido, distinguindo-se de um reposicionamento para uma área completamente nova.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Concluído | 37 | Avalia o efeito hipotensor ocular de latanoprost e dorzolamida em pacientes pediátricos com Glaucoma Primário refratário a procedimentos cirúrgicos; inclui avaliação de eficácia e segurança |

---

## Evidências da Literatura

Atualmente não há literatura relacionada indexada para a combinação Latanoprost + glaucoma hereditário primário.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Um ensaio clínico de Phase 2 concluído apoia diretamente o uso de Latanoprost em glaucoma pediátrico primário, e o mecanismo de ação (redução da PIO via agonismo do receptor FP) é idêntico ao da indicação estabelecida, conferindo plausibilidade biológica máxima. A lacuna está na ausência de literatura PubMed indexada com este descritor específico, não em falta de evidência clínica.

**Para prosseguir, é necessário:**
- Recuperar advertências, contraindicações e informações de posologia da bula ANVISA (dado atualmente ausente — DG001)
- Confirmar mecanismo de ação detalhado via consulta ao DrugBank API (DG002)
- Ampliar busca PubMed com termos alternativos: "latanoprost pediatric glaucoma", "latanoprost congenital glaucoma", "prostaglandin analogue childhood glaucoma"
- Verificar disponibilidade e adequação da formulação colírio 0,005% para faixa etária pediátrica no Brasil
- Consultar especialista em oftalmologia pediátrica para validação clínica antes de qualquer aplicação prática
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

