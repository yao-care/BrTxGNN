---
layout: default
title: Benzbromarone
parent: Apenas Predição do Modelo (L5)
nav_order: 119
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Benzbromarone: nova indicação prevista, Hipouricemia Renal (Hypouricemia, renal) (nível de evidência L5). Indicação original: Antigotoso"
monitor_inn: "benzbromarone"
predicted_indications: ["hypouricemia, renal"]
---

# Benzbromarone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

# Benzbromarona: De antigotoso para hipouricemia renal

## Resumo em Uma Frase

Benzbromarona é um uricosúrico, originalmente registrado no Brasil como antigotoso.
O modelo TxGNN prevê que pode ser eficaz para **Hipouricemia Renal (Hypouricemia, renal)**, mas não há **nenhum ensaio clínico** e a literatura reúne **18 publicações**, que em sua maioria usam a benzbromarona apenas como ferramenta diagnóstica, e não como tratamento. A análise mecanística indica que a previsão provavelmente é um falso positivo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antigotoso |
| Nova Indicação Prevista | Hipouricemia Renal (Hypouricemia, renal) |
| Pontuação de Previsão TxGNN | 99,07% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base de dados compilada. Segundo informações conhecidas, a benzbromarona é um agente uricosúrico que inibe o URAT1 (SLC22A12), transportador responsável pela reabsorção renal de urato, reduzindo assim o ácido úrico sérico. Sua eficácia como antigotoso é a base de sua indicação original.

A hipouricemia renal, por sua vez, é causada por variantes de perda de função no URAT1 (SLC22A12) ou no GLUT9 (SLC2A9), que resultam em excreção urinária excessiva de urato e baixa concentração sérica. O mecanismo da benzbromarona **agravaria**, e não trataria, a doença, pois mimetiza farmacologicamente o defeito de base.

A pontuação alta do TxGNN (0,99) provavelmente reflete uma associação compartilhada de gene/via (transporte de urato), e não uma relação terapêutica. Na direção terapêutica, a previsão parece ser um falso positivo. Há ainda preocupações clínicas: a hipouricemia renal implica risco de lesão renal aguda induzida por exercício e de nefrolitíase, ambos agravados por maior excreção urinária de urato.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Nenhum dos estudos abaixo avalia a benzbromarona como tratamento da hipouricemia renal. Na maioria, ela é usada como teste farmacológico para caracterizar o defeito de transporte de urato. Listam-se as 10 publicações mais relevantes (priorizando revisões e coortes).

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisão | Clin Rheumatol | Atualização sobre hipouricemia (urato sérico < 2 mg/dL) e suas causas, voltada ao reumatologista |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Revisão | Nihon Rinsho | Conceito e classificação das anormalidades do metabolismo do urato |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Coorte | J Am Soc Nephrol | Análise do gene SLC22A12 em 32 pacientes com hipouricemia renal idiopática; mutações do URAT1 causam a doença |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Relato de caso | Am J Kidney Dis | Dois irmãos com hipouricemia renal hereditária e insuficiência renal aguda induzida por exercício |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Série de casos | Clin Nephrol | Hipouricemia renal com insuficiência renal aguda por exercício e disfunção renal crônica |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Série de casos | J Pediatr | Quatro crianças com hipouricemia renal hereditária; benzbromarona e pirazinamida não alteraram a razão de depuração |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Relato de caso | Acta Paediatr | Insuficiência renal aguda recorrente após exercício; teste benzbromarona/pirazinamida indicou defeito de reabsorção pré-secretória |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Relato de caso | Nephron | Defeito renal isolado de transporte de urato; a depuração de urato aumentou ainda mais com benzbromarona |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Relato de caso | Nephron | Hipouricemia com urolitíase; benzbromarona aumentou a depuração de urato |
| [11676906](https://pubmed.ncbi.nlm.nih.gov/11676906/) | 2001 | Relato de caso | An Esp Pediatr | Lactente com hipouricemia renal e cálculos vesicais de ácido úrico; resposta positiva à benzbromarona (defeito pré-secretório) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100380103 (cancelado) | ZILARICINA | Não informada | Antigotoso |

## Considerações de Segurança

- **Hepatotoxicidade**: a benzbromarona tem risco conhecido de toxicidade hepática.
- **Risco específico na nova indicação**: a hipouricemia renal já se associa a lesão renal aguda induzida por exercício e a nefrolitíase; aumentar a excreção urinária de urato tende a agravar ambos.

Para as demais informações de segurança (advertências, contraindicações), consulte a bula. Não foram encontradas interações medicamentosas nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem estudos de eficácia, e o nível de evidência é L5. O mecanismo (inibição do URAT1) vai contra o objetivo terapêutico, pois reproduziria o defeito da doença, e o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Confirmar se a previsão é um artefato de associação gene/via, e não de benefício terapêutico, antes de qualquer investimento adicional.
- Obter os dados de mecanismo de ação via DrugBank.
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada sem esses dados.
- Reavaliar a relevância da literatura, hoje classificada como "pendente", distinguindo uso diagnóstico de uso terapêutico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

