---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

O skill de pipeline confirma que este é trabalho TxGNN. Prossigo gerando o relatório baseado no Evidence Pack fornecido.

---

# Ketoprofen: Do alívio da dor e inflamação à displasia acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Ketoprofen é um anti-inflamatório não esteroidal (AINE) da classe dos ácidos propiônicos, amplamente utilizado no tratamento da dor aguda e crônica, artrite reumatoide e osteoartrite.
O modelo TxGNN prevê que pode ser eficaz para **Displasia Acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**, porém atualmente existem **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção.
A previsão é classificada como nível de evidência **L5**, com recomendação de **Hold**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dor e inflamação (AINE — uso convencional baseado em conhecimento farmacológico; sem registro ANVISA no banco de dados) |
| Nova Indicação Prevista | Displasia Acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (sem registros localizados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados de mecanismo de ação (MOA) disponíveis no Evidence Pack. Com base no conhecimento farmacológico estabelecido, o Ketoprofen é um AINE que inibe de forma não seletiva as enzimas COX-1 e COX-2, bloqueando a cascata do ácido araquidônico e reduzindo a síntese de prostaglandinas, tromboxanos e prostaciclinas. Esse mecanismo confere propriedades analgésicas, antipiréticas e anti-inflamatórias.

A displasia acromesomélica tipo Hunter-Thompson é uma doença esquelética genética rara de herança autossômica recessiva, causada por mutações no gene **CDMP1/BMP14** (Cartilage-Derived Morphogenetic Protein 1). A patologia central envolve uma perturbação da via de sinalização BMP (*Bone Morphogenetic Protein*), essencial para o desenvolvimento dos ossos longos dos membros, particularmente os segmentos médios (antebraço e perna). Trata-se de uma anomalia estrutural congênita que se manifesta ao nascimento com encurtamento característico dos membros.

A pontuação TxGNN de 99,98% é elevada, mas a análise mecanicista revela **baixa plausibilidade biológica** para reposicionamento genuíno. A inibição de COX pelo Ketoprofen não tem capacidade de corrigir o defeito de sinalização BMP/CDMP1 subjacente à displasia; no máximo, poderia oferecer alívio sintomático da dor musculoesquelética associada à condição. Este é um cenário de **falso positivo topológico** no grafo de conhecimento: a alta pontuação reflete a conectividade de nós ósseos/esqueléticos no KG, e não uma relação farmacológica real. Vale notar que, entre as 10 previsões geradas, a de maior relevância mecanicista é a **espondiloartropatia (rank 8)**, para a qual os NSAIDs têm evidência robusta (Grau A nas diretrizes ASAS), mas mesmo ali a evidência local específica para Ketoprofen é escassa (apenas 1 revisão indireta).

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Não foram localizados registros ANVISA para o Ketoprofen neste banco de dados. O fármaco consta como não comercializado na fonte consultada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN é enquadrada em **L5** (exclusivamente baseada no modelo, sem estudos reais), e a análise mecanicista aponta para **baixa plausibilidade biológica** — a inibição de COX-1/COX-2 não atua sobre o defeito na via BMP/CDMP1 que é o núcleo patológico da displasia. A ausência completa de ensaios clínicos, literatura específica e dados regulatórios reforça que este par fármaco-doença não reúne condições mínimas para avançar.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA do Ketoprofen via DrugBank (DG002 — severidade Alta)
- Consultar e processar a bula ANVISA para advertências e contraindicações (DG001 — severidade Bloqueante)
- Buscar evidências pré-clínicas ou estudos mecanicistas que conectem inibição de COX à via BMP/CDMP1
- Considerar redirecionar a análise para a **espondiloartropatia (rank 8)**, que apresenta maior plausibilidade mecanicista e alguma evidência indireta na literatura
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

