---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Degarelix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

O skill é sobre pipeline técnico (treinamento/deployment), não sobre escrita de relatórios — as instruções do sistema já cobrem completamente o formato necessário. Prosseguindo com o relatório:

---

# Degarelix: Do câncer de próstata à hipertricose

## Resumo em Uma Frase

Degarelix é um antagonista do receptor de GnRH aprovado para o tratamento do câncer de próstata avançado, suprimindo a produção de testosterona ao bloquear o eixo hipotálamo-hipófise-gônada.
O modelo TxGNN prevê que pode ser eficaz para **Hipertricose (hypertrichosis)**, com pontuação de **99,99%**; contudo, esta previsão não apresenta **nenhum ensaio clínico** nem **nenhuma publicação** de suporte — nível de evidência **L5**, exclusivamente baseado no modelo computacional.
É importante destacar que, entre as 10 previsões analisadas neste Evidence Pack, a única com conexão mecanística biologicamente plausível é a **puberdade precoce central (rank 9)**, que compartilha diretamente o eixo GnRH do fármaco.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de próstata avançado (terapia de privação androgênica) |
| Nova Indicação Prevista | Hipertricose (hypertrichosis) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Degarelix atua como antagonista competitivo de alta afinidade dos receptores de GnRH (Hormônio Liberador de Gonadotrofinas) na adeno-hipófise. Ao contrário dos agonistas de GnRH (como leuprolida), que provocam um aumento transitório inicial de LH/FSH antes da dessensibilização, Degarelix bloqueia os receptores imediatamente, suprimindo a produção de testosterona a níveis de castração em 24–72 horas sem o efeito de *flare* inicial. Este é o fundamento do seu uso aprovado no câncer de próstata hormônio-sensível.

A hipertricose — crescimento excessivo de pelos em qualquer região do corpo — é clinicamente distinta do hirsutismo. Enquanto o hirsutismo é **andrógeno-dependente** (causado por excesso de andrógenos), a hipertricose tem origem predominantemente **não andrógeno-dependente**, associada a causas genéticas, medicamentosas (minoxidil, ciclosporina, fenitoína) ou idiopáticas. O mecanismo de supressão do eixo GnRH-testosterona do Degarelix, portanto, não endereça a fisiopatologia central da hipertricose.

A alta pontuação do TxGNN para esta previsão é provavelmente um artefato de propagação de sinal no grafo de conhecimento, via a aresta "testosterona → folículo piloso", gerando uma associação estatística sem correspondência biológica direta com a forma não androgênica da doença. Este é um exemplo típico de *pathway confounding* em modelos de aprendizado em grafos. Para referência comparativa: a **puberdade precoce central (rank 9)** é a única das 10 previsões com mecanismo de ação direto — essa condição é GnRH-dependente e o seu tratamento atual já utiliza moduladores do mesmo eixo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Degarelix em hipertricose.

## Evidências da Literatura

Atualmente não há literatura relacionada para Degarelix em hipertricose.

## Informações de Comercialização no Brasil

Degarelix possui **1 registro ativo** na ANVISA com situação comercializada confirmada. Os dados detalhados do registro (número, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack — é necessário consultar a base de dados da ANVISA diretamente.

> Para referência: internacionalmente, Degarelix é comercializado como **Firmagon®** (Ferring Pharmaceuticals), na forma de pó liofilizado para solução injetável subcutânea (dose de ataque 240 mg; manutenção 80 mg a cada 28 dias).

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | **Terapia hormonal** (antagonista de GnRH) — não é citotóxico convencional |
| Risco de Mielossupressão | Baixo (mecanismo hormonal, sem ação mielossupressora direta) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | PSA, testosterona sérica, intervalo QTc (risco de prolongamento), densidade mineral óssea (uso prolongado), glicemia/HbA1c (síndrome metabólica associada à privação androgênica) |
| Proteção no Manuseio | Manipulação padrão de injetáveis; não requer precauções de citotóxico |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Panorama Geral das 10 Previsões TxGNN

Dado o padrão incomum deste Evidence Pack — onde a previsão de maior pontuação (rank 1) não é a mais clinicamente relevante —, apresenta-se abaixo o resumo analítico das 10 indicações avaliadas:

| Rank | Indicação | TxGNN Score | Evidência | Avaliação Mecanística |
|------|-----------|:-----------:|:---------:|----------------------|
| 1 | Hipertricose | 99,99% | L5 | ❌ Não andrógeno-dependente |
| 2 | Hipertricose de Ambras (congênita) | 99,98% | L5 | ❌ Genética X-linked (8q22) |
| 3 | Síndrome de Dandy-Walker | 99,98% | L5 | ❌ Malformação estrutural do SNC |
| 4 | Síndrome com componente periodontal | 99,98% | L5 | ❌ Sem ligação GnRH-periodonto |
| 5 | Anomalia genética do haste capilar | 99,98% | L5 | ❌ Defeito de queratina |
| 6 | Urticária alérgica | 99,97% | L5 | ❌ Mediada por IgE/mastócitos |
| 7 | Urticária a frio | 99,86% | L5 | ❌ Induzida por frio, sem via GnRH |
| 8 | Puberdade precoce familiar masculina | 99,84% | L5 | ❌ GnRH-independente (mut. LHCGR) |
| **9** | **Puberdade precoce central (CPP)** | **99,67%** | **L4** | **✓ GnRH-dependente — mecanismo direto** |
| 10 | Tricromegalia familiar isolada | 99,65% | L5 | ❌ Via FGF/EGFR, não GnRH |

A **puberdade precoce central (rank 9)** destaca-se como a única candidata biologicamente coerente: o eixo GnRH é o alvo direto de Degarelix, o tratamento atual de CPP já usa agonistas de GnRH (leuprolida), e Degarelix ofereceria a vantagem teórica de supressão imediata sem *flare* inicial — razão pela qual o modelo atribui nível L4 (estudos mecanísticos) em vez de L5. Ainda assim, faltam dados clínicos específicos de Degarelix em CPP.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão de maior pontuação (hipertricose) é mecanisticamente incoerente — hipertricose é não andrógeno-dependente — e não possui nenhum ensaio clínico ou publicação associando Degarelix a esta condição. O padrão se repete em 9 das 10 previsões, sugerindo que o sinal do TxGNN neste caso é amplamente artefatual, provavelmente por confundimento via o nó "testosterona" no grafo de conhecimento.

**Para prosseguir, é necessário:**
- Obter dados detalhados do registro ANVISA (número do registro, bula oficial com indicações aprovadas no Brasil)
- Obter dados completos de segurança (advertências, contraindicações da bula brasileira) para cumprir o requisito de avaliação S1
- Avaliar separadamente a **puberdade precoce central (rank 9)** como candidata prioritária de reposicionamento, com busca sistemática de ensaios clínicos de antagonistas de GnRH de classe (cetrorelix, ganirelix) nessa indicação, como evidência indireta de classe farmacológica
- Confirmar dados de segurança pediátrica antes de qualquer exploração em CPP
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

