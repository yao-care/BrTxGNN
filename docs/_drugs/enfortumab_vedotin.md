---
layout: default
title: Enfortumab Vedotin
parent: Apenas Predição do Modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

# Enfortumabe vedotina: De agente antineoplásico para hanseníase (previsão computacional)

## Resumo em Uma Frase

Enfortumabe vedotina (PADCEV) é um conjugado anticorpo-fármaco registrado na ANVISA na categoria de "agentes antineoplásicos".
O modelo TxGNN prevê que pode ser eficaz para **hanseníase (leprosy)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Hanseníase (leprosy) |
| Pontuação de Previsão TxGNN | 99,53% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, enfortumabe vedotina é um conjugado anticorpo-fármaco dirigido contra a Nectina-4, que entrega a monometil auristatina E (MMAE), um agente que rompe os microtúbulos. Sua eficácia como antineoplásico em carcinoma urotelial é conhecida.

Não há relação mecanística identificada entre esse tipo de ação e a infecção por *Mycobacterium leprae*. Nada nos dados conecta o direcionamento à Nectina-4 ou a entrega de carga citotóxica à hanseníase. A pontuação alta (99,53%) reflete apenas uma associação computacional no grafo de conhecimento, sem respaldo em ensaios ou literatura. A similaridade com a indicação original ainda não foi avaliada.

Outras indicações previstas pelo modelo (também todas de nível L5 e com recomendação Hold) incluem neoplasia endócrina múltipla, infecção por citomegalovírus, candidíase, infarto cerebral, infecção por HIV, hipercolesterolemia familiar homozigótica, febre catarral maligna e rinotraqueíte infecciosa bovina. As duas últimas são doenças veterinárias, provavelmente artefatos do grafo de conhecimento. As publicações associadas a citomegalovírus (relato de caso de esofagite ulcerativa grave após enfortumabe vedotina + pembrolizumabe) e a candidíase (análise de farmacovigilância FAERS sobre conjugados anticorpo-fármaco em câncer de bexiga) apontam para sinais de segurança, não para benefício terapêutico.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 121100501 (cancelado) | PADCEV | Não informada | Agentes antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Conjugado anticorpo-fármaco (terapia alvo com carga citotóxica, MMAE) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula; por conter carga citotóxica, seguir os regulamentos de manuseio de citotóxicos |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 147 interações no total. Entre as listadas, a de gravidade **maior** é com **claritromicina**. As demais, de gravidade **moderada**, envolvem principalmente antidiabéticos (acarbose, metformina, pioglitazona, glimepirida, glipizida, glibenclamida, linagliptina, saxagliptina, alogliptina), inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), agonistas de GLP-1 (albiglutida, dulaglutida, exenatida), além de aprepitanto, clorpropamida e acetoexamida.
- Os sinais de segurança observados na literatura (esofagite ulcerativa grave em associação com pembrolizumabe; sinais de farmacovigilância em câncer de bexiga) reforçam a cautela, sobretudo em populações com infecções.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hanseníase não tem ensaios clínicos, literatura nem mecanismo plausível (nível L5). Além disso, o único registro no Brasil está cancelado, e um fármaco citotóxico e imunossupressor dificilmente seria adequado para uma doença infecciosa tratável com terapias estabelecidas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação via DrugBank e avaliar qualquer elo biológico entre Nectina-4/MMAE e hanseníase.
- Buscar evidências pré-clínicas que justifiquem a hipótese antes de qualquer estudo clínico.
- Esclarecer a situação regulatória (registro cancelado) e a viabilidade de acesso ao produto no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

