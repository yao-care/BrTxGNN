---
layout: default
title: Nomegestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Nomegestrol Acetate
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

# Nomegestrol Acetate: Da contracepção hormonal à candidíase

## Resumo em Uma Frase

Nomegestrol acetate é uma progestina sintética de alta seletividade, aprovada internacionalmente como anticoncepcional hormonal oral em combinação com 17β-estradiol (Zoely®), porém **sem registro na ANVISA** e não comercializada no Brasil. O modelo TxGNN prevê como principal indicação candidata a **Candidíase (Candidiasis)**, com **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção. Importante: a análise mecanística indica que esta previsão provavelmente reflete uma associação de **risco** — progestinas tendem a aumentar, e não reduzir, a suscetibilidade à candidíase.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Contracepção hormonal (aprovação internacional; não registrado no Brasil) |
| Nova Indicação Prevista | Candidíase (Candidiasis) |
| Pontuação de Previsão TxGNN | 98,78% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Nomegestrol acetate é uma progestina sintética de terceira geração com alta afinidade seletiva pelos receptores de progesterona e ausência de atividade estrogênica, androgênica ou glicocorticoide clinicamente relevante. É aprovado na União Europeia e em outros países como anticoncepcional oral em combinação com 17β-estradiol (Zoely®: NOMAC 2,5 mg + E2 1,5 mg). No Brasil, não há registro na ANVISA e o fármaco não é comercializado. Dados detalhados de mecanismo de ação (MOA) não estavam disponíveis neste Evidence Pack.

A conexão do TxGNN com candidíase provavelmente origina-se de nós intermediários no grafo de conhecimento que ligam progestinas, imunidade de mucosa e infecções fúngicas. No entanto, a direção mecanística é **oposta** ao que seria esperado de um agente terapêutico: progestinas alteram o pH vaginal e a composição da microbiota local, além de modularem a resposta imune de mucosa de forma a **favorecer** a colonização por *Candida spp.*, não a combatê-la. Gestantes — com níveis endógenos de progesterona elevados — e usuárias de contraceptivos com componente progestínico apresentam maior incidência de candidíase vulvovaginal, dado consistente com ampla literatura clínica.

Portanto, a previsão de ranque 1 provavelmente reflete uma **associação epidemiológica negativa** (progestinas como fator de risco para candidíase) capturada pelo grafo de conhecimento como proximidade topológica, e não como caminho terapêutico real. O uso de Nomegestrol acetate para tratar candidíase não tem base mecanística plausível — na prática, o fármaco poderia **piorar** o quadro clínico em pacientes predispostas a infecções fúngicas.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para candidíase com Nomegestrol acetate.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para candidíase com Nomegestrol acetate.

---

## Informações de Comercialização no Brasil

Nomegestrol acetate não possui registro na ANVISA e não é comercializado no Brasil. Nenhum produto foi localizado no banco de dados regulatório brasileiro. Para comparação, o produto Zoely® (NOMAC + E2) possui aprovação na EMA (Europa) desde 2011, mas nunca foi registrado no Brasil.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> Nota: Os dados de advertências, contraindicações e interações medicamentosas não estavam disponíveis neste Evidence Pack. Recomenda-se consultar a bula aprovada pela EMA e dados do DrugBank antes de qualquer avaliação clínica. Em particular, o perfil pró-trombótico de progestinas (redução da atividade da proteína S, alteração do equilíbrio fibrinolítico) é clinicamente relevante para as indicações previstas nos ranques 2–4 e 9, nas quais o uso de progestinas pode ser **contraindicado**.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Nenhuma das 10 indicações previstas pelo TxGNN apresenta evidências clínicas de eficácia terapêutica, e a previsão de maior pontuação (candidíase) é mecanisticamente contraditória. Várias das demais indicações (deficiência de antitrombina, deficiência de cofator 2 da heparina, excesso de Fator V, doença trombótica) representam condições nas quais progestinas são potencialmente **contraindicadas** — os ensaios clínicos localizados para doença trombótica (ranque 9) tratam apenas de monitoramento de segurança de VTE em estudos anticoncepcionais, e não de eficácia terapêutica. O fármaco também não possui registro na ANVISA, adicionando uma barreira regulatória significativa.

**Para prosseguir, é necessário:**
- Obter registro na ANVISA ou definir estratégia de desenvolvimento regulatório no Brasil
- Completar o perfil de MOA com dados do DrugBank e bula da EMA
- Entre as 10 indicações avaliadas, **artrite reumatoide** (ranque 10) apresenta a fundamentação mecanística relativamente mais coerente — imunorregulação via modulação Th1/Th2, análoga à remissão de AR observada na gestação — sendo a única candidata com alguma plausibilidade biológica, ainda que sem qualquer evidência clínica específica para Nomegestrol acetate
- Realizar estudos pré-clínicos antes de avançar para qualquer avaliação clínica em artrite reumatoide
- Descartar formalmente as indicações pró-trombóticas (ranques 2, 3, 4, 9) por risco de dano ao paciente
---

