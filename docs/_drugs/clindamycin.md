---
layout: default
title: Clindamycin
parent: Apenas Predição do Modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Clindamycin: nova indicação prevista, Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconj… (nível de evidência L5). Indicação original: Antibióticos sistêmicos simples"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Clindamicina: De antibiótico sistêmico e antiacneico para ceratoconjuntivite epitelial punctata
{: .text-alpha }

## Resumo em Uma Frase

Clindamicina é um antibiótico da classe das lincosamidas, originalmente registrado no Brasil como antibiótico sistêmico e como produto antiacne.
O modelo TxGNN prevê que pode ser eficaz para **ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples |
| Nova Indicação Prevista | Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 0,9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 15) |
| Número de Registros | 15 (ativos: 15) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a clindamicina é um antibiótico lincosamida que inibe a síntese proteica bacteriana ao se ligar à subunidade ribossomal 50S. Sua eficácia como antibacteriano e no tratamento da acne está estabelecida.

A relação com a nova indicação é fraca. A ceratoconjuntivite epitelial punctata costuma ter origem viral ou inflamatória, e a clindamicina só faria sentido se houvesse componente bacteriano. A pontuação do modelo é muito alta, mas não há ensaios nem literatura que a sustentem.

Outras indicações previstas pelo modelo também carecem de respaldo. Para ceratite por exposição, a literatura encontrada trata de ceratite bacteriana e infecção ocular em geral (relatos de caso e coortes retrospectivas), de forma apenas indireta, e o mecanismo se aplicaria somente a infecção secundária. Para "doença animal não humana", a associação é adversa: a clindamicina é fator de risco reconhecido para infecção por *C. difficile*, e a previsão provavelmente é falso-positiva. As demais previsões (ceratopatia neurotrófica, ceratoconjuntivite epidêmica, vaginite atrófica pós-menopausa, ceratoconjuntivite límbica superior, síndrome da neve visual, ceratomalácia e oftalmia nodosa) não têm evidência clínica e não apresentam justificativa biológica plausível.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada à indicação principal prevista (ceratoconjuntivite epitelial punctata).

## Informações de Comercialização no Brasil

Todos os 15 registros encontrados têm licença válida. Os cinco primeiros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102350805 | Cloridrato de clindamicina | Não informada | Antibióticos sistêmicos simples |
| Registro 113430103 | Fosfato de clindamicina | Não informada | Antibióticos sistêmicos simples |
| Registro 103870036 | Hyclin | Não informada | Antibióticos sistêmicos simples |
| Registro 121100385 | Dalacin C | Não informada | Antibióticos sistêmicos simples |
| Registro 110130266 | Deriva C Micro | Não informada | Produtos antiacne |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (PrimeKG, não derivadas de bula)**: insuficiência hepática, queimadura solar, doença de Crohn, doença inflamatória intestinal, colite de Crohn, eczema atópico, dermatite atópica, dermatite esfoliativa, doenças diarreicas, colite por *Clostridium difficile*, enterocolite necrosante perinatal, dermatite, colite ulcerativa e candidíase vulvovaginal.
- **Interações Medicamentosas**: foram identificadas 100 interações no total. As de gravidade moderada incluem balsalazida, claritromicina, ácido picossulfúrico, atapulgita e caulim. Outras, de gravidade não classificada, incluem anfotericina B, ácido acetilsalicílico, amoxicilina, bupropiona, pantoprazol, glimepirida, doxiciclina, clotrimazol, morfina, metformina, omeprazol, sucralfato, rosiglitazona, lansoprazol e vancomicina.

As advertências e contraindicações da bula brasileira não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem pontuação alta no modelo, mas nenhuma evidência clínica ou da literatura (L5), e a justificativa mecanística é fraca, pois a doença é tipicamente viral ou inflamatória. Além disso, o medicamento é comercializado no Brasil, com 15 registros válidos de 15.

**Para prosseguir, é necessário:**
- Confirmar o mecanismo de ação em fonte primária (por exemplo, DrugBank) e analisar a plausibilidade mecanística para a nova indicação
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Buscar evidência clínica direta para a indicação prevista (ensaios e estudos controlados)
- Avaliar a via de administração (por exemplo, formulação oftálmica), ainda não definida
- Esclarecer a situação regulatória, já que não há registro vigente no Brasil
- Considerar, entre as previsões listadas, apenas a ceratite por exposição com infecção bacteriana secundária como hipótese a investigar, ainda assim com evidência indireta
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

