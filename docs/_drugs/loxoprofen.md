---
layout: default
title: Loxoprofen
parent: Apenas Predição do Modelo (L5)
nav_order: 428
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Loxoprofen: nova indicação prevista, Síndrome de microftalmia colobomatosa com displasia rizomélica (colob… (nível de evidência L5). Indicação original: Anti-inflamatórios"
monitor_inn: "loxoprofen"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Loxoprofen
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

# Loxoprofeno: De anti-inflamatório para síndrome de microftalmia colobomatosa com displasia rizomélica

## Resumo em Uma Frase

Loxoprofeno é um anti-inflamatório não esteroidal (AINE), registrado na ANVISA com a indicação genérica "anti-inflamatórios".
O modelo TxGNN prevê que pode ser eficaz para a **síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-inflamatórios |
| Nova Indicação Prevista | Síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Pontuação de Previsão TxGNN | 99,80% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 4 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados do mecanismo de ação na base compilada. Segundo informações conhecidas, o loxoprofeno é um pró-fármaco de AINE: seu metabólito ativo (o trans-álcool) inibe as enzimas COX-1 e COX-2, reduzindo a síntese de prostaglandinas, o que explica seu efeito anti-inflamatório e analgésico.

A nova indicação prevista é uma síndrome de desenvolvimento muito rara, sem patologia inflamatória ou mediada por prostaglandinas evidente que a inibição de COX possa plausivelmente tratar. Os dados disponíveis não sustentam nenhuma ligação mecanística entre o fármaco e a doença.

A pontuação alta do TxGNN (99,80%) é apenas uma previsão computacional e pode refletir artefatos do grafo de conhecimento (por exemplo, conectividade com genes ou fenótipos compartilhados), e não uma relação biologicamente validada. Além disso, a exposição a AINEs na gestação traz risco ao desenvolvimento, o que contraria qualquer presunção de benefício em um distúrbio congênito do desenvolvimento.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102351441 | Loxoprofeno Sódico | Não informada | Anti-inflamatórios (cancelado) |
| Registro nº 104540159 | Loxonin | Não informada | Anti-inflamatórios (cancelado) |
| Registro nº 104540188 | Loxonin Flex | Não informada | Anti-inflamatórios (cancelado) |
| Registro nº 105730495 | Oxotron | Não informada | Anti-inflamatórios (cancelado) |

## Considerações de Segurança

Consulte a bula para informações de segurança.

Observação: o risco de exposição a AINEs durante a gestação é relevante para uma doença congênita do desenvolvimento, como a prevista aqui.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem literatura que sustentem a previsão (nível L5), não há ligação mecanística plausível, e todos os registros no Brasil estão cancelados. A pontuação alta do modelo, isoladamente, não é suficiente para avançar.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações)
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Investigar se a pontuação reflete artefatos do grafo de conhecimento e buscar evidências biológicas ou pré-clínicas que justifiquem a hipótese
- Avaliar o risco do uso de AINEs em contexto de desenvolvimento/gestação
- Considerar que não há registro ativo no Brasil, o que exigiria novo processo regulatório

---

**Nota sobre a segunda previsão:** a síndrome de braquidactilia-sindactilia (pontuação 99,75%, nível L5, sem ensaios nem literatura) também não tem racionalidade mecanística, por se tratar de malformação congênita estrutural dos membros; a decisão recomendada é igualmente **Hold**.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

