---
layout: default
title: Vitamin A
parent: Apenas Predição do Modelo (L5)
nav_order: 672
evidence_level: L5
indication_count: 10
---

# Vitamin A
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Vitamina A: Da deficiência de vitamina A à congenital prothrombin deficiency (deficiência congênita de protrombina)

## Resumo em Uma Frase

A vitamina A é um nutriente essencial, originalmente usado no tratamento de distúrbios de deficiência vitamínica e da deficiência de vitamina A.
O modelo TxGNN prevê que pode ser eficaz para **deficiência congênita de protrombina (congenital prothrombin deficiency)**, mas **não há nenhum ensaio clínico nem publicação** apoiando esta direção. A previsão baseia-se apenas na estrutura do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Distúrbio de deficiência vitamínica / deficiência de vitamina A |
| Nova Indicação Prevista | Deficiência congênita de protrombina (congenital prothrombin deficiency) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a vitamina A (retinol) participa da visão, da diferenciação do epitélio, da imunidade e do desenvolvimento embrionário, e sua eficácia na deficiência de vitamina A é bem estabelecida.

A relação com a deficiência congênita de protrombina, porém, é fraca. Trata-se de um distúrbio genético da coagulação, e a vitamina relevante para a síntese de protrombina é a vitamina K, não a vitamina A. A pontuação muito alta do modelo provavelmente reflete uma associação genérica, dentro da rede do grafo, entre fármacos da categoria "vitaminas" e distúrbios nutricionais ou metabólicos, e não um mecanismo específico.

Por isso, esta previsão deve ser tratada com cautela: não há base mecanística estabelecida que a sustente.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Outras Indicações Previstas com Algum Respaldo

Embora a indicação de maior pontuação não tenha evidências, outras previsões do modelo têm dados que merecem registro:

| Indicação Prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Doença perinatal (perinatal disease) | 99,63% | L1 | Várias revisões sistemáticas Cochrane (2000–2016) sobre suplementação de vitamina A em recém-nascidos de muito baixo peso para prevenir displasia broncopulmonar e mortalidade; efeitos modestos e rótulo heterogêneo. O ensaio NCT01115478 (n=2.500, concluído) trata de malária na gravidez e não é específico para vitamina A. |
| Lesão (injury) | 99,69% | L2 | Ensaio NCT01203488 (Fase 1/2, n=807, concluído) e NCT02102711 (n=62), ambos em recém-nascidos de muito baixo peso; relaciona-se mais à lesão pulmonar neonatal do que a lesão em geral. |
| Distúrbio de proliferação celular | 99,64% | L4 | Evidência mecanística (retinoides regulam proliferação e diferenciação); único ensaio é sobre olho seco, não sobre doença proliferativa. |
| Distúrbio induzido por radiação ou químicos | 99,63% | L4 | Literatura indireta sobre fotoenvelhecimento e fotobiologia. |

As demais previsões (doença do metabolismo da biotina, malformação esofágica não sindrômica, displasia odontomaxilar segmentar, displasia cemento-óssea florida e categoria genérica "doença por sistema subcelular afetado") não têm ensaios, e a literatura disponível é geral e não testa a vitamina A como tratamento.

---

## Informações de Comercialização no Brasil

Segundo os dados compilados para este relatório, não há registros ativos de vitamina A isolada na ANVISA, e o fármaco consta como não comercializado.

---

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: o grafo associa a vitamina A a contraindicação em diversas condições, entre elas: doença renal, doença hepática, doença da vesícula biliar, úlcera péptica, sarcoidose, hipercalcemia, nefrocalcinose, nefrolitíase, hiperfosfatemia, hiperoxalúria primária, hemocromatose hereditária, hemossiderose, doença de Wilson, anemia falciforme, anemia hemolítica, retocolite ulcerativa, doença inflamatória intestinal, gastroenterite, hipervitaminose e arteriosclerose obliterante.
- **Interações Medicamentosas**: foram identificadas 68 interações. As principais, de gravidade **maior**, são:
  - Retinoides: isotretinoína, acitretina, tretinoína (risco de toxicidade aditiva por hipervitaminose A).
  - Tetraciclinas: doxiciclina, tetraciclina, minociclina, demeclociclina, oxitetraciclina, omadaciclina, eravaciclina e sarecilina.
  
  De gravidade **moderada**: bexaroteno, colestiramina, colesevelam, colestipol, sevelâmer e selpercatinibe. De gravidade **menor**: orlistate.
- **Toxicidade**: a literatura destaca o risco de hipervitaminose A (toxicidade hepática, óssea) e de teratogenicidade, o que exige atenção especial à dose.

Para advertências e contraindicações em bula, consulte a bula do produto, pois não há texto de bula da ANVISA disponível.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A indicação de maior pontuação (deficiência congênita de protrombina) é uma previsão puramente de grafo (L5), sem ensaios, sem literatura e sem mecanismo plausível; a vitamina relevante para a protrombina é a vitamina K.
- O fármaco não é comercializado no Brasil, e faltam os dados de bula da ANVISA, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), que é uma lacuna bloqueante.
- Obter os dados do mecanismo de ação no DrugBank.
- Se houver interesse em reposicionamento, priorizar a direção com mais respaldo (doença perinatal / displasia broncopulmonar em recém-nascidos de muito baixo peso), definindo dose, via de administração (intramuscular vs. oral) e limites de segurança quanto a toxicidade e teratogenicidade.
- Confirmar a viabilidade regulatória e de via de administração, já que não há registro vigente no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

