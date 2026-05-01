---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose: Da encefalopatia hepática à nefropatia aguda por urato

## Resumo em Uma Frase

Lactulose é um dissacarídeo sintético não absorvível, amplamente utilizado no tratamento da constipação intestinal e da encefalopatia hepática. O modelo TxGNN prevê que pode ser eficaz para **Nefropatia Aguda por Urato (Acute Urate Nephropathy)**, com pontuação de **99,89%** — porém, atualmente **não há ensaios clínicos nem publicações** diretamente apoiando essa direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Encefalopatia hepática / Constipação intestinal (dados detalhados de registro indisponíveis neste pack) |
| Nova Indicação Prevista | Nefropatia Aguda por Urato (Acute Urate Nephropathy) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 19 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento farmacológico estabelecido, a lactulose é um dissacarídeo não absorvível fermentado pela microbiota do cólon, gerando ácidos graxos de cadeia curta que acidificam o ambiente intestinal e produzem efeito osmótico laxante. Essa acidificação do cólon é também o mecanismo central pelo qual a lactulose reduz a absorção intestinal de amônia, sendo aplicada há décadas no tratamento da encefalopatia hepática.

A nefropatia aguda por urato (NAU) é uma complicação comum da síndrome de lise tumoral, em que cristais de ácido úrico se depositam nos túbulos renais, desencadeando insuficiência renal aguda. A lactulose não possui ação direta sobre o metabolismo do ácido úrico. O caminho mecanístico especulativo proposto envolve a excreção intestinal de urato: certas bactérias intestinais (como *Lactobacillus gasseri* e *Bifidobacterium*) são capazes de degradar urato; ao modificar a composição da microbiota intestinal, a lactulose poderia teoricamente aumentar essa degradação, reduzindo a carga sistêmica de urato.

Esse caminho indireto, porém, carece completamente de suporte em estudos clínicos ou em modelos animais para esta indicação específica. A alta pontuação do TxGNN reflete provavelmente a conectividade indireta no grafo do conhecimento entre nós de "lesão renal aguda" e nós de "proteção renal" vinculados à lactulose — e não uma relação farmacológica direta. Trata-se de um sinal de hipótese, não de indicação terapêutica estabelecida.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Os dados individuais dos 19 registros (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack. A situação geral de mercado confirma que a lactulose está **comercializada no Brasil** com 19 registros ativos.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para nefropatia aguda por urato não possui suporte de ensaios clínicos nem de literatura diretamente relacionada. O caminho mecanístico proposto — modulação da microbiota intestinal para aumentar a degradação de urato — é altamente especulativo e carece de qualquer validação experimental, tornando prematuro qualquer avanço clínico nesta direção.

**Para prosseguir, é necessário:**
- Estudos mecanísticos *in vitro* / *in vivo* investigando o efeito da lactulose sobre a excreção intestinal de urato e a microbiota associada
- Modelos animais de síndrome de lise tumoral com avaliação do papel da microbiota intestinal na clearance de urato
- Dados detalhados dos 19 registros ANVISA (indicações aprovadas, formas farmacêuticas e posologia)
- Mecanismo de ação completo (MOA) obtido via consulta ao DrugBank API
- Informações de segurança da bula brasileira (advertências, contraindicações)
---

