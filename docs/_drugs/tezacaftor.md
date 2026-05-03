---
layout: default
title: Tezacaftor
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
---

# Tezacaftor
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

# Tezacaftor: Da Fibrose Cística à Doença Infecciosa por HIV

## Resumo em Uma Frase

Tezacaftor é um corretor de CFTR aprovado, em combinação com Ivacaftor, para o tratamento de fibrose cística em pacientes portadores de mutações específicas no gene CFTR.
O modelo TxGNN prevê que pode ser eficaz para **Doença Infecciosa por HIV (HIV Infectious Disease)**, porém esta associação apresenta **baixa plausibilidade biológica** — atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrose cística (em combinação com Ivacaftor) |
| Nova Indicação Prevista | Doença Infecciosa por HIV (HIV Infectious Disease) |
| Pontuação de Previsão TxGNN | 99.24% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados formais de mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento científico estabelecido, Tezacaftor é um **corretor da proteína CFTR** (Cystic Fibrosis Transmembrane Conductance Regulator): seu mecanismo consiste em estabilizar o dobramento da proteína CFTR mutante — especialmente a variante F508del —, permitindo que ela seja transportada adequadamente até a membrana celular e exerça sua função de canal de cloreto. É utilizado em combinação com Ivacaftor (como Symdeko®/Symkevi®) para potencializar o transporte iônico em pacientes com fibrose cística portadores de mutações específicas.

A conexão hipotética entre fibrose cística e HIV reside no fato de que o CFTR possui expressão funcional em células imunes como linfócitos CD4+ e macrófagos. Em teoria, a modulação do CFTR nessas células poderia influenciar aspectos da resposta imune inata. No entanto, o ciclo replicativo do HIV — baseado na integração retroviral ao DNA do hospedeiro, evasão imune e depleção progressiva de CD4+ — não tem nenhuma interseção conhecida com o dobramento proteico do CFTR. Além disso, o mecanismo de Tezacaftor é restrito a proteínas CFTR com **mutações de dobramento específicas**; pacientes com HIV geralmente não apresentam essas mutações, tornando a ação do fármaco biologicamente irrelevante nesse contexto.

A alta pontuação do TxGNN (99.24%) reflete quase certamente **conexões inespecíficas no grafo de conhecimento**: nós do sistema imunológico onde o CFTR tem expressão estão topologicamente próximos à rede patológica do HIV dentro do KG, gerando uma falsa associação. A ausência de dados de indicação original no Evidence Pack provavelmente agravou esse efeito, impedindo que o modelo contextualizasse adequadamente o escopo restrito de aplicação de Tezacaftor — exclusivo para fibrose cística com mutações CFTR responsivas ao corrector.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Tezacaftor em doença infecciosa por HIV.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Tezacaftor em doença infecciosa por HIV.

---

## Informações de Comercialização no Brasil

Tezacaftor está registrado no Brasil com **3 registros ativos** na ANVISA. Os detalhes individuais de cada registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no conjunto de dados atual. Para consulta completa, acesse o portal da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as 10 indicações previstas pelo TxGNN para Tezacaftor estão classificadas em nível de evidência L5 (somente previsão do modelo, sem estudos reais de suporte), e a análise de plausibilidade biológica demonstra que nenhuma das previsões possui justificativa mecanística suficiente para avançar — especialmente a indicação de maior pontuação (doença infecciosa por HIV), para a qual o próprio Evidence Pack conclui ausência de interseção biológica conhecida. O padrão de distribuição das pontuações (ranks 4.696 a 8.822 de um total de ~17.000 doenças) e a repetição de scores idênticos entre patologias relacionadas (FIV e SIV) reforçam a hipótese de viés sistemático por proximidade de rede no KG.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API (DG002) para análise de plausibilidade biológica aprofundada
- Preencher os dados de registros ANVISA (número, nome comercial, indicação aprovada) para caracterização regulatória completa (DG001 — severidade Blocking)
- Investigar indicações com maior proximidade fisiopatológica à fibrose cística, como bronquiectasias não-CF, DPOC com disfunção de CFTR ou outras channelopatias, que poderiam ter maior plausibilidade de reposicionamento
- Reavaliar o modelo TxGNN após complementar os dados de indicação original no Knowledge Graph, a fim de reduzir o viés de previsão observado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

