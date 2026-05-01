---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: Da hiperplasia prostática benigna à hipertricose universal congênita tipo Ambras

## Resumo em Uma Frase

Dutasteride é um inibidor dual da 5α-redutase, originalmente utilizado no tratamento da **hiperplasia prostática benigna (HPB)** e da alopecia androgenética.
O modelo TxGNN prevê que pode ser eficaz para a **Hipertricose Universal Congênita tipo Ambras (Ambras type hypertrichosis universalis congenita)**, porém atualmente **não há ensaios clínicos nem publicações** diretamente apoiando esta direção.
A pontuação de previsão elevada contrasta com a ausência total de evidências clínicas, o que exige cautela na interpretação dos resultados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hiperplasia prostática benigna (HPB) |
| Nova Indicação Prevista | Hipertricose Universal Congênita tipo Ambras |
| Pontuação de Previsão TxGNN | 99,998% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não registrado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Dutasteride é um inibidor dual da 5α-redutase (tipos 1 e 2), enzima responsável pela conversão de testosterona em di-hidrotestosterona (DHT). Ao suprimir a produção de DHT, o fármaco reduz o volume prostático em pacientes com HPB e, em folículos capilares sensíveis a andrógenos, pode modular o ciclo de crescimento capilar — fundamento do seu uso aprovado na alopecia androgenética (AGA) em vários países.

A Síndrome de Ambras é uma condição geneticamente determinada por mutações no gene **TRPS1**, que resulta em crescimento excessivo e generalizado de pelos em todo o corpo desde o nascimento. Trata-se de uma anomalia estrutural de base genética, **não dependente do eixo androgênico**, o que a distingue fundamentalmente das condições para as quais o Dutasteride possui mecanismo comprovado.

O modelo TxGNN provavelmente associou categoricamente "anormalidades de crescimento piloso" ao grupo farmacológico dos inibidores de 5α-redutase. No entanto, a patofisiologia da Síndrome de Ambras é impulsionada por defeito gênico — não por excesso de DHT —, de modo que a inibição do DHT **não apresenta via de atuação plausível** sobre a causa primária desta condição. A previsão, embora tecnicamente de alta pontuação, carece de correspondência patofisiológica real.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A Síndrome de Ambras é impulsionada por mutação no gene TRPS1 e não pelo eixo androgênico, tornando o mecanismo de ação do Dutasteride — inibição da síntese de DHT — sem via de atuação plausível sobre esta condição. A ausência total de ensaios clínicos e de literatura de suporte confirma que esta previsão ainda não possui base empírica suficiente para avançar.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API
- Identificar estudos pré-clínicos que demonstrem qualquer efeito do Dutasteride em modelos de hipertricose de origem genética
- Obter informações de segurança completas (bula/ANVISA) — atualmente bloqueante para avaliação S1
- Verificar o status de registro do fármaco no mercado brasileiro junto à ANVISA
---

