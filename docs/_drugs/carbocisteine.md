---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Carbocisteine
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

# Carbocisteine: De mucolítico à gota

## Resumo em Uma Frase

Carbocisteine é um agente mucolítico utilizado no manejo de doenças respiratórias com hipersecreção brônquica, atuando na modificação da composição do muco para reduzir sua viscosidade e facilitar a eliminação. O modelo TxGNN prevê que pode ser eficaz para **Gota (Gout)**, com pontuação de previsão de **99,67%**. Contudo, esta indicação conta atualmente com **0 ensaios clínicos** e **0 publicações** de suporte direto.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mucolítico (doenças respiratórias com hipersecreção brônquica) |
| Nova Indicação Prevista | Gota (Gout) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Carbocisteine é classificado farmacologicamente como agente mucolítico. Seu mecanismo de ação envolve a modificação da composição do muco brônquico — inibindo a síntese de sulfomucina e promovendo a secreção de sialomucina —, reduzindo a viscosidade do muco e melhorando a função mucociliar. Como precursor da cisteína, também contribui para a síntese de glutationa e atividade antioxidante celular. Dados detalhados do mecanismo de ação não estão disponíveis na base consultada e precisam ser confirmados via DrugBank.

A gota é causada por hiperuricemia, resultante de distúrbios no metabolismo das purinas. O metabolismo da cisteína — principal via metabólica do Carbocisteine — não possui interseção direta com o metabolismo das purinas. A plausibilidade biológica desta previsão específica é, portanto, **baixa** com base nos dados disponíveis.

Vale notar, porém, que o modelo TxGNN também previu a Síndrome de Lesch-Nyhan para este fármaco (rank 9) — uma doença genética do metabolismo das purinas. Isso sugere que o modelo pode ter capturado uma conexão indireta via eixo "metabolismo cisteína-purinas" no grafo de conhecimento biológico, possivelmente através da hipótese antioxidante: cisteína → glutationa → redução do estresse oxidativo → proteção articular. Esta conexão é altamente especulativa e requer investigação mecanicista básica antes de qualquer consideração clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Carbocisteine em gota.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Carbocisteine em gota.

---

## Informações de Comercialização no Brasil

Carbocisteine não possui registros na base de dados regulatória brasileira consultada. O fármaco não está atualmente comercializado no mercado nacional.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para gota baseia-se exclusivamente no score do modelo (nível L5), sem nenhum suporte de ensaios clínicos, literatura científica ou plausibilidade mecanicista direta bem estabelecida. O Carbocisteine atua no metabolismo da cisteína e na regulação do muco, enquanto a gota envolve o metabolismo das purinas e o depósito de urato — eixos metabólicos distintos com conexão apenas hipotética.

**Para prosseguir, é necessário:**
- Obter dados completos do mecanismo de ação via DrugBank API (DG002 — severidade Alta)
- Obter dados de segurança, advertências e contraindicações da bula TFDA/ANVISA (DG001 — severidade Bloqueante)
- Realizar busca bibliográfica ampliada sobre Carbocisteine e metabolismo de urato ou purinas
- Investigar in vitro a hipótese de proteção antioxidante mediada por glutationa em modelos de gota
- Considerar como indicação prioritária **Bronchite (rank 2, score 98,77%, decisão: Proceed with Guardrails)** — possui plausibilidade mecanicista direta comprovada (inibição de sulfomucina, melhora da clearance mucociliar) e nível de evidência superior (L5/L1★)
---

