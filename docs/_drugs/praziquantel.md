---
layout: default
title: Praziquantel
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

Usando o skill **txgnn-pipeline** para orientação de contexto, e seguindo o formato do sistema de avaliação de reposicionamento de fármacos. Prossigo com a geração do relatório.

---

# Praziquantel: Das helmintíases ao leiomiosarcoma epitelioide uterino

## Resumo em Uma Frase

Praziquantel é um anti-helmíntico de amplo espectro, reconhecido mundialmente como tratamento de primeira linha para esquistossomose e infecções por tenídeos, com 7 registros ativos no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Leiomiosarcoma Epitelioide Uterino (uterine corpus epithelioid leiomyosarcoma)**,
porém atualmente **não há ensaios clínicos nem publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Esquistossomose e outras helmintíases (dados textuais de indicação aprovada não disponíveis no sistema) |
| Nova Indicação Prevista | Leiomiosarcoma Epitelioide Uterino (uterine corpus epithelioid leiomyosarcoma) |
| Pontuação de Previsão TxGNN | 97,28% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Já comercializado |
| Número de Registros | 7 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no sistema. Segundo informações amplamente conhecidas na literatura farmacológica, o Praziquantel (PZQ) aumenta a permeabilidade da membrana celular de platelmintos aos íons cálcio (Ca²⁺), causando contração muscular intensa, vacuolização do tegumento e morte do parasita. Essa ação seletiva sobre canais iônicos de helmintos é a base de seu uso consagrado em esquistossomose, neurocisticercose e outras infecções por trematódeos e cestódeos.

A hipótese de reposicionamento para leiomiosarcoma epitelioide uterino apoia-se em dois mecanismos especulativos identificados pelo modelo TxGNN. O primeiro sugere que o PZQ poderia inibir a via de sinalização Wnt/β-catenina, efeito relatado em estudos iniciais com linhagens celulares de câncer de cólon. O segundo propõe que a ativação de canais TRPV4 pelo PZQ poderia influenciar a proliferação de tumores originados em músculo liso, compartilhando a base tecidual com o leiomiosarcoma uterino.

Contudo, é fundamental deixar claro que **ambos os mecanismos são inteiramente hipotéticos** no contexto oncológico: não existe qualquer dado clínico, pré-clínico direto ou de modelos animais confirmando atividade do PZQ contra leiomiosarcomas. O leiomiosarcoma epitelioide uterino é, ainda, uma variante histológica rara e de alta agressividade. A previsão TxGNN deve ser interpretada exclusivamente como um sinal gerador de hipótese, sem implicação clínica imediata.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Praziquantel em leiomiosarcoma epitelioide uterino.

---

## Evidências da Literatura

Atualmente não há literatura relacionada a Praziquantel e leiomiosarcoma epitelioide uterino.

---

## Informações de Comercialização no Brasil

O sistema registra **7 licenças ativas** de Praziquantel no Brasil (situação: já comercializado). Os dados detalhados dos registros individuais — incluindo número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada — não estão disponíveis no conjunto de dados atual e devem ser consultados diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe nenhuma evidência clínica ou pré-clínica direta que apoie o uso de Praziquantel em leiomiosarcoma epitelioide uterino. A pontuação TxGNN de 97,28% reflete conectividade no grafo de conhecimento, mas a ausência total de evidências experimentais classifica esta candidatura no estágio mais preliminar possível (L5 / S0).

**Para prosseguir, é necessário:**
- Estudos pré-clínicos in vitro em linhagens celulares de leiomiosarcoma uterino (ensaios de viabilidade, apoptose, ciclo celular)
- Confirmação experimental da inibição Wnt/β-catenina ou modulação TRPV4 em células de sarcoma uterino
- Dados de mecanismo de ação (MOA) formalizados a partir do DrugBank (DG002)
- Recuperação das bulas registradas na ANVISA para preenchimento de advertências e contraindicações (DG001)
- Consulta a especialistas em oncologia ginecológica para avaliar relevância clínica da hipótese
---

