---
layout: default
title: Ioversol
parent: Apenas Predição do Modelo (L5)
nav_order: 372
evidence_level: L5
indication_count: 9
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-23
description: "Ioversol: nova indicação prevista, Osteoartrite (osteoarthritis) (nível de evidência L5). Indicação original: Não informada nos textos de registro disponíveis"
---

# Ioversol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Ioversol: De agente de contraste iodado para osteoartrite
{: .text-alpha }

## Resumo em Uma Frase

Ioversol é um meio de contraste iodado não iônico, de baixa osmolaridade, usado em exames de imagem diagnóstica. Não há indicação original descrita nos registros brasileiros compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **Osteoartrite (osteoarthritis)**, mas hoje há **0 ensaios clínicos** e **1 publicação** associada, e essa publicação não estuda o ioversol (usa outro agente iodado, o Lipiodol, como material de embolização). A pontuação vem do modelo TxGNN (aprendizado profundo) e pode refletir similaridades aprendidas pelo modelo entre doenças relacionadas, não evidência biológica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não informada nos textos de registro disponíveis |
| Nova Indicação Prevista | Osteoartrite (osteoarthritis) |
| Pontuação de Previsão TxGNN | 0,9963 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação do ioversol nos dados compilados para este relatório. Segundo informações conhecidas, trata-se de um meio de contraste iodado, usado para visualização de estruturas em exames de imagem, sem atividade farmacológica anti-artrítica conhecida.

A única publicação associada (estudo LipioJoint-1, 2024) avaliou a embolização transitória das artérias genicualres em osteoartrite de joelho usando uma emulsão de óleo etiodado (Lipiodol), outro agente iodado. O efeito terapêutico vem do procedimento de embolização, não do ioversol. O ioversol poderia, no máximo, ser usado de forma incidental como contraste para guiar a angiografia, o que não constitui sinal de reposicionamento.

Portanto, a pontuação alta (0,9963) vem do modelo TxGNN (aprendizado profundo) e pode refletir similaridades aprendidas pelo modelo entre doenças relacionadas, e não uma relação mecanística real. Como nenhum estudo citado investiga o ioversol na osteoartrite, o nível de evidência é L5.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensaio clínico de braço único/piloto | Diagnostic and Interventional Imaging | Avaliou a segurança e a eficácia da embolização transitória das artérias genicualres com emulsão de óleo etiodado (Lipiodol) em osteoartrite de joelho. Não estudou o ioversol. |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 113980036 (válido) | OPTIRAY | Não informada | Não informada |
| Registro 113980030 (cancelado) | OPTIRAY | Não informada | Não informada |
| Registro 149800023 (cancelado) | OPTIRAY | Não informada | Não informada |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as principais estão as de gravidade **maior** com:
  - metformina;
  - anfotericina B (e suas formulações lipídicas, lipossomal e de sulfato de colesterila);
  - mesalazina, balsalazida, olsalazina e sulfasalazina;
  - vancomicina;
  - aminoglicosídeos (canamicina, neomicina, estreptomicina);
  - polimixina B.

  A interação com manitol é de gravidade moderada. Muitas dessas combinações envolvem risco de lesão renal ou de acúmulo de metformina, o que exige cautela.
- **Contexto da previsão**: em doenças como a hemoglobinopatia (por exemplo, anemia falciforme), meios de contraste podem representar preocupação de segurança (osmolaridade, hemólise), o que desaconselha uso terapêutico.

Consulte a bula para as demais informações de segurança, pois advertências e contraindicações da bula não estavam disponíveis.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaio clínico nem publicação que estude o ioversol na osteoartrite; a única referência trata de outro agente (Lipiodol) em um procedimento de embolização. O ioversol é um agente diagnóstico sem mecanismo terapêutico plausível para essa doença, e as demais previsões do modelo (artrite reumatoide, braquiolmia, hemoglobinopatia, alopecia e outras) também carecem de evidências.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências, contraindicações e indicações aprovadas), hoje uma lacuna bloqueante para a triagem de segurança.
- Obter dados de mecanismo de ação no DrugBank.
- Confirmar, com revisão da literatura, se existe algum estudo que avalie o próprio ioversol na osteoartrite; caso contrário, considerar que a pontuação do modelo TxGNN pode refletir apenas similaridades aprendidas entre doenças relacionadas, e não evidência biológica, e não investir em desenvolvimento.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

