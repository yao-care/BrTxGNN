---
layout: default
title: Atosiban
parent: Apenas Predição do Modelo (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Atosiban: nova indicação prevista, Glaucoma hereditário primário (primary hereditary glaucoma) (nível de evidência L5). Indicação original: Outros produtos para uso em ginecologia e obstetrícia"
monitor_inn: "atosiban"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
---

# Atosiban
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Atosibana: Da obstetrícia/ginecologia ao glaucoma hereditário primário
{: .text-alpha }

## Resumo em Uma Frase

Atosibana (atosiban) é um antagonista dos receptores de ocitocina e vasopressina, registrado no Brasil na categoria "outros produtos para uso em ginecologia e obstetrícia" (na prática, usado como tocolítico para retardar o parto prematuro).
O modelo TxGNN prevê que pode ser eficaz para **glaucoma hereditário primário (primary hereditary glaucoma)**, mas **não há ensaios clínicos nem publicações** que sustentem esta direção. Trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos para uso em ginecologia e obstetrícia |
| Nova Indicação Prevista | Glaucoma hereditário primário (primary hereditary glaucoma) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo as informações farmacológicas disponíveis, o atosibana é um peptídeo que atua sobre os receptores de ocitocina (OXTR) e de vasopressina (V1A, V1B e V2). Na prática clínica, é usado como tocolítico em mulheres grávidas entre 24 e 33 semanas com sinais de trabalho de parto prematuro (aprovado pela EMA e por outras agências nacionais, mas não pelo FDA).

**Não há vínculo mecanístico sustentado pelos dados** entre essa atividade e o glaucoma hereditário primário. A pontuação alta (99,92%) é apenas uma saída do modelo. Uma hipótese especulativa seria a sinalização de ocitocina/vasopressina no tecido ocular (dinâmica do humor aquoso e pressão intraocular), mas ela não tem respaldo nos dados disponíveis. A similaridade entre a indicação original e a nova indicação não foi avaliada.

**Outras indicações previstas** (todas com nível L5 e recomendação Hold, exceto onde indicado):

| Posição | Doença prevista | Pontuação TxGNN | Observação |
|---------|------|------|------|
| 2 | Glaucoma de ângulo aberto | 99,92% | Apenas previsão |
| 3 | Hipotricose congênita com milia | 99,89% | Sem justificativa mecanística |
| 4 | Alopecia | 99,89% | Sem vínculo estabelecido |
| 5 | Hipotricose simples do couro cabeludo | 99,89% | Sem vínculo evidenciado |
| 6 | Doença vascular | 99,87% | L4, literatura indireta e pré-clínica |
| 7 | Alopecia areata difusa | 99,86% | Apenas previsão |
| 8 | Síndrome do desfiladeiro torácico arterial | 99,86% | Sem evidência |
| 9 | Síndrome do desfiladeiro torácico venoso | 99,86% | Sem evidência |
| 10 | Calcifilaxia visceral | 99,84% | Sem evidência |

A única indicação com alguma literatura é "doença vascular". Os estudos recuperados são em grande parte pré-clínicos e tratam da ocitocina (o agonista que o atosibana antagoniza) na cardioproteção em modelos de coração de rato. A direção do efeito para o atosibana, como antagonista, é incerta e pode ser oposta à observada nesses estudos.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 128760022 | Acetato de Atosibana | Não informada | Outros produtos para uso em ginecologia e obstetrícia |
| Registro nº 128760010 | Tractocile | Não informada | Outros produtos para uso em ginecologia e obstetrícia |
| Registro nº 155370051 | Acetato de Atosibana | Não informada | Outros produtos para uso em ginecologia e obstetrícia |
| Registro nº 155370058 | Attosy | Não informada | Outros produtos para uso em ginecologia e obstetrícia |

Todos os 4 registros estão **cancelados**; não há registro válido atualmente.

---

## Considerações de Segurança

- **Interações medicamentosas / alvos farmacológicos**: a consulta foi concluída e identificou 4 alvos de atividade farmacológica (não são interações com outros medicamentos): receptores V1A (AVPR1A), V1B (AVPR1B), V2 (AVPR2) e de ocitocina (OXTR).
- **Sinal de segurança na literatura**: um estudo de coorte (PMID 30646165) associou a exposição a tocolíticos à hemorragia intraventricular e à morte em recém-nascidos prematuros. É um sinal de segurança, não uma evidência de benefício.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para glaucoma hereditário primário. A previsão tem nível L5 e não há vínculo mecanístico demonstrado.
- Além disso, o produto não tem nenhum registro válido no Brasil (todos os 4 estão cancelados).

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Investigar, em estudos pré-clínicos, se a sinalização de ocitocina/vasopressina participa da pressão intraocular ou da neuropatia glaucomatosa.
- Avaliar a compatibilidade da via de administração: o atosibana é um peptídeo de uso intravenoso, e a indicação ocular exigiria uma via local ou outro desenvolvimento farmacotécnico.
- Esclarecer a situação regulatória (motivo dos cancelamentos e viabilidade de novo registro).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

