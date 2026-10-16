---
layout: default
title: Upadacitinib
parent: Apenas Predição do Modelo (L5)
nav_order: 660
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Upadacitinib: nova indicação prevista, Síndrome de microftalmia colobomatosa com displasia rizomélica (colob… (nível de evidência L5). Indicação original: Imunossupressores seletivos"
---

# Upadacitinib
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

# Upadacitinibe: De imunossupressor seletivo para a síndrome de microftalmia colobomatosa com displasia rizomélica

## Resumo em Uma Frase

Upadacitinibe (RINVOQ) está registrado na ANVISA na categoria de imunossupressores seletivos.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressores seletivos |
| Nova Indicação Prevista | Síndrome de microftalmia colobomatosa com displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Pontuação de Previsão TxGNN | 99,61% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o upadacitinibe pertence à classe dos inibidores de JAK (com atividade principalmente sobre a JAK1), que modulam a sinalização inflamatória mediada pela via JAK-STAT. Seu uso está associado à imunossupressão seletiva.

A síndrome prevista é uma malformação congênita rara, que afeta os olhos (microftalmia com coloboma) e o esqueleto (displasia rizomélica). Presumivelmente, ela decorre de alterações genéticas ou do desenvolvimento, e não de inflamação dependente de JAK. Não foi fornecido nenhum vínculo de via, alvo ou gene entre a inibição de JAK1 e essa condição, portanto não há relação biológica plausível evidente com a indicação original.

A pontuação muito alta (0,996) provavelmente reflete um artefato do grafo de conhecimento, como vizinhos compartilhados de genes ou fenótipos. Deve ser tratada apenas como um sinal gerador de hipóteses, e não como evidência clínica.

> Observação: a segunda previsão do modelo, **síndrome de braquidactilia-sindactilia** (pontuação de 99,58%), também não tem ensaios clínicos nem literatura e apresenta a mesma limitação mecanística (malformação congênita do desenvolvimento, sem vínculo com a via JAK-STAT).

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 198600017 (cancelado) | RINVOQ | Não informada | Imunossupressores seletivos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 359 interações no total. As principais, de gravidade **Maior**, são:
  - Corticosteroides: hidrocortisona, triamcinolona (incluindo oftálmica), dexametasona, beclometasona, betametasona, budesonida, prednisona e prednisolona
  - Claritromicina
  - Cobicistate
  - Deferiprona
  - Iobenguano (I-131)
- Interações de gravidade **Moderada**: aprepitanto, cimetidina, miconazol e deferasirox.
- Interações de gravidade **Menor**: sulfato, acetato e gluconato de zinco.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se apoia somente na pontuação do modelo (nível L5), sem ensaios clínicos, sem literatura e sem racional mecanístico plausível. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter os dados do mecanismo de ação (por exemplo, via DrugBank) e avaliar qualquer vínculo biológico entre a inibição de JAK1 e a síndrome prevista
- Baixar e analisar a bula na ANVISA para obter advertências e contraindicações, etapa que bloqueia a triagem de segurança
- Realizar busca sistemática de literatura e de registros de ensaios clínicos, além de estudos pré-clínicos que sustentem a hipótese
- Esclarecer a situação regulatória atual do fármaco no Brasil, já que o registro encontrado está cancelado
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original, hoje pendentes
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

