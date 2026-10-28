---
layout: default
title: Bupivacaine
parent: Apenas Predição do Modelo (L5)
nav_order: 162
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Bupivacaine: nova indicação prevista, Acrodermatite crônica atrófica (Acrodermatitis chronica atrophicans) (nível de evidência L5). Indicação original: Anestésicos locais"
monitor_inn: "BUPIVACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Bupivacaína: De anestésico local para acrodermatite crônica atrófica
{: .text-alpha }

## Resumo em Uma Frase

Bupivacaína é um anestésico local, originalmente usado em anestesia (classe "Anestésicos Locais" na ANVISA).
O modelo TxGNN prevê que pode ser eficaz para **Acrodermatite Crônica Atrófica (Acrodermatitis chronica atrophicans)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos locais |
| Nova Indicação Prevista | Acrodermatite crônica atrófica (Acrodermatitis chronica atrophicans) |
| Pontuação de Previsão TxGNN | 0,9923 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 12 de 12) |
| Número de Registros | 12 (ativos: 12) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a bupivacaína é um anestésico local que bloqueia canais de sódio, e sua eficácia como anestésico está estabelecida.

A acrodermatite crônica atrófica é uma manifestação cutânea tardia da infecção por *Borrelia*, tratada com antibióticos. A bupivacaína não tem ação antimicrobiana nem modificadora da doença. No máximo, poderia ter papel sintomático na dor neuropática, o que é especulativo e sem suporte nos dados disponíveis.

A pontuação alta (0,9923) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica nem um vínculo farmacológico verificado. Sem dados de mecanismo, não é possível validar uma ponte mecanística plausível.

**Outras previsões do modelo (todas sem ensaios ou literatura, nível L5, Hold):**

| Posição | Indicação prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Dermatomiosite neonatal | 0,9915 | Bloqueio de canais de sódio não atua na vasculopatia imunomediada; miotoxicidade em altas concentrações locais é preocupação em população miopática, sobretudo neonatos |
| 3 | Doença pulmonar intersticial secundária da infância associada a doença do tecido conjuntivo | 0,9911 | Doença guiada por desregulação imune e fibrose; risco de cardiotoxicidade sistêmica em crianças |
| 4 | Dermatomiosite amiopática | 0,9903 | Sem mecanismo estabelecido sobre a doença cutânea dirigida por interferon; miotoxicidade a considerar |

## Informações de Comercialização no Brasil

Todos os 12 registros estão válidos (12 de 12). A indicação aprovada em todos é "Anestésicos locais". Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 104970185 | BUPSTESIC | — | Anestésicos locais |
| Registro 103870087 | HYPOBUP H | — | Anestésicos locais |
| Registro 103870053 | Cloridrato de Bupivacaína | — | Anestésicos locais |
| Registro 102980053 | NEOCAINA | — | Anestésicos locais |
| Registro 104971448 | BUPICAN | — | Anestésicos locais |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento (não extraídas de bula)**: o grafo de conhecimento do TxGNN associa a bupivacaína a diversas condições de risco, entre elas: hipertensão, insuficiência hepática, doença renal, epilepsia, DPOC, insuficiência respiratória, doenças cardíacas (infarto do miocárdio, doença arterial coronariana, fibrilação atrial, doença de condução cardíaca, parada cardíaca súbita), diabetes e cetoacidose diabética, hipotireoidismo, hemoglobinopatias, glaucoma de ângulo fechado, hiperplasia prostática benigna e doença inflamatória intestinal. Esses itens devem ser confirmados na bula.
- **Interações Medicamentosas**: foram identificadas 56 interações. Entre as listadas, de gravidade **moderada**: aprepitanto e morfina (lipossomal). Outras, com gravidade não classificada: pantoprazol, omeprazol, lansoprazol, vancomicina, atropina, triancinolona, prednisona, sinvastatina, hidrocortisona, cloreto de potássio, prednisolona, ranitidina, ondansetrona, metronidazol, famotidina, naloxona, metoclopramida e dexametasona.
- **Risco específico às indicações previstas**: possível miotoxicidade em altas concentrações locais e cardiotoxicidade sistêmica, especialmente relevantes em populações pediátricas e miopáticas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para nenhuma das indicações previstas (nível L5). A pontuação do TxGNN é apenas uma previsão do modelo de deep learning, sem mecanismo plausível, e há preocupações de segurança em populações específicas. O medicamento está comercializado no Brasil, com 12 registros válidos de 12.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem ela
- Obter dados de mecanismo de ação (por exemplo, via DrugBank) para avaliar qualquer vínculo mecanístico
- Realizar estudos pré-clínicos ou revisão da literatura que sustentem alguma das indicações previstas
- Avaliar a compatibilidade de vias de administração e a situação regulatória, dado que o medicamento está comercializado, com 12 registros válidos de 12
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

