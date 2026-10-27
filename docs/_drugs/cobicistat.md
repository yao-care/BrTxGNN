---
layout: default
title: Cobicistat
parent: Apenas Predição do Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Cobicistat: nova indicação prevista, Síndrome da imunodeficiência adquirida felina (feline acquired immuno… (nível de evidência L5). Indicação original: Associações de antivirais para o tratamento de…"
monitor_inn: "cobicistat"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Cobicistat: Da infecção por HIV à síndrome da imunodeficiência adquirida felina
{: .text-alpha }

## Resumo em Uma Frase

Cobicistat é um potencializador farmacocinético (inibidor de CYP3A) usado em associações de antirretrovirais para o tratamento de infecções por HIV.
O modelo TxGNN prevê que pode ser eficaz para a **síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Associações de antivirais para o tratamento de infecções por HIV |
| Nova Indicação Prevista | Síndrome da imunodeficiência adquirida felina (feline acquired immunodeficiency syndrome) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o cobicistat é um inibidor de CYP3A que atua como potencializador farmacocinético, sem atividade antiviral própria. Ele é usado para aumentar a exposição a inibidores de protease do HIV-1 (como darunavir e atazanavir) e ao inibidor de integrase elvitegravir.

O vírus da imunodeficiência felina (FIV) é um lentivírus relacionado ao HIV, e sua protease tem estrutura semelhante. Por isso, é concebível um raciocínio de regime potencializado. Contudo, a pontuação elevada do TxGNN provavelmente reflete a proximidade no grafo com nós relacionados ao HIV, e não evidência independente.

Não foram fornecidos dados veterinários, ensaios clínicos ou literatura. Além disso, o efeito de potencialização dependeria de um antiviral parceiro ativo contra o FIV; isoladamente, o cobicistat não tem efeito antiviral.

**Outras previsões do modelo (todas com nível L5 e recomendação Hold):**
- **Infecção pelo vírus da imunodeficiência símia (SIV)** (pontuação 99,92%): o SIV é o equivalente em primatas não humanos do HIV e é amplamente usado como modelo. A aplicação do cobicistat seria, em princípio, um uso de pesquisa pré-clínica, e não uma indicação terapêutica humana.
- **Transtorno do neurodesenvolvimento com marcha atáxica, ausência de fala e redução da substância branca cortical** (pontuação 99,91%): não foi possível estabelecer vínculo mecanístico plausível. A pontuação parece ser uma previsão sem respaldo biológico.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 112363434 (cancelado) | SYMTUZA® | Não informada | Associações de antivirais para o tratamento de infecções por HIV |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas **420 interações** registradas. Exemplos de gravidade **maior**: loperamida, triamcinolona, cisaprida e budesonida. Exemplos de gravidade **moderada**: hidrocortisona, aprepitanto, betametasona, clotrimazol, dexametasona, metoclopramida, repaglinida e claritromicina. Exemplo de gravidade **menor**: prucaloprida. Há padrão marcante de interação com corticosteroides, compatível com a inibição de CYP3A.

Consulte a bula para informações adicionais de segurança (advertências e contraindicações).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que sustentem nenhuma das indicações previstas (nível L5). O cobicistat não tem atividade antiviral própria, as indicações previstas são veterinárias ou de pesquisa, ou sem vínculo biológico evidente, e o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem esses dados
- Complementar os dados de mecanismo de ação (consulta ao DrugBank)
- Buscar dados veterinários ou pré-clínicos (FIV/SIV) e definir o antiviral parceiro ativo
- Avaliar se há interesse regulatório e de mercado, dado que o registro no Brasil está cancelado
- Descartar ou reavaliar a previsão para o transtorno do neurodesenvolvimento, por ausência de racional mecanístico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

