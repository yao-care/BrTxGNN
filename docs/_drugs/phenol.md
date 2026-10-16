---
layout: default
title: Phenol
parent: Apenas Predição do Modelo (L5)
nav_order: 521
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Phenol: nova indicação prevista, Acrodermatite crônica atrófica (acrodermatitis chronica atrophicans) (nível de evidência L5). Indicação original: Diluentes e veículos de medicamentos"
---

# Phenol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

# Fenol: De diluente e anestésico local a acrodermatite crônica atrófica

## Resumo em Uma Frase

O fenol foi registrado no Brasil para usos como diluente e veículo de medicamentos, removedor de secreção do conduto auditivo externo e anestésico local.
O modelo TxGNN prevê que pode ser eficaz para **acrodermatite crônica atrófica (acrodermatitis chronica atrophicans)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão baseada em grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diluentes e veículos de medicamentos |
| Nova Indicação Prevista | Acrodermatite crônica atrófica (acrodermatitis chronica atrophicans) |
| Pontuação de Previsão TxGNN | 99,95% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 3 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o fenol é um agente antisséptico e desnaturante de proteínas, usado de forma tópica ou local. Sua eficácia como anestésico local e antisséptico é conhecida, mas não há relação mecanística estabelecida com a nova indicação.

A acrodermatite crônica atrófica é uma infecção cutânea tardia causada por *Borrelia*, tratada com antibióticos. Não há vínculo farmacológico plausível entre o fenol e essa doença, e é improvável que ele tenha efeito terapêutico. A pontuação alta do TxGNN reflete uma previsão baseada na estrutura do grafo, sem respaldo clínico ou de literatura.

Outras previsões do modelo (dermatomiosite neonatal e amiopática, doença pulmonar intersticial pediátrica associada a doença do tecido conjuntivo, hidroa vacciniforme familiar, retinopatia diabética não proliferativa grave e olho seco) também não têm ensaios clínicos nem fundamento mecanístico. A única exceção parcial é a **queloide acneiforme (acne keloid)**, com evidência indireta de peeling químico com fenol em cicatrizes de acne (PMID 17204096, nível L4). Ela foi mencionada apenas como alternativa a ser investigada, pois não é a indicação principal desta avaliação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação principal (acrodermatite crônica atrófica).

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 128600008 (cancelado) | Syrex – Diluente fisiológico injetável de medicamentos | Não informada | Diluentes e veículos de medicamentos |
| Registro nº 105040001 (cancelado) | Auris-Sedina | Não informada | Removedores de secreção do conduto auditivo externo |
| Registro nº 105700050 (cancelado) | Dordente | Não informada | Anestésicos locais |

---

## Considerações de Segurança

- **Contraindicações previstas no grafo de conhecimento** (não provêm de bula): o grafo associa o fenol a contraindicações em doenças como epilepsia, doença hepática, diabetes mellitus, cetoacidose diabética, neutropenia, agranulocitose, parada cardíaca súbita, doenças da condução cardíaca e bloqueio atrioventricular, insuficiência respiratória, doença vascular periférica, dermatite, úlcera péptica ativa, infecções virais (herpes simplex, herpes zoster, citomegalovírus, papilomavírus), câncer e linfomas, entre outras.
- **Preocupações específicas das indicações previstas**: o fenol tem toxicidade sistêmica conhecida, com risco particular em neonatos. É corrosivo e tóxico para os olhos, o que preocupa nas previsões de olho seco e retinopatia diabética. Em tecidos propensos a queloides, peelings profundos podem agravar cicatrizes ou causar alterações de pigmentação.
- Não foram encontradas interações medicamentosas nos dados compilados.

Consulte a bula para advertências e contraindicações oficiais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é apenas computacional (L5), sem ensaios clínicos nem publicações, sem plausibilidade mecanística e com preocupações relevantes de segurança. Todos os registros brasileiros do fármaco estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar as advertências e contraindicações da bula na ANVISA (lacuna bloqueante para a triagem de segurança).
- Complementar os dados de mecanismo de ação (consulta ao DrugBank).
- Demonstrar uma justificativa biológica para a nova indicação; caso contrário, redirecionar a investigação para a hipótese melhor sustentada (cicatrizes de acne/queloide acneiforme), com revisão da literatura e avaliação de segurança.
- Avaliar a compatibilidade de via de administração, hoje pendente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

