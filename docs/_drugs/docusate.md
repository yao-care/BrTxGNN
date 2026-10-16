---
layout: default
title: Docusate
parent: Apenas Predição do Modelo (L5)
nav_order: 274
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Docusate: nova indicação prevista, Síndrome de Plummer-Vinson (Plummer-Vinson syndrome) (nível de evidência L5). Indicação original: Laxantes irritantes ou estimulantes"
---

# Docusate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

# Docusato: Do laxante estimulante à síndrome de Plummer-Vinson

## Resumo em Uma Frase

Docusato (docusate) é um surfactante aniônico, registrado no Brasil na categoria de laxantes irritantes ou estimulantes.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Plummer-Vinson (Plummer-Vinson syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Laxantes irritantes ou estimulantes |
| Nova Indicação Prevista | Síndrome de Plummer-Vinson (Plummer-Vinson syndrome) |
| Pontuação de Previsão TxGNN | 99,18% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o docusato é um surfactante aniônico usado como emoliente fecal, pouco absorvido e de ação local na luz intestinal. Sua eficácia como laxante é a única indicação registrada no Brasil.

A síndrome de Plummer-Vinson é caracterizada por anemia ferropriva, disfagia e membranas esofágicas. Não foi identificado vínculo mecanístico crível com o docusato: um surfactante poderia, em teoria, alterar a permeabilidade da mucosa, mas isso não trataria a deficiência de ferro nem as membranas esofágicas, e poderia até prejudicar a absorção de nutrientes.

A pontuação alta do TxGNN (99,18%) reflete uma previsão baseada em grafo de conhecimento, sem respaldo clínico ou da literatura. Deve ser interpretada com cautela, possivelmente como artefato da topologia da rede.

Uma segunda previsão do modelo, **anemia megaloblástica constitucional independente de vitamina B12 e folato** (pontuação de 99,15%), também não tem ensaios, literatura nem vínculo mecanístico plausível: o docusato não tem efeito conhecido sobre a eritropoese nem sobre o metabolismo de nucleotídeos.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 178170103 (cancelado) | HUMECTOL D | Não informada | Laxantes irritantes ou estimulantes |

## Considerações de Segurança

- **Contraindicações (inferidas do grafo de conhecimento, não da bula):** doença ulcerosa péptica, deficiência de potássio, anemia falciforme, persistência hereditária de hemoglobina fetal, hiperoxalúria primária, hemocromatose hereditária, hemossiderose, doenças do metabolismo do ferro, doença de Wilson, retocolite ulcerativa, doença inflamatória intestinal, anemia hemolítica, apendicite, gastrite atrófica crônica, neuropatia óptica hereditária de Leber e gastroenterite. Observe que várias dessas condições (distúrbios do metabolismo do ferro e anemias) são pertinentes às indicações previstas.
- **Interações Medicamentosas** (4 identificadas):
  - Lactulose: moderada
  - Óleo mineral: moderada
  - Fenolftaleína: moderada
  - Linaclotida: leve

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se apoia apenas no modelo (L5), sem ensaios clínicos nem literatura, sem vínculo mecanístico plausível, e o único registro no Brasil está cancelado. Além disso, o grafo de conhecimento aponta contraindicações relacionadas ao metabolismo do ferro e a anemias, o que enfraquece ainda mais a hipótese.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações oficiais), etapa bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Levantar evidências pré-clínicas ou clínicas que sustentem um vínculo biológico com a nova indicação
- Avaliar a viabilidade regulatória e comercial, dado que não há registro vigente no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

