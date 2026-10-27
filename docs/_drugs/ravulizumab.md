---
layout: default
title: Ravulizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ravulizumab: nova indicação prevista, Neutropenia congênita grave autossômica recessiva por deficiência de… (nível de evidência L5). Indicação original: Outros produtos não enquadrados em classe tera…"
monitor_inn: "ravulizumab"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
---

# Ravulizumab
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

## Ravulizumabe: De produto sem classe terapêutica específica à neutropenia congênita grave por deficiência de G6PC3
{: .text-alpha }

## Resumo em Uma Frase

Ravulizumabe (nome comercial ULTOMIRIS) é um inibidor do complemento C5 de ação prolongada. No registro da ANVISA, porém, consta apenas como "outros produtos não enquadrados em classe terapêutica específica".
O modelo TxGNN prevê que pode ser eficaz para a **neutropenia congênita grave autossômica recessiva por deficiência de G6PC3 (autosomal recessive severe congenital neutropenia due to G6PC3 deficiency)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos não enquadrados em classe terapêutica específica (texto do registro na ANVISA) |
| Nova Indicação Prevista | Neutropenia congênita grave autossômica recessiva por deficiência de G6PC3 |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação na base compilada. Segundo informações conhecidas, o ravulizumabe é um anticorpo monoclonal que inibe o componente C5 do complemento, bloqueando a via terminal do complemento. Como o texto do registro brasileiro não traz uma indicação clínica específica, não é possível estabelecer uma relação direta entre a indicação original e a nova.

Na análise dos dados compilados, **não foi identificada ligação mecanística plausível**. A deficiência de G6PC3 causa apoptose e disfunção de neutrófilos por estresse metabólico (acúmulo de 1,5-anidroglucitol-6-fosfato), um processo que não depende do complemento. A pontuação alta do TxGNN (0,9996) reflete apenas a previsão baseada em grafo, sem respaldo de estudos clínicos ou da literatura.

Outras previsões do modelo seguem o mesmo padrão: ocupam as posições 2 a 10 a ciclicidade hematopoiética (neutropenia cíclica), a hiperoxalúria primária, a neutropenia congênita grave, a neutropenia por deficiência de CXCR2, a imunodeficiência por deficiência de p14, a doença de von Willebrand tipo plaquetário, a neutropenia congênita ligada ao X, o distúrbio primário de liberação plaquetária e a anemia megaloblástica. Todas têm nível de evidência L5, sem ensaios nem publicações, e também com recomendação Hold. A hiperoxalúria primária é a única com um vínculo apenas especulativo (cristais de oxalato de cálcio podem ativar o inflamassoma NLRP3 e, possivelmente, o complemento renal), sem evidência de que o bloqueio de C5 altere a evolução da doença.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116180301 (cancelado) | ULTOMIRIS | Não informada | Outros produtos não enquadrados em classe terapêutica específica |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento)**: o grafo de conhecimento TxGNN (PrimeKG) registra contraindicação com **infecção meningocócica**. Esta informação vem do grafo, não do texto da bula. É coerente com o risco conhecido de infecções por *Neisseria meningitidis* associado ao bloqueio do complemento terminal.
- **Interações medicamentosas**: foram identificadas 4 interações, todas de gravidade **menor** (fonte: DDInter), com imunoglobulina G humana nas vias intravenosa, subcutânea, intramuscular e intravenosa/subcutânea.
- Na população imunocomprometida (por exemplo, deficiência de p14), a inibição do complemento aumentaria ainda mais o risco de infecção.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem nível de evidência L5: não há ensaios clínicos nem literatura, e a análise não encontrou ligação mecanística plausível entre a inibição de C5 e a neutropenia por deficiência de G6PC3.
- O único registro brasileiro está cancelado, e há sinal de contraindicação com infecção meningocócica.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada sem esses dados.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Realizar revisão sistemática da literatura e estudos pré-clínicos que testem o papel do complemento C5 na deficiência de G6PC3.
- Reavaliar a viabilidade regulatória e comercial, dada a situação do registro (cancelado) e a compatibilidade de vias de administração (ainda pendente).
- Caso haja interesse em priorizar outras candidatas da lista, tratar a hiperoxalúria primária como a única hipótese secundária especulativa, ainda dependente de evidência pré-clínica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

