---
layout: default
title: Idursulfase
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Idursulfase
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

Usando `txgnn-pipeline` para contextualizar o relatório. Analisando o Evidence Pack agora.

---

**Observações-chave antes de escrever:**

- **Idursulfase** = ERT (terapia de reposição enzimática) para MPS II (Hunter syndrome); substitui a enzima iduronate-2-sulfatase
- **Top 9 previsões**: todas são anomalias oculares congênitas estruturais → sem base mecanística com GAG → falsos positivos sistêmicos do grafo
- **Rank 10 (Scheie syndrome, L4)**: tem literatura, porém a enzima deficiente é diferente (IDUA, não IDS) → mecanismo incompatível
- **Dados de registro ANVISA**: campos todos vazios → omitir tabela de comercialização
- **Não antineoplásico** → omitir seção Citotoxicidade

---

# Idursulfase: Da Síndrome de Hunter (MPS II) à Síndrome de Ptose-Estrabismo-Pupilas Ectópicas

## Resumo em Uma Frase

Idursulfase é uma terapia de reposição enzimática usada no tratamento da Mucopolissacaridose tipo II (MPS II, Síndrome de Hunter), uma doença lisossomal rara causada pela deficiência hereditária da enzima iduronate-2-sulfatase.
O modelo TxGNN prevê como primeira indicação a **Síndrome de Ptose-Estrabismo-Pupilas Ectópicas (Ptosis-Strabismus-Ectopic Pupils Syndrome)**, porém esta previsão conta com **0 ensaios clínicos** e **0 publicações** de suporte — sendo identificada como um falso positivo sistemático do grafo de conhecimento, sem base mecanística.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Mucopolissacaridose tipo II (Síndrome de Hunter) — deficiência de iduronate-2-sulfatase |
| Nova Indicação Prevista | Síndrome de Ptose-Estrabismo-Pupilas Ectópicas (*Ptosis-Strabismus-Ectopic Pupils Syndrome*) |
| Pontuação de Previsão TxGNN | 97.89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base no conhecimento estabelecido, Idursulfase (Elaprase®) é uma forma recombinante da enzima lisossomal iduronate-2-sulfatase (IDS), que catalisa a hidrólise de resíduos sulfatados em glicosaminoglicanos (GAGs) como dermatan sulfate e heparan sulfate. Na MPS II, a deficiência desta enzima leva ao acúmulo progressivo de GAGs em múltiplos tecidos, com manifestações sistêmicas multiviscerais que incluem, entre outras, **manifestações oculares** — opacidade de córnea, papiledema e alterações retinianas.

São justamente essas manifestações oculares da MPS II que explicam a alta pontuação TxGNN (97.89%) para a síndrome de ptose-estrabismo-pupilas ectópicas. No grafo de conhecimento, os nós de doenças oftalmológicas ficam em proximidade com o nó de Idursulfase por conta das complicações oculares da MPS II — o que cria um **falso positivo estrutural**: o modelo interpreta vizinhança de grafo como plausibilidade terapêutica, sem considerar a etiologia subjacente de cada doença.

Na prática, a síndrome de ptose-estrabismo-pupilas ectópicas é uma **anomalia congênita do desenvolvimento neuro-ocular** — uma malformação da musculatura extraocular e do esfíncter pupilar de origem embriológica. Não envolve acúmulo de GAGs, nem deficiência enzimática lisossomal. O tratamento é cirúrgico. Este padrão se repete nas 9 indicações mais bem ranqueadas pelo TxGNN para Idursulfase: todas são anomalias estruturais oculares congênitas (ptose, Síndrome de Horner congênita, entrópio, ectrópio, Marcus Gunn, *jaw-winking*, etc.), configurando uma classe sistemática de falso positivo sem suporte biológico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para esta indicação prevista.

> **Nota:** A indicação de rank 10 (Síndrome de Scheie, MPS IS) possui 7 publicações, mas a análise mecanística indica incompatibilidade: o Scheie syndrome resulta de deficiência de α-L-iduronidase (IDUA), enzima diferente e posterior a IDS na via de degradação de GAGs. Idursulfase não resolve o bloqueio metabólico do MPS IS; o tratamento correto é Laronidase (Aldurazyme).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as 10 indicações previstas pelo TxGNN carecem de suporte científico válido para Idursulfase: as 9 primeiras são anomalias estruturais congênitas do olho sem relação com metabolismo de GAGs (falsos positivos sistemáticos por proximidade de grafo), e a 10ª envolve deficiência enzimática de uma proteína distinta — inviabilizando o reposicionamento sob qualquer das previsões atuais.

**Para prosseguir, é necessário:**
- Recuperar dados completos dos 2 registros ANVISA (nome comercial, forma farmacêutica, indicação aprovada) para completar o perfil regulatório
- Obter bula ANVISA para preenchimento de advertências, contraindicações e informações de segurança
- Reavaliação das previsões TxGNN com **filtragem de falsos positivos oftalmológicos** gerados por vizinhança de nós de MPS II no grafo de conhecimento
- Explorar indicações dentro do espectro de **doenças lisossomais por armazenamento de GAG** (ex.: MPS VI, MPS VII) onde a similaridade bioquímica com MPS II é real e o mecanismo de ERT é aplicável
- Considerar análise de subgrupos populacionais (pacientes pediátricos vs. adultos) dada a natureza rara e progressiva da doença original
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

