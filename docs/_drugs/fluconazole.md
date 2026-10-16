---
layout: default
title: Fluconazole
parent: Apenas Predição do Modelo (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluconazole: nova indicação prevista, Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconj… (nível de evidência L5). Indicação original: Antimicóticos sistêmicos"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "Plasmodium falciparum malaria", "allergic urticaria", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "pneumocystosis", "blood group incompatibility", "premalignant hematological system disease", "papular urticaria"]
---

# Fluconazole
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

# Fluconazol: De antimicótico sistêmico a ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

Fluconazol é um antifúngico (antimicótico sistêmico) cujos registros no Brasil o descrevem como "antimicóticos sistêmicos".
O modelo TxGNN prevê que pode ser eficaz para **ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimicóticos sistêmicos |
| Nova Indicação Prevista | Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,24% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o fluconazol é um antifúngico triazólico que inibe a enzima fúngica CYP51 (lanosterol 14-α-desmetilase), bloqueando a síntese de ergosterol na membrana do fungo.

A ceratoconjuntivite epitelial punctata é geralmente de origem viral (adenovírus) ou inflamatória. Não há vínculo mecanístico evidente com a ação antifúngica do fluconazol, e a similaridade com a indicação original ainda não foi avaliada. A pontuação alta do TxGNN (99,24%) deve ser interpretada apenas como um sinal computacional, sem respaldo clínico.

### Outras indicações previstas (contexto)

O modelo também previu outras indicações, todas com evidência limitada:

| Posição | Indicação | Pontuação | Nível | Observação |
|------|------|------|------|------|
| 2 | Malária por *Plasmodium falciparum* | 98,62% | L4 | Apenas um estudo *in vitro* e uma revisão; atividade antiplasmódica de azóis geralmente fraca |
| 7 | Pneumocistose | 97,82% | L4 | *Pneumocystis* não possui ergosterol, então azóis em geral não são eficazes; o único ensaio listado (NCT04368559) testa rezafungina, não fluconazol |
| 8 | Incompatibilidade de grupo sanguíneo | 97,75% | L5 | Literatura reflete apenas contexto de transplante e interação com tacrolimo |
| Demais (urticária alérgica, hiperamilasemia, síndrome de hiperviscosidade policlonal, analbuminemia congênita, doença hematológica pré-maligna, urticária papular) | | 97,3% a 98,3% | L5 | Sem evidências e sem mecanismo plausível |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para ceratoconjuntivite epitelial punctata.

## Informações de Comercialização no Brasil

Todos os 20 registros encontram-se cancelados; não há registro vigente. Principais registros (5 de 20):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102350578 | Fluconazol | Não informada | Antimicóticos sistêmicos |
| Registro nº 109170098 | Fluconazol | Não informada | Antimicóticos sistêmicos |
| Registro nº 103920157 | Fluconid | Não informada | Antimicóticos sistêmicos |
| Registro nº 154230014 | Flucanil | Não informada | Antimicóticos sistêmicos |
| Registro nº 125680382 | Fuebllo | Não informada | Antimicótico |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: síndrome do QT longo (incluindo a forma familiar), doença renal, piureter, doença hepática e doença da vesícula biliar.
- **Interações Medicamentosas**: foram identificadas 100 interações no total (amostra analisada com 20). Destaque para:
  - **Maior gravidade**: clorpropamida.
  - **Moderadas**: famotidina, rabeprazol, omeprazol, dexlansoprazol, hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, loperamida, aprepitanto, bisacodil, ácido picossulfúrico, polietilenoglicol com eletrólitos, saxagliptina.
  - **Menores**: anfotericina B (incluindo complexo lipídico) e claritromicina.

Consulte a bula para advertências e contraindicações formais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para ceratoconjuntivite epitelial punctata é puramente computacional (L5), sem ensaios ou literatura, e sem mecanismo plausível, já que a doença é tipicamente viral ou inflamatória. Além disso, não há registro vigente do fármaco no Brasil.

**Para prosseguir, é necessário:**
- Obter os dados do mecanismo de ação (por exemplo, via DrugBank) e avaliar a relação mecanística com a doença.
- Baixar e analisar a bula na ANVISA para advertências e contraindicações, etapa que bloqueia a triagem de segurança.
- Realizar busca sistemática de literatura e ensaios sobre fluconazol em ceratoconjuntivite epitelial punctata.
- Esclarecer a situação regulatória (todos os registros cancelados) e a compatibilidade de via de administração (oftálmica vs. sistêmica).
- Se houver interesse em alternativas, a malária por *P. falciparum* (L4) poderia ser priorizada para estudos pré-clínicos, mas com baixa expectativa de eficácia.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

