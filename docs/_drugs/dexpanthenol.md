---
layout: default
title: Dexpanthenol
parent: Apenas Predição do Modelo (L5)
nav_order: 263
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Dexpanthenol: nova indicação prevista, Estenose anorretal (anorectal stricture) (nível de evidência L5). Indicação original: Outros produtos com ação na pele e mucosas"
monitor_inn: "dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "exanthem (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Dexpanthenol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Dexpantenol: De produtos para pele e mucosas a anorectal stricture (estenose anorretal)
{: .text-alpha }

## Resumo em Uma Frase

Dexpantenol é um precursor do ácido pantotênico (vitamina B5), originalmente registrado no Brasil como produto com ação na pele e mucosas, vitamínico e de uso oftálmico e nasal.
O modelo TxGNN prevê que pode ser eficaz para **estenose anorretal (anorectal stricture)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; a previsão se baseia somente no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos com ação na pele e mucosas |
| Nova Indicação Prevista | Estenose anorretal (anorectal stricture) |
| Pontuação de Previsão TxGNN | 99,72% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 16 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação original. Segundo informações conhecidas, o dexpantenol é convertido em ácido pantotênico, precursor da coenzima A, e acredita-se que favoreça o reparo epitelial e a cicatrização de feridas. Seus registros no Brasil o associam a produtos para pele e mucosas, o que é coerente com esse papel.

A relação com a estenose anorretal é indireta: a cicatrização da mucosa poderia, em tese, ser relevante para o processo de reparo em estenoses. Não há, porém, ensaio clínico ou publicação que sustente essa hipótese, e ela permanece no nível de previsão do modelo.

Vale notar que outras indicações previstas têm justificativas variadas. Proctite (pontuação de 99,60%) e ceratoconjuntivite epitelial punctata (99,34%) têm vínculo biológico plausível com o reparo de mucosa e epitélio. Já o pólipo anal não tem mecanismo plausível, pois é um processo proliferativo. A principal indicação analisada neste relatório é a de maior pontuação.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para estenose anorretal.

Como informação complementar, para outra indicação prevista (exantema) existe um ensaio, que constitui evidência apenas indireta e não sustenta a indicação principal:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Concluído | 160 | Creme Bepanthen® (dexpantenol) versus creme de cetomacrogol, duplo-cego, na prevenção de erupção papulopustular em pacientes que recebem inibidores do EGFR. Resultados não disponibilizados. |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento)**: o grafo de conhecimento do TxGNN indica contraindicação em **hemofilia**. Trata-se de uma associação do modelo, não de texto de bula.
- **Interações Medicamentosas**: nenhuma interação foi encontrada nos dados compilados.

Consulte a bula para informações adicionais de segurança, pois as advertências e contraindicações da bula brasileira não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para estenose anorretal tem pontuação alta (99,72%), mas é puramente baseada no modelo (L5), sem ensaios ou literatura. Além disso, todos os 16 registros no Brasil estão cancelados e faltam dados de segurança da bula.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação no DrugBank e analisar o vínculo mecanístico com a estenose anorretal
- Baixar e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Realizar busca sistemática na literatura e em registros de ensaios sobre dexpantenol em doenças anorretais
- Esclarecer a relevância da hemofilia como contraindicação no grafo de conhecimento
- Definir a via de administração e a forma farmacêutica, e verificar a situação regulatória, já que não há registro vigente
- Avaliar, como alternativa, indicações com maior plausibilidade biológica (proctite, ceratoconjuntivite epitelial punctata) ou com ensaio indireto (exantema, após confirmar a condição estudada em NCT01136005)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

