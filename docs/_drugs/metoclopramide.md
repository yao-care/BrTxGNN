---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Agora vou gerar o relatório de avaliação com base no Evidence Pack fornecido.

---

# Metoclopramide: Do antiemético à úlcera gástrica

## Resumo em Uma Frase

Metoclopramide é um agente antiemético e procinético utilizado no controle de náuseas, vômitos e gastroparesia, atuando como antagonista dopaminérgico (D2) e agonista serotoninérgico (5-HT4).
O modelo TxGNN prevê que pode ser eficaz para **Úlcera Gástrica (Gastric Ulcer Disease)**,
com **2 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiemético / procinético (náuseas, vômitos, gastroparesia) |
| Nova Indicação Prevista | Úlcera Gástrica (Gastric Ulcer Disease) |
| Pontuação de Previsão TxGNN | 99.93% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Metoclopramide é um antagonista dos receptores D2 de dopamina e agonista dos receptores 5-HT4 de serotonina. No trato gastrointestinal, esse duplo mecanismo estimula as contrações do antro gástrico e coordena a abertura do piloro, acelerando o esvaziamento gástrico. É justamente essa ação procinética que fundamenta seu uso estabelecido em gastroparesia diabética, náuseas pós-operatórias e como pré-medicação antiemética em quimioterapia com cisplatina.

A plausibilidade biológica para úlcera gástrica decorre de três mecanismos encadeados: (1) ao acelerar o esvaziamento gástrico, reduz o tempo de contato entre o ácido e a mucosa ulcerada; (2) ao melhorar a coordenação antroduodenal, diminui o refluxo biliar — cofator reconhecido de dano mucoso; e (3) estudos experimentais em ratos e cobaias demonstraram efeito protetor direto contra úlceras induzidas por aspirina e por ligadura pilórica, mecanismo atribuído à melhora da drenagem gástrica, e não à supressão da secreção ácida.

É fundamental contextualizar que metoclopramide não é agente antiácido nem antibacteriano. O tratamento moderno da úlcera gástrica baseia-se na erradicação de *Helicobacter pylori* associada a inibidores de bomba de prótons (IBP), tornando o metoclopramide uma opção potencialmente **adjuvante** — com maior relevância clínica em subpopulações específicas, como pacientes com gastroparesia concomitante ou úlceras refratárias em que o esvaziamento gástrico comprometido perpetua a exposição da mucosa ao ácido.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Desconhecido | 60 | Avalia metoclopramide como pré-medicação em sangramentos digestivos altos (incluindo úlceras hemorrágicas): se reduz necessidade de reendoscopia e melhora a visibilidade das paredes gástricas durante a endoscopia. Desfecho: qualidade de campo endoscópico, não cicatrização de úlcera. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Concluído | 19 | Programa P-DQIP de melhoria de qualidade em prescrição na atenção primária (NHS Escócia): identificação de riscos de farmacoterapia via ferramenta de informática. Sem relação direta com metoclopramide no tratamento de úlcera gástrica. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT | Am J Gastroenterology | Ensaio duplo-cego avaliando eficácia de metoclopramide IV para visualização gástrica em sangramento digestivo alto ativo; maior relevância clínica recente para uso em contexto de úlcera hemorrágica |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | Revisão abrangente de metoclopramide: antagonista dopaminérgico periférico e central; estimula motilidade gástrica, aumenta tônus do esfíncter esofágico inferior e antagoniza vômitos por cisplatina |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Estudo Animal | Arch Int Pharmacodynamie | Metoclopramide (20–50 mg/kg) demonstrou efeito protetor em úlceras gástricas de ratos (modelos aspirina e ligadura pilórica), comparável a ranitidina; mecanismo via procinesia, não antiácido |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Estudo Animal | Indian J Physiol Pharmacol | Efeito protetor contra úlceras gástricas experimentais em cobaias (três modelos distintos) sem alterar secreção ácida; atribuído à melhora da drenagem gástrica e prevenção do refluxo pilórico |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Estudo Animal | J Smooth Muscle Res | Avalia procinéticos (incluindo metoclopramide) no esvaziamento gástrico após úlcera induzida por ácido acético em ratos; demonstra diferenças regionais no efeito conforme localização da úlcera |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Estudo Clínico | Curr Med Res Opin | Investigação do papel do refluxo biliar em úlcera gástrica; avalia efeitos de metoclopramide, tabagismo e carbenoxolona na redução do refluxo como mecanismo protetor |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Estudo Clínico | ZFA | Estudo clínico com titulação dedicada ao uso de metoclopramide no tratamento de úlceras gástrica e duodenal |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Revisão de fármacos no tratamento de úlceras gástrica e duodenal; metoclopramide citado como agente promotor do esvaziamento gástrico com potencial adjuvante |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Clínico (Duplo-cego cruzado) | MMW Münch Med Wochenschr | Estudo em 12 voluntários: metoclopramide e domperidona não alteraram significativamente a gastrina sérica nem a secreção ácida — confirma mecanismo exclusivamente procinético, sem efeito antisecretor |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review Clínica | Postgraduate Medicine | Estratégias terapêuticas para úlceras pépticas refratárias; discute metoclopramide no contexto de gastroparesia associada como opção adjuvante à terapia com H2 bloqueadores |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN é biologicamente plausível e apoiada por estudos animais e revisões históricas; contudo, não existem ensaios clínicos randomizados dedicados ao tratamento primário da úlcera gástrica com metoclopramide, a evidência clínica direta é escassa e datada (décadas de 1970–1990), e o fármaco não possui registros ativos no mercado brasileiro. A ausência completa de dados de segurança no pacote impede qualquer avaliação de risco-benefício.

**Para prosseguir, é necessário:**
- Obter dados de segurança completos (advertências, contraindicações, interações medicamentosas) da bula oficial ou base regulatória
- Confirmar o status regulatório real no Brasil — metoclopramide possui histórico de registro em diversos países; a ausência no banco de dados pode refletir lacuna de consulta, não ausência de fato
- Confirmar o status de conclusão do ensaio [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) (atualmente "UNKNOWN") e obter seus resultados
- Definir subpopulação-alvo com maior benefício potencial (ex.: úlcera gástrica refratária associada a gastroparesia)
- Conduzir revisão sistemática atualizada sobre metoclopramide como terapia adjuvante em úlcera gástrica
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

