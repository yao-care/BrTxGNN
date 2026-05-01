---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

Usando o formato de relatório de reposicionamento para estruturar a avaliação do Evidence Pack de Carbonato de Lítio.

---

# Carbonato de Lítio: Do Transtorno Bipolar à Pseudoacondroplasia

## Resumo em Uma Frase

Carbonato de lítio é um estabilizador de humor clássico, amplamente utilizado no tratamento do transtorno afetivo bipolar em diversas partes do mundo, porém sem registro regulatório no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Pseudoacondroplasia (Pseudoachondroplasia)**, atualmente com **0 ensaios clínicos** e **0 publicações** específicas apoiando esta direção — a previsão apoia-se exclusivamente na análise computacional do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Transtorno afetivo bipolar (uso internacional; sem registro no Brasil) |
| Nova Indicação Prevista | Pseudoacondroplasia (Pseudoachondroplasia) |
| Pontuação de Previsão TxGNN | 99.98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação de DB14509 disponíveis neste pacote de evidências. Segundo o conhecimento farmacológico consolidado, o carbonato de lítio atua principalmente pela **inibição da enzima GSK-3β (Glicogênio Sintase Quinase 3 beta)**, resultando na ativação da via de sinalização **Wnt/β-catenin** — um caminho crítico para a diferenciação e proliferação celular, incluindo condrócitos e osteoblastos.

A pseudoacondroplasia é uma displasia esquelética rara causada por mutações no gene **COMP** (Proteína Oligomérica da Matriz da Cartilagem). Essas mutações provocam o acúmulo intracelular de COMP mal dobrada no retículo endoplasmático dos condrócitos, gerando estresse crônico do ER e morte celular prematura das células cartilaginosas, com consequente nanismo desproporcional. A via Wnt/β-catenin possui papel regulatório demonstrado na diferenciação de condrócitos, o que fornece uma justificativa mecanística **indireta** para a previsão do modelo.

No entanto, a ligação proposta é **altamente indireta**: a ativação de Wnt/β-catenin pelo lítio não possui mecanismo de ação conhecido sobre o acúmulo de proteína COMP mutante — que constitui o problema central da doença. Não há evidências publicadas nem ensaios clínicos relacionando carbonato de lítio à pseudoacondroplasia. A pontuação elevada do TxGNN provavelmente reflete agrupamento de nós de doenças esqueléticas no grafo de conhecimento, e não uma ligação mecanística direta.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Carbonato de lítio (DB14509) não possui nenhum registro ativo na ANVISA e não é comercializado no Brasil.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências resumem-se exclusivamente à previsão computacional do TxGNN (nível L5), sem nenhum ensaio clínico ou publicação científica específica para carbonato de lítio em pseudoacondroplasia. O mecanismo proposto via inibição de GSK-3β não possui ligação direta estabelecida com a patofisiologia primária da doença (acúmulo de COMP mutante e estresse do ER), tornando a hipótese biologicamente especulativa no estágio atual.

**Para prosseguir, é necessário:**
- Confirmar a identidade da entidade química DB14509 versus DB01356 (lítio elementar/íon), pois ambos constam na base DrugBank com perfis farmacológicos distintos — essa ambiguidade é bloqueante para qualquer avaliação subsequente
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API
- Obter informações de segurança, advertências e contraindicações da bula junto à ANVISA ou fontes internacionais (item bloqueante para avaliação clínica)
- Conduzir estudos pré-clínicos em modelos animais de pseudoacondroplasia antes de qualquer consideração clínica
- Verificar a possibilidade de registro ou uso compassivo junto à ANVISA, caso estudos pré-clínicos demonstrem sinal de eficácia
---

