---
layout: default
title: Estradiol Valerate
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Estradiol Valerate
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

# Estradiol Valerate: Da Terapia Hormonal Substitutiva à Síndrome do X Frágil Sintomático em Portadoras

## Resumo em Uma Frase

Estradiol Valerate (Progynova®) é um éster sintético do estradiol amplamente utilizado como terapia hormonal substitutiva no tratamento do déficit estrogênico, menopausa e insuficiência ovariana primária.
O modelo TxGNN prevê que pode ser eficaz para a **Forma Sintomática da Síndrome do X Frágil em Portadoras Femininas (symptomatic form of fragile X syndrome in female carrier)**, indicação que, porém, **não conta com nenhum ensaio clínico registrado nem publicação humana** apoiando esta direção — configurando alta suspeita de falso positivo do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Terapia hormonal substitutiva / déficit estrogênico (uso clínico estabelecido; sem registro localizado na base regulatória consultada) |
| Nova Indicação Prevista | Síndrome do X Frágil Sintomático em Portadoras Femininas |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não localizado na base regulatória consultada |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados de mecanismo de ação (MOA) disponíveis no Evidence Pack para este fármaco. Com base em conhecimento farmacológico estabelecido, o Estradiol Valerate é um éster do 17β-estradiol que, após hidrólise in vivo, libera estradiol ativo capaz de se ligar aos receptores de estrogênio ERα e ERβ, modulando a expressão gênica em tecidos-alvo como endométrio, mama, ossos e sistema nervoso central.

A conexão com a Síndrome do X Frágil em portadoras femininas é indireta: portadoras da pré-mutação do gene FMR1 têm até 20% de probabilidade de desenvolver Insuficiência Ovariana Primária (POI), condição caracterizada justamente por déficit estrogênico endógeno. Adicionalmente, sinalizações anômalas dos receptores ERα/ERβ foram descritas em modelos neuronais da síndrome, sugerindo um possível ponto de convergência molecular entre o eixo estrogênico e a fisiopatologia do FMR1.

No entanto, essa ligação representa um elo mediado — "FMR1 → função ovariana → eixo estrogênico" — identificado pelo TxGNN no grafo de conhecimento, e não um efeito terapêutico direto sobre os sintomas neurológicos ou cognitivos da síndrome. A pontuação elevada do modelo (99,94%) quase certamente reflete o **efeito de hub topológico** (KG hub effect) dos nós de hormônios sexuais no grafo, e não uma relação farmacológica real. A ausência total de evidências clínicas humanas confirma essa interpretação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Estradiol Valerate na indicação de Síndrome do X Frágil em portadoras femininas.

---

## Evidências da Literatura

Atualmente não há literatura relacionada ao uso de Estradiol Valerate para Síndrome do X Frágil em portadoras femininas.

---

## Informações de Comercialização no Brasil

Nenhum registro encontrado na base regulatória consultada para ESTRADIOL VALERATE.

> **Nota de Integridade dos Dados:** Este fármaco provavelmente está comercializado no Brasil (ex.: **Progynova®** — Bayer), mas os registros não foram capturados na consulta atual à base regulatória. Recomenda-se verificação direta no portal ANVISA (anvisa.gov.br) para confirmar registros vigentes e indicações aprovadas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para Síndrome do X Frágil em portadoras femininas é classificada como L5 — exclusivamente baseada em previsão do modelo, sem qualquer ensaio clínico ou publicação humana de suporte. A ligação mecanística identificada é indireta, mediada pelo eixo FMR1–POI–estrogênio, com alta probabilidade de ser artefato de hub topológico no grafo de conhecimento. Não há base clínica para avançar nesta direção no momento.

**Para prosseguir, seria necessário:**
- Identificar publicações descrevendo intervenção com estrogênio em portadoras sintomáticas de pré-mutação FMR1 (busca específica na literatura)
- Obter MOA detalhado via DrugBank API (DB13956) para avaliar ligação direta aos mecanismos neurológicos do FMR1
- Obter dados regulatórios completos da ANVISA para confirmar situação de registro e indicações aprovadas no Brasil
- Avaliar perfil de segurança específico para portadoras de pré-mutação FMR1, dado o risco potencial de estimulação ovariana em contexto de POI

> **Aviso ao revisor:** Embora esta indicação (rank 1) seja classificada como Hold, o Evidence Pack contém indicações com evidência mais robusta neste mesmo candidato — em especial **anovulação** (rank 7, L2, *Proceed with Guardrails*), com 1 RCT Phase 4 relevante (NCT02186782, n=600) e múltiplos estudos de suporte, e **disfunção ovariana** (rank 10, L3). Recomenda-se geração de relatórios dedicados para essas indicações.

---

> ⚠️ *Este relatório é gerado pelo pipeline TxGNN para fins de pesquisa. Os resultados são previsões computacionais e não constituem aconselhamento médico. Candidatos a reposicionamento requerem validação clínica antes de qualquer aplicação.*
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

