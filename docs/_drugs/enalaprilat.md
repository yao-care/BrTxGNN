---
layout: default
title: Enalaprilat
parent: Apenas Predição do Modelo (L5)
nav_order: 288
evidence_level: L5
indication_count: 1
---

# Enalaprilat
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

# Enalaprilato: De anti-hipertensivo para glaucoma hereditário primário

## Resumo em Uma Frase

Enalaprilato é um inibidor da enzima conversora de angiotensina (ECA), originalmente registrado no Brasil como anti-hipertensivo (marca RENITEC).
O modelo TxGNN prevê que pode ser eficaz para **Glaucoma Hereditário Primário (Primary Hereditary Glaucoma)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-hipertensivos |
| Nova Indicação Prevista | Glaucoma Hereditário Primário (Primary Hereditary Glaucoma) |
| Pontuação de Previsão TxGNN | 99,09% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, o enalaprilato é um inibidor da ECA (a enzima conversora de angiotensina, alvo ACE) e é a forma ativa do enalapril, usado para tratar hipertensão. Ao inibir a ECA, reduz a formação de angiotensina II.

Existem componentes do sistema renina-angiotensina em tecidos oculares, e já se propôs que a inibição da ECA possa influenciar a dinâmica do humor aquoso e a pressão intraocular. Esse é o único elo mecanístico plausível entre a indicação original (hipertensão) e a nova (glaucoma).

Esse vínculo, porém, é especulativo. O glaucoma hereditário primário (congênito/do desenvolvimento) costuma decorrer de anomalias genéticas do ângulo da câmara anterior (por exemplo, variantes em *CYP1B1* e *MYOC*), e não de um mecanismo ligado à hipertensão arterial. Além disso, o enalaprilato é uma formulação intravenosa, o que torna duvidosa sua adequação ao uso ocular crônico. A previsão, portanto, deve ser tratada como hipótese a validar, não como achado.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100290031 (cancelado) | RENITEC | Não informada | Anti-hipertensivos |

## Considerações de Segurança

- **Contraindicações (associações no grafo de conhecimento, não texto de bula)**: o grafo de conhecimento do TxGNN (PrimeKG) registra contraindicação com angioedema em suas diversas formas: angioedema, angioedema adquirido, angioedema induzido por bloqueadores do sistema renina-angiotensina-aldosterona, angioedema não histaminérgico, angioedema hereditário e angioedema hereditário com deficiência de C1-inibidor.
- **Interações Medicamentosas**: foi registrada 1 entrada, de natureza farmacológica e não de interação entre fármacos: o alvo ECA (gene *ACE*), que é o próprio mecanismo do enalaprilato. Não há dados suficientes para avaliar a segurança nesta nova indicação.

Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A única sustentação é a alta pontuação do modelo (99,09%), sem nenhum ensaio clínico ou publicação. O mecanismo é especulativo e pouco conectado às causas genéticas do glaucoma hereditário primário. Além disso, o produto está com registro cancelado no Brasil e é de uso intravenoso.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (por exemplo, via DrugBank) e avaliar a relevância do sistema renina-angiotensina ocular no glaucoma hereditário.
- Realizar estudos pré-clínicos e revisão da literatura sobre inibidores da ECA e pressão intraocular.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois esses dados ainda não estão disponíveis.
- Avaliar a viabilidade de via de administração e formulação adequadas ao uso ocular, já que o enalaprilato é intravenoso.
- Considerar o risco de angioedema, contraindicação registrada no grafo de conhecimento.
- Esclarecer a situação regulatória, dado que o único registro no Brasil está cancelado.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

