---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 6
---

# Finasteride
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

# Finasteride: Da alopecia androgênica à hipertricose congênita tipo Ambras

## Resumo em Uma Frase

Finasteride é um inibidor da 5α-redutase, utilizado clinicamente no tratamento da alopecia androgênica masculina (queda de cabelo de padrão masculino) e da hiperplasia prostática benigna.
O modelo TxGNN prevê que pode ser eficaz para a **Hipertricose Congênita Universal Tipo Ambras (Ambras type hypertrichosis universalis congenita)**,
porém essa previsão conta com **0 ensaios clínicos** e **0 publicações** de suporte direto, sendo classificada como provável falso positivo do modelo de grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Alopecia androgênica / Hiperplasia prostática benigna (sem registro ANVISA) |
| Nova Indicação Prevista | Hipertricose Congênita Universal Tipo Ambras |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Finasteride atua como inibidor seletivo da 5α-redutase tipo II, enzima responsável pela conversão da testosterona em diidrotestosterona (DHT). Ao reduzir os níveis circulantes de DHT, o fármaco desacelera a miniaturização dos folículos pilosos androgênio-sensíveis (alopecia androgênica) e diminui o volume prostático (hiperplasia prostática benigna). Esse mecanismo é inteiramente dependente da via androgênica.

A Síndrome de Ambras, por outro lado, é uma doença genética extremamente rara causada por mutações no gene TRPS1 ou por rearranjos cromossômicos na região 8q23-q24, resultando em crescimento difuso de pelos em todo o corpo desde o nascimento — em padrão completamente independente de andrógenos. Não há participação da via DHT na sua fisiopatologia, tornando o mecanismo do Finasteride inaplicável a essa condição.

A alta pontuação do TxGNN (99,99%) provavelmente decorre de adjacência indireta na rede do grafo de conhecimento entre nós de "doenças capilares" e o perfil farmacológico do Finasteride — um fenômeno de falso positivo estrutural do grafo, sem respaldo mecanístico ou empírico. Nenhuma evidência clínica ou pré-clínica publicada foi identificada para essa indicação específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

---

## Evidências da Literatura

Atualmente não há literatura relacionada a esta indicação específica.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A Hipertricose Tipo Ambras é uma doença de origem genética (TRPS1/8q23-q24) completamente independente da via DHT, sem qualquer suporte mecanístico, clínico ou pré-clínico para o uso de Finasteride — a previsão do TxGNN é classificada como provável falso positivo de grafo de conhecimento.

**Para prosseguir, é necessário:**
- Redirecionar a análise para a indicação de **Hipertricose geral (rank 2)**, que possui 1 ensaio clínico e 4 publicações, com mecanismo plausível para o subgrupo androgênio-dependente (hirsutismo feminino)
- Verificar o status regulatório atualizado do Finasteride no Brasil via consulta direta ao portal ANVISA
- Obter dados completos de MOA via DrugBank API (gap de severidade Alta identificado)
- Recuperar advertências, contraindicações e monografias do produto via bula ANVISA (gap Bloqueante identificado)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

