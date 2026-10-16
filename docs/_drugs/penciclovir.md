---
layout: default
title: Penciclovir
parent: Apenas Predição do Modelo (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Penciclovir: nova indicação prevista, Fasciolíase (Fascioliasis) (nível de evidência L5). Indicação original: Herpes labial"
---

# Penciclovir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Penciclovir: Do herpes labial à fasciolíase (previsão computacional)

## Resumo em Uma Frase

Penciclovir é um antiviral análogo de guanosina, originalmente usado no tratamento do herpes labial.
O modelo TxGNN prevê que pode ser eficaz para **Fasciolíase (Fascioliasis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Herpes labial (conforme as relações de indicação do grafo de conhecimento, pois não há registros no Brasil) |
| Nova Indicação Prevista | Fasciolíase (Fascioliasis) |
| Pontuação de Previsão TxGNN | 99,06% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação registrados para este fármaco. Segundo informações conhecidas, o penciclovir é um análogo de guanosina: após ser fosforilado pela timidina quinase viral, sua forma trifosfato ativa inibe a DNA polimerase dos herpesvírus. Sua eficácia no herpes labial é reconhecida.

Para a fasciolíase, porém, **não se identifica um vínculo mecanístico plausível**. *Fasciola hepatica* é um trematódeo e não possui via de ativação dependente de timidina quinase viral. Os anti-helmínticos estabelecidos (como albendazol e praziquantel) atuam por alvos diferentes.

A pontuação alta (99,06%) reflete apenas uma previsão computacional, sem respaldo clínico ou da literatura. As demais previsões do modelo seguem o mesmo padrão: cisticercose, cenurose, helmintíase intestinal, endomiometrite e diversos subtipos de mesotelioma e tumores pleurais ou sinoviais, todas também com nível L5 e sem evidências. Nos mesoteliomas, o único vínculo teórico passa por terapia gênica suicida (HSV-TK associada a um análogo nucleosídico), que exige entrega de gene e não corresponde ao uso do fármaco isolado.

## Informações de Comercialização no Brasil

O penciclovir não possui registros ativos na ANVISA nos dados compilados para este relatório (0 registros), portanto não está comercializado no Brasil.

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para fasciolíase não tem ensaios clínicos nem literatura, e o mecanismo do fármaco (dependente de timidina quinase viral) não é aplicável a trematódeos. Além disso, o fármaco não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações), lacuna que impede a triagem de segurança
- Obter dados do mecanismo de ação a partir do DrugBank
- Realizar estudos pré-clínicos *in vitro* contra *Fasciola hepatica* para testar se há alguma atividade, já que atualmente não há racional mecanístico
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original
- Considerar outras previsões do modelo somente se surgir evidência de suporte
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

