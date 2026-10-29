---
layout: default
title: Hydroquinone
parent: Apenas Predição do Modelo (L5)
nav_order: 357
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-29
description: "Hydroquinone: nova indicação prevista, Ceratose Seborreica (Seborrheic Keratosis) (nível de evidência L4). Indicação original: Desmelanizantes (despigmentantes)"
monitor_inn: "hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Hidroquinona: De desmelanizante a ceratose seborreica
{: .text-alpha }

## Resumo em Uma Frase

Hidroquinona é um agente despigmentante (desmelanizante), usado originalmente para clarear manchas e hiperpigmentações da pele.
O modelo TxGNN prevê que pode ser eficaz para **Ceratose Seborreica (Seborrheic Keratosis)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (estudo observacional indireto) apoiando esta direção. Trata-se, portanto, de uma previsão essencialmente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Desmelanizantes (despigmentantes) |
| Nova Indicação Prevista | Ceratose Seborreica (Seborrheic Keratosis) |
| Pontuação de Previsão TxGNN | 0,9973 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 11 de 12) |
| Número de Registros | 12 (ativos: 11) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a hidroquinona inibe a tirosinase, enzima-chave da síntese de melanina, e reduz a produção desse pigmento. Sua eficácia como despigmentante em condições como melasma e hiperpigmentações é a base de seu uso original.

A relação com a nova indicação é limitada. Mecanisticamente, a hidroquinona poderia clarear a hiperpigmentação das lesões de ceratose seborreica. No entanto, essa condição é uma proliferação epidérmica benigna, e não um distúrbio primário da melanogênese. Clarear a lesão não trataria a lesão em si.

A única publicação disponível é um estudo observacional prospectivo sobre tratamento combinado de distúrbios pigmentares faciais em pacientes asiáticos. Ele não testou a hidroquinona especificamente em ceratose seborreica. A pontuação elevada do TxGNN é uma previsão computacional, sem respaldo clínico direto até o momento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para ceratose seborreica.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Coorte (observacional prospectivo) | J Plast Reconstr Aesthet Surg | Algoritmo de tratamento combinado para distúrbios pigmentares faciais em pacientes asiáticos. Não avalia a hidroquinona isoladamente em ceratose seborreica |

---

## Informações de Comercialização no Brasil

Os 12 registros no Brasil estão vigentes; o medicamento é comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102351141 | Hidroquinona | — | Desmelanizantes |
| Registro 105830901 | Hidroquinona | — | Desmelanizantes |
| Registro 105830634 | Claquinona | — | Desmelanizantes |
| Registro 167730559 | Hidroquinona | — | Desmelanizantes |
| Registro 167730561 | Cleankinol | — | Desmelanizantes |

Há ainda outros 7 registros cancelados (entre eles Solaquin, Hidropeek, Lumiderm, Glyquin XM, Suavicid, Hormoskin e uma associação de hidroquinona + tretinoína + acetonido de fluocinolona).

---

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento (TxGNN/PrimeKG, não derivadas da bula)**: queimadura solar, insuficiência adrenocortical, doença de Addison, atrofia da pele, telangiectasia, doença capilar, telangiectasia hemorrágica hereditária, doença vascular periférica, claudicação intermitente, doença arterial periférica, eczema atópico e dermatite.

Para as demais informações de segurança (advertências, contraindicações e interações), consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos, e a única publicação é um estudo observacional indireto. Além disso, a ceratose seborreica é uma lesão benigna cuja base não é pigmentar, de modo que a plausibilidade mecanística é fraca. Os 12 registros brasileiros estão vigentes.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), que é uma lacuna bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação via DrugBank
- Esclarecer a relevância clínica da despigmentação em ceratose seborreica, com estudos específicos (por exemplo, estudo piloto ou revisão sistemática)
- Verificar a compatibilidade de via de administração e forma farmacêutica
- Confirmar a situação regulatória dos 12 registros vigentes e avaliar o perfil de segurança para essa possível indicação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

