---
layout: default
title: Terbinafine
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Terbinafine
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

# Terbinafine: Das Infecções Fúngicas Superficiais à Miíase Furuncular

## Resumo em Uma Frase

Terbinafine (Lamisil) é um agente antifúngico da classe das alilaminas indicado para infecções superficiais por dermatófitos — incluindo tinea pedis, tinea corporis e onicomicose — cujo mecanismo central é a inibição da esqualeno epoxidase fúngica.
O modelo TxGNN prevê com pontuação de **96.74%** que pode ser eficaz para **Miíase Furuncular (Furuncular Myiasis)**;
contudo, esta predição conta com **0 ensaios clínicos** e apenas **1 relato de caso** documentando falha terapêutica, sendo identificada como sinal falso-positivo do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções fúngicas superficiais por dermatófitos (tinea pedis, tinea corporis, onicomicose) |
| Nova Indicação Prevista | Miíase Furuncular (Furuncular Myiasis) |
| Pontuação de Previsão TxGNN | 96.74% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Terbinafine é um antifúngico da classe das alilaminas que exerce sua ação pela **inibição seletiva da esqualeno epoxidase fúngica (SQLE)**, enzima-chave na biossíntese do ergosterol — componente essencial da membrana celular fúngica. Esta inibição provoca acúmulo tóxico de esqualeno e depleção de ergosterol, resultando em ação fungicida contra dermatófitos e fungistática contra algumas espécies de *Candida*. A alta seletividade pela SQLE fúngica em relação à SQLE humana confere ao fármaco um perfil favorável de segurança sistêmica.

A miíase furuncular é causada pela parasitose por larvas de moscas da ordem Diptera — principalmente *Dermatobia hominis* (berne) nas Américas e *Cordylobia anthropophaga* na África — que invadem o tecido subcutâneo formando nódulos furunculares dolorosos com abertura central. Trata-se de uma infecção parasitária por artrópode, sem qualquer envolvimento fúngico na fisiopatologia ou no ciclo biológico do agente causador.

**Do ponto de vista mecanístico, esta previsão não possui base biológica plausível.** O mecanismo de inibição da SQLE fúngica é específico para fungos e não tem aplicabilidade sobre larvas de dípteros, cujo metabolismo esterólico difere fundamentalmente da célula fúngica. A alta pontuação do TxGNN (96.74%) origina-se provavelmente da proximidade entre nós de doenças cutâneas parasitárias e fúngicas no grafo de conhecimento — ambas envolvem pele e tecido subcutâneo com apresentação clínica nodular —, caracterizando um **falso-positivo estrutural do modelo**, e não uma predição terapeuticamente válida.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25016125](https://pubmed.ncbi.nlm.nih.gov/25016125/) | 2014 | Relato de Caso | Turkiye Parazitolojii Dergisi | Menino de 12 anos com miíase furuncular na nuca, tratado por 2 meses com penicilina, claritromicina, terbinafina e ibuprofeno sem melhora; diagnóstico definitivo revelou parasitose por larva — terbinafina foi usada empiricamente para suposta infecção fúngica e não teve papel terapêutico na miíase |

---

## Informações de Comercialização no Brasil

Terbinafine não possui registros ativos na ANVISA — **0 registros** identificados na base de dados regulatória brasileira. O medicamento não está comercializado no mercado nacional neste momento.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para miíase furuncular constitui um falso-positivo do modelo: terbinafine não possui mecanismo de ação sobre larvas de insetos dipteros, e o único relato de caso identificado na literatura confirma ausência de eficácia nessa condição. Não há base mecanística, ensaio clínico ou evidência clínica direta que suporte o reposicionamento nesta indicação.

**Para prosseguir com a avaliação de reposicionamento de terbinafine, é necessário:**

- Redirecionar a análise para as indicações com suporte biológico e evidência clínica real disponíveis neste pacote:
  - **Tinea manuum** (Rank 8 — Nível L2, Proceed with Guardrails): mecanismo on-target, ensaio clínico direto identificado
  - **Superficial Mycosis** (Rank 10 — Nível L2, Proceed with Guardrails): ensaio comparativo completado (NCT05578950, n=100)
  - **Cutaneous Candidiasis** (Rank 5 — Nível L3, Research Question): múltiplas revisões e dados in vitro de atividade
  - **Blastomycosis** (Rank 7 — Nível L4, Research Question): relato de caso humano com sucesso terapêutico
- Verificar possibilidade de regularização junto à ANVISA para indicações com evidência consolidada em mercados internacionais
- Obter dados completos de segurança (advertências, contraindicações, perfil de interações) via consulta à bula oficial e DrugBank API
- Monitorar emergência de resistência por mutações SQLE em *Trichophyton indotineae*, relevante para indicações dermatofíticas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

