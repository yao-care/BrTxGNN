---
layout: default
title: Histidine
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Histidine
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

# Histidina: Do suporte nutricional à gastroparesia

## Resumo em Uma Frase

Histidina é um aminoácido essencial utilizado principalmente em formulações de nutrição parenteral e suplementação nutricional clínica.
O modelo TxGNN prevê que pode ser eficaz para **Gastroparesia (Gastroparesis)**,
porém atualmente **não há ensaios clínicos nem publicações** que apoiem diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Aminoácido essencial — nutrição parenteral e suplementação |
| Nova Indicação Prevista | Gastroparesia (Gastroparesis) |
| Pontuação de Previsão TxGNN | 99.55% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) de Histidina disponíveis no DrugBank para esta análise. Com base no conhecimento bioquímico estabelecido, Histidina é um aminoácido essencial que serve como substrato direto da enzima histidina descarboxilase (HDC), sendo convertida em histamina. A histamina, por sua vez, é um mediador fisiológico ativo nos receptores H1 e H2 presentes na musculatura lisa e nas células parietais do trato gastrointestinal.

Na gastroparesia — condição caracterizada por esvaziamento gástrico retardado na ausência de obstrução mecânica — a sinalização via receptores gástricos é farmacologicamente relevante. Antagonistas H2 (como ranitidina e famotidina) são utilizados no manejo de sintomas associados, o que sugere que a via histaminérgica possui papel na fisiologia gástrica. Teoricamente, a modulação desta via por suplementação de histidina poderia influenciar a taxa de esvaziamento gástrico por meio do eixo Histidina → HDC → Histamina → Receptores H1/H2 GI.

Contudo, esta conexão permanece inteiramente teórica e especulativa. Não existe atualmente nenhum estudo clínico, pré-clínico ou de revisão sistemática que tenha investigado diretamente o uso de histidina exógena no tratamento da gastroparesia. O TxGNN provavelmente capturou esta associação por meio de nós intermediários partilhados no grafo de conhecimento, sem respaldo experimental direto para esta indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Histidina em gastroparesia.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Histidina em gastroparesia.

---

## Informações de Comercialização no Brasil

Histidina (DrugBank ID: DB00117) não possui nenhum registro ativo na ANVISA. O fármaco não está comercializado no mercado brasileiro na forma de medicamento registrado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O nível de evidência é L5 — a previsão baseia-se exclusivamente no modelo TxGNN, sem nenhum suporte de estudos clínicos, pré-clínicos ou literatura publicada para a indicação de gastroparesia. Embora o mecanismo proposto (Histidina → Histamina → receptores GI) seja biologicamente plausível, a ausência total de dados experimentais diretos impede qualquer avanço na hierarquia de desenvolvimento.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos (modelos animais de gastroparesia) para verificar se a suplementação de histidina altera a taxa de esvaziamento gástrico
- Revisão sistemática da literatura sobre histamina endógena, HDC e motilidade gástrica
- Obtenção do perfil completo de MOA via DrugBank (lacuna DG002)
- Levantamento das advertências e contraindicações junto à ANVISA/bula disponível (lacuna DG001)
- Avaliação da viabilidade regulatória no Brasil antes de qualquer estudo clínico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

