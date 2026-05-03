---
layout: default
title: Gestodene
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Gestodene
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

# Gestodene: De contraceptivo oral à enxaqueca (Migraine Disorder)

## Resumo em Uma Frase

Gestodene é um progestagênio de terceira geração, utilizado como componente ativo em contraceptivos orais combinados (COC).
O modelo TxGNN prevê potencial eficácia para **Enxaqueca (migraine disorder)**,
atualmente sem nenhum ensaio clínico registrado e com apenas **3 publicações** associadas — todas enfocando riscos vasculares do uso de COC, e não tratamento da enxaqueca.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Contracepção oral (componente de COC) |
| Nova Indicação Prevista | Enxaqueca (migraine disorder) |
| Pontuação de Previsão TxGNN | 94.35% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) do gestodene no Evidence Pack. Com base no conhecimento farmacológico estabelecido, o gestodene é um progestagênio de terceira geração com alta seletividade pelo receptor de progesterona, baixa atividade androgênica e sem atividade estrogênica intrínseca. Nos contraceptivos combinados, atua suprimindo a liberação de gonadotrofinas (LH/FSH) para inibir a ovulação.

A hipótese mecanística para enxaqueca baseia-se no fato de que flutuações nos níveis de esteroides sexuais — especialmente a queda abrupta de estrogênio no período peri-menstrual — podem desencadear crises de enxaqueca via ativação do sistema CGRP e da via trigeminovascular. A estabilização hormonal promovida por progestagênios poderia, em tese, reduzir essa variabilidade.

Contudo, esta previsão apresenta uma contradição clínica fundamental: a **enxaqueca com aura** é contraindicação absoluta reconhecida para contraceptivos orais que contêm estrogênio (formulações típicas com gestodene), devido ao risco substancialmente elevado de acidente vascular cerebral isquêmico. As três publicações recuperadas tratam justamente desse risco vascular — reforçando a contraindicação, não suportando um papel terapêutico para gestodene na enxaqueca. A alta pontuação TxGNN provavelmente reflete conexões não-específicas no grafo (hormônios ↔ vascular ↔ enxaqueca) e não um mecanismo terapêutico real.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8984464](https://pubmed.ncbi.nlm.nih.gov/8984464/) | 1996 | Observational | The Practitioner | Avaliação do risco de trombose venosa profunda (TVP) com uso de contraceptivos orais; foco em risco, não em tratamento de enxaqueca |
| [10342951](https://pubmed.ncbi.nlm.nih.gov/10342951/) | 1998 | Review | Prescrire International | Revisão do risco cardiovascular de COC; alerta para risco coronariano aumentado em mulheres >35 anos, fumantes e hipertensas; risco absoluto baixo em jovens sem fatores de risco |
| [9093141](https://pubmed.ncbi.nlm.nih.gov/9093141/) | 1997 | Case-control | Acta Obstet Gynecol Scand | Estudo sobre prescrição preferencial de COC segundo fatores de risco trombótico; não relacionado ao tratamento de enxaqueca |

---

## Informações de Comercialização no Brasil

O sistema registra **2 licenças ativas** para o gestodene no Brasil (status: comercializado), porém os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no presente Evidence Pack. Recomenda-se consulta direta ao banco de dados da ANVISA para obter as informações completas dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para enxaqueca provavelmente é um artefato de grafo — o gestodene está conectado a nós de "doença vascular" e "hormônio", que por sua vez conectam-se à enxaqueca, gerando uma pontuação inflacionada sem sustentação clínica real. Ao contrário: enxaqueca com aura constitui **contraindicação** para COC contendo gestodene, e toda a literatura disponível reforça esse alerta de risco, não um potencial terapêutico.

**Para considerar qualquer avanço nesta direção, seria necessário:**
- Hipótese mecanística clara para uso de progestagênio **puro** (sem estrogênio) na enxaqueca menstrual
- Dados pré-clínicos demonstrando efeito protetor do gestodene isolado em modelos de enxaqueca
- Distinção entre populações (enxaqueca sem aura vs. com aura) para avaliar segurança mínima
- Dados completos de MOA (DrugBank) e dados de segurança (bula ANVISA)

> ⚠️ **Nota clínica importante:** Das 10 indicações previstas pelo TxGNN para gestodene, a indicação com maior suporte mecanístico e evidências reais é **acne vulgaris** (rank 4, L3 — Research Question): o perfil de baixa androgenicidade do gestodene e o aumento de SHBG com consequente redução de testosterona livre são mecanismos bem documentados. Embora as evidências disponíveis sejam de estudos com COC combinado (não gestodene isolado), esta linha investigativa merece atenção prioritária em relação às demais previsões.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

