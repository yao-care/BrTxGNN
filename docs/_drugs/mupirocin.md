---
layout: default
title: Mupirocin
parent: Apenas Predição do Modelo (L5)
nav_order: 466
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-29
description: "Mupirocin: nova indicação prevista, Empiema Pleural (pleural empyema) (nível de evidência L5). Indicação original: Antiinfecciosos tópicos"
monitor_inn: "mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Mupirocin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Mupirocina: De antiinfeccioso tópico a empiema pleural
{: .text-alpha }

## Resumo em Uma Frase

Mupirocina é um antibiótico de uso tópico, registrado na ANVISA na categoria de antiinfecciosos tópicos.
O modelo TxGNN prevê que pode ser eficaz para **Empiema Pleural (pleural empyema)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiinfecciosos tópicos |
| Nova Indicação Prevista | Empiema Pleural (pleural empyema) |
| Pontuação de Previsão TxGNN | 0,9949 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 8) |
| Número de Registros | 8 (ativos: 7) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a mupirocina é um antibacteriano tópico que inibe a isoleucil-tRNA sintetase bacteriana, com atividade principalmente contra bactérias Gram-positivas, como *Staphylococcus aureus* (incluindo MRSA) e estreptococos.

Esses microrganismos são causas comuns de empiema pleural, o que cria uma ligação plausível, porém apenas teórica, entre a indicação original (infecções cutâneas tópicas) e a nova indicação.

Há, contudo, limitações importantes. A mupirocina é formulada apenas para uso tópico; não existe formulação sistêmica ou intrapleural estabelecida, nem dados de penetração pleural, segurança ou posologia. O empiema é tratado com drenagem e antibióticos sistêmicos, de modo que um agente tópico não se encaixa na via de administração necessária. A pontuação alta do TxGNN é uma previsão computacional, sem respaldo de estudos nos dados compilados.

**Segunda previsão do modelo:** ceratoconjuntivite epitelial punctata (pontuação de 0,9910). A atividade antiestafilocócica da mupirocina poderia ser relevante apenas no subconjunto bacteriano; muitos casos são virais ou não infecciosos. A pomada não é aprovada para uso oftálmico, a tolerabilidade na superfície ocular não está estabelecida e já existem antibióticos oftálmicos aprovados. Também não há ensaios ou literatura, e a decisão é Hold.

---

## Informações de Comercialização no Brasil

Os 8 registros estão válidos (8 de 8); o medicamento é comercializado atualmente no Brasil.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 109170132 | Bacrocin | Não informada | Antiinfecciosos tópicos |
| Registro nº 100630269 | Mupirocina | Não informada | Antiinfecciosos tópicos |
| Registro nº 125680157 | Mupirocina | Não informada | Antiinfecciosos tópicos |
| Registro nº 107150145 | Dermoban | Não informada | Antiinfecciosos tópicos |
| Registro nº 102980268 | Mupirocina | Não informada | Antiinfecciosos tópicos |

---

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento)**: o grafo de conhecimento do TxGNN (PrimeKG) registra uma relação de contraindicação com **dermatite**. Isso não provém do texto da bula e deve ser verificado.
- **Interações Medicamentosas**: foram identificadas 118 possíveis interações, todas com nível de gravidade não classificado. Entre as listadas estão calcitriol, clotrimazol, morfina, metformina, pantoprazol, omeprazol, sucralfato, vancomicina, lactulose, triancinolona, prednisona e sinvastatina. A relevância clínica precisa ser avaliada.

Consulte a bula para as demais informações de segurança (advertências e contraindicações).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia apenas na pontuação do modelo (L5), sem ensaios clínicos ou literatura. Além disso, a via tópica é incompatível com o tratamento do empiema pleural, e o medicamento é comercializado no Brasil, com 8 registros válidos de 8.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA para advertências e contraindicações, etapa de segurança que hoje está bloqueada.
- Obter dados de mecanismo de ação no DrugBank.
- Avaliar a viabilidade de uma formulação ou via de administração adequada (por exemplo, intrapleural), com dados de penetração, segurança e posologia.
- Realizar revisão sistemática da literatura e de registros de ensaios para empiema pleural e para ceratoconjuntivite epitelial punctata.
- Esclarecer a relação de contraindicação com dermatite e a relevância clínica das interações medicamentosas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

