---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Elafibranor
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

# Elafibranor: Da Colangite Biliar Primária à Amenorreia

## Resumo em Uma Frase

Elafibranor é um agonista dual de PPAR-α/δ, aprovado para o tratamento da Colangite Biliar Primária (CBP), uma doença hepática autoimune crônica.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (amenorrhea)** como nova indicação potencial,
com pontuação de **99,86%** — porém, atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Colangite Biliar Primária (PBC) |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 99,86% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base nas informações conhecidas, Elafibranor é um agonista dual de PPAR-α/δ (Peroxisome Proliferator-Activated Receptor alpha/delta), cuja eficácia em Colangite Biliar Primária foi clinicamente comprovada — atua reduzindo a inflamação hepática e a fibrose por meio da ativação de vias metabólicas e anti-inflamatórias mediadas pelos receptores PPAR-α e PPAR-δ.

A ligação mecanística proposta com amenorreia é **indireta e especulativa**: a ativação de PPAR-α/δ pode influenciar o metabolismo lipídico e, por via do tecido adiposo como fonte de estrogênio periférico, afetar indiretamente o eixo hipotálamo-hipófise-gonadal (eixo HPG). Contudo, este caminho é de múltiplos passos e não há evidência direta de que Elafibranor module o ciclo menstrual ou corrija deficiências hormonais subjacentes à amenorreia.

Importa notar que a regulação do eixo HPG é primariamente mediada por PPAR-γ (e não PPAR-α/δ), o que torna a hipótese ainda mais tênue. A previsão do TxGNN pode refletir associações indiretas no grafo de conhecimento entre metabolismo lipídico, adiposidade e função reprodutiva, sem necessariamente indicar um efeito farmacológico direto e clinicamente relevante.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O registro consta como ativo na base de dados regulatória brasileira, porém os detalhes de nome comercial, forma farmacêutica e indicação aprovada não estão disponíveis no Evidence Pack atual.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|--------------------|----------------|--------------------|--------------------|
| (não disponível) | (não disponível) | (não disponível) | (não disponível) |

> **Nota:** O `total_licenses = 1` confirma existência de registro ativo. Os campos detalhados devem ser obtidos diretamente junto à ANVISA para complementação.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN apresenta pontuação elevada (99,86%), porém a ligação mecanística entre Elafibranor (PPAR-α/δ) e amenorreia é altamente indireta — sem suporte de ensaios clínicos, publicações científicas ou mecanismo de ação diretamente estabelecido. O nível de evidência L5 (apenas previsão computacional) não é suficiente para avançar para avaliação clínica.

**Para prosseguir, é necessário:**
- Obter dados completos do mecanismo de ação (MOA) via DrugBank API — identificar se há alguma via conhecida relacionada ao eixo HPG ou função reprodutiva
- Descarregar a bula aprovada junto à ANVISA para preencher as lacunas de segurança (advertências, contraindicações)
- Complementar os detalhes do registro ANVISA (nome comercial, forma farmacêutica, indicação aprovada)
- Realizar busca bibliográfica expandida: pesquisar associações entre PPAR agonistas e função reprodutiva/hormonal em literatura pré-clínica
- Revisar se outras indicações no ranking TxGNN (ex.: rank 7 — carcinoma de vesícula biliar, mais próximo da indicação original em CBP) apresentam melhor fundamentação mecanística para priorização
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

