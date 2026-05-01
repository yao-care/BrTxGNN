---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Tetracycline
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

# Tetracycline: De Infecções por Chlamydia à Ceratoconjuntivite Epitelial Puntiforme

## Resumo em Uma Frase

Tetracycline é um antibiótico de amplo espectro com atividade comprovada contra *Chlamydia trachomatis*, micoplasmas, riquétsias e diversas bactérias Gram-positivas e Gram-negativas, sem indicação aprovada nem registro ativo no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Ceratoconjuntivite Epitelial Puntiforme (Punctate Epithelial Keratoconjunctivitis)**, atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas de amplo espectro (sem indicação aprovada registrada no Brasil) |
| Nova Indicação Prevista | Ceratoconjuntivite Epitelial Puntiforme (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99.58% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Tetracycline é um antibiótico bacteriostático de amplo espectro que age pela ligação reversível à subunidade ribossomal 30S bacteriana, bloqueando a associação do aminoacil-tRNA ao complexo ribossomo-mRNA e inibindo, assim, a síntese proteica. Historicamente, é o tratamento de referência para infecções por *Chlamydia trachomatis* — um dos principais agentes etiológicos da ceratoconjuntivite folicular —, além de possuir atividade contra bactérias atípicas, riquétsias e *Helicobacter pylori*.

A ceratoconjuntivite epitelial puntiforme (PEK) é uma condição inflamatória da superfície ocular caracterizada por lesões puntiformes no epitélio corneano, podendo ter origem infecciosa (viral, bacteriana ou por Chlamydia) ou imunomediada. A conexão teórica com Tetracycline assenta em dois eixos: (1) atividade anti-*Chlamydia*, já que a infecção por *C. trachomatis* pode desencadear ou perpetuar a ceratoconjuntivite; e (2) inibição de metaloproteinases da matriz MMP-8 e MMP-9, enzimas envolvidas na degradação do estroma corneano, que em tese poderia atenuar a lesão epitelial por via anti-inflamatória.

No entanto, o único estudo disponível (PMID 1424659, 1992) relata justamente um achado paradoxal: dois pacientes desenvolveram PEK persistente bilateral como *sequela* após o tratamento bem-sucedido de conjuntivite folicular por *C. trachomatis* com Tetracycline ou doxiciclina oral. Esse dado sugere que a alta pontuação TxGNN (0.9958) reflete, provavelmente, a proximidade geográfica no grafo de conhecimento entre doenças associadas a infecção por Chlamydia — e não uma predição genuína de eficácia terapêutica na PEK como alvo primário. As hipóteses mecanísticas permanecem não testadas clinicamente nesta indicação específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Série de Casos Retrospectiva | *Cornea* | Dois casos de PEK puntiforme epitelial bilateral persistente após resolução de conjuntivite folicular por *Chlamydia trachomatis*. Ambos os pacientes foram inicialmente tratados com Tetracycline oral ou doxiciclina, com resolução dos folículos. Apesar da cura da infecção primária, desenvolveram lesões corneanas recidivantes em múltiplos níveis epiteliais com coloração fluorescente puntiforme, além de edema estromal anterior em um dos casos. |

---

## Informações de Comercialização no Brasil

Tetracycline não possui registros ativos na ANVISA e não está comercializado no Brasil (total de registros: 0).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A base de evidências para Tetracycline na ceratoconjuntivite epitelial puntiforme é insuficiente para qualquer avanço clínico — apenas um relato de série de casos de 1992, sem ensaios clínicos registrados, com um achado paradoxal que documenta PEK como *complicação* do tratamento com tetraciclinas, e não como benefício terapêutico. Adicionalmente, o medicamento não está registrado no Brasil, o que representa uma barreira regulatória adicional.

**Para prosseguir, é necessário:**
- Estudos mecanísticos in vitro que validem a hipótese anti-MMP na PEK e na superfície ocular
- Avaliação de citotoxicidade em células epiteliais corneanas e fibroblastos da membrana timpânica humana
- Definição da via de administração adequada (sistêmica vs. tópica ocular) e desenvolvimento de formulação adequada
- Ensaios clínicos de fase inicial (Phase 1/2) específicos para PEK, com estratificação por etiologia (infecciosa vs. imunomediada)
- Regularização do registro de Tetracycline na ANVISA antes de qualquer desenvolvimento clínico no Brasil
- Avaliação comparativa com doxiciclina, que apresenta maior penetração tecidual e perfil anti-MMP mais robusto, e para a qual existem dados clínicos mais extensos em indicações relacionadas (ex.: sinusite rinossinal crônica — Rank 3 neste pacote, Nível L2)

> ⚠️ **Nota sobre o conjunto de previsões**: Embora a ceratoconjuntivite epitelial puntiforme seja a indicação com maior pontuação TxGNN neste pacote, outras indicações apresentam suporte clínico consideravelmente mais robusto — em particular a **Rinossinusite Crônica** (Rank 3, L2, 4 ensaios clínicos incluindo Phase 3 com doxiciclina) e o **Distúrbio Pós-Bacteriano / Erradicação de *H. pylori*** (Rank 7, L2, com ensaio Phase 3 direto utilizando Tetracycline em quadriterapia bismutada). Recomenda-se reavaliar o portfólio de reposicionamento priorizando essas indicações com evidências mais sólidas.
---

