---
layout: default
title: Nimesulide
parent: Evidência Moderada (L3-L4)
nav_order: 470
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Nimesulide: nova indicação prevista, Gota (gout) (nível de evidência L3). Indicação original: Não informada nos dados de registro da ANVISA (referência farmacológi…"
monitor_inn: "Nimesulide"
predicted_indications: ["gout", "headache disorder", "trigeminal autonomic cephalalgia", "rheumatoid arthritis", "migraine disorder", "migraine with brainstem aura", "tendinitis", "exostosis", "idiopathic granulomatous myositis", "myositis fibrosa"]
---

# Nimesulide
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Nimesulida: De fármaco anti-inflamatório (sem indicação registrada no Brasil) para gota

## Resumo em Uma Frase

Nimesulida é um anti-inflamatório não esteroidal (AINE), inibidor preferencial da COX-2, usado em diversos países para dor aguda, osteoartrite e dismenorreia primária. Não há indicação aprovada registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **gota (gout)**, atualmente com **0 ensaios clínicos registrados** e **2 estudos clínicos pequenos em russo** (entre 12 publicações listadas) apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não informada nos dados de registro da ANVISA (referência farmacológica: dor aguda, osteoartrite, dismenorreia primária) |
| Nova Indicação Prevista | Gota (gout) |
| Pontuação de Previsão TxGNN | 97,57% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações farmacológicas conhecidas, a nimesulida é um inibidor preferencial da COX-2 (e também interage com a COX-1), reduzindo a síntese de prostaglandinas que mediam inflamação e dor.

Os AINEs são uma opção padrão no tratamento da artrite gotosa aguda, pois suprimem a inflamação mediada por prostaglandinas. Como a nimesulida atua nessa mesma via, a previsão do modelo é mecanisticamente plausível: o uso original (dor e inflamação) e a nova indicação (crise inflamatória da gota) compartilham o mesmo alvo.

Há, porém, ressalvas importantes. Os dois estudos clínicos específicos em gota são pequenos, em russo e de desenho incerto. Além disso, a nimesulida tem preocupações de hepatotoxicidade em humanos e não é comercializada no Brasil.

**Outras indicações previstas (para contexto):**

| Indicação | Pontuação TxGNN | Nível | Recomendação |
|------|------|------|------|
| Cefaleia (headache disorder) | 96,60% | L3 | Pergunta de pesquisa |
| Cefalalgia autonômica trigeminal | 96,23% | L5 | Hold |
| Artrite reumatoide | 95,32% | L3 | Pergunta de pesquisa |
| Enxaqueca (migraine disorder) | 94,85% | L3 | Pergunta de pesquisa |
| Enxaqueca com aura do tronco encefálico | 94,72% | L5 | Hold |
| Tendinite | 94,20% | L2 | Pergunta de pesquisa |
| Exostose | 94,17% | L5 | Hold |
| Miosite granulomatosa idiopática | 93,97% | L5 | Hold |
| Miosite fibrosa | 93,97% | L5 | Hold |

Entre as alternativas, a **tendinite** tem a evidência clínica mais consistente (estudos duplo-cegos comparativos com naproxeno e diclofenaco), embora antigos e sem controle com placebo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15732721](https://pubmed.ncbi.nlm.nih.gov/15732721/) | 2004 | Estudo clínico (provavelmente aberto/não controlado) | Klinicheskaia meditsina | Eficácia e segurança da nimesulida em pacientes com artrite gotosa, população de alto risco para complicações dos AINEs |
| [17672073](https://pubmed.ncbi.nlm.nih.gov/17672073/) | 2007 | Estudo clínico comparativo | Terapevticheskii arkhiv | Comparação do tempo até o efeito analgésico e anti-inflamatório entre nimesulida (granulado e comprimido) e diclofenaco sódico na artrite gotosa |
| [32841190](https://pubmed.ncbi.nlm.nih.gov/32841190/) | 2020 | Revisão / relato de caso | Georgian Medical News | Erros de diagnóstico e tratamento na gota, à luz das diretrizes ACR e EULAR 2018 (relevância indireta) |
| [14963695](https://pubmed.ncbi.nlm.nih.gov/14963695/) | 2005 | In vitro / mecanístico | Rheumatology International | Efeitos da colchicina e da hidroxicloroquina sobre COX-1 e COX-2 (relevância indireta) |
| [29300762](https://pubmed.ncbi.nlm.nih.gov/29300762/) | 2018 | In vitro | PLoS One | Triagem de propriedades anti-glicação de 18 fármacos comuns, em contexto de reposicionamento |

**Observação:** outras publicações listadas tratam da toxicidade da nimesulida em aves necrófagas (abutres do gênero *Gyps* e milhafres), não relevantes para eficácia em humanos, e foram omitidas desta tabela.

---

## Considerações de Segurança

- **Interações e alvos farmacológicos:** a nimesulida atua sobre COX-1 (PTGS1) e COX-2 (PTGS2) em humanos, e sobre o transportador B⁰AT1 (Slc6a19) em ratos. Não há níveis de gravidade de interação medicamentosa classificados nos dados compilados.
- **Hepatotoxicidade:** a literatura relata preocupações de hepatotoxicidade em humanos, incluindo um caso de hepatite subfulminante que exigiu transplante hepático (PMID 12070417), além de trombocitopenia. O uso oral foi banido em vários países.
- **Toxicidade em animais:** a nimesulida é letal para abutres do gênero *Gyps*, o que é relevante do ponto de vista ambiental, não clínico.

Consulte a bula para informações adicionais de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é mecanisticamente plausível, mas a evidência específica para gota se limita a dois estudos pequenos em russo, sem ensaios registrados. O fármaco não é comercializado no Brasil e tem risco hepático relevante, o que pesa contra o avanço imediato.

**Para prosseguir, é necessário:**
- Obter a bula e os dados de advertências e contraindicações na ANVISA (lacuna bloqueante para a triagem de segurança)
- Obter dados detalhados do mecanismo de ação (MOA) no DrugBank
- Confirmar o desenho e os resultados dos estudos em gota (PMIDs 15732721 e 17672073), incluindo texto completo traduzido
- Comparar o perfil benefício-risco com os AINEs já disponíveis no Brasil para gota (por exemplo, naproxeno e indometacina) e avaliar se o risco hepático é aceitável
- Considerar priorizar a tendinite, que tem a base de evidência mais sólida entre as indicações previstas, se houver interesse em avançar com o fármaco
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

