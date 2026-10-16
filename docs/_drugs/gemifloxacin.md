---
layout: default
title: Gemifloxacin
parent: Apenas Predição do Modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gemifloxacin: nova indicação prevista, Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity sy… (nível de evidência L5). Indicação original: Antibióticos sistêmicos simples"
---

# Gemifloxacin
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

# Gemifloxacino: De antibiótico sistêmico para síndrome de hiperviscosidade policlonal

## Resumo em Uma Frase

Gemifloxacino (FACTIVE) é um antibiótico fluoroquinolônico, registrado na ANVISA na categoria "antibióticos sistêmicos simples".
O modelo TxGNN prevê que pode ser eficaz para **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão é puramente baseada em grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples |
| Nova Indicação Prevista | Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o gemifloxacino pertence à classe das fluoroquinolonas, que inibem a DNA girase e a topoisomerase IV bacterianas, e sua utilidade como antibacteriano é reconhecida.

Na prática, **a previsão principal não parece razoável do ponto de vista biológico**. A hiperviscosidade policlonal decorre do aumento de imunoglobulinas ou proteínas séricas, algo que um antibacteriano não deveria corrigir. A pontuação elevada (99,89%) reflete apenas conectividade no grafo de conhecimento, sem ensaios ou literatura que a sustentem. Outras previsões do topo da lista (hiperamilasemia, analbuminemia congênita, gamopatia monoclonal, entre outras) também carecem de base mecanística.

Entre as previsões analisadas, as mais plausíveis são infecções, por extrapolação de classe:
- **Peste septicêmica** (pontuação 99,67%, nível L4): fluoroquinolonas como ciprofloxacino, levofloxacino e moxifloxacino são opções reconhecidas contra *Yersinia pestis*. Seria necessário teste de suscetibilidade in vitro e dados em modelos animais.
- **Endomiometrite** (pontuação 99,30%, nível L4): infecção pélvica polimicrobiana; o gemifloxacino tem cobertura limitada de anaeróbios e já existem esquemas consolidados (como clindamicina + gentamicina).

## Considerações de Segurança

- **Contraindicações e condições de risco (grafo de conhecimento, não texto de bula)**: síndrome do QT longo (inclusive familiar), torsades de pointes, epilepsia, transtornos de ansiedade e neuróticos, distimia, deficiência de potássio, tendinite, periartrite, exostose, doenças do sistema nervoso periférico e neuropatia periférica, colite por *Clostridium difficile*, enterocolite necrosante perinatal, insuficiência renal, miastenia gravis e doenças da junção neuromuscular.
- **Interações medicamentosas**: foram identificadas 273 interações. Entre as de gravidade **maior** estão hidrocortisona, betametasona, clorpropamida e dolasetrona. Entre as moderadas estão antidiabéticos (acarbose, metformina, pioglitazona, canagliflozina, dapagliflozina, empagliflozina, alogliptina, albiglutida, dulaglutida), famotidina, ácido acetilsalicílico, bisacodil, acetato de cálcio, claritromicina e loperamida. A cimetidina tem interação menor.
- A neuropatia periférica é efeito adverso conhecido das fluoroquinolonas, o que argumenta contra o uso em condições com neuropatia associada (como a hematológica adquirida prevista no ranking).

Consulte a bula para as advertências e contraindicações oficiais.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105730363 (cancelado) | FACTIVE | Não informada | Antibióticos sistêmicos simples |

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a indicação prevista, e não existe vínculo mecanístico plausível entre um antibacteriano e a hiperviscosidade policlonal. Além disso, o único registro no Brasil está cancelado, o que limita a viabilidade prática.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada sem esses dados
- Obter dados do mecanismo de ação no DrugBank
- Se houver interesse, priorizar hipóteses anti-infecciosas (peste septicêmica, endomiometrite) com testes de suscetibilidade in vitro e modelos animais
- Avaliar a viabilidade regulatória e comercial, dado o cancelamento do registro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

