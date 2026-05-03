---
layout: default
title: Levobunolol
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Levobunolol
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

# Levobunolol: Do glaucoma de ângulo aberto ao glaucoma hereditário primário

## Resumo em Uma Frase

Levobunolol é um β-bloqueador ocular tópico não seletivo, amplamente utilizado no tratamento do glaucoma de ângulo aberto e da hipertensão ocular por meio da redução da pressão intraocular.
O modelo TxGNN prevê que pode ser eficaz para o **Glaucoma Hereditário Primário (Primary Hereditary Glaucoma)**, porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente essa indicação específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glaucoma de ângulo aberto / Hipertensão ocular |
| Nova Indicação Prevista | Glaucoma Hereditário Primário (Primary Hereditary Glaucoma) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis nesta base de dados. Com base na literatura científica consultada, levobunolol é um agente bloqueador β-adrenérgico não seletivo (β1 e β2), comercializado como colírio tópico. Seu efeito hipotensor ocular ocorre pela inibição dos receptores β2 no corpo ciliar, reduzindo a produção do humor aquoso e, consequentemente, diminuindo a pressão intraocular (PIO). Essa classe farmacológica é um dos pilares do tratamento médico do glaucoma há décadas.

O glaucoma hereditário primário — que inclui formas associadas a mutações nos genes *MYOC*, *OPTN*, *CYP1B1*, entre outros — frequentemente cursa com elevação da PIO secundária à disfunção na dinâmica do humor aquoso. Em termos mecanísticos, essa disfunção ainda envolve o eixo adrenérgico-β no corpo ciliar, de modo que a capacidade de levobunolol de suprimir a produção de humor aquoso poderia, em princípio, ser aplicável também a pacientes com glaucoma de origem genética.

Contudo, a ausência total de estudos específicos para esta subpopulação é uma limitação crítica. Mutações genéticas podem alterar a expressão dos receptores β, modificar vias de sinalização intracelular ou alterar a resposta farmacológica ao β-bloqueio — aspectos que ainda não foram investigados clinicamente nessa indicação. A alta pontuação do TxGNN reflete, sobretudo, similaridade topológica no grafo de conhecimento entre levobunolol e as formas clássicas de glaucoma, e não evidência direta para o glaucoma hereditário primário.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Levobunolol possui **3 registros** ativos no mercado brasileiro. Os detalhes individuais de cada registro (número ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis nesta versão da base de dados. Recomenda-se consulta direta ao sistema de consulta de medicamentos da ANVISA para obter informações completas e atualizadas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação extremamente alta do modelo TxGNN (99,98%), a previsão para o glaucoma hereditário primário carece de qualquer suporte empírico direto — não há ensaios clínicos nem publicações específicas nessa indicação. A plausibilidade mecanística existe, mas permanece não verificada para esta subpopulação genética específica.

**Para prosseguir, é necessário:**
- Levantamento sistemático de estudos sobre o uso de β-bloqueadores oculares (especialmente levobunolol ou timolol) em pacientes com diagnóstico genético confirmado de glaucoma hereditário primário (mutações *MYOC*, *CYP1B1*, *OPTN* etc.)
- Verificação de como as mutações genéticas associadas ao glaucoma hereditário afetam a expressão e função dos receptores β2 no corpo ciliar e a responsividade ao tratamento β-bloqueador
- Obtenção dos dados completos de segurança via bula oficial (advertências, contraindicações — pendência DG001)
- Documentação estruturada do mecanismo de ação via DrugBank API (pendência DG002)
- Avaliação de risco para uso pediátrico, considerando que as formas hereditárias frequentemente se manifestam em crianças e jovens, população na qual β-bloqueadores tópicos exigem monitoramento cardiovascular e pulmonar rigoroso
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

