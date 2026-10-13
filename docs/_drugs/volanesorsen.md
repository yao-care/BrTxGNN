---
layout: default
title: Volanesorsen
parent: Apenas Predição do Modelo (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
---

# Volanesorsen
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

# Volanesorsen: De agente modificador de lipídios para anemia megaloblástica (previsão sem sustentação)

## Resumo em Uma Frase

Volanesorsen (marca WAYLIVRA) é um oligonucleotídeo antisense registrado no Brasil na categoria "outros agentes modificadores de lipídios".
O modelo TxGNN prevê que pode ser eficaz para **anemia megaloblástica (Megaloblastic Anemia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros agentes modificadores de lipídios |
| Nova Indicação Prevista | Anemia megaloblástica (Megaloblastic Anemia) |
| Pontuação de Previsão TxGNN | 99,997% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, volanesorsen é um oligonucleotídeo antisense que inibe o RNA mensageiro da APOC3 (apolipoproteína C-III) e, com isso, reduz os triglicerídeos.

Não é possível identificar um vínculo mecanístico plausível entre essa inibição e a anemia megaloblástica, que é causada por deficiência de vitamina B12 ou de folato. A pontuação alta do TxGNN reflete apenas associações no grafo de conhecimento e não é sustentada por nenhum ensaio ou publicação. Por isso, esta previsão deve ser tratada com cautela.

Outras previsões do modelo (colangite esclerosante, doenças falciformes, meningococcemia e hemoglobinúria paroxística noturna) também apresentam pontuações muito altas, sem evidências e sem mecanismo plausível. Isso sugere artefatos do grafo, e não sinais independentes de eficácia.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 157700003 (cancelado) | WAYLIVRA | Não informada | Outros agentes modificadores de lipídios |

---

## Considerações de Segurança

- **Sinal do grafo de conhecimento**: a base de conhecimento do TxGNN indica uma relação de contraindicação com **trombocitopenia**. Isso não vem do texto da bula. Trombocitopenia é um efeito adverso conhecido do volanesorsen e seria especialmente preocupante em populações hematológicas, como as das indicações previstas.
- **Interações medicamentosas**: nenhuma interação foi encontrada na consulta realizada.

Para as demais informações de segurança (advertências e contraindicações), consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem nível de evidência L5, sem ensaios clínicos nem literatura, e sem vínculo mecanístico plausível com a anemia megaloblástica.
- O único registro no Brasil está cancelado, e há risco de trombocitopenia, o que desfavorece o uso em doenças hematológicas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que é bloqueante para a triagem de segurança.
- Complementar os dados do mecanismo de ação a partir do DrugBank.
- Realizar uma busca ativa de literatura e de ensaios clínicos que justifiquem qualquer vínculo biológico.
- Avaliar a compatibilidade de vias de administração e o risco de trombocitopenia em populações hematológicas.
- Considerar a priorização de outras indicações, pois nenhuma das 10 previsões apresenta evidências no momento.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

