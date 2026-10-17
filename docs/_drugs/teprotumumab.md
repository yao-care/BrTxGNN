---
layout: default
title: Teprotumumab
parent: Apenas Predição do Modelo (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Teprotumumab: nova indicação prevista, Monossomia do X (Monosomy X) (nível de evidência L5). Indicação original: Imunossupressor"
monitor_inn: "teprotumumab"
predicted_indications: ["monosomy X", "esophageal varices with bleeding", "esophageal varices without bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
---

# Teprotumumab
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

# Teprotumumabe: De imunossupressor para monossomia do X (previsão sem sustentação clínica)

## Resumo em Uma Frase

Teprotumumabe (TEPEZZA) é um anticorpo monoclonal que inibe o receptor do fator de crescimento semelhante à insulina tipo 1 (IGF-1R). No Brasil, o único registro existente o classifica como "imunossupressor".
O modelo TxGNN prevê que pode ser eficaz para **monossomia do X (Monosomy X)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão baseia-se apenas na estrutura do grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressor |
| Nova Indicação Prevista | Monossomia do X (Monosomy X) |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação registrados para este fármaco nos dados compilados. Segundo informações conhecidas, o teprotumumabe é um anticorpo monoclonal inibidor do IGF-1R, e a classificação regulatória brasileira o descreve apenas como imunossupressor.

A monossomia do X (síndrome de Turner) é uma alteração cromossômica que cursa com baixa estatura e disgenesia gonadal. O eixo do IGF-1 tem relação com o crescimento, o que explica a proximidade entre o fármaco e a doença no grafo de conhecimento.

No entanto, a lógica terapêutica é contrária: bloquear o IGF-1R tende a prejudicar o crescimento, e não a favorecê-lo. Não há justificativa terapêutica plausível. A pontuação elevada do TxGNN é uma inferência baseada em grafo, sem respaldo de ensaios ou literatura.

## Outras Indicações Previstas (Todas L5, Hold)

Nenhuma das demais previsões apresenta ensaios clínicos ou literatura.

| Posição | Doença prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Varizes esofágicas com sangramento | 99,64% | Sem vínculo mecanístico claro; hipertensão portal não tem o IGF-1R como alvo estabelecido |
| 3 | Varizes esofágicas sem sangramento | 99,64% | Pontuação idêntica à anterior, sugerindo artefato do grafo |
| 4 | Disgenesia gonadal mista | 99,50% | Provável proximidade com a monossomia do X no grafo |
| 5 | Distúrbio da fosforilação oxidativa mitocondrial por alterações do DNA nuclear | 99,44% | Vínculo apenas especulativo via metabolismo |
| 6 | Síndrome de Turner por anomalias estruturais do X | 99,37% | Mesma ressalva da monossomia do X |
| 7 | Monossomia do X em mosaico | 99,37% | Mesma ressalva da monossomia do X |
| 8 | Distúrbio do desenvolvimento sexual por cromossomos sexuais | 99,34% | Categoria ampla, derivada de vizinhança ontológica |
| 9 | Doença varicosa | 99,33% | Remodelação vascular é hipótese especulativa |
| 10 | Anomalia do número de cromossomos X | 99,32% | Categoria geral sem justificativa mecanística |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102440025 (cancelado) | TEPEZZA | Não informada | Imunossupressor |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 45 interações, todas de gravidade moderada nos 20 itens detalhados. Todas envolvem medicamentos antidiabéticos, entre eles acarbose, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, saxagliptina, dulaglutida, empagliflozina, linagliptina, glimepirida, semaglutida, acetoexamida, ertugliflozina, exenatida, glipizida, glibenclamida e insulina humana. Recomenda-se monitorar a glicemia em pacientes diabéticos.

Para demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem literatura para nenhuma das indicações previstas (nível L5). Além disso, o mecanismo conhecido (inibição do IGF-1R) é contrário ao benefício esperado em doenças com déficit de crescimento, e o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação detalhado, obtidos de fontes como o DrugBank
- Bula do ANVISA com advertências e contraindicações, hoje ausente e que impede a triagem de segurança
- Evidências pré-clínicas ou clínicas que sustentem qualquer das indicações previstas
- Avaliação de compatibilidade de via de administração e de similaridade com a indicação original
- Reavaliação do status regulatório, já que o registro está cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

