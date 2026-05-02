---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Sodium Citrate
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

---

# Citrato de Sódio: De alcalinizante/tampão de pH para Conjuntivite Papilar

## Resumo em Uma Frase

Citrato de sódio é um sal orgânico multipotente com usos farmacêuticos consolidados como tampão de pH, alcalinizante urinário e anticoagulante em formulações, porém sem indicação terapêutica primária formalmente registrada nos dados disponíveis.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Papilar (Papillary Conjunctivitis)**,
atualmente sem ensaios clínicos nem publicações diretamente apoiando esta direção — **Nível de Evidência L5**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível (sem registro no Brasil) |
| Nova Indicação Prevista | Conjuntivite Papilar (Papillary Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação de citrato de sódio neste banco de dados. Com base em informações conhecidas, trata-se de um sal orgânico cujas propriedades farmacológicas incluem tamponamento de pH em ampla faixa fisiológica, alcalinização sistêmica e urinária, e quelação de Ca²⁺ extracelular — este último mecanismo sendo responsável por seu uso clássico como anticoagulante em bolsas de coleta de sangue e soluções de hemodiálise. Citrato de sódio aparece frequentemente como excipiente em formulações oftálmicas, onde atua como estabilizador de pH.

A conjuntivite papilar é uma inflamação ocular mediada por células imunes, caracterizada pela formação de papilas na conjuntiva tarsal, tipicamente desencadeada por uso prolongado de lentes de contato, próteses oculares ou hipersensibilidade a conservantes. Mecanisticamente, citrato de sódio poderia teoricamente beneficiar esta condição por dois caminhos: (1) manutenção do equilíbrio de pH da superfície ocular, reduzindo estímulos inflamatórios locais; (2) quelação de Ca²⁺ extracelular, com potencial de modular a degranulação de mastócitos dependente de cálcio, que é central na fisiopatologia da conjuntivite alérgica e papilar.

Entretanto, a conexão mecanística é altamente especulativa. A pontuação elevada do TxGNN (0,9995) é provavelmente resultado de um efeito de adjacência no grafo de conhecimento — citrato de sódio figura como excipiente em formulações oftálmicas, criando conexões indiretas com o cluster de doenças inflamatórias oculares no grafo — e não reflete uma relação farmacológica primária estabelecida. Não há qualquer evidência pré-clínica ou clínica direta que suporte esta indicação terapêutica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Citrato de sódio não possui registros ativos na ANVISA como princípio ativo terapêutico principal. O produto não está comercializado no mercado brasileiro nesta categoria.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para conjuntivite papilar é fundamentada exclusivamente no modelo computacional (L5), sem qualquer ensaio clínico ou publicação científica direta de suporte. A conexão mecanística é especulativa e a pontuação elevada pode ser artefato de adjacência no grafo de conhecimento, não indicando relação farmacológica estabelecida.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos in vitro avaliando citrato de sódio em modelos de inflamação ocular e inibição de degranulação de mastócitos
- Confirmação do mecanismo de ação relevante para conjuntivite papilar (modulação de Ca²⁺/mastócitos, tamponamento de pH da superfície ocular)
- Avaliação da segurança ocular local — citotoxicidade, tolerância e irritação — de formulações tópicas com citrato de sódio em concentrações terapêuticas
- Levantamento sistemático de literatura sobre citrato de sódio em formulações oftálmicas existentes (como excipiente ativo vs. inerte)
- Avaliação regulatória junto à ANVISA para desenvolvimento de formulação oftálmica e eventual registro no Brasil
---

