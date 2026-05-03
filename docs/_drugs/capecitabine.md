---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: Do câncer colorretal para adenocarcinoma gástrico com polipose proximal do estômago (GAPPS)

## Resumo em Uma Frase

Capecitabine é uma fluoropirimidina oral (pró-fármaco do 5-FU), amplamente utilizada no tratamento do câncer colorretal, gástrico e de mama em âmbito global, embora não registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Adenocarcinoma Gástrico com Polipose Proximal do Estômago (GAPPS — Gastric Adenocarcinoma and Proximal Polyposis of the Stomach)**, uma síndrome hereditária rara de alto risco de malignização.
Atualmente, **não há ensaios clínicos registrados nem publicações** apoiando diretamente esta indicação específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer colorretal, mama e gástrico (uso global estabelecido; não registrado no Brasil) |
| Nova Indicação Prevista | Adenocarcinoma Gástrico com Polipose Proximal do Estômago (GAPPS) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Capecitabine é um pró-fármaco oral da classe das fluoropirimidinas. Embora o mecanismo de ação detalhado não esteja disponível no Evidence Pack, é amplamente documentado na literatura que o Capecitabine sofre ativação enzimática em três etapas: conversão hepática para 5′-DFCR e 5′-DFUR, seguida de conversão preferencial em tecido tumoral — rico em timidina fosforilase (TP) — para 5-fluorouracil (5-FU) ativo. O 5-FU inibe a timidilato sintase (TS), bloqueando a síntese de timidilato e, consequentemente, a replicação do DNA nas células tumorais. Essa ativação tecido-seletiva confere ao Capecitabine um perfil de toxicidade diferenciado em relação ao 5-FU intravenoso contínuo.

GAPPS é uma síndrome hereditária rara causada por mutações pontuais no promotor do gene *APC* (especificamente nos sítios de ligação do fator de transcrição YY1), resultando em polipose adenomatosa extensa da mucosa fúndica gástrica, com risco substancialmente elevado de progressão para adenocarcinoma na região proximal do estômago. Diferentemente do adenocarcinoma gástrico esporádico, o manejo atual de GAPPS é predominantemente cirúrgico — gastrectomia total profilática —, pois os tumores em geral são identificados e ressecados antes da progressão para doença avançada. Nesse contexto, a quimioterapia sistêmica raramente é indicada, e seu papel permanece por definir nesta síndrome específica.

A pontuação elevada atribuída pelo TxGNN (99,94%) reflete provavelmente a similaridade biológica entre GAPPS e outros subtipos de adenocarcinoma gástrico convencional, para os quais o Capecitabine já possui evidências robustas de fase 3 (ex.: ensaios CLASSIC, RESOLVE, SPOTLIGHT). Contudo, essa transferência mecanística não está validada clinicamente para GAPPS: a expressão de TP e TS em tumores derivados de mutação *APC* nesta síndrome é desconhecida, e a eficácia de regimes baseados em fluoropirimidinas nesse contexto hereditário permanece inteiramente hipotética — conforme explicitado no próprio `repurposing_rationale` do Evidence Pack.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (classe Fluoropirimidina — pró-fármaco oral do 5-FU) |
| Risco de Mielossupressão | Médio (neutropenia e trombocitopenia relatadas; menos pronunciada do que com 5-FU intravenoso em infusão contínua) |
| Classificação de Emetogenicidade | Baixa a média (agente oral) |
| Itens de Monitoramento | Hemograma completo com diferencial; função hepática (AST, ALT, bilirrubinas); função renal (creatinina, clearance de creatinina — dosagem requer ajuste se ClCr < 30 mL/min); sinais de eritrodisestesia palmoplantar (síndrome mão-pé) |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de agentes citotóxicos orais |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
GAPPS é uma síndrome hereditária rara cujo tratamento padrão é cirúrgico (gastrectomia total profilática), e não existe qualquer estudo clínico ou publicação avaliando especificamente o papel do Capecitabine nesta condição (Nível de Evidência L5). A alta pontuação do TxGNN deriva da similaridade estrutural com adenocarcinomas gástricos convencionais — nos quais o Capecitabine tem evidências de fase 3 consolidadas —, mas não representa evidência direta para GAPPS.

**Para prosseguir, é necessário:**
- **Registro regulatório**: Obter registro na ANVISA antes de qualquer uso clínico no Brasil
- **Dados de MOA**: Confirmar expressão de TP e TS em tecidos tumorais derivados de mutação *APC* no contexto de GAPPS
- **Estudos pré-clínicos**: Avaliar sensibilidade de modelos celulares GAPPS ao 5-FU/Capecitabine antes de avançar para ensaios clínicos
- **Definição de cenário clínico**: Mapear situações em que GAPPS progride para doença irressecável ou metastática, único contexto em que a quimioterapia sistêmica seria pertinente
- **Informações de segurança**: Revisar bula completa (advertências, contraindicações e interações medicamentosas) via DrugBank ou TFDA antes de qualquer avaliação clínica formal
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

