---
layout: default
title: Fluorometholone
parent: Apenas Predição do Modelo (L5)
nav_order: 323
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Fluorometholone: nova indicação prevista, Vasculite pós-infecciosa (postinfectious vasculitis) (nível de evidência L5). Indicação original: Glicocorticoides tópico oftalmológico simples"
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
---

# Fluorometholone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Fluorometolona: De glicocorticoide oftálmico tópico para vasculite pós-infecciosa
{: .text-alpha }

## Resumo em Uma Frase

A fluorometolona é um glicocorticoide tópico oftálmico simples, originalmente usado para tratar inflamações oculares.
O modelo TxGNN prevê que pode ser eficaz para **vasculite pós-infecciosa (postinfectious vasculitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica. Trata-se apenas de uma previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glicocorticoides tópico oftalmológico simples |
| Nova Indicação Prevista | Vasculite pós-infecciosa (postinfectious vasculitis) |
| Pontuação de Previsão TxGNN | 0,9991 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 7) |
| Número de Registros | 7 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, a fluorometolona é um corticosteroide sintético que atua sobre o receptor de glicocorticoides (NR3C1), com atividade anti-inflamatória e imunossupressora. Seu uso clínico estabelecido é o tratamento de conjuntivite inflamatória.

Corticosteroides são plausíveis em vasculites imunomediadas em geral. Porém, a fluorometolona é de uso tópico oftálmico, com exposição sistêmica mínima, o que torna **fraco** o vínculo com uma vasculite sistêmica. A pontuação alta do modelo (0,9991) não é acompanhada de nenhum ensaio ou publicação.

### Outras previsões do modelo

Outras indicações previstas também têm pontuação semelhante (de 0,9982 a 0,9990). Duas merecem destaque pela plausibilidade anatômica e farmacológica:

| Indicação prevista | Pontuação TxGNN | Nível | Comentário |
|------|------|------|------|
| Ceratoconjuntivite epitelial punctata | 0,9989 | L4 | Maior afinidade com o uso aprovado (inflamação da superfície ocular). Duas publicações indiretas, nenhuma avaliando a fluorometolona. Cautela em infecções, pois corticosteroides podem agravá-las. |
| Glaucomatociclite (crise glaucomatociclítica) | 0,9982 | L5 | Uveíte anterior recorrente; a fluorometolona tem menor tendência a elevar a pressão intraocular, vantagem teórica. Sem evidências diretas. |
| Iridociclite induzida pelo cristalino | 0,9982 | L5 | Uveíte anterior; a fluorometolona é um agente mais fraco para inflamação intraocular, e o manejo definitivo costuma ser cirúrgico. |

As demais previsões (pós-bacteriano, otite externa, estenose uretral infecciosa, síndrome pós-infecciosa, síndrome hemolítico-urêmica associada a infecção e cardiomiopatia chagásica) carecem de evidências e de vínculo mecanístico convincente. Na cardiomiopatia chagásica, a imunossupressão pode inclusive ser prejudicial.

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102980483 | FLUTINOL | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 100230269 | FLORATE | ALCON LABORATÓRIOS DO BRASIL LTDA. | Cancelado |
| 100681096 | FLORATE | NOVARTIS BIOCIENCIAS S.A | Cancelado |
| 101470013 | FLUMEX | ALLERGAN PRODUTOS FARMACÊUTICOS LTDA | Cancelado |
| 101470167 | FLUMEX-N | ALLERGAN PRODUTOS FARMACÊUTICOS LTDA | Cancelado |
| 115600136 | OFTRATE | CIFARMA CIENTÍFICA FARMACÊUTICA LTDA | Cancelado |
| 117250028 | FLUTINOL | LATINOFARMA INDUSTRIAS FARMACEUTICAS LTDA | Cancelado |

Não há registro válido atualmente, o que limita a viabilidade prática.

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas de bula)**: ceratite por herpes simplex, glaucoma de ângulo aberto, hipertensão ocular, infecções oculares (incluindo fúngicas, virais, tuberculose ocular e conjuntivite infecciosa), diabetes mellitus e cetoacidose diabética, porfiria, deficiência de G6PD, doença de depósito de glicogênio, cistinúria, galactosemia e pigmentação corneana.
- **Interações medicamentosas**: foram identificadas 11 interações medicamentosas sem classificação de gravidade, com doxiciclina, salbutamol, ciclosporina, paracetamol, digoxina, brimonidina, cefalexina, ácido alendrônico, aciclovir, diazepam e fenofibrato. Além disso, o fármaco atua sobre o receptor de glicocorticoides (NR3C1).

Consulte a bula para advertências e contraindicações formais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Para a indicação principal (vasculite pós-infecciosa), há apenas previsão do modelo (L5), sem ensaios nem literatura, com vínculo mecanístico fraco devido à exposição sistêmica mínima da forma oftálmica. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações) para a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Se houver interesse em direção mais plausível, priorizar indicações oculares (ceratoconjuntivite epitelial punctata, uveítes anteriores) e buscar estudos que avaliem diretamente a fluorometolona.
- Avaliar compatibilidade de via de administração e viabilidade comercial, dado o status cancelado.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

