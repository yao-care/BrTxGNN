---
layout: default
title: Avibactam
parent: Apenas Predição do Modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 4
monitor_inn: "Avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-10-28
description: "Avibactam: nova indicação prevista, Tuberculose do ureter (nível de evidência L5). Indicação original: Pielonefrite"
---

# Avibactam
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

## Avibactam: Da pielonefrite à tuberculose do ureter
{: .text-alpha }

## Resumo em Uma Frase

Avibactam é um inibidor de beta-lactamases, usado em combinação com um antibiótico beta-lactâmico; sua indicação original registrada no grafo de conhecimento é a pielonefrite.
O modelo TxGNN prevê que pode ser eficaz para **tuberculose do ureter (ureter tuberculosis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Pielonefrite (relação registrada no grafo de conhecimento; os registros locais não trazem texto de indicação aprovada) |
| Nova Indicação Prevista | Tuberculose do ureter |
| Pontuação de Previsão TxGNN | 0,9911 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 3) |
| Número de Registros | 3 (ativos: 2) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o avibactam é um inibidor de beta-lactamases que não é um beta-lactâmico (cobre enzimas das classes A e C de Ambler e algumas da classe D) e é comercializado em combinação com a ceftazidima. A relação com a pielonefrite vem do modelo TxGNN (deep learning), e não de texto de bula; pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

A pontuação alta (0,9911) provavelmente reflete similaridades que o modelo TxGNN (deep learning) aprendeu entre doenças relacionadas, como infecções do trato urinário, e não evidência biológica. Há, porém, uma justificativa mecanística teórica: o *Mycobacterium tuberculosis* produz uma beta-lactamase de classe A codificada no cromossomo (BlaC), e o avibactam demonstrou, in vitro, inibir essa enzima. Isso é apenas raciocínio de contexto, sem respaldo em estudos incluídos nos dados compilados.

Qualquer uso clínico dependeria de associação com um beta-lactâmico. Como não há ensaios nem literatura sobre esta indicação, o mecanismo não pôde ser verificado com os dados disponíveis.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 121100443 | TORGENA | Não informada | Não informada |
| Registro 121100486 | RYAMBIC | Não informada | Não informada |
| Registro 121100485 (cancelado) | CEFTAZIDIMA PENTAIDRATADA + AVIBACTAM SÓDICO | Não informada | Não informada |

Os três registros pertencem à Pfizer Brasil Ltda. O texto de indicação aprovada não consta nos registros compilados.

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Não foram encontradas interações medicamentosas nos dados compilados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para tuberculose do ureter tem pontuação alta, mas não conta com nenhum ensaio clínico ou publicação, sendo classificada como L5. O racional mecanístico (inibição in vitro da BlaC) é apenas teórico e não foi verificado com os dados disponíveis.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança
- Complementar os dados de mecanismo de ação (MOA) do avibactam
- Levantar estudos pré-clínicos e clínicos sobre avibactam associado a beta-lactâmicos na tuberculose, em especial a urogenital
- Confirmar os textos de indicação aprovada e as formas farmacêuticas dos registros brasileiros
- Avaliar a compatibilidade de via de administração (ainda pendente)

**Observação sobre as demais previsões:** as indicações de ranking inferior (esquistossomose urinária, síndrome de hiperviscosidade policlonal e hiperamilasemia) também são L5 e não têm justificativa mecanística plausível. Provavelmente refletem similaridades que o modelo TxGNN (deep learning) aprendeu entre doenças relacionadas, não evidência biológica, e não são recomendadas para avanço.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

